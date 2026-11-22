# \<System Name\> Risk Assessment Management

## 1 Purpose

This document sets out how \<System Name\> is designed to assess risk and respond to it, to meet the 10 Risk Assessment (RA) controls in the CSS Moderate baseline. RA-8, the privacy impact assessment, is in the CSS privacy baseline and is met in \<PII Processing Management\> and \<Data Protection Impact Assessment\>.

Section 3 is the design: the security categorisation, the risk assessment, the supply chain risk assessment, what is monitored for vulnerabilities, the vulnerability timetable, how findings are analysed, shared and reported, the risk response, the critical components, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.



## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.15 (Table 24). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (RA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (RA), and the steps people follow are in \<Procedures\> (RA). The risks, and the method that rates them, are in \<Risk List\>; the categorisation is recorded in \<System Security Plan\>, section 3.3, as RA-2 requires; and the suppliers are managed under the supply chain plan, \<Supply Chain Risk Management\>.

## 3 The design

### 3.1 Principles

Controls met here: RA-3, RA-5, RA-7, RA-9.

1. **Risk-based.** Decisions follow the rated risk, assessed by a stated method.
2. **Named decisions.** A named person decides each risk, at the level its rating calls for.
3. **Keep looking.** Vulnerabilities are looked for all the time, not only at assessment.
4. **Exploited first.** A flaw that is being exploited is dealt with ahead of everything else.
5. **Know what matters most.** The critical components get the closest attention.

These carry out the principles and rules of \<Policy\>, sections RA.3 and RA.4.

![Figure 1: How risk is assessed and answered in \<System Name\>](figures/ram-figure-1.png)

**Figure 1: How risk is assessed and answered in \<System Name\>**

### 3.2 Security categorisation

Controls met here: RA-2.

\<System Name\> is categorised Moderate: confidentiality Moderate, integrity Moderate and availability Low (\<System Description\>, P-01), unless its application profile sets otherwise. Each of its information types (\<System Description\>, section 3.4, Table 6) is mapped to CSS and rated under CSS, and the system takes the highest level of each. An application rated High in any objective is outside the reference system. The record, with the rationale for each level, is in \<System Security Plan\>, section 3.3, as RA-2 requires. \[Name\] owns the information types and confirms their levels, and the authorising official, \[Name\], approves the categorisation (D-RA-01).

Availability is Low because the 120-hour maximum tolerable downtime (\<System Description\>, P-14) means a loss of availability has a limited adverse effect; "business critical" means important to \<Organisation\>, not that \<System Name\> must always be available.

The last information type, held by every application built on the reference system, covers the sign-in identities and the audit records. \<System Name\> holds no accounts or credentials, as users sign in through PingFederate and the API reads their groups from Active Directory.

The categorisation is reviewed with the risk assessment, and whenever an information type is added or changed.

### 3.3 Risk assessment

Controls met here: RA-3, RA-7.

\<System Name\>'s risk assessment is the Risk List, \<Risk List\>. It follows CSS: a threat source exploits a weakness, with a likelihood, to cause an impact. The method is set out in full in its section 4, beside the risks it rates, so that the Risk List can be read on its own. Table 1, below, summarises it. The threats to the application are modelled before it is built, from its profile and functions, and again at each significant change, and the threat model is kept in the Risk List, section 2.1 (\<System Description\>, NFR-083). Each threat in it leads to a risk in the register.

**Table 1: The risk method at a glance**

| Element | Design | Where it is held |
| --- | --- | --- |
| Threat sources | Adversarial, accidental, structural and environmental, each with examples for \<System Name\> | \<Risk List\>, Table 3c |
| Threat model | Each threat event, the critical components and functions it reaches (section 3.9), and the risk it leads to | \<Risk List\>, section 2.1, Table 1a |
| Likelihood | Low, Medium or High, on a scale of how able and motivated the source is and what stands in its way | \<Risk List\>, Table 3a |
| Impact | Low, Medium or High, for the items, for the people they are about and for \<Organisation\>, on a scale set within \<System Name\>'s Moderate categorisation. A harm CSS would rate High goes to the authorising official with a review of the categorisation | \<Risk List\>, Table 3b |
| Rating | A matrix that weights impact: a High impact never rates below Medium, and a Low impact never above Low, because \<System Name\>'s harm is driven by what it holds | \<Risk List\>, Table 3 |
| Uncertainty | Where the evidence is a single test or a document review, the higher of the two plausible ratings is used. Ratings set before the evidence was seen are marked provisional | \<Risk List\>, section 4.1 and Table 3d |
| Privacy risk | Rated by the same method. The data protection impact assessment adds the effects on individuals | \<Risk List\>; \<Data Protection Impact Assessment\> |
| Who decides | Low: the system owner. Medium: the authorising official, on the system owner's advice. High: the authorising official, and only for a stated period while a fix runs. A risk that is reduced is decided at its residual rating. Any tailoring: the authorising official, whatever the rating | \<Risk List\>, section 4.2 |
| Tolerance | The thresholds are \<System Name\>'s own, and the Head of Cyber checks them against \<Organisation\>'s risk management strategy and risk appetite | EV-PM-01 |

