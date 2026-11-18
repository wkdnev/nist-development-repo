# \<DocuView\> Physical and Environmental Protection Management

**\<ref\> | Version \<ver\> | Draft for the system owner's approval**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Summary](#3-summary)

[4 The design](#4-the-design)

[5 Each control and enhancement](#5-each-control-and-enhancement)

[Appendix A Parameter register](#appendix-a-parameter-register)

[Appendix B PE controls outside the Moderate baseline](#appendix-b-pe-controls-outside-the-moderate-baseline)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Physical and Environmental Protection Management |
| Version | \<ver\> |
| Status | Draft for the system owner's approval |
| Date | 17 November 2026 |
| Owner | System owner |
| Applies to | Physical and Environmental Protection family |
| Classification | Restricted |
| Next review | Every 12 months, and after a change of site |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | Neil Ramsbottom | Pending | Pending |

### 1.3 Change history

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 17 November 2026 | The system owner's decisions on the cross-check (D-PE-13): the emergency shut-down step is adopted, and every person who works from home completes the yearly checklist |
| \<ver\> | 17 November 2026 | Cross-check against NIST's guidance for the family: the home working rules name the VPN, public computers, use from abroad and lost devices, as the rules of behaviour do; every home worker completes the yearly checklist; a clear desk is part of protecting output; both data centres are inspected; what happens when a site moves to backup power is set out; the privacy control PE-8(3) is shown; and the PE controls outside the Moderate baseline are listed in a new appendix B |
| \<ver\> | 17 November 2026 | The system owner's decisions on the review (D-PE-12): no \<DocuView\> role enters a data centre; the emergency shutoff must be guarded; ABC Technologies tells the security officer of a physical incident within 24 hours; and a SOC 2 report must cover the availability criteria |
| \<ver\> | 17 November 2026 | Issued into the set as a draft for review |
| \<ver\> | 17 November 2026 | First draft, at the system owner's request (D-PE-11). The physical and environmental protection chapter of \<Control Implementation Register\> moved here in full, so that this design is held only in this document, and each control is set out part by part. The inheritance matrix names four more ISO/IEC 27001 controls as closing evidence, and a SOC 2 report is asked to cover the availability criteria as well as physical access. No agreed value is changed |

| **SECTION 2** |
| --- |

## 2 Purpose

This document shows how the places where \<DocuView\> runs and is used are protected, for each of the 18 Physical and Environmental Protection (PE) controls and enhancements in the NIST SP 800-53 Rev 5 Moderate baseline. Section 4 sets out the design: the sites, who provides each control, how ABC Technologies' evidence is obtained and checked, the rules for offices and for working from home, physical incidents, and the encryption that stands behind the physical controls. Section 5 takes each control in turn. Appendix A lists every value NIST asks the organisation to define, and appendix B the PE controls NIST does not select at Moderate.

This is the only place this design is held. Other documents point here. The policy is in \<Policy\> (PE), and the steps people follow are in \<Procedures\> (PE).

\<DocuView\> has no premises of its own. It runs on two virtual servers in ABC Technologies' data centre, with backups and recovery at a second site, so 15 of the 18 controls are provided wholly by ABC Technologies. \<DocuView\>'s own part is small: how its users treat screens and printouts, how they work from home, how physical incidents are handled, and the encryption of the server disks.

An assessor examines the provider's evidence for each inherited control, and the organisation's check of it; inspects the site; and interviews those who work in the offices and from home (NIST SP 800-53A). So for each control section 5 gives:

- **each part of the control**, as NIST letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Design and today.** For an inherited control, the Design column is what \<DocuView\> requires of ABC Technologies at both sites. The values were agreed as requirements on 10 November 2026 (D-PE-P02). The Today column is what ABC Technologies has evidenced, which is nothing yet: no evidence request has been sent, and no site has been visited.

**Table 4: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet, or it is not evidenced |

| **SECTION 3** |
| --- |

## 3 Summary

Of the 18 controls, none is fully implemented, 1 is partially implemented and 17 are not implemented. No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 5: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| PE-1 | Policy and Procedures | Partially implemented | Not yet shared. The later version awaits the Head of Cyber | NC-PE-01; PA-20 |
| PE-2 | Physical Access Authorizations | Not implemented | ABC Technologies' evidence, for either site | NC-PE-02; PA-122, EV-PE-01 |
| PE-3 | Physical Access Control | Not implemented | ABC Technologies' evidence, for either site | NC-PE-03; PA-122, EV-PE-01 |
| PE-4 | Access Control for Transmission | Not implemented | ABC Technologies' evidence, for either site | NC-PE-04; PA-122, EV-PE-01 |
| PE-5 | Access Control for Output Devices | Not implemented | The managed printers are not listed or evidenced | NC-PE-05; PA-122, EV-PE-05 |
| PE-6 | Monitoring Physical Access | Not implemented | ABC Technologies' evidence, for either site | NC-PE-06; PA-122, EV-PE-01 |
| PE-6(1) | Intrusion Alarms and Surveillance Equipment | Not implemented | ABC Technologies' evidence, for either site | NC-PE-07; PA-122, EV-PE-01 |
| PE-8 | Visitor Access Records | Not implemented | ABC Technologies' evidence, for either site | NC-PE-08; PA-122, EV-PE-01 |
| PE-9 | Power Equipment and Cabling | Not implemented | ABC Technologies' evidence, for either site | NC-PE-09; PA-122, EV-PE-02 |
| PE-10 | Emergency Shutoff | Not implemented | ABC Technologies' evidence, for either site | NC-PE-10; PA-122, EV-PE-02 |
| PE-11 | Emergency Power | Not implemented | ABC Technologies' evidence, for either site | NC-PE-11; PA-122, EV-PE-02 |
| PE-12 | Emergency Lighting | Not implemented | ABC Technologies' evidence, for either site | NC-PE-12; PA-122, EV-PE-02 |
| PE-13 | Fire Protection | Not implemented | ABC Technologies' evidence, for either site | NC-PE-13; PA-122, EV-PE-03 |
| PE-13(1) | Detection Systems, Automatic Activation and Notification | Not implemented | ABC Technologies' evidence, for either site | NC-PE-14; PA-122, EV-PE-03 |
| PE-14 | Environmental Controls | Not implemented | ABC Technologies' evidence, for either site | NC-PE-15; PA-122, EV-PE-03 |
| PE-15 | Water Damage Protection | Not implemented | ABC Technologies' evidence, for either site | NC-PE-16; PA-122, EV-PE-03 |
| PE-16 | Delivery and Removal | Not implemented | ABC Technologies' evidence, for either site | NC-PE-17; PA-122, EV-PE-04 |
| PE-17 | Alternate Work Site | Not implemented | The yearly check has not been held, and ABC Technologies' controls are not evidenced | NC-PE-18; PA-122, EV-PE-05 |

One PE control from the privacy baseline is assessed with the PT family: PE-8(3), which limits the personal data in visitor records to the name, the organisation, and the date and time of the visit (NC-PT-12; PA-122).

This family rests almost wholly on ABC Technologies, and none of its part is evidenced. The two data centres are not yet named, no evidence request has been sent, and no site has been inspected (PA-122). Until the evidence arrives, a physical control does not count. The one protection in \<DocuView\>'s own hands is the encryption of the server disks, so that reaching a host does not expose the documents: that is planned and not yet in place (PA-52).

| **SECTION 4** |
| --- |

## 4 The design

### 4.1 Principles

1. **Inherit with evidence.** A physical control counts only once ABC Technologies has evidenced it.
2. **Same protection everywhere.** The second site meets the same requirements as the main one.
3. **Protect what users see.** Screens and printouts are protected by the people who use them.
4. **Report physical events.** Physical incidents are handled as security incidents.

These carry out the principles and rules of \<Policy\>, sections PE.3 and PE.4.

### 4.2 Sites and contacts

![Figure 1: Where \<DocuView\> is, and who protects each place](figures/pem-figure-1.png)

**Figure 1: Where \<DocuView\> is, and who protects each place**

**Table 6: Sites**

| Site | Use | Location | ABC Technologies contact | Evidence |
| --- | --- | --- | --- | --- |
| Data centre | Hosts both servers | \[Data centre name and address\] | \[Facilities contact\] | EV-PE-01 to EV-PE-04 |
| Second site | Holds backups; used for recovery (\<Contingency Planning Management\>, section 4.9) | \[Second site name and address\] | \[Facilities contact\] | EV-PE-01 to EV-PE-04; PA-66 |
| Offices | Where \<DocuView\> is used and printed | \[ABC Technologies offices\] | \[Office security contact\] | EV-PE-05 |
| Homes | Remote working | Employees' homes | Security officer | C30, TPL-4 |

No \<DocuView\> role needs to enter either data centre, as the system owner confirmed on 17 November 2026 (D-PE-12). The Windows server and database administrators work over ABC Technologies' managed route (\<Maintenance Management\>, section 4.4), and the hardware beneath the servers is maintained by ABC Technologies' engineers.

### 4.3 Who provides each control

Who provides each PE control, and the evidence that closes it. The first choice of evidence is ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability, with the Annex A control shown, for both sites. A SOC 2 report serves instead if it covers physical access (criterion CC6.4) and, for power, fire, environment and water, the availability criteria (A1.2), as the system owner decided on 17 November 2026 (D-PE-12). The site inspection (TPL-20) adds what was seen.

**Table 7: PE inheritance matrix**

| Control | ABC Technologies provides | \<DocuView\> provides | Closing evidence | State now |
| --- | --- | --- | --- | --- |
| PE-1 | Its own physical security policy | The policy, the procedures and this document | Approved documents | Approved; not yet shared |
| PE-2 | Authorised access list for the data centres | Nothing | A.7.2; access list review record | Not evidenced (EV-PE-01) |
| PE-3 | Entry control, logs, visitors, keys and cards | Nothing | A.7.1, A.7.2, A.7.3; TPL-20 | Not evidenced (EV-PE-01) |
| PE-4 | Protected cabling | Nothing | A.7.12 | Not evidenced (EV-PE-01) |
| PE-5 | Managed printers with secure release; office security | Screen lock after 25 minutes; users' rules (A33, A36, A37) | A.7.7; EV-PE-05; AC-11 tests | Printers not yet listed |
| PE-6, PE-6(1) | Monitoring, alarms and CCTV; log review | Incident handling of what is reported | A.7.4; monitoring records | Not evidenced (EV-PE-01) |
| PE-8 | Visitor records and review | Nothing | A.7.2; sample records | Not evidenced (EV-PE-01) |
| PE-9, PE-10, PE-11, PE-12 | Power protection, emergency shutoff, UPS and emergency lighting | Orderly shutdown on UPS (\<Security Operating Procedures\>, section 5.6) | A.7.11, A.7.12; maintenance records | Not evidenced (EV-PE-02) |
| PE-13, PE-13(1) | Fire detection and suppression, with automatic notification | Nothing | A.7.5; fire safety records | Not evidenced (EV-PE-03) |
| PE-14 | Temperature and humidity control and monitoring | Nothing | A.7.5, A.7.8; monitoring records | Not evidenced (EV-PE-03) |
| PE-15 | Water damage protection | Nothing | A.7.5 | Not evidenced (EV-PE-03) |
| PE-16 | Control of deliveries and removals | Approves removal of \<DocuView\> equipment (\<Procedures\>, PRO-MA-2) | A.7.2, A.7.10; sample records | Not evidenced (EV-PE-04) |
| PE-17 | Managed devices and route | Home working rules and the yearly check | A.6.7, A.7.9; EV-PE-05; TPL-4 | Not yet assessed |
| Compensating | Nothing | Server disk encryption, so physical access to hosts does not expose data (PA-52) | Encryption settings on the servers | Planned (PA-52) |

### 4.4 How the evidence is obtained and checked

**Table 8: Steps of the evidence check**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 | ABC Technologies is asked for its certificate, Statement of Applicability and latest audit findings, or its SOC 2 report, for both sites | System owner | \<Evidence Requests\>, EV-PE-01 |
| 2 | Where those do not cover a control, the facility evidence is asked for | System owner | EV-PE-01 to EV-PE-05 |
| 3 | What is received is recorded against each control in the matrix, and each value in appendix A is confirmed as met | System owner | Section 4.3; appendix A |
| 4 | Each data centre, the main site and the second site, is inspected once, at Level 2, by the independent assessor, or by ABC Technologies' auditor if the assessor cannot visit | Independent assessor | TPL-20 |
| 5 | Any shortfall is raised as a risk | System owner | \<Risk List\> |
| 6 | The check is repeated every 12 months, and after a change of site or a significant incident at a site | System owner | Section 4.3 |

The system owner decided on 6 November 2026 that the organisation does not assess the sites itself, and inherits their protection by evidence (D-PE-05). The single inspection at Level 2 was added on 10 November 2026 (D-PE-08).

### 4.5 Offices: screens and printing

1. \<DocuView\> documents are printed only on ABC Technologies' managed printers with secure release: \[managed printers\]. A page prints only when its owner is at the printer.
2. A printout is collected at once, marked RESTRICTED, locked away when not in use, and shredded when no longer needed (\<Media Protection Management\>, section 4.4).
3. A screen is locked when its user leaves it, and placed so that others cannot read it.
4. \<DocuView\> locks the page after 25 minutes idle (\<Access Control Management\>, section 4.7).
5. Desks are kept clear of printed documents and notes.

### 4.6 Working from home

1. People work remotely only from home, unless the system owner has approved another place in writing.
2. They use only ABC Technologies' managed device, and connect to its VPN before opening \<DocuView\>. They never use a public or shared computer, and use public Wi-Fi only with the VPN connected first.
3. They work where others in the home cannot see the screen, and do not print \<DocuView\> documents at home unless the system owner has approved it.
4. They do not use \<DocuView\> from outside the UK, or take a device that can reach it abroad, without written approval from the system owner and the security officer.
5. They report any concern or incident to the security officer at once, and a lost or stolen device within 1 hour.
6. Every 12 months the security officer puts a short checklist to every person who works from home: the managed device, the VPN, screen privacy, no printing, and reporting. The answers are recorded on TPL-4. The system owner decided on 17 November 2026 that every person completes it, and not a sample (D-PE-13).

These are rules A35 to A42 of the rules of behaviour, which each person signs (\<Security Operating Procedures\>, Part A).

### 4.7 Physical incidents

The loss or theft of a device or printout, unauthorised entry to a data centre, and fire, flood or power loss affecting \<DocuView\> are security incidents. Whoever sees one reports it to the security officer at once. ABC Technologies' security contact tells the security officer of any physical incident at a site that affects \<DocuView\>, within 24 hours. The security officer handles it with the playbooks for a lost device or printout and for intrusion, fire, flood or power loss at a data centre (\<Incident Response Management\>, section 4.9), and the contingency plan is invoked if a site is lost (\<Contingency Planning Management\>).

**Loss of power.** When a data centre moves to backup power, ABC Technologies warns the Windows server administrator. The administrators then shut both servers down in order, before the backup power runs out (\<Security Operating Procedures\>, section 5.6), and record it as a physical incident. The system owner adopted this step on 17 November 2026 (D-PE-13). How long the backup power lasts, and how the warning is given, are asked of ABC Technologies (EV-PE-02).

### 4.8 Encryption behind the physical controls

Both servers' disks are encrypted, and backups are encrypted before they leave the database server. Someone who reaches a host, a disk or a backup copy therefore cannot read \<DocuView\>'s documents. This does not replace ABC Technologies' physical controls: it limits the harm if one fails. Today it is planned and not in place (PA-52, PA-64).

### 4.9 What ABC Technologies provides

**Table 9: Asked of ABC Technologies**

| Request | Controls | What is asked | State |
| --- | --- | --- | --- |
| EV-PE-01 | PE-2, PE-3, PE-4, PE-6, PE-6(1), PE-8 | Who can enter each data centre, how entry is controlled and logged, how visitors, keys and cabling are managed, how access is monitored, and how incidents reach \<DocuView\>'s security officer. Its certificate or report, for both sites | Not sent |
| EV-PE-02 | PE-9, PE-10, PE-11, PE-12 | How power is protected, the emergency shutoff, backup power for an orderly shutdown, and emergency lighting | Not sent |
| EV-PE-03 | PE-13, PE-13(1), PE-14, PE-15 | Fire detection and suppression and who they notify, temperature and humidity and how they are monitored, and protection from water | Not sent |
| EV-PE-04 | PE-16 | How hardware and media are authorised and recorded when entering or leaving | Not sent |
| EV-PE-05 | PE-5, PE-17 | Office controls for printers and screens, which managed printers have secure release, and the controls on managed devices and the route at home | Not sent |

**Today:** no request has been sent, the sites and the facilities contacts are not named, and none of this is evidenced (PA-122).

| **SECTION 5** |
| --- |

## 5 Each control and enhancement

The controls are in NIST order. Each has two tables. The first takes each part of the control and gives what NIST requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 5.1 PE-1 Policy and Procedures

**Table 10: PE-1 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A physical and environmental protection policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (PE): a system-level policy, shared with everyone who uses or administers \<DocuView\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-PE-01) and legally reviewed on 10 November 2026. The later version awaits the Head of Cyber (D-PE-09). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (PE): five procedures, PRO-PE-1 to PRO-PE-5. Shared with the same people | Approved by the system owner (D-PE-10). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | Neil Ramsbottom is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or change of site | Reviewed on 10 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 11: PE-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy (\<Policy\>, section PE.4); all five procedures (\<Procedures\> (PE)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-PE-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-PE-09) |

### 5.2 PE-2 Physical Access Authorizations

**Table 12: PE-2 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Keep an approved list of the people authorised to enter the facility where the system is | ABC Technologies keeps the list for each data centre. No \<DocuView\> role needs to enter one: every administrator works remotely (\<Maintenance Management\>, section 4.4) | Not evidenced (EV-PE-01) |
| b | Issue credentials for entry | An individual card or credential for each person on the list | Not evidenced (EV-PE-01) |
| c | Review the list on a schedule | Every 12 months | Not evidenced (EV-PE-01) |
| d | Remove people from the list when they no longer need access | When the need ends, and when someone leaves | Not evidenced (EV-PE-01) |

**Table 13: PE-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The access list and the record of its last review; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.2, or its SOC 2 report (EV-PE-01). None received |
| Status | Not implemented |
| Risk decision | NC-PE-02, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-01), and name the sites |

### 5.3 PE-3 Physical Access Control

**Table 14: PE-3 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Enforce the authorisations at defined entry and exit points, by checking each person and by controlling the way in and out | At every data centre entrance and exit, by ABC Technologies' electronic access control system, with individual cards or credentials | Not evidenced (EV-PE-01) |
| b | Keep entry logs for defined points | For every data centre entrance and exit | Not evidenced (EV-PE-01) |
| c | Control access to areas that are open to the public | A staffed reception, with visitors signed in | Not evidenced (EV-PE-01) |
| d | Escort visitors and control what they do | Always | Not evidenced (EV-PE-01) |
| e | Secure keys, combinations and other entry devices | Held securely by ABC Technologies' facilities staff | Not evidenced (EV-PE-01) |
| f | Inventory the entry devices on a schedule | Keys, cards and combinations, every 12 months | Not evidenced (EV-PE-01) |
| g | Change combinations and keys on a schedule, and when one is lost or compromised or someone leaves | Every 12 months; a combination when someone who knows it leaves; a key when it is lost or not returned | Not evidenced (EV-PE-01) |

**Table 15: PE-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Sample entry logs; the inventory of keys and cards; the site inspection record (TPL-20); ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.1, A.7.2 and A.7.3, or its SOC 2 report (EV-PE-01). None received |
| Status | Not implemented |
| Risk decision | NC-PE-03, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-01), and name the sites |

### 5.4 PE-4 Access Control for Transmission

**Table 16: PE-4 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Control physical access to defined distribution and transmission lines | Power and network cabling in each data centre is kept in locked rooms, cabinets and cable trays | Not evidenced (EV-PE-01) |

**Table 17: PE-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The site inspection record (TPL-20); ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.12, or its SOC 2 report (EV-PE-01). None received |
| Status | Not implemented |
| Risk decision | NC-PE-04, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-01), and name the sites |

