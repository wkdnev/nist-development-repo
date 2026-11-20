# \<System Name\> System and Information Integrity Management

## 1 Purpose

This document shows how \<System Name\> keeps its software and information sound, for each of the 18 System and Information Integrity (SI) controls in the CSS Moderate baseline: fixing flaws, malicious code protection, monitoring, advisories, integrity checks, input validation, error handling, retention and memory protection.

Section 3 sets out the design: the upload checks and malware scanning; flaw remediation and advisories; monitoring and the detection use cases; the integrity baseline and checks; error handling and memory protection; retention; how integrity stands today; and what \<Organisation\> provides. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define.

This is the only place this design is held. Other documents point here. The policy is in \<Policy\> (SI), and the steps people follow are in \<Procedures\> (SI). The vulnerability timetable is in \<Risk Assessment Management\>, section 3.6, the retention schedule in \<PII Processing Management\>, section 3.7, and the audit design in \<Audit and Accountability Management\>. The privacy controls SI-12(1) to SI-12(3), SI-18, SI-18(4) and SI-19 are set out in \<PII Processing Management\>.

An assessor examines the use cases, the baseline, the advisory records and the test results; interviews the security officer, the developers and the Windows server administrator; and tests the upload checks, the error messages, the malware scan and the alerts (CSS). So for each control section 4 gives:

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

Of the 18 controls, 2 are implemented, 6 are partially implemented, 8 are not implemented and 2 are not applicable. No control in the Moderate baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 2: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| SI-1 | Policy and Procedures | Partially implemented | Not yet shared. The later version awaits the Head of Cyber | NC-SI-01; PA-20 |
| SI-2 | Flaw Remediation | Partially implemented | 7 package advisories open | NC-SI-02; PA-56 |
| SI-2(2) | Automated Flaw Remediation Status | Not implemented | Run by hand; dependency alerts off | NC-SI-03; PA-57, PA-91 |
| SI-3 | Malicious Code Protection | Not implemented | No malware scan of uploads; Defender not set up | NC-SI-04; PA-58 |
| SI-4 | System Monitoring | Partially implemented | No forwarding, alerts or reviews; no legal opinion | NC-SI-05; PA-130, EV-SI-01 |
| SI-4(2) | Automated Tools and Mechanisms for Real-time Analysis | Not implemented | No automated analysis | NC-SI-06; PA-59 |
| SI-4(4) | Inbound and Outbound Communications Traffic | Not implemented | Not evidenced | NC-SI-07; PA-130, EV-SI-01 |
| SI-4(5) | System-generated Alerts | Not implemented | Nothing raises an alert | NC-SI-08; PA-59 |
| SI-5 | Security Alerts, Advisories, and Directives | Not implemented | Advisories not yet received | NC-SI-09; PA-130 |
| SI-7 | Software, Firmware, and Information Integrity | Partially implemented | MD5 checksums; the audit chain cannot be recomputed | NC-SI-10; PA-61, PA-74 |
| SI-7(1) | Integrity Checks | Not implemented | No scheduled check | NC-SI-11; PA-61 |
| SI-7(7) | Integration of Detection and Response | Implemented | Nothing | NC-SI-12 (met) |
| SI-8 | Spam Protection | Not applicable | Not applicable | TR-SI-01 |
| SI-8(2) | Automatic Updates | Not applicable | Not applicable | TR-SI-01 |
| SI-10 | Information Input Validation | Implemented | Nothing | NC-SI-13 (met) |
| SI-11 | Error Handling | Partially implemented | About 29 responses return error detail | NC-SI-14; PA-60 |
| SI-12 | Information Management and Retention | Not implemented | Retention and disposal not built | NC-SI-15; PA-70 |
| SI-16 | Memory Protection | Partially implemented | Windows settings not confirmed | NC-SI-16; PA-54 |

Three things matter most. Seven package advisories are open, five of them High, and are due by 20 November 2026 (PA-56, rated High). Nothing scans uploads for malware, and documents in the database are out of Defender's sight (PA-58, Medium). And nothing raises an alert, so an attack would go unnoticed (PA-59, Medium).

## 3 The design

### 3.1 Principles

1. **Fix flaws on time.** Every flaw is fixed to the one timetable.
2. **Check what comes in.** Every upload and input is checked on the server, and every upload is scanned before it is stored.
3. **Watch and alert.** Logs are collected, reviewed and turned into alerts.
4. **Prove nothing has changed.** Releases, documents and audit records are checked against a known-good baseline.

These carry out the principles and rules of \<Policy\>, sections SI.3 and SI.4.

![Figure 1: How integrity is kept, from upload to alert](figures/sim-figure-1.png)

**Figure 1: How integrity is kept, from upload to alert**

### 3.2 Upload checks and malware scanning

Every upload passes these checks on the server before it is stored (SI-3, SI-10). Documents are held in PostgreSQL and never written to disk, so Defender's file scan cannot see them; \<System Name\> must ask Defender to scan each one first. All API inputs and search terms are validated on the server too, and database queries use parameters.

