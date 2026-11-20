# \<System Name\> System and Services Acquisition Management

## 1 Purpose

This document shows how \<System Name\> is built and bought securely, for each of the 17 System and Services Acquisition (SA) controls in the CSS Moderate baseline: the lifecycle and resources, contracts, documentation, engineering principles, external services, developer configuration management and testing, the development process, criticality analysis and unsupported components.

Section 3 sets out the design: the development framework; the lifecycle, roles and resources; contracts and design information; documentation; engineering principles; external services; configuration management; the developer test plan; the process, standards and tools; criticality analysis; unsupported components; how \<System Name\> is built today; and what \<Organisation\> and the providers supply. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define, and appendix B the related controls and enhancements CSS does not select at Moderate.

The policy is in \<Policy\> (SA), and the steps people follow are in \<Procedures\> (SA). Four records sit beside this one, each holding what CSS asks the system's own documents to hold: the engineering principles in \<Security Architecture\>, section 6.5; the functions, ports, protocols and services in \<System Security Plan\>, section 3.7; the critical components in \<Risk Assessment Management\>, section 3.9; and the component support dates in \<Maintenance Management\>, section 3.8.

\<System Name\> is built in-house, so its developers carry most of these duties. What is bought is \<Organisation\>'s hosting and services, and the outside services the developers use.

An assessor examines the framework, the contracts, the guides, the external services, the repository settings and the test evidence; interviews the developers, the system owner and \<Organisation\>'s contract owner; and tests the repositories and the build (CSS). So for each control section 4 gives:

- **each part of the control**, as CSS letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |
| Not applicable | The control does not apply, by a recorded decision |

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded once, in \<System Security Plan\>, section 7.16 (Table 25). This section gives only the overall position.

No control in the Moderate baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

Two things matter most. Nothing stops an unreviewed change reaching a release: no repository protects its default branch or requires a review, and the v1.0 release had no reviewed merge or signed tag (PA-91, rated Medium). And nothing tests a release automatically: there is no build pipeline or unit test, and the build turns the package audit off (PA-68 and PA-92, rated Medium). The authorising official decided that the change workflow and the pipeline must be in place before production (D-SA-14).

## 3 The design

### 3.1 Principles

1. **A named framework.** Development follows CSS \<ver\>, practice by practice.
2. **Known changes only.** Only reviewed and approved changes reach a release.
3. **Test before release.** Every security function is tested at each release, to a stated depth.
4. **Know what you depend on.** Every third-party component and external service is known, assessed and supported.

These carry out the principles and rules of \<Policy\>, sections SA.3 and SA.4.

![Figure 1: How \<System Name\> is built and bought](figures/sam-figure-1.png)

**Figure 1: How \<System Name\> is built and bought**

### 3.2 Development framework

\<System Name\> is developed under CSS \<ver\> (CSS, February 2022). Version \<ver\> is in draft (CSS, December 2025), and is adopted when final. The table gives each of the 19 practices, how \<System Name\> meets it, and the gap where it does not. The UK Software Security Code of Practice's principles 1.1 to 3.5 align with these practices. Its fourth theme, communication with customers, is for software that is sold, which \<System Name\> is not.

**Table 2: CSS practices**

| Practice | How \<System Name\> meets it | Gap |
| --- | --- | --- |
| PO.1 Define security requirements | CSS Moderate and the privacy baseline; family policies; \<System Security Plan\> | None |
| PO.2 Roles and responsibilities | \<Roles and Responsibilities\>; \<Policy\>, section SA.5; the stages in section 3.3 | Module M5, secure development, is not yet written or given (PA-97) |
| PO.3 Supporting toolchains | Tools in section 3.10 | No pipeline (PA-68); package audit off (PA-92) |
| PO.4 Criteria for security checks | Test plan in section 3.9; ASVS 5.0 Level 2 | ASVS not yet assessed |
| PO.5 Secure development environments | Private repositories; offline package feed | No branch protection (PA-91) |
| PS.1 Protect all code | Git on private GitHub repositories | No required review, alerts or protection (PA-91) |
| PS.2 Verify release integrity | Checksums planned at each release | Tags not signed (PA-91); checksums not yet made (PA-61) |
| PS.3 Archive each release | Git tags, starting with v1.0 | No bill of materials (PA-78) |
| PW.1 Design to meet requirements | Security approach and principles in \<Security Architecture\>, section 6 | None |
| PW.2 Review the design | Security officer checks significant designs (PRO-SA-1) | Not yet in routine use |
| PW.4 Reuse well-secured software | Sign-in through \<Organisation\>'s AD FS; ASP.NET Core data protection; the access-control toolkit | Two packages with advisories (PA-56) |
| PW.5 Secure coding practices | .NET defaults; parameterised queries | Raw SQL in the admin portal (PA-89); no written coding standard |
| PW.6 Secure build settings | Release builds | Package audit off (PA-92); floating base images (PA-77) |
| PW.7 Review code | Second developer reviews each change (PRO-SA-1) | One author, no reviewed merges (PA-91); no static analysis (PA-92) |
| PW.8 Test executable code | Fifteen test scripts (section 3.9) | No unit tests or pipeline (PA-68) |
| PW.9 Secure defaults | Deny by default; lock and sign-out times set | Admin portal on every interface in Docker (PA-83) |
| RV.1 Identify vulnerabilities | Test-Vulnerability.ps1; CISA's exploited list weekly (SyOps C50) | No scanner for the images, the VMs or the applications (PA-62) |
| RV.2 Assess and fix vulnerabilities | Timetable in \<Risk Assessment Management\>, section 3.6 | 7 advisories open (PA-56) |
| RV.3 Find root causes | Lessons in incident records (TPL-10) and risk reviews (TPL-23) | Not yet practised |

### 3.3 Lifecycle, roles and resources

