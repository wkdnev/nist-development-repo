# \<System Name\> System and Information Integrity Management

## 1 Purpose

This document sets out how \<System Name\> is designed and configured to keep its software and information sound, to meet the 18 System and Information Integrity (SI) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the upload checks and malware scanning; flaw remediation and advisories; monitoring and the detection use cases; the integrity baseline and checks; error handling and memory protection; retention; what \<Organisation\> provides; email and spam protection; the policy and procedures; and the values chosen for the controls. Each subsection names the controls it helps to meet.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.18 (Table 27). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (SI). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (SI), and the steps people follow are in \<Procedures\> (SI). The vulnerability timetable is in \<Risk Assessment Management\>, section 3.6, the retention schedule in \<PII Processing Management\>, section 3.7, and the audit design in \<Audit and Accountability Management\>. The privacy controls SI-12(1) to SI-12(3), SI-18, SI-18(4) and SI-19 are set out in \<PII Processing Management\>. The values the design runs on are set out in this document, and their approvals, with SI's decisions, are in \<Decision Register\> (D-SI-01, D-SI-02, D-SI-P17 and D-SI-P27, with D-RA-P11, D-CM-P29 and D-MP-P20).

## 3 The design

### 3.1 Principles

1. **Fix flaws on time.** Every flaw is fixed to the one timetable.
2. **Check what comes in.** Every upload and input is checked on the server, and every upload is scanned before it is stored.
3. **Watch and alert.** Logs are collected, reviewed and turned into alerts.
4. **Prove nothing has changed.** Releases, stored files and audit records are checked against a known-good baseline.

These carry out the principles and rules of \<Policy\>, sections SI.3 and SI.4.

![Figure 1: How integrity is kept, from upload to alert](figures/sim-figure-1.png)

**Figure 1: How integrity is kept, from upload to alert**

### 3.2 Upload checks and malware scanning

Every upload passes these checks on the server before it is stored (SI-3, SI-10): a new item, each file in a batch, and a file that replaces a stored one (FR-037). Files are held in the SQL Server database, not as files on disk, so Defender's file scans on the database server cannot see them; the API must pass each one to Defender itself. All API inputs and search terms are validated on the server too, for type, length and range, and database queries use parameters.

**Table 1: Upload checks**

| Check | How |
| --- | --- |
| Allowed types | Only the types on the application's fixed list (reference: PDF, TIFF, JPEG and PNG); any other extension or declared type is refused |
| Type and signature | The declared type and the file's first bytes must match its extension |
| Size | Within the upload limit for the person's role (reference: 25, 50, 75 or 100 MB), and a batch within 100 files and 500 MB |
| File name | A name containing a path or invalid characters is refused |
| ZIP file of a batch | Accepted only as the container of a bulk upload (FR-041), and never stored. It is unpacked in memory, counting the files and their unpacked size as it goes, and refused as soon as either passes the batch limit. A nested archive, an encrypted entry or an entry whose name holds a path is refused. Each entry then passes every other check in this table as a file of its own |
| Malware scan | The API passes the bytes to Defender through the Windows Antimalware Scan Interface (AMSI) before storing; a flagged file is refused, audited and alerted (U3). If the scan cannot run, for example because Defender is not responding, the file is refused, so nothing unscanned is stored (NFR-052) |
| Proof | The EICAR test file, built in memory in the test environment, must be refused, alone and inside a ZIP file |

Microsoft Defender, which is signature and behaviour based, runs on both servers, with real-time protection, definitions that update automatically at least daily through \<Organisation\>'s update route, and a weekly full scan. A definition update changes no configuration item in \<Configuration Management\>, section 3.3, so it needs no change record; Defender's engine and platform updates come with the Windows updates, through change control (SI-3b). Its only exclusions are those Microsoft recommends for SQL Server's data, log and backup files, recorded in the baseline and reviewed with it. What it finds is blocked and quarantined, and the Windows server administrator and the security officer are alerted (U3; PRO-SI-2). A flagged upload is refused and recorded in the audit trail. Each false positive is recorded on the incident record with how it was resolved (PRO-SI-2, step 4). When the upload scan is first turned on, every file already stored is scanned once.