**Table 3: Upload checks**

| Check | How | State now |
| --- | --- | --- |
| Allowed types | Only the supported document types; any other extension is refused | In place (H06) |
| Type and signature | The declared type and the file's first bytes must match its extension | In place (H04, H05) |
| Size | A limit by role: 25 MB read-only, 50 MB default, 75 MB editor, 100 MB administrator | In place (code) |
| File name | A name containing a path or invalid characters is refused | In place (H07) |
| Malware scan | The bytes are passed to Defender through AMSI before storing; a flagged file is refused, audited and reported | Not built (H08; PA-58) |
| Proof | The EICAR test file, built in memory on the test stack, must be refused | Not possible until the scan exists |

Microsoft Defender runs on both servers, with real-time protection, daily updates and a weekly full scan. What it finds is quarantined, and the Windows server administrator and the security officer are alerted (PRO-SI-2). When the upload scan is first turned on, every document already stored is scanned once, as none was scanned when it was uploaded (PA-58). Exports and downloads are of documents already scanned, so no further scan is needed on the way out.

### 3.3 Flaw remediation and advisories

Flaws are fixed to the one timetable in \<Risk Assessment Management\>, section 3.6 (D-RA-P02), which replaced the 14-day and 30-day limits of version \<ver\>. Each update is tested on a separate test stack, then installed through change control (PRO-SI-1). Update status is checked monthly and at each release by Test-Vulnerability.ps1, the repositories' dependency alerts and the Windows Update reports from both servers (SI-2(2)).

**Table 4: Advisory sources**

| Source | What it covers | How often | State now |
| --- | --- | --- | --- |
| NCSC alerts and advisories | UK threats and vulnerabilities | As published | Not started |
| NCSC Early Warning | Incidents, abuse and vulnerable services on \<System Name\>'s addresses | As raised | \<Organisation\> to register (EV-SI-03) |
| CISA Known Exploited Vulnerabilities | Flaws being exploited | Weekly (SyOps C50) | Not started |
| Microsoft Security Response Center | Windows Server, .NET and IIS | Monthly and out of band | Not started |
| GitHub advisories and dependency alerts | NuGet packages | As raised | Alerts off (PA-91) |
| PostgreSQL security | The database | As published | Not started |

An internal advisory is a security officer's note on TPL-7, naming the flaw, the components affected, the deadline under the timetable and who acts. A directive that applies is carried out to the timetable; if it cannot be, the issuer is told (SI-5).

### 3.4 Monitoring and detection use cases

Application, Windows and PostgreSQL logs, and the audit trail, are forwarded to \<Organisation\>'s central logging \[service to be confirmed, EV-SI-01\]; if none is available, CISA's Logging Made Easy is the fallback. The security officer reviews them weekly (PRO-SI-3), and these events must raise an alert (SI-4, SI-4(2), SI-4(5)). None is built yet (H12; PA-59).

Since sign-in moved to AD FS (D-AC-23), failed sign-ins and changes to administrator groups happen in \<Organisation\>'s systems, not in \<System Name\>. Use cases U1 and U4 therefore need those events from \<Organisation\> (EV-SI-01). The system owner confirmed this on 18 November 2026 (D-SR-15).

**Table 5: Detection use cases**

| ID | Event | Source | Threshold | Alert to | Response |
| --- | --- | --- | --- | --- | --- |
| U1 | Failed sign-ins | AD FS sign-in logs, from \<Organisation\> (D-AC-23) | 5 for one account, or 20 in total, in 15 minutes | Security officer | PRO-SI-4 |
| U2 | Audit chain break | Chain check (PA-37) | Any | Security officer, auditor | Incident (\<Incident Response Management\>) |
| U3 | Malware detected | Defender, and the AMSI upload scan | Any | Security officer, Windows server administrator | Incident |
| U4 | Privilege change | Changes to the membership of \<System Name\>'s AD administrator groups, from \<Organisation\> (D-AC-23) | Any person added to an administrator group | Security officer | Check against the approved request (TPL-2) |
| U5 | Bulk export | Audit trail | More than \[number\] documents by one user in a day | Security officer | PRO-SI-4 |
| U6 | Administrator session out of hours | Audit trail: a session started under an administrator role | Outside \[hours\] | Security officer | PRO-SI-4 |
| U7 | Audit logging failure | Application log (AU-5) | Any | Security officer | PRO-SI-4 |
| U8 | Unexpected software change | Integrity check (PRO-SI-6) | Any | Security officer | Incident |

\<Organisation\> monitors traffic into and out of the network continuously, against the agreed flows (SI-4(4)). Users are monitored only after the legal adviser's opinion (D-SI-07), only as far as needed, and with staff told what is monitored and why.

### 3.5 Integrity baseline and checks

The known-good v1.0 release was recorded by Test-Integrity.ps1 on 12 November 2026. Later checks compare against these SHA-256 values (SI-7, SI-7(1)). The full values are kept with the SI evidence. The test images apply to the test environment only; the release packages for the servers get their own baseline when they are built (D-PL-10; PA-61).

