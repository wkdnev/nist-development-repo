# \<System Name\> Audit and Accountability Management

## 1 Purpose

This document sets out how \<System Name\> is designed and configured to meet the 16 Audit and Accountability (AU) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: where audit records come from, which events are logged and why, what a record holds, how records are stored and protected, time, retention and capacity, review, analysis and reporting, failures and alerts, the application logs, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet. Appendix A gives the logging settings for the database server, and Appendix B shows the logging that other controls require and the AU controls CSS does not select at Moderate. The design follows the good practice in CSS.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.3 (Table 12). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (AU). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (AU), and the steps people follow are in \<Procedures\> (AU) and \<Security Operating Procedures\>, section 4.2.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. The settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

Where section 3 notes what "today" is, it means the tested v1.0 build, and the position of the servers, which are not yet built. That build signed in with its own passwords and held sessions of its own. \<System Name\> signs in through \<Organisation\>'s PingFederate (D-AC-23), so the tests are to be repeated on that build (PA-95).

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.3 (Table 12).

## 3 The audit design

### 3.1 Principles

Controls met here: AU-2, AU-3, AU-6, AU-9, AU-11, AU-12.

1. **Complete.** The agreed events are recorded every time they occur.
2. **Attributable.** Each record shows what happened, when, where, from where, the outcome and who was involved. The person is the one PingFederate authenticated.
3. **Protected.** Nobody can change or delete a record. Only auditors read them.
4. **Reviewed.** Records are examined every week by someone who does not administer the system.
5. **Retained.** Records are kept for 24 months: long enough to investigate an incident found late.
6. **No secrets.** Records never hold a password, key, token or authentication cookie, and hold only the personal data an investigation needs.
7. **One audit log.** \<System Name\> has one application audit log, written only by the API, as the system owner confirmed on 12 November 2026 (D-AU-11). Any other log that repeats its content is protected as audit information.

These carry out the principles and rules of \<Policy\>, sections AU.3 and AU.4.

### 3.2 Where audit records come from

Controls met here: AU-2, AU-12.

An investigation must be able to follow an action from the network to the database. So records come from six sources. \<System Name\>'s team controls the first three. \<Organisation\> controls the rest, as part of its corporate configuration (D-AC-21, D-AC-23).

![Figure 1: Where audit records come from, and who reads them](figures/aum-figure-1.png)

**Figure 1: Where audit records come from, and who reads them**

**Table 1: Sources of audit records**

| Source | Events to log | Held in | Set by | Today |
| --- | --- | --- | --- | --- |
| UI application, Admin application and API | The events in Table 2 | The audit log: the audit log table in the \<System Name\> database | The system owner, in Table 2; built by \<System Name\>'s developers through a release | Partly logged (Table 2) |
| The three applications' own logs | Errors, start-up and shut-down, and logging failures. No audit details | Log files on the application server, kept 30 days | \<System Name\>'s developers | They also repeat usernames, IP addresses and the tested build's session IDs (A38, PA-75) |
| PostgreSQL | Connections and failed connections; role and permission changes; schema changes; any change to or deletion of audit records; changes to logging settings | The PostgreSQL log on the database server | Database administrator | Statement and connection logging are off (A30, PA-43) |
| Windows Server 2025, both servers | Sign-ins and failed sign-ins (events 4624, 4625); account and group changes (4720, 4722 to 4726, 4728, 4732, 4756); use of special privileges (4672); audit policy changes (4719); security log cleared (1102); services installed (7045); system time changed (4616) | The Windows Security and System logs on each server, forwarded to \<Organisation\>'s central monitoring if confirmed (D-AU-07) | \<Organisation\>'s Group Policy. \<System Name\> states the events it needs (EV-AU-04) | Not assessable: the servers are not built (PA-43) |
| PingFederate and Active Directory | Every sign-in attempt, failed sign-in, lockout and second-factor result for \<System Name\>; every change to an account; every change to the members of \<System Name\>'s groups | \<Organisation\>'s own logs | \<Organisation\> | Not evidenced. No arrangement yet gives \<System Name\>'s auditor these records (PA-101, EV-AU-05) |
| \<Organisation\>'s network services | Firewall and VPN events, and the time service | \<Organisation\>'s central monitoring | \<Organisation\> | Inherited; to be confirmed (D-AU-07, EV-AU-01) |

