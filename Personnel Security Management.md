# \<System Name\> Personnel Security Management

## 1 Purpose

This document sets out how \<System Name\> makes sure the people who use and run it are trustworthy, and stay so, to meet the 9 Personnel Security (PS) controls in the CSS Moderate baseline.

Section 3 is the design: the principles, the risk designation of every role, the minimum screening, the access agreements, what happens when people join, move and leave, the time limits, external people, sanctions, the personnel security register, what \<Organisation\> provides, role duties in job descriptions, and the policy and procedures. Each subsection names the controls it helps to meet. Appendix A lists the PS controls CSS does not select at Moderate.

Screening, HR and disciplinary processes belong to \<Organisation\>. \<System Name\> sets the minimum it requires of them, records only that each check was confirmed and when, and relies on \<Organisation\>'s evidence for the rest. How access is requested, granted and removed is in \<Access Control Management\>, and the duties of each role are in \<Roles and Responsibilities\>.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.13 (Table 22). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (PS). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (PS), and the steps people follow are in \<Procedures\> (PS).

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. The values in section 3, such as the time limits, the rescreening interval and how long records are kept, should match those corporate values. Where one does not, it is changed in this document.

Where section 3 notes what "today" is, it means the tested v1.0 build, which nobody yet has access to.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.13 (Table 22).

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

Every role in \<Roles and Responsibilities\> has a designation. A role is higher risk if it has privileged technical access, or can see or change security records. The plan consistency test (check L17) confirms that no role is missed.

**Table 1: Risk designations**

| Role | Designation | Why |
| --- | --- | --- |
| System owner | Standard | Approves and decides, but holds no privileged technical access |
| Head of Cyber | Standard | Approves policies; no \<System Name\> account is needed |
| Legal adviser | Standard | Advises and reviews; no privileged access |
| Data protection officer | Standard | Advises; no privileged access |
| Business and information owner | Standard | Owns the information; a user in their own projects |
| Authorising official | Standard | Decides risk; no \<System Name\> account is needed |
| Security assessor | Higher risk | Sees the whole document set and its evidence, which describe every weakness. Made higher risk on 17 November 2026 (D-PS-12) |
| \<Organisation\> security contact | Standard | Provides evidence; no \<System Name\> account is needed |
| Global administrator | Higher risk | Manages every project and the AD groups each uses |
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
2. **The rules of behaviour,** \<Security Operating Procedures\>: Part A for everyone, and Part B, the privileged rules, for administrators as well. Each person signs a declaration on TPL-21 that they have read and understood the rules and agree to follow them, and the signature is recorded in the register of signatures (\<Planning Management\>, section 3.5).

Each person signs both before being added to any \<System Name\> group. The access request checks the register of signatures, and is not approved without a signature in it. The system owner reviews and updates the agreements every 12 months.

### 3.5 Joiners, movers and leavers

Controls met here: PS-3, PS-4, PS-5, PS-6.

\<System Name\> holds no accounts. A person signs in through PingFederate with their Active Directory account, and their access is their membership of \<System Name\>'s AD groups (\<Access Control Management\>). So joining means being added to a group, and leaving means \<Organisation\> disabling the Active Directory account.

![Figure 1: From joining to leaving](figures/psm-figure-1.png)

**Figure 1: From joining to leaving**

**Table 3: Joiners, movers and leavers**

| Event | What happens | Who | Within | Record |
| --- | --- | --- | --- | --- |
| Joiner | The role's designation is looked up; \<Organisation\> confirms the screening; the person completes training and signs the agreements; only then do the group owners add them to the groups the role needs | System owner; \<Organisation\>; the group owners | Before access | TPL-2; TPL-21; the register |
| Mover | The line manager tells the system owner and the owners of the person's groups. Each owner confirms whether the person still needs the group, and removes or adds memberships. A higher risk role needs screening confirmed again first | Line manager; system owner; the group owners | 1 working day | TPL-14 |
| Leaver | \<Organisation\> disables the Active Directory account at once, and ends the person's PingFederate sign-in, which ends access. Its Starters/Leavers system tells the group owners, who remove the memberships. Any service secret the person knew is changed, and exported files and printouts are recovered or destroyed. Separately, anyone who has not signed in for 90 days is removed from \<System Name\>'s groups each month (\<Access Control Management\>, section 3.14) | \<Organisation\>; the group owners; system owner | At once, and memberships within 5 working days | TPL-14 |
| Higher-risk leaver, dismissal or suspected misuse | \<Organisation\>'s service desk disables the Active Directory account and ends the person's PingFederate sign-in, so \<System Name\> refuses the person at the next group lookup (P-AC-13) | \<Organisation\>'s service desk | 1 hour of notice | TPL-14; TPL-10 if it is an incident |

**Leavers.** Disabling the Active Directory account revokes the person's password and second factor. Any service secret the person knew is changed (\<Procedures\>, PRO-IA-4). \<Organisation\> holds an exit interview, which covers the person's continuing confidentiality duties and the return of equipment, and recovers their laptop, phone, pass and any other equipment. Exported files and printouts are recovered or destroyed (\<Security Operating Procedures\>, section 4.4). Documents belong to projects, not to people, so a leaver's documents stay with the project and its members. The system owner confirms this on TPL-14.

**Movers.** Each group owner removes the memberships the person no longer needs, and adds any the new role needs through an access request. A change to a person's groups takes effect at their next sign-in, and a removed membership is refused at the next group lookup (\<Access Control Management\>, sections 3.14 and 3.15). No \<System Name\> role gives physical access to the servers (\<Physical and Environmental Protection Management\>, section 3.2), so a move changes logical access only.

### 3.6 Time limits

Controls met here: PS-2, PS-3, PS-4, PS-5, PS-6, PS-7, PS-8.

