# \<System Name\> Physical and Environmental Protection Management

## 1 Purpose

This document sets out how the places where \<System Name\> runs and is used are designed to be protected, to meet the 18 Physical and Environmental Protection (PE) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the sites and contacts, who provides each control, how \<Organisation\>'s evidence is obtained and checked, the rules for offices and for working from home, physical incidents, the encryption that stands behind the physical controls, what \<Organisation\> is asked for, what \<System Name\> requires at each data centre, and the policy and procedures. Each subsection names the controls it helps to meet.

\<System Name\> has no premises of its own. It runs on two virtual servers in \<Organisation\>'s data centre, with backups and recovery at a second site, so 15 of the 18 controls are provided wholly by \<Organisation\>. \<System Name\>'s own part is small: how its users treat screens and printouts, how they work from home, how physical incidents are handled, and the encryption of the server disks.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.11 (Table 20). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (PE). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (PE), and the steps people follow are in \<Procedures\> (PE).

## 3 The design

### 3.1 Principles

Controls met here: PE-5, PE-6.

1. **Inherit with evidence.** A physical control counts only once \<Organisation\> has evidenced it.
2. **Same protection everywhere.** The second site meets the same requirements as the main one.
3. **Protect what users see.** Screens and printouts are protected by the people who use them.
4. **Report physical events.** Physical incidents are handled as security incidents.

These carry out the principles and rules of \<Policy\>, sections PE.3 and PE.4.

### 3.2 Sites and contacts

Controls met here: PE-2, PE-17.

![Figure 1: Where \<System Name\> is, and who protects each place](figures/pem-figure-1.png)

**Figure 1: Where \<System Name\> is, and who protects each place**

**Table 1: Sites**

| Site | Use | Location | \<Organisation\> contact | Evidence |
| --- | --- | --- | --- | --- |
| Data centre | Hosts both servers | \[Data centre name and address\] | \[Facilities contact\] | EV-PE-01 to EV-PE-04 |
| Second site | Holds backups; used for recovery (\<Contingency Planning Management\>, section 3.9) | \[Second site name and address\] | \[Facilities contact\] | EV-PE-01 to EV-PE-04 |
| Offices | Where \<System Name\> is used and printed | \[\<Organisation\> offices\] | \[Office security contact\] | EV-PE-05 |
| Homes | Remote working | Employees' homes | Security officer | C30, TPL-4 |

No \<System Name\> role needs to enter either data centre. The Windows server and database administrators work from their managed devices over \<Organisation\>'s managed administration route (flow F11; \<Maintenance Management\>, section 3.4), and the hardware beneath the servers is maintained by \<Organisation\>'s engineers.

### 3.3 Who provides each control

Controls met here: PE-1, PE-2, PE-3, PE-4, PE-5, PE-6, PE-6(1), PE-8, PE-9, PE-10, PE-11, PE-12, PE-13, PE-13(1), PE-14, PE-15, PE-16, PE-17.

Who provides each PE control, and the evidence that closes it. The first choice of evidence is \<Organisation\>'s ISO/IEC 27001 certificate and Statement of Applicability, with the Annex A control shown, for both sites. A SOC 2 report serves instead if it covers physical access (criterion CC6.4) and, for power, fire, environment and water, the availability criteria (A1.2). The site inspection (TPL-20) adds what was seen.

**Table 2: PE inheritance matrix**

| Control | \<Organisation\> provides | \<System Name\> provides | Closing evidence |
| --- | --- | --- | --- |
| PE-1 | Its own physical security policy | The policy, the procedures and this document | The policy, the procedures and this document |
| PE-2 | Authorised access list for the data centres | Nothing | A.7.2; access list review record (EV-PE-01) |
| PE-3 | Entry control, logs, visitors, keys and cards | Nothing | A.7.1, A.7.2, A.7.3; TPL-20 (EV-PE-01) |
| PE-4 | Protected cabling | Nothing | A.7.12 (EV-PE-01) |
| PE-5 | Managed printers with secure release; office security | Users' rules (A33, A36, A37); the device screen lock is \<Organisation\>'s (P-03) | A.7.7; EV-PE-05; \<Organisation\>'s device policy |
| PE-6, PE-6(1) | Monitoring, alarms and CCTV; log review | Incident handling of what is reported | A.7.4; monitoring records (EV-PE-01) |
| PE-8 | Visitor records and review | Nothing | A.7.2; sample records (EV-PE-01) |
| PE-9, PE-10, PE-11, PE-12 | Power protection, emergency shutoff, UPS and emergency lighting | Orderly shutdown on UPS (\<Security Operating Procedures\>, section 4.6) | A.7.11, A.7.12; maintenance records (EV-PE-02) |
| PE-13, PE-13(1) | Fire detection and suppression, with automatic notification | Nothing | A.7.5; fire safety records (EV-PE-03) |
| PE-14 | Temperature and humidity control and monitoring | Nothing | A.7.5, A.7.8; monitoring records (EV-PE-03) |
| PE-15 | Water damage protection | Nothing | A.7.5 (EV-PE-03) |
| PE-16 | Control of deliveries and removals | Receives notice of host hardware removal and its sanitising certificate; approves removal of any other \<System Name\> equipment (\<Procedures\>, PRO-MA-2) | A.7.2, A.7.10; sample records (EV-PE-04) |
| PE-17 | Managed devices and route | Home working rules and the yearly check | A.6.7, A.7.9; EV-PE-05; TPL-4 |
| Compensating | Nothing | Server disk encryption, so physical access to hosts does not expose data | Encryption settings on the servers |

