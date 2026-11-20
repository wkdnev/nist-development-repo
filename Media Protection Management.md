# \<System Name\> Media Protection Management

## 1 Purpose

This document shows how media that hold \<System Name\>'s information are protected, for each of the 7 Media Protection (MP) controls in the NIST SP 800-53 Rev 5 Moderate baseline. Section 3 sets out the design: every place the information is held outside the running application, how each is marked, stored, moved and sanitised, the limits on portable storage, and what \<Organisation\> provides. Section 4 takes each control in turn. Appendix A lists every value NIST asks the organisation to define, and appendix B the MP controls NIST does not select at Moderate.

This is the only place this design is held. Other documents point here. The policy is in \<Policy\> (MP), and the steps people follow are in \<Procedures\> (MP). The rules each user signs for exports, printing and copies are in \<Security Operating Procedures\>, Part A.

An assessor examines the media inventory, the marking on what the system produces, the storage and transport records, and the sanitising records and certificates; interviews users and those who handle media; and tests what an export leaves behind and whether portable storage is blocked (NIST SP 800-53A). So for each control section 4 gives:

- **each part of the control**, as NIST letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Design and today.** The Design column is how media are meant to be protected once \<System Name\> runs on the two servers at \<Organisation\>. The Today column is what was found in the build labelled v1.0, tested in the test environment on 10 November 2026, and what \<Organisation\> has evidenced, which is nothing yet.

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

## 2 Summary

Of the 7 controls, none is fully implemented, 2 are partially implemented and 5 are not implemented. No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 2: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| MP-1 | Policy and Procedures | Partially implemented | Not yet shared. The later version awaits the Head of Cyber | NC-MP-01; PA-20 |
| MP-2 | Media Access | Partially implemented | \<Organisation\>'s limits on disks and backup media are not evidenced. The rule for paper is not in use | NC-MP-02; PA-121, EV-MP-01 |
| MP-3 | Media Marking | Not implemented | Nothing \<System Name\> shows or produces is marked | NC-MP-03; PA-87 |
| MP-4 | Media Storage | Not implemented | Export copies are left unencrypted on the server. Disks are not yet encrypted. The document set is outside the restricted store | NC-MP-04; PA-26, PA-52, PA-86, PA-88, PA-121, EV-MP-01 |
| MP-5 | Media Transport | Not implemented | Transport is not evidenced, and backups are not yet encrypted | NC-MP-05; PA-64, PA-121, EV-MP-01 |
| MP-6 | Media Sanitization | Not implemented | Sanitising is not evidenced, and cryptographic erase waits on encryption | NC-MP-06; PA-52, PA-121, EV-MP-02 |
| MP-7 | Media Use | Not implemented | USB blocking is not evidenced | NC-MP-07; PA-121, EV-AC-17, EV-MP-03 |

\<System Name\> has no removable media of its own. Its information leaves the running application as exports, downloads, backups, logs and printouts, and each copy must be protected as the documents are. Two gaps are in the system itself: bulk export leaves full, unencrypted copies of documents on the server (PA-86, rated Medium), and nothing \<System Name\> shows or produces is marked (PA-87). The rest waits on \<Organisation\>, which stores, moves and sanitises the disks and backup media and controls users' devices: none of its part is evidenced (PA-121).

## 3 The design

### 3.1 Principles

1. **Same protection.** Every copy gets the protection of the information it holds.
2. **Know where it is.** Every place \<System Name\> information is held is listed, and copies are kept only as long as needed.
3. **Marked.** \<System Name\> information is marked RESTRICTED wherever it goes.
4. **Nothing left behind.** Media are sanitised, by an approved method, before reuse, release or disposal.

These carry out the principles and rules of \<Policy\>, sections MP.3 and MP.4.

![Figure 1: What happens to every copy](figures/mpm-figure-1.png)

**Figure 1: What happens to every copy**

### 3.2 Media inventory

Every place \<System Name\> information is held outside the running application, with who may reach it. The audit archive, the secret store, incident evidence and the document set were added on 17 November 2026, and confirmed by the system owner (D-MP-10). Managed printers and the approved locations for users' copies were added the same day (D-MP-11). The system owner reviews the inventory every 12 months, and adds any new place before it is used (PRO-MP-6).

