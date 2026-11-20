# \<System Name\> System and Information Integrity Management

## 1 Purpose

This document sets out how \<System Name\> is designed and configured to keep its software and information sound, to meet the 18 System and Information Integrity (SI) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the upload checks and malware scanning; flaw remediation and advisories; monitoring and the detection use cases; the integrity baseline and checks; error handling and memory protection; retention; how integrity stands today; what \<Organisation\> provides; email and spam protection; and the policy and procedures. Each subsection names the controls it helps to meet. Appendix A lists the related controls and enhancements CSS does not select at Moderate.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.18 (Table 27). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (SI). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (SI), and the steps people follow are in \<Procedures\> (SI). The vulnerability timetable is in \<Risk Assessment Management\>, section 3.6, the retention schedule in \<PII Processing Management\>, section 3.7, and the audit design in \<Audit and Accountability Management\>. The privacy controls SI-12(1) to SI-12(3), SI-18, SI-18(4) and SI-19 are set out in \<PII Processing Management\>.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. The settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

Where section 3 notes what "today" is, or the state now, it means the tested v1.0 build. Those notes show where that build differs from the design.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.18 (Table 27).

## 3 The design

### 3.1 Principles

Controls met here: SI-2, SI-3, SI-4, SI-7, SI-10.

1. **Fix flaws on time.** Every flaw is fixed to the one timetable.
2. **Check what comes in.** Every upload and input is checked on the server, and every upload is scanned before it is stored.
3. **Watch and alert.** Logs are collected, reviewed and turned into alerts.
4. **Prove nothing has changed.** Releases, documents and audit records are checked against a known-good baseline.

These carry out the principles and rules of \<Policy\>, sections SI.3 and SI.4.

![Figure 1: How integrity is kept, from upload to alert](figures/sim-figure-1.png)

**Figure 1: How integrity is kept, from upload to alert**

### 3.2 Upload checks and malware scanning

Controls met here: SI-3, SI-10.

Every upload passes these checks on the server before it is stored (SI-3, SI-10). Documents are held in PostgreSQL and never written to disk, so Defender's file scan cannot see them; \<System Name\> must ask Defender to scan each one first. All API inputs and search terms are validated on the server too, and database queries use parameters.

**Table 1: Upload checks**

| Check | How | State now |
| --- | --- | --- |
| Allowed types | Only the supported document types; any other extension is refused | In place (H06) |
| Type and signature | The declared type and the file's first bytes must match its extension | In place (H04, H05) |
| Size | A limit by role: 25 MB read-only, 50 MB default, 75 MB editor, 100 MB administrator | In place (code) |
| File name | A name containing a path or invalid characters is refused | In place (H07) |
| Malware scan | The bytes are passed to Defender through AMSI before storing; a flagged file is refused, audited and reported | Not built (H08; PA-58) |
| Proof | The EICAR test file, built in memory on the test stack, must be refused | Not possible until the scan exists |

Microsoft Defender, which is signature and behaviour based, runs on both servers, with real-time protection, daily updates under configuration management and a weekly full scan. What it finds is blocked and quarantined, and the Windows server administrator and the security officer are alerted (PRO-SI-2). A flagged upload is refused and recorded in the audit trail. Each false positive is recorded on TPL-10 with how it was resolved (PRO-SI-2, step 4). When the upload scan is first turned on, every document already stored is scanned once, as none was scanned when it was uploaded (PA-58). Exports and downloads are of documents already scanned, so no further scan is needed on the way out.

### 3.3 Flaw remediation and advisories

Controls met here: SI-2, SI-2(2), SI-5.

Flaws come from the package check, the advisories in Table 2, scans and tests. Each is recorded on TPL-7 and fixed to the one timetable in \<Risk Assessment Management\>, section 3.6 (D-RA-P02; PRO-SI-1). Each update is tested on a separate test stack, then installed through change control (\<Configuration Management\>; PRO-SI-1, step 3). Update status is checked monthly and at each release by Test-Vulnerability.ps1, the repositories' dependency alerts and the Windows Update reports from both servers (SI-2(2)).

**Table 2: Advisory sources**

| Source | What it covers | How often | State now |
| --- | --- | --- | --- |
| NCSC alerts and advisories | UK threats and vulnerabilities | As published | Not started |
| NCSC Early Warning | Incidents, abuse and vulnerable services on \<System Name\>'s addresses | As raised | \<Organisation\> to register (EV-SI-03) |
| CISA Known Exploited Vulnerabilities | Flaws being exploited | Weekly (SyOps C50) | Not started |
| Microsoft Security Response Center | Windows Server, .NET and IIS | Monthly and out of band | Not started |
| GitHub advisories and dependency alerts | NuGet packages | As raised | Alerts off (PA-91) |
| PostgreSQL security | The database | As published | Not started |

An internal advisory is a security officer's note on TPL-7, naming the flaw, the components affected, the deadline under the timetable and who acts. The security officer passes alerts and advisories to the administrators and developers. A directive that applies is carried out to the timetable, through change control; if it cannot be, the issuer is told (SI-5).

