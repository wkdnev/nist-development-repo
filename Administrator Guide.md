# \<System Name\> Administrator Security Guide

## 1 Purpose and how to use this guide

This guide tells administrators how to install, configure and run \<System Name\> securely, how to use and maintain its security and privacy functions, and what to watch for in its privileged functions (SA-5a). It points to the document that holds each value rather than repeating it, so it stays correct when a value changes.

Values in \[brackets\] are for the developers to fill.

## 2 Secure installation

1. Build the two Windows Server 2025 VMs to \<Organisation\>'s hardened build and the baseline in \<Configuration Management\>; turn on full-disk encryption and Microsoft Defender before \<System Name\> is installed, and deploy the App Control for Business policy in audit mode (\<Configuration Management\>, section 3.15).
2. Install the applications from a release tag only, and check the release checksums; once installed, run the integrity check of the installed files against the release record (\<Procedures\>, PRO-SI-6). Never install from a working branch. Install each application as a Windows service, under its own group managed service account.
3. Put the token signing key, the audit chain key and the OpenID Connect client credential in the key store, never in a settings file or in Git. There is no database password: only the API connects to the database, by Windows authentication under its managed service account. Its SQL Server login is not a system administrator, has rights on \<System Name\>'s database only, and cannot change the database structure.
4. Turn on TLS for every flow in \<System Description\>, section 6.5, that \<System Name\> sets up: F1 to F5, F7 and F10, and the logging, update and backup traffic in F8 where \<Organisation\>'s service allows it (time uses NTP), including the database connection (F5) and the connection to PingFederate (F10), with strict encryption and the server's certificate and name checked in full.
5. Publish the Admin application only on \<Organisation\>'s managed administration route (F2; route R3), never on every interface. Bind the API to the application server's loopback address only (F3, F4). Allow server and database administration only from the administrators' managed devices over the managed administration route, with multi-factor authentication and named accounts (F11). Set each server's host firewall to the rules in \<System and Communications Protection Management\>, section 3.2, denying everything else; set the servers' proxy settings so that only updates leave \<Organisation\>'s network, through its authenticated proxy; and set each server's trust stores to \<Organisation\>'s approved trust anchors (\<Procedures\>, PRO-SC-2).
6. Set up backups as in \<Contingency Planning Management\>, section 3.8: put the database in the full recovery model; create the backup encryption certificate and export it, with its private key, to the key store and its protected copy at the second site before the first backup; take daily encrypted backups with checksums, transaction log backups between them, and weekly backups of the system databases, all written to \<Organisation\>'s backup service.
7. Run Test-AccessControl.ps1, Test-Identification.ps1, Test-ConfigurationManagement.ps1 and Test-Protection.ps1 against the built VMs, and keep the results (\<System and Services Acquisition Management\>, section 3.9).

## 3 Secure configuration

**Table 1: Security settings**