**Table 3: Media inventory**

| Media | Holds | Protection | Who may reach it | Sanitising method (section 3.6) | State now |
| --- | --- | --- | --- | --- | --- |
| Server disks, both servers | Everything on the servers | BitLocker; \<Organisation\>'s data centre | Windows server administrator; \<Organisation\>'s hosting staff | M1 | Disk encryption planned (PA-52) |
| Database and key volumes | Documents, audit records and data protection keys | As the server disks | Database administrator; Windows server administrator | M1 | As the server disks |
| Export folder on the application server | Full copies of exported documents | Removed once downloaded and within 24 hours | Windows server administrator | M5 | Copies left unencrypted (P02 to P06, PA-86) |
| Users' managed devices | Downloads and exports | \<Organisation\>'s disk encryption and USB blocking | The user | M4 | Not evidenced (EV-MP-03) |
| Approved locations for users' copies | Exports and downloads that users keep | \<Organisation\>'s access control and encryption for the location | The user, and those the location is shared with | M5 | The locations are not named (PA-121) |
| \<Organisation\>'s managed printers | Print jobs, held until the user releases them at the printer | Secure release; \<Organisation\>'s control of the printer and its storage | The user who printed; \<Organisation\>'s staff who maintain the printer | M4 | Not evidenced (EV-MP-03) |
| Application logs | Personal data repeated from audit events | Access limited; kept 30 days (C46) | Windows server administrator | M5 | Personal data in logs (PA-75) |
| Backups, at the second site | Everything in the database | Encrypted before they leave (PA-64) | Database administrator; \<Organisation\>'s hosting staff | M2 | Not yet encrypted (R02, PA-64) |
| Support copies | Data, dumps, logs or screenshots sent for support | Approved, minimised and encrypted (\<Procedures\>, PRO-MA-7) | As approved | M5 | Not yet used |
| Audit archive, offline | Audit records older than 12 months | Encrypted, held off the database server, with its SHA-256 value recorded (\<Audit and Accountability Management\>) | Database administrator | M2 | Not built; where it is held is not agreed (EV-AU-03) |
| Secret store, and its copy at the second site | The database password, the signing key and the backup key | Readable only by the named administrators and the API's service account (\<Identification and Authentication Management\>, section 3.5) | Windows server administrator; database administrator | M5, and the secret is changed | Not built: the secrets are in settings files (PA-19) |
| Incident evidence | Audit records and logs exported during an incident | Handled as Restricted, with a hash and a record of custody (\<Incident Response Management\>, section 3.10) | Security officer; the administrators | M5 | Not yet used |
| Physical disks and backup media | \<Organisation\>'s storage under the servers | \<Organisation\>'s data centre | \<Organisation\>'s hosting staff | M3 | Not evidenced (EV-MP-01) |
| Test PCs | Sample data only, in throwaway Docker stacks | Removed after each test, with its data volumes | Developers | M5 | In place |
| The document set and the test evidence | This set of Restricted documents, and the test results | The restricted document store | The people each document is shared with | M5 | One copy, on the system owner's computer, outside the restricted store (PA-88) |
| Printouts | Printed documents | Marked, locked away, kept on site | People authorised to read that project | M6 | Not yet in use |

### 3.3 Marking scheme

All \<System Name\> information is marked RESTRICTED, \<Organisation\>'s marking (MP-3). Each document also holds its own classification (Public, Internal, Confidential or Restricted), which is shown alongside but never lowers the RESTRICTED marking. No other handling caveat is used: who may see a document is set by its project, not by a further marking. No media is exempt.

**Table 4: Where the marking goes**

| Output | How it is marked | State now |
| --- | --- | --- |
| Viewer pages | A RESTRICTED banner with the document's classification | Not built (PA-87) |
| Printouts | The banner on every page, by a print style; by hand until then | By hand (PRO-MP-1) |
| Export files | RESTRICTED in the file name, and a marking notice inside | Not built (PA-87); by hand until then |
| Other digital media | A RESTRICTED label on the media or its record | Through \<Organisation\> (EV-MP-01) |

