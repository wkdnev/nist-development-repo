# \<System Name\> Administrator Security Guide

## 1 Purpose and how to use this guide

This guide tells administrators how to install, configure and run \<System Name\> securely, how to use and maintain its security and privacy functions, and what to watch for in its privileged functions (SA-5a). It points to the document that holds each value rather than repeating it, so it stays correct when a value changes.

Values in \[brackets\] are for the developers to fill.

## 2 Secure installation

1. Build the two Windows Server 2025 VMs to \<Organisation\>'s hardened build and the baseline in \<Configuration Management\>; turn on full-disk encryption and Microsoft Defender before \<System Name\> is installed.
2. Install the applications from a release tag only, and check the release checksums. Never install from a working branch. Install each application as a Windows service, under its own service account.
3. Put the database connection string, the signing key and service secrets in the key store, never in a settings file or in Git. Only API connects to the database, with one account that is not a superuser and cannot change the schema.
4. Turn on TLS for every flow in \<System Security Plan\>, section 3.7, including the database connection.
5. Publish the admin portal only on \<Organisation\>'s managed administration route (route R3), never on every interface.
6. Set up backups, encrypted, with transaction log archiving, as in \<Contingency Planning Management\>.
7. Run Test-AccessControl.ps1, Test-Identification.ps1 and Test-ConfigurationManagement.ps1 against the built VMs, and keep the results (\<System and Services Acquisition Management\>, section 3.9).

## 3 Secure configuration

**Table 1: Security settings**

| Setting | Where | Required value | Source |
| --- | --- | --- | --- |
| Sign-in lifetime | Each application's authentication cookie settings | No longer than PingFederate's sign-in lifetime (P-AC-10). \<System Name\> has no page lock, idle sign-out or session limit of its own | \<Access Control Management\> |
| Sign-in | \<System Name\>'s PingFederate connection (its OpenID Connect client settings) | Password length, lockout and multi-factor authentication are set by \<Organisation\>, not in \<System Name\> | \<Policy\> (IA) |
| Allowed origins | API's allowed origins | Only UI application and Admin application host names | \<System and Communications Protection Management\> |
| Token signing | API's token settings | Key from the key store, rotated as in \<System and Communications Protection Management\> | \<System and Communications Protection Management\> |
| Audit | Audit settings in each application | All events in \<Audit and Accountability Management\> on | \<Audit and Accountability Management\> |
| Exports | Bulk export folder | Copies removed after download | \<Media Protection Management\> |
| Browser libraries | Page templates | Served by \<System Name\>, not a CDN | \<System and Communications Protection Management\> |
| Logging | Each application's logging settings | No personal data or sign-in details in the application log | \<Audit and Accountability Management\> |

Any change to these settings follows \<Procedures\> (CM), and is checked for drift monthly (SyOps C47).

## 4 Secure operation

**Table 2: Routine duties**

| Duty | How often | Procedure | Record |
| --- | --- | --- | --- |
| Grant, change and remove access | On request | \<Procedures\> (AC) | TPL-2, TPL-14 |
| Review group memberships and privileges | Every 3 months | \<Procedures\> (AC) | TPL-3 |
| Review audit records | Weekly | \<Procedures\> (AU) | TPL-8 |
| Apply security updates | To the timetable in \<Risk Assessment Management\>, section 3.6 | \<Procedures\>, PRO-SI-1 | TPL-7 |
| Check for exploited flaws | Weekly | \<Procedures\>, PRO-RA-4 | TPL-7 |
| Test backups and restores | As in \<Contingency Planning Management\> | \<Procedures\> (CP) | TPL-11 |
| Maintenance | As needed | \<Procedures\> (MA), through the managed route | TPL-12 |
| Check the export folder | Each working day (SyOps C49) | \<Procedures\> (MP) | TPL-8 |
| Report an incident | At once | \<Incident Response Management\> | TPL-10 |

## 5 Security functions and how to maintain them

**Table 3: Security functions**

| Function | What it does | How to maintain it | Tested by |
| --- | --- | --- | --- |
| Sign-in | Each person's Active Directory account, through PingFederate with multi-factor authentication; the API reads their groups from Active Directory over LDAPS | Keep the PingFederate connection; never add a local account | Test-Identification.ps1 |
| Project access | Checks the user's project role on every page and API call | Grant roles only through \<Procedures\> (AC); review every 3 months | Test-AccessControl.ps1 |
| Global administrator | Full rights across \<System Name\> | Keep holders to the named few; review every 3 months | Test-AccessControl.ps1 |
| Sign-in lifetime | Holds the sign-in only in the authentication cookie, for no longer than PingFederate's sign-in lifetime. \<System Name\> has no page lock or sign-out of its own | Keep the cookie lifetime in Table 1 | Test-AccessControl.ps1 |
| Audit | Hash-chained records of security events | Run the chain check; keep records as in \<Policy\> (AU) | Test-AuditAndAuth.ps1 |
| Exports | Bulk and single exports of documents | Check the export folder each working day; remove copies | Test-MediaProtection.ps1 |
| Backups | Copies for recovery | Keep encrypted; test restores | Test-BackupRestore.ps1 |

## 6 Privacy functions

1. **Requests from individuals:** search every project for the person's documents and record what was found and changed on TPL-15 (\<Procedures\>, PRO-PT-1).
2. **Corrections and deletions:** record each one on TPL-15.
3. **HR projects:** keep special category documents only in projects the business owner authorises (\<Policy\> (PT), R5).
4. **Retention:** dispose of documents at the end of the period in \<PII Processing Management\>, section 3.7.
5. **Test data:** never copy real personal data to a test stack (PRO-PT-6).

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
| \<System Security Plan\>, \<Security Architecture\> | The system, its flows and its design |
| \<Access Control Management\>, \<Audit and Accountability Management\>, \<Identification and Authentication Management\>, \<System and Communications Protection Management\>, \<Configuration Management\>, \<Media Protection Management\>, \<Contingency Planning Management\>, \<PII Processing Management\>, \<Risk Assessment Management\> | The values each setting takes |
| \<Security Operating Procedures\> | The rules administrators sign, Part B |
| \<Plan of Action and Milestones\> | The fixes this guide works around |
