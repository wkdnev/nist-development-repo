# \<System Name\> Maintenance Management

## 1 Purpose

This document shows how \<System Name\> is maintained, for each of the 9 Maintenance (MA) controls and enhancements in the CSS Moderate baseline. Section 3 sets out the design: who maintains what, how a job is controlled from approval to review, the routes for remote maintenance, the approved tools and people, what may leave and how, the components whose support matters, and what \<Organisation\> provides. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define, and appendix B the MA controls CSS does not select at Moderate.

The policy is in \<Policy\> (MA), and the steps people follow are in \<Procedures\> (MA). Fixing flaws and releasing new versions follow their own designs, in \<System and Information Integrity Management\> and \<Configuration Management\>, and use the same change records.

An assessor examines the maintenance records, the lists of approved tools and people, the remote maintenance routes and their session logs; interviews those who maintain the system; and may watch a remote session being set up and ended (CSS). So for each control section 4 gives:

- **each part of the control**, as CSS letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Design and today.** The Design column is how maintenance is meant to work on the two servers at \<Organisation\>. The Today column is what was found in the build labelled v1.0, tested in the test environment on 10 November 2026. No maintenance has taken place on the servers, as they are not built.

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.9 (Table 18). This section gives only the overall position.

No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

Most of this family is a process that has not started, because the servers are not built. Three gaps are in the system itself: maintenance pages built into the admin portal that can change or delete data and write no audit record (PA-31), an admin portal open to every network in the tested build (PA-83), and schema changes that leave no record (PA-84). The rest waits on \<Organisation\>, which maintains the hardware and provides the route administrators use: none of its part is evidenced (PA-120).

## 3 The design

### 3.1 Principles

1. **Approve first.** No maintenance happens without approval.
2. **Known people, tools and routes.** Only those on the approved lists are used.
3. **Protect data.** Nothing leaves with \<System Name\>'s information on it unless it is approved and protected.
4. **Check and record.** Controls are checked after the work, and every job is recorded and reviewed.

These carry out the principles and rules of \<Policy\>, sections MA.3 and MA.4.

Maintenance means preventive and corrective work, repair and replacement, done on site or remotely. \<System Name\> runs on two virtual servers at \<Organisation\>, so there is no \<System Name\> hardware to repair: \<Organisation\> maintains the hosts beneath them.

### 3.2 Who maintains what

**Table 2: Who maintains what**

| Part | Maintained by | Route | Record |
| --- | --- | --- | --- |
| Hardware and hypervisor | \<Organisation\> | \<Organisation\>'s own process (EV-MA-01) | \<Organisation\>'s report |
| Windows Server on both servers | \[Name\], Windows server administrator | Change record, route R1 | TPL-12 |
| PostgreSQL | \[Name\], database administrator | Change record, route R2 | TPL-12 |
| \<System Name\> set-up and data repair | \[Name\], global administrator | Change record, route R3, PRO-MA-7 | TPL-12 |
| Applications | Developers | Change record and release test, route R4 | TPL-6 |
| The services \<System Name\> depends on: AD FS, Active Directory, the network and firewall, the time service and the backup store | \<Organisation\> | \<Organisation\>'s own process. It is asked to tell the system owner before work that affects \<System Name\> (EV-MA-01), as the system owner decided on 17 November 2026 (D-MA-10) | \<Organisation\>'s notice |

### 3.3 How a maintenance job is controlled

![Figure 1: How a maintenance job is controlled](figures/mam-figure-1.png)

**Figure 1: How a maintenance job is controlled**

**Table 3: Steps of a maintenance job**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 Plan and approve | A change record names the component, the work, who will do it, the tools, the route and any downtime. It is approved before work starts. Emergency work follows the emergency change rule and is recorded within 1 working day | Administrator; the approver under change control (\<Configuration Management\>, section 3.7) | Change record |
| 2 Give notice | Users are told at least 2 working days before planned work that affects them | System owner | Notice |
| 3 Do the work | Only approved people, with approved tools, over an approved route. Anyone else is escorted and supervised | Administrator | Session log, for remote work |
| 4 Check afterwards | The nine checks below | Administrator; the security officer signs within 1 working day | TPL-12 |
| 5 Record | The job is recorded with the fields below | Administrator | TPL-12 |
| 6 Review | Every record is compared with its change record each month. Maintenance with no change record is raised as a security incident | Security officer | TPL-12 |