### 3.4 Storage, export copies and users' copies

**Table 5: Where media are stored**

| Media | Controlled area | Rule |
| --- | --- | --- |
| Server disks, volumes, backups and physical media | \<Organisation\>'s data centres | Encrypted. Reached only by the roles in section 3.2 |
| Export copies on the application server | The application server | Removed once downloaded, and within 24 hours at most. \<System Name\> is to do this itself (PA-86) |
| Users' exports and downloads | A managed device, in the locations \<Organisation\> approves: \[approved locations\] | Kept to the minimum, and deleted within 30 days once no longer needed |
| Printouts | Locked storage in \<Organisation\>'s offices | Printed only on \<Organisation\>'s managed printers with secure release. Collected at once, locked away when not in use, kept on site, and shredded when no longer needed, within 30 days if they hold personal data |

Until \<System Name\> removes export copies itself, the Windows server administrator checks the export folder each working day and deletes anything older than 24 hours. The system owner changed the check from weekly to each working day on 17 November 2026 (D-MP-10), as a weekly check let a copy stay for up to 7 days. A copy made before a weekend can still stay until the next working day: that shortfall is part of the gap registered as PA-86.

### 3.5 Transport

Media are carried physically only by exception. Each move is approved by the system owner, the media are encrypted or, for paper, sealed, an authorised courier carries them with tracking, and the move is recorded on TPL-13. Copies sent over the network, such as backups to the second site, are not transport in this sense: they are protected in transit and must be encrypted first (\<Contingency Planning Management\>, section 3.8).

### 3.6 Sanitising methods

Methods follow NIST SP 800-88 Revision 2 and IEEE 2883-2022, with the NCSC's guidance for the UK. Each action is recorded on TPL-13 (PRO-MP-3). Every 12 months the system owner checks a sample of \<Organisation\>'s certificates against those records. Media records are kept for 3 years, as the system owner decided on 17 November 2026 (D-MP-11). That matches the training records, and covers a full authorisation cycle.

Cryptographic erase is sound only if the media were encrypted before any \<System Name\> information was written to them, and only once every copy of the key is destroyed. Both servers are therefore encrypted before \<System Name\> is installed, and the record on TPL-13 lists each copy of the key and confirms its destruction. Where either condition cannot be shown, the media are purged or destroyed instead.

**Table 6: Sanitising methods by media type**

| Method | Media | How | Who | Evidence |
| --- | --- | --- | --- | --- |
| M1 | Server disks and database and key volumes | Cryptographic erase: destroy every copy of the BitLocker keys, including the recovery keys held in \<Organisation\>'s protected store, then \<Organisation\> deletes the volumes | Windows server administrator, \<Organisation\> | TPL-13; \<Organisation\>'s confirmation |
| M2 | Backups and the audit archive | Cryptographic erase: destroy every copy of the encryption key, including the copy at the second site, then delete the copies | Database administrator | TPL-13 |
| M3 | Physical disks and backup media | Purge or destroy to IEEE 2883-2022 | \<Organisation\> | Certificate (EV-MP-02) |
| M4 | Users' managed devices and managed printers | \<Organisation\>'s device wipe before reuse or disposal | \<Organisation\> | \<Organisation\>'s record |
| M5 | Export copies, logs, support copies, incident evidence, copies of the document set, superseded secrets and test data | Delete; the disk beneath is covered by M1 or M4 | Windows server administrator, user, developers | TPL-8 or TPL-13 |
| M6 | Paper | Cross-cut shred to DIN 66399 level P-4 or better | Everyone | None; bulk on TPL-13 |

### 3.7 Portable storage

1. USB and other portable storage are blocked on users' devices by \<Organisation\>'s device control.
2. No USB device is passed through to either server.
3. The system owner may approve an exception on TPL-17, for a stated purpose and time, using only encrypted media issued by \<Organisation\>.
4. Portable storage with no identifiable owner must not be used. It is handed to the security officer, who records it on TPL-13.

### 3.8 What \<Organisation\> provides

