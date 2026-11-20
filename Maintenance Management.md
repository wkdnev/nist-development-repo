# \<System Name\> Maintenance Management

## 1 Purpose

This document sets out how \<System Name\> is designed to be maintained, to meet the 9 Maintenance (MA) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the principles, who maintains what, how a job is controlled from approval to review, the routes for remote maintenance, the approved tools and people, what may leave and how, the components whose support matters, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.9 (Table 18). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (MA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (MA), and the steps people follow are in \<Procedures\> (MA). Fixing flaws and releasing new versions follow their own designs, in \<System and Information Integrity Management\> and \<Configuration Management\>, and use the same change records.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. Any settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.9 (Table 18).

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
| \<System Name\> set-up and data repair | \[Name\], global administrator | Change record, route R3, PRO-MA-7 | TPL-12 |
| Applications | Developers | Change record and release test, route R4 | TPL-6 |
| The services \<System Name\> depends on: PingFederate, Active Directory, the network and firewall, the time service and the backup store | \<Organisation\> | \<Organisation\>'s own process. It is asked to tell the system owner before work that affects \<System Name\> (EV-MA-01) | \<Organisation\>'s notice |

### 3.3 How a maintenance job is controlled

Controls met here: MA-2, MA-5.

![Figure 1: How a maintenance job is controlled](figures/mam-figure-1.png)

**Figure 1: How a maintenance job is controlled**

**Table 2: Steps of a maintenance job**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 Plan and approve | A change record names the component, the work, who will do it, the tools, the route and any downtime. It is approved before work starts. Emergency work follows the emergency change rule and is recorded within 1 working day | Administrator; the approver under change control (\<Configuration Management\>, section 3.7) | Change record |
| 2 Give notice | Users are told at least 2 working days before planned work that affects them | System owner | Notice |
| 3 Do the work | Only approved people, with approved tools, over an approved route. Anyone else is escorted and supervised | Administrator | Session log, for remote work |
| 4 Check afterwards | The nine checks below | Administrator; the security officer signs within 1 working day | TPL-12 |
| 5 Record | The job is recorded with the fields below | Administrator | TPL-12 |
| 6 Review | Every record is compared with its change record each month. Maintenance with no change record is raised as a security incident | Security officer | TPL-12 |

**The check after maintenance** confirms that: the services answer; anonymous access is refused; sign-in works and is audited; the audit records are intact; the documents are intact; Defender is running; backups still run; the time is right; and the settings are unchanged. The method and the expected result of each are in \<Procedures\>, PRO-MA-1.

**The maintenance record** holds: the date and time; the component; what was done; who did it, their organisation and contact; any escort; whether on site or remote, with the route and session reference; the tools used; parts removed or replaced, with any case or return number; data taken away; the inspection of the tools and the scan of any media; and the check afterwards with its reviewer. Form TPL-12 in \<Record Templates\> has a field for each. Each change to the database schema is also recorded, with its version, date and release. Maintenance records are kept for 3 years. That matches the training records, and covers a full authorisation cycle.

**Routine work** follows the preventive schedule in \<Procedures\>, PRO-MA-6: database upkeep, disk space, updates, certificates, old logs and support dates, each with its owner and how often.

### 3.4 Remote maintenance routes

Controls met here: MA-4.

MA-4 requires every route used for remote maintenance to be documented in the security plan. \<System Security Plan\>, section 3.7, points here. All administration of the servers is remote, as they are at \<Organisation\>'s data centre.

**Table 3: Remote maintenance routes**

| Route | Used by | Tool | Network path | Sign-in | Logged in | How it ends |
| --- | --- | --- | --- | --- | --- | --- |
| R1 Windows administration | Windows server administrator; \<Organisation\>'s engineers | \[Remote desktop or PowerShell remoting\] | \<Organisation\>'s managed route to the servers' management interface (EV-MA-02) | VPN with multi-factor sign-in, then a named Windows account | Windows Security log and \[\<Organisation\>'s route log\] | Sign out and disconnect; temporary accounts disabled |
| R2 Database administration | Database administrator | sqlcmd and SQL Server Management Studio | Route R1 to the database server, then SQL Server locally | As R1, then the administrator's own Windows account with a named SQL Server login, not the application's | SQL Server audit and error logs, and route R1's logs | Close the session and disconnect |
| R3 Admin portal | Global administrator, administrator | Browser | Managed route only, over HTTPS | Sign-in through PingFederate, with multi-factor authentication | \<System Name\> audit log | Close the browser and lock the device. \<System Name\> has no sign-out; the sign-in ends when PingFederate's sign-in lifetime ends (P-AC-10) |
| R4 Application releases | Developers | Release package | No direct route; the Windows server administrator installs the release over R1 | Not applicable | Change record (TPL-6) | Not applicable |
| R5 Hardware and hypervisor | \<Organisation\> | \<Organisation\>'s tools | \<Organisation\>'s internal management network (EV-MA-01) | \<Organisation\>'s controls | \<Organisation\>'s records | \<Organisation\>'s process |

