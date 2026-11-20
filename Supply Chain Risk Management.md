# \<System Name\> Supply Chain Risk Management

## 1 Purpose

This document shows how \<System Name\> manages the risk that it is harmed through what it is built from, where it is hosted and who supplies it, for each of the 12 Supply Chain Risk Management (SR) controls in the CSS Moderate baseline. Section 3 is the supply chain risk management plan that SR-2 requires, on the headings of CSS: the system context, the team, the risks at each stage, the supplier register, the risk tolerance, how components come in, and notices, inspection, authenticity and disposal. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define.

This is the only place this design is held. Other documents point here. The policy is in \<Policy\> (SR), and the steps people follow are in \<Procedures\> (SR). The critical components are in \<Risk Assessment Management\>, section 3.9, the supply chain risk review in its section 3.4, the external services in \<System and Services Acquisition Management\>, section 3.7, and the integrity baseline in \<System and Information Integrity Management\>, section 3.5.

An assessor examines the plan, the supplier register, the supplier reviews, the bill of materials and the release inspection records; interviews the system owner, the developers, the security officer and \<Organisation\>'s IT service desk; and tests where each component comes from and whether a release matches its record (CSS). So for each control section 4 gives:

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

Of the 12 controls, none is implemented, 5 are partially implemented and 7 are not implemented. No control in the Moderate baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 2: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| SR-1 | Policy and Procedures | Partially implemented | Not yet shared. The later version awaits the Head of Cyber | NC-SR-01; PA-20 |
| SR-2 | Supply Chain Risk Management Plan | Partially implemented | Not in the restricted store; not updated after the changes to sign-in and hosting | NC-SR-02; PA-88, PA-127 |
| SR-2(1) | Establish SCRM Team | Not implemented | The team is not confirmed and has not met | NC-SR-03; PA-131 |
| SR-3 | Supply Chain Controls and Processes | Partially implemented | Packages bypass the offline feed; no lock files, trust policy, pinned images or bill of materials | NC-SR-04; PA-94 |
| SR-5 | Acquisition Strategies, Tools, and Methods | Partially implemented | Packages acquired unchecked; NuGet's audit off | NC-SR-05; PA-92, PA-94 |
| SR-6 | Supplier Assessments and Reviews | Not implemented | No supplier review held | NC-SR-06; PA-131 |
| SR-8 | Notification Agreements | Not implemented | \<Organisation\>'s terms not seen | NC-SR-07; PA-131, EV-SR-01 |
| SR-10 | Inspection of Systems or Components | Partially implemented | No release checksums; hardware inspection not seen | NC-SR-08; PA-61, PA-77, PA-78 |
| SR-11 | Component Authenticity | Not implemented | No trust policy; browser files unchecked | NC-SR-09; PA-34, PA-94 |
| SR-11(1) | Anti-counterfeit Training | Not implemented | Not evidenced | NC-SR-10; PA-131, EV-SR-02 |
| SR-11(2) | Configuration Control for Component Service and Repair | Not implemented | Not evidenced | NC-SR-11; PA-131, EV-SR-02 |
| SR-12 | Component Disposal | Not implemented | Not evidenced | NC-SR-12; PA-131, EV-SR-02 |

Two things matter most. Almost every package comes straight from nuget.org, with no lock file or signed-package trust policy, so what a release contains is not fixed or checked (PA-94, rated Medium). And a release has no bill of materials or checksums, so it cannot be shown to match its record (PA-78, PA-61).

## 3 The supply chain risk management plan

### 3.1 Principles

1. **Know the supply chain.** Every supplier is named, with its criticality.
2. **One way in.** Every package comes through one checked source.
3. **Fix and verify.** A release is built from exactly the components recorded for it, and can be shown to be so.
4. **Hear about problems.** Suppliers and advisories tell us when something goes wrong.
5. **Nothing left behind.** \<System Name\> data is removed before anything leaves.

These carry out the principles and rules of \<Policy\>, sections SR.3 and SR.4.