Each source logs at every occurrence. The system owner selects the events, reviews the list every 12 months and on any change, and records the decision in \<Decision Register\> (PRO-AU-5).

### 3.3 Application events

Controls met here: AU-2, AU-12.

Table 2 lists every event type \<System Name\>'s applications log, the actions recorded under each, and what an investigator learns from it. That is the reason each is selected (AU-2, part d). Together they answer who signed in, what they saw or changed, what they were refused, who changed access or settings, and when nothing could be logged.

**Table 2: Application events logged**

| Event type | Actions recorded | What is covered | Why it is needed to investigate an incident | Logged today? |
| --- | --- | --- | --- | --- |
| Sign-in | Sign-in accepted; sign-in response from PingFederate refused | Sign-ins. \<System Name\> records each sign-in it accepts and each sign-in response it refuses. Failed passwords and second factors are recorded by PingFederate (Table 1) | Shows who entered the system, and any attempt to enter without the right | Yes, in the tested build, for its own sign-in and failed sign-in (A15, A16). To be repeated with PingFederate (PA-95) |
| Access refusal at sign-in | Request refused because the authentication cookie has expired or is not valid; request refused because the person's account is disabled or their groups cannot be read from Active Directory | Requests refused at the sign-in and group checks. \<System Name\> has no sessions of its own, so it logs no session start, end or time-out | Shows when a person's access ended or was refused, and links activity to one sign-in | Not tested. The tested build held sessions of its own, which the design does not have |
| Project and group administration | Project created, changed or removed; a project's read or edit group changed; a role mapping changed | Changes to projects, to the AD groups each project uses, and to role mappings | Shows who was given a route to information, and by whom. Changes to the members of a group are recorded by Active Directory (Table 1) | Partly: most changes in the admin portal are not logged (PA-14) |
| Access decision | Access to a page or function refused; access to a project refused; unauthorised attempt | Denied access | Shows attempts to reach restricted information | Yes (A18) |
| Document access; Export | Document viewed; document downloaded; document details viewed; documents searched; documents exported | Document views, downloads, exports and searches | Shows who saw which information | Yes (A17) |
| Data change | Document uploaded; document corrected; document deleted | Document corrections and deletions | Shows who changed or removed a record about a person | No (PA-89) |
| Privileged function | Maintenance page used; cache cleared; database maintenance run; a global administrator opens a project by right of the role | Use of privileged functions: the maintenance pages, cache management and database maintenance (\<Access Control Management\>, section 3.8) | Shows what each administrator did with their extra rights (AC-6(9)) | Partly: the maintenance pages are not logged (PA-31) |
| Configuration change | A security setting changed | Configuration changes | Shows changes to security settings | Not confirmed by any test (PA-103) |
| Audit | Audit log read; audit log searched or exported | Reading or searching the audit log | Shows who looked at audit records, which AU-9 protects | No (PA-76) |
| System | Application started; application stopped | Start-up and shut-down of each application | Shows periods when nothing could be logged | No (PA-76) |
| Audit | Logging setting changed; chain check passed; chain check failed | Changes to logging, and audit chain check results | Shows attempts to stop or hide logging | No (PA-76) |
| Logging failure | An audit record could not be written | Logging failures | Shows periods without records | Application log only (A31, PA-38) |
| Security event | Suspicious activity; a breach of a security rule | Events the applications judge to be an attack or misuse, such as a forged request | Shows attempts to defeat the controls | Not confirmed by any test (PA-103) |
| Faulty document report | A user reports a document or page as faulty | Reports made from the viewer | Shows who reported what, as these reports name documents | Not confirmed by any test (PA-103) |

This table is the full list of event types and actions that \<System Name\>'s applications must be able to log (AU-2, part a). It is the design: a release may add to it only after the system owner has changed this table (PRO-AU-5). Application events are built into each release, so developers make any change to them through a release. A release is reviewed, tested and recorded, so nobody can switch an event off quietly.

