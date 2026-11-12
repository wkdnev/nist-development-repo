# \<DocuView\> Audit and Accountability Management

**\<ref\> | Version \<ver\> | Draft for the system owner's approval**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Summary](#3-summary)

[4 The audit design](#4-the-audit-design)

[5 Each control and enhancement](#5-each-control-and-enhancement)

[Appendix A How logging was built in the tested build](#appendix-a-how-logging-was-built-in-the-tested-build)

[Appendix B Parameter register](#appendix-b-parameter-register)

[Appendix C Server logging settings](#appendix-c-server-logging-settings)

[Appendix D The rest of NIST's catalogue](#appendix-d-the-rest-of-nists-catalogue)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Audit and Accountability Management |
| Version | \<ver\> |
| Status | Draft for the system owner's approval |
| Date | 12 November 2026 |
| Owner | System owner |
| Applies to | Audit and Accountability family |
| Classification | Restricted |
| Next review | Every 12 months, and after a significant incident, audit finding or system change |
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
| \<ver\> | 12 November 2026 | Finalised with the system owner's decisions (D-AU-12): the PostgreSQL logging settings and the legal hold rule are adopted as the design; selection of events by release is recommended for acceptance; and the archive location is settled with ABC Technologies' storage |
| \<ver\> | 12 November 2026 | Cross-check against NIST's guidance for the family: the events include the use of privileged functions; the content of server records, the archive, legal hold, backups and storage failure are stated; the gap in selecting events without a release is registered (PA-105); and three appendix tables are added: proposed PostgreSQL logging settings, the logging other controls require, and the AU controls outside the Moderate baseline |
| \<ver\> | 12 November 2026 | The system owner's answers to the review (D-AU-11), as recommended: only the API writes audit records; ABC Technologies is asked for a weekly report of AD FS and Active Directory records; the session field holds a hash, never the session ID; the reason \<DocuView\> keeps running when logging fails is recorded; and the method for sizing storage is set |
| \<ver\> | 12 November 2026 | Issued with the set: no change to the content |
| \<ver\> | 12 November 2026 | First draft, at the system owner's request (D-AU-10). The audit chapter of \<Control Implementation Register\> moved here in full, so that the audit design is held only in this document, and each control is set out part by part. The wording follows sign-in through AD FS (D-AC-23), the single database account (D-AC-18) and ABC Technologies' corporate configuration (D-AC-21). No agreed value is changed |

| **SECTION 2** |
| --- |

## 2 Purpose

This document shows how audit logging and accountability are designed for \<DocuView\>, for each of the 16 Audit and Accountability (AU) controls and enhancements in the NIST SP 800-53 Rev 5 Moderate baseline. Section 4 sets out the design: where audit records come from, which events are logged and why, what a record holds, how records are stored and protected, time, retention, review, and alerts. Section 5 takes each control in turn. Appendix A records how logging was built in the tested build. Appendix B lists every value NIST asks the organisation to define. Appendix C gives the logging settings for the database server. Appendix D shows the logging that other controls require, and the AU controls NIST does not select at Moderate. The design follows the good practice in NIST SP 800-92.

This is the only place the audit design is held. Other documents point here. The policy is in \<Policy\> (AU), and the steps people follow are in \<Procedures\> (AU) and \<Security Operating Procedures\>, section 5.2.

An assessor examines the list of events, the record content, the settings that protect and keep the records, and the review records. They interview the auditor, the administrators and the system owner, and test that the system logs what the design says (NIST SP 800-53A). So for each control section 5 gives:

- **each part of the control**, as NIST letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Design and today.** The Design column is what the system owner has agreed. The Today column is what was found in the code labelled v1.0, tested in Docker between 5 and 9 November 2026, and the position of the servers, which are not yet built. That build signed in with its own passwords. \<DocuView\> signs in through ABC Technologies' AD FS (D-AC-23), so the tests are to be repeated on that build (PA-95).

**Table 4: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

| **SECTION 3** |
| --- |

## 3 Summary

Of the 16 controls, none is fully implemented, 11 are partially implemented and 5 are not implemented. No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 5: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| AU-1 | Policy and Procedures | Partially implemented | The policy and procedures are not yet shared or walked through | NC-AU-01; PA-20 |
| AU-2 | Event Logging | Partially implemented | Changes made in the admin portal, reading of the audit log, start-up and shut-down, and changes to logging are not logged. Logging of configuration changes is not confirmed. Nothing is agreed with ABC Technologies on its AD FS and Active Directory records | NC-AU-02, NC-AU-17; PA-14, PA-76, PA-101, PA-103 |
| AU-3 | Content of Audit Records | Partially implemented | Some records name "System" instead of the person. Server records are not examined | NC-AU-03; PA-14, PA-43 |
| AU-3(1) | Additional Audit Information | Partially implemented | It is not checked that the session field holds a reference and not the live session ID | None; PA-104 |
| AU-4 | Audit Log Storage Capacity | Not implemented | No capacity is planned, as the servers are not built | NC-AU-04; PA-42 |
| AU-5 | Response to Audit Logging Process Failures | Partially implemented | Nobody is alerted when logging fails | NC-AU-05; PA-38 |
| AU-6 | Audit Record Review, Analysis and Reporting | Not implemented | The weekly review has not started | NC-AU-06; PA-40 |
| AU-6(1) | Automated Process Integration | Not implemented | No alert is built, and ABC Technologies' central monitoring is not confirmed | NC-AU-07; PA-40, PA-59 |
| AU-6(3) | Correlate Audit Record Repositories | Not implemented | Only the application audit log can be reviewed. The manual comparison is accepted to 6 November 2027 | NC-AU-08; PA-40, PA-43, PA-101 |
| AU-7 | Audit Record Reduction and Report Generation | Partially implemented | No export or report | NC-AU-09; PA-41 |
| AU-7(1) | Automatic Processing | Partially implemented | No search by project or document, and no choice of sort order | NC-AU-10; PA-41 |
| AU-8 | Time Stamps | Partially implemented | The servers' time source is not set or evidenced | NC-AU-11; PA-102, EV-AU-02 |
| AU-9 | Protection of Audit Information | Partially implemented | The application's database account can change and delete records. The chain hash has no key, cannot be recomputed, and is not checked. The application log repeats audit details | NC-AU-12, NC-AU-16; PA-29, PA-36, PA-37, PA-73, PA-74, PA-75 |
| AU-9(4) | Access by Subset of Privileged Users | Partially implemented | Global administrators can read the audit records | NC-AU-13; PA-39 |
| AU-11 | Audit Record Retention | Not implemented | No archive, backup or capacity is behind the retention rule | NC-AU-14; PA-42 |
| AU-12 | Audit Record Generation | Partially implemented | PostgreSQL logging is off, Windows logging is not built, and some application events write no record. Events cannot be selected without a release | NC-AU-15, NC-AU-17; PA-14, PA-43, PA-76, PA-105 |

AU-3(3), limiting personal data in audit records, is in the privacy baseline and is assessed with the PT family (NC-PT-09; PA-71, PA-75). Section 4.4 holds its design.

The two most serious gaps are both in AU-9. The application's database account can change and delete audit records (PA-36, rated High), and the chain hash that should reveal a change has no key and cannot be recomputed (PA-73, PA-74). Until they are fixed, the audit log cannot be relied on as evidence (R-AU-01).

| **SECTION 4** |
| --- |

## 4 The audit design

### 4.1 Principles

1. **Complete.** The agreed events are recorded every time they occur.
2. **Attributable.** Each record shows what happened, when, where, from where, the outcome and who was involved. The person is the one AD FS authenticated.
3. **Protected.** Nobody can change or delete a record. Only auditors read them.
4. **Reviewed.** Records are examined every week by someone who does not administer the system.
5. **Retained.** Records are kept for 24 months: long enough to investigate an incident found late.
6. **No secrets.** Records never hold a password, key, token or live session ID, and hold only the personal data an investigation needs.
7. **One audit log.** \<DocuView\> has one application audit log, written only by the API, as the system owner confirmed on 12 November 2026 (D-AU-11). Any other log that repeats its content is protected as audit information.

These carry out the principles and rules of \<Policy\>, sections AU.3 and AU.4.

### 4.2 Where audit records come from

An investigation must be able to follow an action from the network to the database. So records come from six sources. \<DocuView\>'s team controls the first three. ABC Technologies controls the rest, as part of its corporate configuration (D-AC-21, D-AC-23).

![Figure 1: Where audit records come from, and who reads them](figures/aum-figure-1.png)

**Figure 1: Where audit records come from, and who reads them**

**Table 6: Sources of audit records**

| Source | Events to log | Held in | Set by | Today |
| --- | --- | --- | --- | --- |
| DV\_Web, DV\_Admin\_UI and DV\_API | The events in Table 7 | The audit log: table `dbo.AuditLog` in the \<DocuView\> database | \<DocuView\>'s developers, in code | Partly logged (Table 7) |
| The three applications' own logs | Errors, start-up and shut-down, and logging failures. No audit details | Log files on the application server, kept 30 days | \<DocuView\>'s developers | They also repeat usernames, IP addresses and session IDs (A38, PA-75) |
| PostgreSQL | Connections and failed connections; role and permission changes; schema changes; any change to or deletion of audit records; changes to logging settings | The PostgreSQL log on the database server | Database administrator | Statement and connection logging are off (A30, PA-43) |
| Windows Server 2025, both servers | Sign-ins and failed sign-ins (events 4624, 4625); account and group changes (4720, 4722 to 4726, 4728, 4732, 4756); use of special privileges (4672); audit policy changes (4719); security log cleared (1102); services installed (7045); system time changed (4616) | The Windows Security and System logs on each server, forwarded to ABC Technologies' central monitoring if confirmed (D-AU-07) | ABC Technologies' Group Policy. \<DocuView\> states the events it needs (EV-AU-04) | Not assessable: the servers are not built (PA-43) |
| AD FS and Active Directory | Every sign-in attempt, failed sign-in, lockout and second-factor result for \<DocuView\>; every change to an account; every change to the members of \<DocuView\>'s groups | ABC Technologies' own logs | ABC Technologies | Not evidenced. No arrangement yet gives \<DocuView\>'s auditor these records (PA-101, EV-AU-05) |
| ABC Technologies' network services | Firewall and VPN events, and the time service | ABC Technologies' central monitoring | ABC Technologies | Inherited; to be confirmed (D-AU-07, EV-AU-01) |

Each source logs at every occurrence. The system owner selects the events and reviews the list every 12 months (PRO-AU-5).

### 4.3 Application events

Table 7 lists the events \<DocuView\>'s applications log, and what an investigator learns from each. That is the reason each is selected (AU-2, part d).

**Table 7: Application events logged**

| Events | Why they are needed to investigate an incident | Logged today? |
| --- | --- | --- |
| Sign-ins and sign-outs. \<DocuView\> records each sign-in it accepts and each sign-in token it refuses. Failed passwords and second factors are recorded by AD FS (Table 6) | Shows who entered the system, and any attempt to enter without the right | Yes, in the tested build, for its own sign-in and failed sign-in (A15, A16). To be repeated with AD FS (PA-95) |
| Session creation, ending and time-outs | Links activity to one sign-in | Partly: ending all of a user's sessions is not logged (PA-14) |
| Changes to projects, to the AD groups each project uses, and to role mappings | Shows who was given a route to information, and by whom. Changes to the members of a group are recorded by Active Directory (Table 6) | Partly: most changes in the admin portal are not logged (PA-14) |
| Denied access | Shows attempts to reach restricted information | Yes (A18) |
| Document views, downloads, exports and searches | Shows who saw which information | Yes (A17) |
| Document corrections and deletions | Shows who changed or removed a record about a person | No (PA-89) |
| Use of privileged functions: ending sessions, the maintenance pages, cache management and database maintenance (\<Access Control Management\>, section 4.8) | Shows what each administrator did with their extra rights (AC-6(9)) | Partly: ending a user's sessions and the maintenance pages are not logged (T37; PA-14, PA-31) |
| Configuration changes | Shows changes to security settings | Not confirmed: the event type exists (PA-103) |
| Reading or searching the audit log | Shows who looked at audit records, which AU-9 protects | No (PA-76) |
| Start-up and shut-down of each application | Shows periods when nothing could be logged | No (PA-76) |
| Changes to logging, and audit chain check results | Shows attempts to stop or hide logging | No (PA-76) |
| Logging failures | Shows periods without records | Application log only (A31, PA-38) |

\<DocuView\> holds no passwords, so it logs no password change or reset (D-AC-23). Those are recorded in Active Directory.

### 4.4 What a record holds

Every application record has the same fields. Table 8 shows which part of AU-3 each meets.

**Table 8: Audit record content**

| Field | Holds | Meets |
| --- | --- | --- |
| Event type, Action | What happened | AU-3, part a |
| Time | When, in UTC | AU-3, part b; AU-8 |
| Source component | Which application raised the event | AU-3, part c |
| IP address, Browser | Where the person came from | AU-3, part d; AU-3(1) |
| Result | Success, failure or refused | AU-3, part e |
| Username, User ID | Who acted: the person AD FS authenticated | AU-3, part f |
| Project, Document | What was acted on | AU-3, part f; AU-3(1) |
| Session | A reference that links the record to one sign-in: a SHA-256 hash of the session ID, never the ID itself, so that the record cannot be used to take over a session (rule R8; D-AU-11) | AU-3(1) |
| Details, Duration | Free text for the event, and how long it took | Supports investigation |
| Chain hash | A value calculated from the record and the one before it | AU-9 |

**Records from the servers.** PostgreSQL and Windows records must hold the same six kinds of content. Windows events do so by design. PostgreSQL does so once its log line is set to carry the time, the user, the database and the client address (appendix C). Neither has been examined, as the servers are not built (PA-43).

**Limits on content (rule R8; AU-3(3)).** A record never holds a password, key or token. It holds only the personal data an investigation needs: the named fields above. The free text holds no further personal data (check Q04), and is to be reviewed again (PA-71).

### 4.5 How records are stored and protected

**Table 9: Where audit information is held, and who can reach it**

| Store | Written by | Read by | Changed or deleted by | Today |
| --- | --- | --- | --- | --- |
| The audit log, `dbo.AuditLog` | DV\_API only, through its database service account, which can add records and nothing more (D-AC-18). DV\_Web and DV\_Admin\_UI send their events to the API, which accepts them only from those two applications and never from a user's browser (D-AU-11) | The auditor group, through the admin portal's audit pages. The database administrator can reach the table to archive it, under rule B12 | Nobody | Each application writes to the table itself. The application account can change, delete and empty it (A26 to A28; PA-36). A global administrator can read the pages (A25; PA-39). Ordinary users can add records (PA-29) |
| The offline archive, held at \[archive location, to be agreed with ABC Technologies with its storage (EV-AU-03)\], encrypted, and off the database server | The database administrator, each month, for records older than 12 months | The auditor, on request to the system owner | Nobody, until 24 months; then only with the system owner's recorded approval | No archive exists (PA-42) |
| The newest chain hash, copied daily | A scheduled job | The auditor and security officer | Not by the applications or their accounts | Not built (PA-73) |
| Application logs | Each application's Windows service account | The Windows server administrators and the auditor | Removed after 30 days | In the test environment they are not limited (PA-75) |
| PostgreSQL log | PostgreSQL | The database administrator and the auditor | Not by the API's account | Logging is off (PA-43) |
| Windows logs | Windows | The Windows server administrators; the auditor through ABC Technologies' report or monitoring | Clearing the log is itself logged (event 1102) | Not built |

**The chain hash.** Each record holds a hash of its own fields and the previous record's hash, so a changed or removed record breaks the chain. The design uses a keyed hash, HMAC-SHA-256, with the key held outside the database where the applications' accounts cannot read it. The newest hash is copied each day to a store the applications cannot write to, so that removing the newest records is also revealed. The time is rounded to the microsecond before hashing, so that a stored hash can be recomputed. The key is listed in the key register (\<Control Implementation Register\>, section SC.3).

**The chain check.** The check runs on a schedule and at each start-up (PRO-AU-2, PRO-SI-6). A break alerts the security officer and the auditor, who preserve the evidence before anything is changed and raise an incident.

**Table 10: Who may manage audit logging**

| Function | Who | How it is limited |
| --- | --- | --- |
| Read and search audit records | Auditors | AD group `DocViewer_Auditors`, owned by the system owner. An auditor holds no administration role (PRO-AU-6) |
| Change or delete an audit record | Nobody | The database account cannot; rule B12 forbids it |
| Select which application events are logged | System owner | Decided on the record; made by developers through a release (PRO-AU-5) |
| Change PostgreSQL logging settings | Database administrator | A recorded change (\<Configuration Management Plan\>) |
| Change the Windows audit policy | ABC Technologies | Its Group Policy and change process |
| Archive records, and delete them after 24 months | Database administrator | Deletion only with the system owner's recorded approval (PRO-AU-4) |
| Run the chain check and receive its alerts | Auditor and security officer | PRO-AU-2 |

Global administrators and administrators have none of these functions. They are the people whose actions the auditor reviews (\<Access Control Management\>, section 4.5).

### 4.6 Time

1. Every record's time is in UTC, to the nearest second or finer.
2. Each server takes its time from ABC Technologies' time service, \[ABC time source\], and stays within 1 second of UTC.
3. Each month the Windows server administrator checks both servers, records the result on TPL-8, and reports any drift over 5 seconds to the security officer (PRO-AU-4).
4. A change to a server's clock is itself a Windows event (4616).

One time source across the applications, the servers, AD FS and the network is what lets the auditor line records up from different stores (AU-6(3)).

NIST no longer asks for clock synchronisation under AU-8. In Revision 5 it moved to SC-45(1), which is not in the Moderate baseline. \<DocuView\> keeps the rule of 1 second anyway, because the weekly comparison across stores depends on it.

### 4.7 Retention and capacity

**Table 11: Retention**

| Information | Kept | Then |
| --- | --- | --- |
| Audit records | 12 months in the database | Moved to the offline archive, and the archive's SHA-256 hash recorded on TPL-8 |
| Archived audit records | A further 12 months | May be deleted, only with the system owner's recorded approval |
| Application logs | 30 days | Deleted |
| Records held as incident evidence | Until the incident is closed | As the incident record says (\<Incident Response Plan\>) |
| Records under a legal hold: a claim, a tribunal, a regulator's enquiry or a person's request for their data | Until the legal adviser releases them | The legal adviser tells the system owner and the database administrator, who mark the records so that they are not deleted (PRO-AU-4). The system owner adopted this rule on 12 November 2026 (D-AU-12); the legal adviser confirms its wording at the next review of the policy |
| Backup copies of the database, which include the audit log | As the backup schedule: 14 daily, 8 weekly and 12 monthly copies | Encrypted, and protected as audit information (\<Contingency Plan\>) |
| Windows, AD FS and Active Directory logs | As ABC Technologies sets; 12 months is expected | ABC Technologies' process (EV-AU-04, EV-AU-05) |

Storage is sized for the full 24 months: 12 months in the database, and the same again for the archive. The size is the number of records each day, \[records per day, to be measured\], times the average size of a record, \[bytes per record, to be measured\], times 365 days, plus half as much again for growth. Both figures are measured in the test environment before the request goes to ABC Technologies, and again in the first month of use (D-AU-11). The database administrator checks free space and the size of the audit table each month, and asks for more before records are at risk (PRO-AU-4). The audit log is backed up with the database (\<Contingency Plan\>).

### 4.8 Review, analysis and reporting

1. **Weekly review.** The auditor reviews the records since the last review, following \<Security Operating Procedures\>, section 5.2, which lists the unusual activity to look for (PRO-AU-1).
2. **Across stores.** The auditor compares the application records with the PostgreSQL and Windows logs and ABC Technologies' record of sign-ins and group changes, by time and username. This is done by hand, which the system owner has accepted to 6 November 2027 (NC-AU-08).
3. **Against requests.** Every change to access is checked against its approved Jira request (\<Access Control Management\>, section 4.13).
4. **Report.** Findings go to the security officer and system owner on TPL-8. Anything unexplained is raised as a security incident.
5. **More review when risk rises.** After an incident or new threat information, the system owner sets a more frequent or closer review.
6. **A second look at the most powerful.** The Head of Cyber checks the global administrators' actions (\<Security Operating Procedures\>, duty C16).

**Table 12: Search and sort on the audit page**

| Field | Design | Today |
| --- | --- | --- |
| Date | Search and sort | Search |
| Event type | Search and sort | Search |
| Result | Search and sort | Search |
| Username | Search and sort | Search |
| Project | Search and sort | Neither (PA-41) |
| Document | Search and sort | Neither (PA-41) |
| Export of the filtered records | Yes | No (PA-41) |

The page only reads. It cannot change a record or its order.

### 4.9 Failures and alerts

**Table 13: Alerts**

| Event | Alert to | Within | Then | Today |
| --- | --- | --- | --- | --- |
| A logging failure: an audit record cannot be written | Windows server administrator, security officer | 1 hour | \<DocuView\> keeps running, so that a logging fault cannot stop the service. Logging is restored, and the period without records is recorded (PRO-AU-3) | Application log only; nobody is told (PA-38) |
| A break in the audit chain, or other sign of tampering | Security officer, auditor | At once | Evidence is preserved, and an incident is raised (PRO-AU-2) | Nothing runs the check (PA-37) |
| A server clock more than 5 seconds from UTC | Security officer | At the monthly check | The Windows server administrator corrects it with ABC Technologies | Not built |
| Audit storage running low | Database administrator | At the monthly check | More storage is raised before records are at risk (PRO-AU-4) | Not built |

A full disk is a logging failure like any other: if the audit log cannot be written because storage has run out, the first alert in Table 13 applies. NIST's separate warning before storage fills, AU-5(1), is not in the Moderate baseline; the monthly check stands in for it.

Alerts are raised by the detection use cases in \<Control Implementation Register\>, section SI.5, of which U2 and U7 concern audit. None is built yet (PA-59).

### 4.10 The application logs

Each application also keeps its own log of errors, start-up and shut-down. In the tested build that log repeats every audit event, with the username, IP address and session ID (A38). Until that is fixed (PA-75), an interim rule applies, approved by the authorising official (D-AU-06):

1. The application logs are audit information. Only the Windows server administrators and the auditor may read them.
2. They are kept for 30 days and then deleted.
3. They are not copied off the servers, except as incident evidence.
4. Each month the Windows server administrator checks who can read them and how old they are (PRO-AU-7).

Once PA-75 is fixed, the application logs hold no audit details, personal data or session IDs.

### 4.11 What ABC Technologies provides

ABC Technologies sets these as part of its corporate configuration. The \<DocuView\> team has no control over them (D-AC-21, D-AC-23). \<DocuView\> states what it relies on, and asks for the evidence. What is expected below is the system owner's understanding, not evidence.

**Table 14: Provided by ABC Technologies**

| Provided | Controls | What \<DocuView\> relies on | Expected, not confirmed | Evidence asked |
| --- | --- | --- | --- | --- |
| Central log monitoring | AU-6(1), AU-6(3), AU-5 | It takes the Windows and PostgreSQL logs, and \<DocuView\>'s alerts, and tells the security officer | A central service takes the Windows and PostgreSQL logs. Open (D-AU-07) | EV-AU-01 |
| Time service | AU-8 | Both servers stay within 1 second of UTC | The domain controllers provide time | EV-AU-02 |
| Storage and backup | AU-4, AU-11 | Room for 12 months of records online, backed up daily, and somewhere to hold the offline archive | Storage is sized for 12 months, with daily backups | EV-AU-03 |
| Windows audit policy | AU-2, AU-12 | The Windows events in Table 6 are logged on both servers and kept | Group Policy sets the audit policy, and logs are kept for 12 months | EV-AU-04 |
| AD FS and Active Directory audit | AU-2, AU-6, AU-6(3), AU-12 | Every sign-in attempt for \<DocuView\>, and every change to \<DocuView\>'s groups and their members, is recorded, kept for at least 12 months, and sent to \<DocuView\>'s auditor as a weekly report, by \[route to be agreed with ABC Technologies\]. Read access for the auditor would also meet this (D-AU-11) | Not yet asked | EV-AU-05 |

The five requests, EV-AU-01 to EV-AU-05, are sent together, and central monitoring (D-AU-07) is to be settled with ABC Technologies' security contact before the servers are built (D-AU-11).

**Today:** no request has been sent, and none of this is evidenced.

| **SECTION 5** |
| --- |

## 5 Each control and enhancement

The controls are in NIST order. Each has two tables. The first takes each part of the control and gives what NIST requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 5.1 AU-1 Policy and Procedures

**Table 15: AU-1 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | An audit and accountability policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (AU): a system-level policy. Purpose and scope are in section AU.1, responsibilities in AU.5, and commitment, coordination and compliance in AU.6. It is shared with everyone who administers or reviews \<DocuView\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-AU-08). Legally reviewed on 12 November 2026. Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (AU): seven procedures, PRO-AU-1 to PRO-AU-7, each naming who acts, how often and the record. Shared with the same people | Approved by the system owner (D-AU-09). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | Neil Ramsbottom is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed after the audit review of 8 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 16: AU-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control, and each review is recorded in the change history |
| Rules and procedures | The whole policy (\<Policy\>, sections AU.3 and AU.4); all seven procedures (\<Procedures\> (AU)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; walk-through and review records. The approvals exist; the rest do not yet |
| Status | Partially implemented |
| Risk decision | NC-AU-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures, and walk through each procedure |

### 5.2 AU-2 Event Logging

**Table 17: AU-2 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Identify the types of event the system can log | For the applications, the event types listed in code, in `AuditEventTypes` in `DV_Shared/Security/AuditLog.cs`. For the servers, what PostgreSQL and Windows Server 2025 can log. Section 4.2 lists each source | The list exists in the v1.0 code |
| b | Coordinate event logging with the other parts of the organisation that need audit information | The system owner agrees with ABC Technologies' security contact two things, and records them: which logs ABC Technologies' monitoring needs from \<DocuView\> and its servers; and which of ABC Technologies' own records, of AD FS, Active Directory, the network and the VPN, \<DocuView\>'s auditor receives (section 4.11) | Not done. The request has not been sent (EV-AU-01, EV-AU-05), and whether central monitoring will take \<DocuView\>'s logs is open (D-AU-07) |
| c | Select the event types to log, and how often | The events in section 4.3 for the applications, and in section 4.2 for PostgreSQL, Windows and ABC Technologies' services. Each is logged at every occurrence | Partly. Most account, group and role changes in the admin portal are not logged (PA-14). Reading the audit log, start-up and shut-down, and changes to logging are not logged (PA-76). Whether configuration changes are logged is not confirmed (PA-103). PostgreSQL logging is off, and Windows is not built (PA-43) |
| d | Say why the selected events are enough to investigate an incident | Table 7 gives, for each event, what an investigator learns from it. Together they answer who signed in, what they saw or changed, what they were refused, who changed access or settings, and when nothing could be logged | Written and approved (D-AU-03, D-AU-09) |
| e | Review and update the selected events on a schedule | The system owner reviews the list every 12 months and on any change, and records the decision in \<Decision Register\> (PRO-AU-5) | Reviewed on 8 November 2026, and again on 12 November 2026 for sign-in through AD FS |

**Table 18: AU-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | System owner, developers |
| Enforced by | The application's audit service, which writes a record at each event; PostgreSQL and Windows logging settings on the servers |
| Rules and procedures | Policy principle P1; rule R1 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-5 (\<Procedures\> (AU)) |
| Tests | Checks A15 to A18 on the v1.0 code (Test-AuditAndAuth.ps1), 6 November 2026: sign-in and failed sign-in, document views and refused access each wrote a record. These checks ran on a build that used its own passwords and groups, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | The list of events and its yearly review record; the record of what was agreed with ABC Technologies; sample audit records for each event. The list exists; samples exist only from the test environment |
| Status | Partially implemented |
| Risk decision | NC-AU-02, rated Medium: remediate; NC-AU-17, rated Low: remediate (system owner, Low) |
| Open items | PA-14: log every change made in the admin portal. PA-76: log reading of the audit log, start-up and shut-down, and changes to logging. PA-101: agree with ABC Technologies how its AD FS and Active Directory records reach the auditor. PA-103: confirm that configuration changes are logged |

### 5.3 AU-3 Content of Audit Records

**Table 19: AU-3 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | What type of event occurred | Event type and Action (Table 8) | Present in every record tested (A19) |
| b | When it occurred | Time, in UTC | Present, in UTC (A22) |
| c | Where it occurred | Source component: the app that raised the event | Present |
| d | The source of the event | IP address and browser of the person's device | Present |
| e | The outcome | Result: success, failure or refused | Present |
| f | The identity of the people and things involved | Username and user ID of the person, taken from the AD FS token; the project and document acted on | Present. But some records written by the API name "System" where a person acted (PA-14) |

**Table 20: AU-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | Developers |
| Enforced by | The audit record definition in `DV_Shared/Security/AuditLog.cs`, which every app uses |
| Rules and procedures | Policy principle P2 (\<Policy\>, sections AU.3 and AU.4). No procedure: it is built into the system |
| Tests | Check A19 on the v1.0 code, 6 November 2026: every record held the six kinds of content. These checks ran on a build that used its own passwords and groups, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | The record definition; sample records showing each field. Samples exist only from the test environment |
| Status | Partially implemented |
| Risk decision | NC-AU-03, rated Low: remediate |
| Open items | PA-14: name the real person on every record |

### 5.4 AU-3(1) Additional Audit Information

**Table 21: AU-3(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Records also hold defined extra information | A session reference, which is a hash of the session ID and never the ID itself, the browser, the project and the document (Table 8) | The four fields are present in the tested build (A20, A21). Whether its session field holds the live ID or a reference has not been checked (PA-104) |

**Table 22: AU-3(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | Developers |
| Enforced by | The same record definition |
| Rules and procedures | Policy principle P2 (\<Policy\>, sections AU.3 and AU.4). No procedure: it is built into the system |
| Tests | Checks A20 and A21 on the v1.0 code, 6 November 2026: both passed. These checks ran on a build that used its own passwords and groups, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | Sample records showing the four fields |
| Status | Partially implemented |
| Risk decision | None: no finding |
| Open items | PA-104: confirm that the session field holds a hash and not the live session ID, and change it if not. The checks are to be repeated on the AD FS build (PA-95) |

### 5.5 AU-4 Audit Log Storage Capacity

**Table 23: AU-4 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Set aside enough storage for the audit records that must be kept | Storage for 24 months of records: 12 months in the database, and 12 months in the offline archive. The database administrator sizes it by the method in section 4.7: records each day, times their average size, times 365, plus half as much again. Each month they check free space and the size of the audit table, and ask for more before records are at risk (PRO-AU-4) | Not planned: the servers are not built (PA-42). ABC Technologies' storage and backup are not evidenced (EV-AU-03) |

**Table 24: AU-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Database administrator |
| Enforced by | The database server's storage, provided by ABC Technologies; the monthly check |
| Rules and procedures | Policy rule R2 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-4 (\<Procedures\> (AU)) |
| Tests | None: there is nothing to test until the servers are built |
| Records an assessor will ask for | The capacity calculation; the monthly check records on TPL-8; ABC Technologies' storage and backup description (EV-AU-03). None exist yet |
| Status | Not implemented |
| Risk decision | NC-AU-04, rated Low: obtain evidence |
| Open items | PA-42: size the storage and confirm backups on the servers |

### 5.6 AU-5 Response to Audit Logging Process Failures

**Table 25: AU-5 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Alert defined people within a defined time when logging fails | A failed audit write raises an alert to the Windows server administrator and the security officer within 1 hour (detection use case U7 in \<Control Implementation Register\>, section SI.5). The alert goes through ABC Technologies' central monitoring if that is confirmed; otherwise by \[alert route to be set at build\], which must not depend on \<DocuView\> itself being healthy | Not built. A failed write goes to the application log as a critical line, and nobody is told (A31, A35; PA-38) |
| b | Take defined further action | \<DocuView\> keeps running. The system owner chose this (D-AU-11): staff must still be able to reach HR records, a stop would let a logging fault take the whole service down, and the failure is alerted within 1 hour and the gap recorded. The Windows server and database administrators find the cause and restore logging. The security officer records the period with no records and tells the system owner. If records may be lost or changed, the evidence is preserved first (PRO-AU-3) | The tested build keeps running when a write fails (A32). The procedure has not been used |

**Table 26: AU-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Windows server administrator, security officer |
| Enforced by | The audit service's failure handling; the alert route, when built |
| Rules and procedures | Policy rule R6 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-3 (\<Procedures\> (AU)) |
| Tests | Checks A31, A32 and A35 on the v1.0 code, 6 and 8 November 2026. A31 and A32 passed: a failed write is logged as critical and the action carries on. A35 showed the gap: no alert reaches anyone |
| Records an assessor will ask for | The alert configuration; a sample alert and the response record on TPL-8. None exist yet |
| Status | Partially implemented |
| Risk decision | NC-AU-05, rated Medium: remediate |
| Open items | PA-38: send logging failures to the Windows server administrator and security officer within 1 hour |

### 5.7 AU-6 Audit Record Review, Analysis and Reporting

**Table 27: AU-6 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Review and analyse audit records on a schedule, for signs of defined unusual activity | The auditor reviews the records every week (PRO-AU-1), for the activity listed in \<Security Operating Procedures\>, section 5.2: repeated failed sign-ins and lockouts, refused access, sign-ins at unusual times, changes to access, large exports, configuration changes, reading of the audit log, gaps in the records, and records under unknown names. The auditor judges what each finding could lead to. The auditor holds no administration role, so nobody reviews their own actions | Not started: \<DocuView\> is not in use (PA-40) |
| b | Report findings to defined people | To the security officer and the system owner, on TPL-8, with the date, the period covered, the reviewer and the result. Anything unexplained is raised as a security incident | Not started |
| c | Change the level of review when the risk changes | After an incident or new threat information, the system owner sets a more frequent or closer review (PRO-AU-1, step 5) | Not yet used |

**Table 28: AU-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Auditor, security officer |
| Enforced by | Not a system function. The auditor's weekly duty C3 in \<Security Operating Procedures\>, checked by the Head of Cyber for global administrators' actions (duty C16) |
| Rules and procedures | Policy principle P4; rule R5 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-1 (\<Procedures\> (AU)) |
| Tests | None: a procedure, to be examined from its records |
| Records an assessor will ask for | The weekly review records on TPL-8; the reports made; any incident raised from a review. None exist yet |
| Status | Not implemented |
| Risk decision | NC-AU-06, rated Medium: remediate |
| Open items | PA-40: start the weekly review at go-live |

### 5.8 AU-6(1) Automated Process Integration

**Table 29: AU-6(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Join up review, analysis and reporting using automated means | Two means. The admin portal's audit page, which filters and summarises the records for the auditor. And ABC Technologies' central monitoring, if it is confirmed to take \<DocuView\>'s logs, which would raise the alerts in the detection use cases U1 to U8 (\<Control Implementation Register\>, section SI.5) | The audit page only. Whether central monitoring will take the logs is open (D-AU-07), and no alert is built (PA-59) |

**Table 30: AU-6(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Auditor, ABC Technologies |
| Enforced by | The audit page; ABC Technologies' central monitoring, if confirmed |
| Rules and procedures | Policy rule R5 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-1 (\<Procedures\> (AU)) |
| Tests | None |
| Records an assessor will ask for | ABC Technologies' description of its monitoring and what it takes from \<DocuView\> (EV-AU-01); the alert rules. None exist yet |
| Status | Not implemented |
| Risk decision | NC-AU-07, rated Low: obtain evidence |
| Open items | PA-40: confirm ABC Technologies' central monitoring (D-AU-07, EV-AU-01) |

### 5.9 AU-6(3) Correlate Audit Record Repositories

**Table 31: AU-6(3) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Analyse records from different stores together, to see the whole picture | Each week the auditor compares the application audit log with the PostgreSQL log, the Windows logs, and ABC Technologies' record of AD FS sign-ins and Active Directory group changes for \<DocuView\>, lining them up by UTC time and username. This is done by hand. The system owner accepted that as proportionate for one system (NC-AU-08), to 6 November 2027 | Only the application audit log can be reviewed today. The other logs are off, not built, or not yet shared with the auditor (PA-43, PA-101) |

**Table 32: AU-6(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Auditor, ABC Technologies |
| Enforced by | Not a system function: a weekly comparison by the auditor |
| Rules and procedures | Policy rule R5 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-1 (\<Procedures\> (AU)) |
| Tests | None |
| Records an assessor will ask for | The weekly review records showing each store compared; the acceptance of the manual method (\<Risk List\>). The acceptance exists |
| Status | Not implemented |
| Risk decision | NC-AU-08, rated Low: accepted |
| Open items | PA-40: start the review. PA-43: turn on database and Windows logging. PA-101: obtain ABC Technologies' AD FS and Active Directory records |

### 5.10 AU-7 Audit Record Reduction and Report Generation

**Table 33: AU-7 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Provide a way to cut records down and make reports, for review on demand and for investigation after the event | The admin portal's audit page, at `/sysadmin/audit-logs`, filters the records and shows a summary. An export gives the auditor the filtered records as a file for a report or an investigation | The page filters by date, event type, result and username (A23, A24). There is no export and no report (PA-41) |
| b | Do not change the content or time order of the records | The page only reads. It cannot change a record, and an export is a copy. Records are always shown with their stored time | The page changes nothing (A23, A24) |

**Table 34: AU-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | Developers |
| Enforced by | The audit page, open only to the auditor group |
| Rules and procedures | Policy principle P4 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-1 (\<Procedures\> (AU)) |
| Tests | Checks A23 and A24 on the v1.0 code, 6 November 2026: both passed. These checks ran on a build that used its own passwords and groups, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | A demonstration of the page; a sample report or export. No export exists yet |
| Status | Partially implemented |
| Risk decision | NC-AU-09, rated Low: remediate |
| Open items | PA-41: add an export |

### 5.11 AU-7(1) Automatic Processing

**Table 35: AU-7(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Sort and search records on defined fields | Search and sort on six fields: date, event type, result, username, project and document | Search on four of the six: date, event type, result and username. No search by project or document, and no choice of sort order (PA-41) |

**Table 36: AU-7(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | Developers |
| Enforced by | The audit page |
| Rules and procedures | Policy principle P4 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-1 (\<Procedures\> (AU)) |
| Tests | None separate: examined with A23 and A24 |
| Records an assessor will ask for | A demonstration of search and sort on each field |
| Status | Partially implemented |
| Risk decision | NC-AU-10, rated Low: remediate |
| Open items | PA-41: add search by project and document, and a choice of sort order |

### 5.12 AU-8 Time Stamps

**Table 37: AU-8 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Use the system's own clocks to make time stamps | Each record takes its time from the clock of the server that writes it. Both servers set their clocks from ABC Technologies' time service, \[ABC time source\], and stay within 1 second of UTC. Each month the Windows server administrator checks this, and reports any drift over 5 seconds to the security officer (PRO-AU-4) | The applications use the server clock. The servers are not built, and the time service is not evidenced (EV-AU-02, PA-102) |
| b | Record time to a defined precision, in UTC or with the offset from it | UTC, to the nearest second or finer | The applications record UTC (A22), stored to the microsecond |

**Table 38: AU-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Developers, ABC Technologies |
| Enforced by | The application, which records UTC; the Windows time service on each server, set by ABC Technologies |
| Rules and procedures | Policy rule R3 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-4 (\<Procedures\> (AU)) |
| Tests | Check A22 on the v1.0 code, 6 November 2026: passed, records are in UTC |
| Records an assessor will ask for | The servers' time settings; the monthly drift checks on TPL-8; ABC Technologies' time service configuration (EV-AU-02). None exist yet |
| Status | Partially implemented |
| Risk decision | NC-AU-11, rated Low: obtain evidence |
| Open items | PA-102: set and evidence time synchronisation on the servers (EV-AU-02) |

### 5.13 AU-9 Protection of Audit Information

**Table 39: AU-9 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Protect audit information and audit tools from unauthorised access, change and deletion | Section 4.5 sets it out. Only DV\_API writes records, through a database account that can add them but not change or delete them (D-AC-18). Only the auditor group opens the audit pages. Each record carries a keyed chain hash, with the key held outside the database, and the newest hash is copied each day to a store the applications cannot write to. Application logs are readable only by the Windows server administrators and the auditor. The archive is offline, and its hash is recorded. Rule B12 of \<Security Operating Procedures\> forbids anyone to alter, delete or disable audit records or logging | An ordinary user cannot open the audit pages (T71), and records are chained. But the application's database account can change, delete and empty the table (A26 to A28; PA-36). The chain has no key, so it can be rewritten, and the newest records can be removed without trace (A36; PA-73). Stored hashes cannot be recomputed (A37; PA-74). Ordinary users can add records (PA-29). The application log repeats usernames, IP addresses and session IDs (A38; PA-75) |
| b | Alert defined people when unauthorised access, change or deletion is detected | The chain check runs on a schedule and at each start-up. A break alerts the security officer and the auditor (detection use case U2), who preserve the evidence and raise an incident (PRO-AU-2) | Not built. The check exists in the code, but nothing runs it or alerts (PA-37), and until PA-73 and PA-74 are fixed it cannot be relied on |

**Table 40: AU-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | Developers, database administrator |
| Enforced by | Database permissions; the application's role check on the audit pages; the chain hash and its check; Windows file permissions on the logs |
| Rules and procedures | Policy principle P3; rules R4, R7 to R9 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-2, PRO-AU-7 (\<Procedures\> (AU)) |
| Tests | Checks A26 to A29 and A36 to A38 on the v1.0 code, 6 and 8 November 2026. A29 passed: each record holds a chain hash. The rest showed gaps: the application account could update, delete and empty the audit table (A26 to A28); the chain could be rewritten and cut short (A36); stored hashes did not recompute (A37); and the application log repeated audit details (A38) |
| Records an assessor will ask for | Database permissions on the audit table; chain check results; the daily copy of the newest hash; file permissions on the logs; any tampering alert and its incident record. None exist yet in the form designed |
| Status | Partially implemented |
| Risk decision | NC-AU-12, rated High: remediate; NC-AU-16, rated Medium: remediate (D-AU-06) |
| Open items | PA-36: give the API an account that can only add and read records. PA-37: run the chain check and alert. PA-73: key the chain hash. PA-74: make stored hashes recompute. PA-75: take audit details out of the application log. PA-29: stop ordinary users adding records |

### 5.14 AU-9(4) Access by Subset of Privileged Users

**Table 41: AU-9(4) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Allow only a defined few privileged users to manage audit logging | Table 10. Auditors read the records, and nobody can change them. Global administrators and administrators have no access to the audit pages, because their actions are what is reviewed. The auditor group, `DocViewer_Auditors`, is owned by the system owner, who alone adds members (PRO-AU-6). Logging settings change only through a release or a recorded change | An auditor can read the records and cannot manage users (A23, A24; T73, T74). But a global administrator can also read them (A25; PA-39) |

**Table 42: AU-9(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<DocuView\>: built into the system |
| Responsible | System owner, developers |
| Enforced by | The AD group `DocViewer_Auditors` and the application's `AuditorPolicy`; change control for logging settings |
| Rules and procedures | Policy principle P3; rule R4 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-6 (\<Procedures\> (AU)) |
| Tests | Checks A23 to A25 on the v1.0 code, 6 November 2026. A23 and A24 passed. A25 showed the gap: a global administrator can read the audit records. These checks ran on a build that used its own passwords and groups, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | The members of the auditor group, and the Jira requests behind them; the quarterly access review record; the test results. No members or reviews exist yet |
| Status | Partially implemented |
| Risk decision | NC-AU-13, rated Medium: remediate |
| Open items | PA-39: remove the global administrator from the audit pages |

### 5.15 AU-11 Audit Record Retention

**Table 43: AU-11 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Keep audit records for a defined time, to support investigation and meet legal and organisational needs | Audit records are kept 12 months in the database, then 12 months in an offline archive whose SHA-256 hash is recorded. After 24 months they may be deleted, only with the system owner's recorded approval. Application logs are kept for 30 days. The periods are those of \<DocuView\>'s retention schedule (\<Control Implementation Register\>, sections SI.7 and PT.4). Records held as evidence of an incident, or under a legal hold, are kept until the incident is closed or the legal adviser releases them (PRO-AU-4, PRO-AU-7) | Nothing removes or archives records, and there is no backup or capacity behind the rule yet (PA-42). Application logs are not yet controlled (PA-75) |

**Table 44: AU-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Database administrator |
| Enforced by | The database administrator's monthly archive step; backups of the database server |
| Rules and procedures | Policy principle P5; rule R2 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-4, PRO-AU-7 (\<Procedures\> (AU)) |
| Tests | None: there is nothing to test until the servers are built |
| Records an assessor will ask for | The archive files and their recorded hashes; approvals of any deletion; backup records. None exist yet |
| Status | Not implemented |
| Risk decision | NC-AU-14, rated Low: obtain evidence |
| Open items | PA-42: confirm storage and backups for 12 months online and 12 months archived |

### 5.16 AU-12 Audit Record Generation

**Table 45: AU-12 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Provide audit record generation, for the events the system can log, on defined components | Five components generate records: DV\_API, DV\_Web, DV\_Admin\_UI, PostgreSQL and Windows Server 2025 on both servers (section 4.2) | The three applications generate records (A15 to A18). PostgreSQL statement and connection logging are off (A30), and Windows is not built (PA-43) |
| b | Let defined people select which events each component logs | The system owner selects the events. Application events are set in code, so developers make a change through a release (PRO-AU-5). A release is reviewed, tested and recorded, so nobody can switch an event off quietly. PostgreSQL settings are changed by the database administrator, and the Windows audit policy by ABC Technologies' Group Policy, each through a recorded change | The system owner has selected the events (D-AU-P01). But no setting lets an event be turned on or off for a component: every change needs a release. The assessment found this a gap (statement AU-12b), and it is registered as PA-105 |
| c | Generate records for the selected events, with the content AU-3 requires | Every event in sections 4.2 and 4.3 writes a record with the content in Table 8 | Partly: the events in PA-14 and PA-76 write no record |

**Table 46: AU-12 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Developers, administrators |
| Enforced by | The audit service in each application; PostgreSQL and Windows logging settings |
| Rules and procedures | Policy rule R1 (\<Policy\>, sections AU.3 and AU.4); PRO-AU-5 (\<Procedures\> (AU)) |
| Tests | Checks A15 to A18 and A30 on the v1.0 code, 6 November 2026. A15 to A18 passed. A30 showed the gap: PostgreSQL logging is off. These checks ran on a build that used its own passwords and groups, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | Sample records from each of the five components; the PostgreSQL logging settings; the Windows audit policy (EV-AU-04). Application samples exist only from the test environment |
| Status | Partially implemented |
| Risk decision | NC-AU-15, rated Medium: remediate; NC-AU-17, rated Low: remediate (system owner, Low) |
| Open items | PA-14, PA-76: log the missing events. PA-43: set database logging, and collect Windows logs. PA-105: the system owner recommends that selection by release is accepted, as the events change rarely and a release is reviewed, tested and recorded (D-AU-12). The decision is the authorising official's. If it is not accepted, a setting is added |

| **APPENDIX A** |
| --- |

## Appendix A How logging was built in the tested build

This records what the code labelled v1.0 did when it was examined and tested in Docker between 5 and 9 November 2026. It is the basis of the Today columns. That build signed in with its own passwords, and each application connected to the database itself.

**Table 47: How logging was built in the tested build**

| Part | What happens today | Where |
| --- | --- | --- |
| Writing a record | Each application writes to the table `dbo.AuditLog` in the \<DocuView\> database, and also to its application log | `AuditService.cs` in DV\_API, DV\_Web and DV\_Admin\_UI |
| Record content | Event type, action, username, user ID, project, document, result, details, IP address, browser, session, time, duration and source component | `DV_Shared/Security/AuditLog.cs` |
| Chain hash | Each record holds a SHA-256 hash of its fields and the previous record's hash, with no secret key. Anyone who can write to the table can recalculate the chain, and removing the newest records leaves it intact (A36). The time stamp is hashed to 100 nanoseconds but stored to the microsecond, so most stored hashes cannot be recomputed (A37). The chain therefore detects neither deliberate tampering nor, as built, accidental damage | AuditService.cs; A29, A36, A37; PA-73, PA-74 |
| Chain check | VerifyAuditChainIntegrityAsync exists, but nothing calls it. Until PA-74 is fixed it would report a break at almost every record | PA-37, PA-74 |
| Failure | A failed write goes to the application log as critical, and the user's action carries on | A31, A32 |
| Application log | Every audit event is also written to the application log at Information level as two "AUDIT DEBUG" lines, with the username, IP address and session ID, and a failed write logs its details at Critical. Until PA-75 is fixed, the application log is audit information: administrators and auditors only, kept 30 days (PRO-AU-7) | AuditService.cs; A38; PA-75 |
| Reading | The page `/sysadmin/audit-logs` filters by date, event type, result and username. There is no export or choice of sort order | A23 to A25; PA-41 |
| Protection | The application's database account can read, change, delete and empty the table, and there are no triggers | A26 to A28; PA-36 |
| Retention | Nothing removes records, and no retention setting or capacity plan exists | PA-42 |
| Database and server logs | PostgreSQL statement logging is off. Windows logs have not been examined, as the VMs are not built | A30; PA-43 |

| **APPENDIX B** |
| --- |

## Appendix B Parameter register

These are NIST's organisation-defined values for the 16 AU entries: 28 in total. State now says whether the tested build met each value, from the checks of 8 November 2026 and the Level 1 assessment. The values were agreed by the system owner on 5, 6 and 8 November 2026 (D-AU-P01, D-AU-P02).

**Table 48: AU parameter register**

| NIST identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| AU-01\_ODP\[01\] | Who receives the policy | Everyone who administers or reviews \<DocuView\> | Not yet: shared once version \<ver\> is approved (PA-20) |
| AU-01\_ODP\[02\] | Who receives the procedures | Everyone who administers or reviews \<DocuView\> | Not yet: shared once version \<ver\> is approved (PA-20) |
| AU-01\_ODP\[03\] | Level of the policy | System level | Met |
| AU-01\_ODP\[04\] | Official who manages them | System owner | Met |
| AU-01\_ODP\[05\] | Policy review frequency | Every 12 months | Met: set; first review due November 2027 |
| AU-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: this review is one |
| AU-01\_ODP\[07\] | Procedures review frequency | Every 12 months | Met: set |
| AU-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: set |
| AU-02\_ODP\[01\] | Event types the system can log | The event types in `AuditEventTypes` in `DV_Shared/Security/AuditLog.cs` | Met |
| AU-02\_ODP\[02\] | Event types selected for logging | Sections 4.2 and 4.3 | Partly: account, group and role changes and the PA-76 events are not logged; PostgreSQL and Windows not set (PA-14, PA-43, PA-76) |
| AU-02\_ODP\[03\] | How often they are logged | Every occurrence | Met for the events that are logged |
| AU-02\_ODP\[04\] | Review of selected events | Every 12 months | Met: set |
| AU-03(01)\_ODP | Additional record content | Session reference (a hash of the session ID, never the ID itself), browser, project and document | Met for the four fields (A20, A21); the form of the session reference is not yet checked (PA-104) |
| AU-04\_ODP | Retention requirement for capacity | 24 months: 12 months online and 12 months archived | Not assessable: VMs not built (PA-42) |
| AU-05\_ODP\[01\] | Who is alerted to a logging failure | Windows server administrator and security officer | Not met: no alert route (A35, PA-38) |
| AU-05\_ODP\[02\] | Time to alert | Within 1 hour | Not met (PA-38) |
| AU-05\_ODP\[03\] | Additional actions | Investigate and restore; the system keeps running | Met: the system keeps running (A32) |
| AU-06\_ODP\[01\] | Review frequency | Weekly | Not yet: review starts at go-live (PA-40) |
| AU-06\_ODP\[02\] | Activity to look for | The list in \<Security Operating Procedures\>, section 5.2 | Met |
| AU-06\_ODP\[03\] | Who receives findings | Security officer and system owner | Met: set |
| AU-06(01)\_ODP | Automated mechanisms | The admin portal's audit page, plus ABC Technologies' central monitoring if confirmed (D-AU-07) | Partly: audit page only (PA-40) |
| AU-07(01)\_ODP | Fields to search and sort | Date, event type, result, username, project and document | Partly: four of six fields, no sort choice (PA-41) |
| AU-08\_ODP | Time stamp granularity | To the nearest second, in UTC. Clocks synchronised from ABC Technologies' time source, \[ABC time source\], within 1 second of UTC; drift over 5 seconds reported | Partly: the applications use UTC (A22); VMs not built (EV-AU-02) |
| AU-09\_ODP | Who is alerted to tampering | Security officer and auditor | Not met: nothing runs the chain check or alerts, and the chain cannot yet detect tampering (A36, A37; PA-37, PA-73, PA-74) |
| AU-09(04)\_ODP | Who manages audit logging | Auditors read records; nobody can change them; global administrators have no access | Not met: global administrators can read records (A25) and the application account can change them (A26 to A28) |
| AU-11\_ODP | Retention period | 12 months online, then 12 months in an offline archive; application logs 30 days | Not assessable: VMs not built (PA-42); application logs not yet controlled (PA-75) |
| AU-12\_ODP\[01\] | Components generating records | DV\_API, DV\_Web, DV\_Admin\_UI, Windows Server and PostgreSQL | Partly: the applications log; PostgreSQL logging is off and Windows is not assessed (A30, PA-43) |
| AU-12\_ODP\[02\] | Who selects logged events | System owner | Met |

| **APPENDIX C** |
| --- |

## Appendix C Server logging settings

These are the settings for PostgreSQL on the database server, so that it logs the events in Table 6 with the content AU-3 requires. The system owner adopted them as the design on 12 November 2026 (D-AU-12). The database administrator applies them at build and records any value that has to differ, with the reason. None is applied yet (PA-43). The Windows audit policy is ABC Technologies' Group Policy, and its settings are asked for under EV-AU-04.

**Table 49: PostgreSQL logging settings**

| Setting | Value | What it gives |
| --- | --- | --- |
| `logging_collector` | `on` | Log files on the database server |
| `log_connections`, `log_disconnections` | `on` | Every connection and its end; failed connections are logged as errors |
| `log_line_prefix` | `%m [%p] %u@%d %h %a ` | On every line: time to the millisecond, process, user, database, client address and application |
| `log_timezone` | `UTC` | Times that line up with the audit log |
| `log_statement` | `ddl` | Every change to a table, role or permission |
| `log_min_error_statement` | `error` | The statement behind any refused or failed action |
| An audit extension, such as pgAudit, with role and DDL classes, and object logging on `dbo.AuditLog` | \[to be confirmed with ABC Technologies\] | Every read, change or deletion of audit records made outside the API |
| Log file permissions | Readable by the database administrator and the PostgreSQL service account only | Protection as audit information (AU-9) |
| Log retention on the server | \[to be set at build\], then forwarded or archived | Kept as the Windows logs are |

Changing any of these is itself a change to logging: it is made through a recorded change (\<Configuration Management Plan\>), and PostgreSQL logs the reload.

| **APPENDIX D** |
| --- |

## Appendix D The rest of NIST's catalogue

### D.1 Logging that other controls require

NIST's guidance on AU-2 points out that other controls ask for particular events to be logged. Table 50 shows where each of those in the Moderate baseline is met.

**Table 50: Logging required by other controls**

| Control | What it asks to be logged | Met by |
| --- | --- | --- |
| AC-2(4) Automated Audit Actions | Creating, changing, enabling, disabling and removing accounts | Active Directory, for accounts and group members (EV-AU-05). \<DocuView\>'s audit log, for projects and the groups each uses |
| AC-6(9) Log Use of Privileged Functions | Each use of a privileged function | The privileged functions row of Table 7 |
| AC-17(1) Monitoring and Control | Remote access sessions | ABC Technologies' VPN and gateway logs (EV-AC-08 to EV-AC-11) |
| CM-3, CM-5 Change Control and Access Restrictions | Changes to the system, and who made them | The change record in Jira; Windows events for installed services and policy changes; PostgreSQL logging of schema changes |
| MA-4 Nonlocal Maintenance | Remote maintenance sessions | Windows sign-in events on the servers; ABC Technologies' record of the administration route |
| PE-3 Physical Access Control | Entry to the rooms that hold the servers | ABC Technologies' physical access logs, inherited (\<Control Implementation Register\> (PE)) |
| SI-4 System Monitoring | Events that show an attack or misuse | The detection use cases U1 to U8 (\<Control Implementation Register\>, section SI.5) |
| PM-21 Accounting of Disclosures | Disclosures of personal data | The export and download records of Table 7 |

### D.2 AU controls outside the Moderate baseline

NIST does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 51 says where.

**Table 51: AU controls not selected at Moderate**

| Control | What it adds | \<DocuView\>'s position |
| --- | --- | --- |
| AU-5(1) Storage Capacity Warning | A warning before audit storage fills | Not required. The monthly capacity check stands in for it |
| AU-5(2) Real-time Alerts | Alerts at once for defined failures | Not required. The design alerts within 1 hour |
| AU-6(5), AU-6(6) Integrated Analysis; Correlation with Physical Monitoring | Joining audit review with scanning, performance and physical access data | Not required, and not done |
| AU-8(1) Synchronisation with an Authoritative Time Source | Withdrawn in Revision 5; now SC-45(1) | Not required. Done anyway: both servers within 1 second of UTC (section 4.6) |
| AU-9(2) Store on Separate Physical Systems | Audit records kept on a different system from the one audited | Not required. Done in part: the newest chain hash is copied daily to a separate store, and the archive is offline |
| AU-9(3) Cryptographic Protection | Cryptography to protect the integrity of audit information | Not required. Done in design: the keyed chain hash (section 4.5). Not yet built (PA-73, PA-74) |
| AU-10 Non-repudiation | Proof that a person carried out an action | Not required at Moderate. Records name the person AD FS authenticated |
| AU-12(1), AU-12(3) System-wide Audit Trail; Changes by Authorised Individuals | One time-ordered trail across components; changing what is logged at run time | Not required. The weekly comparison by time stands in for the first. The second relates to PA-105 |
| AU-13, AU-14, AU-16 Monitoring for Disclosure; Session Audit; Cross-organisational Logging | Further capabilities | In no baseline. Not done |
| AU-3(3) Limit Personally Identifiable Information Elements | Only the personal data needed in records | In the privacy baseline. Assessed with the PT family; design in section 4.4 |
