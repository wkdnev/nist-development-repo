# \<System Name\> Assessment, Authorization, and Monitoring Management

## 1 Purpose

This document sets out how \<System Name\> is assessed, authorised to operate and monitored afterwards, and how its connections to other systems are approved, to meet the 10 Assessment, Authorization, and Monitoring (CA) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the cycle, assessment, the plan of action, authorisation, inherited controls, information exchanges and internal connections, continuous monitoring, significant change, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.



## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.4 (Table 13). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (CA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (CA), and the steps people follow are in \<Procedures\> (CA).

## 3 The design

### 3.1 Principles

Controls met here: CA-2, CA-2(1), CA-3, CA-5, CA-6, CA-7, CA-9.

1. **Two levels of assessment.** The system owner self-assesses at Level 1. An independent team assesses at Level 2, and every authorisation rests on a Level 2 assessment.
2. **Authorise knowingly.** The authorising official accepts the remaining risk by name, in writing, for no more than 12 months at a time.
3. **Nothing in production before authorisation.** \<System Name\> holds no real data until it is authorised (P-25).
4. **Track what is open.** Every weakness stays on the plan of action until its fix is tested.
5. **Know the connections.** Each connection to another system is recorded and approved before it is used.
6. **Keep watching.** After authorisation, measures are collected and reported, and a significant change sends \<System Name\> back to the authorising official.

These carry out the principles and rules of \<Policy\>, sections CA.3 and CA.4.

### 3.2 The cycle

Controls met here: CA-2, CA-5, CA-6, CA-7, CA-7(1).

![Figure 1: From assessment to authorisation to monitoring](figures/cam-figure-1.png)

**Figure 1: From assessment to authorisation to monitoring**

**Table 1: Who does what in the cycle**

| Step | Who | Record | How often |
| --- | --- | --- | --- |
| Plan the assessment, and approve the plan | System owner and assessor; the authorising official approves | The plan in each chapter of \<Control Assessment Record\> | Every 12 months, and after a significant change |
| Assess the controls | Level 1: the system owner. Level 2: the independent team, after Level 1 and before the authorisation it supports | \<Control Assessment Record\> | The same: both levels every 12 months |
| Report | The assessor | \<Security Assessment Report\> | After each assessment |
| Record and track each weakness | System owner | \<Risk List\> and \<Plan of Action and Milestones\> | Monthly |
| Authorise | Authorising official | TPL-18 | Before operation; every 12 months; after a significant change |
| Monitor and report | Security officer; system owner | TPL-8 | Monthly to the system owner; quarterly to the authorising official |
| Check the monitoring independently | Independent assessor | The assessor's report; TPL-19 | Every 12 months |

### 3.3 Assessment

Controls met here: CA-2, CA-2(1), CA-7(1).

**Levels.** Level 1 is the system owner's self-assessment. It is not independent. It shows the system owner where \<System Name\> stands, and prepares the ground for Level 2. Level 2 is the independent assessment by \[Name\]'s team, which also makes the yearly independent check of monitoring. Level 2 is carried out before the first authorisation and before each yearly re-authorisation, and the authorising official decides only on a Level 2 report. A Level 1 report alone never supports an authorisation (decision D-CA-01).

**Independence.** A member of the team counts as independent once they have completed TPL-19, confirming that they have had no part in designing, building, running or administering \<System Name\>, that they report to no one responsible for it, and declaring any other interest. The authorising official accepts each statement before the assessment starts.

**Method.** Each control is assessed with the procedures of CSS: every determination statement is given a finding of satisfied or other than satisfied, with the basis for it. The methods are examine, interview and test.

**Plan.** Each family's chapter of \<Control Assessment Record\> has a plan: scope, procedures, assessor, dates, site, what is examined, tested and whom is interviewed, with depth and coverage, the boundary, and what is needed from \<Organisation\>. The authorising official approves it before the assessment (PRO-CA-1, step 1).

**Report and results.** The findings are brought together in \<Security Assessment Report\>, which goes to the system owner, the authorising official and the Head of Cyber, and, for the privacy controls, to the legal adviser. No authorisation is given without an approved plan and a report (PRO-CA-4).

**Frequency.** Every 12 months, and after a significant change (section 3.9).