### 5.5 PE-5 Access Control for Output Devices

**Table 18: PE-5 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Control physical access to the output of defined devices, so that nobody unauthorised obtains it | Printers: \<DocuView\> documents are printed only on ABC Technologies' managed printers with secure release, so that a page prints only when its owner is at the printer, and are collected at once. Screens and desks: a screen is locked when left and placed so that others cannot read it, and desks are kept clear of printed documents. \<DocuView\> also locks the page after 25 minutes idle (section 4.5) | The printers are not listed or evidenced (EV-PE-05). The page lock worked in the tested build, under AC-11 (\<Access Control Management\>) |

**Table 19: PE-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | ABC Technologies, everyone |
| Enforced by | ABC Technologies' managed printers; \<DocuView\>'s page lock; the rules of behaviour |
| Rules and procedures | Policy rules R6, R7 (\<Policy\>, section PE.4); PRO-PE-3 (\<Procedures\> (PE)) |
| Tests | None for PE. The page lock was tested under AC-11 |
| Records an assessor will ask for | The list of managed printers with secure release; ABC Technologies' office security rules, or its certificate showing A.7.7 (EV-PE-05) |
| Status | Not implemented |
| Risk decision | NC-PE-05, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-05), and list the printers |

### 5.6 PE-6 Monitoring Physical Access

