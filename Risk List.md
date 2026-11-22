# \<System Name\> Risk List

## 1 Purpose

This list records the risks to \<System Name\> and every non-compliance with the controls, across all control families, and how each is treated. It is used by every control family. Section 2 is the risk register. Section 3 records each risk acceptance. Section 4 sets the method: how risks are rated, who may decide, and the treatments. Section 5 is the non-compliance register, with one section per family.

Risks are numbered R-XX-nn and non-compliances NC-XX-nn, where XX is the family code. Each non-compliance names the risk it contributes to, and each risk names the items in \<Plan of Action and Milestones\> that treat it.

## 2 Risk register

The register has one entry for each risk. Likelihood, impact and rating follow section 4.1. Residual is the rating once the treatment is complete.

**Table 1: Risk register**

| ID | Risk | Cause | Consequence | Likelihood | Impact | Rating | Treatment | Residual | Owner | POA&M | Status | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-AC-01 | A database administrator reads item content directly in SQL Server, outside the application's access checks | Database administrators need high privileges on SQL Server for maintenance, and the item tables are not encrypted against them | Disclosure of items, including personal or special category data, without a record in the application audit log | Low | High | Medium | Reduce: direct queries only under an approved change or incident (B16); SQL Server Audit records every read of the item tables by a login other than the API's, forwarded to central logging and reviewed weekly by the auditor; named accounts over the administration route with multi-factor authentication; the 6-monthly review of SQL Server logins (P-52) | Medium, as the impact stays High | System owner | \[PA-nn\] | Open | \[Date\] |
| R-AC-02 | Access control values and tailoring are used before they are approved | The AC parameter values and tailoring proposals in \<Decision Register\> are recommendations, with no decision recorded | Controls run on values nobody with authority has accepted, and an assessor finds the control other than satisfied | Medium | Low | Low | Approve: the system owner approves the values, and the authorising official the tailoring, in \<Decision Register\> (D-AC-01 to D-AC-04 and D-AC-07 to D-AC-10, D-AC-P02 to D-AC-P55), and the Head of Cyber approves \<Policy\> (AC) | Low | System owner | None | Open | \[Date\] |
| R-AC-03 | An access control that \<System Name\> inherits from \<Organisation\> is weaker than the design assumes | The evidence requested from \<Organisation\> for AC (\<Evidence Requests\>, EV-AC-01 to EV-AC-17, EV-IA-04 and EV-GEN-04) has not been seen | A gap in account handling, lockout, screen lock, remote, wireless or mobile access, or device control goes unnoticed and exposes items | Low | Medium | Low | Evidence: obtain and examine the evidence, then confirm or re-rate each entry | Low | System owner | None | Open | \[Date\] |
| R-AT-01 | A standard user keeps access while their yearly awareness training and briefing are overdue | Overdue standard users are reminded but not suspended; only privileged access is suspended after 30 days (\<Awareness and Training Management\>, section 3.6) | A user misses updated content on new threats or changed rules, and is more likely to mishandle an item or fall for social engineering | Medium | Low | Low | Accept: monthly reminders by the security officer; the number overdue is reported monthly on TPL-8 with a target of 0; access is reviewed every 12 months (P-05) | Low | System owner | None | Proposed (D-AT-01) | \[Date\] |
| R-AT-02 | Awareness and training values and the accepted risk are used before they are approved | The AT parameter values (D-AT-P24, D-AT-P56 to D-AT-P60) and the acceptance of R-AT-01 (D-AT-01) in \<Decision Register\> are recommendations, with no decision recorded | Training runs on frequencies, triggers and roles nobody with authority has accepted, and an assessor finds the control other than satisfied | Medium | Low | Low | Approve: the system owner approves the values and D-AT-01 in \<Decision Register\>, and the Head of Cyber approves \<Policy\> (AT) | Low | System owner | None | Open | \[Date\] |
| R-AT-03 | Training that \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | The evidence requested from \<Organisation\> for AT (\<Evidence Requests\>, EV-AT-01, EV-AT-02 and EV-GEN-04) has not been seen | \<Organisation\>'s course misses insider threat, social engineering or privacy, its records cannot be produced, or the Head of Cyber's or data protection officer's training cannot be shown | Low | Medium | Low | Evidence: obtain and examine the evidence, then confirm or re-rate each entry | Low | System owner | None | Open | \[Date\] |
| R-AU-01 | Audit and accountability values and the accepted risk are used before they are approved | The AU parameter values (D-AU-P07 to D-AU-P09, D-AU-P61, D-AU-P62) and the acceptance of R-AU-03 (D-AU-01) in \<Decision Register\> are recommendations, with no decision recorded | Logging, review, time and retention run on values nobody with authority has accepted, and an assessor finds the control other than satisfied | Medium | Low | Low | Approve: the system owner approves the values and D-AU-01 in \<Decision Register\>, and the Head of Cyber approves \<Policy\> (AU) | Low | System owner | None | Open | \[Date\] |
| R-AU-02 | Logging that \<System Name\> relies on from \<Organisation\> is weaker than the design assumes | The evidence requested from \<Organisation\> for AU (\<Evidence Requests\>, EV-AU-01 to EV-AU-05 and EV-GEN-04) has not been seen, and the storage figures are not yet measured | Server, database, PingFederate or Active Directory events are not logged, kept, protected or passed to the auditor; the time drifts; or storage runs out, so an incident cannot be traced | Low | Medium | Low | Evidence: obtain and examine the evidence and measure the storage figures, then confirm or re-rate each entry | Low | System owner | None | Open | \[Date\] |
| R-AU-03 | A logging fault stops staff from using \<System Name\> | By design every action that cannot be recorded is refused until logging is restored (P-61) | Staff cannot view or change items until the Windows server or database administrator restores logging | Low | Low | Low | Accept: the failure is alerted within 1 hour (U7), availability is rated Low, and the recovery times in \<Contingency Planning Management\> still apply | Low | System owner | None | Proposed (D-AU-01) | \[Date\] |
| R-CA-01 | Assessment, authorisation and monitoring rest on people, values and records nobody with authority has appointed or approved | The authorising official, the Level 2 team and \<Organisation\>'s common control official are not named; the basis of authorisation (D-CA-01), P-25 (D-CA-P25) and the interface record (D-CA-02) are not approved; \<Policy\> (CA) is not approved; no assessment has yet been planned or run | \<System Name\> is assessed by someone who is not independent, authorised by someone without the authority to accept its risk, or operated before it is authorised, and an assessor finds CA-2, CA-6 and CA-7 other than satisfied | Medium | Low | Low | Approve: the system owner has the roles named in \<Roles and Responsibilities\>, approves D-CA-02, the authorising official D-CA-01 and D-CA-P25, and the Head of Cyber approves \<Policy\> (CA); the first assessment then runs under PRO-CA-1 | Low | System owner | None | Open | \[Date\] |
| R-CA-02 | Inherited controls, exchanges or the monitoring strategy that \<System Name\> relies on from \<Organisation\> are weaker than the design assumes | The evidence requested for CA (\<Evidence Requests\>, EV-CA-01, EV-CA-02, EV-PM-03 and EV-GEN-04) has not been seen | The authorising official accepts 68 inherited controls nobody has authorised; an exchange has no agreed terms; or the system's monitoring does not fit \<Organisation\>'s strategy | Low | Medium | Low | Evidence: obtain and examine the evidence, then confirm or re-rate each entry | Low | System owner | None | Open | \[Date\] |
| \[R-XX-nn\] | \[Risk\] | \[Cause\] | \[Consequence\] | \[Likelihood\] | \[Impact\] | \[Rating\] | \[Treatment\] | \[Residual\] | \[Owner\] | \[PA-nn\] | \[Status\] | \[Date\] |