**Table 6: Integrity baseline, v1.0**

| Item | SHA-256 (first 16 characters) |
| --- | --- |
| API test image | 11b7371a90fccf04 |
| UI application test image | 9eac4536e411e28a |
| Admin application test image | 3caa545ce84f4bcc |
| API file | c6dac084e27ee7f9 |
| UI application application file | c73de21d2294b15d |
| Admin application application file | fc79003538bbbc75 |
| shared library library file (the same in all three) | 45df38576a5804b9 |

Release packages, stored documents and audit records are checked at start-up, at each release and monthly; \<Organisation\> checks the servers' firmware. An unexpected change is handled as an incident, and the item is restored from a trusted copy or backup (SI-7(7); PRO-SI-6).

### 3.6 Error handling and memory protection

Users and API callers see a general error message; the detail goes only to the logs, for administrators and developers (SI-11; PA-60). Memory is protected by .NET managed memory and by Windows data execution prevention and address randomisation on the servers (SI-16).

### 3.7 Information retention

Information is kept and disposed of under \<System Name\>'s retention schedule, which is held in \<PII Processing Management\>, section 3.7 (SI-12). This table summarises the periods that other designs set.

**Table 7: Retention**

| Information | Kept for | Source | State now |
| --- | --- | --- | --- |
| Documents and HR records | As in \<PII Processing Management\>, section 3.7 \[periods set by the business owner and legal adviser\] | D-PT-21 | Not applied (PA-70) |
| Audit records | 12 months online, then 12 months archived | \<Audit and Accountability Management\> (AU-11) | Not built (PA-42) |
| Application logs | 30 days | \<Audit and Accountability Management\> | Not controlled |
| Export copies | Deleted once downloaded, and within 24 hours | \<Media Protection Management\> | Copies left behind (PA-86) |
| Backups | 14 daily, 8 weekly and 12 monthly copies | \<Contingency Planning Management\>, section 3.8 | Not built (PA-64) |

### 3.8 How integrity stands today

Test-Integrity.ps1 ran on 12 November 2026 on the build tagged v1.0, in the test stack: 12 checks, 7 passed and 5 gaps. Its results, with their hashes, are kept with the SI evidence.

**Table 8: How integrity is built today**

| Part | What happens today | Check | Item |
| --- | --- | --- | --- |
| Packages | 7 advisories in two packages, 5 High (11 November) | RA V01 | PA-56 |
| Error detail | A malformed upload returns the exception message; about 29 API responses do so | H01 | PA-60 |
| Read endpoints | Bad identifiers return 404 with no detail | H02 | None |
| Injection-style input | Refused cleanly, with no server errors or database text | H03 | None |
| Upload checks | Wrong signatures, disguised executables, unknown types and paths are all rejected | H04 to H07 | None |
| Malware scan | No scanner call in the upload path | H08 | PA-58 |
| Document checksums | MD5, held in a column beside each page | H09 | PA-61 |
| Audit chain | No broken links, but only 1 of 15 records' hashes can be recomputed | H10 | PA-74 |
| Failed sign-ins | Recorded in the audit trail of the v1.0 build, which used its own passwords. Since sign-in moved to AD FS, AD FS records them (D-AC-23) | H11 | None |
| Alerts | Nothing raises one | H12 | PA-59 |
| Memory | .NET managed memory; the test containers run as a non-root user (C08). On the servers each application runs as a Windows service under its own account (D-PL-10) | Code review | None |

### 3.9 What \<Organisation\> provides

**Table 9: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Network monitoring and central logging | SI-4, SI-4(2), SI-4(4) | Traffic is monitored, \<System Name\>'s logs can be forwarded, and AD FS sign-in and AD group change events reach the security officer | EV-SI-01 | Not sent |
| Firmware updates and integrity checks for the hosting | SI-2, SI-7, SI-7(1) | Firmware is kept up to date and checked | EV-SI-02 | Not sent |
| NCSC Early Warning and alert forwarding | SI-5 | \<Organisation\> is registered, and alerts that affect \<System Name\> reach the security officer | EV-SI-03 | Not sent |

**Today:** no request has been sent, and none of this is evidenced.

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 SI-1 Policy and Procedures

**Table 10: SI-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A system and information integrity policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (SI): a system-level policy, shared with everyone who administers or develops \<System Name\>. The legal adviser reviewed it on 12 November 2026 | Version \<ver\> approved by the Head of Cyber (D-SI-01). The later version awaits the Head of Cyber (D-SI-06). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (SI): eight procedures, PRO-SI-1 to PRO-SI-8. Shared with the same people | Version \<ver\> approved by the system owner (D-SI-09). Not yet shared |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 12 November 2026 after the SI pack review. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | Reviewed on 12 November 2026. The first yearly review falls due in November 2027 |

**Table 11: SI-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy; all eight procedures (\<Procedures\>) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-SI-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-SI-06) |

### 4.2 SI-2 Flaw Remediation

