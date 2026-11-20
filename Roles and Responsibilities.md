# \<System Name\> Roles and Responsibilities

## 1 Purpose

This document is used by every control family. It is the one place that names who holds each role, so other documents refer to roles and never to people. The system owner named these holders on 5 November 2026. No person holds more than one role.

## 2 Governance roles

**Table 1: Governance roles**

| Role | Responsibility | Holder |
| --- | --- | --- |
| System owner | Owns \<System Name\> and its documents; accepts risk within their authority; chairs the change control board; keeps the plan of action up to date; invokes the contingency plan; approves equipment removal, data sent for support, and the lists of maintenance people and tools; reviews \<Organisation\>'s physical evidence against the inheritance matrix in \<Physical and Environmental Protection Management\>; keeps risk designations, signed agreements, signed rules (TPL-21 and the register of signatures) and the plan review records; decides whether a change to the rules is material; keeps the plans in the restricted store; monitors external people; gives the \<System Name\> awareness briefing to each user before their account is created (\<Awareness and Training Management\>, section 3.3) | \[Name\] |
| Head of Cyber | Senior information security officer for \<System Name\> (PM-2; confirmation pending, D-PM-03); approves all policies and the incident response plan; concurs with the SSP; confirms \<System Name\>'s risk thresholds against \<Organisation\>'s risk appetite; trains the security officer and auditor; also checks the global administrator's actions every 3 months, as an extra check | \[Name\] |
| Legal adviser | Reviews policies and the system use notice; privacy representative for changes; decides whether to tell the ICO of a breach, and makes the report; owns the privacy plan and impact assessment; confirms the lawful basis; handles requests and data protection complaints from individuals (\<Procedures\> (PT), TPL-15 and TPL-22); completes the data protection impact assessment (\<Data Protection Impact Assessment\>); gives the opinion on lawful monitoring of users (D-SI-07) | \[Name\] |
| Data protection officer | Leads \<Organisation\>'s privacy programme for \<System Name\>'s personal data (PM-19; UK GDPR, Articles 37 to 39): advises on the privacy plan and impact assessment, and is the contact for individuals and the ICO. If none is required, the legal adviser records why (D-PM-04) | \[Name, or the reason none is required\] |
| Business and information owner | Owns the information types and the business use of \<System Name\>; sets retention periods | \[Name\] |
| Authorising official | Accepts residual risk, authorises operation and approves the contingency plan | \[Name\] |
| Security assessor | Leads the independent Level 2 assessment, and confirms independence on TPL-19; inspects the data centre with TPL-20, or accepts \<Organisation\>'s auditor's inspection | \[Name\] |
| \<Organisation\> security contact | Provides evidence for inherited controls; receives incident reports and gives support | \[Name\]; deputy \[Name\] |

## 3 Operating roles

**Table 2: Operating roles**

