# \<System Name\> Risk Assessment Management

## 1 Purpose

This document sets out how \<System Name\> is designed to assess risk and respond to it, to meet the 10 Risk Assessment (RA) controls in the CSS Moderate baseline.

Section 3 is the design: the security categorisation, the risk assessment, the supply chain risk assessment, what is monitored for vulnerabilities, the vulnerability timetable, how findings are analysed, shared and reported, the risk response, the critical components, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.15 (Table 24). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (RA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (RA), and the steps people follow are in \<Procedures\> (RA). The risks, and the method that rates them, are in \<Risk List\>; the categorisation is recorded in \<System Security Plan\>, section 3.3, as RA-2 requires; and the suppliers are managed under the supply chain plan, \<Supply Chain Risk Management\>.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. The settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

Appendix A lists the related controls and enhancements CSS does not select at Moderate.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.15 (Table 24).

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

\<System Name\> is categorised Moderate: confidentiality Moderate, integrity Moderate and availability Low. Each of its four information types was mapped to CSS and rated under CSS, and the system takes the highest level of each. The record, with the rationale for each level, is in \<System Security Plan\>, section 3.3, as RA-2 requires. \[Name\] owns the information types, and the authorising official, \[Name\], approves the categorisation.

Availability is Low because the 120-hour maximum tolerable downtime means a loss of availability has a limited adverse effect; "business critical" means important to \<Organisation\>, not that \<System Name\> must always be available.

The fourth information type covers the identities that arrive at sign-in and the audit records. \<System Name\> holds no accounts or credentials, as users sign in through PingFederate.

The categorisation is reviewed with the risk assessment, and whenever an information type is added or changed.

### 3.3 Risk assessment

Controls met here: RA-3, RA-7.

\<System Name\>'s risk assessment is the Risk List, \<Risk List\>. It follows CSS: a threat source exploits a weakness, with a likelihood, to cause an impact. The method is set out in full in its section 4, beside the risks it rates, so that the Risk List can be read on its own. Table 1, below, summarises it.

**Table 1: The risk method at a glance**

| Element | Design | Where it is held |
| --- | --- | --- |
| Threat sources | Adversarial, accidental, structural and environmental, each with examples for \<System Name\> | \<Risk List\>, Table 3c |
| Likelihood | Low, Medium or High, on a scale of how able and motivated the source is and what stands in its way | \<Risk List\>, Table 3a |
| Impact | Low, Medium or High, on the CSS scale, for the documents and for \<Organisation\> | \<Risk List\>, Table 3b |
| Rating | A matrix that weights impact: a High impact never rates below Medium, and a Low impact never above Low, because \<System Name\>'s harm is driven by what it holds | \<Risk List\>, Table 3 |
| Uncertainty | Where the evidence is a single test or a document review, the higher of the two plausible ratings is used. Ratings set before the evidence was seen are marked provisional | \<Risk List\>, section 4.1 and Table 3d |
| Privacy risk | Rated by the same method. The data protection impact assessment adds the effects on individuals | \<Risk List\>; \<Data Protection Impact Assessment\> |
| Who decides | Low: the system owner. Medium: the authorising official, on the system owner's advice. High: the authorising official, and only for a stated period while a fix runs | \<Risk List\>, section 4.2 |
| Tolerance | The thresholds are \<System Name\>'s own, and the Head of Cyber checks them against \<Organisation\>'s risk management strategy and risk appetite | EV-PM-01 |

**Table 2: When the risk assessment is reviewed**

| When | What is done | Who | Record |
| --- | --- | --- | --- |
| Every 12 months | Each risk is reviewed against the method, and its rating, status and last-reviewed date updated. Each acceptance is checked against its review date, and each Medium and High risk for a decision | System owner | TPL-23; \<Risk List\> |
| After a significant change, an incident or a new test result | The same, for the risks it affects | System owner | TPL-23; \<Risk List\> |
| After each review | The results are shared | System owner, with the authorising official and the Head of Cyber | TPL-23 |
| When a risk needs a decision | Decided by the person its rating calls for | System owner or authorising official | \<Decision Register\> |
| At each review | The categorisation is checked against the information \<System Name\> holds, and any change goes to the authorising official (section 3.2) | System owner | TPL-23 |

After a significant change, such as a change to how users sign in or to where the applications run, the risk assessment is reviewed as a whole, as RA-3 and PRO-RA-1 require.

### 3.4 Supply chain risk assessment

Controls met here: RA-3(1).

Every 12 months, before a new supplier or a new kind of component is added, and after a significant change to the system or where it runs, the system owner and the developers review each item in the supply chain for its origin, support, known problems and end of support (PRO-RA-2). They use the supplier register in \<Supply Chain Risk Management\>, the latest package and image check, and the bill of materials. Each review is recorded on TPL-23, and any new risk goes into the Risk List. The supply chain plan, \<Supply Chain Risk Management\>, holds the suppliers and how they are managed; this section holds the risk assessment.

### 3.5 What is monitored for vulnerabilities

Controls met here: RA-5, RA-5(2), RA-5(5).

**Table 3: Components checked for vulnerabilities**

| Component | How it is checked | Who | How often |
| --- | --- | --- | --- |
| Windows Server 2025, on both VMs | Vendor updates, and a credentialed scan (PRO-RA-3) | Windows server administrator | Monthly, and at each release |
| PostgreSQL | Vendor security announcements | Database administrator | Monthly |
| .NET and NuGet packages, from nuget.org and the offline feed | The package vulnerability report at each build, and Test-Vulnerability.ps1 at each release | Developers | Each build, and monthly |
| Browser libraries | Vendor security announcements | Developers | Monthly |
| Images, and their operating system packages | Test-Vulnerability.ps1, and an image scanner | Developers | Each release |
| \<System Name\>'s own applications: UI application, Admin application and API | A web application scan, reaching them as a user and as an outsider would; the static analysis in the build; and an independent penetration test before go-live | Developers | Each release |
| Server and database settings | The configuration scan against the baseline in \<Configuration Management\>, which finds the improper configurations RA-5 also asks about | Windows server administrator, database administrator | Monthly |
| All components, for exploited flaws | CISA's Known Exploited Vulnerabilities catalogue and \<Organisation\>'s alerts (PRO-RA-4) | Security officer | Weekly (\<Security Operating Procedures\>, C50) |

Monitoring also starts whenever a new vulnerability that may affect \<System Name\> is reported, through these sources or the reporting route in section 3.7.

The scanner must:

1. scan both VMs with an account approved for scanning, so that the scan sees what an administrator sees (RA-5(5));
2. update its definitions before each scan (RA-5(2));
3. name each flaw by its CVE identifier and rate it by CVSS, so that its results and the package check's can be compared and measured the same way (RA-5b);
4. cover the images and their operating system packages, if images are still used to build or run a release;
5. find ports, protocols and services that should not be reachable, against the allowed flows in \<Access Control Management\>, section 3.6;
6. scan \<System Name\>'s three applications at each release, as this section sets out.

Items 5 and 6 come from the CSS guidance on RA-5.

Improper configurations are found by the configuration scan against the baseline, which uses a standard checklist format (\<Configuration Management\>).

### 3.6 Vulnerability timetable

Controls met here: RA-5.

This is the one timetable for vulnerabilities in \<System Name\>, its packages, images and VMs. It replaces any other limit for vulnerabilities, including the general limits for POA&M items in \<Policy\> (CA). It meets the Cyber Essentials limit of 14 days for high and critical updates, which \<Organisation\> holds.

**Table 4: Vulnerability timetable**

| Severity | How it is set | Fix or mitigate within |
| --- | --- | --- |
| Exploited | In CISA's Known Exploited Vulnerabilities catalogue, or confirmed exploited by the vendor or \<Organisation\> | 3 days, as an emergency change (PRO-RA-4) |
| Critical | Vendor rating Critical, or CVSS base 9.0 or more | 14 days |
| High | Vendor rating High, or CVSS base 7.0 to 8.9, or no rating given | 14 days |
| Medium | Vendor rating Medium or Moderate, or CVSS base 4.0 to 6.9 | 30 days |
| Low | Vendor rating Low, or CVSS base below 4.0 | 90 days, or 30 days once a vendor update exists |

The clock starts when the fix is released, or when \<System Name\>'s use of the flaw is detected if that is later. The vendor's rating comes first; the CVSS version is recorded on TPL-7. Mitigating means reducing the risk without the fix, for example by turning off the affected feature or blocking its route. A fix that cannot meet its time goes to a risk decision under \<Policy\>, section RA.7, with its compensating measure.

### 3.7 Analysing, sharing and reporting

Controls met here: RA-5, RA-5(11).

1. **Analysis.** Within 5 working days of each scan or check, the security officer records each finding on TPL-7: its severity under section 3.6, whether \<System Name\> uses the affected part, and its due date (PRO-RA-3).
2. **False positives.** A finding that does not apply, such as a flaw in a feature \<System Name\> does not call, is marked as a false positive on TPL-7 with the reason, and checked again at the next scan.
3. **Fixing.** The people responsible fix or mitigate each finding within its time, as a change (\<Configuration Management\>). An exploited flaw is fixed or mitigated as an emergency change, and the security officer confirms it and tells the system owner (PRO-RA-4).
4. **Sharing.** After each scan the security officer shares each finding that applies with the developers and the Windows server administrator, so that the same flaw is fixed wherever it occurs. A finding that may affect \<Organisation\>'s other systems also goes to its security contact, so that it can be removed there too (PRO-RA-5).
5. **Reports from anyone.** Anyone may report a vulnerability in \<System Name\> to \<Organisation\>'s security contact, which passes the report to the security officer, who records it on TPL-7 and handles it as a scan finding. CSS asks for a public channel, so the contact must be published where people outside \<Organisation\> can find it, for example in a security.txt file on its website (RFC 9116): \[Where the contact is published\] (EV-RA-01). Its published terms must authorise research in good faith, and may ask the reporter to allow a set time for a fix before disclosing the flaw, but must not require it to be kept secret for ever. The time asked for is 90 days (EV-RA-01).
6. **Flaws in other parties' components.** A flaw found in another party's package or image is reported to its maintainer through their published route, and noted on TPL-7.

### 3.8 Risk response

Controls met here: RA-7.

Findings come from four sources: security assessments, privacy assessments, monitoring and audits. Each is answered the same way, within the risk tolerance in section 3.3.

**Table 5: How a finding is answered**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 Record | Each finding that is not satisfied becomes an entry in the Risk List's non-compliance register, linked to the risk it adds to | System owner | \<Risk List\>, section 5 |
| 2 Rate | The entry is rated by the method in section 3.3 | System owner | \<Risk List\> |
| 3 Decide | The person the rating calls for decides: accept, remediate, approve, obtain evidence from \<Organisation\>, or tailor | System owner for Low; authorising official for Medium and High | \<Decision Register\>; acceptances in \<Risk List\>, section 3 |
| 4 Plan | A remediation goes into the Plan of Action and Milestones, with milestones and a due date. A vulnerability follows the timetable in section 3.6 | System owner | \<Plan of Action and Milestones\> |
| 5 Review | Each acceptance is reviewed by its review date: Medium every 6 months and Low every 12 | System owner; authorising official | \<Risk List\>, section 3 |

A monitoring finding, such as a scan result, is first recorded on TPL-7 (section 3.7). It enters the Risk List only if it cannot be fixed in time.

### 3.9 Critical components

Controls met here: RA-9.

**Method.** A component is critical if its failure or compromise would expose or lose the documents, or defeat a security control. Each component in the authorisation boundary, and each outside service it relies on, is judged by the impact levels in \<System Security Plan\>, section 3.3, the recovery priorities in \<Contingency Planning Management\>, section 3.3, and whether it lies on the path to the documents. A component that gives unmediated access to a critical component is critical too. The developers' criticality analysis (SA-15(3)) uses this list.

**Table 6: Critical components**

| Component | Why it is critical | If it fails or is compromised |
| --- | --- | --- |
| Database server VM | Holds every document, document record and audit record | All documents are exposed or lost |
| Application server VM | Runs all three applications, and holds their data protection key rings and the bulk export working folder. Whoever controls it reaches the database through the API | Every document reachable, and the applications' controls bypassed |
| API | The only route to the database. Checks each request's sign-in, role and project access for the other two applications | Access controls can be bypassed, and every document read |
| UI application | Users' document pages, reached after sign-in through PingFederate | Documents shown to the wrong person, or a user's sign-in taken over |
| Admin application | Sets which AD groups open each project, and administers projects, documents and audit records, including raw deletes and maintenance pages | Project access granted, or documents deleted, without trace |
| Audit records | Show who did what | Misuse cannot be traced or proved |
| Backup store | Holds a full copy of every document | Every document exposed from a stolen or unencrypted backup, or lost |
| Bulk export working folder | Holds full, unencrypted copies of documents for each export job | Documents disclosed outside their project's permissions |
| Key store | Holds the signing key and service secrets | Calls between the applications, and database access, can be forged |
| Data protection key rings | Protect each app's cookies and tokens | Sign-in cookies can be forged or read |
| PingFederate, with Active Directory (\<Organisation\>) | PingFederate authenticates every user with multi-factor authentication; Active Directory holds the groups, read by the API over LDAPS, that decide each role and each project's access | Anyone could sign in as another user, or be given any role or project |

PingFederate with Active Directory is critical because \<System Name\> holds no accounts and relies on \<Organisation\> to authenticate every user. The application server VM and the bulk export working folder are critical because each gives a path to the documents that goes round the other controls.

**Critical functions.** CSS asks for critical functions as well as components. Five functions would expose or lose the documents if they failed: signing in and deciding access (PingFederate with Active Directory, API, the key store and the data protection key rings); storing and showing documents (the database server, the application server, API and UI application); administering projects and access (Admin application); recording who did what (the audit records); and recovering documents (the backup store).

The list is reviewed at each major release and after a significant change (PRO-RA-6).

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

1. **Policy.** \<Policy\> (RA) is a system-level policy, shared with everyone who administers \<System Name\>. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (RA) holds six procedures, PRO-RA-1 to PRO-RA-6. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control.

## Appendix A Risk assessment controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes some way towards them, and Table 8 says where. RA-4, RA-5(1), RA-5(7) and RA-5(9) are withdrawn: RA-5(1) is now part of RA-5f, and the others were moved into other controls.

**Table 8: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| RA-2(1) Impact-level Prioritization | Ranks systems within one impact level | Not required. \<System Name\> is one system |
| RA-3(2) Use of All-source Intelligence | Draws on all sources of threat intelligence | Not required. \<Organisation\>'s threat awareness programme (PM-16) and the advisory sources in \<System and Information Integrity Management\>, section 3.3, feed the risk assessment |
| RA-3(3) Dynamic Threat Awareness | Assesses the current threat continuously | Not required. Done in part: CISA's exploited list and \<Organisation\>'s alerts are checked weekly (PRO-RA-4) |
| RA-3(4) Predictive Cyber Analytics | Uses advanced analytics to predict threats | Not required |
| RA-5(3) Breadth and Depth of Coverage | Defines how widely and deeply scans look | Not required. Done in part in design: section 3.5 says which components are checked, how and how often |
| RA-5(4) Discoverable Information | Finds what an adversary could learn about the system, and acts on it | Not required: selected at High only. The penetration test before go-live looks for it |
| RA-5(6) Automated Trend Analyses | Compares scan results over time automatically | Not required. Done in part by hand: the monthly monitoring analysis looks for a trend over three months (\<Assessment, Authorization, and Monitoring Management\>, section 3.8) |
| RA-5(8) Review Historic Audit Logs | Checks the audit records for signs a newly found flaw was exploited before | Not required |
| RA-5(10) Correlate Scanning Information | Combines scan results to find attacks that use several flaws | Not required |
| RA-6 Technical Surveillance Countermeasures Survey | Surveys premises for eavesdropping devices | Not required. \<System Name\> has no premises of its own |
| RA-8 Privacy Impact Assessments | Assesses the effect on people's privacy | In the CSS privacy baseline. Designed and assessed with the personal data controls in \<PII Processing Management\> |
| RA-10 Threat Hunting | Searches actively for threats that have evaded other controls | Not required. Any threat hunting is \<Organisation\>'s security operations |