A file scanned at upload may hold malware that Defender learns to recognise only later, and the weekly scan never reaches it inside the database. So each month, and at each release, the API's file checksum check also passes every stored file to Defender through AMSI, with current definitions (D-SI-02, Neil's choice). A flagged file raises U3; the security officer handles it under PRO-SI-4, the item's file is blocked from viewing, download and export until it is resolved, and the schema's Data Owner decides what happens to the item. A file is therefore at most a month behind the latest definitions when it is downloaded or exported, and users' managed devices scan what arrives there (\<Organisation\>'s endpoint protection).

### 3.3 Flaw remediation and advisories

Flaws come from the package check, the advisories in Table 2, the scans in \<Risk Assessment Management\>, section 3.5, and tests. Each is recorded on the vulnerability and patch review and fixed or mitigated within the one timetable in \<Risk Assessment Management\>, section 3.6, counted from the fix's release, or its detection if later (PRO-SI-1). Each update is tested in the separate test environment for its effect and side effects, then installed through change control (\<Configuration Management\>, section 3.7; PRO-SI-1). A flaw in CISA's Known Exploited Vulnerabilities catalogue is fixed or mitigated within 3 days as an emergency change (PRO-RA-4). A fix that cannot meet its time goes to a risk decision with its compensating measure (PRO-RA-3, step 8). Windows, SQL Server and Defender updates are signed by Microsoft, so App Control for Business lets them run; a release that adds or changes one of \<System Name\>'s own programs updates the App Control policy in the same change (\<Configuration Management\>, section 3.15). Firmware updates for the hosts are \<Organisation\>'s (Table 6).

Update status is checked automatically, monthly and at each release, by the credentialed scan of both servers, Test-Vulnerability.ps1 for the packages and browser libraries, and the Windows Update reports from both servers, and at each build and as raised by the repositories' dependency alerts (SI-2(2)).

**Table 2: Advisory sources**

| Source | What it covers | How often |
| --- | --- | --- |
| NCSC alerts and advisories | UK threats and vulnerabilities | As published |
| NCSC Early Warning, through \<Organisation\> | Incidents, abuse and vulnerable services on \<Organisation\>'s internet-facing addresses, such as the VPN and the proxy that \<System Name\>'s updates pass through. \<System Name\> itself has no internet address (NFR-040) | As raised |
| CISA Known Exploited Vulnerabilities | Flaws being exploited | Each working day, from an alert on new entries (\<Security Operating Procedures\>) |
| Microsoft Security Response Center | Windows Server, SQL Server, .NET and ASP.NET Core | Monthly and out of band |
| GitHub advisories and dependency alerts | NuGet packages | As raised |
| Vendors of the other components | Browser libraries and any other component on the approved list | As published |

An internal advisory is a security officer's note on the vulnerability and patch review, naming the flaw, the components affected, the deadline under the timetable and who acts. The security officer passes alerts and advisories to the Windows server and database administrators and the developers, and to \<Organisation\>'s security contact when one may affect \<Organisation\>'s other systems. A directive that applies is carried out to the timetable, through change control; if it cannot be, the issuer is told (SI-5).

### 3.4 Monitoring and detection use cases

Application, Windows and SQL Server logs, including Defender's detections and the programs App Control for Business blocks, are forwarded to \<Organisation\>'s central logging \[service\] (EV-SI-01). The audit log stays in the database for the auditors; for the events that use cases U2, U5, U6, U7, U8 and U9 need, for each read or export of the audit log, and once a day for the newest audit chain hash, the API also writes a short security event to the application log (the event type, the time, the username, the schema and a count, or the hash, with no item details; \<Audit and Accountability Management\>, section 3.10), so the alerts work without the security officer reading the audit log (\<System Description\>, section 7.6). Alert rules in the central logging service analyse the events in near real time (SI-4(2)). The aim is to detect attacks, misuse and unauthorised local, network and remote connections: local connections through the Windows sign-in events on both servers, network connections through \<Organisation\>'s network monitoring, and remote connections through the VPN and administration route records.