**Table 4: Personnel security time limits**

| Event | Limit | Who acts | Record |
| --- | --- | --- | --- |
| Screening confirmed and agreements signed | Before the person is added to any \<System Name\> group | System owner | TPL-2; TPL-21 |
| Leaver | \<Organisation\> disables the Active Directory account at once, which ends access; group memberships removed within 5 working days | \<Organisation\>; the owners of the person's groups | TPL-14 |
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

The same applies to the independent assessors who carry out the Level 2 assessment, as they see the whole document set and its evidence, which describe \<System Name\>'s weaknesses. Any member of the team who is not \<Organisation\>'s staff is screened, signs a confidentiality agreement and Part A of the rules of behaviour, and is entered in the register, before the evidence is shared: \[whether the assessment team are \<Organisation\>'s staff or external\] (PA-125). The system owner checks each supplier's compliance every 12 months, and records it on TPL-16.

### 3.8 Sanctions

Controls met here: PS-8.

A breach of the rules is handled through \<Organisation\>'s disciplinary process, and the rules of behaviour tell each person so. \<Organisation\> tells the system owner within 1 working day when a formal sanction involves \<System Name\>. If the breach is a security incident, the security officer records it on TPL-10, and the system owner decides whether the person's access must end at once.

### 3.9 Personnel security register

Controls met here: PS-3, PS-6.

The system owner keeps this register for everyone who has, or will have, access to \<System Name\> or its Restricted documents: the system owner, the operating roles in \<Roles and Responsibilities\> and the security assessor. Each user is added when their access is requested. It holds dates only. Entries are kept while the person has access, and for 3 years after it ends. Leaver and mover records on TPL-14 are kept for 3 years. The system owner set both on 17 November 2026 (D-PS-12). Signatures of the rules of behaviour are recorded in the register of signatures (\<Planning Management\>, section 3.5).

**Table 5: Personnel security register**

| Person | Role | Designation | Screening confirmed by \<Organisation\> | Agreements signed | Next review |
| --- | --- | --- | --- | --- | --- |
| \[Name\] | System owner | Standard | \[Date\] | None yet | November 2027 |
| \[Name\] | Global administrator | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Administrator | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Auditor | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Security officer | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Project access approver | Standard | \[Date\] | None yet | November 2027 |
| \[Name\] | Windows server administrator | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Database administrator | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Developer | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Developer | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Developer | Higher risk | \[Date\] | None yet | November 2027 |
| \[Name\] | Security assessor | Higher risk | \[Date\] | None yet | November 2027 |

### 3.10 What \<Organisation\> provides

Controls met here: PS-2, PS-3, PS-4, PS-5, PS-6, PS-7, PS-8, PS-9.

**Table 6: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Pre-employment screening | PS-2, PS-3 | Each person is screened to at least the minimum in section 3.3, rescreened as section 3.6 says, and confirmed to the system owner with the date only | EV-PS-01 | Not sent |
| Starters, movers and leavers | PS-4, PS-5 | A leaver's Active Directory account is disabled at once, and the group owners are told of every mover and leaver | EV-AC-01; PA-32 | Not sent; the prompt is not set up |
| Exit interviews, equipment, discipline and job descriptions | PS-4, PS-8, PS-9 | Exit interviews cover confidentiality, equipment is recovered, sanctions are notified, and job descriptions refer to the duties in \<Roles and Responsibilities\> | EV-PS-02 | Not sent |
| The confidentiality agreement | PS-6 | Every person signs it before access | EV-PS-02 | Not sent |
| Contract terms for external people | PS-7 | Contracts require the same personnel security, and notice of movers and leavers within 1 working day | EV-PS-03 | Not sent |

**Today:** no request has been sent, and none of this is evidenced (PA-125).

### 3.11 Role duties in job descriptions

Controls met here: PS-9.

The security and privacy duties of every \<System Name\> role are stated in \<Roles and Responsibilities\>. \<Organisation\>'s job descriptions for those roles refer to them (EV-PS-02).

### 3.12 Policy and procedures

Controls met here: PS-1.

1. **Policy.** \<Policy\> (PS) is a system-level policy. Its purpose and scope are in section PS.1, responsibilities in PS.5, and commitment, coordination and compliance in PS.6. It is shared with everyone who administers \<System Name\> and every line manager of a \<System Name\> user. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (PS) holds seven procedures, PRO-PS-1 to PRO-PS-7. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control, and each review is recorded in the change record.

## Appendix A PS controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 7 says where.

**Table 7: PS controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| PS-3(1), PS-3(2), PS-6(2) Classified Information; Formal Indoctrination; Classified Information Requiring Special Protection | Clearance, briefing and agreements for access to classified information | Not required. \<System Name\> holds no classified information |
| PS-3(3) Information Requiring Special Protective Measures | Extra screening for access to information that needs special protection | Not required. HR documents, which hold special category data, are protected by limiting each project to the people approved for it, not by further screening |
| PS-3(4) Citizenship Requirements | Citizenship checks for defined roles | Not required. The right to work check covers lawful employment in the United Kingdom |
| PS-4(1), PS-6(3) Post-employment Requirements | People are told of, and bound by, duties that continue after they leave | Not required. Done in part: the exit interview covers continuing confidentiality duties. Whether \<Organisation\>'s confidentiality agreement continues after employment is asked with EV-PS-02 |
| PS-4(2) Automated Actions | Automated notice of a leaver, and automated disabling of access | In the High baseline only. Done in design: disabling the Active Directory account ends access to \<System Name\> at once, and \<Organisation\>'s Starters/Leavers system is to prompt the group owners (PA-32) |
| PS-6(1) | Withdrawn by CSS: moved into PS-3 | Not applicable |