\<System Name\> holds no passwords, so it logs no password change or reset (D-AC-23). Those are recorded in Active Directory.

### 3.4 What a record holds

Controls met here: AU-3, AU-3(1), AU-3(3), AU-8, AU-9, AU-12.

Every application record has the same fields, in one record format that all three applications use. Every event in sections 3.2 and 3.3 writes a record with this content. Table 3 shows which part of AU-3 each meets.

**Table 3: Audit record content**

| Field | Holds | Meets |
| --- | --- | --- |
| Event type, Action | What happened | AU-3, part a |
| Time | When, in UTC | AU-3, part b; AU-8 |
| Source component | Which application raised the event | AU-3, part c |
| IP address, Browser | Where the person came from | AU-3, part d; AU-3(1) |
| Result | Success, failure or refused | AU-3, part e |
| Username, User ID | Who acted: the person PingFederate authenticated | AU-3, part f |
| Project, Document | What was acted on | AU-3, part f; AU-3(1) |
| Sign-in | A reference that links the record to one sign-in: a SHA-256 hash of the sign-in identifier in the authentication cookie, never the identifier itself, so that the record cannot be used to take over a sign-in (rule R8; D-AU-11) | AU-3(1) |
| Details, Duration | Free text for the event, and how long it took | Supports investigation |
| Chain hash | A value calculated from the record and the one before it | AU-9 |

**Records from the servers.** PostgreSQL and Windows records must hold the same six kinds of content. Windows events do so by design. PostgreSQL does so once its log line is set to carry the time, the user, the database and the client address (appendix A). Neither has been examined, as the servers are not built (PA-43).

**Limits on content (rule R8; AU-3(3)).** A record never holds a password, key or token. It holds only the personal data an investigation needs: the named fields above. The free text holds no further personal data (check Q04), and is to be reviewed again (PA-71).

### 3.5 How records are stored and protected

Controls met here: AU-9, AU-9(4).

**Table 4: Where audit information is held, and who can reach it**

| Store | Written by | Read by | Changed or deleted by | Today |
| --- | --- | --- | --- | --- |
| The audit log | API only, through its database service account, which can add records and nothing more (D-AC-18). UI application and Admin application send their events to the API, which accepts them only from those two applications and never from a user's browser (D-AU-11) | The auditor group, through the admin portal's audit pages. The database administrator can reach the table to archive it, under rule B12 | Nobody | Each application writes to the table itself. The application account can change, delete and empty it (A26 to A28; PA-36). A global administrator can read the pages (A25; PA-39). Ordinary users can add records (PA-29) |
| The offline archive, held at \[archive location, to be agreed with \<Organisation\> with its storage (EV-AU-03)\], encrypted, and off the database server | The database administrator, each month, for records older than 12 months | The auditor, on request to the system owner | Nobody, until 24 months; then only with the system owner's recorded approval | No archive exists (PA-42) |
| The newest chain hash, copied daily | A scheduled job | The auditor and security officer | Not by the applications or their accounts | Not built (PA-73) |
| Application logs | Each application's Windows service account | The Windows server administrators and the auditor | Removed after 30 days | In the test environment they are not limited (PA-75) |
| PostgreSQL log | PostgreSQL | The database administrator and the auditor | Not by the API's account | Logging is off (PA-43) |
| Windows logs | Windows | The Windows server administrators; the auditor through \<Organisation\>'s report or monitoring | Clearing the log is itself logged (event 1102) | Not built |

**The chain hash.** Each record holds a hash of its own fields and the previous record's hash, so a changed or removed record breaks the chain. The design uses a keyed hash, HMAC-SHA-256, with the key held outside the database where the applications' accounts cannot read it (key K11 in \<System and Communications Protection Management\>, section 3.4). The newest hash is copied each day to a store the applications cannot write to, so that removing the newest records is also revealed. The time is rounded to the microsecond before hashing, so that a stored hash can be recomputed. The key is listed in the key register (\<System and Communications Protection Management\>, section 3.4).