**Table 2: When the risk assessment is reviewed**

| When | What is done | Who | Record |
| --- | --- | --- | --- |
| Every 12 months (P-74) | The threat model and each risk are reviewed against the method, and each rating, status and last-reviewed date updated. Each acceptance is checked against its review date, and each Medium and High risk for a decision | System owner | TPL-23; \<Risk List\> |
| After a significant change, an incident or a new test result | The same, for the threats and risks it affects | System owner | TPL-23; \<Risk List\> |
| After each review | The results are shared | System owner, with the authorising official and the Head of Cyber | TPL-23 |
| When a risk needs a decision | Decided by the person its rating calls for | System owner or authorising official | \<Decision Register\> |
| At each review | The categorisation is checked against the information \<System Name\> holds, and any change goes to the authorising official (section 3.2) | System owner | TPL-23 |

After a significant change, such as a change to how users sign in or to where the applications run, the risk assessment is reviewed as a whole, as RA-3 and PRO-RA-1 require.

### 3.4 Supply chain risk assessment

Controls met here: RA-3(1).

Every 12 months, before a new supplier or a new kind of component is added, and after a significant change to the system or where it runs, the system owner and the developers review each item in the supply chain for its origin, support, known problems and end of support (PRO-RA-2). They use the risks by stage and the supplier register in \<Supply Chain Risk Management\>, sections 3.4 and 3.5, the latest package check, and the bill of materials. Each review is recorded on TPL-23, and any new risk goes into the Risk List; the risk of a harmful package entering a release is R-RA-06. The intervals are P-74's. The supply chain plan, \<Supply Chain Risk Management\>, holds the suppliers and how they are managed; this section holds the risk assessment.

### 3.5 What is monitored for vulnerabilities

Controls met here: RA-5, RA-5(2), RA-5(5).

**Table 3: Components checked for vulnerabilities**

| Component | How it is checked | Who | How often |
| --- | --- | --- | --- |
| Windows Server 2025, on both servers | Vendor updates, and a credentialed scan (PRO-RA-3) | Windows server administrator | Monthly, and at each release (\<System Description\>, P-30) |
| Microsoft SQL Server 2022 | Vendor updates and security advisories, and the credentialed scan of the database server | Database administrator | Monthly |
| .NET and NuGet packages, through the in-house package feed | The package vulnerability report at each build, and Test-Vulnerability.ps1 at each release | Developers | Each build, and monthly |
| Browser libraries, served by \<System Name\> itself | Vendor security announcements, and Test-Vulnerability.ps1, which checks each library's version in the browser library manifest against the GitHub Advisory Database; NuGet's audit does not cover them | Developers | Monthly, and at each release |
| \<System Name\>'s own applications: UI application, Admin application and API | A web application scan, reaching them as a user and as an outsider would; the static analysis in the build; and an independent penetration test before go-live | Developers | Each release |
| Server and database settings | The configuration scan against the baseline in \<Configuration Management\>, which finds the improper configurations RA-5 also asks about | Windows server administrator, database administrator | Monthly |
| All components, for exploited flaws | CISA's Known Exploited Vulnerabilities catalogue and \<Organisation\>'s alerts (PRO-RA-4) | Security officer | Each working day, from an alert on new entries (\<Security Operating Procedures\>, C50) |

Monitoring also starts whenever a new vulnerability that may affect \<System Name\> is reported, through these sources or the reporting route in section 3.7.

The scanner must:

1. scan both servers with an account approved for scanning, so that the scan sees what an administrator sees (RA-5(5));
2. update its definitions before each scan (RA-5(2));
3. name each platform and flaw by a standard identifier, CPE and CVE, and rate each flaw by CVSS, so that its results and the package check's can be compared and measured the same way (RA-5b.1 and b.3);
4. find ports, protocols and services that should not be reachable, against the allowed flows F1 to F11 in \<System Description\>, section 6.5, \<Access Control Management\>, section 3.6, and the host firewall rules in \<System and Communications Protection Management\>, section 3.2;
5. scan \<System Name\>'s three applications at each release, as this section sets out.