The system owner approves remote work in the change record, which names the route. An administrator watches a supplier's session. For each session the logs must show the start and end time, the account, the source address, the route, and the actions where the tool records them, and the session reference goes on TPL-12. The security officer reviews the logs weekly.

### 3.5 Approved maintenance tools

Controls met here: MA-2, MA-3, MA-3(1), MA-3(2), MA-4.

The Windows server administrator keeps this list and reviews it with the system owner every 12 months, and the system owner approves changes. The list records the version, publisher and file hash of each tool. Before use, each tool's version, publisher and file hash are compared with the list (PRO-MA-3), and the result is recorded on TPL-12.

Microsoft Defender scans any media, and any file copied onto a server for maintenance, before it is used. The servers are virtual, so removable media are used rarely. The scan is recorded on TPL-12.

**Table 4: Approved maintenance tools**

| Tool | Use | Where | Who |
| --- | --- | --- | --- |
| \[Remote desktop or PowerShell remoting\] | Administer the servers | Over route R1 | Windows server administrator |
| Windows built-in tools: Event Viewer, Services, Windows Update, Defender | Diagnose, update and scan | Both servers | Windows server administrator |
| Windows service control | Start, stop and inspect the three application services | Application server | Windows server administrator |
| sqlcmd and SQL Server Management Studio, SQL Server 2022 | Maintain, back up and restore the database | Database server | Database administrator |
| \[Database administration tool, if any\] | \[Use\] | \[Where\] | Database administrator |
| \<System Name\> built-in pages: Database Update, Fresh Start, Legacy Cleanup, Fix Duplicate Users and Seed Project Roles | Schema and data repair | Admin portal | Global administrator, under PRO-MA-7 only |

Not approved on the servers: any shell or package manager carried inside a release, and any tool not in this table.

**The built-in maintenance pages.** Five pages in the admin portal change the database schema or repair data, and can delete data. A page is used only under an approved change record that names it, by a global administrator with the security officer or the system owner present, after a checked backup. Each use is written to the audit log and recorded on TPL-12.

### 3.6 Approved maintenance people

Controls met here: MA-5.

The system owner approves this list. The Windows server administrator checks it when someone leaves, and every 12 months (PRO-MA-5).

Before giving access, the administrator checks that the person is on the list, is screened, has signed Part B of the rules of behaviour, and has a named account. The Windows server administrator or the database administrator escorts and supervises anyone not on the list. A supplier has a temporary account, limited to the job and disabled afterwards, and no access to \<System Name\>'s data.

**Table 5: Approved maintenance people**

| Person or organisation | Role | Maintains | Screened | Part B signed | Account | Escort needed |
| --- | --- | --- | --- | --- | --- | --- |
| \[Name\] | Windows server administrator | Both servers | \[Date\] | \[Date\] | Named Windows administrator account | No |
| \[Name\] | Database administrator | SQL Server 2022 | \[Date\] | \[Date\] | Named SQL Server login | No |
| \[Name\] | Global administrator | Built-in maintenance pages, under PRO-MA-7 | \[Date\] | \[Date\] | Their Active Directory account, in the global administrators group | No, but a second person is present |
| \[Developers\] | Developers | Applications, through releases | \[Date\] | \[Date\] | No access to the servers | Not applicable |
| \<Organisation\>'s engineers, \[names\] | Hardware and hypervisor | The hosts | \<Organisation\>'s screening (EV-MA-01) | Not applicable | \<Organisation\>'s own | Yes, on the \<System Name\> servers |
| \[Supplier\] | \[Role\] | \[As contracted\] | \[Date\] | \[Date\] | Temporary, disabled after the job | Yes |

### 3.7 Equipment and data that leave

Controls met here: MA-2, MA-3(3).

**Table 6: What may leave, and how**

| What | Rule | Approved by | Record |
| --- | --- | --- | --- |
| Hardware or a disk beneath the servers | \<Organisation\> first sanitises it of all \<System Name\> information, including configuration and secrets, by the method in \<Media Protection Management\>, section 3.6, and confirms it with a certificate | System owner, in the change record | TPL-12, TPL-13 |
| Equipment used for maintenance, such as an engineer's laptop or a drive | The administrator checks that it holds no \<System Name\> information. If it does, \<Organisation\> sanitises it by the same method, or it stays at \<Organisation\>'s site | System owner | TPL-12 |
| A copy of data, a database dump, a log or a screenshot, sent for maintenance or support | Kept to the minimum, with personal data removed where possible; encrypted; sent by an approved route; and the receiver confirms deletion when it is no longer needed (PRO-MA-7) | System owner | TPL-12 or TPL-13 |

### 3.8 Security-critical components and support

Controls met here: MA-6.

