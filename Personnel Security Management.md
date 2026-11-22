# \<System Name\> Personnel Security Management

## 1 Purpose

This document sets out how \<System Name\> makes sure the people who use and run it are trustworthy, and stay so, to meet the 9 Personnel Security (PS) controls in the CSS Moderate baseline.

Section 3 is the design: the principles, the risk designation of every role, the minimum screening, the access agreements, what happens when people join, move and leave, the time limits, external people, sanctions, the personnel security register, what \<Organisation\> provides, role duties in job descriptions, and the policy and procedures. Each subsection names the controls it helps to meet.

Screening, HR and disciplinary processes belong to \<Organisation\>. \<System Name\> sets the minimum it requires of them, records only that each check was confirmed and when, and relies on \<Organisation\>'s evidence for the rest. How access is requested, granted and removed is in \<Access Control Management\>, and the duties of each role are in \<Roles and Responsibilities\>.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.13 (Table 22). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (PS). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (PS), and the steps people follow are in \<Procedures\> (PS).

## 3 The design

### 3.1 Principles

Controls met here: PS-2, PS-3, PS-4, PS-5, PS-6.

1. **Check first.** People are screened and sign their agreements before they get access.
2. **Match the risk.** Roles with more power carry a higher risk designation, and more is asked of them.
3. **Act on change.** Access follows people's roles when they move or leave, and fastest where the risk is highest.
4. **Hold only what is needed.** \<System Name\> records that a check was passed, never the result of the check.

These carry out the principles and rules of \<Policy\>, sections PS.3 and PS.4.

### 3.2 Risk designations

Controls met here: PS-2, PS-3.

Every role in \<Roles and Responsibilities\> has a designation. A role is higher risk if it has privileged technical access, or can see or change security records. The plan consistency test confirms that no role is missed.

**Table 1: Risk designations**

| Role | Designation | Why |
| --- | --- | --- |
| System owner | Standard | Approves and decides, but holds no privileged technical access |
| Head of Cyber | Standard | Approves policies; no \<System Name\> account is needed |
| Legal adviser | Standard | Advises and reviews; no privileged access |
| Data protection officer | Standard | Advises; no privileged access |
| Business and information owner | Standard | Owns the information; a user in their own schemas |
| Authorising official | Standard | Decides risk; no \<System Name\> account is needed |
| Security assessor | Higher risk | Sees the whole document set and its evidence, which describe every weakness |
| \<Organisation\> security contact | Standard | Provides evidence; no \<System Name\> account is needed |
| Administrator | Higher risk | Manages schemas, which Active Directory groups open each schema, and system settings, and opens no item content. This is the one administrator role |
| Auditor | Higher risk | Reads every audit record |
| Security officer | Higher risk | Sees logs, alerts and incident records |
| Data Owner | Standard | Owns a schema's data and its read and edit groups, and authorises who may read or edit it in ServiceNow; nobody approves their own access |
| Business owner, in the application | Standard | Approves, in the UI application, the disposal of items due under the retention schedule (\<System Description\>, FR-074); a member of \<Code\>\_BusinessOwners; no privileged technical access |
| Legal adviser's delegate | Higher risk | Searches every schema for one person's items to answer a request under data protection law (\<System Description\>, FR-073), so can see items in every schema; a member of \<Code\>\_LegalSearch, named by the legal adviser; holds no other role |
| Windows server administrator | Higher risk | Full control of both servers |
| Database administrator | Higher risk | Full control of the database that holds every item |
| Developers | Higher risk | Change the code that handles every item, including personal data; hold no administrator access on the servers |
| Reader | Standard | Searches and reads items in their own schemas |
| Editor | Standard | Creates, uploads, manages and exports items within their own schemas |
| Line manager | Standard | Requests access for others; no access of their own is implied |

A higher risk role adds three things: screening is confirmed again before the role is granted and every 5 years; role training is completed first (\<Awareness and Training Management\>, section 3.5); and access is ended within 1 hour when the holder leaves.

### 3.3 Screening standard

Controls met here: PS-2, PS-3.

\<Organisation\> screens its staff. \<System Name\> relies on that screening, and sets the minimum it must cover before anyone is given access. The four checks are those of the HMG Baseline Personnel Security Standard.

**Table 2: Minimum screening before \<System Name\> access**

