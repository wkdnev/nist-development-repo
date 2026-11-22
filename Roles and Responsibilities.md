# \<System Name\> Roles and Responsibilities

## 1 Purpose

This document is used by every control family. It names who holds each role, so the other documents in the set refer to roles and never to people. The system owner names the holders. No person holds more than one role.

## 2 Governance roles

**Table 1: Governance roles**

| Role | Responsibility | Holder |
| --- | --- | --- |
| System owner | Owns \<System Name\>, its design and its documents; owns the five role groups (\<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners and \<Code\>\_LegalSearch), as each group's owner, authorises each member through the ServiceNow access approval workflow and adds them to the group; prepares the role-group review for the auditor to check and sign, and, with the security officer, reviews the server and database accounts every 6 months (P-52); accepts risk within their authority; chairs the change control board; keeps the plan of action up to date; invokes the contingency plan; approves emergency maintenance, removal of equipment other than host hardware, data sent for support, and the lists of maintenance people and tools, and receives \<Organisation\>'s notice and sanitising certificate when host hardware is removed; reviews \<Organisation\>'s physical evidence against the inheritance matrix in \<Physical and Environmental Protection Management\>; keeps risk designations, signed agreements, signed rules (TPL-21 and the register of signatures) and the plan review records; decides whether a change to the rules is material; keeps the plans in the restricted store; monitors external people; gives the \<System Name\> awareness briefing to each user before they are added to any group (\<Awareness and Training Management\>, section 3.3) | \[Name\] |
| Head of Cyber | Senior information security officer for \<Organisation\> (PM-2), the role \<System Name\> relies on; approves all policies and the incident response plan; concurs with the SSP; confirms \<System Name\>'s risk thresholds against \<Organisation\>'s risk appetite; delivers training module M6 to the security officer and auditor, and M7 to the security officer; each quarter, reviews any role-group membership the system owner holds and checks the administrators' group membership and actions, signing TPL-3 for that part | \[Name\] |
| Legal adviser | Reviews policies and the system use notice; member of the change control board as its privacy representative, deciding with it on every change that touches personal data; decides whether to tell the ICO of a breach, and makes the report; owns the privacy plan and impact assessment; agrees any support copy, or supplier's view of a session, that still holds personal data, and the Article 28 terms it needs; confirms the lawful basis; handles requests and data protection complaints from individuals (\<Procedures\> (PT), TPL-15 and TPL-22); completes the data protection impact assessment (\<Data Protection Impact Assessment\>); gives the opinion on lawful monitoring of users; names the legal adviser's delegate, who is added to \<Code\>\_LegalSearch; delivers module M9 and completes module M7 within 30 days of taking the role (\<Awareness and Training Management\>, section 3.5) | \[Name\] |
| Data protection officer | Leads \<Organisation\>'s privacy programme for \<System Name\>'s personal data (PM-19; UK GDPR, Articles 37 to 39): advises on the privacy plan and impact assessment, and is the contact for individuals and the ICO. If none is required, the legal adviser records why | \[Name, or the reason none is required\] |
| Information owner | Owns the information held, its categorisation and who may see it; decides what personal data each schema holds; confirms the information types and their impact levels; takes the briefing and module M9 before their first categorisation decision (\<Awareness and Training Management\>, section 3.5) | \[Name\] |
| Business owner | Owns the business need and the requirements that are theirs to set, including P-32 to P-35; sets retention periods; authorises the schemas that may hold special category data; as a member of \<Code\>\_BusinessOwners, approves in the UI application the disposal of items due under the retention schedule (FR-074); after a recovery from an older backup, lists the items disposed of since, so that they are deleted again (\<Contingency Planning Management\>, section 3.7) | \[Name\] |
| Data Owners | Each owns one schema's data and its read and edit AD groups; as the groups' owner, authorises, through the ServiceNow access approval workflow, who may read or edit the schema; approves any change to which groups open the schema (TPL-6); and adds and removes the members of its groups; reviews those members every 12 months (P-05); decides, on TPL-25, whether the schema's information may be shared outside it, and whether exported items may be taken outside \<Organisation\>'s systems | \[Names, one for each schema\] |
| Authorising official | A senior official of \<Organisation\> with authority to accept the risk of operating \<System Name\>. Approves each assessment plan and accepts each assessor's TPL-19 before the assessment; accepts the inherited controls, and reliance on \<Organisation\>'s programme for the PM controls as one line; authorises operation on TPL-18 and accepts residual risk; receives the quarterly monitoring report; decides whether a significant change needs re-assessment or re-authorisation; approves the contingency plan; reviews and approves the SSP before it is put into effect, and approves the privacy plan with the legal adviser (D-PL-01, D-PL-02); selects the baseline and approves each tailoring entry (D-PL-03; \<Tailoring Register\>); completes module M10 within 30 days of taking the role (\<Awareness and Training Management\>, section 3.5) | \[Name\] |
| Authorising official for \<Organisation\>'s common controls | Authorises the controls \<System Name\> inherits for use (\<Assessment, Authorization, and Monitoring Management\>, section 3.5; EV-CA-01). Named by \<Organisation\> | \[Organisation common control official\] |
| Security assessor | Leads the independent Level 2 assessment, and confirms independence on TPL-19; inspects each data centre, the main site and the second site, with TPL-20, or accepts \<Organisation\>'s auditor's inspection | \[Name\] |
| \<Organisation\> security contact | Provides evidence for inherited controls; is told of every confirmed incident, receives reports and gives support | \[Name\]; deputy \[Name\] |

