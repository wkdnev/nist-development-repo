# \<System Name\> Security Architecture

## 1 Purpose

This document is used by every control family. \<System Name\> is the whole stack on two Windows Server 2025 VMs on \<Organisation\>'s corporate network. It describes the design on the two VMs. Development and testing run in Docker, apart from production.

## 2 System boundary

**Table 1: System boundary**

| Inside the boundary | Outside the boundary |
| --- | --- |
| Application server VM: Windows Server 2025, UI application, Admin application, API | \<Organisation\>'s corporate network and firewalls |
| Database server VM: Windows Server 2025, PostgreSQL, the \<System Name\> database | Users' devices |
| Accounts, service accounts and configuration on both VMs | \<Organisation\>'s remote access, directory and monitoring services, ServiceNow and the Starters/Leavers system |

![Figure 1: Target design, showing the \<System Name\> boundary on \<Organisation\>'s network with flows F1 to F8](figures/arch-figure-1.png)

**Figure 1: Target design, showing the \<System Name\> boundary on \<Organisation\>'s network with flows F1 to F8**

The figure shows the two VMs inside the \<System Name\> boundary, on \<Organisation\>'s corporate network. Users' devices reach UI application (F1) and Admin application (F2). Both call API (F3, F4), and only API connects to SQL Server on the database VM (F5) and reads groups from Active Directory over LDAPS (F7); browsers sign in through PingFederate (F6), and both VMs reach \<Organisation\>'s time, logging, proxy and backup services (F8).

Users sign in through \<Organisation\>'s PingFederate, with multi-factor authentication, which returns a signed OpenID Connect response that names the person and carries no groups. The API reads the person's group membership from Active Directory over LDAPS. \<System Name\> holds no accounts or passwords of its own.

## 3 Data flows

**Table 2: Data flows**

| Flow | From | To | Purpose | On the VMs |
| --- | --- | --- | --- | --- |
| F1 | User's browser | UI application | Document work | HTTPS |
| F2 | Administrator's browser | Admin application | Administration | HTTPS, only over \<Organisation\>'s managed route (\<Maintenance Management\>, route R3) |
| F3 | UI application | API | Sign-in, notifications, bulk work, reports | HTTPS to API on the VM's loopback address only |
| F4 | Admin application | API | Sign-in, notifications | HTTPS to API on the VM's loopback address only |
| F5 | UI application | PostgreSQL | Documents and projects | Not used: UI application gets its data through API |
| F6 | Admin application | PostgreSQL | Administration data | Not used: Admin application gets its data through API |
| F7 | API | PostgreSQL | All API data | Between VMs, with TLS |
| F8 | User's browser | cdn.jsdelivr.net | Scripts and styles for every page, including sign-in | Not used: \<System Name\> serves these files itself |
| F9 | ServiceNow | System owner and approvers | Access and change approvals | With TLS (\<Assessment, Authorization, and Monitoring Management\>) |
| F10 | Starters/Leavers system | Global administrator | Prompts to add or remove access | With TLS (\<Assessment, Authorization, and Monitoring Management\>) |
| F11 | User's and administrator's browser | \<Organisation\>'s PingFederate | Sign-in with multi-factor authentication; PingFederate returns a signed OpenID Connect response that names the user and carries no groups | HTTPS, on \<Organisation\>'s network |

F9 and F10 are not technical connections to \<System Name\>, and are not shown on Figure 1.

## 4 Inherited from \<Organisation\>

\<Organisation\> holds Cyber Essentials Plus, which supports these claims but does not prove a CSS control. Each needs a named service and evidence from \<Organisation\>.

**Table 3: Services inherited from \<Organisation\>**

| Area | Expected from \<Organisation\> | Evidence |
| --- | --- | --- |
| Network firewalls | Boundary and network protection | \<Evidence Requests\> |
| Remote access | Managed route for remote users and administrators | \<Evidence Requests\> |
| User devices | Build, screen lock, encryption, USB and mobile device controls | \<Evidence Requests\> |
| Wireless | Wireless network controls | \<Evidence Requests\> |
| VM hosting | Hypervisor and physical hardware | \<Evidence Requests\> |
| Boundary services | Proxy, DNS, certificates and denial-of-service protection | EV-SC-01 to 05 |
| Network monitoring | Monitoring of inbound and outbound traffic | EV-SI-01 |
| Second site and telecommunications | A separate site for encrypted backups and rebuilt VMs, with alternate telecommunications | EV-CP-01, EV-CP-02 |
| Hardware maintenance | Hardware and hypervisor maintenance, and support and parts within 24 hours | EV-MA-01 |
| Disks and backup media | Storage, transport and sanitising | EV-MP-01, EV-MP-02 |
| Data centre and offices | Physical access, power, fire, environment and water protection | EV-PE-01 to 05 |
| People processes | Screening, exit interviews, job descriptions and disciplinary action | EV-PS-01 to 03 |
| Enterprise architecture | Standards \<System Name\>'s design must fit | EV-PL-01 |
| Privacy notice | An employee privacy notice that names \<System Name\> | EV-PT-01; \<System Name\>'s pages link to it |
| Contracts and suppliers | Standard contract terms, service descriptions and approved suppliers | EV-SA-01, EV-SA-02, EV-SR-01 |
| Hardware buying and disposal | Inspection, trained buyers, control during repair, and disposal | EV-SR-02 |

## 5 Configuration on the VMs

**Table 4: Configuration on the VMs**

| Item | Target |
| --- | --- |
| Host | Two Windows Server 2025 VMs |
| Traffic | HTTPS and encrypted database connections |
| Secrets | Protected store outside source code, changed every 12 months |
| Database role | One least-privilege role, used only by API |
| Storage | Full-disk encryption on both VMs |
| Malicious code | Microsoft Defender on both VMs, and each upload scanned through AMSI before it is stored (\<System and Information Integrity Management\>, section 3.2) |
| Hardening | CIS Benchmarks for Windows Server 2025 and PostgreSQL |
| Backups | Encrypted daily backups and transaction logs, kept at the second site |
| Retention | Schedule in \<PII Processing Management\>, section 3.7, with periods set by the business owner, and disposal when they end |
| Build and test | Build pipeline and release test gate |

## 6 Security approach

This section states how \<System Name\> is protected, as CSS PL-8 requires. It describes the design on the VMs.

### 6.1 Protection goals

**Table 5: Protection goals**

| Objective | Impact | What it means for \<System Name\> | Main protections |
| --- | --- | --- | --- |
| Confidentiality | Moderate | Restricted documents, including personal data in HR documents, are seen only by people with a role in the project | Project roles, encrypted transport and storage, audit |
| Integrity | Moderate | Documents, their metadata and the audit trail cannot be changed without trace | Edit rights by role, change control, hash-chained audit records |
| Availability | Low (\<System Security Plan\>, section 3.3) | \<System Name\> can be restored after a failure within the times in \<Contingency Planning Management\> | Encrypted backups at the second site, rebuild procedure |

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
| Z2 Administration route | \<Organisation\>'s managed route for administrators | Trusted for administration only | Managed route and administrator sign-in |
| Z3 Application | Application VM: UI application, Admin application and API | Trusted to enforce access | HTTPS on 443 from Z1; the admin portal only from Z2 |
| Z4 Data | Database VM: PostgreSQL and the \<System Name\> database | Most protected | Encrypted database connections from Z3 only (F5 to F7) |
| Z5 Provider services | \<Organisation\>'s directory, monitoring, ServiceNow and Starters/Leavers services | Trusted by agreement and evidence | Outbound from Z3 or by people, as in section 4 |

### 6.4 Layers of defence

**Table 7: Layers of defence**

| Layer | Protection | Main controls |
| --- | --- | --- |
| Boundary | \<Organisation\>'s firewalls allow only HTTPS into Z3, and the admin portal only from Z2 | SC-7, AC-17, MA-4 |
| Transport | TLS on F1 to F7, under NCSC's profiles (\<System and Communications Protection Management\>, section 3.3); data protection key rings protected with DPAPI | SC-8, SC-13 |
| Identity | Each person's own Active Directory account, signed in through PingFederate with multi-factor authentication; roles and project access from AD groups | IA-2, IA-5, AC-7 |
| Authorisation | Project roles checked on every page and API call | AC-3, AC-6 |
| Sign-in lifetime and screen lock | No session management in \<System Name\>. The sign-in is held only in the authentication cookie, which lasts no longer than PingFederate's sign-in lifetime (P-AC-10); an unattended screen is locked by the operating system on \<Organisation\>'s managed devices and the servers (P-AC-15) | AC-11, AC-12, SC-23 |
| Data at rest | Full-disk encryption on both VMs; no plain copies left by exports | SC-28, MP-4 |
| Audit | Hash-chained audit records, reviewed and kept | AU-2, AU-6, AU-9 |
| Host | CIS hardening, Microsoft Defender, patching | CM-6, SI-2, SI-3 |
| Recovery | Encrypted backups and logs at the second site | CP-9, CP-10 |
| People | Rules signed before access, training, screening | PL-4, AT-2, PS-3 |

### 6.5 Engineering principles

\<System Name\>'s security engineering principles are the NCSC secure design principles, and its privacy engineering principles are the CSS privacy engineering objectives (\<System and Services Acquisition Management\>; SA-8). The table shows where the design meets each. Development, implementation and changes are checked against it (\<Procedures\>, PRO-SA-1).

**Table 8: Engineering principles**

| Principle | Where \<System Name\>'s design meets it |
| --- | --- |
| NCSC 1: Establish the context | Boundary, data flows and trust zones (sections 2, 3 and 6.3); information types and impact in \<System Security Plan\>, section 3.3; risks in \<Risk List\> |
| NCSC 2: Make compromise difficult | Deny by default and least privilege (section 6.2); project roles on every request; layered defences (Table 7); trust zones with the admin portal only from Z2 |
| NCSC 3: Make disruption difficult | Separate application and database VMs; recovery times in \<Contingency Planning Management\> |
| NCSC 4: Make compromise detection easier | Hash-chained audit records, weekly review and alerts (\<Audit and Accountability Management\>), detection use cases U1 to U8 (\<System and Information Integrity Management\>, section 3.4); log forwarding to \<Organisation\> |
| NCSC 5: Reduce the impact of compromise | Data separated by project schema; database reachable only from Z3; separate administration route; critical components in \<Risk Assessment Management\>, section 3.9 |
| CSS privacy: Predictability | Purposes and processing rules in \<PII Processing Management\>; privacy notice through \<Organisation\> |
| CSS privacy: Manageability | Requests, corrections and deletions through PRO-PT-1; retention schedule |
| CSS privacy: Disassociability | Access limited by project role; audit free text holds no extra personal data |

### 6.6 Assumptions and dependencies

1. \<Organisation\> provides and evidences the services in section 4. \<System Name\> relies on them but does not describe how they are built.
2. The VMs are built to this design, with the configuration in section 5, before production.
3. Users work only on \<Organisation\>'s managed devices, over its network or managed route.
4. The critical components and their failure effects are in \<Risk Assessment Management\>, section 3.9.