### 3.4 How the evidence is obtained and checked

**Table 3: Steps of the evidence check**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 | \<Organisation\> is asked for its certificate, Statement of Applicability and latest audit findings, or its SOC 2 report, for both sites | System owner | \<Evidence Requests\>, EV-PE-01 |
| 2 | Where those do not cover a control, the facility evidence is asked for | System owner | EV-PE-01 to EV-PE-05 |
| 3 | What is received is recorded against each control in the matrix, and each corporate parameter value is confirmed as met | System owner | Section 3.3 |
| 4 | Each data centre, the main site and the second site, is inspected once, at Level 2, by the independent assessor, or by \<Organisation\>'s auditor if the assessor cannot visit | Independent assessor | TPL-20 |
| 5 | Any shortfall is raised as a risk | System owner | \<Risk List\> |
| 6 | The check is repeated every 12 months, and after a change of site or a significant incident at a site | System owner | Section 3.3 |

The organisation does not assess the sites itself. It inherits their protection by evidence, with the single inspection in step 4.

### 3.5 Offices: screens and printing

Controls met here: PE-5.

1. \<System Name\> items are printed only on \<Organisation\>'s managed printers with secure release: \[managed printers\]. A page prints only when its owner is at the printer.
2. A printout is collected at once, marked \<Classification\>, locked away when not in use, and shredded when no longer needed (\<Media Protection Management\>, section 3.4).
3. A screen is locked when its user leaves it, and placed so that others cannot read it.
4. \<Organisation\>'s managed devices lock the screen after the inactivity period it sets (P-03; \<Access Control Management\>, section 3.15). \<System Name\> has no page lock or idle timeout of its own.
5. Desks are kept clear of printouts and notes.

### 3.6 Working from home

Controls met here: PE-17.

1. People work remotely only from home, unless the system owner has approved another place in writing (\<Security Operating Procedures\>, rule A38).
2. They use only \<Organisation\>'s managed device, and connect to its VPN before opening \<System Name\>. They never use a public or shared computer, and use public Wi-Fi only with the VPN connected first.
3. They work where others in the home cannot see the screen, and do not print \<System Name\> items at home unless the system owner has approved it.
4. They do not use \<System Name\> from outside the UK, or take a device that can reach it abroad, without written approval from the system owner and the security officer.
5. They report any concern or incident to the security officer at once, and a lost or stolen device within 1 hour. The security and privacy contacts are in \<Security Operating Procedures\>, section 6.
6. Every 12 months the security officer puts a short checklist to every person who works from home: the managed device, the VPN, screen privacy, no printing, and reporting. The answers are recorded on TPL-4. Every person completes it, not a sample.

These are rules A35 to A42 of the rules of behaviour, which each person signs (\<Security Operating Procedures\>, Part A).

### 3.7 Physical incidents

Controls met here: PE-6, PE-8, PE-11.

The loss or theft of a device or printout, unauthorised entry to a data centre, and fire, flood or power loss affecting \<System Name\> are security incidents. Whoever sees one reports it to the security officer at once. \<Organisation\>'s security contact tells the security officer of any physical incident at a site that affects \<System Name\>, and of any anomaly in the visitor records, within 24 hours. The security officer handles it with the playbooks for a lost device or printout and for intrusion, fire, flood or power loss at a data centre (\<Incident Response Management\>, section 3.9), and the contingency plan is invoked if a site is lost (\<Contingency Planning Management\>).

**Loss of power.** Each data centre has enough backup power for an orderly shutdown of both servers. When a data centre moves to backup power, \<Organisation\> warns the Windows server administrator. The administrators then shut both servers down in order, before the backup power runs out (\<Security Operating Procedures\>, section 4.6), and record it as a physical incident. How long the backup power lasts, and how the warning is given, are asked of \<Organisation\> (EV-PE-02).

### 3.8 Encryption behind the physical controls

Both servers' disks are encrypted, and backups are encrypted before they leave the database server. Someone who reaches a host, a disk or a backup copy therefore cannot read \<System Name\>'s items. This does not replace \<Organisation\>'s physical controls: it limits the harm if one fails.

### 3.9 What \<Organisation\> provides

Controls met here: PE-2, PE-3, PE-4, PE-5, PE-6, PE-6(1), PE-8, PE-9, PE-10, PE-11, PE-12, PE-13, PE-13(1), PE-14, PE-15, PE-16, PE-17.