\<System Name\> goes through six stages, each with its security and privacy check (D-SA-05). The check at each stage, and the separate budget line, were confirmed by the system owner on 18 November 2026 (D-SA-20). The roles are in \<Roles and Responsibilities\>, and the privacy roles in \<Privacy Plan\>, section 3.

**Table 3: Lifecycle stages**

| Stage | Security and privacy check | Who | Record |
| --- | --- | --- | --- |
| 1 Plan | The change's security and privacy effect is noted, including whether it affects personal data | Developers | TPL-6 |
| 2 Design | The security officer checks each significant design against the principles (section 3.6). The critical components are updated at each major change | Security officer, developers | TPL-6; \<Risk Assessment Management\>, section 3.9 |
| 3 Build | Another developer reviews each change before it merges. A new third-party component is checked first (PRO-SA-7) | Developers | The merge review; TPL-6 |
| 4 Test | The developer test plan runs at each release (section 3.9) | Developers, security officer | Results and manifest |
| 5 Release | The release goes through change control, with the guides confirmed, a signed tag and recorded checksums | Developers, system owner | TPL-6; the release tag |
| 6 Retire | A component is replaced before its support ends (section 3.12). When \<System Name\> itself is retired, its documents and media are disposed of as \<Media Protection Management\> and \<PII Processing Management\> set out | Developers, system owner | TPL-7; disposal records |

**Resources.** Every 12 months the system owner raises the cost of security and privacy in \<Organisation\>'s yearly budgeting, as a separate line in \<System Name\>'s budget request, and records it on TPL-23 (PRO-SA-6). It has not yet been raised.

### 3.4 Contracts and design information

\<System Name\>'s software is written in-house. What is bought, now or later, uses \<Organisation\>'s standard contract, with security and privacy terms added for each of the nine things SA-4 asks a contract to hold: the functional requirements, the strength of mechanisms, assurance, the controls, documentation and its protection, the development and operating environments, who is responsible for security, privacy and supply chain risk, and acceptance criteria (D-SA-06; PRO-SA-3). Section 4.4 sets out each; the system owner confirmed them on 18 November 2026 (D-SA-20). The contract also states how and when the supplier gives notice of support, maintenance and updates, as the CSS guidance on SA-4 suggests. \<Organisation\>'s contract has not been seen (EV-SA-01).

As the developer, \<System Name\>'s team provides the design information CSS asks for:

1. **What each control does** (SA-4(1)): each family's design document, and the security plan, section 7.
2. **How the controls are designed** (SA-4(2)): the security-relevant external interfaces and the high-level design in \<Security Architecture\> and the security plan, sections 3 and 4, and how each security function is built, in the family design documents.
3. **The functions, ports, protocols and services in use** (SA-4(9)): the security plan, section 3.7, and the allowed flows in \<Access Control Management\>, section 3.6.

PIV products (SA-4(10)) are not applicable, as \<System Name\> does not use United States government identity cards (TR-SA-01).

### 3.5 Documentation

Two guides are kept with the code: the Administrator Guide (\<Administrator Guide\>), on secure installation, configuration and operation, the security and privacy functions, and known weaknesses in privileged functions; and the User Guide (\<User Guide\>), on signing in, using \<System Name\> securely, personal data and users' responsibilities. They are drafts until the developers confirm them against \<System Name\> (PA-69), and are confirmed again at each release (PRO-SA-4). They go to administrators, the security officer and users. A supplier document that is missing is recorded and chased (D-SA-07).

### 3.6 Engineering principles

The NCSC secure design principles and the CSS privacy engineering objectives are mapped to \<System Name\>'s specification and design in \<Security Architecture\>, section 6.5, which holds them (D-SA-08). The security officer checks each significant design against them (PRO-SA-1). Work before 11 November 2026 was not checked against them; each change is from now on.

### 3.7 External services

These are the services in SA-09(02)\_ODP. Each states its controls in its contract or service terms, and the system owner reviews each every 12 months on TPL-16 (PRO-SA-3). The rows for AD FS and Active Directory, and for the Starters/Leavers system, were added on 18 November 2026, as \<System Name\> now relies on them for sign-in and access (D-AC-22, D-AC-23). The system owner confirmed them the same day (D-SA-20). The Docker Hub row was added by the SA cross-check, as the test stacks take their database image from it.

**Table 4: External services**

| Service | Provider | What it holds or does for \<System Name\> | Basis of trust | Evidence |
| --- | --- | --- | --- | --- |
| Hosting, network and hardware | \<Organisation\> | Runs the two VMs and their network | \<Organisation\>'s service agreement, and its Cyber Essentials Plus certificate | EV-SA-02 |
| ServiceNow | \<Organisation\> | Change, access and incident workflows | \<Organisation\>'s service agreement | EV-SA-02 |
| AD FS and Active Directory | \<Organisation\> | Authenticate every user with multi-factor authentication, and hold the groups that decide each role and each project's access (D-AC-23) | \<Organisation\>'s agreement covering AD FS (EV-CA-02) | EV-CA-02, EV-SA-02 |
| Starters/Leavers system | \<Organisation\> | Raises a leaver request automatically when someone leaves (D-AC-22) | \<Organisation\>'s service agreement | EV-SA-02 |
| Source code hosting | GitHub | Holds all source code, history and release tags | GitHub's published terms and security reports for the account's plan (EV-SA-03) | EV-SA-03 |
| Package registry | nuget.org directly; only the in-house OfflineModules packages come through the offline feed (PA-94) | Supplies .NET packages | Package signatures, and the check made before a package is used (PRO-SA-7). No agreement | Package checks (V01) |
| Container registry | Microsoft Container Registry | Supplies the .NET base images for the build and the test stacks | Microsoft's published images and terms. No agreement | Image checks (V03, V04) |
| Image registry | Docker Hub | Supplies the PostgreSQL image for the test stacks | The official image's publisher. No agreement | Image checks (V03) |
| Browser library CDN | jsDelivr | Serves bootstrap-icons and openseadragon to browsers, until served by \<System Name\> (PA-34) | None: a public service with no agreement, which is why \<System Name\> is to serve these files itself (PA-34) | None |