## 3 Risk acceptance

Each acceptance is recorded here by the person allowed to make it under section 4.2, with the non-compliance, the risk it belongs to, any compensating measure, and the date by which it is reviewed.

**Table 2: Risk acceptance**

| Risk | Decision | Name | Date | Review date |
| --- | --- | --- | --- | --- |
| \[NC-XX-nn\] (\[R-XX-nn\]): \[Non-compliance and compensating measure\] | \[Decision, rating and period\] | \[Name\] | \[Date\] | \[Review date\] |

## 4 Risk method

\<System Name\> is not required to meet every control. The organisation takes a risk-based approach: every non-compliance is identified and documented, its risk is understood, and a named person decides what happens to it. A risk that is acceptable may be accepted with a recorded decision. A risk that is too high requires a remediation plan in \<Plan of Action and Milestones\>. Finding a non-compliance does not by itself start a fix.

This method follows the risk response in CSS (tasks R-2 and R-3). The risk model follows CSS: a threat source exploits a weakness, with a likelihood, to cause an impact.

### 4.1 Rating

Likelihood and impact are each rated Low, Medium or High. Impact considers the confidentiality, integrity and availability of the items \<System Name\> holds, and the effect on \<Organisation\>.

**Table 3: Risk rating**

| Likelihood | Impact Low | Impact Medium | Impact High |
| --- | --- | --- | --- |
| Low | Low | Low | Medium |
| Medium | Low | Medium | High |
| High | Low | Medium | High |