**The chain check.** The check runs on a schedule and at each start-up (PRO-AU-2, PRO-SI-6). A break alerts the security officer and the auditor (detection use case U2), who preserve the evidence before anything is changed and raise an incident.

**Table 5: Who may manage audit logging**

| Function | Who | How it is limited |
| --- | --- | --- |
| Read and search audit records | Auditors | AD group DocViewer\_Auditors, the only group that opens the audit pages. It is owned by the system owner, who alone adds members. An auditor holds no administration role (PRO-AU-6) |
| Change or delete an audit record | Nobody | The database account cannot; rule B12 forbids it |
| Select which application events are logged | System owner | Decided on the record; made by developers through a release (PRO-AU-5) |
| Change PostgreSQL logging settings | Database administrator | A recorded change (\<Configuration Management\>) |
| Change the Windows audit policy | \<Organisation\> | Its Group Policy and change process |
| Archive records, and delete them after 24 months | Database administrator | Deletion only with the system owner's recorded approval (PRO-AU-4) |
| Run the chain check and receive its alerts | Auditor and security officer | PRO-AU-2 |

Global administrators and administrators have none of these functions. They are the people whose actions the auditor reviews (\<Access Control Management\>, section 3.5). Rule B12 of \<Security Operating Procedures\> forbids anyone to alter, delete or disable audit records or logging.

### 3.6 Time

Controls met here: AU-6(3), AU-8.

1. Each record takes its time from the clock of the server that writes it. Every record's time is in UTC, to the nearest second or finer.
2. Each server takes its time from \<Organisation\>'s time service, \[Organisation time source\], and stays within 1 second of UTC.
3. Each month the Windows server administrator checks both servers, records the result on TPL-8, and reports any drift over 5 seconds to the security officer (PRO-AU-4).
4. A change to a server's clock is itself a Windows event (4616).

One time source across the applications, the servers, PingFederate and the network is what lets the auditor line records up from different stores (AU-6(3)).

CSS no longer asks for clock synchronisation under AU-8. In Revision 5 it moved to SC-45(1), which is not in the Moderate baseline. \<System Name\> keeps the rule of 1 second anyway, because the weekly comparison across stores depends on it.

### 3.7 Retention and capacity

Controls met here: AU-4, AU-11.

**Table 6: Retention**

| Information | Kept | Then |
| --- | --- | --- |
| Audit records | 12 months in the database | Moved to the offline archive, and the archive's SHA-256 hash recorded on TPL-8 |
| Archived audit records | A further 12 months | May be deleted, only with the system owner's recorded approval |
| Application logs | 30 days | Deleted |
| Records held as incident evidence | Until the incident is closed | As the incident record says (\<Incident Response Management\>) |
| Records under a legal hold: a claim, a tribunal, a regulator's enquiry or a person's request for their data | Until the legal adviser releases them | The legal adviser tells the system owner and the database administrator, who mark the records so that they are not deleted (PRO-AU-4). The system owner adopted this rule on 12 November 2026 (D-AU-12); the legal adviser confirms its wording at the next review of the policy |
| Backup copies of the database, which include the audit log | As the backup schedule: 14 daily, 8 weekly and 12 monthly copies | Encrypted, and protected as audit information (\<Contingency Planning Management\>) |
| Windows, PingFederate and Active Directory logs | As \<Organisation\> sets; 12 months is expected | \<Organisation\>'s process (EV-AU-04, EV-AU-05) |

Storage is sized for the full 24 months: 12 months in the database, and the same again for the archive. The size is the number of records each day, \[records per day, to be measured\], times the average size of a record, \[bytes per record, to be measured\], times 365 days, plus half as much again for growth. Both figures are measured in the test environment before the request goes to \<Organisation\>, and again in the first month of use (D-AU-11). The database administrator checks free space and the size of the audit table each month, and asks for more before records are at risk (PRO-AU-4). The audit log is backed up with the database (\<Contingency Planning Management\>).

The periods are those of \<System Name\>'s retention schedule (\<System and Information Integrity Management\>, section 3.7, and \<PII Processing Management\>, section 3.7). The database administrator archives records each month, and applies the rules for incident evidence and legal holds (PRO-AU-4, PRO-AU-7).