**Table 20: PE-6 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Monitor physical access to the facility, to detect and respond to physical security incidents | ABC Technologies monitors each data centre and responds to alarms | Not evidenced (EV-PE-01) |
| b | Review the entry logs on a schedule and after defined events | Monthly, and after a physical security incident or alarm | Not evidenced (EV-PE-01) |
| c | Share the results of reviews and investigations with the incident response capability | ABC Technologies' security contact tells \<DocuView\>'s security officer of any physical incident that affects \<DocuView\> within 24 hours (D-PE-12), and the security officer handles it under the incident response plan (section 4.7) | Not evidenced (EV-PE-01). The playbook is written (\<Incident Response Management\>, section 4.9) |

**Table 21: PE-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5, R9 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-2, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Monitoring records; the record of the monthly log review; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.4, or its SOC 2 report (EV-PE-01). None received |
| Status | Not implemented |
| Risk decision | NC-PE-06, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-01), and name the sites |

### 5.7 PE-6(1) Intrusion Alarms and Surveillance Equipment

**Table 22: PE-6(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Monitor physical access with intrusion alarms and surveillance equipment | Intrusion alarms and CCTV at each data centre | Not evidenced (EV-PE-01) |

**Table 23: PE-6(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The site inspection record (TPL-20); ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.4, or its SOC 2 report (EV-PE-01). None received |
| Status | Not implemented |
| Risk decision | NC-PE-07, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-01), and name the sites |

### 5.8 PE-8 Visitor Access Records

**Table 24: PE-8 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Keep visitor records for a defined time | 12 months | Not evidenced (EV-PE-01) |
| b | Review them on a schedule | Monthly | Not evidenced (EV-PE-01) |
| c | Report anomalies to defined people | To ABC Technologies' security contact, who tells \<DocuView\>'s security officer | Not evidenced (EV-PE-01) |

**Table 25: PE-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Sample visitor records, and the record of a monthly review; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.2, or its SOC 2 report (EV-PE-01). None received |
| Status | Not implemented |
| Risk decision | NC-PE-08, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-01), and name the sites |

