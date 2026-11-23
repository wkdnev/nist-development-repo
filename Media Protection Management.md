# \<System Name\> Media Protection Management

## 1 Purpose

This document sets out how \<System Name\>'s media are protected to meet the 7 Media Protection (MP) controls in the CSS Moderate baseline.

Section 3 is the design: every place the information is held outside the running application, how each is marked, stored, moved and sanitised, the limits on portable storage, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.10 (Table 19). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (MP). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (MP), and the steps people follow are in \<Procedures\> (MP). The rules each user signs for exports, printing and copies are in \<Security Operating Procedures\>, Part A.

## 3 The design

### 3.1 Principles

Controls met here: MP-3, MP-4, MP-6.

1. **Same protection.** Every copy gets the protection of the information it holds.
2. **Know where it is.** Every place \<System Name\> information is held is listed, and copies are kept only as long as needed.
3. **Marked.** \<System Name\> information is marked \<Classification\> wherever it goes.
4. **Nothing left behind.** Media are sanitised, by an approved method, before reuse, release or disposal.

These carry out the principles and rules of \<Policy\>, sections MP.3 and MP.4.

![Figure 1: What happens to every copy](figures/mpm-figure-1.png)

**Figure 1: What happens to every copy**

### 3.2 Media inventory

Controls met here: MP-2, MP-4.

Every place \<System Name\> information is held outside the running application, with who may reach it. It includes the audit archive, the secret store, incident evidence, the document set, managed printers and the approved locations for users' copies. The system owner reviews the inventory every 12 months, and adds any new place before it is used (PRO-MP-6). \<System Name\> lets only the editors of a schema create a bulk export of it, and only auditors export the audit log (\<Access Control Management\>, section 3.9). Windows permissions limit the encrypted export working area to the API's service account, and each application's logs to its own service account and the Windows server administrator (\<Access Control Management\>, section 3.6.3). A printout is shared only with people authorised to read that schema.

**Table 1: Media inventory**