**The check after maintenance** confirms that: the services answer; anonymous access is refused; sign-in works and is audited; the audit records are intact; the documents are intact; Defender is running; backups still run; the time is right; and the settings are unchanged. The method and the expected result of each are in \<Procedures\>, PRO-MA-1.

**The maintenance record** holds: the date and time; the component; what was done; who did it, their organisation and contact; any escort; whether on site or remote, with the route and session reference; the tools used; parts removed or replaced, with any case or return number; data taken away; the inspection of the tools and the scan of any media; and the check afterwards with its reviewer. Form TPL-12 in \<Record Templates\> has a field for each. Maintenance records are kept for 3 years, as the system owner decided on 17 November 2026 (D-MP-11). That matches the training records, and covers a full authorisation cycle.

**Routine work** follows the preventive schedule in \<Procedures\>, PRO-MA-6: database upkeep, disk space, updates, certificates, old logs and support dates, each with its owner and how often.

### 3.4 Remote maintenance routes

MA-4 requires every route used for remote maintenance to be documented in the security plan. \<System Security Plan\>, section 3.7, points here. All administration of the servers is remote, as they are at \<Organisation\>'s data centre.

**Table 4: Remote maintenance routes**

| Route | Used by | Tool | Network path | Sign-in | Logged in | How it ends | State now |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 Windows administration | Windows server administrator; \<Organisation\>'s engineers | \[Remote desktop or PowerShell remoting, to be confirmed\] | \<Organisation\>'s managed route to the servers' management interface | VPN with multi-factor sign-in, then a named Windows account | Windows Security log and \[\<Organisation\>'s route log\] | Sign out and disconnect; temporary accounts disabled | Not evidenced (EV-MA-02) |
| R2 Database administration | Database administrator | psql, pg\_dump and pg\_restore | Route R1 to the database server, then PostgreSQL locally | As R1, then a named PostgreSQL account, not the application's | PostgreSQL log (A30) and route R1's logs | Close the session and disconnect | Planned |
| R3 Admin portal | Global administrator, administrator | Browser | Managed route only, over HTTPS (PA-18) | Sign-in through AD FS, with multi-factor authentication (D-AC-23); the tested build used a password | \<System Name\> audit log; the built-in maintenance pages are not audited (PA-31) | Sign out, which ends the session (M12) | Gap: published on every interface (M04, PA-83) |
| R4 Application releases | Developers | Release package | No direct route; the Windows server administrator installs the release over R1 | Not applicable | Change record (TPL-6) | Not applicable | Planned (PA-53) |
| R5 Hardware and hypervisor | \<Organisation\> | \<Organisation\>'s tools | \<Organisation\>'s internal management network | \<Organisation\>'s controls | \<Organisation\>'s records | \<Organisation\>'s process | Inherited; not evidenced (EV-MA-01) |

For each session the logs must show the start and end time, the account, the source address, the route, and the actions where the tool records them. The security officer reviews them weekly.

### 3.5 Approved maintenance tools

This list is provisional until the servers are built (PA-67). The Windows server administrator keeps it, and the system owner approves changes. When the servers are built, the version, publisher and file hash of each tool are added, so that a tool can be inspected against them before use.

**Table 5: Approved maintenance tools**

| Tool | Use | Where | Who | State now |
| --- | --- | --- | --- | --- |
| \[Remote desktop or PowerShell remoting\] | Administer the servers | Over route R1 | Windows server administrator | Provisional |
| Windows built-in tools: Event Viewer, Services, Windows Update, Defender | Diagnose, update and scan | Both servers | Windows server administrator | Provisional |
| Windows service control | Start, stop and inspect the three application services | Application server | Windows server administrator | Provisional |
| Docker command line | Start, stop and inspect containers | Test environment only | Developers | Approved for the test environment only |
| psql, pg\_dump and pg\_restore, PostgreSQL 18 | Maintain, back up and restore the database | Database server | Database administrator | Provisional |
| \[Database administration tool, if any\] | \[Use\] | \[Where\] | Database administrator | Placeholder |
| \<System Name\> built-in pages: Database Update, Fresh Start, Legacy Cleanup, Fix Duplicate Users and Seed Project Roles | Schema and data repair | Admin portal | Global administrator, under PRO-MA-7 only | Restricted until removed (PA-31) |
| The test scripts | Checks on a test stack | Test environment only | Developers | Approved for the test environment only |