### 3.4 Monitoring and detection use cases

Controls met here: SI-4, SI-4(2), SI-4(4), SI-4(5).

Application, Windows and PostgreSQL logs, and the audit trail, are forwarded to \<Organisation\>'s central logging \[service to be confirmed, EV-SI-01\]; if none is available, CISA's Logging Made Easy is the fallback. Alert rules in the central logging service analyse the events in near real time. The aim is to detect attacks, misuse and unauthorised local, network and remote connections. The security officer receives the logs and alerts and reviews them weekly (PRO-SI-3), and these events must raise an alert to the security officer (SI-4, SI-4(2), SI-4(5)). The system owner raises the level of monitoring when risk rises (PRO-SI-3, step 3). None is built yet (H12; PA-59).

Since sign-in moved to PingFederate (D-AC-23), failed sign-ins and changes to administrator groups happen in \<Organisation\>'s systems, not in \<System Name\>. Use cases U1 and U4 therefore need those events, including the PingFederate sign-in logs, from \<Organisation\> (EV-SI-01; D-SR-15).

**Table 3: Detection use cases**

| ID | Event | Source | Threshold | Alert to | Response |
| --- | --- | --- | --- | --- | --- |
| U1 | Failed sign-ins | PingFederate sign-in logs, from \<Organisation\> (D-AC-23) | 5 for one account, or 20 in total, in 15 minutes | Security officer | PRO-SI-4 |
| U2 | Audit chain break | Chain check (PA-37) | Any | Security officer, auditor | Incident (\<Incident Response Management\>) |
| U3 | Malware detected | Defender, and the AMSI upload scan | Any | Security officer, Windows server administrator | Incident |
| U4 | Privilege change | Changes to the membership of \<System Name\>'s AD administrator groups, from \<Organisation\> (D-AC-23) | Any person added to an administrator group | Security officer | Check against the approved request (TPL-2) |
| U5 | Bulk export | Audit trail | More than \[number\] documents by one user in a day | Security officer | PRO-SI-4 |
| U6 | Administrator sign-in out of hours | Audit trail: a sign-in by a person in an administrator group | Outside \[hours\] | Security officer | PRO-SI-4 |
| U7 | Audit logging failure | Application log (AU-5) | Any | Security officer | PRO-SI-4 |
| U8 | Unexpected software change | Integrity check (PRO-SI-6) | Any | Security officer | Incident |

\<Organisation\> monitors traffic into and out of the network continuously, against the allowed flows (\<System and Communications Protection Management\>, section 3.2). Unusual or unauthorised traffic is traffic outside those flows, and, outbound, unusually large transfers (SI-4(4)). Users are monitored only after the legal adviser's opinion (D-SI-07), only as far as needed, and with staff told what is monitored and why.

### 3.5 Integrity baseline and checks

Controls met here: SI-7, SI-7(1), SI-7(7).

The known-good v1.0 release was recorded by Test-Integrity.ps1. Later checks compare against these SHA-256 values (SI-7, SI-7(1)). The full values are kept with the SI evidence. The test images apply to the test environment only; the release packages for the servers get their own baseline when they are built (D-PL-10; PA-61).

**Table 4: Integrity baseline, v1.0**

| Item | SHA-256 (first 16 characters) |
| --- | --- |
| API test image | 11b7371a90fccf04 |
| UI application test image | 9eac4536e411e28a |
| Admin application test image | 3caa545ce84f4bcc |
| API file | c6dac084e27ee7f9 |
| UI application application file | c73de21d2294b15d |
| Admin application application file | fc79003538bbbc75 |
| shared library library file (the same in all three) | 45df38576a5804b9 |

Release packages and stored documents are checked with SHA-256, and audit records with the audit chain, at start-up, at each release and monthly. \<Organisation\> checks the servers' firmware monthly and at a change to the hosting. An unexpected change to software, stored documents or audit records is handled as an incident (\<Incident Response Management\>), and the item is restored from a trusted copy or backup (SI-7(7); PRO-SI-6, step 3). For firmware, \<Organisation\>'s security contact is told.

### 3.6 Error handling and memory protection

Controls met here: SI-11, SI-16.

Users and API callers see a general error message; the detail goes only to the logs, for administrators and developers (SI-11; PA-60). Memory is protected by .NET managed memory and by Windows data execution prevention and address randomisation on the servers (SI-16).

### 3.7 Information retention

Controls met here: SI-12.

Information is kept and disposed of under \<System Name\>'s retention schedule, which is held in \<PII Processing Management\>, section 3.7 (SI-12). This table summarises the periods that other designs set.

**Table 5: Retention**