**Table 12: SI-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Identify, report and correct system flaws | Flaws come from the package check, the advisories in section 3.3, scans and tests. Each is recorded on TPL-7 and fixed (PRO-SI-1) | 7 package advisories open, 5 of them High (V01; PA-56) |
| b | Test updates for effectiveness and side effects before installing them | On a separate test stack first (PRO-SI-1, step 3) | Approved. Not yet in use |
| c | Install security-relevant updates within a defined time of their release | The one timetable in \<Risk Assessment Management\>, section 3.6: 3 days if exploited; 14 days for Critical and High; 30 for Medium; 90 for Low, or 30 once a fix exists | Not met for the 7 package advisories (PA-56) |
| d | Make flaw remediation part of configuration management | Each fix goes through change control (\<Configuration Management\>) | Approved. The change workflow is not set up (PA-53) |

**Table 13: SI-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers, Windows server administrator |
| Enforced by | The package check; the change process |
| Rules and procedures | Policy rule R1 (\<Policy\>, section SI.4); PRO-SI-1 (\<Procedures\>) |
| Tests | Check V01 of Test-Vulnerability.ps1, 11 November 2026: 7 advisories, 5 of them High |
| Records an assessor will ask for | TPL-7 records with due dates and fixes; change records |
| Status | Partially implemented |
| Risk decision | NC-SI-02, rated High: remediate |
| Open items | PA-56: update the packages, or the authorising official decides (D-RA-13) |

### 4.3 SI-2(2) Automated Flaw Remediation Status

**Table 14: SI-2(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Check with automated means, at a defined frequency, whether components have their security updates | Test-Vulnerability.ps1, repository dependency alerts and Windows Update reports, monthly and at each release | The script exists but is run by hand (PA-57); dependency alerts are off (PA-91) |

**Table 15: SI-2(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers |
| Enforced by | Test-Vulnerability.ps1; GitHub dependency alerts; Windows Update |
| Rules and procedures | Policy rule R2 (\<Policy\>, section SI.4); PRO-SI-1, step 1 (\<Procedures\>) |
| Tests | Check V01 of Test-Vulnerability.ps1 |
| Records an assessor will ask for | Scheduled results; the alert settings; Windows Update reports |
| Status | Not implemented |
| Risk decision | NC-SI-03, rated Medium: remediate |
| Open items | PA-57: schedule the check. PA-91: turn on dependency alerts |

### 4.4 SI-3 Malicious Code Protection

**Table 16: SI-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Use signature-based or non-signature-based malicious code protection at entry and exit points | Microsoft Defender, signature and behaviour based, on both servers, and every upload passed to Defender through AMSI before it is stored (section 3.2). Documents stored before the scan exists are scanned once when it is turned on | Not built: no scanner call in the upload path (H08; PA-58). The servers are not built |
| b | Update the protection automatically as new releases are available | Defender updates daily, under configuration management | Not built (PA-58) |
| c.1 | Scan periodically, and in real time as files from outside are downloaded, opened or run | A weekly full scan, real-time protection on both servers, and each upload scanned before it is stored | Not built (PA-58) |
| c.2 | Block or quarantine malicious code, and alert defined people | Block and quarantine; refuse the upload and record it in the audit trail; alert the Windows server administrator and the security officer | Not built (PA-58, PA-59) |
| d | Deal with false positives and their effect on availability | Each false positive is recorded on TPL-10 with how it was resolved (PRO-SI-2, step 4) | Not yet in use |

**Table 17: SI-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Windows server administrator, developers |
| Enforced by | Microsoft Defender and AMSI, once set |
| Rules and procedures | Policy rules R3, R4 (\<Policy\>, section SI.4); PRO-SI-2 (\<Procedures\>) |
| Tests | Check H08 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): no scanner call in the upload path |
| Records an assessor will ask for | Defender's status on both servers; a refused EICAR test file; TPL-10 records |
| Status | Not implemented |
| Risk decision | NC-SI-04, rated Medium: remediate |
| Open items | PA-58: scan uploads through AMSI and set up Defender |

### 4.5 SI-4 System Monitoring

**Table 18: SI-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | Monitor to detect attacks and indicators of attack, against defined objectives | Detect attacks, misuse and unauthorised connections, through the detection use cases in section 3.4 | Use cases set. Nothing raises an alert (H12; PA-59) |
| a.2 | Monitor to detect unauthorised local, network and remote connections | \<Organisation\>'s network monitoring, and the allowed flows (\<System and Communications Protection Management\>, section 3.2) | Not evidenced (EV-SI-01) |
| b | Identify unauthorised use by defined techniques | Log forwarding to \<Organisation\>'s central logging, the detection use cases, the audit records and \<Organisation\>'s network monitoring | No forwarding or alerts (PA-59) |
| c | Place monitoring strategically, and at ad hoc locations for transactions of interest | Application, Windows and PostgreSQL logs, and the audit trail; AD FS sign-in logs from \<Organisation\> | Logs written; not forwarded |
| d | Analyse detected events and anomalies | The security officer reviews the logs and alerts weekly (PRO-SI-3) | Not started (PA-130) |
| e | Adjust monitoring when risk changes | The system owner raises monitoring when risk rises (PRO-SI-3, step 3) | Not yet in use |
| f | Obtain a legal opinion on monitoring | The legal adviser's opinion on monitoring users, before monitoring starts (D-SI-07) | Not given (D-SI-07) |
| g | Provide monitoring information to defined people at a defined frequency | Application, Windows and PostgreSQL logs to the security officer, weekly | Not started (PA-130) |

**Table 19: SI-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Security officer, \<Organisation\> |
| Enforced by | Central logging and alert rules, once built; the weekly review |
| Rules and procedures | Policy rules R5, R6 (\<Policy\>, section SI.4); PRO-SI-3, PRO-SI-4 (\<Procedures\>) |
| Tests | Checks H11 and H12 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): failed sign-ins were recorded by the v1.0 build; nothing raises an alert |
| Records an assessor will ask for | TPL-8 records of weekly reviews; alerts and their responses; the legal opinion |
| Status | Partially implemented |
| Risk decision | NC-SI-05, rated Low: obtain evidence |
| Open items | PA-59: forward logs and build the alerts. PA-130: start the reviews. D-SI-07: the legal opinion |