### 5.9 PE-9 Power Equipment and Cabling

**Table 26: PE-9 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Protect power equipment and power cabling from damage and destruction | ABC Technologies protects the power equipment and cabling that serve the hosts, at both sites | Not evidenced (EV-PE-02) |

**Table 27: PE-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | A description of the power arrangements; maintenance records; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.11 and A.7.12, or its SOC 2 report (EV-PE-02). None received |
| Status | Not implemented |
| Risk decision | NC-PE-09, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-02), and name the sites |

### 5.10 PE-10 Emergency Shutoff

**Table 28: PE-10 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Be able to shut off power to defined components in an emergency | To the hosting equipment for both servers | Not evidenced (EV-PE-02) |
| b | Place the shutoff switches where authorised people can reach them | Near the exits of the data centre room | Not evidenced (EV-PE-02) |
| c | Protect the shutoff from being used without authority | Guarded against accidental and unauthorised use, as the system owner required on 17 November 2026 (D-PE-12). ABC Technologies is asked how | Not evidenced (EV-PE-02) |

**Table 29: PE-10 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The site inspection record (TPL-20); ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.11, or its SOC 2 report (EV-PE-02). None received |
| Status | Not implemented |
| Risk decision | NC-PE-10, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-02), and name the sites |

### 5.11 PE-11 Emergency Power

