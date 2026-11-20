# \<System Name\> Security Architecture

## 1 Purpose

This document is used by every control family. \<System Name\> is the whole stack on two Windows Server 2025 VMs on \<Organisation\>'s corporate network. This describes the target design; the VMs are not built yet, and development and testing run in Docker.

## 2 System boundary

**Table 1: System boundary**

| Inside the boundary | Outside the boundary |
| --- | --- |
| Application server VM: Windows Server 2025, UI application, Admin application, API | \<Organisation\>'s corporate network and firewalls |
| Database server VM: Windows Server 2025, PostgreSQL, the \<System Name\> database | Users' devices |
| Accounts, service accounts and configuration on both VMs | \<Organisation\>'s remote access, directory and monitoring services, ServiceNow and the Starters/Leavers system |

![Figure 1: Target design, showing the \<System Name\> boundary on \<Organisation\>'s network with flows F1 to F8](figures/arch-figure-1.png)

**Figure 1: Target design, showing the \<System Name\> boundary on \<Organisation\>'s network with flows F1 to F8**

The figure shows the two VMs inside the \<System Name\> boundary, on \<Organisation\>'s corporate network. Users' devices reach UI application (F1) and Admin application (F2). Both call API (F3, F4), and only API connects to SQL Server on the database VM (F5) and reads groups from Active Directory over LDAPS (F7); browsers sign in through PingFederate (F6), and both VMs reach \<Organisation\>'s time, logging, proxy and backup services (F8). That is the target design (D-AC-18). Today the two apps also connect to the database themselves (F5, F6), which is to be removed (PA-10). Browsers also load files from cdn.jsdelivr.net (F8), which is to be removed (PA-34).

Users sign in through \<Organisation\>'s AD FS, with multi-factor authentication (D-AC-23), which returns a signed token carrying their Active Directory groups. \<System Name\> holds no accounts or passwords of its own. The tested build checked its own passwords in API, and UI application and Admin application connected to the database themselves.

## 3 Data flows

**Table 2: Data flows**

| Flow | From | To | Purpose | In Docker today | Target on the VMs |
| --- | --- | --- | --- | --- | --- |
| F1 | User's browser | UI application | Document work | HTTP on localhost | HTTPS, to be set up |
| F2 | Administrator's browser | Admin application | Administration | HTTP on localhost | HTTPS, to be set up; only over \<Organisation\>'s managed route (\<Maintenance Management\>, route R3; PA-83) |
| F3 | UI application | API | Sign-in, sessions, notifications, bulk work, reports | HTTP inside Docker | HTTPS to API on the VM's loopback address only (D-SC-07; PA-18) |
| F4 | Admin application | API | Sign-in, sessions, notifications | HTTP inside Docker | HTTPS to API on the VM's loopback address only (D-SC-07; PA-18) |
| F5 | UI application | PostgreSQL | Documents and projects | Inside Docker | Withdrawn: UI application is to get its data through API (D-AC-18; PA-10) |
| F6 | Admin application | PostgreSQL | Administration data | Inside Docker | Withdrawn: Admin application is to get its data through API (D-AC-18; PA-10) |
| F7 | API | PostgreSQL | All API data | Inside Docker | Between VMs, TLS to be set up |
| F8 | User's browser | cdn.jsdelivr.net | Scripts and styles for every page, including sign-in | HTTPS to an outside service | Remove, by serving these files from \<System Name\> (proposed) |
| F9 | ServiceNow | System owner and approvers | Access and change approvals | Not in use | Planned, with TLS (\<Assessment, Authorization, and Monitoring Management\>) |
| F10 | Starters/Leavers system | Global administrator | Prompts to add or remove access | Not in use | Planned, with TLS (\<Assessment, Authorization, and Monitoring Management\>) |
| F11 | User's and administrator's browser | \<Organisation\>'s AD FS | Sign-in with multi-factor authentication; AD FS returns a signed token with the user's AD groups | Not in the tested build | HTTPS, on \<Organisation\>'s network (D-AC-23) |

One external flow is in use, F8, shown dashed on the diagram because it is to be removed (PA-34). In Docker, the web, admin and API ports are also published on all network interfaces, so the API can be reached directly. The API includes an Azure Blob storage library, but no connection is configured.

F9 and F10 are planned, are not technical connections to \<System Name\> today, and are not shown on Figure 1.

## 4 Inherited from \<Organisation\>

\<Organisation\> holds Cyber Essentials Plus, which supports these claims but does not prove a CSS control. Each needs a named service and evidence from \<Organisation\>.

**Table 3: Services inherited from \<Organisation\>**

| Area | Expected from \<Organisation\> | Evidence |
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
| Enterprise architecture | Standards \<System Name\>'s design must fit | Pending (EV-PL-01) |
| Privacy notice | An employee privacy notice that names \<System Name\> | Pending (EV-PT-01); \<System Name\>'s pages to link to it (PA-90) |
| Contracts and suppliers | Standard contract terms, service descriptions and approved suppliers | Pending (EV-SA-01, EV-SA-02, EV-SR-01) |
| Hardware buying and disposal | Inspection, trained buyers, control during repair, and disposal | Pending (EV-SR-02) |

## 5 Docker compared with the target

**Table 4: Docker compared with the target**

| Item | Docker today | Target |
| --- | --- | --- |
| Host | One PC | Two Windows Server 2025 VMs |
| Traffic | Plain HTTP | HTTPS and encrypted database connections |
| Secrets | A local environment file | Protected store outside source code, changed every 12 months (PA-19) |
| Database role | One superuser | To be decided (PA-10) |
| Storage | Not encrypted | Full-disk encryption on both VMs (PA-52) |
| Malicious code | No scan | Microsoft Defender on both VMs, and each upload scanned through AMSI before it is stored (PA-58; \<System and Information Integrity Management\>, section 3.2) |
| Hardening | None set | CIS Benchmarks for Windows Server 2025 and PostgreSQL (PA-54) |
| Backups | None; data is in Docker named volumes | Encrypted daily backups and transaction logs, kept at the second site (PA-64, PA-66) |
| Retention | None; nothing is disposed of automatically | Schedule drafted in \<PII Processing Management\>, section 3.7; periods set by the business owner (D-PT-21), then disposal (PA-70) |
| Build and test | Built by hand; two test scripts | Build pipeline and release test gate (PA-68) |

## 6 Security approach

This section states how \<System Name\> is protected, as CSS PL-8 requires. It describes the target on the VMs. Where the target is not yet in place, the POA&M item is named.

### 6.1 Protection goals

**Table 5: Protection goals**

| Objective | Impact | What it means for \<System Name\> | Main protections |
| --- | --- | --- | --- |
| Confidentiality | Moderate | Restricted documents, including personal data in HR documents, are seen only by people with a role in the project | Project roles, encrypted transport and storage, audit |
| Integrity | Moderate | Documents, their metadata and the audit trail cannot be changed without trace | Edit rights by role, change control, hash-chained audit records |
| Availability | Low (\<System Security Plan\>, section 3.3; D-RA-07) | \<System Name\> can be restored after a failure within the times in \<Contingency Planning Management\> | Encrypted backups at the second site, rebuild procedure |

### 6.2 Design principles

1. **Deny by default:** nothing is reachable or allowed unless a rule permits it.
2. **Least privilege:** people, services and the database role get only what their task needs.
3. **No trust from network position:** every request is authenticated and authorised, even from inside \<Organisation\>'s network.
4. **Defence in depth:** no single control stands alone; each layer in Table 7 has a fallback.
5. **Fail secure:** an error denies access rather than allowing it.

### 6.3 Trust zones

**Table 6: Trust zones**

| Zone | What is in it | Trust | Entry into the zone |
| --- | --- | --- | --- |
| Z1 Users | Users' managed devices and \<Organisation\>'s corporate network | Not trusted by \<System Name\> | Not applicable |
| Z2 Administration route | \<Organisation\>'s managed route for administrators | Trusted for administration only | Managed route and administrator sign-in (PA-83) |
| Z3 Application | Application VM: UI application, Admin application and API | Trusted to enforce access | HTTPS on 443 from Z1; the admin portal only from Z2 |
| Z4 Data | Database VM: PostgreSQL and the \<System Name\> database | Most protected | Encrypted database connections from Z3 only (F5 to F7) |
| Z5 Provider services | \<Organisation\>'s directory, monitoring, ServiceNow and Starters/Leavers services | Trusted by agreement and evidence | Outbound from Z3 or by people, as in section 4 |

### 6.4 Layers of defence

**Table 7: Layers of defence**

| Layer | Protection | Main controls | State |
| --- | --- | --- | --- |
| Boundary | \<Organisation\>'s firewalls allow only HTTPS into Z3, and the admin portal only from Z2 | SC-7, AC-17, MA-4 | Inherited, not evidenced; admin portal open on every interface in Docker (PA-83) |
| Transport | TLS on F1 to F7, under NCSC's profiles (\<System and Communications Protection Management\>, section 3.3); data protection key rings protected with DPAPI (PA-93) | SC-8, SC-13 | Planned; plain HTTP in Docker (R-AC-05) |
| Identity | Each person's own Active Directory account, signed in through AD FS with multi-factor authentication; roles and project access from AD groups | IA-2, IA-5, AC-7 | As the system owner states (D-AC-23); not yet tested or evidenced (PA-95) |
| Authorisation | Project roles checked on every page and API call | AC-3, AC-6 | In place, with known gaps tracked in the POA&M |
| Session | Page lock after 25 minutes and sign-out after 30 | AC-11, AC-12, SC-23 | In place |
| Data at rest | Full-disk encryption on both VMs; no plain copies left by exports | SC-28, MP-4 | Planned (PA-52); export copies (PA-86) |
| Audit | Hash-chained audit records, reviewed and kept | AU-2, AU-6, AU-9 | In place; chain hash has no key (R-AU-01) |
| Host | CIS hardening, Microsoft Defender, patching | CM-6, SI-2, SI-3 | Planned (PA-54, PA-58) |
| Recovery | Encrypted backups and logs at the second site | CP-9, CP-10 | Planned (PA-64) |
| People | Rules signed before access, training, screening | PL-4, AT-2, PS-3 | Rules approved, none signed yet (NC-PL-03) |

### 6.5 Engineering principles

\<System Name\>'s security engineering principles are the NCSC secure design principles, and its privacy engineering principles are the CSS privacy engineering objectives (\<System and Services Acquisition Management\>; SA-8). The table shows where the design meets each, and the gap where it doesn't. Development, implementation and changes are checked against it from now on (\<Procedures\>, PRO-SA-1).

**Table 8: Engineering principles**

| Principle | Where \<System Name\>'s design meets it | Gap |
| --- | --- | --- |
| NCSC 1: Establish the context | Boundary, data flows and trust zones (sections 2, 3 and 6.3); information types and impact in \<System Security Plan\>, section 3.3; risks in \<Risk List\> | Provider evidence not yet seen (\<Evidence Requests\>) |
| NCSC 2: Make compromise difficult | Deny by default and least privilege (7.2); project roles on every request; layered defences (Table 7); trust zones with the admin portal only from Z2 | TLS (PA-18), AD FS sign-in to be shown working (PA-95), admin portal on every interface in Docker (PA-83) |
| NCSC 3: Make disruption difficult | Separate application and database VMs; recovery times in \<Contingency Planning Management\> | No backups yet (PA-64); no rate limit (PA-50) |
| NCSC 4: Make compromise detection easier | Hash-chained audit records, weekly review and alerts (\<Audit and Accountability Management\>), detection use cases U1 to U8 (\<System and Information Integrity Management\>, section 3.4); log forwarding to \<Organisation\> | Chain hash has no key (R-AU-01), and only 1 of 15 records recomputes (PA-74); no alerts or forwarding yet (PA-59) |
| NCSC 5: Reduce the impact of compromise | Data separated by project schema; database reachable only from Z3; separate administration route; critical components in \<Risk Assessment Management\>, section 3.9 | One database role for all apps (PA-10); committed secrets (PA-19) |
| CSS privacy: Predictability | Purposes and processing rules in \<PII Processing Management\>; privacy notice through \<Organisation\> | Notice not linked at sign-in (PA-90) |
| CSS privacy: Manageability | Requests, corrections and deletions through PRO-PT-1; retention schedule drafted | Corrections not audited and no cross-project search (PA-89); no retention fields (PA-70) |
| CSS privacy: Disassociability | Access limited by project role; audit free text holds no extra personal data (Q04) | Application log repeats personal data (PA-75) |

### 6.6 Assumptions and dependencies

1. \<Organisation\> provides and evidences the services in section 4. \<System Name\> relies on them but does not describe how they are built.
2. The VMs will be built to this design, and the differences in section 5 are closed before production.
3. Users work only on \<Organisation\>'s managed devices, over its network or managed route.
4. The critical components and their failure effects are in \<Risk Assessment Management\>, section 3.9.

## 7 Questions moved out

The two open questions in version \<ver\> are now decisions in \<Decision Register\>, so that this approved design has none open: how the applications run on the application VM (D-PL-10, decided on 13 November 2026: as Windows services), and whether \<Organisation\> runs the hypervisor and it is inside the Cyber Essentials Plus scope (D-PL-11).