### 4.6 SI-4(2) Automated Tools and Mechanisms for Real-time Analysis

**Table 20: SI-4(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use automated tools to support near real-time analysis of events | \<Organisation\>'s central logging, or CISA's Logging Made Easy if none is available, with alert rules for the detection use cases | No forwarding or automated analysis (H12; PA-59) |

**Table 21: SI-4(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Security officer |
| Enforced by | Central logging, once connected |
| Rules and procedures | Policy rule R5 (\<Policy\>, section SI.4); PRO-SI-3 (\<Procedures\>) |
| Tests | Check H12 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): nothing raises an alert |
| Records an assessor will ask for | The forwarding connection; the alert rules |
| Status | Not implemented |
| Risk decision | NC-SI-06, rated Medium: remediate |
| Open items | PA-59 |

### 4.7 SI-4(4) Inbound and Outbound Communications Traffic

**Table 22: SI-4(4) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Set criteria for unusual or unauthorised inbound and outbound traffic | Traffic outside the agreed flows; and outbound, unusually large transfers | Defined |
| b | Monitor inbound and outbound traffic at a defined frequency for that activity | Continuously, by \<Organisation\> | Not evidenced (EV-SI-01) |

**Table 23: SI-4(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s network monitoring |
| Rules and procedures | Policy rule R5 (\<Policy\>, section SI.4); PRO-SI-3 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s monitoring description and a sample report |
| Status | Not implemented |
| Risk decision | NC-SI-07, rated Low: obtain evidence |
| Open items | EV-SI-01. PA-130 |

### 4.8 SI-4(5) System-generated Alerts

**Table 24: SI-4(5) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Alert defined people when defined indications of compromise occur | The security officer, for each detection use case in section 3.4 | Nothing raises an alert (H12; PA-59) |

**Table 25: SI-4(5) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers, security officer |
| Enforced by | Alert rules, once built |
| Rules and procedures | Policy rule R5 (\<Policy\>, section SI.4); PRO-SI-4 (\<Procedures\>) |
| Tests | Check H12 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): nothing raises an alert |
| Records an assessor will ask for | The alert rules; alerts raised and their responses |
| Status | Not implemented |
| Risk decision | NC-SI-08, rated Medium: remediate |
| Open items | PA-59 |

### 4.9 SI-5 Security Alerts, Advisories, and Directives

**Table 26: SI-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Receive alerts, advisories and directives from defined external organisations on an ongoing basis | NCSC, including Early Warning; CISA's Known Exploited Vulnerabilities catalogue, weekly; Microsoft; .NET and GitHub; and PostgreSQL (section 3.3) | Not started. Early Warning not registered (EV-SI-03) |
| b | Generate internal alerts and advisories as needed | The security officer's note on TPL-7, naming the flaw, the components affected, the deadline and who acts | Not yet in use |
| c | Pass them to defined people | The security officer, administrators and developers | Not yet in use |
| d | Carry out security directives in time, or tell the issuer how far they are not met | Directives that apply are carried out to the timetable, through change control; the issuer is told if one cannot be met | None received yet |

**Table 27: SI-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R7 (\<Policy\>, section SI.4); PRO-SI-5 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-7 records of advisories and what was done |
| Status | Not implemented |
| Risk decision | NC-SI-09, rated Low: approve |
| Open items | PA-130: start receiving the advisories. EV-SI-03 |

### 4.10 SI-7 Software, Firmware, and Information Integrity

**Table 28: SI-7 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Use integrity verification tools to detect unauthorised changes to defined software, firmware and information | SHA-256 for the release packages and stored documents, the audit chain for audit records, and \<Organisation\> for the servers' firmware (section 3.5) | Baseline recorded. Documents use MD5 (H09; PA-61); the audit chain cannot be recomputed (H10; PA-74) |
| b | Take defined actions when unauthorised changes are detected | Treat it as an incident, and restore from a trusted copy or backup; for firmware, tell \<Organisation\>'s security contact | Defined |

**Table 29: SI-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers, security officer |
| Enforced by | SHA-256 checks and the audit chain, once corrected |
| Rules and procedures | Policy rule R8 (\<Policy\>, section SI.4); PRO-SI-6 (\<Procedures\>) |
| Tests | Checks H09 and H10 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): both showed gaps |
| Records an assessor will ask for | The baseline file; TPL-8 records of each check |
| Status | Partially implemented |
| Risk decision | NC-SI-10, rated Low: remediate |
| Open items | PA-61: SHA-256 and release checksums. PA-74: a verifiable audit chain |