![Figure 1: How components reach \<System Name\>, and the checks on the way](figures/srm-figure-1.png)

**Figure 1: How components reach \<System Name\>, and the checks on the way**

### 3.2 System context

\<System Name\> is three .NET 10 web applications and a PostgreSQL 18 database, to run as Windows services on two Windows Server 2025 servers hosted by \<Organisation\> (D-PL-10). They are built and tested in container images. Its impact level is Moderate (D-GEN-06), and it is not yet in operation. Users sign in through \<Organisation\>'s AD FS, and access is decided by Active Directory groups (D-AC-23).

What it is built from: 59 packages for API, 40 for UI application and 34 for Admin application, counting those pulled in; two Microsoft base images and the PostgreSQL image; and two browser libraries loaded from jsDelivr. The values were agreed on 6 November 2026 and revised on 12 November 2026 (D-SR-P01).

### 3.3 The supply chain team

The supply chain team is the system owner, the security officer, a developer and \<Organisation\>'s IT service desk (D-SR-05). It keeps this plan current, reviews the critical suppliers every 12 months and before a new critical supplier is used, and handles notices of compromise (PRO-SR-2, PRO-SR-5). The system owner leads it and approves the plan. \<Organisation\> has not yet confirmed its part, and the team has not met (EV-SR-01).

### 3.4 Risks across the lifecycle

**Table 3: Supply chain risks by stage**

| Stage | Risk | Response | State now |
| --- | --- | --- | --- |
| Research and development | A harmful, vulnerable or look-alike package is added | PRO-SR-1 check, then into the offline feed | Packages come straight from nuget.org (PA-94) |
| Design | A design relies on an unsuitable supplier | Supplier register; review before a new critical supplier | Register in place |
| Manufacturing | Hardware is altered before arrival | \<Organisation\> inspects | Not seen (EV-SR-02) |
| Acquisition | A supplier makes no security commitment | \<Organisation\>'s contract; open-source security policies checked | Contract terms not seen (EV-SR-01) |
| Delivery | A package, image or release is altered in transit | Lock files, signed-package trust, image digests, release SHA-256 values | Not built (PA-94, PA-77, PA-61) |
| Integration | A new component weakens a control | Release tests and Test-SupplyChain.ps1 | Release tests not built (PA-68) |
| Operation and maintenance | A known flaw appears in a component | Monthly and release checks; \<Procedures\>, PRO-SI-1 | Test-Vulnerability.ps1 by hand; 7 advisories open (PA-56) |
| Disposal | Data leaves with a component | PRO-MP-3 | Not yet used |

### 3.5 Supplier register

Criticality follows the critical components in \<Risk Assessment Management\>, section 3.9: High where a compromise would reach documents, or the way people sign in. Advisories are watched through the sources in \<System and Information Integrity Management\>, section 3.3.

**Table 4: Supplier register**