**Between assessments.** The developers repeat the security tests at each release and after a significant change, on a separate test environment (\<Security Operating Procedures\>, duty C40). The results feed the next assessment and the plan of action.

**Penetration test.** CA-8 is outside the Moderate baseline, but one is commissioned before go-live, by a tester independent of the build (\<Tailoring Register\>, CA-8). Its report goes into the first assessment and the authorisation package, and each finding is rated in \<Risk List\>.

### 3.4 Plan of action and milestones

Controls met here: CA-5.

Every weakness that needs a fix has one item in \<Plan of Action and Milestones\>, with its control, source, fix, owner, resources, milestone, due time and state. The Risk List rates the weakness and records the decision; only those to be fixed go to the plan. Evidence still to come from \<Organisation\> is tracked in \<Evidence Requests\>, an approval still to be given in \<Decision Register\>, and an accepted risk in \<Risk List\>, section 3 (\<Risk List\>, Table 5).

**Table 2: Time allowed to fix an item**

| Rating | Fixed within | Decided by |
| --- | --- | --- |
| High | The time the authorising official has set for the item | Authorising official |
| Medium | 180 days | \<Policy\>, section CA.4 |
| Low | 365 days | \<Policy\>, section CA.4 |

Each time is counted from go-live, or from the date the item is raised if that is later, so an item found after go-live has its full time. A known vulnerability keeps the shorter limit in \<System Description\>, P-11.

1. The system owner updates the plan each month, from assessments, monitoring and audits.
2. Once the development phase is scheduled, each open item is given a calendar date within its time limit.
3. An item is closed only when the fix has been tested, the evidence is recorded against the item, and the system owner agrees. An item fixed in the test environment is tested again on the servers before it closes.
4. Each quarter the system owner reports overdue items, with the reason for each, to the authorising official.

A consistency test checks that every item named in the Risk List exists in the plan, and that \<Security Assessment Report\> gives the plan's counts.

The steps are in \<Procedures\>, PRO-CA-3.

### 3.5 Authorisation

Controls met here: CA-6.

**Table 3: Who authorises**

| Role | Who | Decides |
| --- | --- | --- |
| Authorising official for \<System Name\> | \[Name\] | Whether \<System Name\> may operate; which remaining risks are accepted; whether a significant change needs a new assessment or authorisation |
| Authorising official for \<Organisation\>'s common controls | \[Organisation common control official\] | That the controls \<System Name\> inherits are authorised for use |
| System owner | \[Name\] | Puts the package to the authorising official, and keeps it current |

**Table 4: Authorisation package**

| Item | Document |
| --- | --- |
| System security plan | \<System Security Plan\> |
| Privacy plan and impact assessment | \<Privacy Plan\> and \<Data Protection Impact Assessment\> |
| Security assessment report | \<Security Assessment Report\> for the Level 2 assessment. Its section 2 is the executive summary. A Level 1 report is not enough |
| Plan of action and milestones | \<Plan of Action and Milestones\> |
| Risks and decisions | \<Risk List\> and \<Decision Register\> |
| Family assessments | \<Control Assessment Record\> (AC) to \<Control Assessment Record\> (SR) |
| Evidence | The test results and records in the evidence store, each with a hash manifest |
| Assessor independence | TPL-19, accepted by the authorising official |
| Penetration test | The tester's report, before the first authorisation (section 3.3) |
| Common controls | The record that \<Organisation\>'s authorising official has authorised the inherited controls (EV-CA-01), and \<Organisation\>'s evidence for them (\<Evidence Requests\>) |
| Decision | TPL-18, with terms, conditions, accepted risks, inherited controls accepted and an end date no more than 12 months away |

**Privacy review.** \<System Name\> holds personal data, so before the decision the legal adviser reviews the privacy plan and the impact assessment, and their view goes to the authorising official with the package.

**The decision.** The authorising official records the decision on TPL-18. It is one of three types: a first authorisation, a re-authorisation, or the withdrawal of an authorisation. The record gives the package received, with versions; the decision, to authorise or not; the terms and conditions, such as items to fix by a date or limits on use; each remaining risk accepted, by its Risk List entry; the inherited controls accepted; and an end date no more than 12 months away (PRO-CA-4). It is copied to the system owner and the Head of Cyber. \<System Name\> holds no real data until the authorising official has authorised it. The authorisation is reviewed every 12 months and after a significant change.