**Table 7: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Storage of disks and backup media | MP-2, MP-4 | They stay in its data centres, reached only by its hosting staff | EV-MP-01 | Not sent |
| Transport of physical media | MP-5 | Only by exception, protected, tracked and recorded | EV-MP-01 | Not sent |
| Sanitising | MP-6 | Physical disks are purged or destroyed to IEEE 2883-2022, with a certificate; virtual disks are erased when a server is removed | EV-MP-02 | Not sent |
| Managed devices and device control | MP-4, MP-7 | Users' devices are disk-encrypted, USB storage is blocked, and no USB device is passed through to the servers | EV-MP-03, EV-AC-17 | Not sent |
| Locked storage for paper | MP-4 | Lockable storage in its offices, and a cross-cut shredder | Not yet asked | Added to EV-MP-01 |

**Today:** no request has been sent, and none of this is evidenced (PA-121).

## 4 Each control and enhancement

The controls are in NIST order. Each has two tables. The first takes each part of the control and gives what NIST requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 MP-1 Policy and Procedures

**Table 8: MP-1 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A media protection policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (MP): a system-level policy, shared with everyone who uses or administers \<System Name\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-MP-01) and legally reviewed on 10 November 2026. The later version awaits the Head of Cyber (D-MP-07). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (MP): six procedures, PRO-MP-1 to PRO-MP-6. Shared with the same people | Approved by the system owner (D-MP-08). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 10 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 9: MP-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy (\<Policy\>, section MP.4); all six procedures (\<Procedures\> (MP)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-MP-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-MP-07) |

### 4.2 MP-2 Media Access

**Table 10: MP-2 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Restrict access to defined digital and non-digital media to defined people | The inventory in section 3.2 names who may reach each kind of media. \<System Name\> lets only the editors of a project create an export of it. \<Organisation\> limits its disks and backup media to its hosting staff. A printout is shared only with people authorised to read that project | Exports were limited to editors in the tested build (P01). \<Organisation\>'s limits are not evidenced (EV-MP-01). The rule for paper is not yet in use |

**Table 11: MP-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | \<Organisation\>, administrators, everyone |
| Enforced by | \<System Name\>'s project roles, for exports; Windows permissions on the export folder and the logs; \<Organisation\>'s control of its data centres |
| Rules and procedures | Policy rules R1, R2, R6 (\<Policy\>, section MP.4); PRO-MP-1, PRO-MP-2, PRO-MP-5 (\<Procedures\> (MP)) |
| Tests | Check P01 on the v1.0 build, 10 November 2026: passed |
| Records an assessor will ask for | The inventory and its yearly review; \<Organisation\>'s statement of who can reach disks and backup media (EV-MP-01). The inventory exists |
| Status | Partially implemented |
| Risk decision | NC-MP-02, rated Low: obtain evidence |
| Open items | PA-121: obtain \<Organisation\>'s evidence, and bring the rules into use |

### 4.3 MP-3 Media Marking

**Table 12: MP-3 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Mark media to show their distribution limits, handling caveats and security markings | Everything \<System Name\> shows or produces is marked RESTRICTED, with the document's own classification alongside. Section 3.3 says where each marking goes | Not met: nothing \<System Name\> shows or produces is marked, neither the viewer, a printout nor an export file (P04, P07; PA-87). Printouts are marked by hand |
| b | Exempt defined media from marking while they stay within defined controlled areas | No media is exempt | Nothing to exempt |

**Table 13: MP-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers, everyone |
| Enforced by | \<System Name\>'s viewer, print style and export naming, once built. People, until then |
| Rules and procedures | Policy rule R3 (\<Policy\>, section MP.4); PRO-MP-1, PRO-MP-5 (\<Procedures\> (MP)) |
| Tests | Checks P04, P07 and P08 on the v1.0 build, 10 November 2026 showed the gap |
| Records an assessor will ask for | A marked viewer page, printout and export file |
| Status | Not implemented |
| Risk decision | NC-MP-03, rated Low: remediate |
| Open items | PA-87: mark the viewer, printouts and export files |

### 4.4 MP-4 Media Storage