| Supplier | What it supplies | Criticality | How it reaches \<System Name\> | Evidence | Notification route | Last review | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \<Organisation\> | Hosting, network, hardware, service desk, central logging, and sign-in through AD FS and Active Directory (D-AC-23) | High | Contract | EV-SR-01, EV-SR-02 (not yet received) | Security contact to the security officer, within 24 hours (to confirm) | 11 November 2026 (\<Risk Assessment Management\>, section 3.4) | November 2027 |
| Microsoft | .NET 10, ASP.NET Core and Entity Framework packages, Windows Server 2025 | High | nuget.org; the VM build | Published lifecycle and security advisories | Microsoft and .NET advisories | 11 November 2026 | November 2027 |
| Microsoft container registry (mcr.microsoft.com) | .NET SDK and runtime base images | High | Pulled by tag at build (PA-77) | Published image digests | .NET advisories | 11 November 2026 | November 2027 |
| nuget.org | The package registry for all other packages | High | Restored directly today (PA-94); vulnerability data only once fixed | Repository signatures on every package | GitHub Advisory Database | 12 November 2026 | November 2027 |
| Npgsql project | PostgreSQL driver and Entity Framework provider | High | nuget.org | Open-source project; security policy published | GitHub advisories | 12 November 2026 | November 2027 |
| PostgreSQL Global Development Group, through Docker Hub | The postgres:18 database image | High | Docker Hub (docker.io), pulled by tag (PA-77) | Official image; published support dates | PostgreSQL security announcements | 11 November 2026 | November 2027 |
| GitHub | Source code hosting | High | Private repositories (PA-91) | Published security terms (EV-SA-03) | GitHub advisories | 11 November 2026 | November 2027 |
| OfflineModules packages (in-house, system owner) | Access control modules | High | Offline feed only, by package source mapping | SHA-256 index in the feed (U05) | Internal | 12 November 2026 | November 2027 |
| Six Labors (ImageSharp) | Image processing | Medium | nuget.org | Six Labors Split License, community tier (D-CM-09); 6 advisories open (PA-56) | GitHub advisories | 11 November 2026 | November 2027 |
| SkiaSharp (Microsoft and Mono) | Image rendering and its Linux native library | Medium | nuget.org | Open-source project | GitHub advisories | 12 November 2026 | November 2027 |
| jsDelivr (cdn.jsdelivr.net) | Bootstrap Icons and OpenSeadragon in the browser | Medium | Loaded by each page, with no integrity check (PA-34) | None | None; to stop when files are served locally | 12 November 2026 | November 2027 |
| Swashbuckle and Azure.Storage.Blobs | API documentation; an unused storage client | Low | nuget.org; to be removed from release builds (PA-79) | Open-source and Microsoft packages | GitHub advisories | 12 November 2026 | November 2027 |

### 3.6 Risk tolerance

No critical component may be used without a known source and a SHA-256 record (D-SR-P01). A known flaw in any component is fixed to the timetable in \<Risk Assessment Management\>, section 3.6. A High supplier that has not been reviewed within 12 months, or a component that misses a check in section 3.9, is recorded in \<Risk List\> for a decision.

### 3.7 How components come in

**Table 5: Components, today and required**

| Component | Today | Required | POA&M |
| --- | --- | --- | --- |
| OfflineModules packages | Offline feed only, by package source mapping | As today | None |
| All other packages | Restored straight from nuget.org when the image is built; no lock file; any signature accepted | Mirrored into the offline feed after the PRO-SR-1 check; lock files in locked mode; trust policy for nuget.org's repository signature; NuGet's audit on | PA-94, PA-92 |
| Base and database images, for the build and the test stacks | Pulled by floating tag | Pinned by digest | PA-77 |
| Browser libraries | Loaded from jsDelivr, unchecked | Served by \<System Name\> | PA-34 |
| Releases | No checksum or bill of materials | SHA-256 values and a CycloneDX bill of materials, checked before installation | PA-61, PA-78 |
| Hardware and hosting | Provided by \<Organisation\> | Inspected, controlled under repair and disposed of by \<Organisation\>, with evidence | EV-SR-02 |

### 3.8 Notices, inspection, authenticity and disposal

1. **Notices** (SR-8). \<Organisation\> reports a supply chain compromise to the security officer within 24 hours, and shares assessment or audit results that affect \<System Name\> (EV-SR-01). For open-source suppliers, their published advisories are the notice, through the sources in \<System and Information Integrity Management\>, section 3.3. Each notice that applies is recorded on TPL-7, and a compromise is handled as an incident (PRO-SR-5).
2. **Inspection** (SR-10). Release packages, the test images and \<System Name\>'s application files are checked against their recorded SHA-256 values at each release, before installation, and whenever tampering is suspected. A different value, an unexpected package source or damaged packaging is a sign of tampering. \<Organisation\> inspects hardware (PRO-SR-3; EV-SR-02).
3. **Authenticity** (SR-11). Package names are checked against look-alikes, and packages come only from the offline feed under a signed-package trust policy. A suspected counterfeit is refused and reported to the security officer, \<Organisation\>, the package registry and, if serious, the NCSC. \<Organisation\> trains its buyers every year, and keeps control of hardware sent for repair (PRO-SR-4).
4. **Disposal** (SR-12). \<System Name\> data is removed first (PRO-MP-3), and \<Organisation\> disposes of the component and confirms in writing (PRO-SR-6).