### 3.6 Inherited controls

Controls met here: CA-6.

These 66 entries are provided wholly by \<Organisation\>, and the system owner relies on them (\<System Security Plan\>, section 7). The authorising official accepts them on TPL-18 before \<System Name\> operates, once \<Organisation\>'s evidence has been received (\<Evidence Requests\>). The system owner reviews the list every 12 months with \<Organisation\>'s security contact (PRO-CA-7). \<Organisation\>'s authorising official for its common controls authorises them for use, and \<System Name\> holds the record of that authorisation.

**Table 5: Inherited controls**

| Family | Entries | Controls |
| --- | --- | --- |
| AC | 9 | AC-7, AC-11, AC-11(1), AC-17(3), AC-18, AC-18(1), AC-18(3), AC-19, AC-19(5) |
| IA | 8 | IA-3, IA-5(1), IA-6, IA-7, IA-12, IA-12(2), IA-12(3), IA-12(5) |
| SC | 10 | SC-4, SC-7(3), SC-7(4), SC-7(7), SC-7(8), SC-17, SC-20, SC-21, SC-22, SC-39 |
| CM | 1 | CM-2(7) |
| SI | 1 | SI-4(4) |
| CP | 9 | CP-6, CP-6(1), CP-6(3), CP-7(1), CP-7(2), CP-7(3), CP-8, CP-8(1), CP-8(2) |
| MA | 1 | MA-6 |
| MP | 2 | MP-5, MP-7 |
| PE | 16 | PE-2, PE-3, PE-4, PE-6, PE-6(1), PE-8, PE-8(3), PE-9, PE-10, PE-11, PE-12, PE-13, PE-13(1), PE-14, PE-15, PE-16 |
| PS | 2 | PS-3, PS-8 |
| PT | 1 | PT-5 |
| SA | 2 | SA-4, SA-9(2) |
| SR | 4 | SR-8, SR-11(1), SR-11(2), SR-12 |
| **Total** | **66** |  |

The list matches the Inherited entries in \<System Security Plan\>, section 7. CP-7 is not on it: \<Organisation\> provides the second site, but \<System Name\>'s administrators rebuild the servers there, so it is shared (\<Contingency Planning Management\>, section 3.9). PE-8(3) is listed under PE here; \<System Security Plan\>, Table 8, counts it with PT, because it is in the privacy baseline.

The system owner puts the list of 66 to the authorising official for acceptance as a list, with the other proposed ratings, and for acceptance for operation with the authorisation package, once \<Organisation\>'s evidence is in.

### 3.7 Information exchanges and internal connections

Controls met here: CA-3, CA-9.

This is the single record of \<System Name\>'s connections. Every external exchange is with a service of \<Organisation\> itself, so, as CSS allows within one organisation, this record is the agreement: its row states the interface, the security and privacy needs, the controls, the responsibilities and the impact level, and the system owner and the owner of that service sign it (decision D-CA-04). That is the agreement type chosen under CA-3. Any hosting and services agreement \<Organisation\> holds supports it but is not relied on. An exchange with a system outside \<Organisation\> would need its own interconnection or information exchange agreement, and is a significant change (section 3.9). The system owner approves each connection before it is built, reviews each every 12 months with the owner of the other system, both signing again, and records the date a connection ends (PRO-CA-2).

**Table 6: Interface record**