### 4.11 SI-7(1) Integrity Checks

**Table 30: SI-7(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Check integrity at start-up, at defined events and at a defined frequency | At start-up, at each release and monthly; firmware monthly and at a change to the hosting, by \<Organisation\> | No scheduled check (PA-61) |

**Table 31: SI-7(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Security officer |
| Enforced by | Checks, once built |
| Rules and procedures | Policy rule R8 (\<Policy\>, section SI.4); PRO-SI-6 (\<Procedures\>) |
| Tests | None. The baseline was recorded on 12 November 2026 |
| Records an assessor will ask for | TPL-8 records of each check |
| Status | Not implemented |
| Risk decision | NC-SI-11, rated Low: remediate |
| Open items | PA-61. EV-SI-02 for firmware |

### 4.12 SI-7(7) Integration of Detection and Response

**Table 32: SI-7(7) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Bring the detection of defined unauthorised changes into incident response | Any unexpected change to software, stored documents or audit records is handled as an incident (PRO-SI-6, step 3; \<Incident Response Management\>) | Defined and approved |

**Table 33: SI-7(7) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R8 (\<Policy\>, section SI.4); PRO-SI-6 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Incident records of integrity events |
| Status | Implemented |
| Risk decision | NC-SI-12, rated Low: approve; now satisfied |
| Open items | None |

### 4.13 SI-8 Spam Protection

**Table 34: SI-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use spam protection at entry and exit points, and update it | Not applicable: \<System Name\> sends and receives no email (\<Tailoring Register\>, TR-SI-01) | Not applicable |

**Table 35: SI-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Decision | TR-SI-01 |

### 4.14 SI-8(2) Automatic Updates

**Table 36: SI-8(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Update spam protection automatically | Not applicable: \<System Name\> sends and receives no email (\<Tailoring Register\>, TR-SI-01) | Not applicable |

**Table 37: SI-8(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Decision | TR-SI-01 |

### 4.15 SI-10 Information Input Validation

**Table 38: SI-10 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Check the validity of defined inputs | All API inputs, uploads (type, signature, size and name) and search terms, on the server, with parameterised database queries (section 3.2) | Tested: refused or rejected (H03 to H07) |

**Table 39: SI-10 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers |
| Enforced by | The applications' validation and upload checks |
| Rules and procedures | Policy rules R4, R9 (\<Policy\>, section SI.4); PRO-SI-8 (\<Procedures\>) |
| Tests | Checks H02 to H07 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): all passed |
| Records an assessor will ask for | The test results |
| Status | Implemented |
| Risk decision | NC-SI-13, rated Low: none; now satisfied |
| Open items | None |

### 4.16 SI-11 Error Handling

**Table 40: SI-11 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Give error messages that help put things right, without revealing what could be exploited | Users and callers see a general message; the detail goes to the log | About 29 API responses return the exception message (H01; PA-60) |
| b | Show error detail only to defined people | Administrators and developers, through the logs | Not met while the API returns the detail (PA-60) |

**Table 41: SI-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers |
| Enforced by | The applications' error handling |
| Rules and procedures | Policy rule R10 (\<Policy\>, section SI.4); PRO-SI-8 (\<Procedures\>) |
| Tests | Check H01 (Test-Integrity.ps1 on the v1.0 build, 12 November 2026): showed the gap |
| Records an assessor will ask for | Test results; the log entries for errors |
| Status | Partially implemented |
| Risk decision | NC-SI-14, rated Medium: remediate |
| Open items | PA-60: return general messages |

### 4.17 SI-12 Information Management and Retention

**Table 42: SI-12 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Manage and keep information, and outputs, as laws, policies and operational needs require | \<System Name\>'s retention schedule (\<PII Processing Management\>, section 3.7), with the periods in section 3.7 of this document | Set, with placeholders. Not applied: no retention or disposal is built (PA-70) |

**Table 43: SI-12 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | System owner |
| Enforced by | \<System Name\>, once retention and disposal are built |
| Rules and procedures | Policy rule R11 (\<Policy\>, section SI.4); PRO-SI-7 (\<Procedures\>) |
| Tests | Checks Q03 and Q08 of Test-PersonalData.ps1, 11 November 2026: both showed gaps |
| Records an assessor will ask for | The schedule; disposal records on TPL-13 and in the audit trail |
| Status | Not implemented |
| Risk decision | NC-SI-15, rated Low: approve |
| Open items | PA-70: build retention and disposal. PA-42: audit record retention |

### 4.18 SI-16 Memory Protection

**Table 44: SI-16 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use defined controls to protect memory from unauthorised code execution | Windows data execution prevention and address randomisation, and .NET managed memory | .NET managed memory in place. Data execution prevention and address randomisation to confirm on the servers (PA-54) |

**Table 45: SI-16 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Windows server administrator |
| Enforced by | Windows Server and .NET |
| Rules and procedures | Policy rule R9 (\<Policy\>, section SI.4); no procedure of its own |
| Tests | None. Not testable until the servers exist |
| Records an assessor will ask for | The servers' settings |
| Status | Partially implemented |
| Risk decision | NC-SI-16, rated Low: obtain evidence |
| Open items | PA-54 |

## Appendix A Parameter register

These are the CSS organisation-defined values for the 18 SI entries: 57 in total. They were agreed on 6 November 2026 (D-SI-P01), and those changed on 12 November 2026 in D-SI-P02. **State now** says whether \<System Name\> meets the value today.

**Table 46: SI parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| SI-01\_ODP\[01\] | Who receives the policy | Everyone who administers or develops \<System Name\> | Not yet shared |
| SI-01\_ODP\[02\] | Who receives the procedures | Everyone who administers or develops \<System Name\> | Not yet shared |
| SI-01\_ODP\[03\] | Level of the policy | System level | In place |
| SI-01\_ODP\[04\] | Official who manages them | System owner | In place |
| SI-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review due November 2027 |
| SI-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Reviewed after the SI pack review, 12 November 2026 |
| SI-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review due November 2027 |
| SI-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Reviewed after the SI pack review, 12 November 2026 |
| SI-02\_ODP | Time to install updates | The one timetable in \<Risk Assessment Management\>, section 3.6: 3 days if exploited; 14 days Critical and High; 30 days Medium; 90 days Low (30 once a fix exists); from release or detection | 7 advisories open (PA-56) |
| SI-02(02)\_ODP\[01\] | Automated mechanisms | Test-Vulnerability.ps1, repository dependency alerts and Windows Update reports | Script exists; not scheduled (PA-57); alerts off (PA-91) |
| SI-02(02)\_ODP\[02\] | Frequency | Monthly, and at each release | Run by hand |
| SI-03\_ODP\[01\] | Type of protection | Signature-based and behaviour-based | VMs not built |
| SI-03\_ODP\[02\] | Scan frequency | Weekly | VMs not built |
| SI-03\_ODP\[03\] | Where real-time scans run | Endpoint (both VMs) and network entry: each upload, through AMSI, before it is stored | No scanner call (H08; PA-58) |
| SI-03\_ODP\[04\] | Response | Block and quarantine | VMs not built |
| SI-03\_ODP\[05\] | Other action | Refuse the upload and record it in the audit trail | Not built (PA-58) |
| SI-03\_ODP\[06\] | Who is alerted | Windows server administrator and security officer | Not built (PA-59) |
| SI-04\_ODP\[01\] | Monitoring objectives | Detect attacks, misuse and unauthorised connections | Defined |
| SI-04\_ODP\[02\] | Techniques and methods | Log forwarding to \<Organisation\>'s central logging, the detection use cases in section 3.4, audit records and \<Organisation\>'s network monitoring | No forwarding or alerts (H12; PA-59) |
| SI-04\_ODP\[03\] | Monitoring information | Application, Windows and PostgreSQL logs | Failed sign-ins are recorded by AD FS since sign-in moved there (D-AC-23); \<System Name\>'s logs are not forwarded |
| SI-04\_ODP\[04\] | Who receives it | Security officer | Defined |
| SI-04\_ODP\[05\] | When it is provided | At the set frequency | Defined |
| SI-04\_ODP\[06\] | Frequency | Weekly | Reviews not started |
| SI-04(04)\_ODP\[01\] | Inbound monitoring frequency | Continuous, by \<Organisation\> | Not evidenced (EV-SI-01) |
| SI-04(04)\_ODP\[02\] | Unusual inbound activity | Traffic outside the agreed flows | Defined |
| SI-04(04)\_ODP\[03\] | Outbound monitoring frequency | Continuous, by \<Organisation\> | Not evidenced (EV-SI-01) |
| SI-04(04)\_ODP\[04\] | Unusual outbound activity | Traffic outside the agreed flows, or unusually large transfers | Defined |
| SI-04(05)\_ODP\[01\] | Who is alerted | Security officer | Defined |
| SI-04(05)\_ODP\[02\] | Compromise indicators | The detection use cases in section 3.4 | No alerts (H12; PA-59) |
| SI-05\_ODP\[01\] | Sources of advisories | NCSC (including Early Warning), CISA's Known Exploited Vulnerabilities catalogue, Microsoft, .NET and GitHub, and PostgreSQL | Not started; Early Warning not registered (EV-SI-03) |
| SI-05\_ODP\[02\] | Who advisories go to | Selected personnel | Defined |
| SI-05\_ODP\[03\] | Personnel | Security officer, administrators and developers | Defined |
| SI-05\_ODP\[04\] | Elements | Not applicable; personnel are selected | Defined |
| SI-05\_ODP\[05\] | External organisations | Not applicable; personnel are selected | Defined |
| SI-07\_ODP\[01\] | Software | UI application, Admin application and API release packages | Baseline recorded (section 3.5); checks not built (PA-61) |
| SI-07\_ODP\[02\] | Firmware | VM firmware, through \<Organisation\> | Defined |
| SI-07\_ODP\[03\] | Information | Stored documents and audit records, protected with SHA-256 | Documents use MD5 (H09; PA-61); chain does not verify (H10; PA-74) |
| SI-07\_ODP\[04\] | Action for software | Treat as an incident, and restore from a trusted copy | Defined |
| SI-07\_ODP\[05\] | Action for firmware | Tell \<Organisation\>'s security contact | Defined |
| SI-07\_ODP\[06\] | Action for information | Treat as an incident, and restore from backup | Defined |
| SI-07(01)\_ODP\[01\] | Software checked | As SI-07\_ODP\[01\] | Defined |
| SI-07(01)\_ODP\[02\] | When | At startup, at set events and at a set frequency | Defined |
| SI-07(01)\_ODP\[03\] | Events | Each release | Defined |
| SI-07(01)\_ODP\[04\] | Frequency | Monthly | Not built (PA-61) |
| SI-07(01)\_ODP\[05\] | Firmware checked | As SI-07\_ODP\[02\] | Defined |
| SI-07(01)\_ODP\[06\] | When | At startup, at set events and at a set frequency | Defined |
| SI-07(01)\_ODP\[07\] | Events | A change to the hosting | Defined |
| SI-07(01)\_ODP\[08\] | Frequency | Monthly, by \<Organisation\> | Defined |
| SI-07(01)\_ODP\[09\] | Information checked | As SI-07\_ODP\[03\] | Defined |
| SI-07(01)\_ODP\[10\] | When | At startup, at set events and at a set frequency | Defined |
| SI-07(01)\_ODP\[11\] | Events | Each release | Defined |
| SI-07(01)\_ODP\[12\] | Frequency | Monthly | Not built (PA-37, PA-61) |
| SI-07(07)\_ODP | Changes that go to incident response | Any unexpected change to software, stored documents or audit records | Defined |
| SI-08(02)\_ODP | Update frequency | Not applicable (TR-SI-01) | Not applicable (TR-SI-01) |
| SI-10\_ODP | Inputs checked | All API inputs, uploads (type, signature, size and name) and search terms | Tested: refused or rejected (H03 to H07) |
| SI-11\_ODP | Who sees error detail | Administrators and developers | About 29 API responses leak detail (H01; PA-60) |
| SI-16\_ODP | Memory controls | Windows data execution prevention and address randomisation, and .NET managed memory | .NET managed memory and non-root containers in place; DEP and ASLR to confirm on the VMs |

## Appendix B Integrity controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. SI-8 and SI-8(2) are tailored out (TR-SI-01), and SI-12(1) to SI-12(3), SI-18, SI-18(4) and SI-19 are privacy baseline controls set out in \<PII Processing Management\>. Table 47 says where the design goes some way towards them.

**Table 47: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| SI-2(5), SI-2(6) | Automatic updates; removing previous versions after an update | Not required. Done in part: updates go through change control (section 3.3) |
| SI-3(8), SI-3(10) | Detecting unauthorised commands; analysing malicious code | Not required |
| SI-4(1), SI-4(10), SI-4(11) | System-wide intrusion detection; visibility of encrypted traffic; analysis of outbound traffic | Not required. Done in part: \<Organisation\>'s network monitoring (section 3.4) |
| SI-4(12), SI-4(14), SI-4(20) | Automated organisation alerts; wireless intrusion detection; privileged user monitoring | Not required: selected at High only, or not applicable. Done in part: use cases U4 and U6 watch privileged changes and sessions |
| SI-4(22), SI-4(23) | Unauthorised network services; host-based monitoring | Not required. Done in part: Defender on both servers |
| SI-6 Security and Privacy Function Verification | Checks that security functions work | Not required: selected at High only. Done in part: the test scripts (\<System and Services Acquisition Management\>, section 3.9) |
| SI-7(2), SI-7(5), SI-7(15) | Automated notification and response to integrity failures; code authentication | Not required: selected at High only. Done in part: signed release tags (PA-91) |
| SI-10(3) Predictable Behavior | Behaves predictably on invalid input | Not required. Done in design: invalid input is refused (H03 to H07) |
| SI-13, SI-14, SI-17, SI-20 to SI-23 | Failure prediction, non-persistence, fail-safe procedures, tainting, refresh, information diversity and fragmentation | Not required |
