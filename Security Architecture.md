# \<DocuView\> Security Architecture

**\<ref\> | Version \<ver\> | Approved by the system owner**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 System boundary](#3-system-boundary)

[4 Data flows](#4-data-flows)

[5 Inherited from ABC Technologies](#5-inherited-from-abc-technologies)

[6 Docker compared with the target](#6-docker-compared-with-the-target)

[7 Security approach](#7-security-approach)

[8 Questions moved out](#8-questions-moved-out)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Security Architecture |
| Version | \<ver\> |
| Status | Approved by the system owner |
| Date | 5 November 2026 |
| Owner | System owner |
| Applies to | All control families |
| Classification | Restricted |
| Next review | Every 12 months, and after a significant change |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | Neil Ramsbottom | Approved | 7 November 2026 |

### 1.3 Change history

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | No code references: page addresses, setting names, folder paths and file paths are described in plain words, and names of groups, scripts and releases are shown as plain text. No value, finding or decision is changed. Whole-set review: flow F5 and the privacy notice row follow sign-in through AD FS, as \<DocuView\> holds no accounts and has no sign-in page (D-AC-23) |
| \<ver\> | 18 November 2026 | References to the communications protection design point to \<System and Communications Protection Management\>, where it is now held (D-SC-09). References to the integrity design point to \<System and Information Integrity Management\>, where it is now held (D-SI-10) |
| \<ver\> | 18 November 2026 | References to the acquisition design point to \<System and Services Acquisition Management\>, where it is now held (D-SA-19) |
| \<ver\> | 18 November 2026 | References to the risk assessment design point to \<Risk Assessment Management\>, where it is now held (D-RA-11) |
| \<ver\> | 18 November 2026 | References to the personal data design point to \<PII Processing Management\>, where it is now held (D-PT-22) |
| \<ver\> | 17 November 2026 | References to the maintenance design point to \<Maintenance Management\>, where it is now held (D-MA-09) |
| \<ver\> | 13 November 2026 | The applications run as Windows services (D-PL-10) |
| \<ver\> | 12 November 2026 | References to the assessment, authorisation and monitoring design point to \<Assessment, Authorization, and Monitoring Management\>, where it is now held (D-CA-11) |
| \<ver\> | 12 November 2026 | References to the audit design point to \<Audit and Accountability Management\>, where it is now held (D-AU-10) |
| \<ver\> | 12 November 2026 | The boundary figure shows AD FS and flow F11 (D-AC-23) |
| \<ver\> | 12 November 2026 | Sign-in through AD FS added as flow F11, and the identity layer follows D-AC-23 |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change |
| \<ver\> | 12 November 2026 | The boundary figure is redrawn for the target design in which only the API connects to the database (D-AC-18) |
| \<ver\> | 12 November 2026 | Flows F5 and F6 are withdrawn in the target design (D-AC-18). The figure is to be redrawn |
| \<ver\> | 12 November 2026 | The earlier rows of the change history are folded into one row, as the system owner decided (D-GEN-25). No other change |
| \<ver\> | 12 November 2026 | References to the register, the policy and the assessment record follow their new section and table numbers (D-GEN-24) |
| \<ver\> | 12 November 2026 | Documents are cited by name in angle brackets, in place of their numbers, as the system owner asked (D-GEN-23). No other change |
| \<ver\> | 12 November 2026 | Figure 1 restored as an image, with a description (WS-D2). The combined documents are cited by their new numbers and chapters (D-GEN-21). The document standard is cited as \<Documentation Map\>, section 5. The contents list is rebuilt so that its links work in Markdown |
| \<ver\> | 12 November 2026 | Sweep after the SI policy's legal review: malicious code row names AMSI upload scanning; NCSC principle 4 adds the detection use cases and the audit chain result (PA-74). Approved by the system owner |
| \<ver\> to \<ver\> | 5 to 12 November 2026 | The earlier versions. Their history is kept in the change record (\<Documentation Map\>, section 5.1) |

| **SECTION 2** |
| --- |

## 2 Purpose

This document is used by every control family. \<DocuView\> is the whole stack on two Windows Server 2025 VMs on ABC Technologies' corporate network. This describes the target design; the VMs are not built yet, and development and testing run in Docker.

| **SECTION 3** |
| --- |

## 3 System boundary

**Table 4: System boundary**

| Inside the boundary | Outside the boundary |
| --- | --- |
| Application server VM: Windows Server 2025, DV\_Web, DV\_Admin\_UI, DV\_API | ABC Technologies' corporate network and firewalls |
| Database server VM: Windows Server 2025, PostgreSQL, the \<DocuView\> database | Users' devices |
| Accounts, service accounts and configuration on both VMs | ABC's remote access, directory and monitoring services, Jira Service Desk and the Starters/Leavers system |

![Figure 1: Target design, showing the \<DocuView\> boundary on ABC Technologies' network with flows F1 to F8](figures/arch-figure-1.png)

**Figure 1: Target design, showing the \<DocuView\> boundary on ABC Technologies' network with flows F1 to F8**

The figure shows the two VMs inside the \<DocuView\> boundary, on ABC Technologies' corporate network. Users' devices reach DV\_Web (F1) and DV\_Admin\_UI (F2). Both call DV\_API (F3, F4), and only DV\_API connects to PostgreSQL on the database VM (F7). That is the target design (D-AC-18). Today the two apps also connect to the database themselves (F5, F6), which is to be removed (PA-10). Browsers also load files from cdn.jsdelivr.net (F8), which is to be removed (PA-34).

Users sign in through ABC Technologies' AD FS, with multi-factor authentication (D-AC-23), which returns a signed token carrying their Active Directory groups. \<DocuView\> holds no accounts or passwords of its own. The tested build checked its own passwords in DV\_API, and DV\_Web and DV\_Admin\_UI connected to the database themselves.

| **SECTION 4** |
| --- |

## 4 Data flows

**Table 5: Data flows**

| Flow | From | To | Purpose | In Docker today | Target on the VMs |
| --- | --- | --- | --- | --- | --- |
| F1 | User's browser | DV\_Web | Document work | HTTP on localhost | HTTPS, to be set up |
| F2 | Administrator's browser | DV\_Admin\_UI | Administration | HTTP on localhost | HTTPS, to be set up; only over ABC Technologies' managed route (\<Maintenance Management\>, route R3; PA-83) |
| F3 | DV\_Web | DV\_API | Sign-in, sessions, notifications, bulk work, reports | HTTP inside Docker | HTTPS to DV\_API on the VM's loopback address only (D-SC-07; PA-18) |
| F4 | DV\_Admin\_UI | DV\_API | Sign-in, sessions, notifications | HTTP inside Docker | HTTPS to DV\_API on the VM's loopback address only (D-SC-07; PA-18) |
| F5 | DV\_Web | PostgreSQL | Documents and projects | Inside Docker | Withdrawn: DV\_Web is to get its data through DV\_API (D-AC-18; PA-10) |
| F6 | DV\_Admin\_UI | PostgreSQL | Administration data | Inside Docker | Withdrawn: DV\_Admin\_UI is to get its data through DV\_API (D-AC-18; PA-10) |
| F7 | DV\_API | PostgreSQL | All API data | Inside Docker | Between VMs, TLS to be set up |
| F8 | User's browser | cdn.jsdelivr.net | Scripts and styles for every page, including sign-in | HTTPS to an outside service | Remove, by serving these files from \<DocuView\> (proposed) |
| F9 | Jira Service Desk | System owner and approvers | Access and change approvals | Not in use | Planned, with TLS (\<Assessment, Authorization, and Monitoring Management\>) |
| F10 | Starters/Leavers system | Global administrator | Prompts to add or remove access | Not in use | Planned, with TLS (\<Assessment, Authorization, and Monitoring Management\>) |
| F11 | User's and administrator's browser | ABC Technologies' AD FS | Sign-in with multi-factor authentication; AD FS returns a signed token with the user's AD groups | Not in the tested build | HTTPS, on ABC Technologies' network (D-AC-23) |

One external flow is in use, F8, shown dashed on the diagram because it is to be removed (PA-34). In Docker, the web, admin and API ports are also published on all network interfaces, so the API can be reached directly. The API includes an Azure Blob storage library, but no connection is configured.

F9 and F10 are planned, are not technical connections to \<DocuView\> today, and are not shown on Figure 1.

| **SECTION 5** |
| --- |

## 5 Inherited from ABC Technologies

ABC Technologies holds Cyber Essentials Plus, which supports these claims but does not prove a NIST control. Each needs a named service and evidence from ABC.

**Table 6: Services inherited from ABC Technologies**

| Area | Expected from ABC | Evidence |
| --- | --- | --- |
| Network firewalls | Boundary and network protection | Pending |
| Remote access | Managed route for remote users and administrators | Pending |
| User devices | Build, screen lock, encryption, USB and mobile device controls | Pending |
| Wireless | Wireless network controls | Pending |
| VM hosting | Hypervisor and physical hardware | Pending |
| Boundary services | Proxy, DNS, certificates and denial-of-service protection | Pending (EV-SC-01 to 05) |
| Network monitoring | Monitoring of inbound and outbound traffic | Pending (EV-SI-01) |
| Second site and telecommunications | A separate site for encrypted backups and rebuilt VMs, with alternate telecommunications | Pending (EV-CP-01, EV-CP-02) |
| Hardware maintenance | Hardware and hypervisor maintenance, and support and parts within 24 hours (D-MA-P02) | Pending (EV-MA-01) |
| Disks and backup media | Storage, transport and sanitising | Pending (EV-MP-01, EV-MP-02) |
| Data centre and offices | Physical access, power, fire, environment and water protection | Pending (EV-PE-01 to 05) |
| People processes | Screening, exit interviews, job descriptions and disciplinary action | Pending (EV-PS-01 to 03) |
| Enterprise architecture | Standards \<DocuView\>'s design must fit | Pending (EV-PL-01) |
| Privacy notice | An employee privacy notice that names \<DocuView\> | Pending (EV-PT-01); \<DocuView\>'s pages to link to it (PA-90) |
| Contracts and suppliers | Standard contract terms, service descriptions and approved suppliers | Pending (EV-SA-01, EV-SA-02, EV-SR-01) |
| Hardware buying and disposal | Inspection, trained buyers, control during repair, and disposal | Pending (EV-SR-02) |

| **SECTION 6** |
| --- |

## 6 Docker compared with the target

**Table 7: Docker compared with the target**

| Item | Docker today | Target |
| --- | --- | --- |
| Host | One PC | Two Windows Server 2025 VMs |
| Traffic | Plain HTTP | HTTPS and encrypted database connections |
| Secrets | A local environment file | Protected store outside source code, changed every 12 months (PA-19) |
| Database role | One superuser | To be decided (PA-10) |
| Storage | Not encrypted | Full-disk encryption on both VMs (PA-52) |
| Malicious code | No scan | Microsoft Defender on both VMs, and each upload scanned through AMSI before it is stored (PA-58; \<System and Information Integrity Management\>, section 4.2) |
| Hardening | None set | CIS Benchmarks for Windows Server 2025 and PostgreSQL (PA-54) |
| Backups | None; data is in Docker named volumes | Encrypted daily backups and transaction logs, kept at the second site (PA-64, PA-66) |
| Retention | None; nothing is disposed of automatically | Schedule drafted in \<PII Processing Management\>, section 4.7; periods set by the business owner (D-PT-21), then disposal (PA-70) |
| Build and test | Built by hand; two test scripts | Build pipeline and release test gate (PA-68) |

| **SECTION 7** |
| --- |

## 7 Security approach

This section states how \<DocuView\> is protected, as NIST SP 800-53 PL-8 requires. It describes the target on the VMs. Where the target is not yet in place, the POA&M item is named.

### 7.1 Protection goals

**Table 8: Protection goals**

| Objective | Impact | What it means for \<DocuView\> | Main protections |
| --- | --- | --- | --- |
| Confidentiality | Moderate | Restricted documents, including personal data in HR documents, are seen only by people with a role in the project | Project roles, encrypted transport and storage, audit |
| Integrity | Moderate | Documents, their metadata and the audit trail cannot be changed without trace | Edit rights by role, change control, hash-chained audit records |
| Availability | Low (\<System Security Plan\>, section 4.3; D-RA-07) | \<DocuView\> can be restored after a failure within the times in \<Contingency Planning Management\> | Encrypted backups at the second site, rebuild procedure |

### 7.2 Design principles

1. **Deny by default:** nothing is reachable or allowed unless a rule permits it.
2. **Least privilege:** people, services and the database role get only what their task needs.
3. **No trust from network position:** every request is authenticated and authorised, even from inside ABC Technologies' network.
4. **Defence in depth:** no single control stands alone; each layer in Table 10 has a fallback.
5. **Fail secure:** an error denies access rather than allowing it.

### 7.3 Trust zones

**Table 9: Trust zones**

| Zone | What is in it | Trust | Entry into the zone |
| --- | --- | --- | --- |
| Z1 Users | Users' managed devices and ABC Technologies' corporate network | Not trusted by \<DocuView\> | Not applicable |
| Z2 Administration route | ABC Technologies' managed route for administrators | Trusted for administration only | Managed route and administrator sign-in (PA-83) |
| Z3 Application | Application VM: DV\_Web, DV\_Admin\_UI and DV\_API | Trusted to enforce access | HTTPS on 443 from Z1; the admin portal only from Z2 |
| Z4 Data | Database VM: PostgreSQL and the \<DocuView\> database | Most protected | Encrypted database connections from Z3 only (F5 to F7) |
| Z5 Provider services | ABC Technologies' directory, monitoring, Jira and Starters/Leavers services | Trusted by agreement and evidence | Outbound from Z3 or by people, as in section 5 |

### 7.4 Layers of defence

**Table 10: Layers of defence**

| Layer | Protection | Main controls | State |
| --- | --- | --- | --- |
| Boundary | ABC Technologies' firewalls allow only HTTPS into Z3, and the admin portal only from Z2 | SC-7, AC-17, MA-4 | Inherited, not evidenced; admin portal open on every interface in Docker (PA-83) |
| Transport | TLS on F1 to F7, under NCSC's profiles (\<System and Communications Protection Management\>, section 4.3); data protection key rings protected with DPAPI (PA-93) | SC-8, SC-13 | Planned; plain HTTP in Docker (R-AC-05) |
| Identity | Each person's own Active Directory account, signed in through AD FS with multi-factor authentication; roles and project access from AD groups | IA-2, IA-5, AC-7 | As the system owner states (D-AC-23); not yet tested or evidenced (PA-95) |
| Authorisation | Project roles checked on every page and API call | AC-3, AC-6 | In place, with known gaps tracked in the POA&M |
| Session | Page lock after 25 minutes and sign-out after 30 | AC-11, AC-12, SC-23 | In place |
| Data at rest | Full-disk encryption on both VMs; no plain copies left by exports | SC-28, MP-4 | Planned (PA-52); export copies (PA-86) |
| Audit | Hash-chained audit records, reviewed and kept | AU-2, AU-6, AU-9 | In place; chain hash has no key (R-AU-01) |
| Host | CIS hardening, Microsoft Defender, patching | CM-6, SI-2, SI-3 | Planned (PA-54, PA-58) |
| Recovery | Encrypted backups and logs at the second site | CP-9, CP-10 | Planned (PA-64) |
| People | Rules signed before access, training, screening | PL-4, AT-2, PS-3 | Rules approved, none signed yet (NC-PL-03) |

### 7.5 Engineering principles

\<DocuView\>'s security engineering principles are the NCSC secure design principles, and its privacy engineering principles are NIST's privacy engineering objectives (\<System and Services Acquisition Management\>; SA-8). The table shows where the design meets each, and the gap where it doesn't. Development, implementation and changes are checked against it from now on (\<Procedures\>, PRO-SA-1).

**Table 11: Engineering principles**

| Principle | Where \<DocuView\>'s design meets it | Gap |
| --- | --- | --- |
| NCSC 1: Establish the context | Boundary, data flows and trust zones (sections 3, 4 and 7.3); information types and impact in \<System Security Plan\>, section 4.3; risks in \<Risk List\> | Provider evidence not yet seen (\<Evidence Requests\>) |
| NCSC 2: Make compromise difficult | Deny by default and least privilege (7.2); project roles on every request; layered defences (Table 10); trust zones with the admin portal only from Z2 | TLS (PA-18), AD FS sign-in to be shown working (PA-95), admin portal on every interface in Docker (PA-83) |
| NCSC 3: Make disruption difficult | Separate application and database VMs; recovery times in \<Contingency Planning Management\> | No backups yet (PA-64); no rate limit (PA-50) |
| NCSC 4: Make compromise detection easier | Hash-chained audit records, weekly review and alerts (\<Audit and Accountability Management\>), detection use cases U1 to U8 (\<System and Information Integrity Management\>, section 4.4); log forwarding to ABC Technologies | Chain hash has no key (R-AU-01), and only 1 of 15 records recomputes (PA-74); no alerts or forwarding yet (PA-59) |
| NCSC 5: Reduce the impact of compromise | Data separated by project schema; database reachable only from Z3; separate administration route; critical components in \<Risk Assessment Management\>, section 4.9 | One database role for all apps (PA-10); committed secrets (PA-19) |
| NIST privacy: Predictability | Purposes and processing rules in \<PII Processing Management\>; privacy notice through ABC Technologies | Notice not linked at sign-in (PA-90) |
| NIST privacy: Manageability | Requests, corrections and deletions through PRO-PT-1; retention schedule drafted | Corrections not audited and no cross-project search (PA-89); no retention fields (PA-70) |
| NIST privacy: Disassociability | Access limited by project role; audit free text holds no extra personal data (Q04) | Application log repeats personal data (PA-75) |

### 7.6 Assumptions and dependencies

1. ABC Technologies provides and evidences the services in section 5. \<DocuView\> relies on them but does not describe how they are built.
2. The VMs will be built to this design, and the differences in section 6 are closed before production.
3. Users work only on ABC Technologies' managed devices, over its network or managed route.
4. The critical components and their failure effects are in \<Risk Assessment Management\>, section 4.9.

| **SECTION 8** |
| --- |

## 8 Questions moved out

The two open questions in version \<ver\> are now decisions in \<Decision Register\>, so that this approved design has none open: how the applications run on the application VM (D-PL-10, decided on 13 November 2026: as Windows services), and whether ABC Technologies runs the hypervisor and it is inside the Cyber Essentials Plus scope (D-PL-11).