### 3.9 How the plan is checked today

Test-SupplyChain.ps1 ran on the v1.0 build and its images on 12 November 2026, without a running stack. It passed 2 of 10 checks. Its results, with their hashes, are kept with the SR evidence.

**Table 6: Test-SupplyChain.ps1, 12 November 2026**

| Check | Result | What it found |
| --- | --- | --- |
| U01 Package sources | Gap | API restores 50 of 59 packages, UI application 34 of 40 and Admin application 28 of 34 from outside the offline feed (PA-94) |
| U02 Lock files | Gap | No project has a lock file (PA-94) |
| U03 Trust policy | Gap | Any signature is accepted (PA-94) |
| U04 NuGet audit | Gap | Turned off in the image build (PA-92) |
| U05 Feed index | Pass | All 1,688 indexed packages match their SHA-256 values |
| U06 Image pinning | Gap | 3 images by floating tag (PA-77) |
| U07 Bill of materials | Gap | None (PA-78) |
| U08 Integrity baseline | Pass | The three test images and \<System Name\>'s application files match \<System and Information Integrity Management\>, section 3.5 |
| U09 CDN files | Gap | 14 references to cdn.jsdelivr.net, none with an integrity check (PA-34) |
| U10 Supplier register | Gap | Version \<ver\> of the plan named 3 of the 8 suppliers the code relies on; the register in section 3.5 now names all 8, with criticality |

### 3.10 What \<Organisation\> provides

**Table 7: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Approved suppliers, a seat on the supply chain team, and notice of a compromise within 24 hours | SR-2(1), SR-3, SR-5, SR-6, SR-8 | Its suppliers are approved, the IT service desk joins the team, and a compromise reaches the security officer within 24 hours | EV-SR-01 | Not sent |
| Hardware inspection, buyers' training, control of equipment under repair, and disposal | SR-10, SR-11(1), SR-11(2), SR-12 | Each is done, with records | EV-SR-02 | Not sent |

**Today:** no request has been sent, and none of this is evidenced.

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 SR-1 Policy and Procedures

**Table 8: SR-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A supply chain risk management policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (SR): a system-level policy, shared with developers and administrators. The legal adviser reviewed it on 12 November 2026 | Version \<ver\> approved by the Head of Cyber (D-SR-01). The later version awaits the Head of Cyber (D-SR-12). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (SR): six procedures, PRO-SR-1 to PRO-SR-6. Shared with the same people | Version \<ver\> approved by the system owner (D-SR-13). Not yet shared |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 12 November 2026 after the SR pack review. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | Reviewed on 12 November 2026. The first yearly review falls due in November 2027 |

**Table 9: SR-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy; all six procedures (\<Procedures\>) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-SR-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-SR-12) |

### 4.2 SR-2 Supply Chain Risk Management Plan

**Table 10: SR-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Develop a plan for managing supply chain risk in research and development, design, manufacturing, acquisition, delivery, integration, operation and maintenance, and disposal of defined systems and components | Section 3 of this document is the plan. It covers \<System Name\>, its software packages, container images, browser files, build tools, hosting and hardware, with the risk at each stage in section 3.4 | Approved as version \<ver\> (D-SR-13), and rebuilt in this form on 18 November 2026 (D-SR-14) |
| b | Review and update the plan at a defined frequency, and as threats, the organisation or the environment change | Every 12 months by the supply chain team, and after a significant change (PRO-SR-2) | The first yearly review falls due in November 2027. Not yet updated after the changes to sign-in and hosting (PA-127) |
| c | Protect the plan from unauthorised disclosure and change | Restricted, under version control, and held in the restricted store | Not yet in the restricted store (PA-88) |