The matrix weights impact more than likelihood on purpose. A High impact can never rate below Medium, and a Low impact never above Low, because \<System Name\>'s harm is driven by what it holds: one disclosure of items holding personal or special category data matters more than how often an attempt is made. CSS allows the organisation to set this (Appendix I).

**Table 3a: Likelihood scale**

| Level | Meaning |
| --- | --- |
| High | The threat source is motivated and able, the weakness is known or easy to find, and nothing in place stops it; expected within a year |
| Medium | The threat source is able, but something in place makes success less likely, or the weakness needs inside knowledge; possible within a year |
| Low | Needs rare skill, access or a chain of failures, or a compensating control is in place and tested; unlikely within a year |

**Table 3b: Impact scale**

| Level | Meaning |
| --- | --- |
| High | Severe or serious adverse effect (CSS): disclosure or loss of many items or of special category data, or \<Organisation\> breaching the law |
| Medium | Serious adverse effect on part of the service: some items disclosed or changed, or a loss of service beyond the 72-hour recovery time objective (P-12) |
| Low | Limited adverse effect: no items disclosed, and a short loss of service within the recovery time |

**Table 3c: Threat sources considered**

| Source (CSS, Table D-2) | Examples for \<System Name\> |
| --- | --- |
| Adversarial | An outsider exploiting a known flaw; an insider reading another schema's items; a supplier's compromised package |
| Accidental | An administrator deleting or misconfiguring; a user sending an export to the wrong person |
| Structural | A disk, VM or SQL Server failure; PingFederate or Active Directory unavailable, so nobody can sign in; a software flaw; loss of the key or backup |
| Environmental | Loss of power, cooling or the site, provided by \<Organisation\> |

**Assumptions and uncertainty.**

- Ratings assume \<Organisation\>'s inherited controls work as their Cyber Essentials Plus certificate describes, until the evidence in \<Evidence Requests\> is seen.
- Risks are rated for the target design on its servers.
- Where the evidence is a single test or a document review, not operation over time, the rating is the higher of the two plausible levels.
- Ratings are reviewed every 12 months, and after a significant change, incident or new test result (\<Procedures\>, PRO-RA-1).

**Table 3d: Provisional ratings**

A rating marked provisional was set before the evidence was seen. Each is settled, and the word removed, when the evidence below arrives.