| Connection | Type | Information | Security needs | Privacy needs | Responsibilities | Impact | Agreement | Review and end |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F3, F4: UI application and Admin application to API | Internal (CA-9) | Every request the two user-facing applications make, including item content and audit events | HTTPS on the application server's own loopback address; the API accepts requests only from the two applications, each with a signed, short-lived token that names the signed-in person | Personal data in items and audit events never leaves the application server on this link; the API applies every access check before it returns an item | Developers; Windows server administrator | Moderate | None needed: inside the boundary | Reviewed every 12 months; ends when a component is retired, and is approved again before it is rebuilt in another form |
| F5: API on the application VM to SQL Server on the database VM | Internal (CA-9) | Items, their files, schema definitions and audit records, including personal data. No user accounts are held | SQL Server over TLS with strict encryption, TCP 1433, with Windows authentication under the API's managed service account and no database password; allowed only from the application server | Personal data, including any special category data in items, is held only in the database and reached only through the API; audit records name the fields changed, not their values | Windows server and database administrators | Moderate | None needed: inside the boundary | Reviewed every 12 months; ends when the application server or the database is retired. A rebuild of either VM re-creates the link to the same settings under an approved change, and is not a new connection |
| F6, F7, F10: \<Organisation\>'s PingFederate and Active Directory | External (CA-3) | PingFederate's signed OpenID Connect response, which names the person and carries no groups, and its OpenID Connect metadata and the signing certificate that checks the response, which the UI application and Admin application fetch, and with which they complete each sign-in (F10); each person's group membership, read by the API from Active Directory over LDAPS (F7) | The response is signed and sent over TLS, the applications reach PingFederate over HTTPS, TCP 443, from the application server only (F10), and the groups are read over LDAPS; \<System Name\> trusts only \<Organisation\>'s PingFederate | The response and the directory carry the person's name, username and group memberships: staff data that \<Organisation\> already holds. \<System Name\> keeps only the username in its audit records, and asks for no other attribute | \<Organisation\>, for authentication and the directory; system owner, for which groups \<System Name\> uses | Moderate | This record, signed by the system owner and the owner of PingFederate and Active Directory (EV-CA-02) | Reviewed every 12 months; ends if sign-in moves to another service |
| F9: ServiceNow | Not a system connection: people only (F9) | Access requests and the Data Owner's authorisation; change requests; names of requesters. None of it passes to \<System Name\> | ServiceNow has no connection to \<System Name\>. Group owners act on an authorised request by changing group membership in Active Directory | Requesters' names stay in ServiceNow, under \<Organisation\>'s retention | System owner; Data Owners; \<Organisation\>'s IT service desk | Moderate | None needed: no system connection; ServiceNow is \<Organisation\>'s service | Reviewed every 12 months; ends if the workflow moves |
| F9: Starters and leavers process | Not a system connection: people only (F9) | Leaver notices to group owners; staff names. None of it passes to \<System Name\> | No connection to \<System Name\>. A leaver's Active Directory account is disabled as P-06 sets, which ends their access | Staff names and leaving dates stay in \<Organisation\>'s process | System owner; \<Organisation\> | Moderate | None needed: no system connection; the process is \<Organisation\>'s service | Reviewed every 12 months; ends if the process changes |
| F8: \<Organisation\>'s central logging | External (CA-3) | From both VMs: the Windows security logs; the SQL Server Audit records and error log; the three applications' logs and security events, including each read or export of the audit log and the daily copy of the newest audit-chain hash (\<Audit and Accountability Management\>, section 3.5) | Encrypted in transit; forwarded as written; nobody in \<System Name\>'s team can change or delete the copies; read access only for the auditor, the security officer and \<Organisation\>'s security team (EV-AU-01) | The records hold usernames, IP addresses and item references, never item content or the values of item details; kept as P-07 sets, in the location in P-23 | \<Organisation\>; Windows server and database administrators | Moderate | This record, signed by the system owner and the service's owner (EV-CA-02) | Reviewed every 12 months; ends if logging moves to another service |
| F8: \<Organisation\>'s time service | External (CA-3) | Time, into both VMs | Authenticated NTP where available; within 1 second of UTC (P-09) | None: no personal data passes | \<Organisation\>; Windows server administrator | Moderate, as audit time stamps depend on it | This record, signed by the system owner and the service's owner (EV-CA-02) | As above |
| F8: \<Organisation\>'s backup site | External (CA-3) | Encrypted SQL Server backups, out from the database VM | Encrypted before leaving the database VM; one copy offline or immutable (P-15) | Backups hold every item, including personal data, and items since deleted: kept only as P-15 sets, in the location in P-23, and restored only under the contingency plan or for a restore test on the restore test server at the second site (D-CP-01) | Database administrator; \<Organisation\> | Moderate | This record, signed by the system owner and the service's owner (EV-CA-02) | As above |
| F8: \<Organisation\>'s authenticated proxy | External (CA-3) | Updates for Windows Server, SQL Server and Defender, out from both VMs through the proxy; nothing else outbound | Outbound only, through the authenticated proxy, or blocked (SC-7(8)); updates are signed by the supplier | None: no \<System Name\> data passes | \<Organisation\>; Windows server administrator | Moderate | This record, signed by the system owner and the service's owner (EV-CA-02) | As above |