## 3 Operating roles

**Table 2: Operating roles**

| Role | Responsibility | Holder |
| --- | --- | --- |
| Administrator | Member of \<Code\>\_Admins, the one administrator role: there is no separate global administrator. Manages schemas, the read and edit AD groups each schema uses (a change only with the Data Owner's approval in a change record), and system settings, in the Admin application; opens no item content, and uses a separate everyday account for any item work; runs the fixed diagnostics, which read no item content. Cannot add anyone to an AD group, and issues no accounts or passwords, as \<System Name\> holds none | \[Name\] |
| Auditor | Member of \<Code\>\_Auditors. Reads, searches and exports the audit log in the Admin application, and reviews it weekly (P-08, NFR-027), including privileged activity; compares it with the server, database, PingFederate and Active Directory records, reading the Windows and SQL Server logs through \<Organisation\>'s central logging without a sign-in to the servers, and including SQL Server Audit's record of reads of the item tables by any login other than the API's; checks and signs the system owner's role-group review; records each review; and reports anything suspicious to the security officer. Holds no administration role | \[Name\] |
| Security officer | Member of \<Code\>\_Security, holding no administration role. Reads security information in the Admin application, and does not read the audit log; each month runs the last sign-in report (FR-085) and sends each group's owner the members who have not signed in for 90 days (P-38); with the system owner, reviews the server and database accounts every 6 months (P-52); reviews the alerts and the central logs weekly and responds to each alert (\<Procedures\>, PRO-SI-4), passes on advisories from the sources in \<System and Information Integrity Management\>, section 3.3, checks CISA's exploited list weekly and drives a 3-day response, reviews scan results against the vulnerability timetable, receives vulnerability reports, leads incident response, owns and updates the incident response plan and keeps the incident register, coordinates contingency recovery, keeps its activity log and writes the after-action reports, runs the sign-in, audit chain and checksum checks after maintenance, reviews and signs the check, reviews maintenance records monthly and remote maintenance logs weekly, assesses home working controls, writes the role training modules and delivers those \<Awareness and Training Management\>, Table 3 gives them, keeps the training register and records, and reports the training measures monthly (\<Awareness and Training Management\>), reports monthly on security status, receives and records any portable storage with no identifiable owner (\<Procedures\>, PRO-MP-4), and analyses the security impact of each change and sits on the change control board | \[Name\] |
| Legal adviser's delegate | Member of \<Code\>\_LegalSearch, named by the legal adviser. Searches every schema in the UI application for one person's items to answer a request under data protection law (FR-073). Holds no other role | \[Name\] |
| Windows server administrator | Administers, patches and scans both Windows Server 2025 VMs, runs Defender and BitLocker and tests its recovery keys yearly, sets TLS, certificates and the host firewall allow-lists, runs each application as a Windows service under its own group managed service account, protects the data protection key rings, applies secure settings and checks monthly for drift from the baseline, holds and changes the secrets in the key store (the token signing key, the audit chain key and, with \<Organisation\>'s PingFederate team, the OpenID Connect client credential) with the database administrator, revokes the key rings' keys when a suspected compromise needs every sign-in ended, keeps the server inventory, the approved software list, the App Control for Business policy that enforces it, and the list of maintenance tools within it, runs the check after maintenance, drives and supervises any session in which a supplier watches over a shared screen, checks the export working area each working day, backs up system configuration, rebuilds the VMs in a recovery, and sits on the change control board. Needs no application role | \[Name\] |
| Database administrator | Administers and patches SQL Server 2022; requires TLS with strict encryption and accepts connections only from the application server; gives the API's group managed service account a Windows-authenticated login, with no database password and rights on the application's database only; applies structure changes only from a release, under an approved change; does database maintenance only under an approved change or incident, runs the check after it, and drives any database session in which a supplier watches over a shared screen; takes, encrypts, tests and restores backups, and holds the backup encryption certificate, exporting it to the key store, renewing it every 12 months, and destroying every copy of a retired certificate once the last backup it encrypted is removed (\<Procedures\>, PRO-MP-3); and keeps audit records for 12 months online and 12 months archived (P-07). Needs no application role | \[Name\] |
| Developers | Build and fix the application's security functions, check its components for vulnerabilities, test each release, review the supply chain, check packages each month, bring packages in through the in-house checked package feed (the offline feed) with lock files, package every browser library with the application so that nothing is loaded from a content delivery service, produce each release's bill of materials and run Test-SupplyChain.ps1, review each other's code changes before merge and sign release tags, run the developer test plan, including Test-Protection.ps1, at each release, keep keys out of the code and the page policy strict, and complete and keep the administrator and user guides with the code; work under \<Organisation\>'s corporate SDLC, use only invented data, and hold no administrator access on the servers | \[Name\], \[Name\], \[Name\] |

## 4 Everyone else

**Table 3: Other roles**

| Role | Responsibility |
| --- | --- |
| Reader | Member of a schema's read group. Searches and reads items in their schemas, reports a faulty item, and follows the SyOPS |
| Editor | Member of a schema's edit group, which includes read. Also creates, uploads, manages and exports the schema's items |
| Line manager | Approves access requests from their people in ServiceNow, confirming the need, and reports movers and leavers; takes briefing part B7 before their first approval (\<Awareness and Training Management\>, section 3.5) |

The permissions behind the application roles are defined in \<Access Control Management\>, sections 3.3 and 3.4.

## 5 Deputies

A deputy acts only while the holder is away, and holds the same screening, training and risk designation as the role (\<Personnel Security Management\>, section 3.2). Table 4 lists the deputy for each role and where each is recorded.

**Table 4: Deputies**

| Role | Deputy | Where it is recorded |
| --- | --- | --- |
| System owner | \[Name\] | \<Contingency Planning Management\>, section 3.4; \<Incident Response Management\>, section 3.3 |
| Security officer | \[Name\] | \<Contingency Planning Management\>, section 3.4; \<Incident Response Management\>, section 3.3 |
| Database administrator | \[Name\] | \<Contingency Planning Management\>, section 3.4 |
| Windows server administrator | \[Name\] | \<Contingency Planning Management\>, section 3.4 |
| \<Organisation\> security contact | \[Name\] | Table 1 |
| Administrator | \[Deputy to be named\] | Needed so that the end of a person's access can be confirmed within 1 hour (\<Personnel Security Management\>, section 3.6) |
| Data Owner | \[Deputy to be named for each schema\] | Needed so that access requests for the schema can be authorised while the Data Owner is away |
| Legal adviser | \[Deputy to be named\] | \<Incident Response Management\>, section 3.3 |
| Authorising official | None. A risk decision waits for the authorising official | \<Contingency Planning Management\>, section 3.4 |

## 6 Contact details

This is the list of contact details for the set. Other documents name the role and point here. \<Contingency Planning Management\> and \<Incident Response Management\> keep their own lists in appendix A, because each must work when nothing else can be reached, and they are filled in from this one. Only business contact details are recorded. Items in square brackets are placeholders for the system owner to complete.

**Table 5: Contact details**

| Role | Holder | Team | Business phone, primary and alternate | Business email |
| --- | --- | --- | --- | --- |
| Authorising official | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| System owner | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Information owner | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Business owner | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Data Owners | \[Names, one for each schema\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Head of Cyber | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Data protection officer | \[Name, or the reason none is required\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Legal adviser | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Legal adviser's delegate | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Security officer | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Administrator | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Windows server administrator | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Database administrator | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Security assessor | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| \<Organisation\> security contact | \[Name\]; deputy \[Name\] | \<Organisation\> IT security | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| \<Organisation\>'s IT service desk | \[Name\] | \<Organisation\> | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
