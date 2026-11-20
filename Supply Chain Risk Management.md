# \<System Name\> Supply Chain Risk Management

## 1 Purpose

This document sets out how \<System Name\> manages the risk that it is harmed through what it is built from, where it is hosted and who supplies it, to meet the 12 Supply Chain Risk Management (SR) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design, and is the supply chain risk management plan that SR-2 requires, on the headings of CSS: the principles, the system context, the team, the risks at each stage, the supplier register, the risk tolerance, how components come in, notices, inspection, authenticity and disposal, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.19 (Table 28). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (SR). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (SR), and the steps people follow are in \<Procedures\> (SR). The critical components are in \<Risk Assessment Management\>, section 3.9, the supply chain risk review in its section 3.4, the external services in \<System and Services Acquisition Management\>, section 3.7, and the integrity baseline in \<System and Information Integrity Management\>, section 3.5.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. Any settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.19 (Table 28).

## 3 The supply chain risk management plan

### 3.1 Principles

Controls met here: SR-2, SR-3.

1. **Know the supply chain.** Every supplier is named, with its criticality.
2. **One way in.** Every package comes through one checked source.
3. **Fix and verify.** A release is built from exactly the components recorded for it, and can be shown to be so.
4. **Hear about problems.** Suppliers and advisories tell us when something goes wrong.
5. **Nothing left behind.** \<System Name\> data is removed before anything leaves.

These carry out the principles and rules of \<Policy\>, sections SR.3 and SR.4.

![Figure 1: How components reach \<System Name\>, and the checks on the way](figures/srm-figure-1.png)

**Figure 1: How components reach \<System Name\>, and the checks on the way**

### 3.2 System context

Controls met here: SR-2.

\<System Name\> is three .NET 10 web applications and a PostgreSQL 18 database, to run as Windows services on two Windows Server 2025 servers hosted by \<Organisation\>. They are built and tested in container images. Its impact level is Moderate. Users sign in through \<Organisation\>'s PingFederate, and access is decided by Active Directory groups.

This plan covers \<System Name\>, its software packages, container images, browser files, build tools, hosting and hardware.

What it is built from: 59 packages for API, 40 for UI application and 34 for Admin application, counting those pulled in; two Microsoft base images and the PostgreSQL image; and two browser libraries from jsDelivr.

### 3.3 The supply chain team

Controls met here: SR-2, SR-2(1), SR-6.

The supply chain team is the system owner, the security officer, a developer and \<Organisation\>'s IT service desk. It keeps this plan current, reviews the critical suppliers every 12 months and before a new critical supplier is used, on TPL-16, and handles notices of compromise (PRO-SR-2, PRO-SR-5). The system owner leads it and approves the plan.

The team reviews this plan every 12 months, and after a significant change (PRO-SR-2). The plan is restricted, under version control, and held in the restricted store. \<Organisation\>'s part is evidenced through EV-SR-01.

### 3.4 Risks across the lifecycle

Controls met here: SR-2, SR-3.

**Table 1: Supply chain risks by stage**

| Stage | Risk | Response |
| --- | --- | --- |
| Research and development | A harmful, vulnerable or look-alike package is added | PRO-SR-1 check, then into the offline feed |
| Design | A design relies on an unsuitable supplier | Supplier register; review before a new critical supplier |
| Manufacturing | Hardware is altered before arrival | \<Organisation\> inspects |
| Acquisition | A supplier makes no security commitment | \<Organisation\>'s contract; open-source security policies checked |
| Delivery | A package, image or release is altered in transit | Lock files, signed-package trust, image digests, release SHA-256 values |
| Integration | A new component weakens a control | Release tests and Test-SupplyChain.ps1 |
| Operation and maintenance | A known flaw appears in a component | Monthly and release checks; \<Procedures\>, PRO-SI-1 |
| Disposal | Data leaves with a component | PRO-MP-3 |

### 3.5 Supplier register