**Trust and service levels.** Each row says what \<System Name\>'s trust in the service rests on, as CSS asks (SA-9). For \<Organisation\>'s services, the agreement should state the service levels, how they are measured, and the remedies when they are missed; these are asked for with EV-SA-02. The public services offer none, so \<System Name\> relies on its own checks of what they supply. The authorising official keeps the risk of each external service.

### 3.8 Developer configuration management

1. **What is controlled.** Code, configuration, documents and test scripts, during development, implementation and operation.
2. **Where.** In Git, in six private repositories on GitHub, each with one default branch name.
3. **How a change gets in.** On a branch, reviewed and approved by another developer before it merges into the protected default branch.
4. **Releases.** Each release is tagged, the tag is signed, and its checksums are recorded (PA-61).
5. **Alerts.** Dependency alerts and secret scanning are on.
6. **Deployment.** Only an approved release is deployed, through change control (\<Configuration Management\>).
7. **Flaws.** Each security flaw is tracked in the Risk List and the POA&M, and reported to the system owner and the security officer.

Today items 2 to 5 are not in place (S01 to S05; PA-91), and the change workflow is not set up (PA-53).

### 3.9 Developer test plan

This is the developer security and privacy test plan (SA-11). Each script runs on a separate test stack or only reads, keeps its results with a README and a manifest of SHA-256 hashes in the evidence for its family, and is run at each release until a pipeline runs them (PA-68). The web applications are to be verified to OWASP ASVS 5.0 Level 2.

The sign-in and access checks ran on the v1.0 build, which used \<System Name\>'s own passwords and groups. They are to be run again with sign-in through AD FS and access by Active Directory groups (D-AC-23; PA-95).

The scripts are one kind of analysis among several that the CSS guidance expects for software written in-house. Table 5 says when each is done, and where it stands.

**Table 5: Kinds of analysis**

| Kind | What | When | Today |
| --- | --- | --- | --- |
| Scripted security tests | The 15 scripts in the table below | Each release | In use, run by hand |
| Unit and integration tests | Run by a build pipeline | Each build | Not built (PA-68) |
| Manual code review | Another developer reviews each change before it merges (PRO-SA-1) | Each change | Not enforced (PA-91) |
| Static analysis | The .NET analysers or CodeQL, in the pipeline | Each build | Not built (PA-92) |
| Dynamic analysis | A web application scan of the three applications (\<Risk Assessment Management\>, section 3.5) | Each release | Not built (PA-62) |
| Verification to OWASP ASVS 5.0 Level 2 | The web applications checked against each Level 2 requirement, with the result recorded | Before go-live, then at each major release | Not done (PA-68) |
| Penetration test | By a tester independent of the build | Before go-live | Not commissioned (PA-109) |

The plan, its results and the evidence are protected as the document set is: restricted, and held in the restricted store once the set moves there (PA-88).

**Table 6: Developer test plan**

| Script | Checks | Security functions covered | Evidence kept with |
| --- | --- | --- | --- |
| Test-AccessControl.ps1 | T01 to T55 | Project access, roles, sessions and anonymous endpoints | The AC evidence |
| Test-AuditAndAuth.ps1 | A01 to A38 | Audit records, and sign-in as built at v1.0 | The AU and IA evidence |
| Test-Identification.ps1 | I01 to I11 | Identifiers and authenticators, as built at v1.0 | The AU and IA evidence |
| Test-ConfigurationManagement.ps1 | C01 to C11 | The baseline, images and settings | The CM evidence |
| Test-Protection.ps1 | N01 to N12 | Encryption in transit, security headers and cookies, keys and secrets, and request limits | The SC evidence |
| Test-IncidentReadiness.ps1 | D01 to D08 | Ending sessions, clocks, and the logs an incident needs | The IR evidence |
| Test-BackupRestore.ps1 | R01 to R09 | Backup and restore | The CP evidence |
| Test-Maintenance.ps1 | M01 to M12 | Maintenance pages and tools | The MA evidence |
| Test-MediaProtection.ps1 | P01 to P09 | Exports and marking | The MP evidence |
| Test-PersonalData.ps1 | Q01 to Q10 | How personal data is held, logged and kept | The PT evidence |
| Test-Integrity.ps1 | H01 to H12 | Upload checks, error handling, checksums, the audit chain and alerts | The SI evidence |
| Test-Vulnerability.ps1 | V01 to V09 | Packages, images and the risk records | The RA evidence |
| Test-SupplyChain.ps1 | U01 to U10 | Package sources, lock files, signatures, image pins, the bill of materials and suppliers | The SR evidence |
| Test-Development.ps1 | S01 to S10 | Repositories, the build and component support | The SA evidence |
| Test-PlanConsistency.ps1 | L01 to L24 | The consistency of the document set | The PL evidence |

### 3.10 Development process, standards and tools

The process is CSS \<ver\> (section 3.2). The standards are CSS, OWASP ASVS 5.0 Level 2 for the web applications, the NCSC secure design principles and the CSS privacy engineering objectives, with the UK Software Security Code of Practice alongside. Every 12 months the developers and the security officer review the process, standards and tools against the acquisition policy and the personal data policy, and record the review and any change on TPL-23 (PRO-SA-6).

**Table 7: Development tools**

| Tool | Version or setting | Configuration that matters for security |
| --- | --- | --- |
| .NET SDK and ASP.NET Core | 10.0, long-term support | Release builds. The package audit is turned off in the image build (PA-92) |
| Docker | Desktop on the developer PC, for the build and the test stacks | The .NET SDK and runtime base images, not pinned (PA-77). In production each application runs as a Windows service on the application server, not in a container (D-PL-10) |
| Git and GitHub | Private repositories under one account | No branch protection, required review or alerts (PA-91) |
| Offline NuGet feed | The in-house offline package repository | Packages are checked before they enter the feed (\<Supply Chain Risk Management\>). Only the in-house OfflineModules packages come through it today (PA-94) |
| PowerShell 7 | Runs the test scripts | Run by hand. 10 scripts were not under version control (PA-91) |
| GitHub CLI | Used by Test-Development.ps1 | Read-only calls to GitHub |