| Non-compliance | Control | Rating | Settled by |
| --- | --- | --- | --- |
| NC-AC-01 | AC-1 | Low, provisional | EV-GEN-04: the \<Organisation\> policies that apply |
| NC-AC-02 | AC-2 | Low, provisional | EV-AC-01: Active Directory account lifecycle and group ownership; EV-AC-02: Windows and SQL Server administrator accounts |
| NC-AC-03 | AC-2(1) | Low, provisional | EV-AC-01: Active Directory account lifecycle and group ownership |
| NC-AC-04 | AC-2(3) | Low, provisional | EV-AC-01: Active Directory account lifecycle and group ownership |
| NC-AC-05 | AC-2(5) | Low, provisional | EV-AC-07: screen lock on devices and servers; EV-IA-04: PingFederate's settings for \<System Name\> |
| NC-AC-06 | AC-2(13) | Low, provisional | EV-AC-01: Active Directory account lifecycle and group ownership |
| NC-AC-07 | AC-4 | Low, provisional | EV-AC-03: firewall and network controls for the flows |
| NC-AC-08 | AC-5 | Low, provisional | EV-AC-04: who holds network, hypervisor and firmware security functions |
| NC-AC-09 | AC-6 | Low, provisional | EV-AC-02: Windows and SQL Server administrator accounts; EV-AC-04: who holds network, hypervisor and firmware security functions |
| NC-AC-10 | AC-6(1) | Low, provisional | EV-AC-04: who holds network, hypervisor and firmware security functions |
| NC-AC-12 | AC-6(5) | Low, provisional | EV-AC-02: Windows and SQL Server administrator accounts |
| NC-AC-14 | AC-6(9) | Low, provisional | EV-AC-02: Windows and SQL Server administrator accounts |
| NC-AC-16 | AC-7 | Low, provisional | EV-AC-05: Windows logon lockout on the VMs; EV-IA-04: PingFederate's settings for \<System Name\> |
| NC-AC-17 | AC-8 | Low, provisional | EV-AC-06: Windows logon banner on the VMs; EV-IA-04: PingFederate's settings for \<System Name\> |
| NC-AC-18 | AC-11 | Low, provisional | EV-AC-07: screen lock on devices and servers |
| NC-AC-19 | AC-11(1) | Low, provisional | EV-AC-07: screen lock on devices and servers |
| NC-AC-20 | AC-12 | Low, provisional | EV-IA-04: PingFederate's settings for \<System Name\> |
| NC-AC-21 | AC-14 | Low, provisional | EV-AC-03: firewall and network controls for the flows |
| NC-AC-22 | AC-17 | Low, provisional | EV-AC-08: the remote access service |
| NC-AC-23 | AC-17(1) | Low, provisional | EV-AC-09: monitoring of remote access |
| NC-AC-24 | AC-17(2) | Low, provisional | EV-AC-10: encryption of remote access |
| NC-AC-25 | AC-17(3) | Low, provisional | EV-AC-11: managed remote access points |
| NC-AC-26 | AC-17(4) | Low, provisional | EV-AC-12: privileged remote access through the VPN and administration route |
| NC-AC-27 | AC-18 | Low, provisional | EV-AC-13: wireless controls |
| NC-AC-28 | AC-18(1) | Low, provisional | EV-AC-13: wireless controls |
| NC-AC-29 | AC-18(3) | Low, provisional | EV-AC-14: wireless disabled on the VMs and builds |
| NC-AC-30 | AC-19 | Low, provisional | EV-AC-15: managed, encrypted laptops as the only mobile devices |
| NC-AC-31 | AC-19(5) | Low, provisional | EV-AC-15: managed, encrypted laptops as the only mobile devices |
| NC-AC-32 | AC-20 | Low, provisional | EV-AC-16: blocking of unmanaged devices |
| NC-AC-33 | AC-20(2) | Low, provisional | EV-AC-17: USB and portable storage controls |
| NC-AT-01 | AT-1 | Low, provisional | EV-GEN-04: the \<Organisation\> policies that apply |
| NC-AT-02 | AT-2 | Low, provisional | EV-AT-01: \<Organisation\>'s security and privacy course, its content and completion records |
| NC-AT-03 | AT-2(2) | Low, provisional | EV-AT-01: \<Organisation\>'s security and privacy course, its content and completion records |
| NC-AT-04 | AT-2(3) | Low, provisional | EV-AT-01: \<Organisation\>'s security and privacy course, its content and completion records |
| NC-AT-05 | AT-3 | Low, provisional | EV-AT-01: \<Organisation\>'s training for its server administrators; EV-AT-02: the Head of Cyber's and data protection officer's training |
| NC-AT-06 | AT-4 | Low, provisional | EV-AT-01: \<Organisation\>'s course completion records |
| NC-AU-01 | AU-1 | Low, provisional | EV-GEN-04: the \<Organisation\> policies that apply |
| NC-AU-02 | AU-2 | Low, provisional | EV-AU-01: central monitoring and what it needs; EV-AU-04: the Windows audit policy; EV-AU-05: PingFederate and Active Directory audit |
| NC-AU-03 | AU-3 | Low, provisional | EV-AU-04: the Windows audit policy and a sample log |
| NC-AU-04 | AU-4 | Low, provisional | EV-AU-03: storage and backup; the measured storage figures |
| NC-AU-05 | AU-5 | Low, provisional | EV-AU-01: central monitoring and its alerts |
| NC-AU-06 | AU-6 | Low, provisional | EV-AU-05: PingFederate and Active Directory records for the auditor |
| NC-AU-07 | AU-6(1) | Low, provisional | EV-AU-01: central monitoring and its alert rules |
| NC-AU-08 | AU-6(3) | Low, provisional | EV-AU-01: the auditor's read access in central logging; EV-AU-05: PingFederate and Active Directory records |
| NC-AU-09 | AU-8 | Low, provisional | EV-AU-02: the time source and drift |
| NC-AU-10 | AU-9 | Low, provisional | EV-AU-01: protection of logs in central logging |
| NC-AU-11 | AU-9(4) | Low, provisional | EV-AU-04: the Windows audit policy and who manages it |
| NC-AU-12 | AU-11 | Low, provisional | EV-AU-01, EV-AU-03 to EV-AU-05: retention of central logs, storage and inherited audit records |
| NC-AU-13 | AU-12 | Low, provisional | EV-AU-04: the Windows audit policy; EV-AU-05: PingFederate and Active Directory audit |
| NC-CA-01 | CA-1 | Low, provisional | EV-GEN-04: the \<Organisation\> policies that apply |
| NC-CA-04 | CA-3 | Low, provisional | EV-CA-02: the agreements for the exchanges |
| NC-CA-06 | CA-6 | Low, provisional | EV-CA-01: who authorises the common controls, and the authorisation record |
| NC-CA-07 | CA-7 | Low, provisional | EV-PM-03: \<Organisation\>'s continuous monitoring strategy |
| \[NC-XX-nn\] | \[Control\] | \[Rating\], provisional | \[EV-XX-nn\]: \[The evidence that settles it\] |