**Table 30: PE-11 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Provide an uninterruptible power supply that allows an orderly shutdown, or a move to long-term backup power, when the main power fails | Enough backup power for an orderly shutdown of both servers. ABC Technologies warns the administrators when a site is on backup power, and they shut the servers down in order (section 4.7; \<Security Operating Procedures\>, section 5.6) | Not evidenced (EV-PE-02). How long the backup power lasts and how the warning is given are not known |

**Table 31: PE-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The backup power arrangements and their test records; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.11, or its SOC 2 report (EV-PE-02). None received |
| Status | Not implemented |
| Risk decision | NC-PE-11, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-02), and name the sites |

### 5.12 PE-12 Emergency Lighting

**Table 32: PE-12 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Have automatic emergency lighting that comes on in a power failure and covers emergency exits and evacuation routes | In each data centre | Not evidenced (EV-PE-02) |

**Table 33: PE-12 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The site inspection record (TPL-20); maintenance records; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.11, or its SOC 2 report (EV-PE-02). None received |
| Status | Not implemented |
| Risk decision | NC-PE-12, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-02), and name the sites |

### 5.13 PE-13 Fire Protection

**Table 34: PE-13 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Have fire detection and suppression systems, with an independent energy source | In each data centre | Not evidenced (EV-PE-03) |