### 3.8 Review, analysis and reporting

Controls met here: AU-6, AU-6(1), AU-6(3), AU-7, AU-7(1).

1. **Weekly review.** The auditor reviews the records since the last review, following \<Security Operating Procedures\>, section 4.2, which lists the unusual activity to look for (PRO-AU-1; duty C3). The auditor judges what each finding could lead to. The auditor holds no administration role, so nobody reviews their own actions.
2. **Across stores.** The auditor compares the application records with the PostgreSQL and Windows logs and \<Organisation\>'s record of sign-ins and group changes, lining them up by UTC time and username. This is done by hand, which is proportionate for one system, which the system owner has accepted to 6 November 2027 (NC-AU-08).
3. **Against requests.** Every change to access is checked against its approved ServiceNow request (\<Access Control Management\>, section 3.13).
4. **Report.** Findings go to the security officer and system owner on TPL-8, with the date, the period covered, the reviewer and the result. Anything unexplained is raised as a security incident.
5. **More review when risk rises.** After an incident or new threat information, the system owner sets a more frequent or closer review (PRO-AU-1, step 5).
6. **A second look at the most powerful.** The Head of Cyber checks the global administrators' actions (\<Security Operating Procedures\>, duty C16).
7. **Automated support.** Two means join up review, analysis and reporting. The admin portal's audit page filters and summarises the records for the auditor. \<Organisation\>'s central monitoring, if it is confirmed to take \<System Name\>'s logs, raises the alerts in the detection use cases U1 to U8 (\<System and Information Integrity Management\>, section 3.4).
8. **Reports and exports.** The audit page, open only to the auditor group, filters the records and shows a summary. An export gives the auditor the filtered records as a file, for a report or an investigation. Records are always shown with their stored time.

**Table 7: Search and sort on the audit page**

| Field | Design | Today |
| --- | --- | --- |
| Date | Search and sort | Search |
| Event type | Search and sort | Search |
| Result | Search and sort | Search |
| Username | Search and sort | Search |
| Project | Search and sort | Neither (PA-41) |
| Document | Search and sort | Neither (PA-41) |
| Export of the filtered records | Yes | No (PA-41) |

The page only reads. It cannot change a record or its order, and an export is a copy.

### 3.9 Failures and alerts

Controls met here: AU-5, AU-6(1), AU-9.

**Table 8: Alerts**

| Event | Alert to | Within | Then | Today |
| --- | --- | --- | --- | --- |
| A logging failure: an audit record cannot be written | Windows server administrator, security officer | 1 hour | \<System Name\> keeps running, so that a logging fault cannot stop the service. Logging is restored, and the period without records is recorded (PRO-AU-3) | Application log only; nobody is told (PA-38) |
| A break in the audit chain, or other sign of tampering | Security officer, auditor | At once | Evidence is preserved, and an incident is raised (PRO-AU-2) | Nothing runs the check (PA-37) |
| A server clock more than 5 seconds from UTC | Security officer | At the monthly check | The Windows server administrator corrects it with \<Organisation\> | Not built |
| Audit storage running low | Database administrator | At the monthly check | More storage is raised before records are at risk (PRO-AU-4) | Not built |

The logging failure alert goes through \<Organisation\>'s central monitoring if that is confirmed; otherwise by \[alert route to be set at build\], which must not depend on \<System Name\> itself being healthy.

\<System Name\> keeps running when logging fails. The system owner chose this (D-AU-11): staff must still be able to reach HR records, a stop would let a logging fault take the whole service down, and the failure is alerted within 1 hour and the gap recorded. The Windows server and database administrators find the cause and restore logging. The security officer records the period with no records and tells the system owner. If records may be lost or changed, the evidence is preserved first (PRO-AU-3).

A full disk is a logging failure like any other: if the audit log cannot be written because storage has run out, the first alert in Table 8 applies. The CSS separate warning before storage fills, AU-5(1), is not in the Moderate baseline; the monthly check stands in for it.

Alerts are raised by the detection use cases in \<System and Information Integrity Management\>, section 3.4, of which U2 and U7 concern audit. None is built yet (PA-59).

### 3.10 The application logs