### 4.2 Who may decide

**Table 4: Decision rules by rating**

| Rating | Default position | Who decides | Conditions of acceptance |
| --- | --- | --- | --- |
| Low | May be accepted | System owner | Recorded in this document; reviewed every 12 months |
| Medium | May be accepted or remediated | Authorising official, on the system owner's advice | A compensating measure where one exists; reviewed every 6 months |
| High | Not acceptable by default; a remediation plan is required | Authorising official | Acceptance only for a stated, limited period while the remediation plan runs |

These thresholds are \<System Name\>'s own, and sit within \<Organisation\>'s risk management strategy and risk appetite (PM-9).

### 4.3 Treatments

**Table 5: Treatments**

| Treatment | Meaning | Where it is recorded |
| --- | --- | --- |
| Accept | The risk is understood and tolerated, and the non-compliance remains | Section 3 of this document, and the control's line in \<System Security Plan\>, section 7 |
| Remediate | The non-compliance is to be fixed, on a plan and not immediately | \<Plan of Action and Milestones\>, with milestones |
| Approve | The mechanism exists or no mechanism is needed, and only a decision or value is outstanding | \<System Description\>, section 4, and \<Decision Register\> |
| Evidence | The control is expected to be inherited, and \<Organisation\> must supply the evidence | \<Evidence Requests\> and the control's line in \<System Security Plan\>, section 7, then rated when the evidence is seen |
| Tailor | The control or part is proposed as not applicable, with a rationale | \<System Security Plan\>, section 5 |

## 5 Non-compliance register

This register has one entry for each control that is not fully satisfied, with its family, in CSS order. Who decided each treatment, and when, is in \<Decision Register\>, section 4. Each entry names the risk it contributes to in section 2, its proposed treatment from Table 5, and its item in \<Plan of Action and Milestones\> where it is remediated. Cause codes are D (a decision or approval is outstanding), G (a gap in the system) and E (evidence is not yet available from the servers or \<Organisation\>). Ratings marked "provisional" are set when the evidence is seen (Table 3d).

**Table 6: Non-compliance register**

