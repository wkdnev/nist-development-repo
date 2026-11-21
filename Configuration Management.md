# \<System Name\> Configuration Management

## 1 Purpose

This document sets out how \<System Name\>'s configuration is recorded, controlled and changed to meet the 24 Configuration Management (CM) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: roles and processes, the configuration items, the baseline, the software components and licences, the secure settings, change control and the change control board, impact analysis, least functionality, who may change what, the inventory and where information is held, the library, what \<Organisation\> provides, approved software, devices for travel, and the policy, procedures and this plan. Each subsection names the controls it helps to meet. This document is also the Configuration Management Plan that CM-9 requires, and follows the outline in CSS, Appendix D. Appendix A sets out the development, test and production environments, and Appendix B lists the CM controls CSS does not select at Moderate.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.5 (Table 14). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (CM). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (CM), and the steps people follow are in \<Procedures\> (CM).

## 3 The design

### 3.1 Principles

Controls met here: CM-2, CM-3, CM-6, CM-7, CM-8, CM-8(3).

1. **Known baseline.** The approved configuration is recorded and versioned, so that any release can be rebuilt exactly.
2. **Controlled change.** No change happens without an impact analysis, approval and testing.
3. **Least functionality.** Anything \<System Name\> does not need is turned off or left out.
4. **Accurate inventory.** Every component is recorded, and an unauthorised one is detected.
5. **Secure settings at every layer.** Windows Server 2025, SQL Server 2022, the hosting, the runtime and the applications each follow a named standard.
6. **Nothing drifts unseen.** The running system is compared with the baseline monthly and at each release (P-29).

These carry out the principles and rules of \<Policy\>, sections CM.3 and CM.4.

### 3.2 Roles and processes

Controls met here: CM-3, CM-3(4), CM-9.

**Table 1: Configuration management roles**

| Role | Part in configuration management |
| --- | --- |
| System owner | Owns this plan; chairs the change control board; approves departures from the secure settings, licence decisions and requests to install software |
| Security officer | Analyses the impact of every change; member of the board; receives drift reports |
| Windows server administrator | Member of the board; applies and checks the servers' settings; installs releases; keeps the approved software list |
| Database administrator | Applies and checks the SQL Server settings; applies the database structure scripts in a release |
| Developers | Make, test and release changes to the applications; keep the component list |
| Legal adviser | Privacy representative on the board, for any change that touches personal data |
| Authorising official | Decides on significant changes and High impact changes |
| \<Organisation\> | Provides the hosts, Group Policy, discovery tools, the in-house package feed and ServiceNow |

The holders are named in \<Roles and Responsibilities\>. The processes are the nine procedures of \<Procedures\> (CM).

**Identifying configuration items.** An item is identified when it enters the baseline, and is managed through the change procedure, PRO-CM-1, for its whole life. Each is named by its component and its version or tag, for example the API at a release tag, or Microsoft.Data.SqlClient at its recorded version. Each release is named by its signed tag.

### 3.3 Configuration items

Controls met here: CM-3, CM-9.

**Table 2: Configuration items**

| Item | Held in | Controlled by |
| --- | --- | --- |
| Application code: \<Code\>\_Web, \<Code\>\_Admin, \<Code\>\_API and \<Code\>\_Shared | Git repositories, tagged at each release | Developers, PRO-CM-1 |
| Software components: packages, browser libraries, runtime, operating system and database | Section 3.5 | Developers, PRO-CM-1 and PRO-CM-4 |
| Release scripts: service installation and database structure scripts | Git repositories, tagged at each release | Developers, PRO-CM-1 |
| Application settings, without secrets | Settings files at the release tag; secrets held in the key store, outside the baseline | Developers, Windows server administrator |
| Windows Server 2025 and SQL Server 2022 settings | CIS Benchmarks and recorded exceptions | Windows server and database administrators |
| Security documents | Restricted document store | System owner |

### 3.4 Baseline

Controls met here: CM-2, CM-2(2), CM-2(3).

The baseline is what a release must contain so that it can be rebuilt exactly.

**Table 3: Baseline**