**Table 35: PE-13 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Fire safety and maintenance records; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.5, or its SOC 2 report (EV-PE-03). None received |
| Status | Not implemented |
| Risk decision | NC-PE-13, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-03), and name the sites |

### 5.14 PE-13(1) Detection Systems, Automatic Activation and Notification

**Table 36: PE-13(1) design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Fire detection that works automatically and notifies defined people and emergency responders | It notifies ABC Technologies' facilities staff and the fire and rescue service | Not evidenced (EV-PE-03) |

**Table 37: PE-13(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Fire safety records showing who is notified; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.5, or its SOC 2 report (EV-PE-03). None received |
| Status | Not implemented |
| Risk decision | NC-PE-14, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-03), and name the sites |

### 5.15 PE-14 Environmental Controls

**Table 38: PE-14 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Keep defined environmental levels within defined limits | Temperature and humidity, within the ASHRAE TC 9.9 recommended envelope: 18 to 27°C, a dew point from -9 to 15°C, and at most 60% relative humidity | Not evidenced (EV-PE-03) |
| b | Monitor them on a schedule | Continuously | Not evidenced (EV-PE-03) |

**Table 39: PE-14 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Monitoring records for temperature and humidity; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.5 and A.7.8, or its SOC 2 report (EV-PE-03). None received |
| Status | Not implemented |
| Risk decision | NC-PE-15, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-03), and name the sites |

### 5.16 PE-15 Water Damage Protection

**Table 40: PE-15 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Protect the system from water leaks with master shutoff or isolation valves that can be reached, work, and are known to key people | In each data centre | Not evidenced (EV-PE-03) |

**Table 41: PE-15 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | The site inspection record (TPL-20); ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.5, or its SOC 2 report (EV-PE-03). None received |
| Status | Not implemented |
| Risk decision | NC-PE-16, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-03), and name the sites |

### 5.17 PE-16 Delivery and Removal

**Table 42: PE-16 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Authorise and control defined items entering and leaving the facility | Hardware and media that hold \<DocuView\> information. The system owner approves the removal of anything of \<DocuView\>'s (\<Maintenance Management\>, section 4.7) | Not evidenced (EV-PE-04) |
| b | Keep records of those items | ABC Technologies' delivery and removal records; \<DocuView\>'s own on TPL-12 and TPL-13 | Not evidenced (EV-PE-04). The forms exist; none is used yet |

**Table 43: PE-16 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | ABC Technologies' facilities and staff, at both sites |
| Rules and procedures | Policy rules R1 to R5 (\<Policy\>, section PE.4); PRO-PE-1, PRO-PE-5 (\<Procedures\> (PE)) |
| Tests | None. The site is inspected once, at Level 2 (TPL-20) |
| Records an assessor will ask for | Sample delivery and removal records; ABC Technologies' ISO/IEC 27001 certificate and Statement of Applicability showing A.7.2 and A.7.10, or its SOC 2 report (EV-PE-04). None received |
| Status | Not implemented |
| Risk decision | NC-PE-17, rated Low: obtain evidence |
| Open items | PA-122: obtain ABC Technologies' evidence (EV-PE-04), and name the sites |

### 5.18 PE-17 Alternate Work Site