**Table 14: MP-4 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Physically control and securely store defined media within defined controlled areas | Digital media are stored encrypted in \<Organisation\>'s data centres, or on a managed device. Printouts are locked away in \<Organisation\>'s offices. An export copy on the server is removed once downloaded, and within 24 hours at most (section 3.4) | Export copies are left unencrypted on the server after download and after a restart (P02, P05, P06, P09; PA-86). Disk encryption is planned (PA-52). \<Organisation\>'s storage is not evidenced (EV-MP-01) |
| b | Protect media until they are destroyed or sanitised with approved equipment, techniques and procedures | Each kind of media keeps the protection in section 3.2 until it is sanitised by its method in section 3.6 | An export copy can stay indefinitely if the API restarts before it is cleared (P06; PA-86). The document set is on one computer, outside the restricted store (PA-88) |

**Table 15: MP-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | \<Organisation\>, Windows server administrator, everyone |
| Enforced by | BitLocker on both servers; \<Organisation\>'s data centres and managed devices; \<System Name\>'s removal of export copies, once built |
| Rules and procedures | Policy rules R4, R5, R6 (\<Policy\>, section MP.4); PRO-MP-2, PRO-MP-5 (\<Procedures\> (MP)) |
| Tests | Checks P02, P05, P06 and P09 on the v1.0 build, 10 November 2026 showed the gap |
| Records an assessor will ask for | The encryption settings of both servers; the check of the export folder each working day, on TPL-8; \<Organisation\>'s storage arrangements (EV-MP-01) |
| Status | Not implemented |
| Risk decision | NC-MP-04, rated Medium: remediate, proposed by the system owner; awaits the authorising official |
| Open items | PA-86: remove export copies. PA-52: disk encryption. PA-26: limit where an export can be written. PA-88: the restricted store. PA-121: \<Organisation\>'s evidence |

### 4.5 MP-5 Media Transport

**Table 16: MP-5 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Protect and control defined media while they are carried outside controlled areas, by defined controls | Physical disks, backup media and printouts are moved only by exception. Digital media are encrypted and paper is sealed. Backups travel to the second site over the network, encrypted first (section 3.5) | Not yet used. Backups are not yet encrypted (R02; PA-64) |
| b | Keep accountability for the media during transport | The system owner approves each move, an authorised courier carries it with tracking, and the sender and receiver are recorded | Not yet used; \<Organisation\>'s practice is not evidenced (EV-MP-01) |
| c | Document what is done during transport | Form TPL-13: from, to, protection and courier | Not yet used |
| d | Restrict transport to authorised people | \<Organisation\>'s hosting staff and its authorised courier. A printout does not leave the site without the system owner's approval | Not evidenced (EV-MP-01) |

**Table 17: MP-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\>, system owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R7 (\<Policy\>, section MP.4); PRO-MP-2 (\<Procedures\> (MP)) |
| Tests | None |
| Records an assessor will ask for | TPL-13 records of any move; \<Organisation\>'s transport process and sample records (EV-MP-01) |
| Status | Not implemented |
| Risk decision | NC-MP-05, rated Low: obtain evidence |
| Open items | PA-64: encrypt backups. PA-121: \<Organisation\>'s evidence |

### 4.6 MP-6 Media Sanitization

**Table 18: MP-6 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Sanitise defined media before disposal, release from the organisation's control, or reuse, by defined techniques | The method for each kind of media in section 3.6, following NIST SP 800-88 Revision 2 and IEEE 2883-2022. Each action is recorded on TPL-13, with the tool used and how the result was verified | The methods are set. None has been used. \<Organisation\>'s sanitising is not evidenced (EV-MP-02). Cryptographic erase waits on encryption that is not yet on (PA-52, PA-64) |
| b | Use sanitising that is as strong and as sound as the category of the information requires | The information is rated Moderate. Physical disks are purged or destroyed. Encrypted virtual disks and backups are erased by destroying their keys. Deleting a file is used only where the disk beneath it is covered by one of those two. Paper is cross-cut shredded to DIN 66399 level P-4 or better | As part a |