| Item | Baseline |
| --- | --- |
| Application code | The signed release tag, with the commit of each of the API, UI application, Admin application and shared library: \[commits\] |
| Release packages | One package for each application, with its SHA-256 checksum recorded in the release record |
| Release scripts | Service installation and database structure scripts at the release tag |
| Software components | Section 3.5, at the versions in the lock files, with the software bill of materials |
| Settings | Section 3.6; settings files at the release tag, with secrets held outside them |
| Windows Server 2025 and SQL Server 2022 on the two servers | CIS Benchmarks with recorded exceptions, at their recorded update levels |
| Network placement and connections | The two servers, their zones and the flows between them, as \<Security Architecture\> and \<Access Control Management\>, section 3.6.4, set out; the connections in \<Assessment, Authorization, and Monitoring Management\>, section 3.7 |

Three means keep the baseline current, complete and accurate: signed release tags in the source repositories; lock files and the recorded checksum of each package; and the release record, which states the exact configuration. The build produces a software bill of materials at each release.

The system owner and the Windows server administrator review the baseline every 12 months and at each release (PRO-CM-2). Step 6 of every change updates it (PRO-CM-1). The three previous configurations are kept, so that a release can be rolled back (section 3.13).

### 3.5 Software components and licences

Controls met here: CM-7(5), CM-8, CM-10.

Every package, browser library, runtime, operating system and database \<System Name\> is built from or runs on, with its licence. This is the reference stack of \<System Description\>, sections 6.3 and 6.4; an application that replaces a part records it as a departure in \<System Description\>, section 3.6. A new component is recorded here, and checked for known vulnerabilities, before it enters the baseline (PRO-CM-4). Licences are checked again at each release and every 12 months (PRO-CM-9).

**Table 4: Software components**

| Component | Version | Supplier | Licence | Used by | Note |
| --- | --- | --- | --- | --- | --- |
| Windows Server 2025 | \<ver\> | Microsoft | Commercial, licensed by \<Organisation\> | Both servers | Includes Microsoft Defender, BitLocker and managed service accounts |
| Microsoft SQL Server 2022 | \<ver\> | Microsoft | Commercial, licensed by \<Organisation\> | Database server | |
| .NET 10 and ASP.NET Core 10 runtime, including Blazor Server | 10.0 | Microsoft | MIT | All three applications | Long-term support release |
| .NET 10 SDK | \<ver\> | Microsoft | MIT | Build only | |
| ASP.NET Core OpenID Connect authentication | \<ver\> | Microsoft | MIT | UI application, Admin application | Sign-in through PingFederate |
| Entity Framework Core 10, with the SQL Server provider | \<ver\> | Microsoft | MIT | API, shared library | |
| Microsoft.Data.SqlClient | \<ver\> | Microsoft | MIT | API | TLS with strict encryption and Windows authentication |
| Directory access library for LDAPS | \<ver\> | Microsoft | MIT | API | Group lookup in Active Directory |
| API documentation package | \<ver\> | \[Supplier\] | \[Licence\] | API | Development only; not in release builds |
| \[Server-side rendering library for the viewer\] | \<ver\> | \[Supplier\] | \[Licence\] | API | Renders a file as an image on the server |
| \[Browser libraries, such as a document viewer or an icon set\] | \<ver\> | \[Supplier\] | \[Licence\] | UI application | Packaged with the UI application and served by it. No content delivery service |

Every package comes through \<Organisation\>'s in-house checked package feed, at the version in the lock files.

### 3.6 Secure settings for every layer

Controls met here: CM-6.

**Table 5: Secure settings**

| Layer | Guidance | Key settings | Where set |
| --- | --- | --- | --- |
| Windows Server 2025, both servers | CIS Benchmark, Level 1 member server | Unneeded services and accounts removed, default passwords changed, auto-run off, Defender on, audit policy as \<Audit and Accountability Management\>, section 3.2 | \<Organisation\>'s Group Policy and the server build |
| SQL Server 2022 | CIS Benchmark for Microsoft SQL Server 2022 | TLS with strict encryption on TCP 1433; Windows authentication only, so no database password exists; the built-in sa login disabled; connections accepted only from the application server; logins and changes audited (\<Audit and Accountability Management\>, appendix A) | SQL Server configuration and SQL Server Audit |
| Application hosting | Microsoft's guidance for hosting ASP.NET Core as a Windows service | HTTPS only with HSTS, under NCSC's TLS profiles in \<System and Communications Protection Management\>, section 3.3; data protection key rings protected with DPAPI; each application a Windows service under its own managed service account | Each service's configuration |
| .NET runtime | Microsoft ASP.NET Core security guidance | Production environment; detailed errors off; interactive API documentation left out | Environment values |
| Application security settings | \<Access Control Management\>, \<Identification and Authentication Management\> and \<System and Communications Protection Management\> | The authentication cookie's lifetime, no longer than PingFederate's sign-in lifetime, the PingFederate connection (OpenID Connect client), cookie flags, content security policy and allowed origins, at the values in those documents | Settings files at the release tag |