### 3.11 Criticality analysis

The criticality analysis (SA-15(3)) is held in \<Risk Assessment Management\>, section 3.9, with its method, the critical components and the critical functions. It is done at design and at each major change, across every component. The developers update it under PRO-SA-1 and PRO-RA-6.

### 3.12 Unsupported components

Each component is replaced before its vendor's support ends, with the replacement planned at least 6 months before (D-SA-13). The monthly check compares each component with its support dates, which are held in \<Maintenance Management\>, section 3.8 (PRO-SA-5; \<Security Operating Procedures\>, C11). A package or browser library has no vendor support date. It counts as unsupported when its maintainers stop releasing fixes, or it is marked deprecated, or it has a known flaw with no fix. The developers check each one in the monthly package check; this is not yet in use (PA-128). If a component cannot be replaced in time, the other support allowed is in-house support, or a supplier's extended support by exception approved by the authorising official.

### 3.13 How \<System Name\> is built today

Test-Development.ps1 ran on 11 November 2026. Its results, with their hashes, are kept with the SA evidence.

- **Repositories:** none of the six repositories protects its default branch, needs a review or alerts on vulnerable dependencies (S01, S02). Three name their default branch main and three master (S03). All six are private (S04).
- **Releases:** the v1.0 release of each application was 9 or 10 commits by one author, with no reviewed merge and no signed tag (S05).
- **Build and tests:** the image build and two toolkit projects turn NuGet's audit off (S06). 10 of the then 12 test scripts were not in Git (S07), and the applications have no unit tests (S08).
- **Components and guides:** no component is within 6 months of the end of its support (S09). The administrator and user guides exist only as drafts (S10).

### 3.14 What \<Organisation\> and the providers supply

**Table 8: Asked of \<Organisation\> and the providers**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| The standard contract, with security and privacy terms | SA-4 | Its terms cover the nine things in section 4.4 | EV-SA-01 | Not sent |
| Hosting, network, ServiceNow, AD FS, Active Directory and the Starters/Leavers system | SA-9, SA-9(2) | Each states its controls, and the functions, ports, protocols and services it needs | EV-SA-02; EV-CA-02 for the AD FS agreement | Not sent |
| GitHub | SA-9, SA-9(2), SA-10 | Its controls for private repositories, and the plan and settings of \<System Name\>'s account | EV-SA-03 | Not sent |

**Today:** no request has been sent, and none of this is evidenced.

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 SA-1 Policy and Procedures

**Table 9: SA-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | An acquisition policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (SA): a system-level policy, shared with developers and administrators. The legal adviser reviewed it on 11 November 2026 | Version \<ver\> approved by the Head of Cyber (D-SA-01). The later version awaits the Head of Cyber (D-SA-16). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (SA): seven procedures, PRO-SA-1 to PRO-SA-7. Shared with the same people | Version \<ver\> approved by the system owner (D-SA-18). Not yet shared |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 11 November 2026 after the SA pack review. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | Reviewed and approved as version \<ver\> on 11 November 2026. The first yearly review falls due in November 2027 |

**Table 10: SA-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy; all seven procedures (\<Procedures\>) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-SA-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-SA-16) |

### 4.2 SA-2 Allocation of Resources

**Table 11: SA-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Determine the high-level security and privacy requirements in business process planning | The Moderate baseline and the CSS privacy baseline, chosen from the categorisation, with the privacy plan (\<Planning Management\>, section 3.7; \<Privacy Plan\>) | Done |
| b | Determine, document and allocate the resources needed to protect the system, as part of capital planning and investment control | The system owner raises the cost of security and privacy in \<Organisation\>'s yearly budgeting, and records it on TPL-23 (section 3.3) | Not yet raised in budgeting |
| c | Establish a separate line for security and privacy in programming and budgeting documents | Security and privacy are a separate line in \<System Name\>'s budget request | Not yet raised in budgeting |

**Table 12: SA-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R2 (\<Policy\>, section SA.4); PRO-SA-6 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The budget request, with its security and privacy line; TPL-23 records |
| Status | Partially implemented |
| Risk decision | NC-SA-02, rated Low: approve |
| Open items | PA-128: raise the costs at the next yearly budgeting |

### 4.3 SA-3 System Development Life Cycle

**Table 13: SA-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Acquire, develop and manage the system using a defined lifecycle that includes security and privacy | CSS \<ver\>, practice by practice (section 3.2), through six stages, each with its security and privacy check (section 3.3) | Mapped and approved. Not yet in routine use |
| b | Define and document security and privacy roles and responsibilities throughout the lifecycle | \<Roles and Responsibilities\>, the privacy plan, and the stages in section 3.3 | Done |
| c | Identify the people who hold those roles | Named in \<Roles and Responsibilities\> and in the privacy plan, section 3 | Done |
| d | Integrate security and privacy risk management into the lifecycle | Each change records its security and privacy effect on TPL-6, and the security officer checks significant designs (PRO-SA-1). A change that affects personal data goes to the legal adviser (PRO-PT-3) | Approved. Not yet in use |

**Table 14: SA-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, developers |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R1 (\<Policy\>, section SA.4); PRO-SA-1 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-6 change records showing each check; the framework in section 3.2 |
| Status | Partially implemented |
| Risk decision | NC-SA-03, rated Low: approve |
| Open items | PA-128: bring the lifecycle into routine use |

### 4.4 SA-4 Acquisition Process