| Role | Responsibility | Holder |
| --- | --- | --- |
| Global administrator | Manages projects, the AD groups each project uses, and sessions; ends a person's sessions when asked; issues no accounts or passwords, as \<System Name\> has none; uses the built-in maintenance pages only under an approved change, with a second person present (\<Procedures\>, PRO-MA-7) | \[Name\] |
| Administrator | Manages system settings in the admin portal | \[Name\] |
| Auditor | Reviews audit records and privileged activity | \[Name\] |
| Security officer | Reviews logs and alerts weekly and responds to each alert (\<Procedures\>, PRO-SI-4), passes on advisories from the sources in \<System and Information Integrity Management\>, section 3.3, checks CISA's exploited list weekly and drives a 3-day response, reviews scan results against the vulnerability timetable, receives vulnerability reports, leads incident response, coordinates contingency recovery, keeps its activity log and writes the after-action reports, reviews and signs the check after maintenance and reviews maintenance records monthly, assesses home working controls, writes and runs the role training modules, keeps the training register and records, and reports the training measures monthly (\<Awareness and Training Management\>), reports monthly on security status, and analyses the security impact of each change and sits on the change control board | \[Name\] |
| Project access approver | Approves who may read or edit a project | \[Name\] |
| Windows server administrator | Administers, patches and scans both VMs, runs Defender and BitLocker and tests its recovery keys yearly, sets TLS, certificates and the host firewall allow-lists, protects the data protection key rings, applies secure settings and checks monthly for drift from the baseline, holds and changes the service secrets and signing key with the database administrator, keeps the inventory and the list of maintenance tools, runs the check after maintenance, checks the export folder each working day, backs up system configuration, rebuilds the VMs in a recovery, and sits on the change control board | \[Name\] |
| Database administrator | Administers and patches PostgreSQL, requires TLS with hostssl rules, takes, encrypts, tests and restores backups, and keeps audit records for 12 months online and 12 months archived | \[Name\] |
| Developers | Build and fix the application's security functions, check its components for vulnerabilities, test each release, review the supply chain, check packages each month, bring packages in through the offline feed with lock files, produce each release's bill of materials and run Test-SupplyChain.ps1, review each other's code changes before merge and sign release tags, run the developer test plan, including Test-Protection.ps1, at each release, keep keys out of the code and the page policy strict, and complete and keep the administrator and user guides with the code | \[Name\], \[Name\], \[Name\] |

## 4 Everyone else

**Table 3: Other roles**

| Role | Responsibility |
| --- | --- |
| Document reader | Reads documents in their projects and follows the SyOPS |
| Project editor | Also uploads, exports and manages project documents |
| Line manager | Approves access requests from their people, confirming the need, and reports movers and leavers |

The permissions behind the application roles are defined in \<Access Control Management\>, sections 3.3 and 3.4.

## 5 Deputies

A deputy acts only while the holder is away, and holds the same screening, training and risk designation as the role (\<Personnel Security Management\>, section 3.2). Table 4 brings together the deputies already agreed, and shows where one is still to be named.

**Table 4: Deputies**

| Role | Deputy | Where it is recorded |
| --- | --- | --- |
| System owner | \[Name\] | D-CP-09; \<Contingency Planning Management\>, section 3.4; \<Incident Response Management\>, section 3.3 |
| Security officer | \[Name\] | \<Contingency Planning Management\>, section 3.4; \<Incident Response Management\>, section 3.3 |
| Database administrator | \[Name\] | D-CP-09; \<Contingency Planning Management\>, section 3.4 |
| Windows server administrator | \[Name\] | D-CP-09; \<Contingency Planning Management\>, section 3.4 |
| \<Organisation\> security contact | \[Name\] | Table 1 |
| Global administrator | \[Deputy to be named\] | Needed so that a person's sessions can be ended within 1 hour (\<Personnel Security Management\>, section 3.6) |
| Legal adviser | \[Deputy to be named\] | \<Incident Response Management\>, section 3.3 |
| Authorising official | None. A risk decision waits for the authorising official | \<Contingency Planning Management\>, section 3.4 |

## 6 Contact details

This is the one list of contact details for the set. Other documents name the role and point here. \<Contingency Planning Management\> and \<Incident Response Management\> keep their own lists in appendix A, because each must work when nothing else can be reached, and they are filled in from this one. Only business contact details are recorded. Items in square brackets are placeholders for the system owner to complete.

**Table 5: Contact details**

| Role | Holder | Team | Business phone, primary and alternate | Business email |
| --- | --- | --- | --- | --- |
| Authorising official | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| System owner | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Business and information owner | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Head of Cyber | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Data protection officer | \[Name, or the reason none is required\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Legal adviser | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Security officer | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Global administrator | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Windows server administrator | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Database administrator | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| Security assessor | \[Name\] | \[Team\] | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| \<Organisation\> security contact | \[Name\]; deputy \[Name\] | \<Organisation\> IT security | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
| \<Organisation\>'s IT service desk | \[Name\] | \<Organisation\> | \[Primary phone\]; \[alternate phone\] | \[Business email\] |