The security officer receives the alerts and reviews the central logs weekly (PRO-SI-3), but does not read the application audit log. Auditors read it and review it weekly, compare it with the server, database, PingFederate and Active Directory records, and report anything suspicious to the security officer (\<Audit and Accountability Management\>, section 3.8). The events in Table 3 must raise an alert to the person named, who acknowledges it within the time shown (SI-4, SI-4(2), SI-4(5); PRO-SI-4). The system owner raises the level of monitoring when risk rises, such as during an incident or after a relevant advisory (PRO-SI-3, step 3). The security officer reports what monitoring found, with the alerts and their outcomes, to the system owner in the monthly measures (\<Assessment, Authorization, and Monitoring Management\>, section 3.8), and to \<Organisation\>'s security contact for any confirmed incident (SI-4g).

As users sign in through PingFederate, failed sign-ins and changes to group membership happen in \<Organisation\>'s systems, not in \<System Name\>. Use cases U1 and U4 therefore need those events, including the PingFederate sign-in logs and the Active Directory group changes, from \<Organisation\> (EV-SI-01).

**Table 3: Detection use cases**

| ID | Event | Source | Threshold | Alert to | Acknowledge within | Response |
| --- | --- | --- | --- | --- | --- | --- |
| U1 | Failed sign-ins | PingFederate sign-in logs, from \<Organisation\> | 5 for one account, or 20 in total, in 15 minutes | Security officer | 1 working day | PRO-SI-4 |
| U2 | Audit chain break | Application security event from the chain check; the auditor's weekly comparison with the daily copies | Any | Security officer, auditor | 1 hour | Incident (\<Incident Response Management\>) |
| U3 | Malware detected | Defender on either server, the AMSI scan of an upload, and the monthly rescan of stored files | Any | Security officer, Windows server administrator | 1 hour | Incident |
| U4 | Privilege change | Active Directory changes to the membership of \<System Name\>'s five role groups (\<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners and \<Code\>\_LegalSearch), from \<Organisation\>; and Windows changes to the local Administrators group on either server | Any person added | Security officer | 1 working day | Check against the approved ServiceNow request or change record; if there is none, incident |
| U5 | Bulk export | Application security event | More than \[number\] items by one user in a day; proposed reference value 200, awaiting the system owner and business owner (D-SI-P27) | Security officer | 1 working day | PRO-SI-4 |
| U6 | Administrator sign-in out of hours | Application security event: a sign-in by a person in \<Code\>\_Admins | Outside \[hours\]; proposed reference value 07:00 to 19:00 UK time, Monday to Friday except public holidays, awaiting the system owner and business owner (D-SI-P27) | Security officer | 1 working day | PRO-SI-4 |
| U7 | Audit logging failure | Application log (AU-5) | Any | Security officer, Windows server administrator | 1 hour | PRO-SI-4, and logging restored (PRO-AU-3) |
| U8 | Unexpected software change, or a changed stored file | The integrity check of the release files (PRO-SI-6); the file checksum check; a program blocked by App Control for Business | Any | Security officer, Windows server administrator | 1 hour | Incident |
| U9 | Change to which groups open a schema | Application security event, from the Admin application | Any | Security officer | 1 working day | Check against the change record approved by the schema's Data Owner; if there is none, incident |

The thresholds for U5 and U6 are set by the system owner with the business owner, from the hours of service and the expected numbers of users and items, and approved with the alert events (D-SI-P27). An alert that turns out to be an incident is then handled within the targets for its severity in \<Incident Response Management\>, section 3.6.

\<Organisation\> monitors traffic into and out of the network continuously, against the allowed flows (\<System and Communications Protection Management\>, section 3.2). Unusual or unauthorised traffic is traffic outside those flows, and, outbound, unusually large transfers (SI-4(4)). Users are monitored only after the legal adviser's opinion, only as far as needed, and with staff told what is monitored and why (SI-4f).

### 3.5 Integrity baseline and checks

The integrity baseline is the release record of the running release (\<Configuration Management\>, section 3.4). It holds the SHA-256 value of each release package and of every file the release installs on the application server, including the release scripts, which are the same hashes App Control for Business allows to run (\<Configuration Management\>, section 3.15). Table 4 names the items; the full values are kept with the release record.

**Table 4: Integrity baseline**