Not approved on the servers: any shell or package manager carried inside a release, as the tested build's container images carry (PA-85), and any tool not in this table.

**The built-in maintenance pages.** The tested build has five pages in the admin portal that change the database schema or repair data. They can delete data, and they write no audit record. The design is that they are removed from production builds and replaced by controlled set-up steps (PA-31). Until then, a page is used only under an approved change record that names it, by a global administrator with the security officer or the system owner present, after a checked backup, and the use is recorded on TPL-12.

### 3.6 Approved maintenance people

This list is provisional until the servers are built (PA-67). The system owner approves it.

**Table 6: Approved maintenance people**

| Person or organisation | Role | Maintains | Screened | Part B signed | Account | Escort needed |
| --- | --- | --- | --- | --- | --- | --- |
| \[Name\] | Windows server administrator | Both servers | \[Date\] | \[Date\] | Named Windows administrator account | No |
| \[Name\] | Database administrator | PostgreSQL | \[Date\] | \[Date\] | Named PostgreSQL account | No |
| \[Name\] | Global administrator | Built-in maintenance pages, under PRO-MA-7 | \[Date\] | \[Date\] | Their Active Directory account, in the global administrators group | No, but a second person is present |
| \[Developers\] | Developers | Applications, through releases | \[Date\] | \[Date\] | No access to the servers | Not applicable |
| \<Organisation\>'s engineers, \[names\] | Hardware and hypervisor | The hosts | \<Organisation\>'s screening (EV-MA-01) | Not applicable | \<Organisation\>'s own | Yes, on the \<System Name\> servers |
| \[Supplier\] | \[Role\] | \[As contracted\] | \[Date\] | \[Date\] | Temporary, disabled after the job | Yes |

### 3.7 Equipment and data that leave

**Table 7: What may leave, and how**

| What | Rule | Approved by | Record |
| --- | --- | --- | --- |
| Hardware or a disk beneath the servers | \<Organisation\> sanitises it first, by the method in \<Media Protection Management\>, section 3.6, and confirms it with a certificate | System owner, in the change record | TPL-12, TPL-13 |
| Equipment used for maintenance, such as an engineer's laptop or a drive | Checked to hold no \<System Name\> information. If it does, it is sanitised, or it stays on site | System owner | TPL-12 |
| A copy of data, a database dump, a log or a screenshot, sent for maintenance or support | Kept to the minimum, with personal data removed where possible; encrypted; sent by an approved route; and the receiver confirms deletion when it is no longer needed | System owner | TPL-12 or TPL-13 |

### 3.8 Security-critical components and support

These are the components that \<System Name\>'s security depends on (MA-06\_ODP\[01\]). Support dates are checked each month against the vendors' published lifecycles. On the servers each application runs as a Windows service (D-PL-10); the tested build ran in containers, so the image base applies to the test environment only, and the container engine is no longer a component of the servers. The system owner confirmed this on 17 November 2026 (D-MA-10).

**Table 8: Security-critical components**

