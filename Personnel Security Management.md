# \<DocuView\> Personnel Security Management

**\<ref\> | Version \<ver\> | Draft for the system owner's approval**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Summary](#3-summary)

[4 The design](#4-the-design)

[5 Each control and enhancement](#5-each-control-and-enhancement)

[Appendix A Parameter register](#appendix-a-parameter-register)

[Appendix B PS controls outside the Moderate baseline](#appendix-b-ps-controls-outside-the-moderate-baseline)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Personnel Security Management |
| Version | \<ver\> |
| Status | Draft for the system owner's approval |
| Date | 17 November 2026 |
| Owner | System owner |
| Applies to | Personnel Security family |
| Classification | Restricted |
| Next review | Every 12 months, and when a role's access changes |
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
| \<ver\> | 17 November 2026 | The system owner's decisions on the cross-check (D-PS-12): the security assessor is higher risk; register entries are kept while the person has access and for 3 years after, and leaver and mover records for 3 years |
| \<ver\> | 17 November 2026 | Cross-check against NIST's guidance for the family: the independent assessors are covered as external people and entered in the register; the retention of the register and of leaver records is shown as not yet set; the basic criminal record check is explained for the United Kingdom; PS-6 is shown as in the privacy baseline too; and the PS controls outside the Moderate baseline are listed in a new appendix B |
| \<ver\> | 17 November 2026 | The system owner's decisions on the review (D-PS-11): the leaver row notes the monthly removal of members who have not signed in for 90 days |
| \<ver\> | 17 November 2026 | First draft |
| \<ver\> | 17 November 2026 | First draft, at the system owner's request (D-PS-10). The personnel security chapter of \<Control Implementation Register\> moved here in full, so that this design is held only in this document, and each control is set out part by part. Joiners, movers and leavers follow sign-in through AD FS: \<DocuView\> holds no accounts, and a leaver's access ends when ABC Technologies disables their Active Directory account (D-AC-23). No agreed value is changed |

| **SECTION 2** |
| --- |

## 2 Purpose

This document shows how \<DocuView\> makes sure the people who use and run it are trustworthy, and stay so, for each of the 9 Personnel Security (PS) controls in the NIST SP 800-53 Rev 5 Moderate baseline. Section 4 sets out the design: the risk designation of every role, the minimum screening, the access agreements, what happens when people join, move and leave, the time limits, external people, sanctions, the personnel security register, and what ABC Technologies provides. Section 5 takes each control in turn. Appendix A lists every value NIST asks the organisation to define, and appendix B the PS controls NIST does not select at Moderate.

This is the only place this design is held. Other documents point here. The policy is in \<Policy\> (PS), and the steps people follow are in \<Procedures\> (PS). How access is requested, granted and removed is in \<Access Control Management\>, and the duties of each role are in \<Roles and Responsibilities\>.

Screening, HR and disciplinary processes belong to ABC Technologies. \<DocuView\> sets the minimum it requires of them, records only that each check was confirmed and when, and relies on ABC Technologies' evidence for the rest.

An assessor examines the designations, the screening confirmations, the signed agreements and the leaver and mover records; follows one leaver and one mover from notice to the change in access; and interviews those who act on them (NIST SP 800-53A). So for each control section 5 gives:

- **each part of the control**, as NIST letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Table 4: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet, or it is not evidenced |

| **SECTION 3** |
| --- |

## 3 Summary

Of the 9 controls, none is fully implemented, 2 are partially implemented and 7 are not implemented. No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

**Table 5: Status of each control**

| Control | Title | Status | What is missing | Registered as |
| --- | --- | --- | --- | --- |
| PS-1 | Policy and Procedures | Partially implemented | Not yet shared. The later version awaits the Head of Cyber | NC-PS-01; PA-20 |
| PS-2 | Position Risk Designation | Not implemented | ABC Technologies' screening criteria have not been seen | NC-PS-02; PA-125, EV-PS-01 |
| PS-3 | Personnel Screening | Not implemented | ABC Technologies' screening is not evidenced, and the register has no screening dates | NC-PS-03; PA-125, EV-PS-01 |
| PS-4 | Personnel Termination | Not implemented | The Starters/Leavers prompt is not set up, and the exit process is not evidenced | NC-PS-04; PA-32, PA-125, EV-PS-02 |
| PS-5 | Personnel Transfer | Not implemented | The Starters/Leavers prompt is not set up | NC-PS-05; PA-32 |
| PS-6 | Access Agreements | Partially implemented | Nobody has signed. ABC Technologies' confidentiality agreement has not been seen | NC-PS-06; PA-123, PA-125 |
| PS-7 | External Personnel Security | Not implemented | Contract terms have not been seen. Whether the assessment team are external is not recorded | NC-PS-07; PA-125, EV-PS-03 |
| PS-8 | Personnel Sanctions | Not implemented | ABC Technologies' disciplinary process is not evidenced | NC-PS-08; PA-125, EV-PS-02 |
| PS-9 | Position Descriptions | Not implemented | ABC Technologies' job descriptions have not been seen | NC-PS-09; PA-125, EV-PS-02 |

What \<DocuView\> decides for itself is defined: a designation for every role, the minimum screening, the agreements, the time limits and the register. Nobody has access yet, so nothing is in use. What remains is ABC Technologies' evidence of its screening, HR and disciplinary processes (PA-125), the prompt from its Starters/Leavers system that tells the group owners of a mover or leaver (PA-32, rated Medium), and the first signatures.

| **SECTION 4** |
| --- |

## 4 The design

### 4.1 Principles

1. **Check first.** People are screened and sign their agreements before they get access.
2. **Match the risk.** Roles with more power carry a higher risk designation, and more is asked of them.
3. **Act on change.** Access follows people's roles when they move or leave, and fastest where the risk is highest.
4. **Hold only what is needed.** \<DocuView\> records that a check was passed, never the result of the check.

These carry out the principles and rules of \<Policy\>, sections PS.3 and PS.4.

### 4.2 Risk designations

Every role in \<Roles and Responsibilities\> has a designation. A role is higher risk if it has privileged technical access, or can see or change security records. The plan consistency test (check L17) confirms that no role is missed.

**Table 6: Risk designations**

| Role | Designation | Why |
| --- | --- | --- |
| System owner | Standard | Approves and decides, but holds no privileged technical access |
| Head of Cyber | Standard | Approves policies; no \<DocuView\> account is needed |
| Legal adviser | Standard | Advises and reviews; no privileged access |
| Data protection officer | Standard | Advises; no privileged access |
| Business and information owner | Standard | Owns the information; a user in their own projects |
| Authorising official | Standard | Decides risk; no \<DocuView\> account is needed |
| Security assessor | Higher risk | Sees the whole document set and its evidence, which describe every weakness. Made higher risk on 17 November 2026 (D-PS-12) |
| ABC Technologies security contact | Standard | Provides evidence; no \<DocuView\> account is needed |
| Global administrator | Higher risk | Manages every project, the AD groups each uses, and every session |
| Administrator | Higher risk | Changes system settings |
| Auditor | Higher risk | Reads every audit record |
| Security officer | Higher risk | Sees logs, alerts and incident records |
| Project access approver | Standard | Decides who may see a project, but cannot grant access alone |
| Windows server administrator | Higher risk | Full control of both VMs |
| Database administrator | Higher risk | Full control of the database that holds every document |
| Developers | Higher risk | Change the code that handles HR documents, and have held the secrets in PA-19 |
| Document reader | Standard | Reads documents in their own projects |
| Project editor | Standard | Uploads and exports within their own projects |
| Line manager | Standard | Requests access for others; no access of their own is implied |

A higher risk role adds three things: screening is confirmed again before the role is granted and every 5 years; role training is completed first (\<Awareness and Training Management\>, section 4.5); and access is ended within 1 hour when the holder leaves.

### 4.3 Screening standard

ABC Technologies screens its staff. \<DocuView\> relies on that screening, and sets the minimum it must cover before anyone is given access. The four checks are those of the HMG Baseline Personnel Security Standard.

**Table 7: Minimum screening before \<DocuView\> access**

| Check | What it confirms | ABC Technologies' practice |
| --- | --- | --- |
| Identity | The person is who they say they are | \[ABC Technologies' standard and evidence\] (EV-PS-01) |
| Right to work | They may lawfully work in the UK | \[ABC Technologies' standard and evidence\] (EV-PS-01) |
| Employment history | Their recent employment is as stated | \[ABC Technologies' standard and evidence\] (EV-PS-01) |
| Basic criminal record check | Unspent convictions only | \[ABC Technologies' standard and evidence\] (EV-PS-01) |

\<DocuView\> records only that ABC Technologies confirmed the screening, and the date. It never holds a screening result or criminal record data (\<Policy\> (PS), R4). If ABC Technologies' standard is fuller, for example BS 7858:2019, that standard applies.

In the United Kingdom a basic criminal record check is made through the Disclosure and Barring Service in England and Wales, Disclosure Scotland or AccessNI, and shows only unspent convictions. The Rehabilitation of Offenders Act 1974 limits what may be asked beyond that, which is why the minimum is a basic check.

### 4.4 Access agreements

Two agreements are signed before access, and again every 12 months and after a material change. NIST places PS-6 in its privacy baseline as well as the Moderate baseline, so the agreements cover privacy too: the rules on personal data are A23 to A29.

1. **ABC Technologies' confidentiality agreement,** signed on employment or engagement.
2. **The rules of behaviour,** \<Security Operating Procedures\>: Part A for everyone, and Part B, the privileged rules, for administrators as well. Each person signs a declaration on TPL-21 that they have read and understood the rules and agree to follow them, and the signature is recorded in the register of signatures (\<Planning Management\>, section 4.5).

### 4.5 Joiners, movers and leavers

\<DocuView\> holds no accounts. A person signs in through AD FS with their Active Directory account, and their access is their membership of \<DocuView\>'s AD groups (\<Access Control Management\>). So joining means being added to a group, and leaving means ABC Technologies disabling the Active Directory account.

![Figure 1: From joining to leaving](figures/psm-figure-1.png)

**Figure 1: From joining to leaving**

**Table 8: Joiners, movers and leavers**

| Event | What happens | Who | Within | Record |
| --- | --- | --- | --- | --- |
| Joiner | The role's designation is looked up; ABC Technologies confirms the screening; the person completes training and signs the agreements; only then do the group owners add them to the groups the role needs | System owner; ABC Technologies; the group owners | Before access | TPL-2; TPL-21; the register |
| Mover | The line manager tells the system owner and the owners of the person's groups. Each owner confirms whether the person still needs the group, and removes or adds memberships. A higher risk role needs screening confirmed again first | Line manager; system owner; the group owners | 1 working day | TPL-14 |
| Leaver | ABC Technologies disables the Active Directory account at once, which ends access. Its Starters/Leavers system tells the group owners, who remove the memberships. A global administrator ends any open session. Any service secret the person knew is changed, and exported files and printouts are recovered or destroyed. Separately, anyone who has not signed in for 90 days is removed from \<DocuView\>'s groups each month (\<Access Control Management\>, under AC-2(3)) | ABC Technologies; the group owners; global administrator; system owner | At once, and memberships within 5 working days | TPL-14 |
| Higher-risk leaver, dismissal or suspected misuse | ABC Technologies' service desk disables the Active Directory account, and a global administrator ends the person's sessions and confirms none remains | ABC Technologies' service desk; global administrator | 1 hour of notice | TPL-14; TPL-10 if it is an incident |

### 4.6 Time limits

**Table 9: Personnel security time limits**

| Event | Limit | Who acts | Record |
| --- | --- | --- | --- |
| Screening confirmed and agreements signed | Before the person is added to any \<DocuView\> group | System owner | TPL-2; TPL-21 |
| Leaver | ABC Technologies disables the Active Directory account at once, which ends access; group memberships removed within 5 working days | ABC Technologies; the owners of the person's groups | TPL-14 |
| Higher-risk leaver, dismissal or suspected misuse | Active Directory account disabled, and sessions ended, within 1 hour of notice | ABC Technologies' service desk; global administrator | TPL-14; TPL-10 if it is an incident |
| Mover | Access reviewed, and the system owner told, within 1 working day | Line manager, system owner, the owners of the person's groups | TPL-14 |
| Supplier's leaver or mover | Supplier tells the system owner within 1 working day | Supplier | TPL-14 |
| Formal sanction involving \<DocuView\> | System owner told within 1 working day | ABC Technologies | TPL-10 if it is an incident |
| Agreements signed again | Every 12 months, and after a material change to the rules | Everyone | TPL-21 |
| Designations and agreements reviewed | Every 12 months, and when a role's access changes | System owner | TPL-3 |
| Rescreening for higher risk roles | Every 5 years, and before the role is granted | ABC Technologies | Personnel security register |

### 4.7 External people

People who are not ABC Technologies' staff, such as contracted developers or a supplier's engineer, may hold a \<DocuView\> role only on the same terms as staff: screened to the minimum in section 4.3, signed up to the agreements in section 4.4, and designated by their role. Each contract states their security duties, and requires the supplier to tell the system owner within 1 working day when one of its people moves or leaves.

The same applies to the independent assessors who carry out the Level 2 assessment, as they see the whole document set and its evidence, which describe \<DocuView\>'s weaknesses. Any member of the team who is not ABC Technologies' staff is screened, signs a confidentiality agreement and Part A of the rules of behaviour, and is entered in the register, before the evidence is shared: \[whether the assessment team are ABC Technologies' staff or external\] (PA-125). The system owner checks each supplier's compliance every 12 months, and records it on TPL-16.

### 4.8 Sanctions

A breach of the rules is handled through ABC Technologies' disciplinary process, and the rules of behaviour tell each person so. ABC Technologies tells the system owner within 1 working day when a formal sanction involves \<DocuView\>. If the breach is a security incident, the security officer records it on TPL-10, and the system owner decides whether the person's access must end at once.

### 4.9 Personnel security register

The system owner keeps this register for everyone who has, or will have, access to \<DocuView\> or its Restricted documents: the system owner, the operating roles in \<Roles and Responsibilities\> and the security assessor. Each user is added when their access is requested. It holds dates only. Entries are kept while the person has access, and for 3 years after it ends. Leaver and mover records on TPL-14 are kept for 3 years. The system owner set both on 17 November 2026 (D-PS-12). Signatures of the rules of behaviour are recorded in the register of signatures (\<Planning Management\>, section 4.5).

**Table 10: Personnel security register**

| Person | Role | Designation | Screening confirmed by ABC Technologies | Agreements signed | Next review |
| --- | --- | --- | --- | --- | --- |
| Neil Ramsbottom | System owner | Standard | \[Date\] | None yet | November 2027 |
| Talha Chris | Global administrator | Higher risk | \[Date\] | None yet | November 2027 |
| Alan Craig | Administrator | Higher risk | \[Date\] | None yet | November 2027 |
| Terry Hard | Auditor | Higher risk | \[Date\] | None yet | November 2027 |
| James Preston | Security officer | Higher risk | \[Date\] | None yet | November 2027 |
| Tony Tilley | Project access approver | Standard | \[Date\] | None yet | November 2027 |
| Jake Howard | Windows server administrator | Higher risk | \[Date\] | None yet | November 2027 |
| Richard McCaron | Database administrator | Higher risk | \[Date\] | None yet | November 2027 |
| Lee Martin | Developer | Higher risk | \[Date\] | None yet | November 2027 |
| Ryan Giggs | Developer | Higher risk | \[Date\] | None yet | November 2027 |
| Joe Allen | Developer | Higher risk | \[Date\] | None yet | November 2027 |
| Josh Leak | Security assessor | Higher risk | \[Date\] | None yet | November 2027 |

### 4.10 What ABC Technologies provides

**Table 11: Asked of ABC Technologies**

| Provided | Controls | What \<DocuView\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Pre-employment screening | PS-2, PS-3 | Each person is screened to at least the minimum in section 4.3, rescreened as section 4.6 says, and confirmed to the system owner with the date only | EV-PS-01 | Not sent |
| Starters, movers and leavers | PS-4, PS-5 | A leaver's Active Directory account is disabled at once, and the group owners are told of every mover and leaver | EV-AC-01; PA-32 | Not sent; the prompt is not set up |
| Exit interviews, equipment, discipline and job descriptions | PS-4, PS-8, PS-9 | Exit interviews cover confidentiality, equipment is recovered, sanctions are notified, and job descriptions refer to the duties in \<Roles and Responsibilities\> | EV-PS-02 | Not sent |
| The confidentiality agreement | PS-6 | Every person signs it before access | EV-PS-02 | Not sent |
| Contract terms for external people | PS-7 | Contracts require the same personnel security, and notice of movers and leavers within 1 working day | EV-PS-03 | Not sent |

**Today:** no request has been sent, and none of this is evidenced (PA-125).

| **SECTION 5** |
| --- |

## 5 Each control and enhancement

The controls are in NIST order. Each has two tables. The first takes each part of the control and gives what NIST requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 5.1 PS-1 Policy and Procedures

**Table 12: PS-1 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A personnel security policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (PS): a system-level policy, shared with everyone who administers \<DocuView\> and every line manager of a \<DocuView\> user. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-PS-01) and legally reviewed on 12 November 2026. The later version awaits the Head of Cyber (D-PS-08). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (PS): seven procedures, PRO-PS-1 to PRO-PS-7. Shared with the same people | Approved by the system owner (D-PS-09). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | Neil Ramsbottom is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 12 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 13: PS-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy (\<Policy\>, section PS.4); PRO-PS-7 (\<Procedures\>) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-PS-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-PS-08) |

### 5.2 PS-2 Position Risk Designation

**Table 14: PS-2 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Assign a risk designation to every organisational position | Every role in \<Roles and Responsibilities\> is designated higher risk or standard (section 4.2). A role is higher risk if it has privileged technical access, or can see or change security records | Done for all 19 roles (D-PS-07). The plan consistency test confirms that none is missed (check L17). The security assessor was made higher risk on 17 November 2026 (D-PS-12) |
| b | Set screening criteria for the people who fill each position | Every person: identity, right to work, employment history and a basic criminal record check, before access (section 4.3). Higher risk roles: the same, confirmed again before the role is granted and every 5 years | Set. ABC Technologies' own criteria have not been seen (EV-PS-01) |
| c | Review and update the designations on a schedule | Every 12 months, and when a role's access changes | Reviewed on 12 November 2026. The first yearly review falls due in November 2027 |

**Table 15: PS-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R1 (\<Policy\>, section PS.4); PRO-PS-1, PRO-PS-4 (\<Procedures\>) |
| Tests | The plan consistency test, check L17: every role in \<Roles and Responsibilities\> has a designation. It passes |
| Records an assessor will ask for | The designations, and the record of their review on TPL-3 |
| Status | Not implemented |
| Risk decision | NC-PS-02, rated Low: approve |
| Open items | PA-125: obtain ABC Technologies' screening criteria (EV-PS-01) |

### 5.3 PS-3 Personnel Screening

**Table 16: PS-3 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Screen people before giving them access to the system | ABC Technologies screens each person before employment. Before anyone is added to a \<DocuView\> group, the system owner has ABC Technologies confirm that the person passed, and that the screening covered the minimum in section 4.3. Only the confirmation and its date are recorded (section 4.9) | Nobody has access yet. ABC Technologies' screening has not been evidenced (EV-PS-01), and the screening dates in the register are placeholders |
| b | Rescreen people under defined conditions and at a defined frequency | Before someone moves into a higher risk role, and every 5 years for anyone in one | Not yet used. ABC Technologies' practice has not been seen (EV-PS-01) |

**Table 17: PS-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | Not a system function. ABC Technologies' pre-employment checks |
| Rules and procedures | Policy rules R2, R3, R4 (\<Policy\>, section PS.4); PRO-PS-1 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | ABC Technologies' screening standard, and its confirmation, with the date only, for each person with \<DocuView\> access (EV-PS-01); the personnel security register |
| Status | Not implemented |
| Risk decision | NC-PS-03, rated Low: obtain evidence |
| Open items | PA-125: obtain ABC Technologies' evidence, and fill in the screening dates |

### 5.4 PS-4 Personnel Termination

**Table 18: PS-4 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Disable system access within a defined time of a person leaving | \<DocuView\> holds no accounts of its own: a person reaches it with their Active Directory account. ABC Technologies disables that account at once, which ends their access to \<DocuView\>. The owners of the person's groups remove the memberships within 5 working days. For a higher-risk leaver, a dismissal or suspected misuse, the account is disabled and the person's sessions ended within 1 hour of notice (section 4.5) | Not in use. The prompt from ABC Technologies' Starters/Leavers system is not set up (PA-32) |
| b | Terminate or revoke the authenticators and credentials the person held | Disabling the Active Directory account revokes the password and the second factor. A global administrator ends any session still open. Any service secret the person knew is changed (\<Procedures\>, PRO-IA-4) | Not in use. The service secrets are in settings files today (PA-19) |
| c | Hold an exit interview that covers defined information security topics | ABC Technologies holds the exit interview. It covers the person's continuing confidentiality duties, and returning equipment | Not evidenced (EV-PS-02) |
| d | Retrieve all security-related property | ABC Technologies recovers the person's laptop, phone, pass and any other equipment. Any exported files or printouts are recovered or destroyed (\<Security Operating Procedures\>, section 5.4) | Not evidenced (EV-PS-02) |
| e | Keep access to the information and systems the person controlled | Documents belong to projects, not to people, so a leaver's documents stay with the project and its members. The system owner confirms this on TPL-14 | Not yet used |

**Table 19: PS-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | Global administrator, ABC Technologies |
| Enforced by | Active Directory: a disabled account cannot sign in through AD FS. \<DocuView\>'s session service, which a global administrator uses to end sessions |
| Rules and procedures | Policy rules R5, R6 (\<Policy\>, section PS.4); PRO-PS-2, with PRO-AC-3 and PRO-AC-4 (\<Procedures\>) |
| Tests | None for this family. Ending a person's sessions was shown in the test environment under the incident response drill (D01) |
| Records an assessor will ask for | TPL-14 for a sample of leavers, with the times compared with ABC Technologies' record of disabling the account and \<DocuView\>'s audit records; ABC Technologies' exit process (EV-PS-02). None exist yet |
| Status | Not implemented |
| Risk decision | NC-PS-04, rated Low: remediate |
| Open items | PA-32: the Starters/Leavers prompt. PA-125: ABC Technologies' exit process. PA-19: move the service secrets out of the settings files |

### 5.5 PS-5 Personnel Transfer

**Table 20: PS-5 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | When someone is reassigned, review and confirm their continuing need for their current logical and physical access | The line manager tells the system owner and the owners of the person's groups. Each owner confirms whether the person still needs that group. No \<DocuView\> role gives physical access to the servers (\<Physical and Environmental Protection Management\>, section 4.2) | Not in use (PA-32) |
| b | Start defined transfer actions within a defined time | A review of access, and any change needed, within 1 working day. If the new role is higher risk, screening is confirmed again before it is granted | Not in use (PA-32) |
| c | Change access as needed to match the new role | The owners remove the memberships no longer needed, and add any the new role needs through an access request. A change to a person's groups takes effect at their next sign-in, and a global administrator can end their sessions to bring it in at once (\<Identification and Authentication Management\>, section 4.7) | Not yet used |
| d | Tell defined people within a defined time | The system owner, within 1 working day | Not in use (PA-32) |

**Table 21: PS-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, global administrator |
| Enforced by | Not a system function. Active Directory groups, changed only by their owners |
| Rules and procedures | Policy rule R7 (\<Policy\>, section PS.4); PRO-PS-3, with PRO-AC-2 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-14 for a sample of movers, with the changes to their groups. None exist yet |
| Status | Not implemented |
| Risk decision | NC-PS-05, rated Low: remediate |
| Open items | PA-32: the Starters/Leavers prompt |

### 5.6 PS-6 Access Agreements

**Table 22: PS-6 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Develop and document access agreements | Two agreements (section 4.4): ABC Technologies' confidentiality agreement, and the rules of behaviour in \<Security Operating Procedures\>, Part A for everyone and Part B for administrators. They cover privacy as well as security, as PS-6 is in the privacy baseline too | The rules of behaviour are approved (D-PL-05). ABC Technologies' confidentiality agreement has not been seen (EV-PS-02) |
| b | Review and update the agreements on a schedule | Every 12 months | The first review falls due in November 2027 |
| c.1 | Verify that people sign the agreements before they are given access | Each person signs before being added to any \<DocuView\> group. Their signature of the rules is recorded on TPL-21 and in the register of signatures (\<Planning Management\>, section 4.5), which the access request checks | Nobody has signed yet (PA-123) |
| c.2 | Verify that people sign again when the agreements change, or at a defined frequency | Every 12 months, and after a material change to the rules: a new or stricter rule, a changed consequence, new monitoring or a new privileged duty | Nobody has signed yet |

**Table 23: PS-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, everyone |
| Enforced by | Not a system function. An access request is not approved without a signature in the register |
| Rules and procedures | Policy rule R8 (\<Policy\>, section PS.4); PRO-PS-1, PRO-PS-4 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Both agreements; signed TPL-21 forms, checked against the register of signatures and the access requests. None signed yet |
| Status | Partially implemented |
| Risk decision | NC-PS-06, rated Low: approve |
| Open items | PA-123: take the first signatures. PA-125: see ABC Technologies' confidentiality agreement |

### 5.7 PS-7 External Personnel Security

**Table 24: PS-7 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Set personnel security requirements, with security roles and responsibilities, for external providers | External people with a \<DocuView\> role, such as contracted developers or a supplier's engineer, meet the same requirements as staff: screening to the minimum in section 4.3, the agreements in section 4.4, and the rules of behaviour (section 4.7). The independent assessors are covered in the same way, if they are not ABC Technologies' staff | Not evidenced (EV-PS-03). Whether the assessment team are external is not recorded |
| b | Require external providers to comply with the organisation's personnel security policies and procedures | Each contract requires it | Contract terms not seen (EV-PS-03) |
| c | Document the requirements | In each contract, and in this document | Contract terms not seen (EV-PS-03) |
| d | Require providers to report the transfer or departure of any of their people who hold credentials or access, within a defined time | To the system owner, within 1 working day | Contract terms not seen (EV-PS-03) |
| e | Monitor provider compliance | The system owner checks each supplier every 12 months, and records it on TPL-16 | Not yet started |

**Table 25: PS-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, ABC Technologies |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R9 (\<Policy\>, section PS.4); PRO-PS-5 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Standard contract terms (EV-PS-03); the yearly check on TPL-16. None exist yet |
| Status | Not implemented |
| Risk decision | NC-PS-07, rated Low: obtain evidence |
| Open items | PA-125: obtain the contract terms (EV-PS-03) |

### 5.8 PS-8 Personnel Sanctions

**Table 26: PS-8 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| a | Use a formal sanctions process for people who fail to comply with the security and privacy policies and procedures | ABC Technologies' disciplinary process. The rules of behaviour tell each person that a breach may lead to it | Not evidenced (EV-PS-02) |
| b | Tell defined people within a defined time when a formal sanction starts, naming the person and the reason | ABC Technologies tells the system owner within 1 working day when a sanction involves \<DocuView\>. If the breach is a security incident, the security officer records it, and the system owner decides whether access must end at once (section 4.8) | Not yet used |

**Table 27: PS-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | ABC Technologies |
| Responsible | ABC Technologies |
| Enforced by | Not a system function. ABC Technologies' HR |
| Rules and procedures | Policy rule R10 (\<Policy\>, section PS.4); PRO-PS-6 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | ABC Technologies' disciplinary process (EV-PS-02); any notice to the system owner |
| Status | Not implemented |
| Risk decision | NC-PS-08, rated Low: obtain evidence |
| Open items | PA-125: obtain ABC Technologies' evidence (EV-PS-02) |

### 5.9 PS-9 Position Descriptions

**Table 28: PS-9 design**

| Part | NIST requires | Design | Today |
| --- | --- | --- | --- |
| All | Include security and privacy roles and responsibilities in position descriptions | The security and privacy duties of every \<DocuView\> role are stated in \<Roles and Responsibilities\>. ABC Technologies' job descriptions for those roles refer to them | \<Roles and Responsibilities\> states them. ABC Technologies' job descriptions have not been seen (EV-PS-02) |

**Table 29: PS-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<DocuView\> and ABC Technologies |
| Responsible | System owner, ABC Technologies |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R11 (\<Policy\>, section PS.4); PRO-PS-4 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | \<Roles and Responsibilities\>; a sample of ABC Technologies' job descriptions (EV-PS-02) |
| Status | Not implemented |
| Risk decision | NC-PS-09, rated Low: obtain evidence |
| Open items | PA-125: obtain ABC Technologies' evidence (EV-PS-02) |

| **APPENDIX A** |
| --- |

## Appendix A Parameter register

These are NIST's organisation-defined values for the 9 PS entries: 23 in total. They were agreed on 6 November 2026 (D-PS-P01) and revised on 12 November 2026 (D-PS-P02).

**Table 30: PS parameter register**

| NIST identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| PS-01\_ODP\[01\] | Who receives the policy | Everyone who administers \<DocuView\>, and every line manager of a \<DocuView\> user | Not yet shared |
| PS-01\_ODP\[02\] | Who receives the procedures | The same people | Not yet shared |
| PS-01\_ODP\[03\] | Level of the policy | System level | In place |
| PS-01\_ODP\[04\] | Official who manages them | System owner | Neil Ramsbottom is named |
| PS-01\_ODP\[05\] | Policy review frequency | Every 12 months | First review due November 2027 |
| PS-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Reviewed after the whole-set review, 12 November 2026 |
| PS-01\_ODP\[07\] | Procedures review frequency | Every 12 months | First review due November 2027 |
| PS-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Reviewed after the whole-set review, 12 November 2026 |
| PS-02\_ODP | Designation review frequency | Every 12 months, and when a role's access changes | Reviewed 12 November 2026 (section 4.2) |
| PS-03\_ODP\[01\] | When people are rescreened | Before moving into a higher risk role, and at the set frequency | Not yet used; ABC Technologies' practice not seen (EV-PS-01) |
| PS-03\_ODP\[02\] | Rescreening frequency | Every 5 years for higher risk roles | Not yet used; ABC Technologies' practice not seen (EV-PS-01) |
| PS-04\_ODP\[01\] | Time to disable a leaver | 5 working days, on the condition in \<Access Control Management\>, P-AC-06; 1 hour for a higher-risk leaver, a dismissal or suspected misuse | Route not built (PA-32) |
| PS-04\_ODP\[02\] | Exit interview topics | Confidentiality duties, and returning equipment | ABC Technologies' process, not seen (EV-PS-02) |
| PS-05\_ODP\[01\] | What happens on a transfer | Review of access, and any change needed | Not yet used |
| PS-05\_ODP\[02\] | Time to start | 1 working day | Route not built (PA-32) |
| PS-05\_ODP\[03\] | Who is notified | System owner | Not yet used |
| PS-05\_ODP\[04\] | Time to notify | 1 working day | Route not built (PA-32) |
| PS-06\_ODP\[01\] | Agreement review frequency | Every 12 months | First review due November 2027 |
| PS-06\_ODP\[02\] | Re-sign frequency | Every 12 months, and after a material change to the rules | None signed yet |
| PS-07\_ODP\[01\] | Who suppliers notify | System owner | Contract terms not seen (EV-PS-03) |
| PS-07\_ODP\[02\] | Time to notify | 1 working day | Contract terms not seen (EV-PS-03) |
| PS-08\_ODP\[01\] | Who is told of a sanction | System owner | Not yet used |
| PS-08\_ODP\[02\] | Time to tell them | 1 working day | Not yet used |

| **APPENDIX B** |
| --- |

## Appendix B PS controls outside the Moderate baseline

NIST does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 31 says where.

**Table 31: PS controls not selected at Moderate**

| Control | What it adds | \<DocuView\>'s position |
| --- | --- | --- |
| PS-3(1), PS-3(2), PS-6(2) Classified Information; Formal Indoctrination; Classified Information Requiring Special Protection | Clearance, briefing and agreements for access to classified information | Not required. \<DocuView\> holds no classified information |
| PS-3(3) Information Requiring Special Protective Measures | Extra screening for access to information that needs special protection | Not required. HR documents, which hold special category data, are protected by limiting each project to the people approved for it, not by further screening |
| PS-3(4) Citizenship Requirements | Citizenship checks for defined roles | Not required. The right to work check covers lawful employment in the United Kingdom |
| PS-4(1), PS-6(3) Post-employment Requirements | People are told of, and bound by, duties that continue after they leave | Not required. Done in part: the exit interview covers continuing confidentiality duties. Whether ABC Technologies' confidentiality agreement continues after employment is asked with EV-PS-02 |
| PS-4(2) Automated Actions | Automated notice of a leaver, and automated disabling of access | In the High baseline only. Done in design: disabling the Active Directory account ends access to \<DocuView\> at once, and ABC Technologies' Starters/Leavers system is to prompt the group owners (PA-32) |
| PS-6(1) | Withdrawn by NIST: moved into PS-3 | Not applicable |