| Item | SHA-256 |
| --- | --- |
| API release package, and each file it installs | \[SHA-256 values, in the release record\] |
| UI application release package, and each file it installs | \[SHA-256 values, in the release record\] |
| Admin application release package, and each file it installs | \[SHA-256 values, in the release record\] |
| Shared library file (the same in all three) | \[SHA-256\] |
| Release scripts: service installation and database structure scripts | \[SHA-256 values, in the release record\] |

**Table 4a: What is checked, how and when**

| What | Tool | When (SI-7(1)) | Who |
| --- | --- | --- | --- |
| Software: the installed release files and release scripts on the application server | The integrity check compares each file's SHA-256 with the release record, and reports a missing, changed or extra file. App Control for Business also refuses to run any program not allowed by its signature or hash | At start-up of the application server, at each release once it is installed, and monthly | Windows server administrator (PRO-SI-6) |
| Information: each stored file | The API's file checksum check recomputes each file's SHA-256 and compares it with the value held on the item (FR-039), and passes the file to Defender (section 3.2). The security officer can also run it from the Admin application | Monthly and at each release, after maintenance, and after a restore (NFR-062) | Scheduled in the API; the security officer reviews the result |
| Information: the audit records | The keyed audit chain check (\<Audit and Accountability Management\>, section 3.5; PRO-AU-2) | Daily and at each start-up of the API; at each weekly review by the auditor; after a restore | Scheduled in the API; the auditor and security officer review the result |
| Firmware of the hosts beneath the two VMs | \<Organisation\>'s checks | Monthly, and at a change to the hosting | \<Organisation\> (EV-SI-02) |

A difference found by any of these raises U8, or U2 for the audit chain, and is handled as an incident (\<Incident Response Management\>; SI-7(7)): the item is restored from the release record's package, a trusted copy or a backup taken before the change (PRO-SI-6, step 4). For firmware, \<Organisation\>'s security contact is told. Settings, the App Control policy and the CIS Benchmark settings are checked for drift by \<Procedures\>, PRO-CM-7, at the same times.

Test-Integrity.ps1 is the test of these controls: it checks the upload checks, error handling, checksums, the audit chain and the alerts on a throwaway test stack built from the release (PRO-SI-8), and an assessor may run it against the VMs.

### 3.6 Error handling and memory protection

Users and API callers see a general error message, with a reference they can quote when they report it; the detail goes only to the application log, under the same reference (SI-11a). Error detail holds no password, key, token, cookie or personal data beyond the username (FR-076, NFR-023). On the servers only the Windows server administrators can read the application logs, and in central logging the auditor and the security officer (\<Audit and Accountability Management\>, section 3.10). Developers hold no administrator access on the servers, so they see the detail of a fault only as the Windows server administrator passes it to them on the fault's record (SI-11b). Memory is protected by .NET managed memory and by Windows data execution prevention and address randomisation on the servers (SI-16).

### 3.7 Information retention

Information and output are kept and disposed of under \<System Name\>'s retention schedule, which is held in \<PII Processing Management\>, section 3.7, Table 3 (SI-12). This table summarises it, with the periods that other designs set; where the two differ, the schedule is right and this table is corrected.

**Table 5: Retention**

| Information | Kept for | Source |
| --- | --- | --- |
| Items and their files | The period set for each record type, then disposed of once the business owner approves (FR-074), audited, with the database space cleared \[periods set by the business owner and legal adviser\] | \<PII Processing Management\>, Table 3, rows H1 to H5 and A1 |
| Audit records | 12 months online, then 12 months in an offline archive; the same for the SQL Server Audit records, Windows logs and application security events in central logging | \<Audit and Accountability Management\> (AU-11); row A2 |
| Application logs | 30 days on the servers, then deleted; the security events among them are kept 12 months in central logging, then archived for 12 months | \<Audit and Accountability Management\>, section 3.10; row A3 |
| Export working copies | Deleted once downloaded, and always within 24 hours | \<Media Protection Management\>; row A17 |
| Users' exports, downloads and printouts | Deleted or shredded once no longer needed, and within 30 days at most if they hold personal data | \<Media Protection Management\>; row A18 |
| Backups | 14 daily, 8 weekly and 12 monthly copies. Items deleted or disposed of stay in them until they expire, at most 12 months, beyond use, and a recovery deletes them again before users return | \<Contingency Planning Management\>, section 3.8; row A12 |
| Notifications, fault reports, and the operating, incident and request records | As rows A4 to A11 and A13 to A16 | \<PII Processing Management\>, Table 3 |