| Component | Version seen | Support ends | Support or parts within | Who |
| --- | --- | --- | --- | --- |
| Hardware and hypervisor hosts | \[\<Organisation\>\] | \[Per \<Organisation\>'s service agreement\] | 24 hours | \<Organisation\> |
| Windows Server 2025, both servers | 2025 | Mainstream to November 2029; extended to November 2034 | Vendor updates | Windows server administrator |
| PostgreSQL | 18.6 (M11) | November 2030 | Community updates | Database administrator |
| .NET and ASP.NET Core runtime | 10.0.14 (M11) | November 2028, long-term support | Vendor updates | Developers |
| Application image base, Ubuntu, in the test environment only | 24.04.5 LTS (M11) | Standard support to May 2029 | Vendor updates | Developers |
| Microsoft Defender | \[Version\] | While Windows Server is supported | Vendor updates | Windows server administrator |

### 3.9 What \<Organisation\> provides

**Table 9: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Maintenance of the hardware and the hypervisor | MA-2 | Approved, recorded maintenance by screened engineers, with notice to the system owner of work that affects \<System Name\> | EV-MA-01 | Not sent |
| Sanitising before equipment leaves | MA-2, MA-3(3) | Disks and equipment are sanitised to CSS, with a certificate | EV-MA-01 | Not sent |
| Support and parts | MA-6 | Within 24 hours of a failure, for the hardware and the hypervisor | EV-MA-01 | Not sent |
| The managed route administrators use | MA-4 | Multi-factor sign-in; a log of each session; sessions and connections that end when the work does; a firewall rule that limits the admin portal to the route | EV-MA-02 | Not sent |
| Maintenance of the services \<System Name\> depends on | MA-2 | Notice before work on AD FS, Active Directory, the network, the time service or the backup store that affects \<System Name\> | EV-MA-01 | Not sent |

**Today:** no request has been sent, and none of this is evidenced (PA-120).

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 MA-1 Policy and Procedures

**Table 10: MA-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A maintenance policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (MA): a system-level policy, shared with everyone who maintains \<System Name\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-MA-01) and legally reviewed on 10 November 2026. The later version awaits the Head of Cyber (D-MA-07). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (MA): seven procedures, PRO-MA-1 to PRO-MA-7. Shared with the same people | Approved by the system owner (D-MA-08). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 10 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 11: MA-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy (\<Policy\>, section MA.4); all seven procedures (\<Procedures\> (MA)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-MA-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-MA-07) |

### 4.2 MA-2 Controlled Maintenance

**Table 12: MA-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Schedule, document and review records of maintenance, repair and replacement, to the maker's specification or the organisation's own requirements | Every job is planned in a change record. Routine work follows the preventive schedule (PRO-MA-6). Each job is recorded on TPL-12, and the security officer reviews every record against its change record each month (section 3.3) | Written. No maintenance has taken place on the servers, which are not built |
| b | Approve and monitor all maintenance, on site or remote, whether the item is serviced in place or taken away | The change is approved before work starts. Emergency work follows the emergency change rule and is recorded within 1 working day. An administrator watches work by anyone not on the approved list, remote sessions are logged (section 3.4), and each use of a built-in maintenance page is audited | Not in use. The built-in maintenance pages write no audit record (M03; PA-31) |
| c | Require defined people to approve the removal of the system or its parts for maintenance, repair or replacement elsewhere | The system owner, in the change record. The servers are virtual: the hardware beneath them is \<Organisation\>'s, and leaves only under its process (section 3.7) | Not yet used |
| d | Sanitise equipment to remove defined information before it leaves | All \<System Name\> information, including configuration and secrets. \<Organisation\> sanitises by the method in \<Media Protection Management\>, section 3.6, and confirms it with a certificate | Not evidenced (EV-MA-01) |
| e | Check that every control the work could have affected still works afterwards | A nine-point checklist (section 3.3). The administrator runs it, and the security officer reviews and signs the result within 1 working day | The first three checks passed in the test environment after a simulated restart (M06 to M08). Not used on the servers |
| f | Include defined information in the maintenance records | The fields in section 3.3, on TPL-12. Each change to the database schema is recorded with its version, date and release | TPL-12 holds the fields. Not yet used. Schema changes leave no record in the database (M09; PA-84) |

**Table 13: MA-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Administrators, security officer, \<Organisation\> |
| Enforced by | Not a system function, apart from the audit of the built-in pages. Change control (\<Configuration Management\>, section 3.7) |
| Rules and procedures | Policy rules R1, R2, R3, R8, R11 (\<Policy\>, section MA.4); PRO-MA-1, PRO-MA-2, PRO-MA-6 (\<Procedures\> (MA)) |
| Tests | Checks M03 and M06 to M09 on the v1.0 build, 10 November 2026: the check after maintenance worked; the built-in pages and schema changes left no record |
| Records an assessor will ask for | Change records and TPL-12 records for a sample of jobs; the monthly review; the preventive schedule; sanitising certificates. None exist yet |
| Status | Not implemented |
| Risk decision | NC-MA-02, rated Low: remediate |
| Open items | PA-120: bring controlled maintenance into use, with \<Organisation\>'s part evidenced. PA-31: the built-in pages. PA-84: record schema changes |