| Media | Holds | Protection | Who may reach it | Sanitising method (section 3.6) |
| --- | --- | --- | --- | --- |
| Server disks, both servers | Everything on the servers, including each application's key ring, which is not backed up | BitLocker; \<Organisation\>'s data centre | Windows server administrator; \<Organisation\>'s hosting staff | M1 |
| Database volumes | Items, their files, schema definitions and audit records | As the server disks | Database administrator; Windows server administrator | M1 |
| Encrypted export working area on the application server | Working copies of exported items | Encrypted; deleted once downloaded, and always within 24 hours | The API's service account; Windows server administrator | M5 |
| Users' managed devices | Downloads and exports | \<Organisation\>'s disk encryption and USB blocking (EV-MP-03) | The user | M4 |
| Approved locations for users' copies | Exports and downloads that users keep | \<Organisation\>'s access control and encryption for the location | The user, and those the location is shared with | M5 |
| Audit log exports | Filtered audit records that the auditor exports for a report or an investigation | Marked; kept on the auditor's managed device or in an approved location; each export is a security event that the security officer reviews (\<Audit and Accountability Management\>, section 3.8) | Auditor | M5 |
| \<Organisation\>'s managed printers | Print jobs, held until the user releases them at the printer | Secure release; \<Organisation\>'s control of the printer and its storage (EV-MP-03) | The user who printed; \<Organisation\>'s staff who maintain the printer | M4 |
| Application logs | Errors, start-up and shut-down events, and the security events | Access limited; kept 30 days | Windows server administrator | M5 |
| \<Organisation\>'s central logging | The application security events, SQL Server Audit records and Windows logs, for 12 months | \<Organisation\>'s access control for central logging (EV-AU-01) | Auditor; security officer; \<Organisation\>'s logging staff | M5 |
| Backups, through \<Organisation\>'s backup service, at both sites | Everything in the database, its transaction log backups and the system-level backups | Encrypted with AES-256 under the backup encryption certificate before they leave the database server; \<Organisation\>'s backup service copies them to the second site and keeps one copy offline or immutable (\<Contingency Planning Management\>, section 3.8) | Database administrator, who writes them; \<Organisation\>'s backup service staff, who cannot read them | M2 |
| Support copies | Data, dumps, logs or screenshots sent for support | Approved, minimised and encrypted; under UK GDPR Article 28 terms if personal data remains (\<Procedures\>, PRO-MA-7) | As approved | M5 |
| Audit archive, offline | Audit records older than 12 months, and the SQL Server Audit records, Windows logs and application security events exported from central logging after 12 months | Encrypted by the archive storage \<Organisation\> provides, held off the database server, with the SHA-256 value of each addition recorded on TPL-8 (\<Audit and Accountability Management\>, section 3.7; EV-AU-03) | Database administrator and security officer, who add to it; the auditor, on request to the system owner | M5, after 24 months and only with the system owner's recorded approval |
| Secret store, and its protected copy at the second site | The token signing key, the audit chain key, the OpenID Connect client credential and the exported backup encryption certificate, with the retired versions kept as \<Contingency Planning Management\>, section 3.8, sets. There is no database password: the API uses Windows authentication | Each secret readable only by the service account that needs it: the API's for the token signing key and the audit chain key, and the UI and Admin applications' for the OpenID Connect client credential (\<Identification and Authentication Management\>, section 3.5). The protected copy is held apart from the backups | Windows server administrator; database administrator; the system owner, for the protected copy | M5, and the secret is changed. A retired backup encryption certificate is destroyed only once the last backup it encrypted is removed (M2) |
| Incident evidence | Audit records and logs exported during an incident | Handled at \<Classification\>, with a hash and a record of custody, and held in the restricted document store or on an encrypted managed device, as TPL-10 records (\<Incident Response Management\>, section 3.10) | Auditor, for exported audit records, which only auditors read; security officer, for the logs and the rest of the evidence; the administrators | M5 |
| Physical disks and backup media | \<Organisation\>'s storage under the servers | \<Organisation\>'s data centre (EV-MP-01) | \<Organisation\>'s hosting staff | M3 |
| Test environments | Invented data only, in throwaway copies of the system | Removed after each test, with its data volumes | Developers | M5 |
| Restore test server | Real data, restored from a backup for the 6-monthly restore test | A throwaway server at the second site, built to the database server's baseline with BitLocker, no route to production, reached only by the database administrator and the security officer (\<Contingency Planning Management\>, section 3.8) | Database administrator and security officer, during the test; Windows server administrator, who builds and removes it | M1, once the test is recorded |
| The document set and assessment evidence | This document set, marked \<Classification\>, and the assessment records | The restricted document store. Until \<Organisation\>'s store is set up, the master copy and change record are the private records repository on the system owner's managed device (\<Documentation Map\>, section 4.1) | The people each document is shared with; the system owner, for the repository | M5 |
| Offline copies of the contingency plan | Section 3 and appendices A and B of \<Contingency Planning Management\>, for use when \<System Name\> and the document store are down | An encrypted managed device, or printed, marked and locked away; replaced whenever the plan changes (\<Contingency Planning Management\>, section 1.1) | System owner; security officer | M5 or M6, for the superseded copy |
| Printouts | Printed items | Marked, locked away, kept on site | People authorised to read that schema | M6 |

### 3.3 Marking scheme

Controls met here: MP-3.

All \<System Name\> information is marked \<Classification\>, \<Organisation\>'s marking (MP-3). Each item also holds its own classification, chosen from a fixed list, which is shown alongside but never lowers the \<Classification\> marking. No other handling caveat is used: who may see an item is set by its schema, not by a further marking. No media is exempt.

**Table 2: Where the marking goes**