### 3.8 What \<Organisation\> provides

**Table 6: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Network monitoring and central logging | SI-4, SI-4(2), SI-4(4), SI-4(5) | Traffic is monitored, \<System Name\>'s logs can be forwarded, the alert rules in Table 3 run, and PingFederate sign-in events and Active Directory changes to the five role groups reach the security officer | EV-SI-01 |
| Firmware updates and integrity checks for the hosting | SI-2, SI-7, SI-7(1) | The hosts' firmware is tested, kept up to date and checked monthly | EV-SI-02 |
| NCSC Early Warning and alert forwarding | SI-5 | \<Organisation\> is registered for its internet-facing addresses, and alerts that affect \<System Name\> reach the security officer | EV-SI-03 |

### 3.9 Email and spam protection

\<System Name\> sends and receives no email, so it has no spam protection of its own to set or update (\<Tailoring Register\>, TR-SI-01).

### 3.10 Policy and procedures

\<Policy\> (SI) and \<Procedures\> (SI) meet SI-1. Who they are shared with is in \<Policy\>, section SI.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.

### 3.11 Values chosen for the controls

These are the organisation-defined parameters for the SI controls. The values that are \<System Description\> parameters are approved in \<Decision Register\> (D-RA-P11, D-SI-P17, D-SI-P27, D-CM-P29, D-RA-P30), and the rest with this design.

**Table 7: Values chosen**

| Control | Parameter | Value |
| --- | --- | --- |
| SI-2 | Time to install security-relevant software and firmware updates | From the fix's release or its detection if later: 3 days if exploited, 14 days Critical or High, 30 days Medium, 90 days Low |
| SI-2(2) | Mechanisms; frequency | The credentialed scan, Test-Vulnerability.ps1, the dependency alerts and the Windows Update reports; monthly and at each release, and at each build for packages (section 3.3) |
| SI-3 | Type; scan frequency; where real-time scans run; response; who is alerted | Signature and non-signature based (Defender); a full scan weekly; on both servers' endpoints, and each file as it is uploaded, with every stored file rescanned monthly and at each release; block and quarantine, refuse the upload, and block a stored file found flagged; the security officer and the Windows server administrator (U3) |
| SI-4 | Objectives; techniques; information provided, to whom and how often | Detect attacks, misuse, and unauthorised local, network and remote connections; the use cases in Table 3, the weekly review and \<Organisation\>'s network monitoring; the alerts, reviews and their outcomes, to the system owner monthly and to \<Organisation\>'s security contact for a confirmed incident |
| SI-4(4) | Frequency; unusual or unauthorised activity, inbound and outbound | Continuously; traffic outside the allowed flows in \<System and Communications Protection Management\>, section 3.2, and, outbound, unusually large transfers |
| SI-4(5) | Who is alerted; indications of compromise | As Table 3 names for each; the events U1 to U9 |
| SI-5 | Sources; who advisories go to | Table 2; the Windows server and database administrators and the developers, and \<Organisation\>'s security contact when one may affect its other systems |
| SI-7 | Software, firmware and information; actions | The release files and scripts, the hosts' firmware, the stored files and the audit records; raise U8 or U2, handle as an incident and restore from a trusted copy |
| SI-7(1) | When each is checked | Table 4a |
| SI-7(7) | Security-relevant changes handled as incidents | Any unexpected change to the release files or scripts, a stored file, an audit record or the hosts' firmware, and any program App Control for Business blocks that is not explained by an approved change |
| SI-10 | Inputs checked | Every API request's parameters and body, each upload and the files in a batch, the batch list, and search terms and filters |
| SI-11 | Who sees error detail | The Windows server administrators on the servers; the auditor and the security officer in central logging; developers only through the fault's record |
| SI-16 | Controls protecting memory | .NET managed memory, and hardware-enforced data execution prevention and address space layout randomisation on both servers, which are Windows Server 2025 defaults that the baseline keeps on |