| Setting | Where | Required value | Source |
| --- | --- | --- | --- |
| Sign-in lifetime | Each application's authentication cookie settings | Absolute lifetime of 8 hours, no sliding expiry, never longer than PingFederate's sign-in; no groups in the cookie; open pages re-check the person every 5 minutes (NFR-102). Sign out clears the cookie and calls PingFederate's sign-out (FR-084). No page lock, idle sign-out or session limit | \<Access Control Management\> |
| Sign-in | \<System Name\>'s PingFederate connection (its OpenID Connect client settings) | Password length, lockout and multi-factor authentication are set by \<Organisation\>, not in \<System Name\>. The applications use the authorisation code flow and check the nonce in each response; the client credential comes from the key store. The signed response names the person and carries no groups. The UI and Admin applications reach PingFederate for its OpenID Connect metadata and signing certificate, and to complete each sign-in, over HTTPS on TCP 443 from the application server only (F10) | \<Identification and Authentication Management\>, section 3.3 |
| Group lookup | API's directory settings | Active Directory read over LDAPS (F7, TCP 636), read-only, under the API's managed service account, with the directory's certificate checked | \<Identification and Authentication Management\> |
| Database connection | API's connection settings | Microsoft SQL Server 2022 by Windows authentication, with no password; TLS with strict encryption on TCP 1433 (F5), from the application server only | \<Identification and Authentication Management\> |
| Allowed origins | API's allowed origins | Only UI application and Admin application host names | \<System and Communications Protection Management\> |
| Token signing | API's token settings | Key from the key store, rotated as in \<System and Communications Protection Management\>; tokens issued only to the UI and Admin applications' service accounts, short-lived, each naming the signed-in person, who is taken from the token alone | \<System and Communications Protection Management\> |
| Audit | Audit settings in each application | All events in \<Audit and Accountability Management\> on | \<Audit and Accountability Management\> |
| Exports | Encrypted export working area | Copies deleted after download, and always within 24 hours | \<Media Protection Management\> |
| Browser libraries | Page templates | Recorded with their SHA-256 values in the browser library manifest, and packaged with and served by \<System Name\> itself. No content delivery service or other outside host | \<System and Communications Protection Management\> |
| Page policy | Each application's security headers | The page policy in \<System and Communications Protection Management\>, Table 6: only \<System Name\>'s own scripts, no inline scripts, no eval, no WebAssembly and no outside hosts | \<System and Communications Protection Management\> |
| Logging | Each application's logging settings | No personal data or sign-in details in the application log | \<Audit and Accountability Management\> |

Any change to these settings follows \<Procedures\> (CM), and is checked for drift monthly (\<Security Operating Procedures\>, C47).

## 4 Secure operation

**Table 2: Routine duties**

| Duty | How often | Procedure | Record |
| --- | --- | --- | --- |
| Name a schema's read and edit groups. Group members are changed only by the groups' owners, on requests authorised in ServiceNow | On request | \<Procedures\> (AC) | TPL-2, TPL-14 |
| Review group memberships and privileges | Role groups every 3 months; schema groups every 12 months, by their Data Owners | \<Procedures\> (AC) | TPL-3 |
| Give the auditors the server and database records they compare with the audit log. Auditors, not administrators, read and review the audit log | Weekly, for the auditors' review | \<Procedures\> (AU) | TPL-8 |
| Apply security updates | To the timetable in \<Risk Assessment Management\>, section 3.6 | \<Procedures\>, PRO-SI-1 | TPL-7 |
| Check for exploited flaws | Each working day, from an alert on new entries in CISA's catalogue | \<Procedures\>, PRO-RA-4 | TPL-7 |
| Test backups and restores | Backups checked weekly (C8); a restore every 6 months on the restore test server at the second site, which is erased afterwards (C18) | \<Procedures\>, PRO-CP-1 and PRO-CP-2 | TPL-8, TPL-11, TPL-13 |
| Maintenance | As needed, under an approved change; routine work under the standing change for the preventive schedule | \<Procedures\> (MA), through the managed route, signing out at the end; a supplier only watches your shared screen | TPL-12 |
| Check the export working area | Each working day (\<Security Operating Procedures\>, C49) | \<Procedures\> (MP) | TPL-8 |
| Destroy a retired backup encryption certificate, in SQL Server, the key store and its protected copy, once the last backup it encrypted is removed | When due, after each yearly renewal | \<Procedures\>, PRO-MP-3 | TPL-13 |
| Start the servers after a loss of power: \<Organisation\>'s hosting staff shut them down cleanly and tell the Windows server administrator; start the database server first, check that SQL Server recovered each database, and run the start-up checks | When power returns at either site | \<Security Operating Procedures\>, section 4.6; \<Procedures\>, PRO-PE-2 | TPL-10 |
| Report an incident to the security officer, and preserve evidence before changing anything | At once, and within 1 hour | \<Procedures\>, PRO-IR-1 and PRO-IR-6; \<Incident Response Management\> | TPL-10 |
| End every \<System Name\> sign-in at once, when the security officer asks during an incident: revoke every key in the UI and Admin applications' key rings, not only add a new key | As asked | \<Procedures\>, PRO-SC-3 and PRO-IA-3 | TPL-6 |