These are the components that \<System Name\>'s security depends on (MA-06\_ODP\[01\]). Support dates are checked each month against the vendors' published lifecycles. \<Organisation\> provides support and parts for the hardware and the hypervisor within 24 hours of a failure, so that a restore fits the 72-hour recovery time objective. Software is kept on supported versions, and a replacement is planned at least 6 months before support ends. On the servers each application runs as a Windows service.

**Table 7: Security-critical components**

| Component | Version | Support ends | Support or parts within | Who |
| --- | --- | --- | --- | --- |
| Hardware and hypervisor hosts | \[\<Organisation\>\] | \[Per \<Organisation\>'s service agreement\] | 24 hours | \<Organisation\> |
| Windows Server 2025, both servers | 2025 | Mainstream to November 2029; extended to November 2034 | Vendor updates | Windows server administrator |
| Microsoft SQL Server, database server | 2022 | Mainstream to January 2028; extended to January 2033 | Vendor updates | Database administrator |
| .NET and ASP.NET Core runtime | 10.0 | November 2028, long-term support | Vendor updates | Developers |
| Microsoft Defender | \[Version\] | While Windows Server is supported | Vendor updates | Windows server administrator |

### 3.9 What \<Organisation\> provides

Controls met here: MA-2, MA-3(3), MA-4, MA-6.

**Table 8: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Maintenance of the hardware and the hypervisor | MA-2 | Approved, recorded maintenance by screened engineers, with notice to the system owner of work that affects \<System Name\> | EV-MA-01 |
| Sanitising before equipment leaves | MA-2, MA-3(3) | Disks and equipment are sanitised to CSS, with a certificate | EV-MA-01 |
| Support and parts | MA-6 | Within 24 hours of a failure, for the hardware and the hypervisor | EV-MA-01 |
| The managed route administrators use | MA-4 | Multi-factor sign-in; a log of each session; sessions and connections that end when the work does; a firewall rule that limits the admin portal to the route | EV-MA-02 |
| Maintenance of the services \<System Name\> depends on | MA-2 | Notice before work on PingFederate, Active Directory, the network, the time service or the backup store that affects \<System Name\> | EV-MA-01 |

### 3.10 Policy and procedures

Controls met here: MA-1.

1. **Policy.** \<Policy\> (MA) is a system-level policy, shared with everyone who maintains \<System Name\>. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (MA) holds seven procedures, PRO-MA-1 to PRO-MA-7. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control.

## Appendix A MA controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 9 says where.

**Table 9: MA controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| MA-2(2) Automated Maintenance Activities | Maintenance scheduled, done and recorded by automated means | Not required. The maintenance record is a form |
| MA-3(4), MA-3(5) Restricted Tool Use; Execution with Privilege | Tools limited to authorised people, and their privileged use monitored | Not required. Done in part: each tool in section 3.5 is tied to a role, and the built-in pages are limited to global administrators |
| MA-3(6) Software Updates and Patches | Maintenance tools kept up to date | Not required. Done in part: the Windows and SQL Server tools are updated with the servers |
| MA-4(1) Logging and Review | Remote maintenance sessions logged, and the logs reviewed | Not required. Done in design: section 3.4 says what each session logs, and the security officer reviews the logs weekly |
| MA-4(3) Comparable Security and Sanitization | Remote maintenance done only from a system as secure as the one maintained | Not required. Administrators use \<Organisation\>'s managed devices and route (EV-MA-02) |
| MA-4(4) Authentication and Separation of Maintenance Sessions | Maintenance sessions kept apart from other network sessions | Not required. Done in part: the servers are administered through a management interface on \<Organisation\>'s managed route |
| MA-4(5) Approvals and Notifications | Each remote session approved by named people, who are told when it is planned | Not required. Done in design: the system owner approves remote work in the change record |
| MA-4(6), MA-4(7) Cryptographic Protection; Disconnect Verification | Remote sessions encrypted, and their end verified | Not required. Done in part: the VPN and TLS protect the session. The end of a session is not verified separately |
| MA-5(1) Individuals Without Appropriate Access | Rules for maintenance people who lack the access authorisations | Not required. Done in part: they are escorted and supervised, have a temporary account, and have no access to \<System Name\>'s data |
| MA-5(2), MA-5(3), MA-5(4) Security Clearances; Citizenship; Foreign Nationals | Clearance and nationality rules for classified systems | Not required. \<System Name\> holds no classified information |
| MA-5(5) Non-system Maintenance | Rules for people who maintain the building and its services near the system | Not required. \<Organisation\> controls its data centres (\<Physical and Environmental Protection Management\>) |
| MA-6(1), MA-6(2), MA-6(3) Preventive Maintenance; Predictive Maintenance; Automated Support for Predictive Maintenance | Maintenance done before a failure, by schedule or by prediction | Not required. Done in design for preventive work: the schedule in \<Procedures\>, PRO-MA-6. Nothing is predictive |
| MA-7 Field Maintenance | Limits on maintenance done away from a trusted facility | Not required. The servers stay at \<Organisation\>'s data centres |
| MA-2(1), MA-4(2) | Withdrawn by CSS | Not applicable |