| Information | Kept for | Source | State now |
| --- | --- | --- | --- |
| Documents and HR records | As in \<PII Processing Management\>, section 3.7 \[periods set by the business owner and legal adviser\] | D-PT-21 | Not applied (PA-70) |
| Audit records | 12 months online, then 12 months archived | \<Audit and Accountability Management\> (AU-11) | Not built (PA-42) |
| Application logs | 30 days | \<Audit and Accountability Management\> | Not controlled |
| Export copies | Deleted once downloaded, and within 24 hours | \<Media Protection Management\> | Copies left behind (PA-86) |
| Backups | 14 daily, 8 weekly and 12 monthly copies | \<Contingency Planning Management\>, section 3.8 | Not built (PA-64) |

### 3.8 How integrity stands today

Test-Integrity.ps1 ran on the build tagged v1.0, in the test stack: 12 checks, 7 passed and 5 gaps. Its results, with their hashes, are kept with the SI evidence.

**Table 6: How integrity is built today**

| Part | What happens today | Check | Item |
| --- | --- | --- | --- |
| Packages | 7 advisories in two packages, 5 High | RA V01 | PA-56 |
| Error detail | A malformed upload returns the exception message; about 29 API responses do so | H01 | PA-60 |
| Read endpoints | Bad identifiers return 404 with no detail | H02 | None |
| Injection-style input | Refused cleanly, with no server errors or database text | H03 | None |
| Upload checks | Wrong signatures, disguised executables, unknown types and paths are all rejected | H04 to H07 | None |
| Malware scan | No scanner call in the upload path | H08 | PA-58 |
| Document checksums | MD5, held in a column beside each page | H09 | PA-61 |
| Audit chain | No broken links, but only 1 of 15 records' hashes can be recomputed | H10 | PA-74 |
| Failed sign-ins | Recorded in the audit trail of the v1.0 build, which used its own passwords. Since sign-in moved to PingFederate, PingFederate records them (D-AC-23) | H11 | None |
| Alerts | Nothing raises one | H12 | PA-59 |
| Memory | .NET managed memory; the test containers run as a non-root user (C08). On the servers each application runs as a Windows service under its own account (D-PL-10) | Code review | None |

### 3.9 What \<Organisation\> provides

Controls met here: SI-2, SI-4, SI-4(2), SI-4(4), SI-5, SI-7, SI-7(1).

**Table 7: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Network monitoring and central logging | SI-4, SI-4(2), SI-4(4) | Traffic is monitored, \<System Name\>'s logs can be forwarded, and PingFederate sign-in and AD group change events reach the security officer | EV-SI-01 | Not sent |
| Firmware updates and integrity checks for the hosting | SI-2, SI-7, SI-7(1) | Firmware is kept up to date and checked | EV-SI-02 | Not sent |
| NCSC Early Warning and alert forwarding | SI-5 | \<Organisation\> is registered, and alerts that affect \<System Name\> reach the security officer | EV-SI-03 | Not sent |

**Today:** no request has been sent, and none of this is evidenced.

### 3.10 Email and spam protection

Controls met here: SI-8, SI-8(2).

\<System Name\> sends and receives no email, so it has no spam protection of its own to set or update (\<Tailoring Register\>, TR-SI-01).

### 3.11 Policy and procedures

Controls met here: SI-1.

1. **Policy.** \<Policy\> (SI) is a system-level policy. It is shared with everyone who administers or develops \<System Name\>. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (SI) holds eight procedures, PRO-SI-1 to PRO-SI-8. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control.

## Appendix A Integrity controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. SI-8 and SI-8(2) are tailored out (TR-SI-01), and SI-12(1) to SI-12(3), SI-18, SI-18(4) and SI-19 are privacy baseline controls set out in \<PII Processing Management\>. Table 8 says where the design goes some way towards them.

**Table 8: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| SI-2(5), SI-2(6) | Automatic updates; removing previous versions after an update | Not required. Done in part: updates go through change control (section 3.3) |
| SI-3(8), SI-3(10) | Detecting unauthorised commands; analysing malicious code | Not required |
| SI-4(1), SI-4(10), SI-4(11) | System-wide intrusion detection; visibility of encrypted traffic; analysis of outbound traffic | Not required. Done in part: \<Organisation\>'s network monitoring (section 3.4) |
| SI-4(12), SI-4(14), SI-4(20) | Automated organisation alerts; wireless intrusion detection; privileged user monitoring | Not required: selected at High only, or not applicable. Done in part: use cases U4 and U6 watch privileged changes and administrator sign-ins |
| SI-4(22), SI-4(23) | Unauthorised network services; host-based monitoring | Not required. Done in part: Defender on both servers |
| SI-6 Security and Privacy Function Verification | Checks that security functions work | Not required: selected at High only. Done in part: the test scripts (\<System and Services Acquisition Management\>, section 3.9) |
| SI-7(2), SI-7(5), SI-7(15) | Automated notification and response to integrity failures; code authentication | Not required: selected at High only. Done in part: signed release tags (PA-91) |
| SI-10(3) Predictable Behavior | Behaves predictably on invalid input | Not required. Done in design: invalid input is refused (H03 to H07) |
| SI-13, SI-14, SI-17, SI-20 to SI-23 | Failure prediction, non-persistence, fail-safe procedures, tainting, refresh, information diversity and fragmentation | Not required |