Controls met here: SR-3, SR-5, SR-6, SR-8.

Criticality follows the critical components in \<Risk Assessment Management\>, section 3.9: High where a compromise would reach documents, or the way people sign in. Advisories are watched through the sources in \<System and Information Integrity Management\>, section 3.3.

**Table 2: Supplier register**

| Supplier | What it supplies | Criticality | How it reaches \<System Name\> | Evidence | Notification route | Last review | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \<Organisation\> | Hosting, network, hardware, service desk, central logging, and sign-in through PingFederate and Active Directory | High | Contract | EV-SR-01, EV-SR-02 | Security contact to the security officer, within 24 hours | \[Date\] (\<Risk Assessment Management\>, section 3.4) | \[Date\] |
| Microsoft | .NET 10, ASP.NET Core and Entity Framework packages, Windows Server 2025 | High | nuget.org; the VM build | Published lifecycle and security advisories | Microsoft and .NET advisories | \[Date\] | \[Date\] |
| Microsoft container registry (mcr.microsoft.com) | .NET SDK and runtime base images | High | Pulled by digest at build | Published image digests | .NET advisories | \[Date\] | \[Date\] |
| nuget.org | The package registry for all other packages | High | Mirrored into the offline feed after the PRO-SR-1 check; vulnerability data | Repository signatures on every package | GitHub Advisory Database | \[Date\] | \[Date\] |
| Npgsql project | PostgreSQL driver and Entity Framework provider | High | nuget.org | Open-source project; security policy published | GitHub advisories | \[Date\] | \[Date\] |
| PostgreSQL Global Development Group, through Docker Hub | The postgres:18 database image | High | Docker Hub (docker.io), pulled by digest | Official image; published support dates | PostgreSQL security announcements | \[Date\] | \[Date\] |
| GitHub | Source code hosting | High | Private repositories | Published security terms (EV-SA-03) | GitHub advisories | \[Date\] | \[Date\] |
| OfflineModules packages (in-house, system owner) | Access control modules | High | Offline feed only, by package source mapping | SHA-256 index in the feed | Internal | \[Date\] | \[Date\] |
| Six Labors (ImageSharp) | Image processing | Medium | nuget.org | Six Labors Split License, community tier | GitHub advisories | \[Date\] | \[Date\] |
| SkiaSharp (Microsoft and Mono) | Image rendering and its Linux native library | Medium | nuget.org | Open-source project | GitHub advisories | \[Date\] | \[Date\] |
| jsDelivr (cdn.jsdelivr.net) | Bootstrap Icons and OpenSeadragon in the browser | Medium | Copied into \<System Name\> and served by it, with SHA-256 values recorded | None | Library advisories | \[Date\] | \[Date\] |
| Swashbuckle and Azure.Storage.Blobs | API documentation; an unused storage client | Low | nuget.org; left out of release builds | Open-source and Microsoft packages | GitHub advisories | \[Date\] | \[Date\] |

### 3.6 Risk tolerance

Controls met here: SR-2, SR-3.

No critical component may be used without a known source and a SHA-256 record. A known flaw in any component is fixed to the timetable in \<Risk Assessment Management\>, section 3.6. A High supplier that has not been reviewed within 12 months, or a component that fails a check in section 3.8, is recorded in \<Risk List\> for a decision.

### 3.7 How components come in

Controls met here: SR-3, SR-5, SR-10, SR-11.

Three processes find and address weaknesses in the supply chain: component checks before use (PRO-SR-1), supplier reviews (PRO-SR-2) and release inspection (PRO-SR-3). They are coordinated with \<Organisation\>'s IT service desk and the suppliers in section 3.5. The processes and controls are documented in this plan and in \<System Security Plan\>.

**Table 3: How each component comes in**