Every system connection is encrypted. A connection ends when it is no longer needed, or when a component at either end is retired: the Windows server administrator removes it, and the system owner records the end date (PRO-CA-2, step 3). Rebuilding a VM re-creates its connections to the same settings under an approved change; anything different is a new connection. \<Organisation\>'s name resolution and certificate authority are infrastructure services that carry no \<System Name\> data; they are covered by \<System and Communications Protection Management\> and are not exchanges here. The API listens only on the loopback address and accepts only the two applications, and the database accepts only the application server (\<Access Control Management\>, section 3.6). A new or changed external exchange is a significant change (section 3.9), so the authorising official weighs its risk before it is built.

Users' and administrators' devices are outside the boundary. They connect by browser, as a class and not one by one: \<Organisation\>'s managed devices, over HTTPS, in the office or on the VPN (\<Access Control Management\>, section 3.6). Server and database administrators' managed devices reach both servers only over \<Organisation\>'s managed administration route, with multi-factor authentication, using named accounts (F11). \<Organisation\>'s firewall allows only the flows \<System Name\> has asked for (\<Access Control Management\>, section 3.6.4).

### 3.8 Continuous monitoring

Controls met here: CA-7, CA-7(1), CA-7(4).

This is \<System Name\>'s system-level strategy. It carries out \<Organisation\>'s organisation-level continuous monitoring strategy (PM-31, inherited: \<Program Management\>; EV-PM-03), and follows CSS. Where the two differ, \<Organisation\>'s strategy wins and this section is changed to match. Monitoring starts at go-live.

**How often controls are checked.** Each control is checked at the frequency of its duty in the \<Security Operating Procedures\> operating calendar: daily, weekly, monthly, quarterly or yearly. Controls with no duty there are checked at the yearly assessment.

**What is measured.** The measures cover effectiveness (do the controls work), compliance (are the procedures followed) and change (has the system changed), with two for privacy.

**Table 7: Monitoring measures**

| Measure | Kind | Target | Threshold for action | Source | Frequency | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| POA&M items past their date | Compliance | None | Any | \<Plan of Action and Milestones\> | Monthly | System owner |
| Security updates applied within the limits in \<System Description\>, P-11 | Effectiveness | All | Any late critical or high update | TPL-7 | Monthly | Windows server administrator |
| Failed sign-ins and lockouts | Effectiveness | Reviewed every week | More than 10 failures for one account in a day, or any for a disabled account | \<Organisation\>'s PingFederate record, and \<System Name\>'s audit log for refused sign-in responses; TPL-8 | Weekly | Auditor |
| Weekly audit reviews completed | Compliance | All | Any missed week | TPL-8 | Monthly | Security officer |
| Audit logging failures | Effectiveness | None | Any | PRO-AU-3; TPL-8 | Monthly | Windows server administrator |
| Backup jobs succeeded, and restore tested in the last 6 months | Effectiveness | All | Any failed job, or a restore test overdue | Backup logs; TPL-11 | Weekly | Database administrator |
| Access and privileged access reviews on time | Compliance | All | Any overdue | TPL-3 | Quarterly | System owner |
| Members of \<System Name\>'s AD groups who have not signed in for 90 days | Compliance | None | Any | C9; TPL-3 | Monthly | System owner |
| Significant changes made since the last report | Change | Each assessed before it was made | Any not assessed | TPL-6 | Monthly | System owner |
| Requests from individuals about their data answered within one month | Privacy | All | Any late | TPL-15 | Monthly | Legal adviser |
| Personal data incidents | Privacy | None | Any | TPL-10 | Monthly | Security officer |
| Configuration drift from the baseline | Change | None unapproved | Any | PRO-CM-7; TPL-8 | Monthly | Windows server administrator |
| Security incidents open past their time limit | Effectiveness | None | Any | TPL-10 | Monthly | Security officer |
| Vulnerabilities past their fix time | Effectiveness | None | Any Critical or High past its time | TPL-7; the timetable in \<Risk Assessment Management\>, section 3.6 | Monthly | Windows server administrator, developers |
| Changes to the inherited controls: a change to a service \<Organisation\> provides, or its evidence past its review date | Change | None unassessed | Any | \<Organisation\>'s notices; \<Evidence Requests\>; TPL-8 | Quarterly | System owner |