**Table 15: SA-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | The contract includes security and privacy functional requirements | The controls of the Moderate and privacy baselines that the product or service must meet, by reference to the security plan | Contract not seen (EV-SA-01) |
| b | The contract includes strength of mechanism requirements | The strength required of each mechanism, such as encryption and sign-in, as the family design documents set it | Contract not seen (EV-SA-01) |
| c | The contract includes security and privacy assurance requirements | The evidence the supplier must give that its controls work, such as test results, certifications or audit reports | Contract not seen (EV-SA-01) |
| d | The contract includes the controls needed to meet the requirements | The controls the supplier must operate, stated or referenced | Contract not seen (EV-SA-01) |
| e | The contract includes security and privacy documentation requirements | The administrator and user documentation the supplier must provide (SA-5) | Contract not seen (EV-SA-01) |
| f | The contract includes requirements for protecting that documentation | The documentation is restricted, and handled as \<System Name\>'s own documents are | Contract not seen (EV-SA-01) |
| g | The contract describes the development environment and the environment the system will run in | How the product is built, and \<Organisation\>'s environment it will run in | Contract not seen (EV-SA-01) |
| h | The contract allocates responsibility for security, privacy and supply chain risk | Each party's responsibilities, including reporting a compromise to the security officer (\<Supply Chain Risk Management\>) | Contract not seen (EV-SA-01) |
| i | The contract includes acceptance criteria | The tests or evidence that must pass before \<Organisation\> accepts the product or service | Contract not seen (EV-SA-01) |

**Table 16: SA-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | System owner, \<Organisation\> |
| Enforced by | \<Organisation\>'s standard contract |
| Rules and procedures | Policy rule R3 (\<Policy\>, section SA.4); PRO-SA-3, step 1 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The standard contract, with the security and privacy terms added |
| Status | Not implemented |
| Risk decision | NC-SA-04, rated Low: obtain evidence |
| Open items | EV-SA-01: obtain the contract terms. PA-128 |

### 4.5 SA-4(1) Functional Properties of Controls