| ID | Family | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-AC-01 | AC | AC-1 Policy and Procedures | \<Policy\> (AC) is not yet approved by the Head of Cyber, nor \<Procedures\> (AC) by the system owner. Not yet evidenced by \<Organisation\>: EV-GEN-04. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The policy and procedures are written, and only their approval is outstanding. \<Organisation\>'s policies are expected to apply, but are not yet seen | None |
| NC-AC-02 | AC | AC-2 Account Management | Not yet approved: D-AC-02, D-AC-P04, D-AC-P05, D-AC-P06, D-AC-P36, D-AC-P37, D-AC-P52, D-AC-P55. Not yet evidenced by \<Organisation\>: EV-AC-01, EV-AC-02. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-03 | AC | AC-2(1) Automated Account Management | Not yet evidenced by \<Organisation\>: EV-AC-01. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-04 | AC | AC-2(3) Disable Accounts | Not yet approved: D-AC-P38. Not yet evidenced by \<Organisation\>: EV-AC-01. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-05 | AC | AC-2(5) Inactivity Logout | Not yet approved: D-AC-P53. Not yet evidenced by \<Organisation\>: EV-AC-07, EV-IA-04. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-06 | AC | AC-2(13) High-risk Individuals | Not yet approved: D-AC-P41. Not yet evidenced by \<Organisation\>: EV-AC-01. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-07 | AC | AC-4 Information Flow Enforcement | Not yet evidenced by \<Organisation\>: EV-AC-03. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-08 | AC | AC-5 Separation of Duties | Not yet evidenced by \<Organisation\>: EV-AC-04. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-09 | AC | AC-6 Least Privilege | Not yet evidenced by \<Organisation\>: EV-AC-02, EV-AC-04. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-10 | AC | AC-6(1) Authorize Access to Security Functions | Not yet approved: D-AC-P44. Not yet evidenced by \<Organisation\>: EV-AC-04. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-11 | AC | AC-6(2) Non-privileged Access for Nonsecurity Functions | Not yet approved: D-AC-P45. | D | R-AC-02 | Low | Approve | The design meets the control, and only the approval of its values or tailoring is outstanding | None |
| NC-AC-12 | AC | AC-6(5) Privileged Accounts | Not yet evidenced by \<Organisation\>: EV-AC-02. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-13 | AC | AC-6(7) Review of User Privileges | Not yet approved: D-AC-P04, D-AC-P52. | D | R-AC-02 | Low | Approve | The design meets the control, and only the approval of its values or tailoring is outstanding | None |
| NC-AC-14 | AC | AC-6(9) Log Use of Privileged Functions | Not yet approved: D-AC-P44. Not yet evidenced by \<Organisation\>: EV-AC-02. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-15 | AC | AC-6(10) Prohibit Non-privileged Users from Executing Privileged Functions | Not yet approved: D-AC-P44. | D | R-AC-02 | Low | Approve | The design meets the control, and only the approval of its values or tailoring is outstanding | None |
| NC-AC-16 | AC | AC-7 Unsuccessful Logon Attempts | Not yet approved: D-AC-09, D-AC-P42. Not yet evidenced by \<Organisation\>: EV-AC-05, EV-IA-04. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-17 | AC | AC-8 System Use Notification | Not yet approved: D-AC-03, D-AC-04, D-AC-P43. Not yet evidenced by \<Organisation\>: EV-AC-06, EV-IA-04. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-18 | AC | AC-11 Device Lock | Not yet approved: D-AC-P03. Not yet evidenced by \<Organisation\>: EV-AC-07. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-19 | AC | AC-11(1) Pattern-hiding Displays | Not yet approved: D-AC-P03. Not yet evidenced by \<Organisation\>: EV-AC-07. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-20 | AC | AC-12 Session Termination | Not yet approved: D-AC-P02. Not yet evidenced by \<Organisation\>: EV-IA-04. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-21 | AC | AC-14 Permitted Actions Without Identification | Not yet approved: D-AC-P51. Not yet evidenced by \<Organisation\>: EV-AC-03. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-22 | AC | AC-17 Remote Access | Not yet approved: D-AC-P46. Not yet evidenced by \<Organisation\>: EV-AC-08. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-23 | AC | AC-17(1) Monitoring and Control | Not yet evidenced by \<Organisation\>: EV-AC-09. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-24 | AC | AC-17(2) Encryption | Not yet evidenced by \<Organisation\>: EV-AC-10. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-25 | AC | AC-17(3) Managed Access Control Points | Not yet evidenced by \<Organisation\>: EV-AC-11. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-26 | AC | AC-17(4) Privileged Commands and Access | Not yet approved: D-AC-P54. Not yet evidenced by \<Organisation\>: EV-AC-12. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-27 | AC | AC-18 Wireless Access | Not yet approved: D-AC-P47. Not yet evidenced by \<Organisation\>: EV-AC-13. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-28 | AC | AC-18(1) Authentication and Encryption | Not yet approved: D-AC-P47. Not yet evidenced by \<Organisation\>: EV-AC-13. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-29 | AC | AC-18(3) Disable Wireless Networking | Not yet evidenced by \<Organisation\>: EV-AC-14. | E | R-AC-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-30 | AC | AC-19 Mobile Devices | Not yet approved: D-AC-P47. Not yet evidenced by \<Organisation\>: EV-AC-15. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-31 | AC | AC-19(5) Device Encryption | Not yet approved: D-AC-P47. Not yet evidenced by \<Organisation\>: EV-AC-15. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-32 | AC | AC-20 External Systems | Not yet approved: D-AC-10, D-AC-P48. Not yet evidenced by \<Organisation\>: EV-AC-16. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-33 | AC | AC-20(2) Portable Storage Devices | Not yet approved: D-AC-P48. Not yet evidenced by \<Organisation\>: EV-AC-17. | D, E | R-AC-02, R-AC-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or tailoring is outstanding. \<Organisation\>'s part is expected to be in place under its Cyber Essentials Plus certificate, but is not yet seen | None |
| NC-AC-34 | AC | AC-21 Information Sharing | Not yet approved: D-AC-P49. | D | R-AC-02 | Low | Approve | The design meets the control, and only the approval of its values or tailoring is outstanding | None |
| NC-AT-01 | AT | AT-1 Policy and Procedures | \<Policy\> (AT) is not yet approved by the Head of Cyber, nor \<Procedures\> (AT) by the system owner. Not yet evidenced by \<Organisation\>: EV-GEN-04. | D, E | R-AT-02, R-AT-03 | Low, provisional | Approve; Evidence | The policy and procedures are written, and only their approval is outstanding. \<Organisation\>'s policies are expected to apply, but are not yet seen | None |
| NC-AT-02 | AT | AT-2 Literacy Training and Awareness | Not yet approved: D-AT-01, D-AT-P24, D-AT-P56, D-AT-P57, D-AT-P58. Not yet evidenced by \<Organisation\>: EV-AT-01. | D, E | R-AT-01, R-AT-02, R-AT-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or accepted risk is outstanding. \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AT-03 | AT | AT-2(2) Insider Threat | Not yet evidenced by \<Organisation\>: EV-AT-01. | E | R-AT-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AT-04 | AT | AT-2(3) Social Engineering and Mining | Not yet evidenced by \<Organisation\>: EV-AT-01. | E | R-AT-03 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AT-05 | AT | AT-3 Role-based Training | Not yet approved: D-AT-P24, D-AT-P56, D-AT-P58, D-AT-P59. Not yet evidenced by \<Organisation\>: EV-AT-01, EV-AT-02. | D, E | R-AT-02, R-AT-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or accepted risk is outstanding. \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AT-06 | AT | AT-4 Training Records | Not yet approved: D-AT-P60. Not yet evidenced by \<Organisation\>: EV-AT-01. | D, E | R-AT-02, R-AT-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values or accepted risk is outstanding. \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AU-01 | AU | AU-1 Policy and Procedures | \<Policy\> (AU) is not yet approved by the Head of Cyber, nor \<Procedures\> (AU) by the system owner. Not yet evidenced by \<Organisation\>: EV-GEN-04. | D, E | R-AU-01, R-AU-02 | Low, provisional | Approve; Evidence | The policy and procedures are written, and only their approval is outstanding. \<Organisation\>'s policies are expected to apply, but are not yet seen | None |
| NC-AU-02 | AU | AU-2 Event Logging | Not yet approved: D-AU-P62. Not yet evidenced by \<Organisation\>: EV-AU-01, EV-AU-04, EV-AU-05. | D, E | R-AU-01, R-AU-02 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values and \<Organisation\>'s part are outstanding. \<Organisation\>'s logging is expected to be in place, but is not yet seen | None |
| NC-AU-03 | AU | AU-3 Content of Audit Records | Not yet evidenced by \<Organisation\>: EV-AU-04, for the content of Windows records. | E | R-AU-02 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AU-04 | AU | AU-4 Audit Log Storage Capacity | Not yet approved: D-AU-P07. Not yet evidenced: the records per day and bytes per record are not measured, and EV-AU-03 from \<Organisation\> is not seen. | D, E | R-AU-01, R-AU-02 | Low, provisional | Approve; Evidence | The design meets the control; the storage figures are measured in the test environment and the first month of use, and \<Organisation\>'s storage is not yet seen | None |
| NC-AU-05 | AU | AU-5 Response to Logging Failures | Not yet approved: D-AU-01, D-AU-P61. Not yet evidenced by \<Organisation\>: EV-AU-01. | D, E | R-AU-01, R-AU-02, R-AU-03 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values and accepted risk is outstanding. \<Organisation\>'s central monitoring is expected to raise the alert, but is not yet seen | None |
| NC-AU-06 | AU | AU-6 Review, Analysis and Reporting | Not yet approved: D-AU-P08. Not yet evidenced by \<Organisation\>: EV-AU-05. | D, E | R-AU-01, R-AU-02 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values and \<Organisation\>'s records for the comparison are outstanding | None |
| NC-AU-07 | AU | AU-6(1) Automated Process Integration | Not yet evidenced by \<Organisation\>: EV-AU-01. | E | R-AU-02 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AU-08 | AU | AU-6(3) Correlate Repositories | Not yet evidenced by \<Organisation\>: EV-AU-01, EV-AU-05. | E | R-AU-02 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AU-09 | AU | AU-8 Time Stamps | Not yet approved: D-AU-P09. Not yet evidenced by \<Organisation\>: EV-AU-02. | D, E | R-AU-01, R-AU-02 | Low, provisional | Approve; Evidence | The design meets the control, and only the approval of its values and \<Organisation\>'s time source are outstanding | None |
| NC-AU-10 | AU | AU-9 Protection of Audit Information | Not yet evidenced by \<Organisation\>: EV-AU-01, that nobody in \<System Name\>'s team can change or delete logs in central logging. | E | R-AU-02 | Low, provisional | Evidence | The design meets the control within the boundary; the protection of the central copies is \<Organisation\>'s and is not yet seen | None |
| NC-AU-11 | AU | AU-9(4) Access by Subset of Privileged Users | Not yet evidenced by \<Organisation\>: EV-AU-04, for who may change the Windows audit policy. | E | R-AU-02 | Low, provisional | Evidence | \<Organisation\>'s part is expected to be in place, but is not yet seen | None |
| NC-AU-12 | AU | AU-11 Audit Record Retention | Not yet approved: D-AU-P07. Not yet evidenced by \<Organisation\>: EV-AU-01, EV-AU-03, EV-AU-04, EV-AU-05, for how long it keeps the logs \<System Name\> relies on. | D, E | R-AU-01, R-AU-02 | Low, provisional | Approve; Evidence | The design meets the control for the application's records, and only the approval of its values and \<Organisation\>'s retention are outstanding | None |
| NC-AU-13 | AU | AU-12 Audit Record Generation | Not yet evidenced by \<Organisation\>: EV-AU-04, EV-AU-05. | E | R-AU-02 | Low, provisional | Evidence | The application, SQL Server settings and selection are designed; \<Organisation\>'s logging is expected to be in place, but is not yet seen | None |
| NC-CA-01 | CA | CA-1 Policy and Procedures | \<Policy\> (CA) is not yet approved by the Head of Cyber, nor \<Procedures\> (CA) by the system owner. Not yet evidenced by \<Organisation\>: EV-GEN-04. | D, E | R-CA-01, R-CA-02 | Low, provisional | Approve; Evidence | The policy and procedures are written, and only their approval is outstanding. \<Organisation\>'s policies are expected to apply, but are not yet seen | None |
| NC-CA-02 | CA | CA-2 Control Assessments | Not yet operated: no assessment plan is approved and no assessment has been run, so \<Control Assessment Record\> and \<Security Assessment Report\> are not filled. Not yet appointed: the Level 1 assessor. | D | R-CA-01 | Low | Approve | The assessment is designed; it runs under PRO-CA-1 once the plan is approved, before authorisation | None |
| NC-CA-03 | CA | CA-2(1) Independent Assessors | Not yet approved: D-CA-01. Not yet appointed: the Level 2 team, and no TPL-19 is completed or accepted. | D | R-CA-01 | Low | Approve | The independence test and form are designed; only the appointment is outstanding | None |
| NC-CA-04 | CA | CA-3 Information Exchange | Not yet approved: D-CA-02, the interface record. Not yet evidenced by \<Organisation\>: EV-CA-02. | D, E | R-CA-01, R-CA-02 | Low, provisional | Approve; Evidence | The exchanges are recorded with their security and privacy needs; the approval and \<Organisation\>'s agreement are outstanding | None |
| NC-CA-05 | CA | CA-5 Plan of Action and Milestones | Not yet operated: no assessment has yet produced weaknesses to plan, and the Risk List's POA&M references are not yet checked against the plan (R-AC-01 names \[PA-nn\], pending its decision). | D | R-CA-01 | Low | Approve | The plan, its update cycle and its time limits are designed; it fills as assessments run | None |
| NC-CA-06 | CA | CA-6 Authorization | Not yet appointed: the authorising official. Not yet approved: D-CA-P25. Not yet operated: no TPL-18. Not yet evidenced by \<Organisation\>: EV-CA-01, its common control official and their authorisation. | D, E | R-CA-01, R-CA-02 | Low, provisional | Approve; Evidence | The package, decision form and inherited-control acceptance are designed; the appointment, approval and \<Organisation\>'s authorisation are outstanding | None |
| NC-CA-07 | CA | CA-7 Continuous Monitoring | Not yet operated: monitoring starts at go-live. Not yet evidenced by \<Organisation\>: EV-PM-03, the strategy this one carries out. | D, E | R-CA-01, R-CA-02 | Low, provisional | Approve; Evidence | The strategy, measures and reporting are designed; \<Organisation\>'s strategy is not yet seen | None |
| NC-CA-08 | CA | CA-7(1) Independent Assessment | Not yet appointed: the independent assessor, with TPL-19. | D | R-CA-01 | Low | Approve | The yearly independent check is designed; only the appointment is outstanding | None |
| NC-CA-09 | CA | CA-9 Internal Connections | Not yet approved: D-CA-02, the interface record for F3, F4 and F5. | D | R-CA-01 | Low | Approve | The internal connections are recorded; only the system owner's approval is outstanding | None |
| \[NC-XX-nn\] | \[XX\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] |