Items 4 and 5 come from the CSS guidance on RA-5.

Improper configurations are found by the monthly configuration scan against the baseline, which uses a standard checklist format (\<Configuration Management\>; \<Procedures\>, PRO-CM-7; RA-5b.1 and b.2).

### 3.6 Vulnerability timetable

Controls met here: RA-5.

This is the one timetable for vulnerabilities in \<System Name\>, its packages and its servers (\<System Description\>, P-11). It replaces any other limit for vulnerabilities, including the general limits for POA&M items in \<Policy\> (CA). It meets the Cyber Essentials limit of 14 days for high and critical updates, which \<Organisation\> holds.

**Table 4: Vulnerability timetable**

| Severity | How it is set | Fix or mitigate within |
| --- | --- | --- |
| Exploited | In CISA's Known Exploited Vulnerabilities catalogue, or confirmed exploited by the vendor or \<Organisation\> | 3 days, as an emergency change (PRO-RA-4) |
| Critical | Vendor rating Critical, or CVSS base 9.0 or more | 14 days |
| High | Vendor rating High, or CVSS base 7.0 to 8.9, or no rating given | 14 days |
| Medium | Vendor rating Medium or Moderate, or CVSS base 4.0 to 6.9 | 30 days |
| Low | Vendor rating Low, or CVSS base below 4.0 | 90 days |

The clock starts when the fix is released, or when \<System Name\>'s use of the flaw is detected if that is later. The vendor's rating comes first; the CVSS version is recorded on TPL-7. Mitigating means reducing the risk without the fix, for example by turning off the affected feature or blocking its route. A fix that cannot meet its time goes to a risk decision under \<Policy\>, section 1.2, with its compensating measure.

### 3.7 Analysing, sharing and reporting

Controls met here: RA-5, RA-5(11).

1. **Analysis.** Within 5 working days of each scan or check, the security officer records each finding on TPL-7: its severity under section 3.6, whether \<System Name\> uses the affected part, and its due date (PRO-RA-3).
2. **False positives.** A finding that does not apply, such as a flaw in a feature \<System Name\> does not call, is marked as a false positive on TPL-7 with the reason, and checked again at the next scan.
3. **Fixing.** The people responsible fix or mitigate each finding within its time, as a change (\<Configuration Management\>). An exploited flaw is fixed or mitigated as an emergency change, and the security officer confirms it and tells the system owner (PRO-RA-4).
4. **Sharing.** After each scan the security officer shares each finding that applies with the developers and the Windows server administrator, so that the same flaw is fixed wherever it occurs. A finding that may affect \<Organisation\>'s other systems also goes to its security contact, so that it can be removed there too (PRO-RA-5).
5. **Reports from anyone.** Anyone may report a vulnerability in \<System Name\> to \<Organisation\>'s security contact, which passes the report to the security officer, who records it on TPL-7 and handles it as a scan finding. CSS asks for a public channel, so the contact must be published where people outside \<Organisation\> can find it, for example in a security.txt file on its website (RFC 9116): \[Where the contact is published\] (EV-RA-01). Its published terms must authorise research in good faith, and may ask the reporter to allow a set time for a fix before disclosing the flaw, but must not require it to be kept secret for ever. The time asked for is 90 days (EV-RA-01).
6. **Flaws in other parties' components.** A flaw found in another party's package or browser library is reported to its maintainer through their published route, and noted on TPL-7.

### 3.8 Risk response

Controls met here: RA-7.

Findings come from four sources: security assessments, privacy assessments, monitoring and audits. Each is answered the same way, within the risk tolerance in section 3.3.

**Table 5: How a finding is answered**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 Record | Each finding that is not satisfied becomes an entry in the Risk List's non-compliance register, linked to the risk it adds to | System owner | \<Risk List\>, section 5 |
| 2 Rate | The entry is rated by the method in section 3.3 | System owner | \<Risk List\> |
| 3 Decide | The person the rating calls for decides: accept, remediate, approve, obtain evidence from \<Organisation\>, or tailor | System owner for Low; authorising official for Medium and High, and for any tailoring (PRO-PL-4) | \<Decision Register\>; acceptances in \<Risk List\>, section 3 |
| 4 Plan | A remediation goes into the Plan of Action and Milestones, with milestones and a due date. A vulnerability follows the timetable in section 3.6 | System owner | \<Plan of Action and Milestones\> |
| 5 Review | Each acceptance is reviewed by its review date: Medium every 6 months and Low every 12 | System owner; authorising official | \<Risk List\>, section 3 |

