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

Every place \<System Name\> information is held outside the running application, with who may reach it. It includes the audit archive, the secret store, incident evidence, the document set, managed printers and the approved locations for users' copies. The system owner reviews the inventory every 12 months, and adds any new place before it is used (PRO-MP-6). \<System Name\> lets only the editors of a schema, or an administrator, create a bulk export of it, and Windows permissions limit the encrypted export working area and the logs to the API's service account and the Windows server administrator. A printout is shared only with people authorised to read that schema.

**Table 1: Media inventory**

| Media | Holds | Protection | Who may reach it | Sanitising method (section 3.6) |
| --- | --- | --- | --- | --- |
| Server disks, both servers | Everything on the servers | BitLocker; \<Organisation\>'s data centre | Windows server administrator; \<Organisation\>'s hosting staff | M1 |
| Database volumes | Items, their files, schema definitions and audit records | As the server disks | Database administrator; Windows server administrator | M1 |
| Encrypted export working area on the application server | Working copies of exported items | Encrypted; deleted once downloaded, and always within 24 hours (P-20) | The API's service account; Windows server administrator | M5 |
| Users' managed devices | Downloads and exports | \<Organisation\>'s disk encryption and USB blocking (EV-MP-03) | The user | M4 |
| Approved locations for users' copies | Exports and downloads that users keep | \<Organisation\>'s access control and encryption for the location | The user, and those the location is shared with | M5 |
| \<Organisation\>'s managed printers | Print jobs, held until the user releases them at the printer | Secure release; \<Organisation\>'s control of the printer and its storage (EV-MP-03) | The user who printed; \<Organisation\>'s staff who maintain the printer | M4 |
| Application logs | Errors, start-up and shut-down events | Access limited; kept 30 days (C46) | Windows server administrator | M5 |
| Backups, at the second site | Everything in the database | Encrypted before they leave | Database administrator; \<Organisation\>'s hosting staff | M2 |
| Support copies | Data, dumps, logs or screenshots sent for support | Approved, minimised and encrypted (\<Procedures\>, PRO-MA-7) | As approved | M5 |
| Audit archive, offline | Audit records older than 12 months | Encrypted, held off the database server, with its SHA-256 value recorded (\<Audit and Accountability Management\>; EV-AU-03) | Database administrator | M2 |
| Secret store, and its copy at the second site | The token signing key, the audit chain key and the backup key. There is no database password: the API uses Windows authentication | Readable only by the named administrators and the API's service account (\<Identification and Authentication Management\>, section 3.5) | Windows server administrator; database administrator | M5, and the secret is changed |
| Incident evidence | Audit records and logs exported during an incident | Handled at \<Classification\>, with a hash and a record of custody (\<Incident Response Management\>, section 3.10) | Auditor, for exported audit records, which only auditors read; security officer, for the logs and the rest of the evidence; the administrators | M5 |
| Physical disks and backup media | \<Organisation\>'s storage under the servers | \<Organisation\>'s data centre (EV-MP-01) | \<Organisation\>'s hosting staff | M3 |
| Test environments | Invented data only, in throwaway copies of the system | Removed after each test, with its data volumes | Developers | M5 |
| The document set and assessment evidence | This document set, marked \<Classification\>, and the assessment records | The restricted document store | The people each document is shared with | M5 |
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
| Other digital media | A \<Classification\> label on the media or its record, through \<Organisation\> (EV-MP-01) |

### 3.4 Storage, export copies and users' copies

Controls met here: MP-2, MP-4.

**Table 3: Where media are stored**

| Media | Controlled area | Rule |
| --- | --- | --- |
| Server disks, volumes, backups and physical media | \<Organisation\>'s data centres | Encrypted. Reached only by the roles in section 3.2 |
| Export working copies on the application server | The encrypted working area on the application server | Deleted by \<System Name\> once downloaded, and always within 24 hours (P-20) |
| Users' exports and downloads | A managed device, in the locations \<Organisation\> approves: \[approved locations\] | Kept to the minimum, and deleted within 30 days once no longer needed |
| Printouts | Locked storage in \<Organisation\>'s offices | Printed only on \<Organisation\>'s managed printers with secure release. Collected at once, locked away when not in use, kept on site, and shredded when no longer needed, within 30 days if they hold personal data |