**Table 44: PE-17 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Decide and record which alternate work sites are allowed | Employees' homes, and any other place the system owner approves in writing | In place: stated in the rules of behaviour (\<Security Operating Procedures\>, rule A38). The rules are not yet signed |
| b | Use defined controls at those sites | ABC Technologies' managed device, with its VPN connected first; no public or shared computer; a screen that others in the home cannot see; no printing at home unless approved (section 4.6) | Not evidenced (EV-PE-05) |
| c | Assess how well those controls work | Every 12 months the security officer puts a short checklist to every person who works from home, and records the answers on TPL-4 | Not yet held |
| d | Give employees a way to reach security and privacy staff when there is an incident | The contacts in \<Security Operating Procedures\>, section 7 | The people are named. Their contact details are placeholders |

**Table 45: PE-17 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Security officer, ABC Technologies |
| Enforced by | ABC Technologies' managed devices and route; the rules of behaviour |
| Rules and procedures | Policy rule R8 (\<Policy\>, section PE.4); PRO-PE-4 (\<Procedures\> (PE)) |
| Tests | None |
| Records an assessor will ask for | The yearly checklist on TPL-4; ABC Technologies' remote working policy, or its certificate showing A.6.7 and A.7.9 (EV-PE-05) |
| Status | Not implemented |
| Risk decision | NC-PE-18, rated Low: approve |
| Open items | PA-122: hold the first yearly check, and obtain ABC Technologies' evidence (EV-PE-05) |

| **APPENDIX A** |
| --- |

## Appendix A Parameter register

These are NIST's organisation-defined values for the 18 PE entries: 40 in total. They apply to the data centre and the second site alike. They were agreed on 6 November 2026 (D-PE-P01, D-PE-07) and restated as requirements on 10 November 2026 (D-PE-P02). ABC Technologies must confirm it meets them at both sites.

**Table 46: PE parameter register**

| NIST identifier | What must be defined | Value (requirement) | State now |
| --- | --- | --- | --- |
| PE-01\_ODP\[01\] | Who receives the policy | Everyone who uses or administers \<DocuView\> | Not yet shared (PA-20) |
| PE-01\_ODP\[02\] | Who receives the procedures | Everyone who uses or administers \<DocuView\> | Not yet shared (PA-20) |
| PE-01\_ODP\[03\] | Level of the policy | System level | In place |
| PE-01\_ODP\[04\] | Official who manages them | System owner | In place |
| PE-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review due November 2027 |
| PE-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or change of site | Reviewed after the PE pack review, 10 November 2026 |
| PE-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review due November 2027 |
| PE-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Reviewed after the PE pack review, 10 November 2026 |
| PE-02\_ODP | Access list review frequency | Every 12 months | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[01\] | Entry and exit points | Data centre entrances and exits | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[02\] | How entry is controlled | Electronic access control with individual cards or credentials | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[03\] | Systems or devices used | ABC Technologies' physical access control system | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[04\] | Points with access logs | Data centre entrances and exits | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[05\] | Controls on publicly accessible areas | Staffed reception, with visitors signed in | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[06\] | When visitors are escorted and monitored | Always | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[07\] | Physical access devices inventoried | Keys, cards and combinations | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[08\] | Inventory frequency | Every 12 months | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[09\] | Combination change frequency | Every 12 months, and when someone with the combination leaves | Not evidenced (EV-PE-01) |
| PE-03\_ODP\[10\] | Key change frequency | Every 12 months, and when a key is lost or someone leaves without returning it | Not evidenced (EV-PE-01) |
| PE-04\_ODP\[01\] | Lines protected | Power and network cabling in the data centre | Not evidenced (EV-PE-01) |
| PE-04\_ODP\[02\] | Controls used | Locked rooms, cabinets and cable trays | Not evidenced (EV-PE-01) |
| PE-05\_ODP | Output devices | ABC Technologies' managed printers with secure release, and screens used for \<DocuView\> | Printers not yet listed (EV-PE-05) |
| PE-06\_ODP\[01\] | Log review frequency | Monthly | Not evidenced (EV-PE-01) |
| PE-06\_ODP\[02\] | Events requiring log review | A physical security incident or alarm | Not evidenced (EV-PE-01) |
| PE-08\_ODP\[01\] | How long visitor records are kept | 12 months | Not evidenced (EV-PE-01) |
| PE-08\_ODP\[02\] | Visitor record review frequency | Monthly | Not evidenced (EV-PE-01) |
| PE-08\_ODP\[03\] | Who anomalies go to | ABC Technologies' security contact, who tells the security officer | Not evidenced (EV-PE-01) |
| PE-10\_ODP\[01\] | What can be shut off | Hosting equipment for both servers | Not evidenced (EV-PE-02) |
| PE-10\_ODP\[02\] | Where the switches are | Near the data centre room exits | Not evidenced (EV-PE-02) |
| PE-11\_ODP | What the backup power allows | An orderly shutdown of both servers | Not evidenced (EV-PE-02) |
| PE-13(01)\_ODP\[01\] | Who fire detection notifies | ABC Technologies' facilities staff | Not evidenced (EV-PE-03) |
| PE-13(01)\_ODP\[02\] | Emergency responders notified | The fire and rescue service | Not evidenced (EV-PE-03) |
| PE-14\_ODP\[01\] | Levels kept | Temperature and humidity | Not evidenced (EV-PE-03) |
| PE-14\_ODP\[02\] | Controls used | Data centre cooling and humidity control | Not evidenced (EV-PE-03) |
| PE-14\_ODP\[03\] | Acceptable levels | The ASHRAE TC 9.9 recommended envelope: 18 to 27°C, dew point from -9 to 15°C and at most 60% relative humidity | Not evidenced (EV-PE-03) |
| PE-14\_ODP\[04\] | Monitoring frequency | Continuously | Not evidenced (EV-PE-03) |
| PE-16\_ODP\[01\] | Items authorised entering | Hardware and media holding \<DocuView\> information | Not evidenced (EV-PE-04) |
| PE-16\_ODP\[02\] | Items authorised leaving | Hardware and media holding \<DocuView\> information | Not evidenced (EV-PE-04) |
| PE-17\_ODP\[01\] | Alternate work sites | Employees' homes, and any place the system owner approves in writing | In place (SyOps A38) |
| PE-17\_ODP\[02\] | Controls used | ABC Technologies' managed devices and route; screen privacy; no printing at home unless approved | Not yet assessed (C30) |

