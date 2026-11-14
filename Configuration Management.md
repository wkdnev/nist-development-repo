# \<DocuView\> Configuration Management

**\<ref\> | Version \<ver\> | Draft for the system owner's approval**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Summary](#3-summary)

[4 The design](#4-the-design)

[5 Each control and enhancement](#5-each-control-and-enhancement)

[Appendix A How configuration was built in the tested build](#appendix-a-how-configuration-was-built-in-the-tested-build)

[Appendix B Parameter register](#appendix-b-parameter-register)

[Appendix C Environments](#appendix-c-environments)

[Appendix D CM controls outside the Moderate baseline](#appendix-d-cm-controls-outside-the-moderate-baseline)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Configuration Management |
| Version | \<ver\> |
| Status | Draft for the system owner's approval. Until 13 November 2026 this was the Configuration Management Plan, whose version \<ver\> the system owner approved. It has been rebuilt in the form of the other family documents, with no agreed value changed |
| Date | 13 November 2026 |
| Owner | System owner |
| Applies to | Configuration Management family |
| Classification | Restricted |
| Next review | Every 12 months, and after a significant change |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | Neil Ramsbottom | Pending for this version. Version \<ver\> approved (D-CM-12); version \<ver\> approved with the SC pack review (D-SC-07) | 8 November 2026 |

### 1.3 Change history

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 13 November 2026 | Appendix C: wording of the development environment |
| \<ver\> | 13 November 2026 | Cross-check against NIST's guidance for the family: the baseline includes network placement; each change records who made it; the environments are set out in a new appendix C; the CM controls outside the Moderate baseline are listed in a new appendix D; and the Administrator Guide's statement on the server build is noted against the open fact |
| \<ver\> | 13 November 2026 | The fact still to be supplied on the server build is worded as one placeholder |
| \<ver\> | 13 November 2026 | The system owner's decisions on the review (D-CM-14): the applications run as Windows services (D-PL-10); the value for CM-12 no longer lists accounts; the owner and licence of the internal access control component are tracked (PA-113); and who builds the servers to which standard is recorded as a fact still to be supplied |
| \<ver\> | 13 November 2026 | Rebuilt in the form of the other family documents, at the system owner's request (D-CM-13), and renamed from Configuration Management Plan to Configuration Management. It remains the plan that CM-9 requires. Each control is set out part by part, with change control, least functionality and who may change what each given a section. No agreed value is changed |
| \<ver\> | 12 November 2026 | References to the assessment, authorisation and monitoring design point to \<Assessment, Authorization, and Monitoring Management\>, where it is now held (D-CA-11) |
| \<ver\> | 12 November 2026 | References to the audit design point to \<Audit and Accountability Management\>, where it is now held (D-AU-10) |
| \<ver\> | 12 November 2026 | Application settings name the trust in AD FS (D-AC-23) |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change |
| \<ver\> | 12 November 2026 | References to the access control design point to \<Access Control Management\>, where it is now held |
| \<ver\> | 12 November 2026 | The earlier rows of the change history are folded into one row, as the system owner decided (D-GEN-25). No other change |
| \<ver\> | 12 November 2026 | References to the register, the policy and the assessment record follow their new section and table numbers (D-GEN-24) |
| \<ver\> | 12 November 2026 | Documents are cited by name in angle brackets, in place of their numbers, as the system owner asked (D-GEN-23). No other change |
| \<ver\> | 12 November 2026 | The combined documents are cited by their new numbers and chapters (D-GEN-21). The document standard is cited as \<Documentation Map\>, section 5. The contents list is rebuilt so that its links work in Markdown |
| \<ver\> | 12 November 2026 | Sweep after the SC policy's legal review: the application hosting benchmark follows NCSC's TLS profiles and protects the key rings, in place of "TLS 1.2 or later" (D-SC-07). Approved by the system owner |
| \<ver\> to \<ver\> | 6 to 8 November 2026 | The earlier versions. Their history is kept in the change record (\<Documentation Map\>, section 5.1) |

| **SECTION 2** |
| --- |

## 2 Purpose

This document shows how \<DocuView\>'s configuration is recorded, controlled and changed, for each of the 24 Configuration Management (CM) controls and enhancements in the NIST SP 800-53 Rev 5 Moderate baseline. It is also the Configuration Management Plan that CM-9 requires, and follows the outline in NIST SP 800-128, Appendix D. Section 4 sets out the design: roles and processes, the configuration items, the baseline, the software components, the secure settings, change control, impact analysis, least functionality, who may change what, the inventory, and the library. Section 5 takes each control in turn. Appendix A records how configuration was built in the tested build. Appendix B lists every value NIST asks the organisation to define. Appendix C sets out the development, test and production environments. Appendix D lists the CM controls NIST does not select at Moderate.

This is the only place the configuration management design is held. Other documents point here. The policy is in \<Policy\> (CM), and the steps people follow are in \<Procedures\> (CM).

An assessor examines the baseline, the inventory, the settings, the change records and the board's decisions, interviews those who make and approve changes, and tests that the system is configured as the documents say (NIST SP 800-53A). So for each control section 5 gives:

- **each part of the control**, as NIST letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Design and today.** The Design column is what the system owner has agreed. The Today column is what was found in the build labelled v1.0, tested in Docker on 6 and 8 November 2026, and the position of the servers, which are not yet built.

**Table 4: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

| **SECTION 3** |
| --- |

## 3 Summary

Of the 24 controls, 2 are implemented, 7 are partially implemented and 15 are not implemented. No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 5: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| CM-1 | Policy and Procedures | Partially implemented | The policy and procedures are not yet shared or walked through | NC-CM-01; PA-20 |
| CM-2 | Baseline Configuration | Partially implemented | The images are not pinned, so a release cannot be rebuilt exactly. No server baseline exists | NC-CM-02, NC-CM-25; PA-54, PA-77, PA-80 |
| CM-2(2) | Automation Support for Accuracy and Currency | Partially implemented | Images are not pinned, no bill of materials is produced, and the change workflow is not set up | NC-CM-03, NC-CM-25; PA-53, PA-77, PA-78 |
| CM-2(3) | Retention of Previous Configurations | Not implemented | Only one release exists, so no earlier configuration is kept yet | NC-CM-04; PA-53 |
| CM-2(7) | Configure Systems and Components for High-risk Areas | Implemented | Nothing | NC-CM-05 |
| CM-3 | Configuration Change Control | Not implemented | The change workflow is not set up, and the board has not met | NC-CM-06; PA-53, PA-84, PA-91 |
| CM-3(2) | Testing, Validation, and Documentation of Changes | Not implemented | Nothing makes a release wait for its tests | NC-CM-07; PA-53 |
| CM-3(4) | Security and Privacy Representatives | Implemented | Nothing | NC-CM-08 |
| CM-4 | Impact Analyses | Not implemented | Impact analysis is defined but not in use | NC-CM-09; PA-53 |
| CM-4(2) | Verification of Controls | Not implemented | Verification after a change is defined but not in use | NC-CM-10; PA-53 |
| CM-5 | Access Restrictions for Change | Not implemented | The servers are not built, the repositories need no review, and ABC Technologies' restrictions are not evidenced | NC-CM-11; PA-91, PA-112, EV-CM-01 |
| CM-6 | Configuration Settings | Not implemented | No settings are applied, as the servers are not built. Nothing checks for drift | NC-CM-12; PA-54, PA-80 |
| CM-7 | Least Functionality | Partially implemented | Diagnostic, test and maintenance pages remain; unused packages are built in | NC-CM-13, NC-CM-27; PA-07, PA-18, PA-31, PA-79, PA-85 |
| CM-7(1) | Periodic Review | Not implemented | The first yearly review has not been held | NC-CM-14; PA-110 |
| CM-7(2) | Prevent Program Execution | Not implemented | Not enforced by the system, by decision. The risk is accepted to 6 November 2027 | NC-CM-15; PA-55 |
| CM-7(5) | Authorized Software, Allow-by-exception | Not implemented | The approved software list is not written. Not enforced, by decision; risk accepted | NC-CM-16; PA-55 |
| CM-8 | System Component Inventory | Partially implemented | No bill of materials. Server details wait for the servers | NC-CM-17, NC-CM-26; PA-54, PA-78 |
| CM-8(1) | Updates During Installation and Removal | Not implemented | Updating at each change is not yet in use | NC-CM-18, NC-CM-26; PA-78, PA-111 |
| CM-8(3) | Automated Unauthorized Component Detection | Not implemented | ABC Technologies' detection is not evidenced | NC-CM-19; PA-112, EV-CM-02 |
| CM-9 | Configuration Management Plan | Partially implemented | The plan is not yet in use, and not yet in the restricted store | NC-CM-20; PA-53, PA-88 |
| CM-10 | Software Usage Restrictions | Not implemented | ABC Technologies' licences are not evidenced. One internal component's licence is to be confirmed | NC-CM-21; PA-112, PA-113, EV-CM-03 |
| CM-11 | User-installed Software | Not implemented | The servers are not built, and the first yearly check has not been held | NC-CM-22; PA-55, PA-110 |
| CM-12 | Information Location | Partially implemented | The approved access list is not built | NC-CM-23; PA-111 |
| CM-12(1) | Automated Tools to Support Information Location | Not implemented | The tools are not confirmed | NC-CM-24; PA-112, EV-CM-02 |

Most of this family is a process that has not started, because \<DocuView\> is not in use and its servers are not built. Three gaps are in the system itself: the change workflow is not set up (PA-53), diagnostic and maintenance pages remain in the release (PA-07, PA-31), and a release cannot yet be rebuilt exactly (PA-77). One risk is accepted: software is not technically restricted on the servers, by decision (NC-CM-15, NC-CM-16).

| **SECTION 4** |
| --- |

## 4 The design

### 4.1 Principles

1. **Known baseline.** The approved configuration is recorded and versioned, so that any release can be rebuilt exactly.
2. **Controlled change.** No change happens without an impact analysis, approval and testing.
3. **Least functionality.** Anything \<DocuView\> does not need is turned off or left out.
4. **Accurate inventory.** Every component is recorded, and an unauthorised one is detected.
5. **Secure settings at every layer.** Windows Server, PostgreSQL, the hosting, the runtime and the applications each follow a named standard.
6. **Nothing drifts unseen.** The running system is compared with the baseline every month.

These carry out the principles and rules of \<Policy\>, sections CM.3 and CM.4.

### 4.2 Roles and processes

**Table 6: Configuration management roles**

| Role | Part in configuration management |
| --- | --- |
| System owner | Owns this plan; chairs the change control board; approves departures from the secure settings, licence decisions and requests to install software |
| Security officer | Analyses the impact of every change; member of the board; receives drift reports |
| Windows server administrator | Member of the board; applies and checks the servers' settings; installs releases; keeps the approved software list |
| Database administrator | Applies and checks the PostgreSQL settings |
| Developers | Make, test and release changes to the applications; keep the component list |
| Legal adviser | Privacy representative on the board, for any change that touches personal data |
| Authorising official | Decides on significant changes and High impact changes |
| ABC Technologies | Provides the hosts, Group Policy, discovery tools and Jira |

The holders are named in \<Roles and Responsibilities\>. The processes are the nine procedures of \<Procedures\> (CM).

**Identifying configuration items.** An item is identified when it enters the baseline, and is managed through the change procedure, PRO-CM-1, for its whole life. Each is named by its component and its version or tag, for example DV\_API v1.0 or Npgsql 10.0.2. Each release is named by its tag.

### 4.3 Configuration items

**Table 7: Configuration items**

| Item | Held in | Controlled by |
| --- | --- | --- |
| Application code, DV\_API, DV\_Web, DV\_Admin\_UI, DV\_Shared | Git repositories, tagged v1.0 | Developers, PRO-CM-1 |
| Access-control toolkit (OfflineModules.AccessControl 0.2.0) | Its own repository, commit 20524d8 | Developers, PRO-CM-1 |
| Software components: packages, base images, runtime and database | Section 4.5 | Developers, PRO-CM-1 and PRO-CM-4 |
| Container and deployment files | DV\_Workspace, tagged v1.0 | Developers, PRO-CM-1 |
| Application settings and environment values, without secrets | Settings files and deployment files; secrets outside the baseline once PA-19 is fixed | Developers, Windows server administrator |
| Windows Server 2025 and PostgreSQL settings | CIS Benchmarks and recorded exceptions; VMs not built | Windows server and database administrators |
| Security documents | Restricted document store | System owner |

### 4.4 Baseline

The baseline is what a release must contain so that it can be rebuilt exactly. The current baseline is v1.0. Checks C01 to C03 test it.

**Table 8: Baseline v1.0**

| Item | Baseline | State now |
| --- | --- | --- |
| Application code | Tag v1.0: DV\_API `b82831a`, DV\_Web `b06b4e1`, DV\_Admin\_UI `43ef895`, DV\_Shared `a8c3a3a` | Met (C03) |
| Deployment files | DV\_Workspace tag v1.0, commit `21018a6` | Met |
| Access-control toolkit | Commit `20524d8`, packaged as 0.2.0 | Met |
| Application base images | `mcr.microsoft.com/dotnet/aspnet:10.0` and `sdk:10.0`, to be pinned by digest; .NET runtime 10.0.14 observed on 8 November 2026 | Not met: floating tags (C01; PA-77) |
| Database image | `postgres:18`, to be pinned by digest; observed as PostgreSQL 18.6, digest `sha256:3a4264520e12…` | Not met: floating tag (C02; PA-77) |
| Software components | Section 4.5 | Met: listed by hand; no bill of materials yet (PA-78) |
| Settings | Section 4.6; settings files at tag v1.0, with secrets moved out (PA-19) | Partly: secrets still in settings files (C07) |
| Windows Server and PostgreSQL on the VMs | CIS Benchmarks with recorded exceptions | Not assessable: VMs not built (PA-54) |
| Network placement and connections | The two servers, their zones and the flows between them, as \<Security Architecture\> and \<Access Control Management\>, section 4.6.4, set out; the connections in \<Assessment, Authorization, and Monitoring Management\>, section 4.7 | Recorded as the design. Not built |

The system owner and the Windows server administrator review the baseline every 12 months and at each release (PRO-CM-2). The three previous configurations are kept (section 4.13).

### 4.5 Software components and licences

Every package, image, runtime and database \<DocuView\> is built from, with its licence. The check of 8 November 2026 wrote the same list from the build, and the two agreed (C04). A new component is recorded here, and checked for known vulnerabilities, before it enters the baseline (PRO-CM-4). Licences are checked again at each release and every 12 months (PRO-CM-9).

**Table 9: Software components**

| Component | Version | Supplier | Licence | Used by | Note |
| --- | --- | --- | --- | --- | --- |
| .NET and ASP.NET Core runtime (aspnet image) | 10.0, observed 10.0.14 | Microsoft | MIT | All three applications | Image to be pinned (PA-77) |
| .NET SDK image | \<ver\> | Microsoft | MIT | Build only | Image to be pinned (PA-77) |
| PostgreSQL (postgres image) | 18, observed 18.6 | PostgreSQL Global Development Group | PostgreSQL Licence | Database | Image to be pinned (PA-77) |
| Microsoft.AspNetCore.Authentication.JwtBearer | 10.0.5 | Microsoft | MIT | DV\_API |  |
| Microsoft.AspNetCore.Authorization | 10.0.5 | Microsoft | MIT | DV\_Web |  |
| Microsoft.AspNetCore.Components.Authorization | 10.0.5 | Microsoft | MIT | DV\_Web, DV\_Admin\_UI |  |
| Microsoft.AspNetCore.OpenApi | 10.0.5 | Microsoft | MIT | DV\_API |  |
| Microsoft.EntityFrameworkCore | 10.0.5 | Microsoft | MIT | DV\_Shared, DV\_Web |  |
| Microsoft.EntityFrameworkCore.Design and .Tools | 10.0.5 | Microsoft | MIT | DV\_API, DV\_Web, DV\_Admin\_UI | Design-time tools |
| Npgsql | 10.0.2 | Npgsql project | PostgreSQL Licence | DV\_Shared, DV\_Web |  |
| Npgsql.EntityFrameworkCore.PostgreSQL | 10.0.1 | Npgsql project | PostgreSQL Licence | All three applications |  |
| OfflineModules.AccessControl (Accounts, AspNetCore, Sessions) | 0.2.0 | Access-control toolkit repository | \[owner and licence to confirm\] (PA-113) | DV\_Shared | Internal component |
| SixLabors.ImageSharp | 3.1.12 | Six Labors | Six Labors Split License 1.0, free community tier (D-CM-09) | DV\_API, DV\_Web | Known advisories (PA-56) |
| SkiaSharp and SkiaSharp.NativeAssets.Linux.NoDependencies | 3.119.2 | Microsoft (.NET Foundation) | MIT | DV\_API, DV\_Web |  |
| Swashbuckle.AspNetCore | 10.1.7 | Swashbuckle project | MIT | DV\_API | Development only; to leave release builds (PA-79) |
| Azure.Storage.Blobs | 12.27.0 | Microsoft | MIT | DV\_API | Not used; to be removed (PA-79) |

### 4.6 Secure settings for every layer

**Table 10: Secure settings**

| Layer | Guidance | Key settings | Where set | State now |
| --- | --- | --- | --- | --- |
| Windows Server 2025, both VMs | CIS Benchmark, Level 1 member server | Unneeded services and accounts removed, default passwords changed, auto-run off, Defender on, audit policy as \<Audit and Accountability Management\>, section 4.2 | Group policy and VM build | Not assessable: VMs not built (PA-54) |
| PostgreSQL 18 | CIS Benchmark for PostgreSQL | TLS required; scram-sha-256 passwords; listens only on the database VM's address; connections and changes logged | postgresql.conf, pg\_hba.conf | Not met in Docker: TLS off (B02), logging off (A30) |
| Application hosting | Microsoft's guidance for hosting ASP.NET Core as a Windows service | HTTPS only with HSTS, under NCSC's TLS profiles in \<Control Implementation Register\>, section SC.4; data protection key rings protected with DPAPI; each application under its own low-privilege account | Each service's configuration | Decided on 13 November 2026: each application runs as a Windows service, under its own service account (D-PL-10, D-AC-19). Not built, as the servers are not built |
| .NET runtime | Microsoft ASP.NET Core security guidance | Production environment; detailed errors off; API documentation off | Environment values | Met in Docker (C08, C11) |
| Application security settings | \<Access Control Management\>, \<Control Implementation Register\> (IA) and \<Control Implementation Register\> (SC) | Session time-outs, the trust in AD FS, cookie flags, content security policy and allowed origins, at the values in those documents | Settings files at tag v1.0 | As assessed in the AC, IA and SC assessments |

Each departure from the guidance is recorded on TPL-6 with a reason, and approved by the system owner (PRO-CM-3). Some Windows settings are set by ABC Technologies' Group Policy as part of its corporate configuration: account lockout, the logon banner and the screen lock. \<DocuView\> accepts the corporate standard for those (D-AC-21).

One fact is still to be supplied: \[who builds the two servers and to which standard\]. The Administrator Guide, \<Administrator Guide\>, has them built from ABC Technologies' hardened build and then brought to this baseline. If that is confirmed, ABC Technologies' build standard is asked for as evidence, and the CIS Benchmark scan shows what the build leaves to be done. Until it is, the design stands as written: the CIS Benchmark, applied by the Windows server administrator. If ABC Technologies builds them, its standard is asked for as evidence, compared with the benchmark, and any shortfall recorded as a departure.

### 4.7 Change control

Every change to a configuration item follows one route. Figure 1 shows it.

![Figure 1: The route every change follows](figures/cmm-figure-1.png)

**Figure 1: The route every change follows**

**Table 11: Steps of a change**

| Step | Who | What | Record |
| --- | --- | --- | --- |
| 1 Request | Whoever needs the change | States what is to change and why | A Jira change, or TPL-6 until Jira is set up |
| 2 Impact analysis | Security officer | Answers the questions in section 4.9, and rates the impact | On the change, with the rating |
| 3 Decision | Change control board | Approves, refuses, defers or asks for more. A significant or High impact change goes to the authorising official first | On the change, with the date and members present |
| 4 Make and test | Developers or administrators | Make the change, and test it on a separate test environment before release | Test result on the change |
| 5 Verify | Those who made it | Check that the controls named in the analysis still work | Result on the change |
| 6 Update | Those who made it | Update the baseline, the component list and the inventory; tag the release; record the pinned image versions; produce the bill of materials | This document; the release record |

**Who made each change.** The change record names who made it. The servers and the database record it independently: Windows logs each administrator sign-in, installed service and policy change, and PostgreSQL logs each change to a table, role or permission (\<Audit and Accountability Management\>, section 4.2). The monthly comparison with the baseline finds a change that has no record.

**Emergency changes.** An emergency change is allowed only to stop or limit an incident or an outage. The system owner, or their deputy, approves it by phone or in person before it is made. It is recorded within 1 working day, with the impact analysis done afterwards, and the board confirms or reverses it at its next meeting (PRO-CM-8).

**Today:** the Jira workflow is not set up, and no change has followed this route. Changes so far are commits in the source repositories (PA-53).

### 4.8 Change control board charter

This charter follows NIST SP 800-128, Appendix H.

**Table 12: Change control board charter**

| Item | Rule |
| --- | --- |
| Purpose | To consider every change to \<DocuView\>'s configuration items, make sure its impact is analysed and tested, decide on it, and tell those affected |
| Members | The system owner (chair), the security officer and the Windows server administrator. The legal adviser joins for any change touching personal data, as privacy representative. The database administrator and developers attend when their work is affected |
| Quorum | The system owner, or their deputy, and the security officer |
| Meetings | Monthly, and whenever a change needs a decision sooner |
| Inputs | A change request on TPL-6 or in Jira, with its impact analysis (section 4.9) and test plan |
| Decisions | Approve, refuse, defer, or ask for more analysis. Each decision is recorded on the change with the date and the members present |
| Conflicts | Nobody approves a change they requested or made |
| Significant changes | Referred to the authorising official before they are made (\<Assessment, Authorization, and Monitoring Management\>, section 4.9) |
| Emergency changes | Made under PRO-CM-8 and reviewed at the next meeting |
| Records | Kept for 3 years (CM-03\_ODP\[01\]) |

### 4.9 Security impact analysis

The security officer answers each question on the change before the board decides. This follows NIST SP 800-128, Appendix I.

**Table 13: Impact analysis criteria**

| Question | What to check |
| --- | --- |
| What changes? | The configuration items in section 4.3 and the components in section 4.5 affected |
| Which controls are affected? | The families touched, for example access, sign-in, audit, encryption, boundary or backup, and the procedures that rely on them |
| Does it touch personal data? | If so, the legal adviser joins the decision |
| Does it add or change a connection or component? | Connections need \<Assessment, Authorization, and Monitoring Management\>, section 4.7; components need section 4.5 and a vulnerability check on TPL-7 |
| Is it a significant change? | The test in \<Assessment, Authorization, and Monitoring Management\>, section 4.9 |
| How will it be tested? | The test scripts in `DV_Workspace/tests` that apply, on a separate stack, and what proves the affected controls still work |
| How is it undone? | The back-out plan |
| What must be updated? | This plan, \<System Security Plan\> and any family document the change affects |

The security officer rates the impact Low, Medium or High. A High impact needs the authorising official's agreement as well as the board's.

### 4.10 Least functionality

\<DocuView\> is configured to do four things: store, search and show documents, and administer them. Table 14 lists what is prohibited or restricted.

**Table 14: What is prohibited or restricted**

| Kind | Prohibited or restricted | Today |
| --- | --- | --- |
| Functions | Diagnostic, test and maintenance pages in production; the API documentation page outside development | The documentation page is off (B06). Diagnostic, test and maintenance pages remain (PA-07, PA-31) |
| Ports | Everything except HTTPS to the applications, the database from the application server only, and administration from ABC Technologies' network. The flows \<DocuView\> asks ABC Technologies to allow are in \<Access Control Management\>, section 4.6.4 | The database is reachable only locally in the test environment (C09). The servers are not built |
| Protocols | Everything except TLS-protected ones on those routes | Plain HTTP in the test environment (PA-18) |
| Software | Anything not on the approved software list, and any package the applications do not use | An unused package and a development-only package are in the release (C05, C06; PA-79). Each image holds a shell and a package manager (PA-85) |
| Services | Any Windows service not needed for those four things | Not assessable: the servers are not built |

The Windows server administrator and the developers review all five every 12 months, and remove what is not needed (PRO-CM-5).

### 4.11 Who may change what

**Table 15: Access restrictions for change**

| What | Who may change it | How it is limited |
| --- | --- | --- |
| The applications | Developers, each change reviewed by a second developer | Permissions and required reviews in the source repositories (PA-91) |
| What runs on the application server | The named Windows server administrators, installing an approved release | Windows permissions: only they can write to each application's program folder, and no application can change its own files (\<Access Control Management\>, section 4.6.3) |
| Windows settings | The named Windows server administrators; ABC Technologies, through Group Policy | Named administrator accounts; ABC Technologies' change process |
| PostgreSQL settings and structure | The named database administrators. The API's database account cannot create, alter or drop tables | Database permissions (\<Access Control Management\>, section 4.6) |
| Application settings and secrets | The named Windows server administrators | Windows permissions on the settings files; secrets in the key store (PA-19) |
| The hosts, network and firewall | ABC Technologies | Its physical and logical controls, and its change process (EV-CM-01) |
| This document set | The system owner | The restricted document store, under version control (PA-88) |

Nobody approves a change they requested or made. Every change by any of these people follows the route in section 4.7.

### 4.12 Inventory and where information is held

**Inventory.** Two lists make up the inventory, and no component is in both. The servers and the other components of the system are in \<System Security Plan\>, section 4.4. The software components are in section 4.5. Each entry gives the name, type, version, location and owner, and for software also the supplier and licence. Both are updated as step 6 of every change.

**Where information is held.** Documents and audit records are in PostgreSQL on the database server, each project in its own schema. The application server holds only working files. \<System Security Plan\>, section 5.4, holds the record.

**Who has access to it.** The approved access list names the members of each of \<DocuView\>'s AD groups, the Windows server and database administrators, and ABC Technologies' staff with access to the hosts and backups. The first list is made before any production documents are held (D-AC-14).

### 4.13 Library, tools, monitoring and retention

**Table 16: Library, tools, monitoring and retention**

| Item | Detail |
| --- | --- |
| Configuration library | Git repositories for code and deployment files; an image registry holding images by digest, \[registry to be chosen when the VMs are built\]; the restricted document store for documents; release records with their bill of materials |
| Tools | Git and its tags; Docker; Jira for changes (PA-53); CIS-CAT or an equivalent scanner (PA-80); `Test-ConfigurationManagement.ps1`; ABC Technologies' discovery tools (EV-CM-02) |
| Monitoring | Monthly drift check under PRO-CM-7, reported on TPL-8 to the security officer, and included in the monthly measures in \<Assessment, Authorization, and Monitoring Management\>, section 4.8 |
| Retention | Change records for 3 years; the 3 previous configurations, each with tag, digests, settings and bill of materials; superseded documents for 3 years |
| Disposal | Removed configurations are deleted from the library only after their retention period, with the system owner's approval |

### 4.14 What ABC Technologies provides

**Table 17: Asked of ABC Technologies**

| Provided | Controls | What \<DocuView\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Physical and logical limits on changing the hosts | CM-5 | Only authorised ABC Technologies staff can change the hosts and hosting, through its change process | EV-CM-01 | Not sent |
| Tools that detect unauthorised components, and that locate information | CM-8(3), CM-12(1) | Both servers are checked every month, and the Windows server administrator is alerted | EV-CM-02 | Not sent |
| Licences for the software on the servers and hosting, and controls on peer-to-peer software | CM-10 | Windows Server and the hosting are licensed, and peer-to-peer software is blocked | EV-CM-03 | Not sent |
| Group Policy settings on the servers | CM-6 | The corporate standard for lockout, the logon banner and the screen lock (D-AC-21) | EV-AC-05 to EV-AC-07 | Not sent |
| Jira, for the change workflow | CM-3 | A workflow built by the Application Support Team to \<DocuView\>'s design | None: tracked by PA-53 | Not built |

| **SECTION 5** |
| --- |

## 5 Each control and enhancement

The controls are in NIST order. Each has two tables. The first takes each part of the control and gives what NIST requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 5.1 CM-1 Policy and Procedures

**Table 18: CM-1 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A configuration management policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (CM): a system-level policy. Purpose and scope are in section CM.1, responsibilities in CM.5, and commitment, coordination and compliance in CM.6. It is shared with everyone who changes or administers \<DocuView\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-CM-11). Legally reviewed on 12 November 2026. Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (CM): nine procedures, PRO-CM-1 to PRO-CM-9, each naming who acts, how often and the record. Shared with the same people | Approved by the system owner (D-CM-12). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | Neil Ramsbottom is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 8 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 19: CM-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control, and each review is recorded in the change history |
| Rules and procedures | The whole policy (\<Policy\>, sections CM.3 and CM.4); all nine procedures (\<Procedures\> (CM)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; walk-through records on TPL-4; review records. The approvals exist; the rest do not yet |
| Status | Partially implemented |
| Risk decision | NC-CM-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures, and walk through each procedure |

### 5.2 CM-2 Baseline Configuration

**Table 20: CM-2 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Write down and keep a current baseline configuration of the system | Section 4.4. The baseline is what a release must contain so that it can be rebuilt exactly: the applications at a tag, each image and component at a pinned version, the settings in section 4.6, and the server build to the CIS Benchmarks | Baseline v1.0 is recorded, and the applications are tagged (C03). The images are not pinned, so the release cannot be rebuilt exactly (C01, C02; PA-77). No baseline exists for the servers, as the servers are not built (PA-54) |
| b.1 | Review and update the baseline on a schedule | Every 12 months, by the system owner and the Windows server administrator (PRO-CM-2) | Not yet due |
| b.2 | Review and update it when defined circumstances require | At each release | Done for v1.0 |
| b.3 | Review and update it when components are installed or changed | Step 6 of every change updates the baseline and the component list (PRO-CM-1) | Not yet used: no change has been made under the procedure |

**Table 21: CM-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, Windows server administrator |
| Enforced by | Release tags; pinned image versions; the monthly comparison of the servers with the baseline (PRO-CM-7) |
| Rules and procedures | Policy principle P1; rules R1, R8 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-2 (\<Procedures\> (CM)) |
| Tests | Checks C01 to C03 on the v1.0 build, 8 November 2026. C03 passed: the applications are at their tag. C01 and C02 showed the gap: the application and database images are not pinned |
| Records an assessor will ask for | The baseline record for each release; the release tags; the pinned image versions; the yearly review record; the monthly comparison results. The v1.0 record and tags exist |
| Status | Partially implemented |
| Risk decision | NC-CM-02, rated Low: obtain evidence; NC-CM-25, rated Medium: remediate (authorising official, D-CM-10) |
| Open items | PA-77: pin each image. PA-54: set the server baseline when the servers are built. PA-80: compare the servers with the baseline each month |

### 5.3 CM-2(2) Automation Support for Accuracy and Currency

**Table 22: CM-2(2) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Keep the baseline current, complete, accurate and available by automated means | Three means: release tags in the source repositories; image versions pinned by digest; and the deployment files, which state the exact configuration. A bill of materials is produced by the build at each release | Release tags are in use. Images are not pinned (PA-77), no bill of materials is produced (PA-78), and the change workflow is not set up (PA-53) |

**Table 23: CM-2(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Developers |
| Enforced by | The source repositories and the build |
| Rules and procedures | Policy principle P1; rule R8 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-2 (\<Procedures\> (CM)) |
| Tests | Checks C01 and C02, as CM-2 |
| Records an assessor will ask for | The tags; the pinned versions in the deployment files; the bill of materials for each release |
| Status | Partially implemented |
| Risk decision | NC-CM-03, rated Low: approve; NC-CM-25, rated Medium: remediate (authorising official, D-CM-10) |
| Open items | PA-53, PA-77, PA-78 |

### 5.4 CM-2(3) Retention of Previous Configurations

**Table 24: CM-2(3) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Keep a defined number of earlier baselines, so that a release can be rolled back | The 3 previous configurations are kept in the configuration library, each as its tagged applications, pinned image versions, settings and bill of materials (section 4.13) | Only v1.0 exists, so there is nothing earlier to keep yet |

**Table 25: CM-2(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Developers |
| Enforced by | The configuration library |
| Rules and procedures | Policy rule R1 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-2 (\<Procedures\> (CM)) |
| Tests | None: nothing to test until a second release exists |
| Records an assessor will ask for | The configuration library, showing the three earlier releases |
| Status | Not implemented |
| Risk decision | NC-CM-04, rated Low: approve |
| Open items | PA-53: with the change workflow. The number builds up with releases |

### 5.5 CM-2(7) Configure Systems and Components for High-risk Areas

**Table 26: CM-2(7) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Issue specially configured devices to people travelling to high-risk places | No \<DocuView\> device is issued to anyone, for travel or otherwise. \<DocuView\> is reached only from ABC Technologies' managed devices, and phones and tablets cannot reach it (\<Access Control Management\>, section 4.6.5) | Met: none is issued (D-CM-05) |
| b | Apply defined controls to the devices when the person returns | Not applicable while none is issued. If that changes, the system owner sets the configuration and the checks on return before the first device is issued | Met |

**Table 27: CM-2(7) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | No policy rule of its own (\<Policy\>, sections CM.3 and CM.4); no procedure of its own (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The decision to keep the control in scope (D-CM-05) |
| Status | Implemented |
| Risk decision | NC-CM-05, rated Low: approve; now satisfied |
| Open items | None |

### 5.6 CM-3 Configuration Change Control

**Table 28: CM-3 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Decide and record which kinds of change are under configuration control | Every change to a configuration item in section 4.3: the applications, components, images, deployment files, settings, the servers' and database's settings, and the security documents. Routine patches follow the same route | Set in this document |
| b | Review each proposed change and approve or refuse it, with security and privacy impact in mind | The change control board decides each change, on its impact analysis (sections 4.8 and 4.9). Nobody approves a change they requested or made | Not in use: the Jira change workflow is not set up (PA-53) |
| c | Record the decision on each change | On the change request, with the date and the members present | Not in use |
| d | Make the approved changes | Developers or administrators make the change through a release, and nothing else reaches the servers (section 4.7) | Changes so far are commits in the source repositories only |
| e | Keep the records of changes for a defined time | 3 years | Set. No records yet |
| f | Monitor and review the activity around controlled changes | The board reviews the month's changes, emergency changes and drift reports at each meeting. The monthly comparison with the baseline finds any change made outside the route (PRO-CM-7) | Not in use (PA-53, PA-80) |
| g | Coordinate and oversee change control through a defined body that meets on a schedule | The change control board: the system owner, the security officer and the Windows server administrator. It meets monthly, and whenever an urgent or security change needs it (section 4.8) | Chartered. It has not met |

**Table 29: CM-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, security officer, Windows server administrator |
| Enforced by | The change workflow in Jira, once built; until then form TPL-6. Only the Windows server administrators can write to the applications' program folders (\<Access Control Management\>, section 4.6.3) |
| Rules and procedures | Policy principle P2; rule R2 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1, PRO-CM-8 (\<Procedures\> (CM)) |
| Tests | None: the workflow does not exist to test |
| Records an assessor will ask for | The list of changes; each change request with its impact analysis, decision, test result and verification; the board's meeting records. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CM-06, rated Medium: remediate |
| Open items | PA-53: set up the change workflow and the release test gate. PA-91: protect the source repositories. PA-84: record schema changes |

### 5.7 CM-3(2) Testing, Validation, and Documentation of Changes

**Table 30: CM-3(2) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Test, validate and document each change before it is finished | Each change is tested on a separate test environment before release, with the security tests that apply, and the result is recorded on the change (PRO-CM-1, step 4). A release that fails a test does not go out | The security tests exist and were run on the v1.0 build. Nothing makes a release wait for them (PA-53) |

**Table 31: CM-3(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Developers |
| Enforced by | The release test gate, once built |
| Rules and procedures | Policy rule R2 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None for this control |
| Records an assessor will ask for | The test result recorded on each change; the release record |
| Status | Not implemented |
| Risk decision | NC-CM-07, rated Low: remediate |
| Open items | PA-53: set up the release test gate |

### 5.8 CM-3(4) Security and Privacy Representatives

**Table 32: CM-3(4) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Make defined security and privacy representatives members of the change control body | The security officer is a member of the board. The legal adviser joins, as privacy representative, for any change that touches personal data (section 4.8) | Met: both are named in the charter |

**Table 33: CM-3(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | The board's charter and quorum |
| Rules and procedures | Policy rule R2 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The charter; meeting records showing who attended |
| Status | Implemented |
| Risk decision | NC-CM-08, rated Low: approve; now satisfied |
| Open items | None |

### 5.9 CM-4 Impact Analyses

**Table 34: CM-4 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Analyse each change for its security and privacy impact before it is made | The security officer answers the eight questions in section 4.9 on every change, rates the impact Low, Medium or High, and records it on the change before the board decides. A High impact also needs the authorising official's agreement. A significant change goes to the authorising official (\<Assessment, Authorization, and Monitoring Management\>, section 4.9) | Defined. Not in use: no change has gone through it (PA-53) |

**Table 35: CM-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function. The board does not decide a change without its analysis |
| Rules and procedures | Policy rule R11 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The impact analysis on each change (TPL-6 or the Jira change) |
| Status | Not implemented |
| Risk decision | NC-CM-09, rated Low: approve |
| Open items | PA-53: set up the change workflow |

### 5.10 CM-4(2) Verification of Controls

**Table 36: CM-4(2) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | After a change, check that the controls it affected are still in place, working as intended and giving the result wanted | After each change, those who made it run the tests for the controls named in the impact analysis, and record the result on the change (PRO-CM-1, step 5) | Defined. Not in use (PA-53) |

**Table 37: CM-4(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers, security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R11 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The verification result on each change |
| Status | Not implemented |
| Risk decision | NC-CM-10, rated Low: approve |
| Open items | PA-53: set up the change workflow |

### 5.11 CM-5 Access Restrictions for Change

**Table 38: CM-5 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Define, record, approve and enforce the physical and logical limits on who can change the system | Section 4.11. Only developers can change the applications, in the source repositories, and each change needs a second person's review. Only the named Windows server administrators can change the servers or install a release. Only the named database administrators can change PostgreSQL. No application account can change its own program files. Each change leaves a record of who made it, in the change record and in the Windows and PostgreSQL logs. Physical access to the hosts is ABC Technologies' | Not assessable: the servers are not built. The source repositories do not yet require a review (PA-91). ABC Technologies' restrictions are not evidenced (EV-CM-01) |

**Table 39: CM-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Windows server administrator, ABC Technologies |
| Enforced by | Windows permissions on the servers; database permissions; repository permissions; ABC Technologies' physical controls |
| Rules and procedures | Policy rule R2 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None: nothing to test until the servers are built |
| Records an assessor will ask for | The list of who may change what; Windows and database permissions; repository settings; ABC Technologies' access lists and change process (EV-CM-01). The list exists in section 4.11 |
| Status | Not implemented |
| Risk decision | NC-CM-11, rated Low: obtain evidence |
| Open items | PA-112: obtain ABC Technologies' evidence (EV-CM-01). PA-91: require a review in the source repositories |

### 5.12 CM-6 Configuration Settings

**Table 40: CM-6 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Set and record configuration settings, from a defined secure standard, that are as restrictive as the work allows | Section 4.6. The CIS Benchmarks for Windows Server 2025 and PostgreSQL 18, and the settings there for the application hosting, the .NET runtime and the applications | Recorded. The applications run as Windows services (D-PL-10) |
| b | Apply the settings | The Windows server and database administrators apply the benchmarks when the servers are built, and the developers apply the hosting and application settings (PRO-CM-3) | Not applied: the servers are not built (PA-54). In the test environment the runtime settings are met (C08, C11), and PostgreSQL has TLS and logging off |
| c | Identify, record and approve each departure from the settings | Each departure is recorded on TPL-6 with its reason, and approved by the system owner | None recorded yet |
| d | Monitor and control changes to the settings | Each month the Windows server administrator scans both servers against the benchmarks, the database administrator compares the PostgreSQL settings, and any difference is reported to the security officer and put back or raised as a change (PRO-CM-7) | Not built (PA-80) |

**Table 41: CM-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Windows server and database administrators |
| Enforced by | Group Policy and the server build; PostgreSQL's settings files; each application's settings; the monthly scan |
| Rules and procedures | Policy rules R3, R10, R12 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-3, PRO-CM-7 (\<Procedures\> (CM)) |
| Tests | Checks C07 and C11 on the v1.0 build, 8 November 2026. C11 passed: the runtime runs in production mode with detailed errors off. C07 showed the gap: secrets are still in the settings files (PA-19) |
| Records an assessor will ask for | The benchmark scan results for both servers; the PostgreSQL settings; the list of approved departures; the monthly drift reports on TPL-8. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CM-12, rated Low: obtain evidence |
| Open items | PA-54: apply the benchmarks when the servers are built. PA-80: the monthly comparison |

### 5.13 CM-7 Least Functionality

**Table 42: CM-7 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Configure the system to provide only the capabilities its purpose needs | \<DocuView\> stores, searches, shows and administers documents, and nothing else (section 4.10) | Partly. The API documentation page is off outside development (B06), the database is reachable only locally (B07), and the applications do not run as root (B08) |
| b | Prohibit or restrict defined functions, ports, protocols, software and services | Table 14 in section 4.10 lists what is prohibited in each of the five kinds | Not met in part. Diagnostic, test and maintenance pages remain in the release (PA-07, PA-31). Plain HTTP is used in the test environment (PA-18). Unused packages are built in (C05, C06; PA-79), and each image holds a shell and a package manager (PA-85) |

**Table 43: CM-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Developers, Windows server administrator |
| Enforced by | The applications' build; the servers' services and firewall; ABC Technologies' network firewall |
| Rules and procedures | Policy principle P3; rule R4 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-5 (\<Procedures\> (CM)) |
| Tests | Checks C05, C06 and C08 to C10 on the v1.0 build, 8 November 2026. C08 to C10 passed. C05 and C06 showed the gap: an unused package and a development-only package are in the release |
| Records an assessor will ask for | The list of what is prohibited; the servers' open ports and running services; the list of packages in a release. The list exists; the rest wait for the servers |
| Status | Partially implemented |
| Risk decision | NC-CM-13, rated High: remediate; NC-CM-27, rated Low: remediate (system owner, Low) |
| Open items | PA-07, PA-31: remove the diagnostic, test and maintenance pages. PA-79: remove the unused packages. PA-85: use minimal images. PA-18: TLS on every route |

### 5.14 CM-7(1) Periodic Review

**Table 44: CM-7(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Review the system on a schedule, to find functions, ports, protocols, software and services that are not needed or not secure | Every 12 months the Windows server administrator and the developers review all five kinds against Table 14, and record the result on TPL-3 (PRO-CM-5) | Not yet held: the first is due 12 months after go-live (PA-110) |
| b | Disable or remove what the review finds | Anything not needed is removed through a change | Not yet used |

**Table 45: CM-7(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Windows server administrator, developers |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R4 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-5 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The yearly review record on TPL-3, and the changes raised from it |
| Status | Not implemented |
| Risk decision | NC-CM-14, rated Low: approve |
| Open items | PA-110: hold the first review |

### 5.15 CM-7(2) Prevent Program Execution

**Table 46: CM-7(2) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Prevent programs from running unless they are allowed by defined rules | The approved software list says what may run on the servers. It is not enforced by the system: the system owner decided against Windows application control (D-CM-06). Software is installed only by the named Windows server administrators, on an approved request | The risk is accepted by the authorising official for 12 months, to 6 November 2027 (NC-CM-15). The list is not yet written (PA-55) |

**Table 47: CM-7(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Windows server administrator |
| Enforced by | Not enforced by the system. Installation rights are limited to the Windows server administrators |
| Rules and procedures | Policy rule R5 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-4 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The approved software list; the acceptance of the risk (\<Risk List\>, section 4) |
| Status | Not implemented |
| Risk decision | NC-CM-15, rated Medium: accepted |
| Open items | PA-55: write the list. The acceptance is reviewed by 6 November 2027 |

### 5.16 CM-7(5) Authorized Software, Allow-by-exception

**Table 48: CM-7(5) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Identify the software allowed to run | The approved software list, kept by the Windows server administrator. For the applications themselves, the component list in section 4.5 | The component list exists. The list for the servers is not written (PA-55) |
| b | Deny everything else, and allow by exception | By procedure, not by the system: nothing is installed without an approved request (PRO-CM-4). Not technically enforced, by decision (D-CM-06) | The risk is accepted for 12 months, to 6 November 2027 (NC-CM-16) |
| c | Review and update the list on a schedule | Every 12 months | Not yet due |

**Table 49: CM-7(5) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Windows server administrator |
| Enforced by | Not enforced by the system |
| Rules and procedures | Policy rule R5 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-4 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The approved software list and its yearly review; the requests behind each entry |
| Status | Not implemented |
| Risk decision | NC-CM-16, rated Medium: accepted |
| Open items | PA-55: write the list |

### 5.17 CM-8 System Component Inventory

**Table 50: CM-8 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Keep an inventory that reflects the system accurately, includes every component, counts none twice, is detailed enough to track and report, and holds defined information | Two lists, with no overlap: the servers and other components in \<System Security Plan\>, section 4.4, and the software components in section 4.5. Each entry gives name, type, version, location and owner, and for software also the supplier and licence. A bill of materials from each build checks the software list | The software list is complete for v1.0, and matched a list written from the build (C04). It is kept by hand, with no bill of materials (PA-78). Server names, asset numbers and exact versions wait for the servers (PA-54) |
| b | Review and update the inventory on a schedule | At each change (PRO-CM-1, step 6) | Not yet used |

**Table 51: CM-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner |
| Enforced by | Step 6 of the change procedure; the bill of materials, once built |
| Rules and procedures | Policy principle P4; rule R7 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1, PRO-CM-4 (\<Procedures\> (CM)) |
| Tests | Check C04 on the v1.0 build, 8 November 2026: passed, the component list matches the build |
| Records an assessor will ask for | Both lists; the bill of materials for each release; the change that last updated each entry. The lists exist |
| Status | Partially implemented |
| Risk decision | NC-CM-17, rated Low: obtain evidence; NC-CM-26, rated Low: remediate (system owner, Low) |
| Open items | PA-54: complete the server entries. PA-78: produce a bill of materials at each release |

### 5.18 CM-8(1) Updates During Installation and Removal

**Table 52: CM-8(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Update the inventory as part of installing, removing and updating components | A change is not closed until the inventory is updated: it is step 6 of every change (PRO-CM-1) | Not in use: no change has gone through the procedure (PA-111) |

**Table 53: CM-8(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Windows server administrator |
| Enforced by | The change procedure |
| Rules and procedures | Policy rule R7 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None separate: examined with C04 |
| Records an assessor will ask for | Change records showing the inventory updated |
| Status | Not implemented |
| Risk decision | NC-CM-18, rated Low: approve; NC-CM-26, rated Low: remediate (system owner, Low) |
| Open items | PA-78: the bill of materials. PA-111: bring the update step into use with the first change |

### 5.19 CM-8(3) Automated Unauthorized Component Detection

**Table 54: CM-8(3) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Detect unauthorised hardware, software and firmware by automated means, on a schedule | ABC Technologies' discovery tools check its network, including both servers, every month | Not evidenced (EV-CM-02) |
| b | Take defined action when one is found | The tool alerts the Windows server administrator, who removes the component or disables its network access, tells the security officer, and records it on TPL-8 (PRO-CM-6) | Not yet used |

**Table 55: CM-8(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' tools |
| Rules and procedures | Policy principle P4; rule R7 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-6 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | ABC Technologies' tool names and a sample report (EV-CM-02); TPL-8 records of any detection |
| Status | Not implemented |
| Risk decision | NC-CM-19, rated Low: obtain evidence |
| Open items | PA-112: obtain ABC Technologies' evidence (EV-CM-02) |

### 5.20 CM-9 Configuration Management Plan

**Table 56: CM-9 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | A plan that covers roles, responsibilities, and configuration management processes and procedures | This document is the plan. Roles and processes are in section 4.2, the route a change follows in section 4.7, the environments in appendix C, and the procedures are \<Procedures\> (CM) | Written |
| b | It sets how configuration items are identified through the life of the system, and how their configuration is managed | Section 4.2: an item is identified when it enters the baseline, named by its component and version, and managed through the change procedure for its whole life | Written |
| c | It defines the configuration items and places them under configuration management | Section 4.3 | Written |
| d | It is reviewed and approved by defined people | The system owner | Version \<ver\> was approved (D-CM-12, D-SC-07). This restructured version awaits the system owner's approval |
| e | It is protected from unauthorised disclosure and change | It is classified Restricted and held in the restricted document store, under version control | Not yet in the restricted store: held in a private local records repository until the store is set up (PA-88) |

**Table 57: CM-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function. Version control records every change to the plan |
| Rules and procedures | The whole policy (\<Policy\>, sections CM.3 and CM.4); all nine procedures (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | This document with its approval; its change history; where it is held and who can reach it |
| Status | Partially implemented |
| Risk decision | NC-CM-20, rated Low: approve |
| Open items | PA-88: move the document set to the restricted store. The plan is not yet in use, as no change has gone through it (PA-53) |

### 5.21 CM-10 Software Usage Restrictions

**Table 58: CM-10 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Use software and its documentation within its contracts and copyright law | Every component's licence is recorded in section 4.5 before it enters the baseline, and must permit \<DocuView\>'s use. A licence that is not a standard open source licence goes to the system owner for a recorded decision. Licences are checked again at each release and every 12 months (PRO-CM-9) | All 16 components are recorded with their licences. One needed a decision: ImageSharp, used under its free community licence (D-CM-09). One internal component's owner and licence are to be confirmed. ABC Technologies' licences for Windows Server and the hosting are not evidenced (EV-CM-03) |
| b | Track software licensed by quantity, to control copying and distribution | \<DocuView\>'s own components are not licensed by quantity. Windows Server and anything else licensed by quantity is ABC Technologies', and is tracked in its licence record | Not evidenced (EV-CM-03) |
| c | Control and record any use of peer-to-peer file sharing | None is allowed: no peer-to-peer software is on the approved list, and ABC Technologies' network controls apply | ABC Technologies' controls are not evidenced (EV-CM-03) |

**Table 59: CM-10 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, ABC Technologies |
| Enforced by | The component approval step (PRO-CM-4); ABC Technologies' licence management |
| Rules and procedures | Policy rule R9 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-9 (\<Procedures\> (CM)) |
| Tests | Check C04, which lists every component with its licence |
| Records an assessor will ask for | The component list with licences; the licence decisions in \<Decision Register\>; ABC Technologies' licence record and policy (EV-CM-03). The first two exist |
| Status | Not implemented |
| Risk decision | NC-CM-21, rated Low: obtain evidence |
| Open items | PA-112: obtain ABC Technologies' licence record (EV-CM-03). PA-113: record the owner and licence of the internal access control component |

### 5.22 CM-11 User-installed Software

**Table 60: CM-11 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Set the rules for users installing software | Nobody may install software on the servers without approval. A person who needs software there raises a request, and the system owner approves or refuses it (D-CM-07). ABC Technologies' policy governs users' own devices | Set |
| b | Enforce the rules by defined means | The approval in Jira, and Windows user rights: only the named Windows server administrators can install | Not assessable: the servers are not built |
| c | Check compliance on a schedule | Every 12 months, with the functions review: what is installed is compared with the approved software list | Not yet due (PA-110) |

**Table 61: CM-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, Windows server administrator |
| Enforced by | Windows user rights on the servers; the approval workflow |
| Rules and procedures | Policy rule R6 (\<Policy\>, sections CM.3 and CM.4); PRO-CM-4 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The approved requests; the yearly comparison of installed software with the list |
| Status | Not implemented |
| Risk decision | NC-CM-22, rated Low: approve |
| Open items | PA-110: hold the first yearly check. PA-55: write the list |

### 5.23 CM-12 Information Location

**Table 62: CM-12 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Identify and record where defined information is, and the components that process and store it | Documents and audit records are held in PostgreSQL on the database server, with each project in its own schema. The application server holds only working files: export output for up to 24 hours, each application's key ring, and logs. Backups go to ABC Technologies' backup site. \<System Security Plan\>, sections 4.4 and 5.4, hold the record | Recorded |
| b | Identify and record who has access to the system and components where it is held | The approved access list: the members of each of \<DocuView\>'s AD groups, the named Windows server and database administrators, and ABC Technologies' staff with access to the hosts and backups | Not built: the first list is to be made before any production documents are held (D-AC-14; PA-111) |
| c | Record changes to where the information is held | A change of location is a change to the baseline, and a new site is a significant change. Each is recorded on the change and in \<System Security Plan\> | Not yet used |

**Table 63: CM-12 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | No policy rule of its own (\<Policy\>, sections CM.3 and CM.4); PRO-CM-1 (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | The record of locations; the approved access list; change records for any move. The record of locations exists |
| Status | Partially implemented |
| Risk decision | NC-CM-23, rated Low: approve |
| Open items | PA-111: build the approved access list |

### 5.24 CM-12(1) Automated Tools to Support Information Location

**Table 64: CM-12(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Use automated tools to find defined information on defined components | Restricted documents are held by project in the database, so the database itself lists them. For anything outside it, ABC Technologies' tools are to scan both servers for stray copies, if it has such tools | The value is agreed. The tools are not confirmed (EV-CM-02) |

**Table 65: CM-12(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' tools, if confirmed |
| Rules and procedures | No policy rule of its own (\<Policy\>, sections CM.3 and CM.4); no procedure of its own (\<Procedures\> (CM)) |
| Tests | None |
| Records an assessor will ask for | ABC Technologies' tool name and a sample report (EV-CM-02) |
| Status | Not implemented |
| Risk decision | NC-CM-24, rated Low: approve |
| Open items | PA-112: confirm the tools with ABC Technologies (EV-CM-02) |

| **APPENDIX A** |
| --- |

## Appendix A How configuration was built in the tested build

This records the position of the build labelled v1.0 when it was examined and tested in Docker on 6 and 8 November 2026. It is the basis of the Today columns.

**Table 66: How configuration was built in the tested build**

| Part | What happens today | Where |
| --- | --- | --- |
| Baseline | Code and Docker files tagged v1.0. No baseline for the VMs, which are not built | DV\_Workspace |
| Change control | Git commits only. Jira is planned | PA-53 |
| Least functionality | The API documentation page is off outside development (B06), the database is local only (B07), and the application does not run as root (B08). Diagnostic and maintenance pages remain | PA-07, PA-31 |
| Software list | Not yet written, and not technically enforced, by decision | PA-55 |
| Inventory | Servers in \<System Security Plan\>, section 4.4; software components in section 4.5 (C04) | PA-54 |

| **APPENDIX B** |
| --- |

## Appendix B Parameter register

These are NIST's organisation-defined values for the 24 CM entries: 57 in total. State now says whether each value is met today. Forty-six were agreed in the meeting of 6 November 2026, and the other 11 by the system owner later the same day (D-CM-P01, D-CM-P02). Four were extended on 8 November 2026 (D-CM-08).

**Table 67: CM parameter register**

| NIST identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| CM-01\_ODP\[01\] | Who receives the policy | Everyone who changes or administers \<DocuView\> | Not yet: shared when issued (PA-20) |
| CM-01\_ODP\[02\] | Who receives the procedures | Everyone who changes or administers \<DocuView\> | Not yet: shared when issued (PA-20) |
| CM-01\_ODP\[03\] | Level of the policy | System level | Met |
| CM-01\_ODP\[04\] | Official who manages them | System owner | Met |
| CM-01\_ODP\[05\] | Policy review frequency | Every 12 months | Met: set |
| CM-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: reviewed on 8 November 2026 |
| CM-01\_ODP\[07\] | Procedures review frequency | Every 12 months | Met: set |
| CM-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: reviewed on 8 November 2026 |
| CM-02\_ODP\[01\] | Baseline review frequency | Every 12 months | Not yet due |
| CM-02\_ODP\[02\] | Circumstances | Each release | Partly: v1.0 is tagged, but images are not pinned (C01, C02; PA-77) |
| CM-02(02)\_ODP | Automated mechanisms | Git tags, pinned image digests and the deployment files | Partly: Git tags yes; digests not pinned (PA-77) |
| CM-02(03)\_ODP | Previous versions kept | 3 | Not yet: only v1.0 exists |
| CM-02(07)\_ODP\[01\] | Systems issued for travel | None; no \<DocuView\> device is issued for travel | Met |
| CM-02(07)\_ODP\[02\] | Configurations | Not applicable while none is issued | Met |
| CM-02(07)\_ODP\[03\] | Controls on return | Not applicable while none is issued | Met |
| CM-03\_ODP\[01\] | Record retention | 3 years | Met: set |
| CM-03\_ODP\[02\] | Change control element | System owner, security officer and Windows server administrator | Met: chartered in section 4.8 |
| CM-03\_ODP\[03\] | How it convenes | At a set frequency, and when a change needs it | Met: set |
| CM-03\_ODP\[04\] | Frequency | Monthly | Not yet: the board starts with the Jira workflow (PA-53) |
| CM-03\_ODP\[05\] | Conditions | An urgent or security change | Met: set |
| CM-03(04)\_ODP\[01\] | Security representative | Security officer | Met |
| CM-03(04)\_ODP\[02\] | Privacy representative | Legal adviser | Met |
| CM-03(04)\_ODP\[03\] | Element | As CM-03\_ODP\[02\] | Met |
| CM-06\_ODP\[01\] | Secure configurations | CIS Benchmarks, and the settings for the hosting and applications in section 4.6 | Not assessable: VMs not built (PA-54) |
| CM-06\_ODP\[02\] | Components | Windows Server 2025, PostgreSQL 18, the application hosting and the three applications | Not assessable: VMs not built (PA-54) |
| CM-06\_ODP\[03\] | Operational requirements | Recorded exceptions | Met: set |
| CM-07\_ODP\[01\] | Capabilities | Storing, searching and viewing documents, and administering them | Met |
| CM-07\_ODP\[02\] | Functions prohibited | Diagnostic, test and maintenance pages in production | Not met: they remain (PA-07, PA-31) |
| CM-07\_ODP\[03\] | Ports | Everything except HTTPS to the application, the database from the application VM, and administration from ABC Technologies' network | Partly: database local in Docker (C09); VMs not built |
| CM-07\_ODP\[04\] | Protocols | Everything except TLS-protected ones on those routes | Not met: plain HTTP in Docker (PA-18) |
| CM-07\_ODP\[05\] | Software | Anything not on the approved list | Not met: unused packages in release builds (C05, C06; PA-79) |
| CM-07\_ODP\[06\] | Services | Anything not needed for those capabilities | Not assessable: VMs not built |
| CM-07(01)\_ODP\[01\] | Review frequency | Every 12 months | Not yet due |
| CM-07(01)\_ODP\[02\] | Functions | As CM-07\_ODP\[02\] | Met: set |
| CM-07(01)\_ODP\[03\] | Ports | As CM-07\_ODP\[03\] | Met: set |
| CM-07(01)\_ODP\[04\] | Protocols | As CM-07\_ODP\[04\] | Met: set |
| CM-07(01)\_ODP\[05\] | Software | As CM-07\_ODP\[05\] | Met: set |
| CM-07(01)\_ODP\[06\] | Services | As CM-07\_ODP\[06\] | Met: set |
| CM-07(02)\_ODP\[01\] | Prevention rule | Authorised software rules | Accepted risk: not technically enforced (NC-CM-15) |
| CM-07(02)\_ODP\[02\] | Rules | The approved software list | Accepted risk: not technically enforced (NC-CM-15) |
| CM-07(05)\_ODP\[01\] | Authorised software | The approved software list | Not yet: list to be written when the VMs are built (PA-55) |
| CM-07(05)\_ODP\[02\] | Review frequency | Every 12 months | Met: set |
| CM-08\_ODP\[01\] | Inventory information | Name, type, version, location and owner; for software, also supplier and licence | Partly: software components in section 4.5 (C04); servers when built |
| CM-08\_ODP\[02\] | Review frequency | At each change | Met: set; PRO-CM-1 |
| CM-08(03)\_ODP\[01\] | Mechanism, hardware | ABC Technologies' tools | Not assessable: ABC Technologies (EV-CM-02) |
| CM-08(03)\_ODP\[02\] | Mechanism, software | ABC Technologies' tools | Not assessable: ABC Technologies (EV-CM-02) |
| CM-08(03)\_ODP\[03\] | Mechanism, firmware | ABC Technologies' tools | Not assessable: ABC Technologies (EV-CM-02) |
| CM-08(03)\_ODP\[04\] | Frequency | Monthly | Not assessable: ABC Technologies (EV-CM-02) |
| CM-08(03)\_ODP\[05\] | Action | Disable network access, and tell the person below | Met: set; PRO-CM-6 |
| CM-08(03)\_ODP\[06\] | Who is told | Windows server administrator | Met: set |
| CM-09\_ODP | Who approves the plan | System owner | Met: version \<ver\> approved |
| CM-11\_ODP\[01\] | Installation policy | Allowed on the VMs only with approval; ABC Technologies' policy covers workstations | Met: set |
| CM-11\_ODP\[02\] | Enforcement | Jira approval; Windows user rights | Not assessable: VMs not built |
| CM-11\_ODP\[03\] | Compliance monitoring | Every 12 months, with the functions review | Not yet due |
| CM-12\_ODP | Information | Documents and audit records | Met. Revised on 13 November 2026: \<DocuView\> holds no accounts, which are in Active Directory (D-CM-14) |
| CM-12(01)\_ODP\[01\] | Information by type | Restricted documents, by project | Met |
| CM-12(01)\_ODP\[02\] | Components | Both VMs, using ABC Technologies' tools if available | Not yet: tools to be confirmed (EV-CM-02) |

| **APPENDIX C** |
| --- |

## Appendix C Environments

NIST's guidance on CM-9 asks the plan to say how the development, test and operational environments are controlled. \<DocuView\> has three, and nothing moves from one to the next except as a tagged release.

**Table 68: Environments**

| Environment | What it is | What it may hold | Who may change it | Today |
| --- | --- | --- | --- | --- |
| Development | The developers' PCs, and the source repositories | Sample data only. Never production documents or production secrets | Developers, each change reviewed by a second developer | In use. Reviews are not yet required by the repositories (PA-91) |
| Test | A separate, throwaway copy of the whole system, built from a tagged release and removed after each test run | Sample data only | Developers | In use for every test recorded in the evidence store. It runs in Docker on one PC, not on servers like the production ones |
| Production | The application server and the database server at ABC Technologies | Production documents, once \<DocuView\> is authorised | The named Windows server and database administrators only, installing an approved release | Not built |

A release is tested in the test environment before it reaches production (section 4.7, step 4). NIST asks for a separate test environment only at High, as CM-4(1); \<DocuView\> has one already. The tests are to be repeated on the production servers once they are built, because the test environment differs from them.

| **APPENDIX D** |
| --- |

## Appendix D CM controls outside the Moderate baseline

NIST does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 69 says where.

**Table 69: CM controls not selected at Moderate**

| Control | What it adds | \<DocuView\>'s position |
| --- | --- | --- |
| CM-3(1) Automated Documentation, Notification, and Prohibition of Changes | A workflow that records each change, tells the approvers, and blocks a change until approved | Not required. Done in part once the Jira workflow is built (PA-53) |
| CM-3(6) Cryptography Management | Cryptographic mechanisms under configuration management | Not required. Keys and certificates are in the key register (\<Control Implementation Register\>, section SC.3), and a new key or certificate goes through change control |
| CM-4(1) Separate Test Environments | Changes analysed in a separate test environment | Not required. Done: appendix C |
| CM-5(1) Automated Access Enforcement and Audit Records | Automated enforcement of who may change the system, with audit records | Not required. Done in part: Windows and database permissions enforce it, and their logs record it |
| CM-6(1), CM-6(2) Automated Management and Verification; Respond to Unauthorized Changes | Automated checking of settings, and a set response to an unauthorised change | Not required. Done in part in design: the monthly benchmark scan, and the drift procedure (PA-80) |
| CM-7(4) Unauthorized Software, Deny-by-exception | A list of software that must not run | Not required. \<DocuView\> uses the stricter alternative, CM-7(5), an approved list, though it is not enforced by the system |
| CM-8(2), CM-8(4) Automated Maintenance; Accountability Information | An inventory kept by automated means, naming who is accountable for each component | Not required. Each entry names an owner. The bill of materials will keep the software list by automated means (PA-78) |
| CM-13 Data Action Mapping | A map of what the system does with personal data | In no security baseline. The personal data inventory is in \<Control Implementation Register\>, section PT.3 |
| CM-14 Signed Components | Components installed only if signed with an approved certificate | In no baseline. Release tags are to be signed, and packages checked for their signature (PA-91, PA-94) |