**Table 19: MP-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | \<Organisation\>, administrators, everyone |
| Enforced by | Not a system function. BitLocker, for cryptographic erase |
| Rules and procedures | Policy rules R8, R9 (\<Policy\>, section MP.4); PRO-MP-3 (\<Procedures\> (MP)) |
| Tests | Check P06 on the v1.0 build, 10 November 2026, on export copies |
| Records an assessor will ask for | TPL-13 records; \<Organisation\>'s certificates (EV-MP-02); the system owner's yearly check of a sample of them. None exist yet |
| Status | Not implemented |
| Risk decision | NC-MP-06, rated Low: obtain evidence |
| Open items | PA-52: disk encryption. PA-121: \<Organisation\>'s evidence |

### 4.7 MP-7 Media Use

**Table 20: MP-7 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Restrict or prohibit the use of defined kinds of media on defined systems, by defined controls | Restricted. \<Organisation\>'s device control blocks USB and other portable storage on users' devices, and no USB device is passed through to the servers. The system owner may approve an exception, for a stated purpose and time, using only encrypted media issued by \<Organisation\> (section 3.7) | Not evidenced (EV-AC-17, EV-MP-03) |
| b | Prohibit portable storage that has no identifiable owner | It must not be used, and is handed to the security officer, who records it on TPL-13 | The rule is written. The rules of behaviour are not yet signed |

**Table 21: MP-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\>, system owner |
| Enforced by | \<Organisation\>'s device control |
| Rules and procedures | Policy rules R10, R11 (\<Policy\>, section MP.4); PRO-MP-4 (\<Procedures\> (MP)) |
| Tests | None. To be tested on a managed device (EV-MP-03) |
| Records an assessor will ask for | The device control settings (EV-MP-03); the exception register on TPL-17 |
| Status | Not implemented |
| Risk decision | NC-MP-07, rated Low: obtain evidence |
| Open items | PA-121: \<Organisation\>'s evidence |

## Appendix A Parameter register

These are NIST's organisation-defined values for the 7 MP entries: 33 in total. They were agreed on 6 November 2026 (D-MP-P01), and revised on 10 November 2026 (D-MP-P02).

**Table 22: MP parameter register**

