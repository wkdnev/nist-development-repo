# \<System Name\> Supply Chain Risk Management

## 1 Purpose

This document sets out how \<System Name\> manages the risk that it is harmed through what it is built from, where it is hosted and who supplies it, to meet the 12 Supply Chain Risk Management (SR) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design, and is the supply chain risk management plan that SR-2 requires, on the headings of CSS: the principles, the system context, the team, the risks at each stage, the supplier register, the risk tolerance, how components come in, notices, inspection, authenticity and disposal, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.19 (Table 28). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (SR). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (SR), and the steps people follow are in \<Procedures\> (SR). The critical components are in \<Risk Assessment Management\>, section 3.9, the supply chain risk review in its section 3.4, the external services in \<System and Services Acquisition Management\>, section 3.7, and the integrity baseline in \<System and Information Integrity Management\>, section 3.5.

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

\<System Name\> is three .NET 10 web applications, the UI application, the Admin application and the API, with a shared library built into all three, and a Microsoft SQL Server 2022 database (\<System Description\>, sections 6.3 and 6.4). The applications run as Windows services, each under its own group managed service account, on two Windows Server 2025 virtual servers in \<Organisation\>'s data centre. The test environment is a throwaway copy of the whole system, built from a tagged release. Its impact level is Moderate. Users sign in through \<Organisation\>'s PingFederate, and the API reads their Active Directory groups over LDAPS to decide their access. \<System Name\> is built in-house under \<Organisation\>'s corporate SDLC.

This plan covers \<System Name\>, its software packages, browser libraries, build tools, hosting and hardware.

What it is built from: the Microsoft products in the reference stack; \[number\] packages for the API, \[number\] for the UI application and \[number\] for the Admin application, counting those pulled in, all through the in-house package feed; and the browser libraries the pages need, packaged with the UI application and served by it.

### 3.3 The supply chain team

Controls met here: SR-2, SR-2(1), SR-6.

The supply chain team is the system owner, the security officer, a developer and \<Organisation\>'s IT service desk. It keeps this plan current, reviews the critical suppliers every 12 months and before a new critical supplier is used, on TPL-16, and handles notices of compromise (PRO-SR-2, PRO-SR-5). The system owner leads it and approves the plan.

The team reviews this plan every 12 months, and after a significant change (PRO-SR-2). The plan is restricted, under version control, and held in the restricted store. \<Organisation\>'s part is evidenced through EV-SR-01.

### 3.4 Risks across the lifecycle

Controls met here: SR-2, SR-3.

**Table 1: Supply chain risks by stage**

| Stage | Risk | Response |
| --- | --- | --- |
| Research and development | A harmful, vulnerable or look-alike package is added | PRO-SR-1 check, then into the in-house package feed |
| Design | A design relies on an unsuitable supplier | Supplier register; review before a new critical supplier |
| Manufacturing | Hardware is altered before arrival | \<Organisation\> inspects |
| Acquisition | A supplier makes no security commitment | \<Organisation\>'s contract; open-source security policies checked |
| Delivery | A package or release is altered in transit | Lock files, signed-package trust, and releases from a signed tag with SHA-256 values |
| Integration | A new component weakens a control | Release tests and Test-SupplyChain.ps1 |
| Operation and maintenance | A known flaw appears in a component | Monthly and release checks; \<Procedures\>, PRO-SI-1 |
| Disposal | Data leaves with a component | PRO-MP-3 |

### 3.5 Supplier register

Controls met here: SR-3, SR-5, SR-6, SR-8.

Criticality follows the critical components in \<Risk Assessment Management\>, section 3.9: High where a compromise would reach items, or the way people sign in. Advisories are watched through the sources in \<System and Information Integrity Management\>, section 3.3.

**Table 2: Supplier register**