The benchmarks are applied when the servers are built, and the developers apply the hosting and application settings (PRO-CM-3). Each departure from the guidance is recorded on TPL-6 with a reason, and approved by the system owner (PRO-CM-3).

Each month the Windows server administrator scans both servers against the benchmarks, and the database administrator compares the SQL Server settings. Any difference is reported to the security officer, and is put back or raised as a change (PRO-CM-7). Some Windows settings are set by \<Organisation\>'s Group Policy as part of its corporate configuration: account lockout, the logon banner and the screen lock. \<System Name\> accepts the corporate standard for those.

Both servers are configured to the CIS Benchmark by policy that \<Organisation\> applies, with only the functions, ports and services \<System Name\> needs, and checked with a benchmark tool (\<System Description\>, NFR-091). Where \<Organisation\>'s hardened build already sets a setting, its build standard is asked for as evidence and compared with the benchmark, and any shortfall is recorded as a departure.

### 3.7 Change control

Controls met here: CM-3, CM-3(2), CM-4, CM-4(2), CM-5, CM-8(1).

Every change to a configuration item in section 3.3 follows one route, including routine patches. Developers or administrators make the change through a release, and nothing else reaches the servers. Figure 1 shows the route.

![Figure 1: The route every change follows](figures/cmm-figure-1.png)

**Figure 1: The route every change follows**

**Table 6: Steps of a change**

| Step | Who | What | Record |
| --- | --- | --- | --- |
| 1 Request | Whoever needs the change | States what is to change and why | A ServiceNow change, or TPL-6 until ServiceNow is set up |
| 2 Impact analysis | Security officer | Answers the questions in section 3.9, and rates the impact | On the change, with the rating |
| 3 Decision | Change control board | Approves, refuses, defers or asks for more. A significant or High impact change goes to the authorising official first | On the change, with the date and members present |
| 4 Make and test | Developers or administrators | Make the change, and test it on a separate test environment before release | Test result on the change |
| 5 Verify | Those who made it | Check that the controls named in the analysis still work | Result on the change |
| 6 Update | Those who made it | Update the baseline, the component list and the inventory; sign the release tag; record each package's checksum; produce the software bill of materials | This document; the release record |

**Testing.** Each change is tested on the separate test environment before release, with the security tests that apply, and the result is recorded on the change (PRO-CM-1, step 4). A release that fails a test does not go out.

**Who made each change.** The change record names who made it. The servers and the database record it independently: Windows logs each administrator sign-in, installed service and policy change, and SQL Server Audit records each change to a table, login, role or permission (\<Audit and Accountability Management\>, section 3.2). The comparison with the baseline, monthly and at each release (P-29), finds a change that has no record.

**Emergency changes.** An emergency change is allowed only to stop or limit an incident or an outage. The system owner, or their deputy, approves it by phone or in person before it is made. It is recorded within 1 working day, with the impact analysis done afterwards, and the board confirms or reverses it at its next meeting (PRO-CM-8).

### 3.8 Change control board charter

Controls met here: CM-3, CM-3(4).

This charter follows CSS, Appendix H.

**Table 7: Change control board charter**