**Table 8: The strategy against CSS**

| Step in CSS | Where it is met |
| --- | --- |
| Define the strategy | This section |
| Establish the programme: measures and frequencies | The measures above, and the \<Security Operating Procedures\> operating calendar |
| Implement: collect the data | The duties in the operating calendar, each with its record |
| Analyse and report | Analysis and Reporting, below |
| Respond | Response, below; \<Plan of Action and Milestones\> |
| Review and update | Review of this strategy, below |

**Analysis.** The analysis and response steps are in PRO-CA-5. Each month the security officer reads the measures together with the audit review findings, the vulnerability results and the incident records, and looks for a trend across three months. The system owner also reviews the Risk List each month for new or changed risks.

**Response.** A measure past its threshold is acted on in the month, and the action is recorded on TPL-8. One not put right in the month becomes an item in \<Plan of Action and Milestones\>.

**Reporting.** The security officer reports the measures monthly to the system owner on TPL-8, and sends the privacy measures and any personal data incident to the legal adviser in the same month: that is the privacy status. Each quarter the system owner reports them to the authorising official, with overdue POA&M items, changes in risk, significant changes and incidents.

**Independent check.** Each year, alongside the Level 2 assessment, an independent assessor whose TPL-19 the authorising official has accepted checks a sample of the monitoring: that the measures were collected, are accurate, and were acted on (PRO-CA-5, step 3). Together with the yearly Level 2 assessment of every control, this yearly check is the ongoing basis on which independent assessors monitor the controls (CA-7(1); decision D-CA-03).

**What forces a re-assessment.** A significant change (section 3.9), a measure past its threshold for three months running, a serious incident, or a new High risk. The authorising official then decides whether \<System Name\> must be re-authorised.

**Review of this strategy.** Every 12 months with the policy, and after a re-authorisation.

### 3.9 Significant change

Controls met here: CA-2, CA-3, CA-6, CA-7.

A significant change is one likely to alter \<System Name\>'s security or privacy risk. It must be assessed before it is made (PRO-CA-6), and the authorising official decides whether \<System Name\> must be re-assessed or re-authorised. These always count as significant:

1. A new or changed external connection, or a change to an agreement in section 3.7.
2. A new hosting site, or a new major version of Windows Server, SQL Server or .NET.
3. A change to how people sign in, or to the access control model in \<Access Control Management\>.
4. A new type of information, or a higher impact level for any information type.
5. A change to the boundary in \<System Security Plan\>.
6. A new High risk in \<Risk List\>.
7. A serious security incident or personal data breach.
8. A new class of users, such as people outside \<Organisation\>, or a new role.
9. A new application function (\<System Description\>, section 3.5) or a new departure from the reference design (section 3.6 of the same).
10. A change to cryptography: the protocols or ciphers in P-26, the token or chain algorithms, or the key store.
11. A new port, protocol or service on either server, or a new flow in \<System Description\>, section 6.5.

Routine patches within the time limits of \<Security Operating Procedures\>, and changes to content or users, are not significant.

### 3.10 What \<Organisation\> provides

Controls met here: CA-3, CA-6.

**Table 9: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| An authorising official for its common controls, and their authorisation | CA-6 | The 66 inherited controls are authorised and working | EV-CA-01 |
| The agreements for the exchanges | CA-3 | The owner of each service signs its row in Table 6: PingFederate and Active Directory, central logging, the time service, the backup site and the authenticated proxy, with the hosting and services agreement, if any, as support. ServiceNow and the starters and leavers process are \<Organisation\>'s services used by people, with no connection to \<System Name\> | EV-CA-02 |
| Evidence for each inherited control | CA-6, and each control's own family | Each control's evidence request in \<Evidence Requests\> | By family |

### 3.11 Policy and procedures

Controls met here: CA-1.

\<Policy\> (CA) and \<Procedures\> (CA) meet CA-1. Who they are shared with is in \<Policy\>, section CA.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
