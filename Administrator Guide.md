# \<System Name\> Administrator Security Guide

**\<ref\> | Version \<ver\> | Draft for the developers to confirm**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose and how to use this draft](#2-purpose-and-how-to-use-this-draft)

[3 Secure installation](#3-secure-installation)

[4 Secure configuration](#4-secure-configuration)

[5 Secure operation](#5-secure-operation)

[6 Security functions and how to maintain them](#6-security-functions-and-how-to-maintain-them)

[7 Privacy functions](#7-privacy-functions)

[8 Known problems with privileged functions](#8-known-problems-with-privileged-functions)

[9 References](#9-references)

| **SECTION 1** |
| --- |

## 1 Document control

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<System Name\> Administrator Security Guide |
| Version | \<ver\> |
| Status | Draft prepared from the document set (D-SA-17); to be confirmed against the release by the developers before version \<ver\> (PA-69) |
| Date | 11 November 2026 |
| Owner | Developers, for the system owner |
| Applies to | Global administrators, project administrators, audit administrators, the Windows server administrator and the database administrator |
| Classification | Restricted |
| Next review | At each release (\<Procedures\>, PRO-SA-4) |
| Format | \<Documentation Map\>, section 5 |

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| Prepared by | Claude, an AI assistant, for the system owner, \[Name\] | Draft \<ver\>, from the approved document set | 11 November 2026 |
| Developers | \[Name\] | Pending: confirm each fact against the release |  |
| System owner | \[Name\] | Drafts approved for confirmation (D-SA-18) | 11 November 2026 |

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | Whole-set review: the access review is of group memberships (D-AC-23). For the developers to confirm (PA-69) |
| \<ver\> | 18 November 2026 | References to the communications protection design point to \<System and Communications Protection Management\>, where it is now held (D-SC-09) |
| \<ver\> | 18 November 2026 | References to the acquisition design point to \<System and Services Acquisition Management\>, where it is now held (D-SA-19). Section 3: each application is installed as a Windows service (D-PL-10). Settings are named in plain words, not by their keys or file names. For the developers to confirm (PA-69) |
| \<ver\> | 18 November 2026 | References to the risk assessment design point to \<Risk Assessment Management\>, where it is now held (D-RA-11) |
| \<ver\> | 18 November 2026 | References to the personal data design point to \<PII Processing Management\>, where it is now held (D-PT-22) |
| \<ver\> | 17 November 2026 | The export folder is checked each working day (D-MP-10), and the check is recorded on TPL-8, as the procedure says |
| \<ver\> | 17 November 2026 | References to the media protection design point to \<Media Protection Management\>, where it is now held (D-MP-09) |
| \<ver\> | 16 November 2026 | Installation step 3 follows the decision that only the API connects to the database (D-AC-18) |
| \<ver\> | 15 November 2026 | References to the identification and authentication design point to \<Identification and Authentication Management\>, where it is now held (D-IA-11) |
| \<ver\> | 12 November 2026 | No document sends the reader to the application's code: source file, class and setting names are replaced by what they stand for, stated in plain words. No value, finding or decision is changed |
| \<ver\> | 12 November 2026 | References to the audit design point to \<Audit and Accountability Management\>, where it is now held (D-AU-10) |
| \<ver\> | 12 November 2026 | Sign-in follows D-AC-23 |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change |
| \<ver\> | 12 November 2026 | References to the access control design point to \<Access Control Management\>, where it is now held |
| \<ver\> | 12 November 2026 | References to the register, the policy and the assessment record follow their new section and table numbers (D-GEN-24) |
| \<ver\> | 12 November 2026 | Documents are cited by name in angle brackets, in place of their numbers, as the system owner asked (D-GEN-23). No other change |
| \<ver\> | 12 November 2026 | The combined documents are cited by their new numbers and chapters (D-GEN-21). The document standard is cited as \<Documentation Map\>, section 5 |
| \<ver\> | 11 November 2026 | First draft for the SA pack review (D-SA-17) |

| **SECTION 2** |
| --- |

## 2 Purpose and how to use this draft

This guide tells administrators how to install, configure and run \<System Name\> securely, how to use and maintain its security and privacy functions, and what to watch for in its privileged functions (SA-5a). It points to the approved document that holds each value rather than repeating it, so it stays correct when a value changes.

It is a draft. Values in \[brackets\] are for the developers to fill or confirm. Until version \<ver\>, administrators follow the procedures named here.

| **SECTION 3** |
| --- |

## 3 Secure installation

1. Build the two Windows Server 2025 VMs to \<Organisation\>'s hardened build and the baseline in \<Configuration Management\>; turn on full-disk encryption and Microsoft Defender before \<System Name\> is installed (PA-52, PA-58).
2. Install the applications from a release tag only, and check the release checksums (PA-61). Never install from a working branch. Install each application as a Windows service, under its own service account (D-PL-10).
3. Put the database connection string, the signing key and service secrets in the key store, never in a settings file or in Git (PA-19). Only API connects to the database, with one account that is not a superuser and cannot change the schema (D-AC-18, PA-10).
4. Turn on TLS for every flow in \<System Security Plan\>, section 4.7, including the database connection (PA-18).
5. Publish the admin portal only on \<Organisation\>'s managed administration route (route R3), never on every interface (PA-83).
6. Set up backups, encrypted, with transaction log archiving, as in \<Contingency Planning Management\> (PA-64).
7. Run Test-AccessControl.ps1, Test-Identification.ps1 and Test-ConfigurationManagement.ps1 against the built VMs, and keep the results (\<System and Services Acquisition Management\>, section 4.9).

| **SECTION 4** |
| --- |

## 4 Secure configuration

**Table 4: Security settings**

| Setting | Where | Required value | Source |
| --- | --- | --- | --- |
| Page lock and sign-out | Each application's security settings | Lock after 25 minutes; sign out after 30 | \<Access Control Management\> |
| Sign-in | The trust in \<Organisation\>'s AD FS | Password length, lockout and multi-factor authentication are set by \<Organisation\>, not in \<System Name\> (D-AC-23) | \<Policy\> (IA) |
| Allowed origins | API's allowed origins | Only UI application and Admin application host names | \<System and Communications Protection Management\> |
| Token signing | API's token settings | Key from the key store, rotated as in \<System and Communications Protection Management\> | \<System and Communications Protection Management\> |
| Audit | Audit settings in each application | All events in \<Audit and Accountability Management\> on | \<Audit and Accountability Management\> |
| Exports | Bulk export folder | Copies removed after download (PA-86) | \<Media Protection Management\> |
| Browser libraries | Page templates | Served by \<System Name\>, not a CDN (PA-34) | \<System and Communications Protection Management\> |
| Logging | Each application's logging settings | No personal data or session IDs in the application log (PA-75) | \<Audit and Accountability Management\> |

Any change to these settings follows \<Procedures\> (CM), and is checked for drift monthly (SyOps C47).

| **SECTION 5** |
| --- |

## 5 Secure operation

**Table 5: Routine duties**

| Duty | How often | Procedure | Record |
| --- | --- | --- | --- |
| Grant, change and remove access | On request | \<Procedures\> (AC) | TPL-2, TPL-14 |
| Review group memberships and privileges | Every 3 months | \<Procedures\> (AC) | TPL-3 |
| Review audit records | Weekly | \<Procedures\> (AU) | TPL-8 |
| Apply security updates | To the timetable in \<Risk Assessment Management\>, section 4.6 | \<Procedures\>, PRO-SI-1 | TPL-7 |
| Check for exploited flaws | Weekly | \<Procedures\>, PRO-RA-4 | TPL-7 |
| Test backups and restores | As in \<Contingency Planning Management\> | \<Procedures\> (CP) | TPL-11 |
| Maintenance | As needed | \<Procedures\> (MA), through the managed route | TPL-12 |
| Check the export folder | Each working day (SyOps C49) | \<Procedures\> (MP) | TPL-8 |
| Report an incident | At once | \<Incident Response Management\> | TPL-10 |

| **SECTION 6** |
| --- |

## 6 Security functions and how to maintain them

**Table 6: Security functions**

| Function | What it does | How to maintain it | Tested by |
| --- | --- | --- | --- |
| Sign-in | Each person's Active Directory account, through AD FS with multi-factor authentication | Keep the trust in AD FS; never add a local account | Test-Identification.ps1 |
| Project access | Checks the user's project role on every page and API call | Grant roles only through \<Procedures\> (AC); review every 3 months | Test-AccessControl.ps1 |
| Global administrator | Full rights across \<System Name\> | Keep holders to the named few; review every 3 months | Test-AccessControl.ps1 |
| Session control | Page lock and sign-out | Keep the timeouts in Table 4 | Test-AccessControl.ps1 |
| Audit | Hash-chained records of security events | Run the chain check; keep records as in \<Policy\> (AU) | Test-AuditAndAuth.ps1 |
| Exports | Bulk and single exports of documents | Check the export folder each working day; remove copies | Test-MediaProtection.ps1 |
| Backups | Copies for recovery | Keep encrypted; test restores | Test-BackupRestore.ps1 |

| **SECTION 7** |
| --- |

## 7 Privacy functions

1. **Requests from individuals:** search every project for the person's documents and record what was found and changed on TPL-15 (\<Procedures\>, PRO-PT-1). Until \<System Name\> can search all projects in one step, search each in turn (PA-89).
2. **Corrections and deletions:** record each one on TPL-15, as the admin portal doesn't audit them yet (PA-89).
3. **HR projects:** keep special category documents only in projects the business owner authorises (\<Policy\> (PT), R5).
4. **Retention:** dispose of documents at the end of the period in \<PII Processing Management\>, section 4.7, once retention is built (PA-70).
5. **Test data:** never copy real personal data to a test stack (PRO-PT-6).

| **SECTION 8** |
| --- |

## 8 Known problems with privileged functions

These are known weaknesses administrators must work around until they are fixed (SA-5a.03).

**Table 7: Known problems**

| Function | Problem | What to do until fixed | Item |
| --- | --- | --- | --- |
| Diagnostic and maintenance pages in the admin portal (for example database update, fresh start, schema migration, legacy clean-up and audit test pages) | Some can change the database or write audit records, and some aren't audited | Don't use them in production without a change record; \[developers to list which pages are removed for production\] | PA-29, PA-31 |
| Document delete in the admin portal | Deletes rows with no audit record; deleted pages stay until the database is vacuumed | Record each deletion on TPL-15 or TPL-6 | PA-89, PA-70 |
| Global administrator role | One role holds every right | Use a separate everyday account; reviewed every 3 months | PA-14, PA-15 |
| Admin portal network exposure | Listens on every interface in Docker | Reach it only through the managed route | PA-83 |
| Application log | Repeats usernames, IP addresses and session IDs | Treat it as audit information; limit access | PA-75 |

| **SECTION 9** |
| --- |

## 9 References

**Table 8: References**

| Reference | Use |
| --- | --- |
| \<System Security Plan\>, \<Security Architecture\> | The system, its flows and its design |
| \<Access Control Management\>, \<Audit and Accountability Management\>, \<Identification and Authentication Management\>, \<System and Communications Protection Management\>, \<Configuration Management\>, \<Media Protection Management\>, \<Contingency Planning Management\>, \<PII Processing Management\>, \<Risk Assessment Management\> | The values each setting takes |
| \<Security Operating Procedures\> | The rules administrators sign, Part B |
| \<Plan of Action and Milestones\> | The fixes this guide works around |