| NIST identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| MP-01\_ODP\[01\] | Who receives the policy | Everyone who uses or administers \<System Name\> | Not yet shared (PA-20) |
| MP-01\_ODP\[02\] | Who receives the procedures | Everyone who uses or administers \<System Name\> | Not yet shared (PA-20) |
| MP-01\_ODP\[03\] | Level of the policy | System level | In place |
| MP-01\_ODP\[04\] | Official who manages them | System owner | In place |
| MP-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review due November 2027 |
| MP-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Reviewed after the MP pack review, 10 November 2026 |
| MP-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review due November 2027 |
| MP-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Reviewed after the MP pack review, 10 November 2026 |
| MP-02\_ODP\[01\] | Digital media with restricted access | The digital media in section 3.2 | Inventory written |
| MP-02\_ODP\[02\] | Who may access them | As section 3.2 says for each: the Windows server administrator, database administrator and \<Organisation\>'s hosting staff for disks, volumes and backups; editors in a project for its exports; the user for their own managed device | Exports limited to editors (P01); the rest not evidenced (EV-MP-01) |
| MP-02\_ODP\[03\] | Non-digital media with restricted access | Printed \<System Name\> documents | Not yet in use |
| MP-02\_ODP\[04\] | Who may access them | People authorised to read that project | Not yet in use |
| MP-03\_ODP\[01\] | Media exempt from marking | None | In place |
| MP-03\_ODP\[02\] | Controlled areas for exempt media | Not applicable, as none is exempt | In place |
| MP-04\_ODP\[01\] | Digital media physically controlled | The digital media in section 3.2 | Not evidenced (EV-MP-01) |
| MP-04\_ODP\[02\] | Non-digital media physically controlled | Printed \<System Name\> documents | Not yet in use |
| MP-04\_ODP\[03\] | Digital media securely stored | The digital media in section 3.2 | Export copies left unencrypted on the server (PA-86) |
| MP-04\_ODP\[04\] | Non-digital media securely stored | Printed \<System Name\> documents | Not yet in use |
| MP-04\_ODP\[05\] | Controlled areas for digital media | \<Organisation\>'s data centres, and managed devices for users' copies | Not evidenced (EV-MP-01, EV-MP-03) |
| MP-04\_ODP\[06\] | Controlled areas for non-digital media | Locked storage in \<Organisation\>'s offices | Not yet in use |
| MP-05\_ODP\[01\] | Media protected in transport | Physical disks, backup media and printouts, moved only by exception | Not yet used |
| MP-05\_ODP\[02\] | Controls that protect them | Encryption for digital media, and sealed packaging for paper | Backups not yet encrypted (PA-64) |
| MP-05\_ODP\[03\] | Controls that keep them under control | The system owner's approval, an authorised courier with tracking, and a TPL-13 record | Not yet used |
| MP-06\_ODP\[01\] | Media sanitised before disposal | All media in section 3.2, and paper | Not evidenced (EV-MP-02) |
| MP-06\_ODP\[02\] | Media sanitised before release | The digital media in section 3.2 | Not evidenced (EV-MP-02) |
| MP-06\_ODP\[03\] | Media sanitised before reuse | The digital media in section 3.2 | Not evidenced (EV-MP-02) |
| MP-06\_ODP\[04\] | Technique before disposal | The method for each media type in section 3.6, following NIST SP 800-88 Revision 2 and IEEE 2883-2022; paper cross-cut to DIN 66399 level P-4 or better | Methods set |
| MP-06\_ODP\[05\] | Technique before release | The method for each media type in section 3.6 | Methods set |
| MP-06\_ODP\[06\] | Technique before reuse | The method for each media type in section 3.6 | Methods set |
| MP-07\_ODP\[01\] | Media types limited | USB and other portable storage | Not evidenced (EV-MP-03) |
| MP-07\_ODP\[02\] | Restrict or prohibit | Restrict | In place |
| MP-07\_ODP\[03\] | Where this applies | Users' devices and both servers | Not evidenced (EV-MP-03) |
| MP-07\_ODP\[04\] | Controls used | Blocked by device control unless an exception is approved; no USB device passed through to the servers | Not evidenced (EV-AC-17, EV-MP-03) |

## Appendix B MP controls outside the Moderate baseline

NIST does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 23 says where.

**Table 23: MP controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| MP-4(2) Automated Restricted Access | Access to media storage areas restricted and logged by automated means | Not required. \<Organisation\> is asked how access to its data centres is controlled (\<Physical and Environmental Protection Management\>) |
| MP-5(3) Custodians | A named custodian for media in transport | Not required. Done in part: the system owner approves each move, and an authorised courier carries it with tracking |
| MP-6(1) Review, Approve, Track, Document, and Verify | Sanitising and disposal reviewed, approved, tracked, documented and verified | Not required. Done in part: each action is recorded on TPL-13 with its verification, and the system owner checks a sample of certificates every 12 months |
| MP-6(2) Equipment Testing | Sanitising equipment and procedures tested on a schedule | Not required. \<Organisation\> is asked how each action is verified (EV-MP-02) |
| MP-6(3) Nondestructive Techniques | Portable storage sanitised before it is first connected | Not required. Portable storage is blocked, and an exception uses only encrypted media issued by \<Organisation\> |
| MP-6(7) Dual Authorization | Two people to authorise sanitising | Not required |
| MP-6(8) Remote Purging or Wiping of Information | Devices purged or wiped from a distance | Not required. Done in part: \<Organisation\> can lock or wipe a lost managed device (\<Incident Response Management\>, section 3.9) |
| MP-7(2) Prohibit Use of Sanitization-resistant Media | Media that cannot be sanitised are not used | Not required. Every kind of media in section 3.2 has a method in section 3.6 |
| MP-8, MP-8(1) to MP-8(4) Media Downgrading | A process for lowering the classification of media | Not required. No media is downgraded: everything is RESTRICTED until sanitised |
| MP-2(1), MP-2(2), MP-4(1), MP-5(1), MP-5(2), MP-5(4), MP-6(4), MP-6(5), MP-6(6), MP-7(1) | Withdrawn by NIST | Not applicable |
