# \<DocuView\> Assessment, Authorization, and Monitoring Management

**\<ref\> | Version \<ver\> | Draft for the system owner's approval**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Summary](#3-summary)

[4 The design](#4-the-design)

[5 Each control and enhancement](#5-each-control-and-enhancement)

[Appendix A Parameter register](#appendix-a-parameter-register)

[Appendix B CA controls outside the Moderate baseline](#appendix-b-ca-controls-outside-the-moderate-baseline)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Assessment, Authorization, and Monitoring Management |
| Version | \<ver\> |
| Status | Draft for the system owner's approval |
| Date | 13 November 2026 |
| Owner | System owner |
| Applies to | Assessment, Authorization, and Monitoring family |
| Classification | Restricted |
| Next review | Every 12 months, and after a significant change or a re-authorisation |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | Neil Ramsbottom | Pending | Pending |

### 1.3 Change history

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 13 November 2026 | Finalised with the system owner's decisions (D-CA-13): two monitoring measures added, on open incidents and on vulnerabilities past their fix time; and the legal adviser's privacy review before authorisation adopted |
| \<ver\> | 13 November 2026 | Cross-check against NIST's guidance for the family: Level 1 is stated as not independent; the authorising official accepts each independence statement; the package includes the privacy plan and impact assessment, with the legal adviser's review; the decision record is set out field by field; a new exchange is a significant change; and the strategy is mapped to NIST SP 800-137. Two measures are proposed |
| \<ver\> | 12 November 2026 | Completed with the system owner's decisions (D-CA-12): the list of 65 inherited controls goes to the authorising official; the AD FS agreement is asked for with EV-CA-02; the analysis and response steps of monitoring are confirmed; and a penetration test is to be commissioned before go-live, beyond the baseline |
| \<ver\> | 12 November 2026 | CA-3 counts the six external exchanges; the two internal connections are under CA-9 |
| \<ver\> | 12 November 2026 | Issued with the set: no change to the content |
| \<ver\> | 12 November 2026 | First draft, at the system owner's request (D-CA-11). The assessment, authorisation and monitoring chapter of \<Control Implementation Register\> moved here in full, so that this design is held only in this document, and each control is set out part by part. The interface record and the monitoring measures follow sign-in through AD FS (D-AC-23). No agreed value is changed |

| **SECTION 2** |
| --- |

## 2 Purpose

This document shows how \<DocuView\> is assessed, authorised to operate and monitored afterwards, and how its connections to other systems are approved, for each of the 10 Assessment, Authorization, and Monitoring (CA) controls and enhancements in the NIST SP 800-53 Rev 5 Moderate baseline. Section 4 sets out the design: the cycle, assessment, the plan of action, authorisation, inherited controls, information exchanges, continuous monitoring and significant change. Section 5 takes each control in turn. Appendix A lists every value NIST asks the organisation to define. Appendix B lists the CA controls NIST does not select at Moderate.

This is the only place this design is held. Other documents point here. The policy is in \<Policy\> (CA), and the steps people follow are in \<Procedures\> (CA). The design follows NIST SP 800-37 Rev 2 for assessment and authorisation, SP 800-137 for monitoring, and SP 800-47 Rev 1 for information exchanges.

This family is about processes that people carry out, so an assessor examines documents and records and interviews the people named: the system owner, the authorising official, the security officer and the assessor (NIST SP 800-53A). There is nothing in the system to test. So for each control section 5 gives:

- **each part of the control**, as NIST letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, and the rules and procedures that apply;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

\<DocuView\> is not authorised and is not in use. The Level 1 self-assessment is complete. The independent assessment, the authorisation decision and monitoring have not started.

**Table 4: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

| **SECTION 3** |
| --- |

## 3 Summary

Of the 10 controls, none is fully implemented, 4 are partially implemented and 6 are not implemented. No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 5: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| CA-1 | Policy and Procedures | Partially implemented | The policy and procedures are not yet shared or walked through | NC-CA-01; PA-20 |
| CA-2 | Control Assessments | Partially implemented | The independent Level 2 assessment has not been held | NC-CA-02; PA-106 |
| CA-2(1) | Independent Assessors | Not implemented | No assessor has confirmed their independence on TPL-19 | NC-CA-03; PA-106 |
| CA-3 | Information Exchange | Not implemented | No exchange is approved, and no agreement is signed | NC-CA-04; PA-63 |
| CA-5 | Plan of Action and Milestones | Partially implemented | The monthly updates and quarterly reports have not started, and items have no calendar dates | NC-CA-05; PA-108 |
| CA-6 | Authorization | Partially implemented | \<DocuView\> is not authorised. ABC Technologies' official for common controls is not named, and the inherited controls are not accepted for operation | NC-CA-06; PA-107, EV-CA-01 |
| CA-7 | Continuous Monitoring | Not implemented | Monitoring and reporting have not started | NC-CA-07; PA-80, PA-108 |
| CA-7(1) | Independent Assessment | Not implemented | No independent check of monitoring has been held | NC-CA-08; PA-108 |
| CA-7(4) | Risk Monitoring | Not implemented | Risk monitoring has not started | NC-CA-09; PA-108 |
| CA-9 | Internal Connections | Not implemented | Neither internal connection is authorised, as the servers are not built | NC-CA-10; PA-63 |

None of the gaps is a fault in the system. Each is a step that has not yet been taken, because \<DocuView\> is not built on its servers and is not in use.

| **SECTION 4** |
| --- |

## 4 The design

### 4.1 Principles

1. **Two levels of assessment.** The system owner self-assesses at Level 1. An independent team assesses at Level 2.
2. **Authorise knowingly.** The authorising official accepts the remaining risk by name, in writing, for no more than 12 months at a time.
3. **Nothing in production before authorisation.** \<DocuView\> holds no production documents until it is authorised.
4. **Track what is open.** Every weakness stays on the plan of action until its fix is tested.
5. **Know the connections.** Each connection to another system is recorded and approved before it is used.
6. **Keep watching.** After authorisation, measures are collected and reported, and a significant change sends \<DocuView\> back to the authorising official.

These carry out the principles and rules of \<Policy\>, sections CA.3 and CA.4.

### 4.2 The cycle

![Figure 1: From assessment to authorisation to monitoring](figures/cam-figure-1.png)

**Figure 1: From assessment to authorisation to monitoring**

**Table 6: Who does what in the cycle**

| Step | Who | Record | How often |
| --- | --- | --- | --- |
| Plan the assessment, and approve the plan | System owner and assessor; the authorising official approves | The plan in each chapter of \<Control Assessment Record\> | Every 12 months, and after a significant change |
| Assess the controls | Level 1: the system owner. Level 2: the independent team | \<Control Assessment Record\> | The same |
| Report | The assessor | \<Security Assessment Report\> | After each assessment |
| Record and track each weakness | System owner | \<Risk List\> and \<Plan of Action and Milestones\> | Monthly |
| Authorise | Authorising official | TPL-18 | Before operation; every 12 months; after a significant change |
| Monitor and report | Security officer; system owner | TPL-8 | Monthly to the system owner; quarterly to the authorising official |
| Check the monitoring independently | Independent assessor | The assessor's report; TPL-19 | Every 12 months |

### 4.3 Assessment

**Levels.** Level 1 is the system owner's self-assessment, carried out by Claude, an AI assistant, for the system owner. It is not independent: the same assistant drafted the documents and assessed them. It shows the system owner where \<DocuView\> stands, and prepares the ground for Level 2. Level 2 is the independent assessment by Josh Leak's team, which also makes the yearly independent check of monitoring.

**Independence.** A member of the team counts as independent once they have completed TPL-19, confirming that they have had no part in designing, building, running or administering \<DocuView\>, that they report to no one responsible for it, and declaring any other interest. The authorising official accepts each statement before the assessment starts.

**Method.** Each control is assessed with the procedures of NIST SP 800-53A Rev 5: every determination statement is given a finding of satisfied or other than satisfied, with the basis for it. The methods are examine, interview and test.

**Plan.** Each family's chapter of \<Control Assessment Record\> has a plan: scope, procedures, assessor, dates, site, what is examined, tested and whom is interviewed, with depth and coverage, the boundary, and what is needed from ABC Technologies. The authorising official approves it before the assessment.

**Report and results.** The findings are brought together in \<Security Assessment Report\>, which goes to the system owner, the authorising official and the Head of Cyber.

**Frequency.** Every 12 months, and after a significant change (section 4.9).

**Between assessments.** The developers repeat the security tests at each release and after a significant change, on a separate test environment (\<Security Operating Procedures\>, duty C40). The results feed the next assessment and the plan of action.

### 4.4 Plan of action and milestones

Every weakness that needs a fix has one item in \<Plan of Action and Milestones\>. The Risk List rates the weakness and records the decision; only those to be fixed, or to be evidenced, go to the plan.

**Table 7: Time allowed to fix an item**

| Rating | Fixed within | Decided by |
| --- | --- | --- |
| High | The time the authorising official has set for the item | Authorising official |
| Medium | 180 days of go-live | Authorising official (D-CA-07) |
| Low | 365 days of go-live | Authorising official (D-CA-07) |

1. The system owner updates the plan each month, from assessments, monitoring and audits.
2. Once the development phase is scheduled, each open item is given a calendar date within its time limit.
3. An item is closed only when the fix has been tested, the evidence is recorded against the item, and the system owner agrees. An item fixed in the test environment is tested again on the servers before it closes.
4. Each quarter the system owner reports overdue items, with the reason for each, to the authorising official.

The steps are in \<Procedures\>, PRO-CA-3.

### 4.5 Authorisation

**Table 8: Who authorises**

| Role | Who | Decides |
| --- | --- | --- |
| Authorising official for \<DocuView\> | Bob Jones | Whether \<DocuView\> may operate; which remaining risks are accepted; whether a significant change needs a new assessment or authorisation |
| Authorising official for ABC Technologies' common controls | \[ABC common control official\] | That the controls \<DocuView\> inherits are authorised for use |
| System owner | Neil Ramsbottom | Puts the package to the authorising official, and keeps it current |

**Table 9: Authorisation package**

| Item | Document |
| --- | --- |
| System security plan | \<System Security Plan\> |
| Privacy plan and impact assessment | \<Privacy Plan\> and \<Data Protection Impact Assessment\> |
| Security assessment report | \<Security Assessment Report\> at Level 1, replaced by the Level 2 report. Its section 3 is the executive summary |
| Plan of action and milestones | \<Plan of Action and Milestones\> |
| Risks and decisions | \<Risk List\> and \<Decision Register\> |
| Family assessments | \<Control Assessment Record\> (AC) to \<Control Assessment Record\> (SR) |
| Evidence | The test results and records in the evidence store, each with a hash manifest |
| Assessor independence | TPL-19 |
| Decision | TPL-18, with terms, conditions, accepted risks, inherited controls accepted and an end date no more than 12 months away |

**Privacy review.** The system owner adopted this step on 13 November 2026 (D-CA-13); the legal adviser confirms its wording at the next review of the policy. \<DocuView\> holds HR records, so before the decision the legal adviser reviews the privacy plan and the impact assessment, and their view goes to the authorising official with the package.

**The decision.** The authorising official records the decision on TPL-18. It is one of three types: a first authorisation, a re-authorisation, or the withdrawal of an authorisation. The record gives the package received, with versions; the decision, to authorise or not; the terms and conditions, such as items to fix by a date or limits on use; each remaining risk accepted, by its Risk List entry; the inherited controls accepted; and an end date no more than 12 months away. It is copied to the system owner and the Head of Cyber. The authorisation is reviewed every 12 months and after a significant change.

**Current state.** \<DocuView\> is not authorised and holds no production documents. \<Security Assessment Report\>, section 7, lists the conditions to meet first.

### 4.6 Inherited controls

These 65 entries are provided wholly by ABC Technologies, and the system owner relies on them (\<System Security Plan\>, section 8). The authorising official accepts them on TPL-18 before \<DocuView\> operates, once ABC Technologies' evidence has been received (\<Evidence Requests\>). The system owner reviews the list every 12 months with ABC Technologies' security contact (PRO-CA-7).

**Table 10: Inherited controls**

| Family | Entries | Controls |
| --- | --- | --- |
| AC | 6 | AC-2(3), AC-7, AC-17(3), AC-18, AC-18(1), AC-18(3) |
| IA | 8 | IA-3, IA-5(1), IA-6, IA-7, IA-12, IA-12(2), IA-12(3), IA-12(5) |
| SC | 10 | SC-4, SC-7(3), SC-7(4), SC-7(7), SC-7(8), SC-17, SC-20, SC-21, SC-22, SC-39 |
| CM | 2 | CM-8(3), CM-12(1) |
| SI | 1 | SI-4(4) |
| CP | 10 | CP-6, CP-6(1), CP-6(3), CP-7, CP-7(1), CP-7(2), CP-7(3), CP-8, CP-8(1), CP-8(2) |
| MA | 1 | MA-6 |
| MP | 2 | MP-5, MP-7 |
| PE | 16 | PE-2, PE-3, PE-4, PE-6, PE-6(1), PE-8, PE-8(3), PE-9, PE-10, PE-11, PE-12, PE-13, PE-13(1), PE-14, PE-15, PE-16 |
| PS | 2 | PS-3, PS-8 |
| PT | 1 | PT-5 |
| SA | 2 | SA-4, SA-9(2) |
| SR | 4 | SR-8, SR-11(1), SR-11(2), SR-12 |
| **Total** | **65** |  |

The authorising official accepted an earlier list of 66 as a list (D-CA-08). Since then five entries became shared between \<DocuView\> and ABC Technologies, and four were added when sign-in moved to AD FS (D-AC-23). The system owner puts the list of 65 to the authorising official for acceptance as a list now, with the other proposed ratings, and for acceptance for operation with the authorisation package, once ABC Technologies' evidence is in (D-CA-12, PA-107).

### 4.7 Information exchanges and internal connections

This is the single record of \<DocuView\>'s connections. Each has an agreement type chosen under NIST SP 800-47 Rev 1. None is in use yet. The system owner approves each before it is built, reviews each every 12 months with the owner of the other system, and records the date a connection ends (PRO-CA-2).

**Table 11: Interface record**

| Connection | Type | Information | Security and privacy needs | Responsibilities | Impact | Agreement | Agreed, review and end | State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DV\_Web and DV\_Admin\_UI to DV\_API | Internal (CA-9) | Every request the two user-facing apps make, including document content and audit events | HTTPS on the application server's own loopback address; the API accepts requests only from the two apps | Developers; Windows server administrator | Moderate | None needed: inside the boundary | Reviewed every 12 months; ends when a component is retired | Planned (PA-18) |
| Application VM to database VM | Internal (CA-9) | Documents, accounts and audit records, including personal data in HR documents | TLS; allowed only between these VMs | Windows server and database administrators | Moderate | None needed: inside the boundary | Reviewed every 12 months; ends when a VM is rebuilt | Planned (PA-18) |
| ABC Technologies' AD FS and Active Directory | External (CA-3) | Sign-in tokens, carrying each user's identity and AD groups; the certificate that checks them | Tokens are signed and sent over TLS; \<DocuView\> trusts only ABC Technologies' AD FS | ABC Technologies, for authentication and the directory; system owner, for which groups \<DocuView\> uses | Moderate | ABC Technologies' hosting and services agreement | \[agreement name and date, asked for with EV-CA-02\]; reviewed every 12 months; ends if sign-in moves to another service | Stated by the system owner (D-AC-23); not evidenced (EV-IA-04, PA-95) |
| Jira Service Desk | External (CA-3) | Access and change requests and approvals; names of requesters | TLS; approved accounts only | System owner; ABC Technologies' IT service desk | Moderate | Information exchange agreement with ABC Technologies' IT service desk | \[date agreed\]; reviewed every 12 months; ends if the workflow moves | Planned (PA-63) |
| Starters/Leavers system | External (CA-3) | Prompts to add or remove access; staff names and leaving dates | TLS; approved accounts only | System owner; ABC Technologies | Moderate | Information exchange agreement with ABC Technologies | \[date agreed\]; reviewed every 12 months; ends if the process changes | Planned (PA-63) |
| ABC Technologies' central logging | External (CA-3) | Windows and application security logs | Protected in transit; access limited to ABC Technologies' security team | ABC Technologies; Windows server administrator | Moderate | ABC Technologies' hosting and services agreement | \[agreement name and date\]; reviewed every 12 months | Stated, not evidenced (EV-AU-01) |
| ABC Technologies' time service | External (CA-3) | Time | Authenticated NTP where available | ABC Technologies | Low | ABC Technologies' hosting and services agreement | As above | Stated, not evidenced (EV-AU-02) |
| ABC Technologies' backup site | External (CA-3) | Encrypted database backups | Encrypted before leaving the database VM | Database administrator; ABC Technologies | Moderate | ABC Technologies' hosting and services agreement | As above | Planned (PA-64, PA-66) |

Every connection uses TLS. A connection ends when it is no longer needed, or when a server is rebuilt. A new or changed external exchange is a significant change (section 4.9), so the authorising official weighs its risk before it is built.

Users' and administrators' devices are outside the boundary. They connect by browser, as a class and not one by one: ABC Technologies' managed devices, over HTTPS, in the office or on the VPN (\<Access Control Management\>, section 4.6). ABC Technologies' firewall allows only the flows \<DocuView\> has asked for (\<Access Control Management\>, section 4.6.4).

### 4.8 Continuous monitoring

This strategy follows NIST SP 800-137. Monitoring starts at go-live. Nothing below is running yet.

**How often controls are checked.** Each control is checked at the frequency of its duty in the \<Security Operating Procedures\> operating calendar: daily, weekly, monthly, quarterly or yearly. Controls with no duty there are checked at the yearly assessment.

**What is measured.** The measures cover effectiveness (do the controls work), compliance (are the procedures followed) and change (has the system changed), with two for privacy.

**Table 12: Monitoring measures**

| Measure | Kind | Target | Threshold for action | Source | Frequency | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| POA&M items past their date | Compliance | None | Any | \<Plan of Action and Milestones\> | Monthly | System owner |
| Security updates applied within the limits in \<Security Operating Procedures\>, Table 7 | Effectiveness | All | Any late critical or high update | TPL-7 | Monthly | Windows server administrator |
| Failed sign-ins and lockouts | Effectiveness | Reviewed every week | More than 10 failures for one account in a day, or any for a disabled account | ABC Technologies' AD FS record, and \<DocuView\>'s audit log for refused tokens; TPL-8 | Weekly | Auditor |
| Weekly audit reviews completed | Compliance | All | Any missed week | TPL-8 | Monthly | Security officer |
| Audit logging failures | Effectiveness | None | Any | PRO-AU-3; TPL-8 | Monthly | Windows server administrator |
| Backup jobs succeeded, and restore tested in the last 6 months | Effectiveness | All | Any failed job, or a restore test overdue | Backup logs; TPL-11 | Weekly | Database administrator |
| Access and privileged access reviews on time | Compliance | All | Any overdue | TPL-3 | Quarterly | System owner |
| Members of \<DocuView\>'s AD groups who have not signed in for 90 days | Compliance | None | Any | C9; TPL-3 | Monthly | System owner |
| Significant changes made since the last report | Change | Each assessed before it was made | Any not assessed | TPL-6 | Monthly | System owner |
| Requests from individuals about their data answered within one month | Privacy | All | Any late | TPL-15 | Monthly | Legal adviser |
| Personal data incidents | Privacy | None | Any | TPL-10 | Monthly | Security officer |
| Configuration drift from the baseline | Change | None unapproved | Any | PRO-CM-7; TPL-8 | Monthly | Windows server administrator |
| Security incidents open past their time limit | Effectiveness | None | Any | TPL-10 | Monthly | Security officer |
| Vulnerabilities past their fix time | Effectiveness | None | Any Critical or High past its time | TPL-7; the timetable in \<Control Implementation Register\>, section RA.3 | Monthly | Windows server administrator, developers |

The last two measures, on open incidents and on vulnerabilities past their fix time, were added by the system owner on 13 November 2026 (D-CA-13).

**Table 13: The strategy against NIST SP 800-137**

| Step in SP 800-137 | Where it is met |
| --- | --- |
| Define the strategy | This section, approved by the system owner (D-CA-03, D-CA-10) |
| Establish the programme: measures and frequencies | The measures above, and the \<Security Operating Procedures\> operating calendar |
| Implement: collect the data | The duties in the operating calendar, each with its record |
| Analyse and report | Analysis and Reporting, below |
| Respond | Response, below; \<Plan of Action and Milestones\> |
| Review and update | Review of this strategy, below |

**Analysis.** The system owner confirmed the analysis and response steps on 12 November 2026 (D-CA-12). Each month the security officer reads the measures together with the audit review findings, the vulnerability results and the incident records, and looks for a trend across three months.

**Response.** A measure past its threshold is acted on in the month, and the action is recorded on TPL-8. One not put right in the month becomes an item in \<Plan of Action and Milestones\>.

**Reporting.** The security officer reports the measures monthly to the system owner on TPL-8. Each quarter the system owner reports them to the authorising official, with overdue POA&M items, changes in risk, significant changes and incidents.

**Independent check.** Each year an independent assessor checks a sample of the monitoring.

**What forces a re-assessment.** A significant change (section 4.9), a measure past its threshold for three months running, a serious incident, or a new High risk. The authorising official then decides whether \<DocuView\> must be re-authorised.

**Review of this strategy.** Every 12 months with the policy, and after a re-authorisation.

### 4.9 Significant change

A significant change is one likely to alter \<DocuView\>'s security or privacy risk. It must be assessed before it is made (PRO-CA-6), and the authorising official decides whether \<DocuView\> must be re-assessed or re-authorised. These always count as significant:

1. A new or changed external connection, or a change to an agreement in section 4.7.
2. A new hosting site, or a new major version of Windows Server, PostgreSQL or .NET.
3. A change to how people sign in, or to the access control model in \<Access Control Management\>.
4. A new type of information, or a higher impact level for any information type.
5. A change to the boundary in \<System Security Plan\>.
6. A new High risk in \<Risk List\>.
7. A serious security incident or personal data breach.

Routine patches within the time limits of \<Security Operating Procedures\>, and changes to content or users, are not significant.

### 4.10 What ABC Technologies provides

**Table 14: Asked of ABC Technologies**

| Provided | Controls | What \<DocuView\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| An authorising official for its common controls, and their authorisation | CA-6 | The 65 inherited controls are authorised and working | EV-CA-01 | Not sent. To go in the first batch of requests to ABC Technologies (D-CA-12) |
| The agreements for the exchanges | CA-3 | A hosting and services agreement covering AD FS, central logging, the time service and the backup site; information exchange agreements for Jira and the Starters/Leavers system | EV-CA-02 | Not sent. To go in the first batch |
| Evidence for each inherited control | CA-6, and each control's own family | Each control's evidence request in \<Evidence Requests\> | By family | None sent |

| **SECTION 5** |
| --- |

## 5 Each control and enhancement

The controls are in NIST order. Each has two tables. The first takes each part of the control and gives what NIST requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 5.1 CA-1 Policy and Procedures

**Table 15: CA-1 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | An assessment, authorisation and monitoring policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (CA): a system-level policy. Purpose and scope are in section CA.1, responsibilities in CA.5, and commitment, coordination and compliance in CA.6. It is shared with everyone who administers \<DocuView\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-CA-09). Legally reviewed on 12 November 2026. Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (CA): seven procedures, PRO-CA-1 to PRO-CA-7, each naming who acts, how often and the record. Shared with the same people | Approved by the system owner (D-CA-10). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | Neil Ramsbottom is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 8 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 16: CA-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control, and each review is recorded in the change history |
| Rules and procedures | The whole policy (\<Policy\>, sections CA.3 and CA.4); all seven procedures (\<Procedures\> (CA)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; walk-through records on TPL-4; review records. The approvals exist; the rest do not yet |
| Status | Partially implemented |
| Risk decision | NC-CA-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures, and walk through each procedure |

### 5.2 CA-2 Control Assessments

**Table 17: CA-2 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Choose an assessor or team suited to the assessment | Two levels (section 4.3). Level 1 is the system owner's self-assessment. Level 2 is by an independent team led by Josh Leak | Level 1 was carried out by Claude, an AI assistant, for the system owner. Josh Leak's team is chosen for Level 2 (D-CA-05) |
| b | Write an assessment plan: the controls in scope, the procedures, and the environment, team and roles | Each family has a plan in \<Control Assessment Record\>, giving the scope, NIST SP 800-53A procedures, site, assessor, methods, depth and coverage, and what is needed from ABC Technologies | All 19 plans are written |
| c | The authorising official approves the plan before the assessment | The authorising official approves each plan (PRO-CA-1, step 1) | All 19 plans approved (D-GEN-18) |
| d | Assess the controls on a schedule, to see whether they are in place, work as intended and give the result wanted | Every 12 months, and after a significant change. Every determination statement in NIST SP 800-53A is given a finding | Level 1 done for all 19 families, between 5 and 12 November 2026. Level 2 has not been held (PA-106) |
| e | Write a report of the results | \<Security Assessment Report\>, the Security Assessment Report, which brings together the 19 family chapters of \<Control Assessment Record\> | Issued for Level 1. The Level 2 report will replace it |
| f | Give the results to defined people | The system owner, the authorising official and the Head of Cyber | \<Security Assessment Report\> was given to all three on 8 November 2026 (D-CA-10) |

**Table 18: CA-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, security assessor |
| Enforced by | Not a system function. No authorisation is given without an approved plan and a report (PRO-CA-4) |
| Rules and procedures | Policy principle P1; rule R1 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-1 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | The approved plans; the assessment record and report; proof the report was given to the three recipients; the evidence each finding rests on. All exist for Level 1; none for Level 2 |
| Status | Partially implemented |
| Risk decision | NC-CA-02, rated Low: approve |
| Open items | PA-106: hold the Level 2 assessment. PA-109: commission a penetration test before go-live, which goes beyond the baseline |

### 5.3 CA-2(1) Independent Assessors

**Table 19: CA-2(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Use assessors who are independent | Josh Leak's team carries out Level 2. A member counts as independent if they have had no part in designing, building, running or administering \<DocuView\>, and each confirms it on TPL-19 before starting (policy rule R2) | The team is chosen (D-CA-05). No member has completed TPL-19, and Level 2 has not been held (PA-106) |

**Table 20: CA-2(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security assessor |
| Enforced by | Not a system function. The authorising official accepts each TPL-19 before the assessment starts |
| Rules and procedures | Policy principle P1; rule R2 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-1 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | A completed TPL-19 for each assessor; the Level 2 plan naming the team. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CA-03, rated Low: approve |
| Open items | PA-106: obtain each assessor's independence statement on TPL-19, then hold Level 2 |

### 5.4 CA-3 Information Exchange

**Table 21: CA-3 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Approve and manage each exchange with another system, using a defined kind of agreement | Every exchange is recorded in the interface record (section 4.7) with its agreement type, chosen under NIST SP 800-47 Rev 1, and the system owner approves it before it is used (PRO-CA-2). Exchanges with ABC Technologies' own services rest on its hosting and services agreement; the Jira and Starters/Leavers exchanges each have an information exchange agreement | Six external exchanges are recorded. None is approved or in use, and no agreement is signed (PA-63). The agreements have not been asked for (EV-CA-02) |
| b | Record, in each agreement, the interface, the security and privacy needs, the controls, the responsibilities and the impact level | The interface record holds all of these for each exchange, and each agreement repeats them | Recorded for all six. No agreement yet holds them |
| c | Review and update the agreements on a schedule | Every 12 months, by the system owner with the owner of the other system. An exchange no longer needed is ended | Not yet due: nothing is signed |

**Table 22: CA-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, ABC Technologies |
| Enforced by | The system owner's approval before a connection is built; ABC Technologies' firewall, which allows only the flows \<DocuView\> has asked for (\<Access Control Management\>, section 4.6.4) |
| Rules and procedures | Policy principle P4; rule R3 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-2 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | The interface record; each signed agreement, with its date and review date; the yearly review records. Only the interface record exists |
| Status | Not implemented |
| Risk decision | NC-CA-04, rated Low: approve |
| Open items | PA-63: approve each exchange when it is built, and sign the agreements (EV-CA-02) |

### 5.5 CA-5 Plan of Action and Milestones

**Table 23: CA-5 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Keep a plan of action and milestones that records the planned fixes for weaknesses found in assessments | \<Plan of Action and Milestones\>. Every weakness that needs a fix has one item, with its control, source, fix, owner, resources, milestone, due time and state. Each open item must be fixed within the time for its rating (section 4.4) | The plan exists and is current to 12 November 2026 |
| b | Update it on a schedule, from assessments, audits and monitoring | Monthly, by the system owner. An item closes only when the fix is tested and the evidence recorded. Overdue items go to the authorising official each quarter (PRO-CA-3) | Updated as each review has found items. The monthly cycle and calendar dates start when development is scheduled (PA-108) |

**Table 24: CA-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function. The consistency test checks that every item named in the Risk List exists in the plan, and that the report gives the plan's counts |
| Rules and procedures | Policy principle P3; rule R4 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-3 (\<Procedures\> (CA)) |
| Tests | Checks of the consistency test on the plan's item counts and links pass. They test the documents, not the process |
| Records an assessor will ask for | The plan and its change history; the monthly update records; the quarterly reports of overdue items; evidence for each closed item. The plan and history exist; no monthly or quarterly record yet |
| Status | Partially implemented |
| Risk decision | NC-CA-05, rated Low: approve |
| Open items | PA-108: start the monthly updates and quarterly reports |

### 5.6 CA-6 Authorization

**Table 25: CA-6 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Name a senior official as the authorising official for the system | The authorising official, Bob Jones | Assigned (D-GEN-02) |
| b | Name a senior official as the authorising official for the common controls the system inherits | ABC Technologies' official for its common controls, \[ABC common control official\] | Not named: asked of ABC Technologies (EV-CA-01), not yet sent |
| c.1 | Before operation, the system's authorising official accepts the use of the inherited common controls | The authorising official accepts the 65 inherited controls in section 4.6 on TPL-18, once ABC Technologies' evidence is in (PRO-CA-7) | An earlier list of 66 was accepted as a list (D-CA-08). The list has since changed, and no control is accepted for operation (PA-107) |
| c.2 | Before operation, the authorising official authorises the system | \<DocuView\> holds no production documents until the authorising official has authorised it, from the package in section 4.5, accepting the remaining risk by name on TPL-18, with terms, conditions and an end date no more than 12 months away (PRO-CA-4) | Not authorised. \<Security Assessment Report\>, section 7, lists the conditions to meet first |
| d | The common controls' authorising official authorises them for use | ABC Technologies' official authorises its common controls, and \<DocuView\> holds the record | Not evidenced (EV-CA-01) |
| e | Update the authorisations on a schedule | Every 12 months, and after a significant change (section 4.9) | Not yet due: nothing is authorised |

**Table 26: CA-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Authorising official |
| Enforced by | Policy: no production documents before authorisation. The decision is recorded on TPL-18 |
| Rules and procedures | Policy principle P2; rules R5, R7 to R9 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-4, PRO-CA-6, PRO-CA-7 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | The authorisation package; the signed TPL-18 decision, with its terms and end date; ABC Technologies' authorisation of its common controls; each yearly update. The package is defined, and most of it exists; no decision exists |
| Status | Partially implemented |
| Risk decision | NC-CA-06, rated Medium: decide before production |
| Open items | PA-107: obtain ABC Technologies' evidence and its official's name (EV-CA-01), have the inherited controls accepted again, and put the package to the authorising official |

### 5.7 CA-7 Continuous Monitoring

**Table 27: CA-7 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Set the measures to be monitored | The 14 measures in section 4.8, each with a target, a threshold for action, a source, a frequency and an owner | Twelve set and approved on 6 and 8 November 2026 (D-CA-03, D-CA-10); two added on 13 November 2026 (D-CA-13) |
| b | Set how often to monitor, and how often to assess controls | Measures monthly, with each duty in the \<Security Operating Procedures\> operating calendar at its own frequency. Control assessment every 12 months | Set |
| c | Keep assessing controls, as the strategy says | Each control is checked at the frequency of its duty in the operating calendar; those with no duty are checked at the yearly assessment | Not started: \<DocuView\> is not in use (PA-108) |
| d | Keep monitoring the measures | The security officer collects the measures each month on TPL-8 | Not started |
| e | Bring together and analyse what the assessments and monitoring produce | Each month the security officer reads the measures together with the audit review findings, the vulnerability results and the incident records, and looks for a trend across three months | Not started |
| f | Act on the results | A measure past its threshold is acted on in the month and the action recorded on TPL-8. One not put right in the month becomes a POA&M item. Three months past a threshold, a serious incident or a new High risk forces a re-assessment | Not started |
| g | Report the security and privacy state to defined people on a schedule | Monthly to the system owner, and quarterly to the authorising official, with overdue POA&M items, changes in risk, significant changes and incidents. Privacy measures are in the same report | Not started |

**Table 28: CA-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer, system owner |
| Enforced by | Not a system function. The duties are in the \<Security Operating Procedures\> operating calendar, and each names its record |
| Rules and procedures | Policy rule R6 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-5 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | The strategy; the monthly reports on TPL-8; the quarterly reports to the authorising official; records of action on any measure past its threshold. The strategy exists; no report yet |
| Status | Not implemented |
| Risk decision | NC-CA-07, rated Low: approve |
| Open items | PA-108: start monitoring and reporting at go-live. PA-80: compare the servers with the baseline each month |

### 5.8 CA-7(1) Independent Assessment

**Table 29: CA-7(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Use independent assessors to monitor the controls on a continuing basis | Each year an independent assessor, who has completed TPL-19, checks a sample of the monitoring: that the measures were collected, are accurate, and were acted on (PRO-CA-5, step 3) | Not started (PA-108) |

**Table 30: CA-7(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security assessor |
| Enforced by | Not a system function |
| Rules and procedures | Policy rules R2, R6 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-5 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | The assessor's TPL-19; the report of each yearly check. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CA-08, rated Low: approve |
| Open items | PA-108: hold the first independent check within 12 months of go-live |

### 5.9 CA-7(4) Risk Monitoring

**Table 31: CA-7(4) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Monitor whether the controls are effective | Six of the measures are of effectiveness: updates applied in time, failed sign-ins and lockouts, logging failures, backups with restore tests, incidents past their time limit, and vulnerabilities past their fix time (section 4.8) | Defined. Not started (PA-108) |
| b | Monitor compliance | Four of the measures are of compliance: overdue POA&M items, audit reviews completed, access reviews on time, and unused group members | Defined. Not started |
| c | Monitor change | Two of the measures are of change: significant changes assessed before they were made, and drift from the baseline. The system owner also reviews the Risk List each month for new or changed risks | Defined. Not started |

**Table 32: CA-7(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R6 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-5 (\<Procedures\> (CA)) |
| Tests | None: this control is examined from documents and records. There is no system mechanism to test |
| Records an assessor will ask for | The monthly reports showing each kind of measure; the Risk List's review dates. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CA-09, rated Low: approve |
| Open items | PA-108: start monitoring at go-live |

### 5.10 CA-9 Internal Connections

**Table 33: CA-9 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Authorise the internal connections of defined components | Two internal connections, between the components on the application server and the database server: the two user-facing apps to the API, and the API to the database. The system owner authorises each in the interface record before it is built (section 4.7) | Both are recorded as planned. Neither is authorised, as the servers are not built (PA-63) |
| b | Record, for each, the interface, the security and privacy needs and the information carried | The interface record holds all three for each | Recorded |
| c | End a connection after defined conditions | When it is no longer needed, or a server is rebuilt. The Windows server administrator removes it, and the system owner records the end date (PRO-CA-2, step 3) | Not yet used |
| d | Review the continued need on a schedule | Every 12 months, with the external exchanges | Not yet due |

**Table 34: CA-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Windows server and database administrators |
| Enforced by | The API listens only on the loopback address and accepts only the two apps; the database accepts only the application server (\<Access Control Management\>, section 4.6) |
| Rules and procedures | Policy principle P4; rule R3 (\<Policy\>, sections CA.3 and CA.4); PRO-CA-2 (\<Procedures\> (CA)) |
| Tests | None for this control. The tests of the connections themselves are under AC-4 and SC-8, in the tested build |
| Records an assessor will ask for | The interface record with the system owner's authorisation of each connection; the yearly review. Only the record exists |
| Status | Not implemented |
| Risk decision | NC-CA-10, rated Low: approve |
| Open items | PA-63: authorise each connection when the servers are built |

| **APPENDIX A** |
| --- |

## Appendix A Parameter register

These are NIST's organisation-defined values for the 10 CA entries: 25 in total. State now says whether each is met today. The values were agreed on 6 and 8 November 2026 (D-CA-P01).

**Table 35: CA parameter register**

| NIST identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| CA-01\_ODP\[01\] | Who receives the policy | Everyone who administers \<DocuView\> | Not yet: shared when issued (PA-20) |
| CA-01\_ODP\[02\] | Who receives the procedures | Everyone who administers \<DocuView\> | Not yet: shared when issued (PA-20) |
| CA-01\_ODP\[03\] | Level of the policy | System level | Met |
| CA-01\_ODP\[04\] | Official who manages them | System owner | Met |
| CA-01\_ODP\[05\] | Policy review frequency | Every 12 months | Met: set |
| CA-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: reviewed on 8 November 2026 |
| CA-01\_ODP\[07\] | Procedures review frequency | Every 12 months | Met: set |
| CA-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: reviewed on 8 November 2026 |
| CA-02\_ODP\[01\] | Assessment frequency | Every 12 months, and after a significant change | Met: Level 1 done; Level 2 to come |
| CA-02\_ODP\[02\] | Who receives results | System owner, authorising official and Head of Cyber | Met: \<Security Assessment Report\> issued on 8 November 2026 |
| CA-03\_ODP\[01\] | How exchanges are managed | Another type of agreement | Met: set |
| CA-03\_ODP\[02\] | Type of agreement | The type set for each exchange in section 4.7 | Not yet: no agreement signed |
| CA-03\_ODP\[03\] | Review frequency | Every 12 months | Not yet: no agreement signed |
| CA-05\_ODP | POA&M update frequency | Monthly | Met: updated on 8 November 2026; monthly from go-live |
| CA-06\_ODP | Authorisation update frequency | Every 12 months, and after a significant change | Not yet: not authorised |
| CA-07\_ODP\[01\] | System-level metrics | The measures in section 4.8 | Not yet: monitoring starts at go-live |
| CA-07\_ODP\[02\] | Monitoring frequency | Monthly, with the duties in \<Security Operating Procedures\> at their own frequency | Not yet: starts at go-live |
| CA-07\_ODP\[03\] | Assessment frequency | Every 12 months | Not yet: starts at go-live |
| CA-07\_ODP\[04\] | Who receives security status | System owner and authorising official | Not yet: starts at go-live |
| CA-07\_ODP\[05\] | Security reporting frequency | Monthly to the system owner, quarterly to the authorising official | Not yet: starts at go-live |
| CA-07\_ODP\[06\] | Who receives privacy status | System owner and authorising official | Not yet: starts at go-live |
| CA-07\_ODP\[07\] | Privacy reporting frequency | Monthly to the system owner, quarterly to the authorising official | Not yet: starts at go-live |
| CA-09\_ODP\[01\] | Components | The application VM and the database VM | Not assessable: VMs not built |
| CA-09\_ODP\[02\] | When a connection ends | When it is no longer needed, or a VM is rebuilt | Met: set; PRO-CA-2 |
| CA-09\_ODP\[03\] | Review frequency | Every 12 months | Not yet: VMs not built |

| **APPENDIX B** |
| --- |

## Appendix B CA controls outside the Moderate baseline

NIST does not select these at Moderate, so they are not assessed.

**Table 36: CA controls not selected at Moderate**

| Control | What it adds | \<DocuView\>'s position |
| --- | --- | --- |
| CA-2(2) Specialized Assessments | In-depth monitoring, scanning and testing as part of assessment | Not required. Vulnerability scanning is done under RA-5 |
| CA-2(3) Leveraging Results from External Organizations | Accepting another organisation's assessment | Not required. ABC Technologies' evidence is examined, not accepted unseen |
| CA-3(6), CA-3(7) Transfer Authorizations; Transitive Information Exchanges | Checks on what the other system may do with the information | Not required, and not done |
| CA-7(3) Trend Analyses | Using trends to adjust monitoring | Not required. Done in part: the monthly analysis looks across three months |
| CA-7(5), CA-7(6) Consistency Analysis; Automation Support | Further assurance and automation of monitoring | Not required, and not done |
| CA-8 Penetration Testing | Penetration testing of the system | Selected only at High, so not required. The system owner has decided to commission one anyway, before go-live: by a tester independent of the build, on the servers, covering the two user-facing apps, the API and sign-in through AD FS, with each finding rated in the Risk List (D-CA-12, PA-109). Tester and date: \[to be set\] |
| CA-9(1) Compliance Checks | Security checks on a component before it connects | Not required, and not done |