### 3.5 Transport

Controls met here: MP-5.

Media are carried physically only by exception. Each move is approved by the system owner, the media are encrypted or, for paper, sealed, an authorised courier carries them with tracking, and the move is recorded on TPL-13: from and to, the sender and receiver, the protection and the courier. Only \<Organisation\>'s hosting staff and its authorised courier carry media, and a printout does not leave the site without the system owner's approval. Copies sent over the network, such as backups to the second site, are not transport in this sense: they are protected in transit and must be encrypted first (\<Contingency Planning Management\>, section 3.8).

### 3.6 Sanitising methods

Controls met here: MP-6.

Methods follow CSS and IEEE 2883-2022, with the NCSC's guidance for the UK. Each action is recorded on TPL-13, with the tool used and how the result was verified (PRO-MP-3). Every 12 months the system owner checks a sample of \<Organisation\>'s certificates against those records. Media records are kept for 3 years. That matches the training records, and covers a full authorisation cycle.

Cryptographic erase is sound only if the media were encrypted before any \<System Name\> information was written to them, and only once every copy of the key is destroyed. Both servers are therefore encrypted before \<System Name\> is installed, and the record on TPL-13 lists each copy of the key and confirms its destruction. Where either condition cannot be shown, the media are purged or destroyed instead.

The information is rated Moderate, and the methods in Table 4 are chosen to match it: physical disks are purged or destroyed, encrypted virtual disks and backups are erased by destroying their keys, and deleting a file is used only where the disk beneath it is covered by one of those.

**Table 4: Sanitising methods by media type**

| Method | Media | How | Who | Evidence |
| --- | --- | --- | --- | --- |
| M1 | Server disks and database volumes | Cryptographic erase: destroy every copy of the BitLocker keys, including the recovery keys held in \<Organisation\>'s protected store, then \<Organisation\> deletes the volumes | Windows server administrator, \<Organisation\> | TPL-13; \<Organisation\>'s confirmation |
| M2 | Backups and the audit archive | Cryptographic erase: destroy every copy of the encryption key, including the copy at the second site, then delete the copies | Database administrator | TPL-13 |
| M3 | Physical disks and backup media | Purge or destroy to IEEE 2883-2022 | \<Organisation\> | Certificate (EV-MP-02) |
| M4 | Users' managed devices and managed printers | \<Organisation\>'s device wipe before reuse or disposal | \<Organisation\> | \<Organisation\>'s record |
| M5 | Export copies, logs, support copies, incident evidence, copies of the document set, superseded secrets and test data | Delete; the disk beneath is covered by M1 or M4 | Windows server administrator, user, developers | TPL-8 or TPL-13 |
| M6 | Paper | Cross-cut shred to DIN 66399 level P-4 or better | Everyone | None; bulk on TPL-13 |

### 3.7 Portable storage

Controls met here: MP-7.

1. USB and other portable storage are blocked on users' devices by \<Organisation\>'s device control.
2. No USB device is passed through to either server.
3. The system owner may approve an exception on TPL-17, for a stated purpose and time, using only encrypted media issued by \<Organisation\>.
4. Portable storage with no identifiable owner must not be used. It is handed to the security officer, who records it on TPL-13.

### 3.8 What \<Organisation\> provides

Controls met here: MP-2, MP-4, MP-5, MP-6, MP-7.

**Table 5: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Storage of disks and backup media | MP-2, MP-4 | They stay in its data centres, reached only by its hosting staff | EV-MP-01 |
| Transport of physical media | MP-5 | Only by exception, protected, tracked and recorded | EV-MP-01 |
| Sanitising | MP-6 | Physical disks are purged or destroyed to IEEE 2883-2022, with a certificate; virtual disks are erased when a server is removed | EV-MP-02 |
| Managed devices and device control | MP-4, MP-7 | Users' devices are disk-encrypted, USB storage is blocked, and no USB device is passed through to the servers | EV-MP-03, EV-AC-17 |
| Locked storage for paper | MP-4 | Lockable storage in its offices, and a cross-cut shredder | EV-MP-01 |

### 3.9 Policy and procedures

Controls met here: MP-1.

\<Policy\> (MP) and \<Procedures\> (MP) meet MP-1. Who they are shared with is in \<Policy\>, section MP.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