**Table 11: SR-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function. The plan is under version control |
| Rules and procedures | Policy rule R1 (\<Policy\>, section SR.4); PRO-SR-2 (\<Procedures\>) |
| Tests | None. Examined from the plan |
| Records an assessor will ask for | This plan, its approvals, and the records of its reviews |
| Status | Partially implemented |
| Risk decision | NC-SR-02, rated Low: approve |
| Open items | PA-88: move the set to the restricted store. PA-127: update it after the changes to sign-in and hosting |

### 4.3 SR-2(1) Establish SCRM Team

**Table 12: SR-2(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Set up a supply chain risk management team of defined people, to lead and support defined activities | The system owner, the security officer, a developer and \<Organisation\>'s IT service desk. They keep this plan current, review suppliers and handle notices of compromise (section 3.3) | Named. \<Organisation\> has not confirmed its part, and the team has not met (EV-SR-01) |

**Table 13: SR-2(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R1 (\<Policy\>, section SR.4); PRO-SR-2 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The team's membership and its records of meetings and reviews |
| Status | Not implemented |
| Risk decision | NC-SR-03, rated Low: approve |
| Open items | PA-131: confirm the team and hold its first meeting. EV-SR-01 |

### 4.4 SR-3 Supply Chain Controls and Processes

**Table 14: SR-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Set up processes to find and address weaknesses in supply chain elements and processes, coordinated with defined people | Supplier reviews (PRO-SR-2), component checks before use (PRO-SR-1) and release inspection (PRO-SR-3), coordinated with \<Organisation\>'s IT service desk and the suppliers in section 3.5 | Approved. No supplier review held yet |
| b | Use defined controls to protect against supply chain risk and limit the harm of supply chain events | Approved suppliers; every package through the offline feed; lock files and signed-package trust; images pinned by digest; integrity checks on browser files; a bill of materials; and monthly and release checks (section 3.7) | Only the OfflineModules packages use the feed (U01; PA-94); no lock files or trust policy (U02, U03); images by floating tag (U06; PA-77); browser files unchecked (U09; PA-34); no bill of materials (U07; PA-78) |
| c | Document the processes and controls in defined documents | This plan, and the security plan | Done |

**Table 15: SR-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | System owner, developers |
| Enforced by | The offline feed; the build, once lock files and a trust policy are set |
| Rules and procedures | Policy rules R2, R4 to R8 (\<Policy\>, section SR.4); PRO-SR-1, PRO-SR-3 (\<Procedures\>) |
| Tests | Checks U01 to U09 (Test-SupplyChain.ps1 on the v1.0 build, 12 November 2026): 2 passed, 7 showed gaps |
| Records an assessor will ask for | Test-SupplyChain.ps1 results; the lock files; the bill of materials |
| Status | Partially implemented |
| Risk decision | NC-SR-04, rated Medium: remediate (proposed by the system owner; awaits the authorising official) |
| Open items | PA-94, PA-77, PA-78, PA-34 |

### 4.5 SR-5 Acquisition Strategies, Tools, and Methods

**Table 16: SR-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use defined acquisition strategies, contract tools and procurement methods to protect against, find and reduce supply chain risk | Approved suppliers; every package through the offline feed after the PRO-SR-1 check; lock files and signed-package trust; images pinned by digest; and a review before a new critical supplier is used | Packages come straight from nuget.org (U01; PA-94); NuGet's audit is off in the build (U04; PA-92) |

**Table 17: SR-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers, \<Organisation\> |
| Enforced by | The offline feed and the build |
| Rules and procedures | Policy rules R3, R4 (\<Policy\>, section SR.4); PRO-SR-1 (\<Procedures\>) |
| Tests | Checks U01 and U04 (Test-SupplyChain.ps1 on the v1.0 build, 12 November 2026): both showed gaps |
| Records an assessor will ask for | The feed index; the build settings; \<Organisation\>'s approved supplier list |
| Status | Partially implemented |
| Risk decision | NC-SR-05, rated Low: remediate |
| Open items | PA-94, PA-92. EV-SR-01 |

### 4.6 SR-6 Supplier Assessments and Reviews

**Table 18: SR-6 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Assess and review the supply chain risks of suppliers and what they provide, at a defined frequency | Every critical supplier every 12 months, and before a new critical supplier is used, on TPL-16 (PRO-SR-2) | No supplier review held on TPL-16. The first supply chain risk review was held on 11 November 2026 (\<Risk Assessment Management\>, section 3.4) |

**Table 19: SR-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R10 (\<Policy\>, section SR.4); PRO-SR-2 (\<Procedures\>) |
| Tests | Check U10 (Test-SupplyChain.ps1 on the v1.0 build, 12 November 2026): the register named 3 of 8 suppliers at version \<ver\>, and names all 8 now |
| Records an assessor will ask for | TPL-16 records for each critical supplier |
| Status | Not implemented |
| Risk decision | NC-SR-06, rated Low: approve |
| Open items | PA-131: hold the first supplier reviews |

### 4.7 SR-8 Notification Agreements

**Table 20: SR-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Agree with those in the supply chain how compromises are notified, and assessment or audit results shared | \<Organisation\> reports a supply chain compromise to the security officer within 24 hours, and shares assessment or audit results that affect \<System Name\>. Open-source suppliers' advisories are treated as notice (section 3.8) | \<Organisation\>'s terms not seen (EV-SR-01). The advisories are not yet watched (PA-130) |

**Table 21: SR-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\>, suppliers |
| Enforced by | \<Organisation\>'s contract; the advisory sources |
| Rules and procedures | Policy rule R10 (\<Policy\>, section SR.4); PRO-SR-5 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The notification terms; TPL-7 records of notices |
| Status | Not implemented |
| Risk decision | NC-SR-07, rated Low: obtain evidence |
| Open items | EV-SR-01. PA-131 |

### 4.8 SR-10 Inspection of Systems or Components

**Table 22: SR-10 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Inspect defined systems or components, at defined times or on signs of need, to detect tampering | Release packages, the test images and \<System Name\>'s application files at each release and whenever tampering is suspected, against the recorded SHA-256 values; hardware by \<Organisation\> (section 3.8) | The test images and application files match the baseline (U08). Release checksums not built (PA-61). Hardware inspection not seen (EV-SR-02) |

**Table 23: SR-10 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers, \<Organisation\> |
| Enforced by | Test-SupplyChain.ps1; release checksums, once built |
| Rules and procedures | Policy rule R9 (\<Policy\>, section SR.4); PRO-SR-3 (\<Procedures\>) |
| Tests | Checks U05 and U08 (Test-SupplyChain.ps1 on the v1.0 build, 12 November 2026): both passed |
| Records an assessor will ask for | Test-SupplyChain.ps1 results; release records with SHA-256 values; \<Organisation\>'s inspection records |
| Status | Partially implemented |
| Risk decision | NC-SR-08, rated Low: remediate |
| Open items | PA-61, PA-77, PA-78. EV-SR-02 |

### 4.9 SR-11 Component Authenticity

**Table 24: SR-11 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Develop and carry out anti-counterfeit policy and procedures, with the means to detect and prevent counterfeit components | Policy rule R11 and PRO-SR-4: package names checked against look-alikes, packages only from the offline feed with signed-package trust, and hardware inspected by \<Organisation\> | Approved. No trust policy (U03; PA-94); browser files have no integrity check (U09; PA-34) |
| b | Report counterfeit components to defined parties | The source, the security officer and \<Organisation\>; for software, the package registry and, if serious, the NCSC | Approved. Not yet used |

**Table 25: SR-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Signed-package trust, once set |
| Rules and procedures | Policy rule R11 (\<Policy\>, section SR.4); PRO-SR-4 (\<Procedures\>) |
| Tests | Checks U03 and U09 (Test-SupplyChain.ps1 on the v1.0 build, 12 November 2026): both showed gaps |
| Records an assessor will ask for | The trust policy; TPL-10 records of any report |
| Status | Not implemented |
| Risk decision | NC-SR-09, rated Low: remediate |
| Open items | PA-94, PA-34 |

### 4.10 SR-11(1) Anti-counterfeit Training

**Table 26: SR-11(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Train defined people to detect counterfeit components | \<Organisation\> trains its buyers every year | Not seen (EV-SR-02) |

**Table 27: SR-11(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R11 (\<Policy\>, section SR.4); PRO-SR-4, step 3 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s training records |
| Status | Not implemented |
| Risk decision | NC-SR-10, rated Low: obtain evidence |
| Open items | EV-SR-02. PA-131 |

### 4.11 SR-11(2) Configuration Control for Component Service and Repair

**Table 28: SR-11(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Keep configuration control over components awaiting or returning from service or repair | Hardware away for service or repair stays under \<Organisation\>'s control | Not seen (EV-SR-02) |

**Table 29: SR-11(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R11 (\<Policy\>, section SR.4); PRO-SR-4, step 3 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s repair records |
| Status | Not implemented |
| Risk decision | NC-SR-11, rated Low: obtain evidence |
| Open items | EV-SR-02. PA-131 |

### 4.12 SR-12 Component Disposal

**Table 30: SR-12 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Dispose of defined data, documentation, tools or components by defined techniques | Hardware, media, data and documents: \<System Name\> data is removed first (PRO-MP-3), and \<Organisation\> disposes of the component and confirms in writing | PRO-MP-3 approved. \<Organisation\>'s disposal not seen (EV-SR-02) |

**Table 31: SR-12 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>; PRO-MP-3 |
| Rules and procedures | Policy rule R12 (\<Policy\>, section SR.4); PRO-SR-6 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Sanitisation records; \<Organisation\>'s disposal confirmations |
| Status | Not implemented |
| Risk decision | NC-SR-12, rated Low: obtain evidence |
| Open items | EV-SR-02. PA-131 |

## Appendix A Parameter register

These are the CSS organisation-defined values for the 12 SR entries: 32 in total. They were agreed on 6 November 2026 and revised on 12 November 2026 (D-SR-P01). **State now** says how far each is in place.

**Table 32: SR parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| SR-01\_ODP\[01\] | Who receives the policy | Developers and administrators | Not yet shared |
| SR-01\_ODP\[02\] | Who receives the procedures | Developers and administrators | Not yet shared |
| SR-01\_ODP\[03\] | Level of the policy | System level | In place |
| SR-01\_ODP\[04\] | Official who manages them | System owner | In place |
| SR-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review due November 2027 |
| SR-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Reviewed after the SR pack review, 12 November 2026 |
| SR-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review due November 2027 |
| SR-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Reviewed after the SR pack review, 12 November 2026 |
| SR-02\_ODP\[01\] | What the plan covers | \<System Name\>, its software packages, container images, browser files, build tools, hosting and hardware | Defined |
| SR-02\_ODP\[02\] | Review frequency | Every 12 months | First review due November 2027 |
| SR-02(01)\_ODP\[01\] | Team | System owner, security officer, a developer and \<Organisation\>'s IT service desk | Named; \<Organisation\> not yet confirmed |
| SR-02(01)\_ODP\[02\] | What the team does | Keeps this plan current, reviews suppliers, and handles notices of compromise | Team has not met |
| SR-03\_ODP\[01\] | What is covered | \<System Name\> and every component in its supplier register | Defined |
| SR-03\_ODP\[02\] | Who is coordinated with | \<Organisation\>'s IT service desk and the suppliers in section 4 | Defined |
| SR-03\_ODP\[03\] | Controls | Approved suppliers; every package through the offline feed; lock files and signed-package trust; images pinned by digest; integrity checks on browser files; a bill of materials; monthly and release checks | Only OfflineModules packages use the feed (U01; PA-94); no lock files or trust policy (U02, U03); images floating (U06; PA-77); CDN files unchecked (U09; PA-34); no bill of materials (U07; PA-78) |
| SR-03\_ODP\[04\] | Where controls are documented | Security and privacy plans, and this plan | Defined |
| SR-03\_ODP\[05\] | Other document | This plan | Defined |
| SR-05\_ODP | Strategies and methods | Approved suppliers; every package through the offline feed after the PRO-SR-1 check; lock files and signed-package trust; images pinned by digest; review before a new critical supplier | Packages come straight from nuget.org (U01; PA-94); NuGet audit off in the build (U04; PA-92) |
| SR-06\_ODP | Review frequency | Every 12 months, and before a new critical supplier is used | No review held on TPL-16; first supply chain review held 11 November 2026 (\<Risk Assessment Management\>, section 3.4) |
| SR-08\_ODP\[01\] | What is notified | A compromise in the supply chain, within 24 hours | \<Organisation\>'s terms not seen (EV-SR-01); open-source advisories watched (\<System and Information Integrity Management\>, section 3.3) |
| SR-08\_ODP\[02\] | Other results shared | Assessment or audit results that affect \<System Name\> | Not seen (EV-SR-01) |
| SR-10\_ODP\[01\] | What is inspected | Release packages, container images, \<System Name\> assemblies and hardware | Images and assemblies match the baseline (U08); release checksums not built (PA-61); hardware not seen (EV-SR-02) |
| SR-10\_ODP\[02\] | When | At each release, and when something suggests tampering | Defined |
| SR-10\_ODP\[03\] | Frequency | Each release | Test-SupplyChain.ps1 run on v1.0, 12 November 2026 |
| SR-10\_ODP\[04\] | Signs of tampering | A SHA-256 value that differs from the release record or baseline, an unexpected package source, or damaged packaging | Defined |
| SR-11\_ODP\[01\] | Who is told | The source of the counterfeit, and the two below | Defined |
| SR-11\_ODP\[02\] | External bodies told | The supplier, the package registry (NuGet or GitHub) and, if serious, the NCSC | Defined |
| SR-11\_ODP\[03\] | Who is told | Security officer and \<Organisation\> | Procedure approved; not yet used |
| SR-11(01)\_ODP | Who is trained | \<Organisation\>'s buyers, yearly | Not seen (EV-SR-02) |
| SR-11(02)\_ODP | Components under control | Hardware away for service or repair | Not seen (EV-SR-02) |
| SR-12\_ODP\[01\] | What is disposed of | Hardware, media, data and documents | Not seen (EV-SR-02) |
| SR-12\_ODP\[02\] | How | \<Procedures\>, PRO-MP-3 | PRO-MP-3 approved; not yet used |

## Appendix B Supply chain controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Table 33 says where the design goes some way towards them.

**Table 33: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| SR-3(1) to SR-3(3) | Diverse supply base; limiting harm; flowing controls down to sub-tier suppliers | Not required. Done in part: the risk tolerance limits harm (section 3.6) |
| SR-4 Provenance | Records where each component came from and every change to it | Not required. Done in part in design: the offline feed's SHA-256 records and the bill of materials (PA-78) |
| SR-5(1), SR-5(2) | Adequate supply; assessments before selection | Not required. Done in part: the PRO-SR-1 check before a component is used |
| SR-6(1) Testing and Analysis | Tests what suppliers provide | Not required. Done in part: release inspection (section 3.8) |
| SR-7 Supply Chain Operations Security | Hides supply chain information from adversaries | Not required. The plan and the register are restricted |
| SR-9 Tamper Resistance and Detection | Resists and detects tampering | Not required: selected at High only. Done in part: SHA-256 checks of each release |
| SR-10 enhancements, SR-11(3) | Further inspection; scanning for counterfeits | Not required |