| Output | How it is marked |
| --- | --- |
| Viewer pages | A \<Classification\> banner and watermark, with the item's classification |
| Printouts | The banner on every page, by a print style |
| Export files | \<Classification\> in the file name, and a marking notice inside |
| Downloaded files | A banner with \<Classification\> and the item's classification stamped on each page or image of the copy sent, and the marking in the file name. The stored file is never changed: its checksum is checked before the marked copy is made, and only the copy carries the stamp, so the copy's checksum differs from the stored one (FR-020; D-MP-02) |
| Audit log exports | As export files |
| Other digital media | A \<Classification\> label on the media or its record, through \<Organisation\> (EV-MP-01) |

### 3.4 Storage, export copies and users' copies

Controls met here: MP-2, MP-4.

**Table 3: Where media are stored**

| Media | Controlled area | Rule |
| --- | --- | --- |
| Server disks, volumes, backups and physical media | \<Organisation\>'s data centres, at the main and second sites | Encrypted. Reached only by the roles in section 3.2 |
| Export working copies on the application server | The encrypted working area on the application server | Deleted by \<System Name\> once downloaded, and always within 24 hours |
| Users' exports and downloads | A managed device, in the locations \<Organisation\> approves: \[approved locations\] | Kept to the minimum, and deleted once no longer needed, and within 30 days at most if they hold personal data (\<Security Operating Procedures\>) |
| Printouts | Locked storage in \<Organisation\>'s offices | Printed only on \<Organisation\>'s managed printers with secure release. Collected at once, locked away when not in use, kept on site, and shredded when no longer needed, within 30 days if they hold personal data |

### 3.5 Transport

Controls met here: MP-5.

Media are carried physically only by exception. Each move is approved by the system owner, the media are encrypted or, for paper, sealed, an authorised courier carries them with tracking, and the move is recorded on TPL-13: from and to, the sender and receiver, the protection and the courier. The receiver confirms arrival on the same record, so that the media are accounted for from release to receipt. Only \<Organisation\>'s hosting staff and its authorised courier carry media, with one exception: the holder of an approved portable storage exception carries that media themselves, encrypted, to and from the external system named in the approval, as TPL-17 records (section 3.7). A printout does not leave the site without the system owner's approval. Copies sent over the network, such as backups that \<Organisation\>'s backup service copies to the second site, are not transport in this sense: they are encrypted before they leave the database server and protected in transit (\<Contingency Planning Management\>, section 3.8). Any physical movement of backup media by \<Organisation\> follows this section (EV-MP-01).

### 3.6 Sanitising methods

Controls met here: MP-6.

Methods follow CSS and IEEE 2883-2022, with the NCSC's guidance for the UK. Each action is recorded on TPL-13, with the tool used and how the result was verified (PRO-MP-3). Every 12 months the system owner checks a sample of \<Organisation\>'s certificates against those records. Media records are kept for 3 years. That matches the training records, and covers a full authorisation cycle.

Cryptographic erase is sound only if the media were encrypted before any \<System Name\> information was written to them, and only once every copy of the key is destroyed. Both servers are therefore encrypted before \<System Name\> is installed, and the record on TPL-13 lists each copy of the key and confirms its destruction. Where either condition cannot be shown, the media are purged or destroyed instead.

A backup cannot be erased on its own by destroying its key, because one backup encryption certificate protects every backup made in its 12 months, and destroying it early would make the current backups unusable. Backups are therefore deleted when they expire, and each retired certificate is destroyed only once the last backup it encrypted has been removed, which leaves any copy that survives unreadable (\<Contingency Planning Management\>, section 3.8).

The information is rated Moderate, and the methods in Table 4 are chosen to match it: physical disks are purged or destroyed, encrypted virtual disks are erased by destroying their keys, expired backups are deleted and their retired keys destroyed, and deleting a file is used only where the storage beneath it is covered by one of those.

**Table 4: Sanitising methods by media type**

