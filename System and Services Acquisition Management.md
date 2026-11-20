# \<System Name\> System and Services Acquisition Management

## 1 Purpose

This document sets out how \<System Name\> is designed to be built and bought securely, to meet the 17 System and Services Acquisition (SA) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the development framework; the lifecycle, roles and resources; contracts and design information; documentation; engineering principles; external services; developer configuration management; the developer test plan; the process, standards and tools; criticality analysis; unsupported components; how \<System Name\> is built today; what \<Organisation\> and the providers supply; and the policy and procedures. Each subsection names the controls it helps to meet. Appendix A lists the related controls and enhancements CSS does not select at Moderate.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.16 (Table 25). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (SA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (SA), and the steps people follow are in \<Procedures\> (SA). Four records sit beside this one, each holding what CSS asks the system's own documents to hold: the engineering principles in \<Security Architecture\>, section 6.5; the functions, ports, protocols and services in \<System Security Plan\>, section 3.7; the critical components in \<Risk Assessment Management\>, section 3.9; and the component support dates in \<Maintenance Management\>, section 3.8.

\<System Name\> is built in-house, so its developers carry most of these duties. What is bought is \<Organisation\>'s hosting and services, and the outside services the developers use.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. The settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

Where section 3 notes what "today" is, it means the tested v1.0 build. Those notes show where that build differs from the design.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.16 (Table 25).

## 3 The design

### 3.1 Principles

Controls met here: SA-3, SA-9, SA-10, SA-11, SA-15, SA-22.

1. **A named framework.** Development follows CSS \<ver\>, practice by practice.
2. **Known changes only.** Only reviewed and approved changes reach a release.
3. **Test before release.** Every security function is tested at each release, to a stated depth.
4. **Know what you depend on.** Every third-party component and external service is known, assessed and supported.

These carry out the principles and rules of \<Policy\>, sections SA.3 and SA.4.

![Figure 1: How \<System Name\> is built and bought](figures/sam-figure-1.png)

**Figure 1: How \<System Name\> is built and bought**

### 3.2 Development framework

Controls met here: SA-3, SA-15.

\<System Name\> is developed under CSS \<ver\>. A later version is in draft, and is adopted when final. The table gives each of the 19 practices, how \<System Name\> meets it, and the gap where it does not. The UK Software Security Code of Practice's principles 1.1 to 3.5 align with these practices. Its fourth theme, communication with customers, is for software that is sold, which \<System Name\> is not.

**Table 1: CSS practices**

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

Controls met here: SA-2, SA-3.

\<System Name\> goes through six stages, each with its security and privacy check (D-SA-05, D-SA-20). The roles are in \<Roles and Responsibilities\>, and the privacy roles in \<Privacy Plan\>, section 3.

**Table 2: Lifecycle stages**

| Stage | Security and privacy check | Who | Record |
| --- | --- | --- | --- |
| 1 Plan | The change's security and privacy effect is noted, including whether it affects personal data | Developers | TPL-6 |
| 2 Design | The security officer checks each significant design against the principles (section 3.6). The critical components are updated at each major change | Security officer, developers | TPL-6; \<Risk Assessment Management\>, section 3.9 |
| 3 Build | Another developer reviews each change before it merges. A new third-party component is checked first (PRO-SA-7) | Developers | The merge review; TPL-6 |
| 4 Test | The developer test plan runs at each release (section 3.9) | Developers, security officer | Results and manifest |
| 5 Release | The release goes through change control, with the guides confirmed, a signed tag and recorded checksums | Developers, system owner | TPL-6; the release tag |
| 6 Retire | A component is replaced before its support ends (section 3.12). When \<System Name\> itself is retired, its documents and media are disposed of as \<Media Protection Management\> and \<PII Processing Management\> set out | Developers, system owner | TPL-7; disposal records |

**Requirements.** The high-level security and privacy requirements are the CSS Moderate baseline and the CSS privacy baseline, chosen from the categorisation, with the privacy plan (\<Planning Management\>, section 3.7; \<Privacy Plan\>).

**Risk management in each change.** Each change records its security and privacy effect on TPL-6, and the security officer checks each significant design (PRO-SA-1). A change that affects personal data goes to the legal adviser (PRO-PT-3).

**Resources.** Every 12 months the system owner raises the cost of security and privacy in \<Organisation\>'s yearly budgeting, as a separate line in \<System Name\>'s budget request, and records it on TPL-23 (PRO-SA-6). It has not yet been raised.

### 3.4 Contracts and design information

Controls met here: SA-4, SA-4(1), SA-4(2), SA-4(9), SA-4(10).

\<System Name\>'s software is written in-house. What is bought, now or later, uses \<Organisation\>'s standard contract, with security and privacy terms added for each of the nine things SA-4 asks a contract to hold: the functional requirements, the strength of mechanisms, assurance, the controls, documentation and its protection, the development and operating environments, who is responsible for security, privacy and supply chain risk, and acceptance criteria (D-SA-06, D-SA-20; PRO-SA-3). The contract sets them out as follows:

1. **Functional requirements:** the controls of the Moderate and privacy baselines that the product or service must meet, by reference to the security plan.
2. **Strength of mechanisms:** the strength required of each mechanism, such as encryption and sign-in, as the family design documents set it.
3. **Assurance:** the evidence the supplier must give that its controls work, such as test results, certifications or audit reports.
4. **Controls:** the controls the supplier must operate, stated or referenced.
5. **Documentation:** the administrator and user documentation the supplier must provide (section 3.5).
6. **Protecting the documentation:** it is restricted, and handled as \<System Name\>'s own documents are.
7. **Environments:** how the product is built, and \<Organisation\>'s environment it will run in.
8. **Responsibilities:** each party's responsibilities for security, privacy and supply chain risk, including reporting a compromise to the security officer (\<Supply Chain Risk Management\>).
9. **Acceptance criteria:** the tests or evidence that must pass before \<Organisation\> accepts the product or service.

The contract also states how and when the supplier gives notice of support, maintenance and updates, as the CSS guidance on SA-4 suggests. \<Organisation\>'s contract has not been seen (EV-SA-01).

As the developer, \<System Name\>'s team provides the design information CSS asks for:

1. **What each control does** (SA-4(1)): each family's design document, and the security plan, section 7.
2. **How the controls are designed** (SA-4(2)): the security-relevant external interfaces and the high-level design in \<Security Architecture\> and the security plan, sections 3 and 4, and how each security function is built, in the family design documents: enough for an assessor to judge each control.
3. **The functions, ports, protocols and services in use** (SA-4(9)): the security plan, section 3.7, and the allowed flows in \<Access Control Management\>, section 3.6.

PIV products (SA-4(10)) are not applicable, as \<System Name\> does not use United States government identity cards (TR-SA-01).

### 3.5 Documentation

Controls met here: SA-5.

Two guides are kept with the code: the Administrator Guide (\<Administrator Guide\>), on secure installation, configuration and operation, the security and privacy functions, and known weaknesses in privileged functions; and the User Guide (\<User Guide\>), on signing in, using \<System Name\> securely, personal data and users' responsibilities. They are drafts until the developers confirm them against \<System Name\> (PA-69), and are confirmed again at each release (PRO-SA-4). They go to administrators, the security officer and users.

**Table 3: Where the guides cover each topic**

| Topic | Where |
| --- | --- |
| Secure configuration, installation and operation | \<Administrator Guide\>, sections 2 to 4 |
| Using and maintaining the security and privacy functions | \<Administrator Guide\>, sections 5 and 6 |
| Known weaknesses in configuring and using privileged functions | \<Administrator Guide\>, section 7 |
| The security and privacy functions users can reach, and how to use them | \<User Guide\>, sections 2 to 4 |
| Using \<System Name\> securely and protecting people's privacy | \<User Guide\>, sections 3 and 4 |
| Users' responsibilities for security and privacy | \<User Guide\>, sections 4 and 5 |

The system owner records each supplier document that is missing, and chases the supplier for it (D-SA-07; PRO-SA-4).

### 3.6 Engineering principles

Controls met here: SA-8.

The NCSC secure design principles and the CSS privacy engineering objectives are mapped to \<System Name\>'s specification and design in \<Security Architecture\>, section 6.5, which holds them (D-SA-08). They are applied in the specification, design, development, implementation and modification of \<System Name\>. The security officer checks each significant design against them (PRO-SA-1). Work on the tested v1.0 build was not checked against them; each change is from now on.

### 3.7 External services

Controls met here: SA-9, SA-9(2).

These are the services in SA-09(02)\_ODP. Each provider must meet \<System Name\>'s security and privacy requirements, and states the controls it uses in its contract or service terms. Each provider must also identify the functions, ports, protocols and other services it needs. \<System Name\> relies on \<Organisation\>'s AD FS, Active Directory and Starters/Leavers system for sign-in and access (D-AC-22, D-AC-23, D-SA-20).

**Oversight.** The system owner oversees each service, and reviews each provider's compliance every 12 months on TPL-16 (PRO-SA-3). Table 4 and \<Roles and Responsibilities\> say who uses each service.

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

Controls met here: SA-10.

1. **What is controlled.** Code, configuration, documents and test scripts, during development, implementation and operation.
2. **Where.** In Git, in six private repositories on GitHub, each with one default branch name.
3. **How a change gets in.** On a branch, reviewed and approved by another developer before it merges into the protected default branch.
4. **Releases.** Each release is tagged, the tag is signed, and its checksums are recorded (PA-61).
5. **Alerts.** Dependency alerts and secret scanning are on.
6. **Deployment.** Only an approved release is deployed, through change control (\<Configuration Management\>).
7. **Recording.** Each approved change records its security and privacy effect on TPL-6 (PRO-SA-1).
8. **Flaws.** Each security flaw is tracked in the Risk List and the POA&M, and reported to the system owner and the security officer.

Today items 2 to 5 are not in place (S01 to S05; PA-91), and the change workflow is not set up (PA-53).

### 3.9 Developer test plan

Controls met here: SA-11.

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

**Flaws.** Each flaw found goes to the Risk List and the POA&M, and is fixed in development. A fixed flaw is accepted only when its test passes on a repeat run (PRO-SA-2, step 4).

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

Controls met here: SA-15.

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

Controls met here: SA-15(3).

The criticality analysis (SA-15(3)) is held in \<Risk Assessment Management\>, section 3.9, with its method, the critical components and the critical functions. It is done at design and at each major change, across every component. The developers update it under PRO-SA-1 and PRO-RA-6.

### 3.12 Unsupported components

Controls met here: SA-22.

Each component is replaced before its vendor's support ends, with the replacement planned at least 6 months before (D-SA-13). The monthly check compares each component with its support dates, which are held in \<Maintenance Management\>, section 3.8 (PRO-SA-5; \<Security Operating Procedures\>, C11). A package or browser library has no vendor support date. It counts as unsupported when its maintainers stop releasing fixes, or it is marked deprecated, or it has a known flaw with no fix. The developers check each one in the monthly package check; this is not yet in use (PA-128). If a component cannot be replaced in time, the other support allowed is in-house support, or a supplier's extended support by exception approved by the authorising official.

### 3.13 How \<System Name\> is built today

Test-Development.ps1 ran on the v1.0 build. Its results, with their hashes, are kept with the SA evidence.

- **Repositories:** none of the six repositories protects its default branch, needs a review or alerts on vulnerable dependencies (S01, S02). Three name their default branch main and three master (S03). All six are private (S04).
- **Releases:** the v1.0 release of each application was 9 or 10 commits by one author, with no reviewed merge and no signed tag (S05).
- **Build and tests:** the image build and two toolkit projects turn NuGet's audit off (S06). 10 of the then 12 test scripts were not in Git (S07), and the applications have no unit tests (S08).
- **Components and guides:** no component is within 6 months of the end of its support (S09). The administrator and user guides exist only as drafts (S10).

### 3.14 What \<Organisation\> and the providers supply

Controls met here: SA-4, SA-9, SA-9(2), SA-10.

**Table 8: Asked of \<Organisation\> and the providers**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| The standard contract, with security and privacy terms | SA-4 | Its terms cover the nine things in section 3.4 | EV-SA-01 | Not sent |
| Hosting, network, ServiceNow, AD FS, Active Directory and the Starters/Leavers system | SA-9, SA-9(2) | Each states its controls, and the functions, ports, protocols and services it needs | EV-SA-02; EV-CA-02 for the AD FS agreement | Not sent |
| GitHub | SA-9, SA-9(2), SA-10 | Its controls for private repositories, and the plan and settings of \<System Name\>'s account | EV-SA-03 | Not sent |

**Today:** no request has been sent, and none of this is evidenced.

### 3.15 Policy and procedures

Controls met here: SA-1.

1. **Policy.** \<Policy\> (SA) is a system-level policy. It is shared with the developers and administrators. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (SA) holds seven procedures, PRO-SA-1 to PRO-SA-7. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control.

## Appendix A Acquisition controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes some way towards them, and Table 9 says where. SA-6, SA-7, SA-12, SA-13, SA-14, SA-18 and SA-19 are withdrawn, and so are the enhancements of SA-5. SA-22(1) is now part of SA-22.

**Table 9: Related controls and enhancements not selected**

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