A monitoring finding, such as a scan result, is first recorded on TPL-7 (section 3.7). It enters the Risk List only if it cannot be fixed in time.

### 3.9 Critical components

Controls met here: RA-9.

**Method.** A component is critical if its failure or compromise would expose or lose the items, or defeat a security control. Each component in the authorisation boundary, and each outside service it relies on, is judged by the impact levels in \<System Security Plan\>, section 3.3, the recovery priorities in \<Contingency Planning Management\>, section 3.3, and whether it lies on the path to the items. A component that gives unmediated access to a critical component is critical too. The developers' criticality analysis (SA-15(3)) uses this list.

**Table 6: Critical components**

| Component | Why it is critical | If it fails or is compromised |
| --- | --- | --- |
| Database server | Holds every item, its files, the schema definitions and the audit records, each schema in its own database schema | All items are exposed or lost |
| Application server | Runs all three applications, and holds their data protection key rings and the encrypted export working area. Whoever controls it reaches the database through the API | Every item reachable, and the applications' controls bypassed |
| API | The only route to the database. Reads each person's groups from Active Directory over LDAPS, and checks each request's sign-in, role and schema access for the other two applications | Access controls can be bypassed, and every item read |
| UI application | Users' pages for items, reached after sign-in through PingFederate; also lets business owners approve disposals due under the retention schedule, and gives the legal adviser's delegate the search across every schema | Items shown to the wrong person, a user's sign-in taken over, items disposed of too early, or one person's items found across every schema by someone not entitled to search |
| Admin application | Sets which Active Directory groups open each schema, administers schemas and system settings, runs fixed diagnostics, gives auditors the audit log, and gives the security officer the last sign-in report. It shows no item content | Schema access granted to the wrong groups, or schemas changed or closed |
| Audit records | Show who did what | Misuse cannot be traced or proved |
| Backup store | Holds a full, encrypted copy of every item | Every item exposed from a stolen backup and its key, or lost |
| Export working area | Holds encrypted working copies of items for each export job, deleted as \<System Description\>, P-20 sets | Items disclosed outside their schema's access |
| Key store | Holds the token signing key, the audit chain key, the OpenID Connect client credential and the exported backup encryption certificate. There is no database password: the API uses Windows authentication | Calls between the applications can be forged, the audit chain rewritten unnoticed, or no backup can be restored |
| Data protection key rings | Protect each application's authentication cookie and anti-forgery tokens | Sign-in cookies can be forged or read |
| PingFederate, with Active Directory (\<Organisation\>) | PingFederate authenticates every user with multi-factor authentication; Active Directory holds the groups, read by the API over LDAPS, that decide each role and each schema's access | Anyone could sign in as another user, or be given any role or schema |

PingFederate with Active Directory is critical because \<System Name\> holds no accounts and relies on \<Organisation\> to authenticate every user. The application server and the export working area are critical because each gives a path to the items that goes round the other controls.

**Critical functions.** CSS asks for critical functions as well as components. Five functions would expose or lose the items if they failed: signing in and deciding access (PingFederate with Active Directory, the API, the key store and the data protection key rings); storing and showing items (the database server, the application server, the API and the UI application); administering schemas and access (the Admin application); recording who did what (the audit records); and recovering items (the backup store).

The list is made at design, before the application is built, and reviewed at each major release and after a significant change (PRO-RA-6). The system owner approves it (D-RA-04).

### 3.10 What \<Organisation\> provides

Controls met here: RA-3, RA-3(1), RA-5, RA-5(11), RA-7, RA-9.

**Table 7: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| The security contact for vulnerability reports | RA-5(11) | It is published, and passes any report about \<System Name\> to the security officer | EV-RA-01 |
| A shared scanning service, or a list of exploited flaws it tracks, if it offers one | RA-5 | Whether \<System Name\> can use it | EV-RA-01 |
| The risk management strategy and risk appetite | RA-3, RA-7 | System risk decisions respect them, and the Head of Cyber confirms the thresholds against them | EV-PM-01 |
| PingFederate and Active Directory | RA-9 | PingFederate authenticates every user, and Active Directory holds the groups that decide access; they are critical components (section 3.9) | The AC evidence requests in \<Evidence Requests\> |
| Hosting, network and hardware, and their suppliers | RA-3(1) | Their supply chain risk is managed, and the approved suppliers are known | EV-SR-01, EV-SR-02 |

### 3.11 Policy and procedures

Controls met here: RA-1.

\<Policy\> (RA) and \<Procedures\> (RA) meet RA-1. Who they are shared with is in \<Policy\>, section RA.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