| Method | Media | How | Who | Evidence |
| --- | --- | --- | --- | --- |
| M1 | Server disks and database volumes | Cryptographic erase: destroy every copy of the BitLocker keys, including the recovery keys held in \<Organisation\>'s protected store, then \<Organisation\> deletes the volumes | Windows server administrator, \<Organisation\> | TPL-13; \<Organisation\>'s confirmation |
| M2 | Backups, transaction log backups and system-level backups | \<Organisation\>'s backup service deletes each expired copy at both sites, including the offline or immutable copy once its lock ends. Once the last backup a retired backup encryption certificate encrypted is removed, the database administrator destroys every copy of that certificate, in SQL Server, the key store and its protected copy (cryptographic erase). The storage beneath is sanitised by M3 | \<Organisation\>; database administrator | \<Organisation\>'s deletion record (EV-CP-01); TPL-13 for each certificate destroyed |
| M3 | Physical disks and backup media | Purge or destroy to IEEE 2883-2022 | \<Organisation\> | Certificate (EV-MP-02) |
| M4 | Users' managed devices and managed printers | \<Organisation\>'s device wipe before reuse or disposal | \<Organisation\> | \<Organisation\>'s record |
| M5 | Export copies, users' copies, audit log exports, logs and central logging, the audit archive, support copies, incident evidence, copies of the document set and of the contingency plan, superseded secrets and test data | Delete. The storage beneath is covered by M1 or M4, or is \<Organisation\>'s and sanitised by M3. A support copy is deleted by its receiver, who confirms it in writing (\<Procedures\>, PRO-MA-7) | Windows server administrator, database administrator, security officer, auditor, user, developers, \<Organisation\>, the receiver of a support copy | TPL-8 or TPL-13 |
| M6 | Paper | Cross-cut shred to DIN 66399 level P-4 or better | Everyone | None; bulk on TPL-13 |

### 3.7 Portable storage

Controls met here: MP-7.

\<System Name\> restricts portable storage rather than prohibiting it outright: it is blocked by default on users' devices and on both servers, and used only under an approved exception.

1. USB and other portable storage are blocked on users' devices by \<Organisation\>'s device control.
2. No USB device or other removable media is passed through to, or mounted on, either server (\<Maintenance Management\>, MA-3(2)).
3. The system owner may approve an exception on TPL-17, for a stated purpose and time, using only encrypted media issued by \<Organisation\>. That media is used only on \<Organisation\>'s managed devices and the external system named in the approval, is never connected to a personal or other unmanaged device, and is returned for sanitising when the exception ends (AC-20(2)).
4. Portable storage with no identifiable owner must not be used. It is handed to the security officer, who records it on TPL-13.

### 3.8 What \<Organisation\> provides

Controls met here: MP-2, MP-4, MP-5, MP-6, MP-7.

**Table 5: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Storage of disks and backup media | MP-2, MP-4 | They stay in its data centres, reached only by its hosting staff | EV-MP-01 |
| Transport of physical media | MP-5 | Only by exception, protected, tracked and recorded | EV-MP-01 |
| Sanitising | MP-6 | Physical disks are purged or destroyed to IEEE 2883-2022, with a certificate; virtual disks are erased when a server is removed | EV-MP-02 |
| Deleting expired backups | MP-6 | The backup service deletes each expired copy at both sites, including the offline or immutable copy, and records it | EV-CP-01 |
| Managed devices and device control | MP-4, MP-7 | Users' devices are disk-encrypted, USB storage is blocked, and no USB device is passed through to the servers | EV-MP-03, EV-AC-17 |
| Locked storage for paper | MP-4 | Lockable storage in its offices, and a cross-cut shredder | EV-MP-01 |

### 3.9 Policy and procedures

Controls met here: MP-1.

\<Policy\> (MP) and \<Procedures\> (MP) meet MP-1. Who they are shared with is in \<Policy\>, section MP.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