| Item | Rule |
| --- | --- |
| Purpose | To consider every change to \<System Name\>'s configuration items, make sure its impact is analysed and tested, decide on it, and tell those affected |
| Members | The system owner (chair), the security officer and the Windows server administrator. The legal adviser joins for any change touching personal data, as privacy representative. The database administrator and developers attend when their work is affected |
| Quorum | The system owner, or their deputy, and the security officer |
| Meetings | Monthly, and whenever an urgent or security change needs a decision sooner. Each meeting reviews the month's changes, emergency changes and drift reports |
| Inputs | A change request on TPL-6 or in ServiceNow, with its impact analysis (section 3.9) and test plan |
| Decisions | Approve, refuse, defer, or ask for more analysis. Each decision is recorded on the change with the date and the members present |
| Conflicts | Nobody approves a change they requested or made |
| Significant changes | Referred to the authorising official before they are made (\<Assessment, Authorization, and Monitoring Management\>, section 3.9) |
| Emergency changes | Made under PRO-CM-8 and reviewed at the next meeting |
| Records | Kept for 3 years (CM-03\_ODP\[01\]) |

### 3.9 Security impact analysis

Controls met here: CM-4.

The security officer answers each question on the change before the board decides. This follows CSS, Appendix I.

**Table 8: Impact analysis criteria**

| Question | What to check |
| --- | --- |
| What changes? | The configuration items in section 3.3 and the components in section 3.5 affected |
| Which controls are affected? | The families touched, for example access, sign-in, audit, encryption, boundary or backup, and the procedures that rely on them |
| Does it touch personal data? | If so, the legal adviser joins the decision |
| Does it add or change a connection or component? | Connections need \<Assessment, Authorization, and Monitoring Management\>, section 3.7; components need section 3.5 and a vulnerability check on TPL-7 |
| Is it a significant change? | The test in \<Assessment, Authorization, and Monitoring Management\>, section 3.9 |
| How will it be tested? | The test scripts in the test scripts folder that apply, in the test environment, and what proves the affected controls still work |
| How is it undone? | The back-out plan |
| What must be updated? | This plan, \<System Security Plan\> and any family document the change affects |

The security officer rates the impact Low, Medium or High. A High impact needs the authorising official's agreement as well as the board's.

### 3.10 Least functionality

Controls met here: CM-7, CM-7(1).

\<System Name\> is configured to do four things: store, search and show items, and administer them. Table 9 lists what is prohibited or restricted.

**Table 9: What is prohibited or restricted**

| Kind | Prohibited or restricted |
| --- | --- |
| Functions | Test pages, and any diagnostic not on the fixed list, in production; the interactive API documentation outside development; email or other outbound messages; any interface for other systems |
| Ports | Everything except the flows in \<System Description\>, section 6.5: HTTPS on TCP 443 to the UI application; the Admin application over the administration route; the API on the loopback address only; SQL Server on TCP 1433 from the application server only; LDAPS on TCP 636 to Active Directory; HTTPS on TCP 443 from the application server to \<Organisation\>'s PingFederate (F10); server and database administration only over \<Organisation\>'s managed administration route (F11); and \<Organisation\>'s time, logging, proxy and backup services. The flows \<System Name\> asks \<Organisation\> to allow are in \<Access Control Management\>, section 3.6.4 |
| Protocols | Everything except TLS-protected ones on those routes |
| Software | Anything not on the approved software list, and any package the applications do not use |
| Services | Any Windows service not needed for those four things |

The Windows server administrator and the developers review all five every 12 months, and record the result on TPL-3 (PRO-CM-5). Anything not needed is removed through a change.

### 3.11 Who may change what

Controls met here: CM-5.

**Table 10: Access restrictions for change**

| What | Who may change it | How it is limited |
| --- | --- | --- |
| The applications | Developers, each change reviewed by a second developer | Permissions and required reviews in the source repositories |
| What runs on the application server | The named Windows server administrators, installing an approved release | Windows permissions: only they can write to each application's program folder, and no application can change its own files (\<Access Control Management\>, section 3.6.3) |
| Windows settings | The named Windows server administrators; \<Organisation\>, through Group Policy | Named administrator accounts, only over \<Organisation\>'s managed administration route, with multi-factor authentication (F11); \<Organisation\>'s change process |
| SQL Server settings and database structure | The named database administrators, the structure only through a release. The API's database account cannot create, alter or drop tables | Database permissions (\<Access Control Management\>, section 3.6) |
| Application settings and secrets | The named Windows server administrators | Windows permissions on the settings files; secrets in the key store |
| The hosts, network and firewall | \<Organisation\> | Its physical and logical controls, and its change process (EV-CM-01) |
| This document set | The system owner | The restricted document store, under version control |

Nobody approves a change they requested or made. Every change by any of these people follows the route in section 3.7.