### 4.3 MA-3 Maintenance Tools

**Table 14: MA-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Approve, control and monitor the use of maintenance tools | Only the tools in section 3.5 are used, and the system owner approves each addition. The maintenance pages built into the tested build are removed from production builds. Until they are, each use needs an approved change record and a second person, and is recorded on TPL-12 (PRO-MA-7) | The list is provisional (PA-67). Five built-in pages remain, open to global administrators, and write no audit record (M01, M03; PA-31). The tested build's container images hold a shell and a package manager (M10; PA-85) |
| b | Review the approved tools on a schedule | Every 12 months, by the Windows server administrator with the system owner | The first review is when the servers are built |

**Table 15: MA-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Windows server administrator |
| Enforced by | The approved list; \<System Name\>'s roles, which limit the built-in pages to global administrators |
| Rules and procedures | Policy rules R4, R5 (\<Policy\>, section MA.4); PRO-MA-3, PRO-MA-7 (\<Procedures\> (MA)) |
| Tests | Checks M01, M02 and M10 on the v1.0 build, 10 November 2026 showed the gaps |
| Records an assessor will ask for | The approved tool list and its yearly review; TPL-12 records naming the tools used |
| Status | Not implemented |
| Risk decision | NC-MA-03, rated Low: remediate |
| Open items | PA-67: confirm the list when the servers are built. PA-31: remove the built-in pages. PA-85: releases without a shell or package manager |

### 4.4 MA-3(1) Inspect Tools