**Table 4: Asked of \<Organisation\>**

| Request | Controls | What is asked |
| --- | --- | --- |
| EV-PE-01 | PE-2, PE-3, PE-4, PE-6, PE-6(1), PE-8 | Who can enter each data centre, how entry is controlled and logged, how visitors, keys and cabling are managed, how access is monitored, and how incidents reach \<System Name\>'s security officer. Its certificate or report, for both sites |
| EV-PE-02 | PE-9, PE-10, PE-11, PE-12 | How power is protected, the emergency shutoff, backup power for an orderly shutdown, and emergency lighting |
| EV-PE-03 | PE-13, PE-13(1), PE-14, PE-15 | Fire detection and suppression and who they notify, temperature and humidity and how they are monitored, and protection from water |
| EV-PE-04 | PE-16 | How hardware and media are authorised and recorded when entering or leaving |
| EV-PE-05 | PE-5, PE-17 | Office controls for printers and screens, which managed printers have secure release, and the controls on managed devices and the route at home |

### 3.10 What \<System Name\> requires at each data centre

These are what \<System Name\> requires of \<Organisation\> at both the main data centre and the second site. \<Organisation\> provides them, and they count only once evidenced (section 3.4).

#### 3.10.1 Entry, keys and cabling

Controls met here: PE-2, PE-3, PE-4.

1. **Access list.** \<Organisation\> keeps the list of people authorised to enter each data centre, and issues each an individual card or credential. The list is reviewed every 12 months, and a person is removed when their need ends or they leave. No \<System Name\> role is on it: every administrator works remotely (\<Maintenance Management\>, section 3.4).
2. **Entry control.** Every data centre entrance and exit is controlled by \<Organisation\>'s electronic access control system, with individual cards or credentials, and every entry and exit is logged.
3. **Public areas and visitors.** A staffed reception controls the areas open to the public. Visitors are signed in, and always escorted.
4. **Keys and combinations.** \<Organisation\>'s facilities staff hold keys, combinations and other entry devices securely, and inventory keys, cards and combinations every 12 months. Keys and combinations are changed every 12 months; a combination when someone who knows it leaves; and a key when it is lost or not returned.
5. **Cabling.** Power and network cabling is kept in locked rooms, cabinets and cable trays.

#### 3.10.2 Monitoring and visitor records

Controls met here: PE-6, PE-6(1), PE-8.

1. **Monitoring.** \<Organisation\> monitors each data centre with intrusion alarms and CCTV, and responds to alarms.
2. **Entry log review.** The entry logs are reviewed monthly, and after a physical security incident or alarm.
3. **Visitor records.** Visitor records are kept for 12 months and reviewed monthly. Anomalies go to \<Organisation\>'s security contact, who tells \<System Name\>'s security officer (section 3.7).

#### 3.10.3 Power and lighting

Controls met here: PE-9, PE-10, PE-11, PE-12.

1. **Power equipment.** \<Organisation\> protects the power equipment and cabling that serve the hosts from damage and destruction.
2. **Emergency shutoff.** Power to the hosting equipment for both servers can be shut off in an emergency, by switches near the exits of the data centre room. The shutoff is guarded against accidental and unauthorised use, and \<Organisation\> is asked how (EV-PE-02).
3. **Backup power.** Enough for an orderly shutdown of both servers (section 3.7).
4. **Emergency lighting.** Automatic emergency lighting in each data centre comes on in a power failure and covers the emergency exits and evacuation routes.

#### 3.10.4 Fire, temperature, humidity and water

Controls met here: PE-13, PE-13(1), PE-14, PE-15.

1. **Fire.** Each data centre has fire detection and suppression systems, with an independent energy source. Detection works automatically and notifies \<Organisation\>'s facilities staff and the fire and rescue service.
2. **Temperature and humidity.** Kept within the ASHRAE TC 9.9 recommended envelope: 18 to 27°C, a dew point from -9 to 15°C, and at most 60% relative humidity. They are monitored continuously.
3. **Water.** Each data centre has master shutoff or isolation valves that can be reached, work, and are known to key people.

#### 3.10.5 Deliveries and removals

Controls met here: PE-16.

1. **What is controlled.** Hardware and media that hold \<System Name\> information, entering and leaving each data centre.
2. **Approval.** \<Organisation\>'s own process approves the removal of host hardware beneath the servers, after sanitising it, and tells the system owner beforehand where it can and afterwards with the certificate; the system owner approves the removal of anything else of \<System Name\>'s (\<Maintenance Management\>, section 3.7; PRO-MA-2; D-MA-03).
3. **Records.** \<Organisation\> keeps its delivery and removal records. \<System Name\>'s own are on TPL-12 and TPL-13.

### 3.11 Policy and procedures

Controls met here: PE-1.

\<Policy\> (PE) and \<Procedures\> (PE) meet PE-1. Who they are shared with is in \<Policy\>, section PE.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