### 3.12 Inventory and where information is held

Controls met here: CM-8, CM-8(1), CM-8(3), CM-12, CM-12(1).

**Inventory.** Two lists make up the inventory, and no component is in both. The servers and the other components of the system are in \<System Security Plan\>, section 3.4. The software components are in section 3.5. Each entry gives the name, type, version, location and owner, and for software also the supplier and licence. Both are updated as step 6 of every change, and a change is not closed until they are. A bill of materials from each build checks the software list.

**Unauthorised components.** \<Organisation\>'s discovery tools check its network, including both servers, every month. When one finds an unauthorised component, it alerts the Windows server administrator, who removes the component or disables its network access, tells the security officer, and records it on TPL-8 (PRO-CM-6).

**Where information is held.** Items, their files, schema definitions and audit records are in SQL Server 2022 on the database server, each schema in its own database schema. The application server holds only working files: encrypted export working copies, deleted as P-20 sets, each application's key ring, and logs. Backups go to \<Organisation\>'s backup site. \<System Security Plan\>, sections 3.4 and 4.4, hold the record. A change of location is a change to the baseline, and a new site is a significant change. Each is recorded on the change and in \<System Security Plan\>.

**Finding information.** Items are held by schema in the database, so the database itself lists them. For anything outside it, \<Organisation\>'s tools are to scan both servers for stray copies, if it has such tools.

**Who has access to it.** The approved access list names the members of each of \<System Name\>'s AD groups, the Windows server and database administrators, and \<Organisation\>'s staff with access to the hosts and backups. The first list is made before any real data is held.

### 3.13 Library, tools, monitoring and retention

Controls met here: CM-2(3), CM-3, CM-6.

**Table 11: Library, tools, monitoring and retention**

| Item | Detail |
| --- | --- |
| Configuration library | Git repositories for code and release scripts; \<Organisation\>'s in-house package feed, holding each package at its recorded version; the restricted document store for documents; release records with their checksums and software bill of materials |
| Tools | Git and its signed tags; the build pipeline; NuGet through the in-house package feed; ServiceNow for changes; CIS-CAT or an equivalent scanner; Test-ConfigurationManagement.ps1; \<Organisation\>'s discovery tools (EV-CM-02) |
| Monitoring | Drift check, monthly and at each release (P-29), under PRO-CM-7, reported on TPL-8 to the security officer, and included in the monthly measures in \<Assessment, Authorization, and Monitoring Management\>, section 3.8 |
| Retention | Change records for 3 years; the 3 previous configurations, each with tag, package checksums, settings and software bill of materials; superseded documents for 3 years |
| Disposal | Removed configurations are deleted from the library only after their retention period, with the system owner's approval |

### 3.14 What \<Organisation\> provides

Controls met here: CM-3, CM-5, CM-6, CM-8(3), CM-10, CM-12(1).

**Table 12: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Physical and logical limits on changing the hosts | CM-5 | Only authorised \<Organisation\> staff can change the hosts and hosting, through its change process | EV-CM-01 |
| Tools that detect unauthorised components, and that locate information | CM-8(3), CM-12(1) | Both servers are checked every month, and the Windows server administrator is alerted | EV-CM-02 |
| Licences for the software on the servers and hosting, and controls on peer-to-peer software | CM-10 | Windows Server and the hosting are licensed, and peer-to-peer software is blocked | EV-CM-03 |
| Group Policy settings on the servers | CM-6 | The corporate standard for lockout, the logon banner and the screen lock | EV-AC-05 to EV-AC-07 |
| ServiceNow, for the change workflow | CM-3 | A workflow built by the Application Support Team to \<System Name\>'s design | None |

### 3.15 Approved software and installation

Controls met here: CM-7(2), CM-7(5), CM-10, CM-11.