**Table 16: MA-3(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Inspect the tools maintenance people use for improper or unauthorised changes | Before use, the version, publisher and file hash of each tool are compared with the approved list (PRO-MA-3), and the result is recorded on TPL-12 | Not in use. The list does not yet give a version, publisher and hash for each tool to be compared with: they are recorded when the servers are built (PA-67) |

**Table 17: MA-3(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Windows server administrator |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R4 (\<Policy\>, section MA.4); PRO-MA-3 (\<Procedures\> (MA)) |
| Tests | None |
| Records an assessor will ask for | The list with each tool's version, publisher and hash; a record of an inspection on TPL-12 |
| Status | Not implemented |
| Risk decision | NC-MA-04, rated Low: approve |
| Open items | PA-120: bring inspection into use. PA-67: record the versions and hashes |

### 4.5 MA-3(2) Inspect Media

**Table 18: MA-3(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Check media that hold diagnostic and test programs for malicious code before they are used | Microsoft Defender scans any media, and any file copied onto a server for maintenance, before it is used. The servers are virtual, so removable media are used rarely. The scan is recorded on TPL-12 | Defender is not yet on the servers (PA-58) |

**Table 19: MA-3(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Windows server administrator |
| Enforced by | Microsoft Defender on both servers |
| Rules and procedures | Policy rule R4 (\<Policy\>, section MA.4); PRO-MA-3 (\<Procedures\> (MA)) |
| Tests | None |
| Records an assessor will ask for | Defender's settings and a scan record |
| Status | Not implemented |
| Risk decision | NC-MA-05, rated Low: obtain evidence |
| Open items | PA-58: Defender on the servers |

### 4.6 MA-3(3) Prevent Unauthorized Removal

**Table 20: MA-3(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Prevent the removal of maintenance equipment holding the organisation's information, by checking that it holds none | Before any equipment used for maintenance leaves, such as an engineer's laptop or a drive, the administrator checks that it holds no \<System Name\> information (section 3.7) | Not yet used |
| b | Or by sanitising or destroying it | If it does, \<Organisation\> sanitises it by the method in \<Media Protection Management\>, section 3.6 | Not yet used; sanitising is not evidenced (EV-MA-01) |
| c | Or by keeping it within the facility | Or it stays at \<Organisation\>'s site | Not yet used |
| d | Or by an exemption from defined people that explicitly allows the removal | Only the system owner may allow equipment or data to leave. That includes any copy of data, database dump, log or screenshot sent for support: kept to the minimum, encrypted, recorded, and deleted when no longer needed (PRO-MA-7) | Not yet used |

**Table 21: MA-3(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rules R8, R9 (\<Policy\>, section MA.4); PRO-MA-2, PRO-MA-7 (\<Procedures\> (MA)) |
| Tests | None |
| Records an assessor will ask for | TPL-12 and TPL-13 records showing each approval and each deletion |
| Status | Not implemented |
| Risk decision | NC-MA-06, rated Low: approve |
| Open items | PA-120: bring removal control into use |

### 4.7 MA-4 Nonlocal Maintenance

**Table 22: MA-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Approve and monitor maintenance and diagnostic work done remotely | The system owner approves remote work in the change record, which names the route. Each session is logged, a supplier's session is watched by an administrator, and the security officer reviews the session logs weekly (section 3.4) | Not in use |
| b | Allow remote maintenance tools only as policy says and as the security plan documents | The five routes in section 3.4 and the tools in section 3.5, which \<System Security Plan\>, section 3.7, points to. The admin portal is reachable only through \<Organisation\>'s managed route | Not met for the admin portal: the tested build publishes it on every network interface (M04; PA-83) |
| c | Use strong authentication to set up remote sessions | Routes R1 and R2: the VPN with multi-factor sign-in, then a named account. Route R3: sign-in through AD FS, with multi-factor authentication (D-AC-23) | \<Organisation\>'s route is not evidenced (EV-MA-02). The tested build's admin portal was password-only (PA-23, PA-95) |
| d | Keep records of remote maintenance and diagnostic work | TPL-12, with the session reference. The logs show the start and end time, the account, the source address, the route, and the actions where the tool records them | Not in use |
| e | End the session and the network connection when the work is finished | The person signs out and disconnects, and any temporary account is disabled. Signing out of the admin portal ends its session | Signing out of the admin portal ended the session in the tested build (M12). \<Organisation\>'s route is not evidenced (EV-MA-02) |

**Table 23: MA-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Administrators, \<Organisation\> |
| Enforced by | \<Organisation\>'s managed route and VPN; AD FS; \<System Name\>'s session |
| Rules and procedures | Policy rules R6, R12 (\<Policy\>, section MA.4); PRO-MA-4 (\<Procedures\> (MA)) |
| Tests | Checks M04, M05 and M12 on the v1.0 build, 10 November 2026: the portal was open to every network and the settings pointed at a public database address; sign-out ended the session |
| Records an assessor will ask for | The route settings and sample session logs (EV-MA-02); change records approving remote work; TPL-12 records with session references |
| Status | Not implemented |
| Risk decision | NC-MA-07, rated Medium: remediate, proposed by the system owner; awaits the authorising official |
| Open items | PA-83: limit the admin portal to the managed route. PA-120: bring remote maintenance into use, with the route evidenced. PA-19, PA-23: secrets and multi-factor sign-in |

### 4.8 MA-5 Maintenance Personnel

**Table 24: MA-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Have a process for authorising maintenance people, and keep a list of the organisations and people authorised | The system owner approves the list in section 3.6. The Windows server administrator checks it when someone leaves, and every 12 months (PRO-MA-5) | The process is approved (D-MA-02). The list is provisional (PA-67) |
| b | Check that people who maintain the system unescorted hold the access authorisations required | Before giving access, the administrator checks that the person is on the list, is screened, has signed Part B of the rules of behaviour, and has a named account | The screening and signing dates are placeholders in section 3.6 |
| c | Name people with the authorisations and the technical skill to supervise those who lack them | The Windows server administrator or the database administrator escorts and supervises anyone not on the list. A supplier has a temporary account, limited to the job and disabled afterwards, and no access to \<System Name\>'s data | Not yet used |

**Table 25: MA-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function. Named accounts on the servers and in PostgreSQL |
| Rules and procedures | Policy rule R7 (\<Policy\>, section MA.4); PRO-MA-5 (\<Procedures\> (MA)) |
| Tests | None |
| Records an assessor will ask for | The approved list with screening and signing dates; a TPL-12 record naming an escort |
| Status | Not implemented |
| Risk decision | NC-MA-08, rated Low: approve |
| Open items | PA-67: confirm the list and fill in the dates when the servers are built |

### 4.9 MA-6 Timely Maintenance

**Table 26: MA-6 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Obtain maintenance support or spare parts for defined components within a defined time of a failure | The components in section 3.8. \<Organisation\> provides support and parts for the hardware and the hypervisor within 24 hours, so that a restore fits the 72-hour recovery time objective. Software is kept on supported versions, with a replacement planned at least 6 months before support ends, and the support dates are checked each month | Not evidenced for the hardware (EV-MA-01). The software versions seen in the tested build are supported (M11) |

**Table 27: MA-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s service agreement; the monthly check of support dates |
| Rules and procedures | Policy rule R10 (\<Policy\>, section MA.4); PRO-MA-6 (\<Procedures\> (MA)) |
| Tests | Check M11 on the v1.0 build, 10 November 2026: supported versions |
| Records an assessor will ask for | \<Organisation\>'s service agreement (EV-MA-01); the monthly check records on TPL-7 |
| Status | Not implemented |
| Risk decision | NC-MA-09, rated Low: obtain evidence |
| Open items | PA-120: obtain \<Organisation\>'s evidence (EV-MA-01) |

## Appendix A Parameter register

These are the CSS organisation-defined values for the 9 MA entries: 15 in total. They were agreed on 6 November 2026 (D-MA-P01), and two were revised on 10 November 2026 (D-MA-P02).

**Table 28: MA parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| MA-01\_ODP\[01\] | Who receives the policy | Everyone who maintains \<System Name\> | Not yet shared (PA-20) |
| MA-01\_ODP\[02\] | Who receives the procedures | Everyone who maintains \<System Name\> | Not yet shared (PA-20) |
| MA-01\_ODP\[03\] | Level of the policy | System level | In place |
| MA-01\_ODP\[04\] | Official who manages them | System owner | In place |
| MA-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review due November 2027 |
| MA-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Reviewed after the MA pack review, 10 November 2026 |
| MA-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review due November 2027 |
| MA-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Reviewed after the MA pack review, 10 November 2026 |
| MA-02\_ODP\[01\] | Who approves removal | System owner | Not yet used |
| MA-02\_ODP\[02\] | Information removed before equipment leaves | All \<System Name\> information, including configuration and secrets | Not yet used; sanitising not evidenced (EV-MA-01) |
| MA-02\_ODP\[03\] | Information in maintenance records | Date and time; component; what was done; who did it, their organisation and contact; any escort; on site or remote, the route and session reference; tools used; parts removed or replaced, with any case or return number; data taken away; the check afterwards and its reviewer | TPL-12 extended (\<Record Templates\> \<ver\>); not yet used |
| MA-03\_ODP | Tool review frequency | Every 12 months | Provisional list in section 3.5; first review at server build (C28) |
| MA-03(03)\_ODP | Who may allow equipment or data to leave | System owner | Not yet used |
| MA-06\_ODP\[01\] | Components supported | The security-critical components in section 3.8 | Table written. The container engine was removed on 17 November 2026, as the applications run as Windows services (D-PL-10, D-MA-10) |
| MA-06\_ODP\[02\] | Time to obtain support and parts | 24 hours for hardware and the hypervisor; software kept on supported versions, with a replacement planned at least 6 months before support ends | Not evidenced (EV-MA-01) |

## Appendix B MA controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 29 says where.

**Table 29: MA controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| MA-2(2) Automated Maintenance Activities | Maintenance scheduled, done and recorded by automated means | Not required. The change records move to ServiceNow when it is set up (PA-53); the maintenance record stays a form |
| MA-3(4), MA-3(5) Restricted Tool Use; Execution with Privilege | Tools limited to authorised people, and their privileged use monitored | Not required. Done in part: each tool in section 3.5 is tied to a role, and the built-in pages are limited to global administrators |
| MA-3(6) Software Updates and Patches | Maintenance tools kept up to date | Not required. Done in part: the Windows and PostgreSQL tools are updated with the servers |
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