## 5 Security functions and how to maintain them

**Table 3: Security functions**

| Function | What it does | How to maintain it | Tested by |
| --- | --- | --- | --- |
| Sign-in | Each person's Active Directory account, through PingFederate with multi-factor authentication; the API reads their groups from Active Directory over LDAPS | Keep the PingFederate connection; never add a local account | Test-Identification.ps1 |
| Schema access | Checks the person's schema read or edit group on every page and API call; a schema with no group is closed to everyone, administrators included | Name each schema's groups only through \<Procedures\> (AC); groups' owners review members: role groups every 3 months, schema groups every 12 months, and server and database accounts every 6 months | Test-AccessControl.ps1 |
| Administrator | Manages schemas, their groups (a change only with the Data Owner's approval in a change record, which raises alert U9) and settings. Opens no item content, and can delete only an empty schema: a schema in use is deactivated, with the Data Owner's approval, and its items leave only by disposal (FR-060). This is the one administration role: there is no separate global administrator | Keep the administrators' group to the named few; review every 3 months | Test-AccessControl.ps1 |
| Other roles | Auditor, security officer, business owner and legal adviser's delegate, each given by its own role group (\<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners, \<Code\>\_LegalSearch). The system owner owns all five role groups. None of these roles holds administration | Never give an administrator one of these roles; role groups are reviewed every 3 months | Test-AccessControl.ps1 |
| Sign-in lifetime and sign-out | The authentication cookie is the session: 8 hours at most, re-checked every 5 minutes, ended by Sign out. No page lock | Keep the cookie settings in Table 1 | Test-AccessControl.ps1 |
| Audit | Records of security events, written only by the API and chained by a keyed hash (HMAC-SHA-256) | Run the chain check; keep records as in \<Policy\> (AU) | Test-AuditAndAuth.ps1 |
| Exports | Bulk exports of a schema's items, run as background jobs | Check the export working area each working day; remove copies | Test-MediaProtection.ps1 |
| Backups | Copies for recovery, encrypted under the backup encryption certificate | Keep the certificate and its retired versions apart from the backups; test restores | Test-BackupRestore.ps1 |

## 6 Privacy functions

1. **Requests from individuals:** the legal adviser's delegate, a member of \<Code\>\_LegalSearch named by the legal adviser, uses the search across all schemas (\<System Description\>, FR-073) to find every item about the person; administrators do not run this search. Record what was found and changed on TPL-15 (\<Procedures\>, PRO-PT-1).
2. **Corrections and deletions:** record each one on TPL-15.
3. **Special category data:** keep it only in schemas the business owner authorises (\<Policy\> (PT), R5).
4. **Retention:** dispose of items at the end of the period in \<PII Processing Management\>, section 3.7, only once the business owner has approved their disposal in the UI application (\<System Description\>, FR-074).
5. **Test data:** never copy real personal data to the test environment (PRO-PT-6).

## 7 Known problems with privileged functions

This section lists the known weaknesses in configuring and using privileged functions that administrators must work around until they are fixed (SA-5a.03). Each is also tracked in \<Plan of Action and Milestones\>.

**Table 4: Known problems**

| Function | Problem | What to do until fixed |
| --- | --- | --- |
| \[Function\] | \[Problem\] | \[What to do\] |

## 8 References

**Table 5: References**

| Reference | Use |
| --- | --- |
| \<System Security Plan\>; \<System Description\>, section 6 | The system, its flows and its design |
| \<Access Control Management\>, \<Audit and Accountability Management\>, \<Identification and Authentication Management\>, \<System and Communications Protection Management\>, \<Configuration Management\>, \<Media Protection Management\>, \<Contingency Planning Management\>, \<PII Processing Management\>, \<Risk Assessment Management\> | The values each setting takes |
| \<Security Operating Procedures\> | The rules administrators sign, Part B |
| \<Plan of Action and Milestones\> | The fixes this guide works around |