| Supplier | What it supplies | Criticality | How it reaches \<System Name\> | Evidence | Notification route | Review |
| --- | --- | --- | --- | --- | --- | --- |
| \<Organisation\> | Hosting on its virtual platform and data centre, network, hardware, service desk, central logging, sign-in through PingFederate and Active Directory, ServiceNow, and the corporate SDLC with its source repositories, build pipeline and in-house package feed (\<System Description\>, section 10) | High | Contract and corporate services | EV-SR-01, EV-SR-02 | Security contact to the security officer, within 24 hours | Every 12 months, and before a new critical service is used |
| Microsoft | Windows Server 2025, with Defender and BitLocker; Microsoft SQL Server 2022; .NET 10, ASP.NET Core 10 and Blazor Server; Entity Framework Core 10 with the SQL Server provider (Microsoft.Data.SqlClient) | High | The server build, by \<Organisation\>, with updates through the proxy; packages through the in-house package feed | Published lifecycle and security advisories | Microsoft and .NET advisories | Every 12 months |
| nuget.org | The package registry behind the in-house package feed | High | Copied into the in-house package feed after the PRO-SR-1 check; vulnerability data | Repository signatures on every package | GitHub Advisory Database | Every 12 months |
| \<System Name\>'s developers (in-house) | The shared library, \<Code\>\_Shared, which holds the data model, the access checks and the audit record format, built into all three applications | High | Built from \<System Name\>'s own source repositories under the corporate SDLC | Reviewed changes and the release record | Internal | Every 12 months |
| \[Supplier of each other third-party package\] | \[Packages the application needs beyond the reference stack\] | \[Medium or Low\] | The in-house package feed | \[Licence and security policy\] | \[Advisory source\] | Every 12 months |
| \[Supplier of each browser library\] | Third-party scripts and styles the pages need, for example a document viewer or an icon set | Medium | Through the in-house package feed, packaged with the UI application and served by \<System Name\> itself, with SHA-256 values recorded. No content delivery service is used | \[Licence and security policy\] | Library advisories | Every 12 months |
| \[Supplier of the API documentation package\] | Interactive API documentation, for development only | Low | The in-house package feed; left out of release builds | \[Licence\] | \[Advisory source\] | Every 12 months |

### 3.6 Risk tolerance

Controls met here: SR-2, SR-3.

No critical component may be used without a known source and a SHA-256 record. A known flaw in any component is fixed to the timetable in \<Risk Assessment Management\>, section 3.6. A High supplier that has not been reviewed within 12 months, or a component that fails a check in section 3.8, is recorded in \<Risk List\> for a decision.

### 3.7 How components come in

Controls met here: SR-3, SR-5, SR-10, SR-11.

Three processes find and address weaknesses in the supply chain: component checks before use (PRO-SR-1), supplier reviews (PRO-SR-2) and release inspection (PRO-SR-3). They are coordinated with \<Organisation\>'s IT service desk and the suppliers in section 3.5. They sit within \<Organisation\>'s corporate SDLC, which provides the one checked package feed, lock files and a software bill of materials for each release (\<System Description\>, section 7.12). The processes and controls are documented in this plan and in \<System Security Plan\>.

**Table 3: How each component comes in**

| Component | How it comes in |
| --- | --- |
| The shared library | Built from \<System Name\>'s own source repositories, under the corporate SDLC |
| All other packages | Through the in-house package feed only, by package source mapping, after the PRO-SR-1 check; lock files in locked mode; trust policy for nuget.org's repository signature; NuGet's audit on |
| Windows Server 2025 and SQL Server 2022 | Installed by \<Organisation\>'s server build from Microsoft's media, and updated through \<Organisation\>'s proxy |
| Browser libraries | Through the in-house package feed, packaged with the UI application and served by \<System Name\> itself. No content delivery service |
| Releases | From a signed tag, with SHA-256 values and a CycloneDX bill of materials, checked before installation |
| Hardware and hosting | Inspected, controlled under repair and disposed of by \<Organisation\>, with evidence |

### 3.8 Notices, inspection, authenticity and disposal

Controls met here: SR-8, SR-10, SR-11, SR-11(1), SR-11(2), SR-12.

1. **Notices** (SR-8). \<Organisation\> reports a supply chain compromise to the security officer within 24 hours, and shares assessment or audit results that affect \<System Name\> (EV-SR-01). For open-source suppliers, their published advisories are the notice, through the sources in \<System and Information Integrity Management\>, section 3.3. Each notice that applies is recorded on TPL-7, and a compromise is handled as an incident (PRO-SR-5).
2. **Inspection** (SR-10). Release packages and \<System Name\>'s application files are checked against their recorded SHA-256 values at each release, before installation, and whenever tampering is suspected. A different value, an unexpected package source or damaged packaging is a sign of tampering. \<Organisation\> inspects hardware (PRO-SR-3; EV-SR-02).
3. **Authenticity** (SR-11). Under policy rule R11, package names are checked against look-alikes, and packages come only from the in-house package feed under a signed-package trust policy. A suspected counterfeit is refused and reported to its source, the security officer, \<Organisation\>, the package registry and, if serious, the NCSC. \<Organisation\> trains its buyers every year, and keeps control of hardware sent for repair (PRO-SR-4).
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

\<Policy\> (SR) and \<Procedures\> (SR) meet SR-1. Who they are shared with is in \<Policy\>, section SR.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