| **APPENDIX B** |
| --- |

## Appendix B PE controls outside the Moderate baseline

NIST does not select these in the Moderate security baseline, so they are not assessed in this family. One is in NIST's privacy baseline and applies because visitor records hold personal data: it is assessed with the PT family. All but that one would be ABC Technologies' to provide, and Table 47 says where its evidence may already show them.

**Table 47: PE controls not selected at Moderate**

| Control | What it adds | \<DocuView\>'s position |
| --- | --- | --- |
| PE-2(1), PE-2(2), PE-2(3) Access by Position or Role; Two Forms of Identification; Restrict Unescorted Access | Tighter rules for who may enter | Not required. No \<DocuView\> role enters a data centre |
| PE-3(1) System Access | Entry to the room holding the system controlled separately from entry to the building | Not required. ABC Technologies' evidence may show it (A.7.1, A.7.2) |
| PE-3(2), PE-3(3), PE-3(4), PE-3(5), PE-3(7), PE-3(8) Facility and Systems; Continuous Guards; Lockable Casings; Tamper Protection; Physical Barriers; Access Control Vestibules | Further physical barriers and checks | Not required. Done in part in design: the server disks are encrypted, so that reaching a host does not expose the documents (section 4.8) |
| PE-5(2) Link to Individual Identity | Output released only to the person who asked for it | Not required. Done in design: managed printers with secure release (section 4.5) |
| PE-6(2), PE-6(3), PE-6(4) Automated Intrusion Recognition and Responses; Video Surveillance; Monitoring Physical Access to Systems | More monitoring, some of it automated | Not required. CCTV is already required under PE-6(1) |
| PE-8(1) Automated Records Maintenance and Review | Visitor records kept and reviewed by automated means | Not required |
| PE-8(3) Limit Personally Identifiable Information Elements | Visitor records hold only defined personal data | Privacy baseline, so it applies. The data allowed is the name, the organisation, and the date and time of the visit. Assessed with the PT family; not evidenced (NC-PT-12; EV-PT-02; PA-122) |
| PE-9(1), PE-9(2) Redundant Cabling; Automatic Voltage Controls | Spare power cabling and voltage control | Not required |
| PE-11(1), PE-11(2) Alternate Power Supply | Long-term backup power that keeps the system running | Not required. Availability is rated Low, and an orderly shutdown is enough. ABC Technologies is asked how long its backup power lasts (EV-PE-02) |
| PE-12(1) Essential Mission and Business Functions | Emergency lighting for all areas that support essential functions | Not required |
| PE-13(2), PE-13(4) Suppression Systems, Automatic Activation and Notification; Inspections | Fire suppression that works and notifies automatically, and fire inspections | Not required. ABC Technologies' evidence may show them (A.7.5) |
| PE-14(1), PE-14(2) Automatic Controls; Monitoring with Alarms and Notifications | Environmental levels controlled automatically, with alarms | Not required. Done in part in design: the levels are monitored continuously |
| PE-15(1) Automation Support | Water detected automatically, with an alert | Not required |
| PE-18 Location of System Components | Components placed to limit damage from hazards and from unauthorised access | Not required. The second site is asked not to share the main site's hazards (\<Contingency Planning Management\>, section 4.9) |
| PE-19, PE-19(1), PE-20, PE-21, PE-22, PE-23 Information Leakage; Asset Monitoring and Tracking; Electromagnetic Pulse Protection; Component Marking; Facility Location | Protection from emanations and pulses, tracking of assets, and the siting of the facility | Not required |
| PE-3(6), PE-5(1), PE-5(3), PE-7, PE-8(2), PE-10(1), PE-13(3), PE-18(1) | Withdrawn by NIST | Not applicable |