| Check | What it confirms | \<Organisation\>'s practice |
| --- | --- | --- |
| Identity | The person is who they say they are | \[\<Organisation\>'s standard and evidence\] (EV-PS-01) |
| Right to work | They may lawfully work in the UK | \[\<Organisation\>'s standard and evidence\] (EV-PS-01) |
| Employment history | Their recent employment is as stated | \[\<Organisation\>'s standard and evidence\] (EV-PS-01) |
| Basic criminal record check | Unspent convictions only | \[\<Organisation\>'s standard and evidence\] (EV-PS-01) |

\<System Name\> records only that \<Organisation\> confirmed the screening, and the date. It never holds a screening result or criminal record data (\<Policy\> (PS), R4). If \<Organisation\>'s standard is fuller, for example BS 7858:2019, that standard applies.

In the United Kingdom a basic criminal record check is made through the Disclosure and Barring Service in England and Wales, Disclosure Scotland or AccessNI, and shows only unspent convictions. The Rehabilitation of Offenders Act 1974 limits what may be asked beyond that, which is why the minimum is a basic check.

### 3.4 Access agreements

Controls met here: PS-6.

Two agreements are signed before access, and again every 12 months and after a material change. CSS places PS-6 in its privacy baseline as well as the Moderate baseline, so the agreements cover privacy too: the rules on personal data are A23 to A29.

1. **\<Organisation\>'s confidentiality agreement,** signed on employment or engagement.
2. **The rules of behaviour,** \<Security Operating Procedures\>: Part A for everyone, and Part B, the privileged rules, for privileged users as well. Each person signs a declaration on TPL-21 that they have read and understood the rules and agree to follow them, and the signature is recorded in the register of signatures (\<Planning Management\>, section 3.5).

Each person signs both before being added to any \<System Name\> group. The ServiceNow access request checks the register of signatures, and is not approved without a signature in it. The system owner reviews and updates the agreements every 12 months.

### 3.5 Joiners, movers and leavers

Controls met here: PS-3, PS-4, PS-5, PS-6.

\<System Name\> holds no accounts. A person signs in through PingFederate with their Active Directory account, and the API reads their membership of \<System Name\>'s Active Directory groups directly from Active Directory over LDAPS; that membership is their access (\<Access Control Management\>). So joining means being added to a group, and leaving means \<Organisation\> disabling the Active Directory account.

![Figure 1: From joining to leaving](figures/psm-figure-1.png)

**Figure 1: From joining to leaving**

**Table 3: Joiners, movers and leavers**

| Event | What happens | Who | Within | Record |
| --- | --- | --- | --- | --- |
| Joiner | The role's designation is looked up; \<Organisation\> confirms the screening; the person completes training and signs the agreements; the access request is authorised in ServiceNow, by the Data Owner for a schema's groups and by the system owner for a role group; only then do the group owners add them to the groups the role needs | System owner; \<Organisation\>; the Data Owner; the group owners | Before access | TPL-2; TPL-21; the register |
| Mover | The line manager tells the system owner and the owners of the person's groups. Each owner confirms whether the person still needs the group, and removes or adds memberships. A higher risk role needs screening confirmed again first | Line manager; system owner; the group owners | 1 working day | TPL-14 |
| Leaver | \<Organisation\> disables the Active Directory account at once, and ends the person's PingFederate sign-in, which ends access. Its starters and leavers process gives notice of the leaver to the group owners, through ServiceNow, and they remove the memberships. Any service secret the person knew is changed, and exported files and printouts are recovered or destroyed. Separately, anyone who has not signed in for 90 days is removed from \<System Name\>'s groups each month (\<Access Control Management\>, section 3.14) | \<Organisation\>; the group owners; system owner | At once, and memberships within 5 working days (\<System Description\>, P-06) | TPL-14 |
| Higher-risk leaver, dismissal or suspected misuse | \<Organisation\>'s service desk disables the Active Directory account and ends the person's PingFederate sign-in, and \<System Name\> refuses the person within 5 minutes, even while a sign-in is open (P-41) | \<Organisation\>'s service desk | 1 hour of notice | TPL-14; TPL-10 if it is an incident |

**Leavers.** Disabling the Active Directory account revokes the person's password and second factor. Any service secret the person knew is changed (\<Procedures\>, PRO-IA-4). \<Organisation\> holds an exit interview, which covers the person's continuing confidentiality duties and the return of equipment, and recovers their laptop, phone, pass and any other equipment. Exported files and printouts are recovered or destroyed (\<Security Operating Procedures\>, section 4.4). Items belong to schemas, not to people, so the items a leaver created stay with the schema and its members. The system owner confirms this on TPL-14.

**Movers.** Each group owner removes the memberships the person no longer needs, and adds any the new role needs through an access request. A change to a person's groups takes effect within 5 minutes, because the API reads them from Active Directory on every request (\<Access Control Management\>, sections 3.14 and 3.15). No \<System Name\> role gives physical access to the servers (\<Physical and Environmental Protection Management\>, section 3.2), so a move changes logical access only.

### 3.6 Time limits

Controls met here: PS-2, PS-3, PS-4, PS-5, PS-6, PS-7, PS-8.

**Table 4: Personnel security time limits**

| Event | Limit | Who acts | Record |
| --- | --- | --- | --- |
| Screening confirmed and agreements signed | Before the person is added to any \<System Name\> group | System owner | TPL-2; TPL-21 |
| Leaver | \<Organisation\> disables the Active Directory account at once, which ends access; group memberships removed within 5 working days (\<System Description\>, P-06) | \<Organisation\>; the owners of the person's groups | TPL-14 |
| Higher-risk leaver, dismissal or suspected misuse | Active Directory account disabled, and PingFederate sign-in ended, within 1 hour of notice | \<Organisation\>'s service desk | TPL-14; TPL-10 if it is an incident |
| Mover | Access reviewed, and the system owner told, within 1 working day | Line manager, system owner, the owners of the person's groups | TPL-14 |
| Supplier's leaver or mover | Supplier tells the system owner within 1 working day | Supplier | TPL-14 |
| Formal sanction involving \<System Name\> | System owner told within 1 working day | \<Organisation\> | TPL-10 if it is an incident |
| Agreements signed again | Every 12 months, and after a material change to the rules | Everyone | TPL-21 |
| Designations and agreements reviewed | Every 12 months, and when a role's access changes | System owner | TPL-3 |
| Rescreening for higher risk roles | Every 5 years, and before the role is granted | \<Organisation\> | Personnel security register |

### 3.7 External people

Controls met here: PS-7.

People who are not \<Organisation\>'s staff, such as contracted developers or a supplier's engineer, may hold a \<System Name\> role only on the same terms as staff: screened to the minimum in section 3.3, signed up to the agreements in section 3.4, and designated by their role. Each contract states these requirements and their security duties, requires the supplier and its people to comply with \<Policy\> (PS) and \<Procedures\> (PS), and requires the supplier to tell the system owner within 1 working day when one of its people moves or leaves.

The same applies to the independent assessors who carry out the Level 2 assessment, as they see the whole document set and its evidence, which describe \<System Name\>'s weaknesses. Any member of the team who is not \<Organisation\>'s staff is screened, signs a confidentiality agreement and Part A of the rules of behaviour, and is entered in the register, before the evidence is shared: \[whether the assessment team are \<Organisation\>'s staff or external\]. The system owner checks each supplier's compliance every 12 months, and records it on TPL-16.

### 3.8 Sanctions

Controls met here: PS-8.

A breach of the rules is handled through \<Organisation\>'s disciplinary process, and the rules of behaviour tell each person so. \<Organisation\> tells the system owner within 1 working day when a formal sanction involves \<System Name\>. If the breach is a security incident, the security officer records it on TPL-10, and the system owner decides whether the person's access must end at once.

### 3.9 Personnel security register

Controls met here: PS-3, PS-6.

The system owner keeps this register for everyone who has, or will have, access to \<System Name\> or its Restricted documents: the system owner, the operating roles in \<Roles and Responsibilities\> and the security assessor. Each user is added when their access is requested. It holds dates only. Entries are kept while the person has access, and for 3 years after it ends. Leaver and mover records on TPL-14 are kept for 3 years. Signatures of the rules of behaviour are recorded in the register of signatures (\<Planning Management\>, section 3.5).

**Table 5: Personnel security register**

| Person | Role | Designation | Screening confirmed by \<Organisation\> | Agreements signed | Next review |
| --- | --- | --- | --- | --- | --- |
| \[Name\] | \[Role\] | \[Standard or Higher risk\] | \[Date\] | \[Date\] | \[Date\] |

### 3.10 What \<Organisation\> provides

Controls met here: PS-2, PS-3, PS-4, PS-5, PS-6, PS-7, PS-8, PS-9.

**Table 6: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Pre-employment screening | PS-2, PS-3 | Each person is screened to at least the minimum in section 3.3, rescreened as section 3.6 says, and confirmed to the system owner with the date only | EV-PS-01 |
| Starters, movers and leavers | PS-4, PS-5 | A leaver's Active Directory account is disabled at once, and the group owners are told of every mover and leaver | EV-AC-01 |
| Exit interviews, equipment, discipline and job descriptions | PS-4, PS-8, PS-9 | Exit interviews cover confidentiality, equipment is recovered, sanctions are notified, and job descriptions refer to the duties in \<Roles and Responsibilities\> | EV-PS-02 |
| The confidentiality agreement | PS-6 | Every person signs it before access | EV-PS-02 |
| Contract terms for external people | PS-7 | Contracts require the same personnel security, and notice of movers and leavers within 1 working day | EV-PS-03 |

### 3.11 Role duties in job descriptions

Controls met here: PS-9.

The security and privacy duties of every \<System Name\> role are stated in \<Roles and Responsibilities\>. \<Organisation\>'s job descriptions for those roles refer to them (EV-PS-02).

### 3.12 Policy and procedures

Controls met here: PS-1.

\<Policy\> (PS) and \<Procedures\> (PS) meet PS-1. Who they are shared with is in \<Policy\>, section PS.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