Controls met here: AU-9, AU-11.

Each application also keeps its own log of errors, start-up and shut-down. In the tested build that log repeats every audit event, with the username, IP address and the tested build's session ID (A38). Until that is fixed (PA-75), an interim rule applies, approved by the authorising official (D-AU-06):

1. The application logs are audit information. Only the Windows server administrators and the auditor may read them.
2. They are kept for 30 days and then deleted.
3. They are not copied off the servers, except as incident evidence.
4. Each month the Windows server administrator checks who can read them and how old they are (PRO-AU-7).

Once PA-75 is fixed, the application logs hold no audit details, personal data or sign-in identifiers.

### 3.11 What \<Organisation\> provides

Controls met here: AU-2, AU-4, AU-5, AU-6, AU-6(1), AU-6(3), AU-8, AU-11, AU-12.

\<Organisation\> sets these as part of its corporate configuration. The \<System Name\> team has no control over them (D-AC-21, D-AC-23). \<System Name\> states what it relies on, and asks for the evidence. What is expected below is the system owner's understanding, not evidence.

**Table 9: Provided by \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Expected, not confirmed | Evidence asked |
| --- | --- | --- | --- | --- |
| Central log monitoring | AU-6(1), AU-6(3), AU-5 | It takes the Windows and PostgreSQL logs, and \<System Name\>'s alerts, and tells the security officer | A central service takes the Windows and PostgreSQL logs. Open (D-AU-07) | EV-AU-01 |
| Time service | AU-8 | Both servers stay within 1 second of UTC | The domain controllers provide time | EV-AU-02 |
| Storage and backup | AU-4, AU-11 | Room for 12 months of records online, backed up daily, and somewhere to hold the offline archive | Storage is sized for 12 months, with daily backups | EV-AU-03 |
| Windows audit policy | AU-2, AU-12 | The Windows events in Table 1 are logged on both servers and kept | Group Policy sets the audit policy, and logs are kept for 12 months | EV-AU-04 |
| PingFederate and Active Directory audit | AU-2, AU-6, AU-6(3), AU-12 | Every sign-in attempt for \<System Name\>, and every change to \<System Name\>'s groups and their members, is recorded, kept for at least 12 months, and sent to \<System Name\>'s auditor as a weekly report, by \[route to be agreed with \<Organisation\>\]. Read access for the auditor would also meet this (D-AU-11) | Not yet asked | EV-AU-05 |

The system owner agrees two things with \<Organisation\>'s security contact, and records them: which logs \<Organisation\>'s monitoring needs from \<System Name\> and its servers; and which of \<Organisation\>'s own records, of PingFederate, Active Directory, the network and the VPN, \<System Name\>'s auditor receives. The five requests, EV-AU-01 to EV-AU-05, are sent together, and central monitoring (D-AU-07) is to be settled with \<Organisation\>'s security contact before the servers are built (D-AU-11).

**Today:** no request has been sent, and none of this is evidenced.

### 3.12 Policy and procedures

Controls met here: AU-1.

1. **Policy.** \<Policy\> (AU) is a system-level policy. Its purpose and scope are in section AU.1, responsibilities in AU.5, and commitment, coordination and compliance in AU.6. It is shared with everyone who administers or reviews \<System Name\>. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (AU) holds seven procedures, PRO-AU-1 to PRO-AU-7, each naming who acts, how often and the record. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control, and each review is recorded in the change record.

## Appendix A Server logging settings

These are the settings for PostgreSQL on the database server, so that it logs the events in Table 1 with the content AU-3 requires. The system owner adopted them as the design on 12 November 2026 (D-AU-12). The database administrator applies them at build and records any value that has to differ, with the reason. None is applied yet (PA-43). The Windows audit policy is \<Organisation\>'s Group Policy, and its settings are asked for under EV-AU-04.

**Table 10: PostgreSQL logging settings**