1. **Approved software list.** The Windows server administrator keeps the approved software list, which says what may run on the servers. For the applications themselves, the component list in section 3.5 is the list. Both are reviewed every 12 months.
2. **Allow by exception, by procedure.** Nothing is installed on the servers without an approved request (PRO-CM-4). A person who needs software there raises a request in ServiceNow, and the system owner approves or refuses it. Only the named Windows server administrators have the Windows user rights to install software.
3. **Not enforced by the system.** Windows application control is not used, so the list is not technically enforced on the servers.
4. **Compliance check.** Every 12 months, with the functions review in section 3.10, what is installed on the servers is compared with the approved software list.
5. **Users' devices.** \<Organisation\>'s policy governs software on users' own devices.
6. **Licences.** Every component's licence is recorded in section 3.5 before it enters the baseline, and must permit \<System Name\>'s use. A licence that is not a standard open source licence goes to the system owner for a recorded decision. \<System Name\>'s own components are not licensed by quantity. Windows Server and anything else licensed by quantity is \<Organisation\>'s, and is tracked in its licence record.
7. **Peer-to-peer file sharing.** None is allowed: no peer-to-peer software is on the approved list, and \<Organisation\>'s network controls apply.

### 3.16 Devices for travel to high-risk areas

Controls met here: CM-2(7).

No \<System Name\> device is issued to anyone, for travel or otherwise. \<System Name\> is reached only from \<Organisation\>'s managed devices, and phones and tablets cannot reach it (\<Access Control Management\>, section 3.6.5). If that changes, the system owner sets the configuration of the devices, and the checks made on them when the person returns, before the first device is issued.

### 3.17 Policy, procedures and this plan

Controls met here: CM-1, CM-9.

\<Policy\> (CM) and \<Procedures\> (CM) meet CM-1. Who they are shared with is in \<Policy\>, section CM.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.

This document is the configuration management plan. Roles and processes are in section 3.2, the configuration items in section 3.3, the route a change follows in section 3.7, and the environments in Appendix A. The system owner reviews and approves it. It is classified Restricted and held in the restricted document store.

## Appendix A Environments

The CSS guidance on CM-9 asks the plan to say how the development, test and operational environments are controlled. \<System Name\> has three, and nothing moves from one to the next except as a tagged release.

**Table 13: Environments**

| Environment | What it is | What it may hold | Who may change it |
| --- | --- | --- | --- |
| Development | The developers' computers, and the source repositories | Invented data only. Never real data or production secrets | Developers, each change reviewed by a second developer |
| Test | A separate, throwaway copy of the whole system, built from a tagged release, configured as production is, including TLS, and removed after each test run | Invented data only, loaded by script | Developers |
| Production | The application server and the database server at \<Organisation\> | Real data, once \<System Name\> is authorised | The named Windows server and database administrators only, installing an approved release |

A release is tested in the test environment before it reaches production (section 3.7, step 4). CSS asks for a separate test environment only at High, as CM-4(1); \<System Name\> has one.

## Appendix B CM controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 14 says where.

**Table 14: CM controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| CM-3(1) Automated Documentation, Notification, and Prohibition of Changes | A workflow that records each change, tells the approvers, and blocks a change until approved | Not required. Done in part by the ServiceNow workflow |
| CM-3(6) Cryptography Management | Cryptographic mechanisms under configuration management | Not required. Keys and certificates are in the key register (\<System and Communications Protection Management\>, section 3.4), and a new key or certificate goes through change control |
| CM-4(1) Separate Test Environments | Changes analysed in a separate test environment | Not required. Done: appendix A |
| CM-5(1) Automated Access Enforcement and Audit Records | Automated enforcement of who may change the system, with audit records | Not required. Done in part: Windows and database permissions enforce it, and their logs record it |
| CM-6(1), CM-6(2) Automated Management and Verification; Respond to Unauthorized Changes | Automated checking of settings, and a set response to an unauthorised change | Not required. Done in part in design: the monthly benchmark scan, and the drift procedure |
| CM-7(4) Unauthorized Software, Deny-by-exception | A list of software that must not run | Not required. \<System Name\> uses the stricter alternative, CM-7(5), an approved list, though it is not enforced by the system |
| CM-8(2), CM-8(4) Automated Maintenance; Accountability Information | An inventory kept by automated means, naming who is accountable for each component | Not required. Each entry names an owner. The bill of materials will keep the software list by automated means |
| CM-13 Data Action Mapping | A map of what the system does with personal data | In no security baseline. The personal data inventory is in \<PII Processing Management\>, section 3.3 |
| CM-14 Signed Components | Components installed only if signed with an approved certificate | In no baseline. Release tags are to be signed, and packages checked for their signature |