| Component | How it comes in |
| --- | --- |
| OfflineModules packages | Offline feed only, by package source mapping |
| All other packages | Mirrored into the offline feed after the PRO-SR-1 check; lock files in locked mode; trust policy for nuget.org's repository signature; NuGet's audit on |
| Base and database images, for the build and the test stacks | Pinned by digest |
| Browser libraries | Served by \<System Name\> |
| Releases | SHA-256 values and a CycloneDX bill of materials, checked before installation |
| Hardware and hosting | Inspected, controlled under repair and disposed of by \<Organisation\>, with evidence |

### 3.8 Notices, inspection, authenticity and disposal

Controls met here: SR-8, SR-10, SR-11, SR-11(1), SR-11(2), SR-12.

1. **Notices** (SR-8). \<Organisation\> reports a supply chain compromise to the security officer within 24 hours, and shares assessment or audit results that affect \<System Name\> (EV-SR-01). For open-source suppliers, their published advisories are the notice, through the sources in \<System and Information Integrity Management\>, section 3.3. Each notice that applies is recorded on TPL-7, and a compromise is handled as an incident (PRO-SR-5).
2. **Inspection** (SR-10). Release packages, the test images and \<System Name\>'s application files are checked against their recorded SHA-256 values at each release, before installation, and whenever tampering is suspected. A different value, an unexpected package source or damaged packaging is a sign of tampering. \<Organisation\> inspects hardware (PRO-SR-3; EV-SR-02).
3. **Authenticity** (SR-11). Under policy rule R11, package names are checked against look-alikes, and packages come only from the offline feed under a signed-package trust policy. A suspected counterfeit is refused and reported to its source, the security officer, \<Organisation\>, the package registry and, if serious, the NCSC. \<Organisation\> trains its buyers every year, and keeps control of hardware sent for repair (PRO-SR-4).
4. **Disposal** (SR-12). For hardware, media, data and documents, \<System Name\> data is removed first (PRO-MP-3), and \<Organisation\> disposes of the component and confirms in writing (PRO-SR-6).

### 3.9 What \<Organisation\> provides

Controls met here: SR-2(1), SR-3, SR-5, SR-6, SR-8, SR-10, SR-11(1), SR-11(2), SR-12.

**Table 4: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Approved suppliers, a seat on the supply chain team, and notice of a compromise within 24 hours | SR-2(1), SR-3, SR-5, SR-6, SR-8 | Its suppliers are approved, the IT service desk joins the team, and a compromise reaches the security officer within 24 hours | EV-SR-01 |
| Hardware inspection, buyers' training, control of equipment under repair, and disposal | SR-10, SR-11(1), SR-11(2), SR-12 | Each is done, with records | EV-SR-02 |

### 3.10 Policy and procedures

Controls met here: SR-1.

1. **Policy.** \<Policy\> (SR) is a system-level policy, shared with developers and administrators. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (SR) holds six procedures, PRO-SR-1 to PRO-SR-6. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control.

## Appendix A Supply chain controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Table 5 says where the design goes some way towards them.

**Table 5: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| SR-3(1) to SR-3(3) | Diverse supply base; limiting harm; flowing controls down to sub-tier suppliers | Not required. Done in part: the risk tolerance limits harm (section 3.6) |
| SR-4 Provenance | Records where each component came from and every change to it | Not required. Done in part in design: the offline feed's SHA-256 records and the bill of materials |
| SR-5(1), SR-5(2) | Adequate supply; assessments before selection | Not required. Done in part: the PRO-SR-1 check before a component is used |
| SR-6(1) Testing and Analysis | Tests what suppliers provide | Not required. Done in part: release inspection (section 3.8) |
| SR-7 Supply Chain Operations Security | Hides supply chain information from adversaries | Not required. The plan and the register are restricted |
| SR-9 Tamper Resistance and Detection | Resists and detects tampering | Not required: selected at High only. Done in part: SHA-256 checks of each release |
| SR-10 enhancements, SR-11(3) | Further inspection; scanning for counterfeits | Not required |