| Setting | Value | What it gives |
| --- | --- | --- |
| Log collection | On | Log files on the database server |
| Connection and disconnection logging | On | Every connection and its end; failed connections are logged as errors |
| Line prefix | Time, process, user, database, client address and application | On every line: time to the millisecond, process, user, database, client address and application |
| Log time zone | UTC | Times that line up with the audit log |
| Statement logging | Definition changes | Every change to a table, role or permission |
| Statements logged on error | Errors and above | The statement behind any refused or failed action |
| An audit extension, such as pgAudit, with role and DDL classes, and object logging on the audit log table | \[to be confirmed with \<Organisation\>\] | Every read, change or deletion of audit records made outside the API |
| Log file permissions | Readable by the database administrator and the PostgreSQL service account only | Protection as audit information (AU-9) |
| Log retention on the server | \[to be set at build\], then forwarded or archived | Kept as the Windows logs are |

Changing any of these is itself a change to logging: it is made through a recorded change (\<Configuration Management\>), and PostgreSQL logs the reload.

## Appendix B The rest of the CSS catalogue

### B.1 Logging that other controls require

The CSS guidance on AU-2 points out that other controls ask for particular events to be logged. Table 11 shows where each of those in the Moderate baseline is met.

**Table 11: Logging required by other controls**

| Control | What it asks to be logged | Met by |
| --- | --- | --- |
| AC-2(4) Automated Audit Actions | Creating, changing, enabling, disabling and removing accounts | Active Directory, for accounts and group members (EV-AU-05). \<System Name\>'s audit log, for projects and the groups each uses |
| AC-6(9) Log Use of Privileged Functions | Each use of a privileged function | The privileged functions row of Table 2 |
| AC-17(1) Monitoring and Control | Remote access sessions | \<Organisation\>'s VPN and gateway logs (EV-AC-08 to EV-AC-11) |
| CM-3, CM-5 Change Control and Access Restrictions | Changes to the system, and who made them | The change record in ServiceNow; Windows events for installed services and policy changes; PostgreSQL logging of schema changes |
| MA-4 Nonlocal Maintenance | Remote maintenance sessions | Windows sign-in events on the servers; \<Organisation\>'s record of the administration route |
| PE-3 Physical Access Control | Entry to the rooms that hold the servers | \<Organisation\>'s physical access logs, inherited (\<Physical and Environmental Protection Management\>) |
| SI-4 System Monitoring | Events that show an attack or misuse | The detection use cases U1 to U8 (\<System and Information Integrity Management\>, section 3.4) |
| PM-21 Accounting of Disclosures | Disclosures of personal data | The export and download records of Table 2 |

### B.2 AU controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 12 says where.

**Table 12: AU controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| AU-5(1) Storage Capacity Warning | A warning before audit storage fills | Not required. The monthly capacity check stands in for it |
| AU-5(2) Real-time Alerts | Alerts at once for defined failures | Not required. The design alerts within 1 hour |
| AU-6(5), AU-6(6) Integrated Analysis; Correlation with Physical Monitoring | Joining audit review with scanning, performance and physical access data | Not required, and not done |
| AU-8(1) Synchronisation with an Authoritative Time Source | Withdrawn in Revision 5; now SC-45(1) | Not required. Done anyway: both servers within 1 second of UTC (section 3.6) |
| AU-9(2) Store on Separate Physical Systems | Audit records kept on a different system from the one audited | Not required. Done in part: the newest chain hash is copied daily to a separate store, and the archive is offline |
| AU-9(3) Cryptographic Protection | Cryptography to protect the integrity of audit information | Not required. Done in design: the keyed chain hash (section 3.5). Not yet built (PA-73, PA-74) |
| AU-10 Non-repudiation | Proof that a person carried out an action | Not required at Moderate. Records name the person PingFederate authenticated |
| AU-12(1), AU-12(3) System-wide Audit Trail; Changes by Authorised Individuals | One time-ordered trail across components; changing what is logged at run time | Not required. The weekly comparison by time stands in for the first. The second relates to PA-105 |
| AU-13, AU-14, AU-16 Monitoring for Disclosure; Session Audit; Cross-organisational Logging | Further capabilities | In no baseline. Not done |
| AU-3(3) Limit Personally Identifiable Information Elements | Only the personal data needed in records | In the privacy baseline. Assessed with the PT family; design in section 3.4 |
