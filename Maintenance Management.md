# \<System Name\> Maintenance Management

## 1 Purpose

This document sets out how \<System Name\> is designed to be maintained, to meet the 9 Maintenance (MA) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the principles, who maintains what, how a job is controlled from approval to review, the routes for remote maintenance, the approved tools and people, what may leave and how, the components whose support matters, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.9 (Table 18). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (MA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (MA), and the steps people follow are in \<Procedures\> (MA). Fixing flaws and releasing new versions follow their own designs, in \<System and Information Integrity Management\> and \<Configuration Management\>, and use the same change records.

## 3 The design

### 3.1 Principles

Controls met here: MA-2, MA-3, MA-5.

1. **Approve first.** No maintenance happens without approval.
2. **Known people, tools and routes.** Only those on the approved lists are used.
3. **Protect data.** Nothing leaves with \<System Name\>'s information on it unless it is approved and protected.
4. **Check and record.** Controls are checked after the work, and every job is recorded and reviewed.

These carry out the principles and rules of \<Policy\>, sections MA.3 and MA.4.

Maintenance means preventive and corrective work, repair and replacement, done on site or remotely. \<System Name\> runs on two virtual servers at \<Organisation\>, so there is no \<System Name\> hardware to repair: \<Organisation\> maintains the hosts beneath them.

### 3.2 Who maintains what

Controls met here: MA-2, MA-5.

**Table 1: Who maintains what**

| Part | Maintained by | Route | Record |
| --- | --- | --- | --- |
| Hardware and hypervisor | \<Organisation\> | \<Organisation\>'s own process (EV-MA-01) | \<Organisation\>'s report |
| Windows Server on both servers | \[Name\], Windows server administrator | Change record, route R1 | TPL-12 |
| SQL Server 2022 | \[Name\], database administrator | Change record, route R2 | TPL-12 |
| \<System Name\> schemas, settings and diagnostics | \[Name\], administrator | Change record, route R3 | TPL-12 |
| Applications, and changes to the database's structure | Developers; the database administrator applies structure changes from the release | Change record and release test, route R4 | TPL-6 |
| The services \<System Name\> depends on: PingFederate, Active Directory, the network and firewall, the time service and the backup store | \<Organisation\> | \<Organisation\>'s own process. It is asked to tell the system owner before work that affects \<System Name\> (EV-MA-01) | \<Organisation\>'s notice |

\<Organisation\>'s engineers maintain the hosts over route R5 and hold no account on the two servers. If one ever needs to work on a server, they work as a supplier does, through an administrator's session (section 3.6). \<System Name\>'s change records and TPL-12 cover the work of \<System Name\>'s own people; \<Organisation\>'s maintenance of the hosts and services is approved, monitored and recorded under its own process, which \<System Name\> inherits (EV-MA-01).

### 3.3 How a maintenance job is controlled

Controls met here: MA-2, MA-5.

![Figure 1: How a maintenance job is controlled](figures/mam-figure-1.png)

**Figure 1: How a maintenance job is controlled**

**Table 2: Steps of a maintenance job**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 Plan and approve | A change record names the component, the work, who will do it, the tools, the route and any downtime. The change control board approves it before work starts (\<Configuration Management\>, sections 3.7 and 3.8). The routine work in the preventive schedule (PRO-MA-6) runs under one standing change: the board approves the schedule, reviews it every 12 months and whenever it changes, and each run cites that change. Emergency work follows the emergency change rule: the system owner or their deputy approves it before it is made, and it is recorded within 1 working day | Administrator; the change control board, or the system owner or deputy in an emergency | Change record |
| 2 Give notice | Users are told at least 2 working days before planned work that affects them | System owner | Notice |
| 3 Do the work | Only approved people, with approved tools, over an approved route. A supplier, or anyone else not on the list, takes part only through an approved administrator's session, which the administrator drives (section 3.6) | Administrator | Session log, for remote work |
| 4 Check afterwards | The checks below | Administrator; the security officer runs the sign-in, audit chain and checksum checks, and signs within 1 working day | TPL-12 |
| 5 Record | The job is recorded with the fields below | Administrator | TPL-12 |
| 6 Review | Every record is compared with its change record each month. Maintenance with no change record is raised as a security incident | Security officer | TPL-12 |

**The check after maintenance** confirms that: the services answer; anonymous access is refused; sign-in works and is recorded; the audit chain is intact; the stored files match their checksums; Defender is running; backups still run; the time is right; the settings are unchanged, with App Control for Business enforced; and nothing the job needed is left behind, such as an added group membership, login or copied tool. The administrator who did the work runs most of them. The security officer runs the sign-in, audit chain and checksum checks, because the administrators hold no application role and nobody but the auditor reads the audit log. The method, who runs it and the expected result of each are in \<Procedures\>, PRO-MA-1.

**The maintenance record** holds: the date and time; the component; what was done; who did it, their organisation and contact; the administrator who drove a supplier's session; whether on site or remote, with the route and session reference; the tools used; parts removed or replaced, with any case or return number; data taken away; the inspection of the tools and the scan of any media; and the check afterwards with its reviewer. Form TPL-12 in \<Record Templates\> has a field for each. Each change to the database's structure is also recorded, with its version and release. Maintenance records are kept for 3 years (\<System Description\>, P-67). That matches the change records and training records, and covers a full authorisation cycle.

**Routine work** follows the preventive schedule in \<Procedures\>, PRO-MA-6: database upkeep, disk space, updates, certificates, keys and secrets, old logs and support dates, each with its owner and how often. The change control board approves the schedule as a standing change (step 1).

### 3.4 Remote maintenance routes

Controls met here: MA-4.

MA-4 requires the tools used for remote maintenance to be allowed only as policy says and documented in the security plan. \<System Security Plan\>, section 3.7, points here for the routes, and section 3.5 lists the tools. CSS counts maintenance over any network, internal or external, as remote (nonlocal), so all administration of the servers is remote: they are at \<Organisation\>'s data centre, and no \<System Name\> role enters it.

**Table 3: Remote maintenance routes**

| Route | Used by | Tool | Network path | Sign-in | Logged in | How it ends |
| --- | --- | --- | --- | --- | --- | --- |
| R1 Windows administration | Windows server administrator; a supplier or \<Organisation\>'s engineer only by watching the administrator's session (section 3.6) | \[Remote desktop or PowerShell remoting\] | From the administrators' managed devices, only over \<Organisation\>'s managed administration route to the servers' management interface (flow F11; EV-MA-02); from outside the office, through the VPN first (P-54) | Multi-factor authentication on the managed administration route, and on the VPN as well from outside the office (P-54); then the administrator's named Windows account | Windows Security log and \[\<Organisation\>'s route log\] | Sign out of Windows rather than only disconnect, so that no session is left open on the server; close the route connection; end any screen sharing |
| R2 Database administration | Database administrator | sqlcmd and SQL Server Management Studio | Route R1 (flow F11) to the database server, then SQL Server locally | As R1; then SQL Server by Windows authentication, with the administrator's own account as a named login, never the API's. SQL Server accepts Windows authentication only | SQL Server Audit and error logs, and route R1's logs | Close the SQL Server session, then end the R1 session as above |
| R3 Admin application | Administrator | Browser | \<Organisation\>'s managed administration route only, over HTTPS (F2); from outside the office, through the VPN first (P-54) | Sign-in through PingFederate, with multi-factor authentication | \<System Name\> audit log | Use Sign out (FR-084) and lock the device. Otherwise the sign-in ends 8 hours after sign-in, never later than PingFederate's sign-in (P-02) |
| R4 Application releases | Developers | Release package | No direct route; the Windows server administrator installs the release over R1 | Not applicable | Change record (TPL-6) | Not applicable |
| R5 Hardware and hypervisor | \<Organisation\> | \<Organisation\>'s tools | \<Organisation\>'s internal management network (EV-MA-01) | \<Organisation\>'s controls | \<Organisation\>'s records | \<Organisation\>'s process |

The change control board approves remote work in the change record, which names the route, or the system owner or deputy in an emergency (section 3.3). Strong authentication (MA-4c) comes from the multi-factor sign-in on the managed administration route, and from PingFederate's on R3: a Windows password alone never opens a session. A supplier never holds a credential: an approved administrator drives the session and the supplier watches and guides over a shared screen (section 3.6). For each session the logs must show the start and end time, the account, the source address, the route, and the actions where the tool records them, and the session reference goes on TPL-12. The security officer reviews the logs weekly.

### 3.5 Approved maintenance tools

Controls met here: MA-2, MA-3, MA-3(1), MA-3(2), MA-4.

MA-3 covers tools used specifically to diagnose and repair \<System Name\>: those on the administrators' managed devices and any tool installed or copied onto a server for maintenance. CSS's guidance leaves out the utilities that are part of the system itself, so the parts of Windows Server and SQL Server in the baseline are listed below for completeness but are controlled as the baseline is, by change control and the drift check (\<Configuration Management\>).

The Windows server administrator keeps this list as part of the approved software list (\<Configuration Management\>, section 3.15), and reviews it with the system owner every 12 months (P-67). The list records the version, publisher and file hash of each tool. A new tool on the servers is added only through a change: the system owner approves the request (PRO-CM-4), and the change that installs it adds it to the App Control for Business policy (PRO-CM-1). App Control then refuses to run any tool on the servers whose publisher or hash does not match its rule, so a modified tool cannot run there. A tool from outside the baseline, such as one on an administrator's managed device or one copied onto a server for a job, has its version, publisher and file hash compared with the list before use (PRO-MA-3), and the result is recorded on TPL-12. A tool found modified is handled as a security incident.

No removable media reach the servers: no USB device is passed through to the VMs (\<Policy\>, section MP.4, R10). Any file or disk image copied onto a server for maintenance is scanned by Microsoft Defender before it is used, the scan is recorded on TPL-12, and the file is removed when the job ends.

**Table 4: Approved maintenance tools**

| Tool | Use | Where | Who |
| --- | --- | --- | --- |
| \[Remote desktop or PowerShell remoting\] | Administer the servers | Over route R1 | Windows server administrator |
| Windows built-in tools: Event Viewer, Services, Windows Update, Defender | Diagnose, update and scan. Part of the baseline | Both servers | Windows server administrator |
| Windows service control | Start, stop and inspect the three application services. Part of the baseline | Application server | Windows server administrator |
| \[Screen-sharing tool\] | Show an administrator's session to a supplier, who can watch but not type (section 3.6) | The administrator's managed device | Windows server or database administrator |
| sqlcmd and SQL Server Management Studio, SQL Server 2022 | Maintain, back up and restore the database | Database server | Database administrator |
| \[Database administration tool, if any\] | \[Use\] | \[Where\] | Database administrator |
| \<System Name\> diagnostics page | Fixed checks that read no item content | Admin application | Administrator |

Not approved on the servers: any shell or package manager carried inside a release, and any tool not in this table. App Control for Business blocks them.

**No maintenance pages.** No page in \<System Name\> changes the database's structure, repairs data in bulk or deletes data outside the normal, audited functions. The Admin application offers only fixed diagnostics that read no item content, and each run is written to the audit log. They are run as part of an approved maintenance job or an incident, whose reference is recorded with the run on TPL-12, and the auditor sees each run in the weekly review. No second person is needed (D-MA-02). A change to the database's structure is a script in a release, applied by the database administrator under an approved change record, after a checked backup. Database maintenance, like any direct query of the database, is done only under an approved change or incident; SQL Server Audit records each read of the item tables by any login other than the API's, and the auditor reviews it weekly (\<Risk List\>, R-AC-01). No second person is needed (D-MA-02). An item's details are corrected, a file replaced or an item deleted only through the application's own functions, each of which is audited.

### 3.6 Approved maintenance people

Controls met here: MA-5.

The system owner approves this list. The Windows server administrator checks it when someone leaves, and every 12 months (P-67; PRO-MA-5).

Before giving access, the administrator checks that the person is on the list, is screened, has signed Part B of the rules of behaviour, and has a named account, granted through the access process in \<Access Control Management\>. Only people on the list work without supervision.

A supplier, \<Organisation\>'s engineer, or anyone else not on the list holds no account on the servers or in \<System Name\>, as temporary and emergency accounts are prohibited (P-39; D-MA-01). They watch and guide over a shared screen while the Windows server administrator or the database administrator, who is on the list and competent in the work, signs in and drives the session, and can end it at once. That administrator is the supervisor MA-5 asks for. The supplier receives no copy of \<System Name\>'s data, apart from a support copy approved under section 3.7. The administrator keeps item content and personal data off the shared screen where the job allows; where it does not, the supplier must be under a contract with UK GDPR Article 28 terms, as for a support copy.

**Table 5: Approved maintenance people**

| Person or organisation | Role | Maintains | Screened | Part B signed | Account | Supervised |
| --- | --- | --- | --- | --- | --- | --- |
| \[Name\] | Windows server administrator | Both servers | \[Date\] | \[Date\] | Named Windows administrator account | No |
| \[Name\] | Database administrator | SQL Server 2022 | \[Date\] | \[Date\] | Named SQL Server login | No |
| \[Name\] | Administrator | Schemas, settings and diagnostics, in the Admin application | \[Date\] | \[Date\] | Their Active Directory account, in the administrators' group | No |
| \[Developers\] | Developers | Applications, through releases | \[Date\] | \[Date\] | No access to the servers | Not applicable |
| \<Organisation\>'s engineers, \[names\] | Hardware and hypervisor | The hosts | \<Organisation\>'s screening (EV-MA-01) | Not applicable | \<Organisation\>'s own, on the hosts only; none on the servers | On the hosts, no; on a server, only through an administrator's session |
| \[Supplier\] | \[Role\] | \[As contracted\] | Not required, as always supervised | Not applicable; bound by the contract's confidentiality terms | None: watches an administrator's shared screen | Yes, always |

### 3.7 Equipment and data that leave

Controls met here: MA-2, MA-3(3).

**Table 6: What may leave, and how**

| What | Rule | Approved by | Record |
| --- | --- | --- | --- |
| Hardware or a disk beneath the servers | The hosts are \<Organisation\>'s and shared, and the servers' disks are encrypted with BitLocker. \<Organisation\>'s own process approves the removal, and \<Organisation\> first sanitises the hardware of all \<System Name\> information, including configuration and secrets, by the method in \<Media Protection Management\>, section 3.6, and confirms it with a certificate. It tells the system owner beforehand where it can, and afterwards in every case, with the certificate (D-MA-03; EV-MA-01) | \<Organisation\>'s data centre, under its own process (MA-02\_ODP\[01\]) | \<Organisation\>'s record; TPL-12 and TPL-13 for the notice and certificate |
| Equipment used for maintenance: the administrators' managed devices, and a supplier's own device | Nothing from \<System Name\> is kept on an administrator's device after the job, apart from an approved support copy; the device stays under \<Organisation\>'s management. A supplier sees a shared screen and receives no copy, so their equipment holds no \<System Name\> information. \<Organisation\>'s engineers' equipment at the data centre follows its own process (EV-MA-01) | System owner, for any copy | TPL-12 |
| A copy of data, a database dump, a log or a screenshot, sent for maintenance or support | Kept to the minimum, with personal data removed where possible; encrypted; sent by an approved route; and the receiver confirms deletion when it is no longer needed (PRO-MA-7). If personal data cannot be removed, the legal adviser agrees first, and the receiver must hold it under a contract with UK GDPR Article 28 terms, in the UK (P-23) | System owner; the legal adviser as well where personal data remains | TPL-12 or TPL-13 |

### 3.8 Security-critical components and support

Controls met here: MA-6.

These are the components that \<System Name\>'s security depends on (MA-06\_ODP\[01\]), taken from the critical components in \<Risk Assessment Management\>, section 3.9. PingFederate and Active Directory are critical too, but are \<Organisation\>'s, and their support is its own. \<Organisation\> provides support and parts for the hardware and the hypervisor within 24 hours of a failure (P-68), so that a restore fits the 72-hour recovery time objective. Support for Microsoft software is obtained through \<Organisation\>'s Microsoft support agreement, under which an administrator raises a case (EV-MA-01); if a component cannot be fixed in time, the server is rebuilt under \<Contingency Planning Management\>. Support dates are checked each month against the vendors' published lifecycles, software is kept on supported versions, and a replacement is planned at least 6 months before support ends (SA-22).

**Table 7: Security-critical components**

| Component | Version | Support ends | Support or parts within | Who |
| --- | --- | --- | --- | --- |
| Hardware and hypervisor hosts | \[\<Organisation\>\] | \[Per \<Organisation\>'s service agreement\] | Support and parts within 24 hours | \<Organisation\> |
| Windows Server 2025, both servers, with BitLocker and App Control for Business | 2025 | \[As Microsoft's published lifecycle states\] | Updates; a support case under \<Organisation\>'s agreement, \[response time, EV-MA-01\] | Windows server administrator |
| Microsoft SQL Server, database server | 2022 | \[As Microsoft's published lifecycle states\] | Updates; a support case as above | Database administrator |
| .NET and ASP.NET Core runtime | 10.0, long-term support | \[As Microsoft's published lifecycle states\] | Updates; a support case as above | Developers |
| Microsoft Defender | \[Version\] | While Windows Server is supported | Updates; a support case as above | Windows server administrator |
| \[Key store, to be chosen\] | \[Version\] | \[As its supplier states\] | \[Supplier's support terms\] | Windows server administrator |

### 3.9 What \<Organisation\> provides

Controls met here: MA-2, MA-3(3), MA-4, MA-6.

**Table 8: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Maintenance of the hardware and the hypervisor | MA-2 | Approved, recorded maintenance by screened engineers, with notice to the system owner of work that affects \<System Name\> | EV-MA-01 |
| Approving and sanitising before host equipment leaves | MA-2, MA-3(3) | Removal approved under \<Organisation\>'s process; disks and equipment sanitised to CSS, with a certificate; the system owner told beforehand where possible and given the certificate (D-MA-03) | EV-MA-01 |
| Support and parts | MA-6 | Within 24 hours of a failure, for the hardware and the hypervisor; a Microsoft support agreement under which \<System Name\>'s administrators can raise a case | EV-MA-01 |
| The managed route administrators use | MA-4 | Multi-factor sign-in; a log of each session; sessions and connections that end when the work does; a firewall rule that limits the Admin application to the route; a screen-sharing tool that lets a supplier watch an administrator's session without control | EV-MA-02 |
| Maintenance of the services \<System Name\> depends on | MA-2 | Notice before work on PingFederate, Active Directory, the network, the time service or the backup store that affects \<System Name\> | EV-MA-01 |

### 3.10 Policy and procedures

Controls met here: MA-1.

\<Policy\> (MA) and \<Procedures\> (MA) meet MA-1. Who they are shared with is in \<Policy\>, section MA.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