**Table 17: SA-4(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The developer describes the functional properties of the controls to be implemented | Each family's design document, and the security plan, section 7, set out what each control does | Done |

**Table 18: SA-4(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R4 (\<Policy\>, section SA.4); no procedure of its own |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The family design documents; \<System Security Plan\>, section 7 |
| Status | Implemented |
| Risk decision | NC-SA-05, rated Low: approve; now satisfied |
| Open items | None |

### 4.6 SA-4(2) Design and Implementation Information for Controls

**Table 19: SA-4(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The developer provides design and implementation information for the controls, at a defined level of detail | The security-relevant external interfaces and the high-level design (\<Security Architecture\>; \<System Security Plan\>, sections 3 and 4), and how each security function is built, in the family design documents: enough for an assessor to judge each control | Done |

**Table 20: SA-4(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R4 (\<Policy\>, section SA.4); no procedure of its own |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | \<Security Architecture\>; \<System Security Plan\>, sections 3 and 4; the family design documents |
| Status | Implemented |
| Risk decision | NC-SA-06, rated Low: approve; now satisfied |
| Open items | None |

### 4.7 SA-4(9) Functions, Ports, Protocols, and Services in Use

**Table 21: SA-4(9) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The developer identifies the functions, ports, protocols and services intended for use | \<System Security Plan\>, section 3.7, and the allowed flows in \<Access Control Management\>, section 3.6 | Done |

**Table 22: SA-4(9) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R4 (\<Policy\>, section SA.4); no procedure of its own |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | \<System Security Plan\>, section 3.7 |
| Status | Implemented |
| Risk decision | NC-SA-07, rated Low: approve; now satisfied |
| Open items | None |

### 4.8 SA-4(10) Use of Approved PIV Products

**Table 23: SA-4(10) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use only products on the approved list for PIV capability | Not applicable: It requires products on the United States government's list for PIV identity cards, which \<System Name\> does not use (\<Tailoring Register\>, TR-SA-01) | Not applicable |

**Table 24: SA-4(10) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Decision | TR-SA-01, agreed by the system owner on 6 November 2026 |

### 4.9 SA-5 System Documentation

**Table 25: SA-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | Administrator documentation on the secure configuration, installation and operation of the system | \<Administrator Guide\>, sections 2 to 4 | Drafted. Not yet confirmed by the developers (S10; PA-69) |
| a.2 | Administrator documentation on using and maintaining the security and privacy functions | \<Administrator Guide\>, sections 5 and 6 | Drafted. Not yet confirmed |
| a.3 | Administrator documentation on known weaknesses in configuring and using privileged functions | \<Administrator Guide\>, section 7 | Drafted. Not yet confirmed |
| b.1 | User documentation on the security and privacy functions users can reach, and how to use them | \<User Guide\>, sections 2 to 4 | Drafted. Not yet confirmed |
| b.2 | User documentation on using the system securely and protecting people's privacy | \<User Guide\>, sections 3 and 4 | Drafted. Not yet confirmed |
| b.3 | User documentation on users' responsibilities for security and privacy | \<User Guide\>, sections 4 and 5 | Drafted. Not yet confirmed |
| c | Record attempts to obtain documentation that is missing, and act on it | The system owner records each missing supplier document, and chases the supplier (PRO-SA-4) | Approved. Not yet in use |
| d | Distribute the documentation to defined people | Administrators, the security officer and users | Drafts not yet distributed |

**Table 26: SA-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>'s developers, who write the guides |
| Responsible | Developers |
| Enforced by | Not a system function. The guides are kept with the code |
| Rules and procedures | Policy rule R5 (\<Policy\>, section SA.4); PRO-SA-4 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The confirmed guides; the record of missing documents |
| Status | Partially implemented |
| Risk decision | NC-SA-08, rated Low: remediate |
| Open items | PA-69: the developers confirm the guides, which are then shared |

### 4.10 SA-8 Security and Privacy Engineering Principles

**Table 27: SA-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Apply defined security and privacy engineering principles in the specification, design, development, implementation and modification of the system | The NCSC secure design principles and the CSS privacy engineering objectives, mapped to \<System Name\> in \<Security Architecture\>, section 6.5 (section 3.6). The security officer checks each significant design against them (PRO-SA-1) | Applied to the specification and design. Work before 11 November 2026 was not checked against them; changes are checked from now on |

**Table 28: SA-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers, security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R6 (\<Policy\>, section SA.4); PRO-SA-1, step 2 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | \<Security Architecture\>, section 6.5; TPL-6 records of design checks |
| Status | Partially implemented |
| Risk decision | NC-SA-09, rated Low: approve |
| Open items | PA-128: check changes against the principles in routine use |

### 4.11 SA-9 External System Services

**Table 29: SA-9 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Require providers of external services to meet the security and privacy requirements and use defined controls | The controls stated in each provider's contract or service terms (section 3.7). Each row records what the trust in the service rests on, and \<Organisation\>'s agreements are to state service levels and remedies | Terms not seen (EV-SA-02, EV-SA-03) |
| b | Define and document oversight, and user roles and responsibilities, for external services | The system owner oversees each service. Section 3.7 and \<Roles and Responsibilities\> say who uses each | Done |
| c | Monitor providers' compliance on an ongoing basis by defined means | The system owner's review of each service every 12 months, on TPL-16 (PRO-SA-3) | No review yet held |

**Table 30: SA-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and its providers |
| Responsible | System owner, \<Organisation\> |
| Enforced by | Contracts and service terms |
| Rules and procedures | Policy rule R9 (\<Policy\>, section SA.4); PRO-SA-3 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Each provider's terms and evidence; TPL-16 reviews |
| Status | Partially implemented |
| Risk decision | NC-SA-10, rated Low: obtain evidence |
| Open items | EV-SA-02, EV-SA-03: obtain the providers' evidence. PA-128: hold the first review |

### 4.12 SA-9(2) Identification of Functions, Ports, Protocols, and Services

**Table 31: SA-9(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Require providers of defined external services to identify the functions, ports, protocols and other services they need | Every service in section 3.7, including \<Organisation\>'s hosting, network, ServiceNow, AD FS and Active Directory, and GitHub | Providers' lists not seen (EV-SA-02, EV-SA-03) |

**Table 32: SA-9(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | The providers of external services |
| Responsible | \<Organisation\> |
| Enforced by | Contracts and service terms |
| Rules and procedures | Policy rule R9 (\<Policy\>, section SA.4); PRO-SA-3, step 2 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Each provider's list of functions, ports, protocols and services |
| Status | Not implemented |
| Risk decision | NC-SA-11, rated Low: obtain evidence |
| Open items | EV-SA-02, EV-SA-03. PA-128 |

### 4.13 SA-10 Developer Configuration Management

**Table 33: SA-10 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Perform configuration management during defined stages of the lifecycle | Development, implementation and operation: code, configuration, documents and test scripts held in Git, in private repositories on GitHub (section 3.8) | Code is in Git, in private repositories (S04). 10 test scripts were not (S07) |
| b | Document, manage and control the integrity of changes to defined items | Each default branch protected, with at least one approving review before a change merges, and each release tag signed | Not in place: no branch protection, required review or signed tag (S01, S05; PA-91) |
| c | Implement only approved changes | Only reviewed changes merge, and only approved releases are deployed, through change control (\<Configuration Management\>) | Not enforced (S01, S05; PA-91, PA-53) |
| d | Document approved changes and their security and privacy effects | Each change records its effect on TPL-6 (PRO-SA-1) | Approved. Not yet in routine use |
| e | Track security flaws and their resolution, and report findings to defined people | Flaws are tracked in the Risk List and the POA&M, and reported to the system owner and the security officer | Done |

**Table 34: SA-10 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\>'s developers, on GitHub |
| Responsible | Developers |
| Enforced by | GitHub branch protection and signed tags, once set (PA-91) |
| Rules and procedures | Policy rule R7 (\<Policy\>, section SA.4); PRO-SA-1 (\<Procedures\>) |
| Tests | Checks S01 to S05 and S07 (Test-Development.ps1, 11 November 2026): no protection, required review or signed tag, and test scripts outside Git |
| Records an assessor will ask for | The branch settings; merged changes with their reviews; signed tags; TPL-6 records |
| Status | Partially implemented |
| Risk decision | NC-SA-12, rated Medium: remediate |
| Open items | PA-91: protect the branches, require review, sign tags and commit the scripts. PA-53: the change workflow |

### 4.14 SA-11 Developer Testing and Evaluation

**Table 35: SA-11 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Develop and carry out a plan for ongoing security and privacy control assessments | The developer test plan in section 3.9: 15 scripts covering the security functions, with privacy checks in Test-PersonalData.ps1 | Carried out: the scripts ran on the v1.0 build, and the evidence is kept |
| b | Test at a defined frequency, depth and coverage | Unit, integration and security tests at each release, covering every security function, with the web applications verified to OWASP ASVS 5.0 Level 2 | Run by hand; no unit tests or pipeline (S08; PA-68). ASVS not yet verified (PA-68) |
| c | Produce evidence that the plan was carried out, and the results | Each run is kept with its results, a README and a manifest of SHA-256 hashes | Done |
| d | Use a flaw remediation process that can be verified | A fixed flaw is accepted only when its test passes on a repeat run (PRO-SA-2, step 4) | Done, as for the access control fixes |
| e | Correct the flaws found | Each flaw goes to the Risk List and the POA&M, and is fixed in development | Waiting for the development phase |

**Table 36: SA-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\>'s developers, with the build tools |
| Responsible | Developers |
| Enforced by | The test scripts; a build pipeline, once built (PA-68) |
| Rules and procedures | Policy rule R8 (\<Policy\>, section SA.4); PRO-SA-2 (\<Procedures\>) |
| Tests | The 15 scripts in section 3.9. The sign-in and access checks ran on a build with \<System Name\>'s own passwords and groups, and are to be run again with sign-in through AD FS (PA-95) |
| Records an assessor will ask for | The results and manifest of each run; the pipeline's results, once built |
| Status | Partially implemented |
| Risk decision | NC-SA-13, rated Medium: remediate |
| Open items | PA-68: build the pipeline and unit tests, and verify the web applications to ASVS Level 2. PA-92: turn the package audit on, and add static analysis. PA-95: test sign-in through AD FS |

### 4.15 SA-15 Development Process, Standards, and Tools

**Table 37: SA-15 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | Follow a documented development process that explicitly addresses security and privacy requirements | CSS \<ver\> (section 3.2), with the acquisition policy and the personal data policy | Done |
| a.2 | The process identifies the standards and tools used | CSS, OWASP ASVS 5.0, the NCSC principles and the tools in section 3.10 | Done |
| a.3 | The process documents the tool options and configurations used | Section 3.10, with the settings that matter for security | Done, including the package audit turned off (PA-92) |
| a.4 | The process documents, manages and protects changes to itself and its tools | Changes to the process or tools are reviewed every 12 months and recorded on TPL-23 (PRO-SA-6) | Approved. Not yet in use |
| b | Review the process, standards, tools and configurations at a defined frequency, against defined requirements | Every 12 months, against the acquisition policy and the personal data policy | No review yet held |

**Table 38: SA-15 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers |
| Enforced by | Not a system function |
| Rules and procedures | Policy rules R1, R8 (\<Policy\>, section SA.4); PRO-SA-6 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-23 records of the yearly review |
| Status | Partially implemented |
| Risk decision | NC-SA-14, rated Low: approve |
| Open items | PA-128: hold the first yearly review |

### 4.16 SA-15(3) Criticality Analysis

**Table 39: SA-15(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Perform a criticality analysis at defined decision points | At design and at each major change (\<Risk Assessment Management\>, section 3.9) | Done on 11 November 2026, and redone on 18 November 2026 for sign-in through AD FS |
| b | At a defined breadth and depth | Every component, in enough depth to identify the critical ones | Done |

**Table 40: SA-15(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers |
| Enforced by | Not a system function |
| Rules and procedures | The risk assessment policy, rule R10 (\<Policy\> (RA)); PRO-RA-6; PRO-SA-1, step 2 (\<Procedures\>) |
| Tests | Check V08 (Test-Vulnerability.ps1): every critical component is described in the security plan. It passed |
| Records an assessor will ask for | \<Risk Assessment Management\>, section 3.9; TPL-23 records |
| Status | Implemented |
| Risk decision | NC-SA-15, rated Low: approve; now satisfied |
| Open items | The system owner confirms the components the RA cross-check added |

### 4.17 SA-22 Unsupported System Components

**Table 41: SA-22 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Replace components when support for them is no longer available | Each is replaced before its support ends, with the replacement planned at least 6 months before (section 3.12) | No component within 6 months of the end of support (S09). Packages and browser libraries are not yet checked for loss of support (PA-128) |
| b | Provide defined options for other support for unsupported components | In-house support, or a supplier's extended support by exception, approved by the authorising official | None needed yet |

**Table 42: SA-22 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers, authorising official |
| Enforced by | Not a system function. The monthly support check (\<Security Operating Procedures\>, C11) |
| Rules and procedures | Policy rule R10 (\<Policy\>, section SA.4); PRO-SA-5 (\<Procedures\>) |
| Tests | Check S09 (Test-Development.ps1, 11 November 2026): no component near the end of support. It passed |
| Records an assessor will ask for | The support dates in \<Maintenance Management\>, section 3.8; the monthly check records |
| Status | Implemented |
| Risk decision | NC-SA-16, rated Low: approve; now satisfied |
| Open items | None |

## Appendix A Parameter register

These are the CSS organisation-defined values for the SA entries: 35 in total. SA-4(10) is tailored (\<Tailoring Register\>, TR-SA-01), and has no parameters. They were agreed on 6 November 2026, and restated as requirements on 11 November 2026 (D-SA-P01). **State now** says whether \<System Name\> meets the value today.

**Table 43: SA parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| SA-01\_ODP\[01\] | Who receives the policy | Developers and administrators | Not yet shared |
| SA-01\_ODP\[02\] | Who receives the procedures | Developers and administrators | Not yet shared |
| SA-01\_ODP\[03\] | Level of the policy | System level | Met |
| SA-01\_ODP\[04\] | Official who manages them | System owner | Met |
| SA-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review not yet due |
| SA-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: reviewed after the SA pack review |
| SA-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review not yet due |
| SA-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: reviewed as version \<ver\> |
| SA-03\_ODP | Lifecycle | CSS \<ver\>, as in section 3.2 | Mapped; not yet in routine use |
| SA-04\_ODP\[01\] | Contract method | Standard contract language | Contract not seen (EV-SA-01) |
| SA-04\_ODP\[02\] | Contract language | \<Organisation\>'s standard contract, with security and privacy requirements added | Contract not seen (EV-SA-01) |
| SA-04(02)\_ODP\[01\] | Design information level | Security-relevant external interfaces and high-level design | Met: \<Security Architecture\> and \<System Security Plan\>, sections 3 and 4 |
| SA-04(02)\_ODP\[02\] | Other information | Implementation notes for security functions | Met: the design document of each family |
| SA-04(02)\_ODP\[03\] | Level of detail | Enough for an assessor to judge each control | Met: SSP section 7 and the assessments |
| SA-05\_ODP\[01\] | What to do about missing documents | Record it and chase the supplier | Met by procedure |
| SA-05\_ODP\[02\] | Who receives documentation | Administrators, the security officer and users | Guides drafted, not yet shared |
| SA-08\_ODP\[01\] | Security engineering principles | NCSC secure design principles | Mapped in \<Security Architecture\>, section 6.5 |
| SA-08\_ODP\[02\] | Privacy engineering principles | The CSS privacy engineering objectives | Mapped in \<Security Architecture\>, section 6.5 |
| SA-09\_ODP\[01\] | Controls providers must use | Those stated in the contract or service terms | Terms not seen (EV-SA-02, EV-SA-03) |
| SA-09\_ODP\[02\] | How compliance is monitored | System owner's review every 12 months, on TPL-16 | First review not yet held |
| SA-09(02)\_ODP | Services concerned | The services in section 3.7 | Lists not seen |
| SA-10\_ODP\[01\] | When change control applies | Development, implementation and operation | Not enforced (PA-91) |
| SA-10\_ODP\[02\] | What is controlled | Code, configuration, documents and test scripts | 10 test scripts not in Git (PA-91) |
| SA-10\_ODP\[03\] | Who is told of flaws | System owner and security officer | Met: through \<Risk List\> and \<Plan of Action and Milestones\> |
| SA-11\_ODP\[01\] | Test types | Unit, integration and security | Integration and security only; no unit tests (PA-68) |
| SA-11\_ODP\[02\] | Frequency | Each release | Run by hand; no pipeline (PA-68) |
| SA-11\_ODP\[03\] | Depth and coverage | Every security function in section 3.9, verified to OWASP ASVS 5.0 Level 2 for the web applications | Security functions covered by scripts; ASVS not yet assessed |
| SA-15\_ODP\[01\] | Review frequency | Every 12 months | First review not yet due |
| SA-15\_ODP\[02\] | Security requirements | \<Policy\> (SA) | Met |
| SA-15\_ODP\[03\] | Privacy requirements | \<Policy\> (PT) | Met |
| SA-15(03)\_ODP\[01\] | When criticality is analysed | Design, and each major change | Met: first analysis on 11 November 2026 |
| SA-15(03)\_ODP\[02\] | Breadth | All components | Met: \<Risk Assessment Management\>, section 3.9 |
| SA-15(03)\_ODP\[03\] | Depth | Enough to identify critical components | Met |
| SA-22\_ODP\[01\] | Support options | In-house support, or an external provider | Met |
| SA-22\_ODP\[02\] | External support | A supplier's extended support, by exception approved by the authorising official, with a replacement planned at least 6 months before support ends | Met: no component near the end of support (S09) |

## Appendix B Acquisition controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes some way towards them, and Table 44 says where. SA-6, SA-7, SA-12, SA-13, SA-14, SA-18 and SA-19 are withdrawn, and so are the enhancements of SA-5. SA-22(1) is now part of SA-22.

**Table 44: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| SA-3(1) Manage Preproduction Environment | Protects the development and test environments | Not required. Done in part: the test stacks are separate from production |
| SA-3(2) Use of Live or Operational Data | Limits the use of real data in development and testing | Not required. Done in design: the test stacks hold sample data only (Q09; \<PII Processing Management\>) |
| SA-3(3) Technology Refresh | Plans the replacement of technology | Not required. Done in part: replacements are planned 6 months before support ends (section 3.12) |
| SA-4(3) Development Methods, Techniques, and Practices | Requires a stated development method | Not required. Done in design: CSS \<ver\> (section 3.2) |
| SA-4(5) System, Component, and Service Configurations | Delivers products with secure settings in place | Not required: selected at High only |
| SA-4(6), SA-4(7) Use of Information Assurance Products; NIAP-approved Protection Profiles | Uses United States government evaluated products | Not applicable |
| SA-4(8) Continuous Monitoring Plan for Controls | Requires the developer to plan monitoring of the controls | Not required. The monitoring plan is in \<Assessment, Authorization, and Monitoring Management\>, section 3.8 |
| SA-4(11) System of Records | Privacy Act terms for a United States system of records | Not applicable |
| SA-4(12) Data Ownership | States that the organisation owns its data | Not required. \<Organisation\> owns the data \<System Name\> holds |
| SA-8(1) to SA-8(32) | Individual security engineering principles | Not required. The NCSC secure design principles cover the same ground (section 3.6) |
| SA-8(33) Minimization | The privacy principle of minimisation | In the CSS privacy baseline. Designed and assessed in \<PII Processing Management\> |
| SA-9(1) Risk Assessments and Organizational Approvals | Assesses risk and approves before an external service is used | Not required. Done in part: a new supplier or component is reviewed before use (PRO-RA-2, PRO-SA-7) |
| SA-9(3) to SA-9(8) | Trust relationships, consistent interests, location, the organisation's own keys and integrity checks, and United States jurisdiction | Not required. Done in part: each external service's basis of trust is recorded (section 3.7) |
| SA-10(1) to SA-10(7) | Integrity checks, trusted generation and distribution, and other forms of developer configuration management | Not required. Done in part in design: signed tags and release checksums (PA-61, PA-91) |
| SA-11(1) to SA-11(9) | Static and dynamic analysis, threat modelling, code review, penetration testing and other developer tests | Not required. Done in part in design: the kinds of analysis in section 3.9 |
| SA-15 enhancements other than SA-15(3) | Quality metrics, tracking tools, attack surface reduction, continuous improvement, automated analysis and others | Not required. Done in part: the yearly process review (PRO-SA-6) |
| SA-16 Developer-provided Training | Training from the developer on the controls | Not required: selected at High only. Administrators' training is in \<Awareness and Training Management\> |
| SA-17 Developer Security and Privacy Architecture and Design | A formal security architecture from the developer | Not required: selected at High only. Done in part: \<Security Architecture\> |
| SA-20 Customized Development of Critical Components | Builds critical components in-house | Not required. \<System Name\>'s own applications are written in-house |
| SA-21 Developer Screening | Screens the developers | Not required: selected at High only. Developers are screened as their risk designation requires (\<Personnel Security Management\>) |
| SA-23 Specialization; SA-24 Design for Cyber Resiliency | Specialised components; designing to withstand and recover from attack | Not required |
