# \<System Name\> Concept of Operations

**\<ref\> | Version \<ver\> | Approved by the system owner**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose of this document](#2-purpose-of-this-document)

[3 Mission and purpose](#3-mission-and-purpose)

[4 User communities](#4-user-communities)

[5 Business workflows](#5-business-workflows)

[6 Operational scenarios](#6-operational-scenarios)

[7 Operational concepts](#7-operational-concepts)

[8 Open questions](#8-open-questions)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<System Name\> Concept of Operations |
| Version | \<ver\> |
| Status | Approved by the system owner |
| Date | 5 November 2026 |
| Owner | System owner |
| Applies to | All control families |
| Classification | Restricted |
| Next review | 12 months after approval, and after a significant change |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | \[Name\] | Approved | 7 November 2026 |
| Business owner | \[Name\] | Approved | 7 November 2026 |

### 1.3 Change history

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | Whole-set review: who starts a new person, where \<System Name\> runs and the database-down mode follow sign-in through AD FS and the Windows services (D-AC-23, D-PL-10) |
| \<ver\> | 18 November 2026 | Whole-set review: the joiner and leaver workflows follow sign-in through AD FS and access by Active Directory groups (D-AC-23) |
| \<ver\> | 18 November 2026 | References to the communications protection design point to \<System and Communications Protection Management\>, where it is now held (D-SC-09). References to the integrity design point to \<System and Information Integrity Management\>, where it is now held (D-SI-10) |
| \<ver\> | 18 November 2026 | References to the acquisition design point to \<System and Services Acquisition Management\>, where it is now held (D-SA-19) |
| \<ver\> | 18 November 2026 | References to the risk assessment design point to \<Risk Assessment Management\>, where it is now held (D-RA-11) |
| \<ver\> | 17 November 2026 | References to the personnel security design point to \<Personnel Security Management\>, where it is now held (D-PS-10) |
| \<ver\> | 17 November 2026 | References to the physical and environmental protection design point to \<Physical and Environmental Protection Management\>, where it is now held (D-PE-11) |
| \<ver\> | 17 November 2026 | References to the media protection design point to \<Media Protection Management\>, where it is now held (D-MP-09) |
| \<ver\> | 17 November 2026 | References to the maintenance design point to \<Maintenance Management\>, where it is now held (D-MA-09) |
| \<ver\> | 16 November 2026 | The modes of operation follow sign-in through AD FS: a row for AD FS being down (D-AC-23) |
| \<ver\> | 12 November 2026 | References to the assessment, authorisation and monitoring design point to \<Assessment, Authorization, and Monitoring Management\>, where it is now held (D-CA-11) |
| \<ver\> | 12 November 2026 | References to the training design point to \<Awareness and Training Management\>, where it is now held (D-AT-09) |
| \<ver\> | 12 November 2026 | Sign-in follows D-AC-23: single sign-on through AD FS |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change |
| \<ver\> | 12 November 2026 | The access request steps follow D-AC-22 |
| \<ver\> | 12 November 2026 | References to documents that no longer exist now name where their content is, as the system owner asked. No other change |
| \<ver\> | 12 November 2026 | Section 7.4 is cut to a brief table that points to where each value is held, in place of repeating the values (D-GEN-25). No value is changed. The earlier rows of the change history are folded into one row, as the system owner decided (D-GEN-25). No other change |
| \<ver\> | 12 November 2026 | References to the register, the policy and the assessment record follow their new section and table numbers (D-GEN-24) |
| \<ver\> | 12 November 2026 | Documents are cited by name in angle brackets, in place of their numbers, as the system owner asked (D-GEN-23). No other change |
| \<ver\> | 12 November 2026 | Whole-set review (WS-F15): the business owner is named, and the business facts still needed are shown as placeholders for the business owner; section 7.4 is one numbered list; the 1-hour limit for a higher-risk leaver is stated (D-PS-07). The combined documents are cited by their new numbers. The document standard is cited as \<Documentation Map\>, section 5. The contents list is rebuilt so that its links work in Markdown |
| \<ver\> | 12 November 2026 | AT pack review (D-AT-06): the training item names the \<System Name\> briefing, the role modules and \<Control Implementation Register\> (AT). Approved by the system owner |
| \<ver\> to \<ver\> | 5 to 12 November 2026 | The earlier versions. Their history is kept in the change record (\<Documentation Map\>, section 5.1) |

| **SECTION 2** |
| --- |

## 2 Purpose of this document

This document is used by every control family. It describes how \<System Name\> is intended to be used: why it exists, who uses it, the business processes it supports and how it works day to day. How it meets controls is in the SSP. The business details are proposals until the business owner confirms them.

| **SECTION 3** |
| --- |

## 3 Mission and purpose

\<System Name\> gives authorised people one place to find and read scanned and electronic documents, such as PDFs and TIFFs. Each project's documents are kept separate from the others.

Teams need one controlled place to keep scanned and electronic documents, so that the right people can find them quickly and others cannot see them. Keeping each project's documents separate lets one system serve several parts of the business.

The business and information owner is \[Name\] (\<Roles and Responsibilities\>). The benefits the business expects are still to be stated: \[Benefits expected, from the business owner\].

| **SECTION 4** |
| --- |

## 4 User communities

**Table 4: User communities**

| Community | What they do | Where |
| --- | --- | --- |
| Document readers | Search and read documents in their projects, and report bad files | UI application |
| Project editors | Readers' work, plus upload, bulk upload, bulk export and manage project documents | UI application |
| Administrators | Manage system settings | Admin portal |
| Global administrators | Manage projects, the AD groups each project uses, and sessions, in every project | Admin portal and UI application |
| Auditors | Read audit logs | Admin portal |
| Security officers | Monitor security information | Admin portal |

| **SECTION 5** |
| --- |

## 5 Business workflows

A document normally moves through four stages: it is added to a project, found and read, corrected if something is wrong, and exported if it is needed elsewhere. The business processes \<System Name\> will support are still to be confirmed: \[Business processes, from the business owner\]. The sample data uses invoices, correspondence and HR projects.

**Table 5: Business workflows**

| Activity | Who | What happens |
| --- | --- | --- |
| Find and read a document | Reader | Chooses a project, searches by title, author, number or date, and opens the document on screen |
| Add documents | Editor | Uploads files one at a time or in bulk, with details such as title and author |
| Report a bad file | Reader, editor | Flags a corrupt or wrong document so it can be corrected |
| Export a project's documents | Editor | Downloads a set of documents for approved use elsewhere |
| Start a new person | The person, their line manager, the group's owner | The person requests access, their line manager approves it and the owner authorises it, then the owner adds the person to the project's or role's Active Directory group. \<System Name\> creates no account (D-AC-23) |
| Remove a leaver | \<Organisation\>, the group owners | \<Organisation\> disables the person's Active Directory account at once, which ends their access, and the group owners remove their group memberships within 5 working days |
| Check activity | Auditor | Reviews who did what |

| **SECTION 6** |
| --- |

## 6 Operational scenarios

**Table 6: Operational scenarios**

| Scenario | Situation | What happens |
| --- | --- | --- |
| Answering a query | A reader needs a past document | They sign in, choose their project, search and read it on screen |
| Adding a batch | An editor has a set of newly scanned documents | They bulk upload them to the project with their details, and readers can then find them |
| A poor scan | A reader finds a page is unreadable | They report a bad file, and an editor corrects it and updates the report |
| A request for documents | Someone needs a project's documents elsewhere | The project access approver decides, and an editor exports them as a download |
| Wrong project | A user opens a project they are not approved for | \<System Name\> refuses, and they request access, which their line manager approves and the project's owner authorises |
| Forgotten password or lockout | A user cannot sign in | \<Organisation\>'s IT service desk resets the Active Directory password or releases the lock, after checking who they are |
| Leaving a desk | A user walks away while signed in | The screen locks after 25 minutes idle, and the session ends after 30 |
| A new starter or a leaver | Staff change | Access is requested and approved for a starter, and removed for a leaver |

| **SECTION 7** |
| --- |

## 7 Operational concepts

### 7.1 Where it runs

It is not in production. It will run on the corporate network of \<Organisation\>, on an application server VM and a separate database server VM, both Windows Server 2025, with each application running as a Windows service (D-PL-10). The current development stack runs in Docker on one PC with sample data.

### 7.2 How access works day to day

1. A person signs in through \<Organisation\>'s single sign-on, AD FS, with multi-factor authentication (D-AC-23). \<System Name\> has no password of its own.
2. \<System Name\> takes their roles and project access from their Active Directory groups.
3. Their group memberships decide which projects they see. Each project names a read group and an edit group.
4. An idle session locks on screen at 25 minutes and ends at 30. Every session ends after 8 hours.

### 7.3 Modes of operation

**Table 7: Modes of operation**

| Mode | What happens |
| --- | --- |
| Normal | Everyone can work as usual |
| AD FS down | Nobody can sign in, because \<Organisation\>'s AD FS authenticates every user. People already signed in carry on until their session ends |
| API down | Nobody can work, because both apps reach the documents only through API |
| Database down | Session checks fail, so users are signed out, and nobody can open a document |
| Maintenance | Users cannot reach \<System Name\>; there is no notice page explaining why. Users get 2 working days' notice of planned maintenance, and a maintenance page is recommended (REC-53) |

These modes come from reading the design. They have not been exercised.

### 7.4 How it is kept secure in operation

None of this has started, as \<System Name\> is not live. Table 8 says in brief how each part of operation is kept secure. The time limits, frequencies and other values are held only in the document named, so that they cannot fall out of step.

**Table 8: Keeping \<System Name\> secure in operation**

| Activity | In brief | Held in |
| --- | --- | --- |
| Changes | Approved by the change control board, after a security impact analysis and a review by a second developer. The running system is checked against the approved baseline | \<Configuration Management\> |
| Patches and vulnerabilities | The system is scanned regularly, and flaws are fixed within time limits set by their severity | \<Risk Assessment Management\>, section 4.6 |
| Malicious code and monitoring | Microsoft Defender runs on both VMs and uploads are scanned. Audit records and logs are reviewed, and detection use cases alert the security officer | \<System and Information Integrity Management\>, section 4.4; \<Security Operating Procedures\>, section 5 |
| Encryption | TLS on every flow, encrypted disks and backups, and a register of keys. Not yet built (PA-18, PA-52, PA-93) | \<System and Communications Protection Management\> |
| Backups and recovery | Encrypted backups, tested restores, and recovery within the objectives the business has set | \<Contingency Planning Management\> |
| Incidents and breaches | Reported to the security officer and handled by severity. The legal adviser decides whether to tell the ICO and the people affected | \<Incident Response Management\> |
| Training | Security training and a \<System Name\> briefing before access, repeated on a schedule, with role modules for those with special duties | \<Awareness and Training Management\> |
| Maintenance | Approved first, done by known people with approved tools, checked afterwards and recorded | \<Maintenance Management\> |
| Media and paper | Exports, downloads and printouts are limited, marked and removed. \<Organisation\> looks after disks and backup media | \<Media Protection Management\>; \<Security Operating Procedures\>, Part A |
| Buildings | \<Organisation\> protects the data centre and the second site, and its evidence is checked | \<Physical and Environmental Protection Management\> |
| People | Screened before access, bound by signed rules, and their access changed promptly when they move or leave | \<Personnel Security Management\>, section 4.6 |
| Personal data | Used only for HR administration and managing project documents. Requests and complaints go to the legal adviser, and the impact assessment is completed before production | \<Privacy Plan\>; \<Data Protection Impact Assessment\> |
| Building and buying | Changes follow the development lifecycle. Suppliers are approved, and packages are to arrive through the offline feed (PA-94) | \<System and Services Acquisition Management\>; \<Supply Chain Risk Management\> |
| Risk and authorisation | The risk list and plan of action are kept current, and the authorising official is kept informed. Authorisation is decided from the authorisation package | \<Assessment, Authorization, and Monitoring Management\>, section 4.5; \<Security Assessment Report\> |

\<System Name\> is not authorised. No production documents are held until multi-factor authentication through AD FS is shown working (PA-95), or the acceptance of password-only sign-in ends on 6 May 2027.

| **SECTION 8** |
| --- |

## 8 Open questions

1. Which \<Organisation\> staff will use \<System Name\>, and from where? Still open: \[Teams and locations, from the business owner\].
2. Answered: \[Name\], as project access approver, decides who may read each project.
3. Which business processes will \<System Name\> support, and what are the expected benefits? Still open: see sections 3 and 5.
4. What hours must it be available, and how many users and documents are expected? Still open: \[Hours, and numbers of users and documents, from the business owner\].
