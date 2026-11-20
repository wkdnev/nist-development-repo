# \<System Name\> Identification and Authentication Management

## 1 Purpose

This document shows how people and services are identified and authenticated in \<System Name\>, for each of the 24 Identification and Authentication (IA) controls and enhancements in the CSS Moderate baseline. Section 3 sets out the design: who is identified and how, sign-in through AD FS, the assurance levels, the authenticators, the settings against CSS, sessions, and identity proofing. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define. Appendix B lists the IA controls CSS does not select at Moderate.

The policy is in \<Policy\> (IA), and the steps people follow are in \<Procedures\> (IA). Who may do what once signed in is in \<Access Control Management\>.

An assessor examines the authenticator settings and inventory, the identity proofing records and the trust with the sign-in service; interviews those who issue and reset authenticators; and tests sign-in, including what happens with a wrong password, a replayed token and an idle session (CSS). So for each control section 4 gives:

- **each part of the control**, as CSS letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Design and today.** On 12 November 2026 the system owner stated that every user signs in through \<Organisation\>'s AD FS, with multi-factor authentication, and that \<System Name\> holds no accounts or passwords of its own (D-AC-23). The Design column is written on that basis. The Today column is what was found in the build labelled v1.0, tested between 6 and 9 November 2026. That build signed in with its own passwords, so its results describe that build and not this design, and the tests are to be repeated with AD FS (PA-95).

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |
| Not applicable | The control does not apply, by a recorded tailoring decision |

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.7 (Table 16). This section gives only the overall position.

No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

Two gaps matter most. Nothing yet shows sign-in through AD FS working, with its second factor (PA-95, rated High as a proposal). And the signing key and database password are in settings files in the source repositories (PA-19, rated High). Most of what remains is \<Organisation\>'s to evidence: of the 18 controls that apply, 15 are provided wholly or partly by its Active Directory, AD FS, network and HR.

## 3 The design

### 3.1 Principles

1. **Unique.** Each person has one named identifier, which is never reused.
2. **Proven.** A person's identity is established before they have an account.
3. **Strong.** Every sign-in needs more than a password.
4. **Protected.** Authenticators are never stored or sent in the clear, and secrets are kept out of the source repositories.
5. **Current.** Authenticators change whenever they may be compromised.
6. **One place to sign in.** \<System Name\> holds no accounts and no passwords. \<Organisation\>'s AD FS authenticates every user.

These carry out the principles and rules of \<Policy\>, sections IA.3 and IA.4.

### 3.2 Who and what is identified

**Table 2: Identifiers**

| Who or what | Identifier | Issued by | Authenticated by | Reused |
| --- | --- | --- | --- | --- |
| Every user, whatever their role | Their Active Directory account name. It shows whether they are staff or a contractor | \<Organisation\>, after HR's pre-employment checks | AD FS: password and second factor | Never |
| The API, to the database | One database service account, which is not a superuser | Database administrator | Its password, held in the protected store | Not applicable |
| Each application, on the application server | Its own Windows service account | \<Organisation\>, in Active Directory | Windows: a group managed service account, whose password no person knows | Not applicable |
| Windows server and database administrators, on the servers | Their own named administrator accounts | \<Organisation\> | \<Organisation\>'s directory and approved route | Never |
| The database server, to the API | Its TLS certificate | \[Issuer to be agreed with \<Organisation\>\] | The API checks the certificate and the server's name in full before it sends the password (PA-18) | Not applicable |
| AD FS, to the applications | Its token-signing certificate | \<Organisation\> | Each application checks every token against it | Not applicable |
| Users' devices | The managed device, to the network | \<Organisation\> | Its network access control | Not applicable |

There are no shared, guest, anonymous or local accounts, and nobody outside \<Organisation\>'s staff and contractors may use \<System Name\> (\<Access Control Management\>, section 3.2).

### 3.3 Sign-in through AD FS

![Figure 1: How a person signs in](figures/iam-figure-1.png)

**Figure 1: How a person signs in**

**Table 3: Steps of a sign-in**

| Step | What happens | Who does it |
| --- | --- | --- |
| 1 | The person opens \<System Name\>. Having no session, they are sent to AD FS | \<System Name\> |
| 2 | The person gives their password and their second factor. \<System Name\> never sees either | AD FS |
| 3 | AD FS issues a signed token that names the person and lists their AD groups | AD FS |
| 4 | \<System Name\> checks the token: that AD FS signed it, that it was issued for \<System Name\>, that it is within its short life, and that it has not been used before | \<System Name\> |
| 5 | \<System Name\> opens a session for that person, with the roles and project access their groups give, and records the sign-in | \<System Name\> |
| 6 | The session ends after 30 minutes idle, after 8 hours, at sign-out, or when a global administrator ends it. The person then signs in again | \<System Name\> |

**Table 4: The trust between AD FS and \<System Name\>**

| Setting | Design | Today |
| --- | --- | --- |
| Protocol | \[federation protocol to be confirmed with \<Organisation\>\] | Not built |
| Who \<System Name\> trusts | \<Organisation\>'s AD FS only, by its token-signing certificate | Not built |
| What a token must show | Signed by AD FS; issued for \<System Name\>; within its life; not used before | Not built |
| Token life | Short: \[minutes to be agreed with \<Organisation\>\] | Not built |
| What the token carries | The person's account name and their AD groups, and nothing more than \<System Name\> needs | Not built |
| Certificate renewal | \<System Name\> picks up AD FS's new certificate when \<Organisation\> renews it | Not built |
| Federation assurance level | Level 2 of CSS. The system owner set this as the target on 16 November 2026 (D-IA-12): a signed token that only \<System Name\> can use. It is to be agreed with \<Organisation\> | Not agreed (PA-117) |
| If AD FS is unavailable | Nobody can sign in. There is no local sign-in to fall back on | By design (\<Contingency Planning Management\>, section 3.3.3) |

The steps and the trust are the design, from the system owner's statement of how \<System Name\> works (D-AC-23, D-IA-12). The settings shown as placeholders are asked of \<Organisation\> with EV-IA-04, and are filled in when it answers (PA-117). None of it has been tested or evidenced (PA-95).

### 3.4 Assurance levels

This follows CSS, section 3, and the federal acceptance statement template. It was proposed by the system owner on 9 November 2026 and accepted by the authorising official the same day, as confirmed by the system owner (D-IA-08). The statement was revised on 12 November 2026 for sign-in through AD FS (D-AC-23), and the revision awaits the authorising official.

Identity assurance is how sure we are that a person is who they claim. Authenticator assurance is how sure we are that the person signing in holds the account. Federation assurance applies when another system, here AD FS, vouches for the person.

**Table 5: Assurance levels by user group**

| User group | Harm if impersonated | Identity assurance | Authenticator assurance: target | Authenticator assurance: today | Federation | Until the target is met |
| --- | --- | --- | --- | --- | --- | --- |
| Global administrators | High: every document, account and setting | \<Organisation\>'s pre-employment checks, with the request confirmed by the system owner (PRO-IA-1) | AAL2: multi-factor sign-in through AD FS | Multi-factor through AD FS, as the system owner states (D-AC-23); not yet evidenced | AD FS, at federation assurance level 2 (D-IA-12), to be agreed with \<Organisation\> | No production documents held (D-GEN-13); 8-hour sessions; all actions audited |
| Project access approvers and editors | Moderate: one project's documents | As above, confirmed by the project access approver | AAL2: multi-factor sign-in through AD FS | Multi-factor through AD FS, as the system owner states (D-AC-23); not yet evidenced | AD FS, at federation assurance level 2 (D-IA-12), to be agreed with \<Organisation\> | No production documents held (D-GEN-13); 8-hour sessions; all actions audited |
| Readers and auditors | Moderate: reading one project's documents, or the audit trail | As above | AAL2: multi-factor sign-in through AD FS | Multi-factor through AD FS, as the system owner states (D-AC-23); not yet evidenced | AD FS, at federation assurance level 2 (D-IA-12), to be agreed with \<Organisation\> | No production documents held (D-GEN-13); 8-hour sessions; all actions audited |
| Services (API to PostgreSQL) | High: the whole database | Not applicable | A secret held outside source code, changed every 12 months (section 3.5) | Secret in settings files (PA-19) | Not applicable | Database reachable only from the host (B07, C09) |

**Reasoning:** \<System Name\> will hold HR and finance documents rated Moderate, so a failed sign-in check could expose personal data. CSS points to authenticator assurance level 2 for that harm, which needs two factors and replay resistance. Identity proofing is done once, by \<Organisation\>'s HR, and is not repeated by \<System Name\>. Federation is used: AD FS proves who the person is and vouches for them to \<System Name\> (D-AC-23).

### 3.5 Authenticators

**Table 6: Authenticator inventory**

| Authenticator | Used by | Held or stored | Changed | If lost or exposed | Today |
| --- | --- | --- | --- | --- | --- |
| Active Directory password | Every user | Active Directory; the person. \<System Name\> never sees it | Under \<Organisation\>'s corporate standard, and on suspected compromise (PRO-IA-3) | \<Organisation\>'s service desk resets it; a global administrator ends the \<System Name\> sessions | \<Organisation\>'s standard is to be supplied |
| Temporary password | Not used by \<System Name\> | Not applicable | Not applicable | Not applicable | The tested build used them (A01) |
| Second factor | Every user | Held by the person; registered with \<Organisation\> for AD FS | On loss or replacement (PRO-IA-6) | \<Organisation\>'s service desk resets it after checking who the person is | Provided by AD FS, as the system owner states (D-AC-23); not yet evidenced |
| Session token | UI application, Admin application and API callers | Issued by \<System Name\> after AD FS has signed the user in, and tied to a session row | Under 8 hours; ends on sign-out or administrator action | Administrator ends the session | Replays from another client (PA-46) |
| Token signing key | API | \[Secret store to be chosen\]; protected copy at the second site (\<Contingency Planning Management\>, section 3.8) | Every 12 months, and when an administrator leaves (PRO-IA-4) | Change it; every session ends | In settings files (PA-19) |
| Database account password | API only: one service account, which is not a superuser and cannot change the schema (D-AC-18) | \[Secret store to be chosen\]; protected copy at the second site (\<Contingency Planning Management\>, section 3.8) | Every 12 months, and when an administrator leaves (PRO-IA-4) | Change it in PostgreSQL and API | In settings files, and the account is a superuser in the tested build (PA-19, PA-10) |
| Windows service accounts | UI application, Admin application and API, one each | Group managed service accounts in Active Directory. Windows sets and changes the password, and no person knows it (D-AC-19) | By Windows, automatically | \<Organisation\> resets the account | Not built. \<Organisation\>'s agreement to group managed service accounts is to be confirmed |
| First administrator account | Not used | Not applicable: \<System Name\> holds no accounts (D-AC-23) | Not applicable | Not applicable | The tested build had one (D-AC-13) |
| AD FS token-signing certificate | UI application, Admin application, API, to check each sign-in token | Published by \<Organisation\>'s AD FS; \<System Name\> holds only the public part | When \<Organisation\> renews it | \<Organisation\> replaces it, and \<System Name\> picks up the new one | To be set up and evidenced |
| ASP.NET Data Protection keys | UI application, Admin application, API | A volume on each application | Rolled by the framework | Users sign in again; no data is lost | As designed |
| VM administrator accounts | Windows server and database administrators | \<Organisation\>'s directory | \[\<Organisation\>'s rule\] | \<Organisation\>'s process | Not assessable (EV-IA-01) |
| PostgreSQL superuser | Database administrator | \[To be set on the database VM\] | Every 12 months, and when an administrator leaves | Change it | Not assessable |
| TLS certificates | UI application, Admin application, API | \[Issuer and store to be agreed with \<Organisation\>\] | Before expiry | Revoke and reissue | Not in use (PA-18) |

Only the API connects to PostgreSQL, with one service account that is not a superuser (D-AC-18). The system owner and security officer review the inventory every 12 months (PRO-IA-7).

### 3.6 Settings against CSS

\<System Name\> sets no password rule of its own. \<Organisation\>'s corporate standard applies, and is to be compared with CSS and NCSC password guidance when \<Organisation\> supplies it (EV-IA-04).

**Table 7: Authentication settings at authenticator assurance level 2**

| Requirement | CSS | \<System Name\> | Evidence | State |
| --- | --- | --- | --- | --- |
| Password length, password only | At least 15 characters | \<Organisation\>'s corporate standard, to be supplied | None yet | To be compared when supplied |
| Password length, with multi-factor | At least 8 characters | \<Organisation\>'s corporate standard, to be supplied | None yet | To be compared when supplied |
| Longest password allowed | At least 64 should be allowed | \<Organisation\>'s corporate standard | None yet | To be compared when supplied |
| Spaces and all characters | Should be allowed | \<Organisation\>'s corporate standard | None yet | To be compared when supplied |
| Composition rules | Must not be imposed | \<Organisation\>'s corporate standard | None yet | To be compared when supplied |
| Scheduled changes | Must not be required | \<Organisation\>'s corporate standard | None yet | To be compared when supplied |
| Blocklist | Must be checked | \<Organisation\>'s corporate standard | None yet | To be compared when supplied |
| Storage | Salted, with a costly function | Active Directory. \<System Name\> stores no passwords | None yet | Provided by \<Organisation\>; to be evidenced |
| Rate limiting | At most 100 failures | Lockout by AD FS and Active Directory, under the corporate standard (P-AC-14) | None yet | To be compared when supplied |
| Inactivity timeout | No more than 1 hour | 30 minutes | T44 | Met, stricter |
| Overall session limit | No more than 24 hours | 8 hours | I08, I11, T45 | Met, stricter |
| Second factor | Required | Provided by AD FS (D-AC-23) | None yet | To be evidenced by \<Organisation\> |
| Replay resistance | Required | To be assessed with AD FS sign-in and TLS | A13, A14 | Gap in the tested build (PA-46, PA-18) |
| Sessions end on password change | Expected | Not applicable: \<System Name\> holds no passwords. A global administrator ends sessions on notice (PRO-IA-3) | T38 | Met by other means |
| Feedback | No hint whether the user exists | Given by AD FS, not \<System Name\> | None yet | To be evidenced by \<Organisation\> |

### 3.7 Sessions and signing in again

1. A session ends after 30 minutes without activity, and after 8 hours whatever the activity.
2. The page locks after 25 minutes, 5 minutes before the session ends (\<Access Control Management\>, section 3.7).
3. A change to a person's AD groups takes effect at their next sign-in.
4. A global administrator can end any person's sessions at once. This is the first step when a password or second factor may be compromised, when someone leaves, and when a role is removed (PRO-IA-3).
5. Each session is tied to the person AD FS authenticated, and every audit record names them.

### 3.8 Identity proofing

\<Organisation\>'s HR proves who each person is, once, in its pre-employment checks, before the person has an Active Directory account. As stated by \<Organisation\>, that is photo identification and a right-to-work check for staff, and the same through the agency for contractors, with a notice of proofing sent to the person. \<System Name\> does not repeat it. Before adding anyone to a group, the group's owner confirms the request came from that person and their line manager (PRO-IA-1).

### 3.9 What \<Organisation\> provides

**Table 8: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | As stated by \<Organisation\> | Evidence asked |
| --- | --- | --- | --- | --- |
| AD FS and its multi-factor authentication | IA-2, IA-2(1), IA-2(2), IA-2(8), IA-6 | Every user is authenticated with two factors; the token is signed and carries the person's groups; the sign-in page hides what is typed | Stated by the system owner (D-AC-23); not yet by \<Organisation\> | EV-IA-04 |
| Active Directory accounts and passwords | IA-4, IA-4(4), IA-5, IA-5(1) | One named account for each person, never reused, showing staff or contractor; passwords under the corporate standard | Not yet asked | EV-IA-04, EV-AC-01 |
| Device identification | IA-3 | Only managed devices join the network | Network access control with device certificates, and disk encryption on managed devices | EV-IA-01 |
| Identity proofing | IA-12, IA-12(2), IA-12(3), IA-12(5) | Each person's identity is checked before they have an account | Photo ID and right-to-work checks for staff, and the same through the agency for contractors | EV-IA-02 |
| Cryptographic modules on the servers | IA-7 | The modules meet the applicable standards | Standard Windows modules, not in CSS-approved cryptographic mode | EV-IA-03 |

**Today:** no request has been sent, and none of this is evidenced.

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open. Six controls are not applicable, and each says why.

### 4.1 IA-1 Policy and Procedures

**Table 9: IA-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | An identification and authentication policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (IA): a system-level policy, shared with everyone who uses or administers \<System Name\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-IA-09) and legally reviewed on 9 November 2026. The rules rewritten for AD FS on 12 November 2026 await the Head of Cyber. Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (IA): eight procedures, PRO-IA-1 to PRO-IA-8. Shared with the same people | Approved by the system owner (D-IA-10), and rewritten for AD FS on 12 November 2026. Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 9 and 12 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 10: IA-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy (\<Policy\>, section IA.4); all eight procedures (\<Procedures\> (IA)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals of version \<ver\> exist |
| Status | Partially implemented |
| Risk decision | NC-IA-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the rules rewritten for AD FS |

### 4.2 IA-2 Identification and Authentication (Organizational Users)

**Table 11: IA-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Identify and authenticate each organisational user uniquely, and tie that identity to the processes acting for them | Every person signs in through \<Organisation\>'s AD FS with their own Active Directory account (section 3.3). \<System Name\> holds no accounts or passwords. It accepts a sign-in only on a token AD FS has signed, takes the person's name and groups from it, and ties every request and every audit record to that person through the session. Shared accounts are prohibited | Stated by the system owner (D-AC-23). Not yet tested or evidenced (PA-95). The tested build identified each user uniquely with its own accounts (A09, A10) |

**Table 12: IA-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers |
| Enforced by | AD FS, which authenticates; \<System Name\>'s check of the token, and its session |
| Rules and procedures | Policy rules R1, R2 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | Checks A09 and A10 on the v1.0 build, 6 November 2026: both passed. These checks ran on a build that used its own passwords, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | The trust settings between AD FS and \<System Name\>; a sign-in shown end to end; audit records naming the person. None exist yet for AD FS |
| Status | Partially implemented |
| Risk decision | NC-IA-02, rated Low: obtain evidence |
| Open items | PA-95: test sign-in through AD FS. PA-117: agree the federation settings with \<Organisation\> |

### 4.3 IA-2(1) Multi-factor Authentication to Privileged Accounts

**Table 13: IA-2(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use multi-factor authentication for access to privileged accounts | AD FS requires a second factor from every user, so every privileged user has one. The application roles are AD groups, and nobody reaches an administration page without signing in through AD FS. The named Windows server and database administrators reach the servers only through \<Organisation\>'s managed route, which also requires a second factor (\<Maintenance Management\>, section 3.4) | Stated by the system owner (D-AC-23); not yet tested or evidenced (PA-95). The tested build had password-only sign-in, which the authorising official accepted to 6 May 2027 with no production documents held (NC-IA-03). The route to the servers is not evidenced (EV-MA-02) |

**Table 14: IA-2(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | \<Organisation\>, developers |
| Enforced by | AD FS's authentication policy for \<System Name\> |
| Rules and procedures | Policy rule R6 (\<Policy\>, section IA.4); PRO-IA-6 (\<Procedures\> (IA)) |
| Tests | Checks A11 and A12 on the v1.0 build showed no second factor. These checks ran on a build that used its own passwords, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | AD FS's policy for \<System Name\>, showing the factors required (EV-IA-04); a sign-in shown with the second factor |
| Status | Not implemented |
| Risk decision | NC-IA-03, rated High: accepted to 6 May 2027 |
| Open items | PA-95. PA-23 is closed once PA-95 shows it working |

### 4.4 IA-2(2) Multi-factor Authentication to Non-privileged Accounts

**Table 15: IA-2(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use multi-factor authentication for access to non-privileged accounts | The same AD FS policy applies to every user | As IA-2(1). The acceptance for ordinary users is NC-IA-04, to 6 May 2027 |

**Table 16: IA-2(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | \<Organisation\>, developers |
| Enforced by | AD FS's authentication policy for \<System Name\> |
| Rules and procedures | Policy rule R6 (\<Policy\>, section IA.4); PRO-IA-6 (\<Procedures\> (IA)) |
| Tests | As IA-2(1) |
| Records an assessor will ask for | As IA-2(1) |
| Status | Not implemented |
| Risk decision | NC-IA-04, rated Medium: accepted to 6 May 2027 |
| Open items | PA-95 |

### 4.5 IA-2(8) Access to Accounts, Replay Resistant

**Table 17: IA-2(8) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use replay-resistant authentication for defined accounts | For privileged and non-privileged accounts alike. Sign-in tokens from AD FS are signed, short-lived, issued for \<System Name\> only and used once. Everything travels over TLS. \<System Name\>'s own session token is tied to one session and ends with it | Not met in the tested build: a session token still worked from another client (A13), and traffic was plain HTTP (A14). To be assessed again with AD FS and TLS (PA-18, PA-46, PA-95) |

**Table 18: IA-2(8) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers, Windows server administrator |
| Enforced by | TLS; AD FS's token settings; \<System Name\>'s session |
| Rules and procedures | Policy rule R10 (\<Policy\>, section IA.4); no procedure of its own (\<Procedures\> (IA)) |
| Tests | Checks A13 and A14 on the v1.0 build showed the gap |
| Records an assessor will ask for | The token lifetime and audience settings; a replay test; the TLS settings |
| Status | Not implemented |
| Risk decision | NC-IA-05, rated Medium: remediate |
| Open items | PA-18: TLS on every route. PA-46: stop a session token working from another client. PA-117: agree the token settings |

### 4.6 IA-2(12) Acceptance of PIV Credentials

**Table 19: IA-2(12) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Accept and check Personal Identity Verification credentials | Not applicable: PIV is a United States federal credential, and no \<System Name\> user holds one (TR-IA-01 in \<Tailoring Register\>) | Not applicable. The independent assessor may test the tailoring decision |

**Table 20: IA-2(12) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Tailoring decision | TR-IA-01, agreed by the system owner (D-IA-05) |

### 4.7 IA-3 Device Identification and Authentication

**Table 21: IA-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Identify and authenticate defined devices before they connect | \<Organisation\>'s network access control identifies each managed device before it joins the network, and unmanaged devices are kept off it. \<System Name\> does not identify devices itself: it is reached only from that network or the VPN | Not evidenced (EV-IA-01, PA-116) |

**Table 22: IA-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s network access control |
| Rules and procedures | No policy rule of its own (\<Policy\>, section IA.4); no procedure of its own (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of its network access control (EV-IA-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-IA-06, rated Low: obtain evidence |
| Open items | PA-116: obtain \<Organisation\>'s evidence |

### 4.8 IA-4 Identifier Management

**Table 23: IA-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Get authorisation from defined people before an identifier is assigned | \<Organisation\> authorises each Active Directory account through its starters process. \<System Name\>'s part is membership of its groups, authorised by the group's owner through the ServiceNow workflow (\<Access Control Management\>, section 3.13) | The ServiceNow workflow is not set up (PA-20). \<Organisation\>'s process is not evidenced (EV-AC-01) |
| b | Choose an identifier that identifies one person, group, role, service or device | The person's Active Directory account name. Service accounts are named for the application they run | Not evidenced |
| c | Assign the identifier to the intended person or thing | By \<Organisation\>, to the person its HR has checked | Not evidenced |
| d | Prevent reuse of an identifier for a defined time | Never reused: \<Organisation\>'s rule for Active Directory accounts. \<System Name\> issues no identifiers, so it has none to reuse | To be evidenced by \<Organisation\>. The tested build freed a username when an account was deleted (PA-47, overtaken) |

**Table 24: IA-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | System owner, global administrator |
| Enforced by | Active Directory; the access request workflow |
| Rules and procedures | Policy rule R2 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | Check A09 on the v1.0 build: usernames were unique. These checks ran on a build that used its own passwords, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | \<Organisation\>'s account naming and reuse rule (EV-AC-01); the ServiceNow requests |
| Status | Partially implemented |
| Risk decision | NC-IA-07, rated Low: remediate |
| Open items | PA-20: the ServiceNow workflow. PA-47 is closed once PA-95 shows AD FS working |

### 4.9 IA-4(4) Identify User Status

**Table 25: IA-4(4) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Show each person's status in their identifier, as defined | Active Directory shows whether a person is staff or a contractor. The group's owner sees it when authorising a request | To be evidenced by \<Organisation\>. The tested build had no such field (PA-47, overtaken) |

**Table 26: IA-4(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers, global administrator |
| Enforced by | Active Directory |
| Rules and procedures | Policy rule R2 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | A directory entry showing the status (EV-AC-01) |
| Status | Not implemented |
| Risk decision | NC-IA-08, rated Low: remediate |
| Open items | PA-95; evidence from \<Organisation\> |

### 4.10 IA-5 Authenticator Management

**Table 27: IA-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Check who a person or thing is before first giving it an authenticator | People: \<Organisation\>'s service desk, after HR's pre-employment checks (PRO-IA-2). Service secrets: set by the named administrators | Not evidenced for people |
| b | Set the first content of each authenticator | People: under \<Organisation\>'s corporate standard. Service secrets and the signing key: generated randomly by the administrator. Service accounts: set by Windows | Secrets in the tested build were typed into settings files (PA-19) |
| c | Make sure authenticators are strong enough for their use | Section 3.6 compares each setting with CSS at authenticator assurance level 2 | \<Organisation\>'s standard is to be supplied and compared |
| d | Have procedures for first issue, for lost, compromised or damaged authenticators, and for revoking them | PRO-IA-2, PRO-IA-3 and PRO-IA-6: \<Organisation\>'s service desk issues, resets and revokes; a global administrator ends the person's \<System Name\> sessions at once | Written. Not yet used |
| e | Change default authenticators before first use | \<System Name\> ships with no default account or password. The PostgreSQL superuser's password is set when the database server is built, and no vendor default is left on either server | The tested build seeded a sample administrator account, in the test environment only (D-AC-13) |
| f | Change or refresh authenticators on a schedule by type, and when defined events occur | User passwords: \<Organisation\>'s corporate standard, and on suspected compromise. Service secrets and the signing key: every 12 months, and when an administrator leaves (PRO-IA-4) | Secrets have never been changed (PA-19) |
| g | Protect authenticator content from disclosure and change | User passwords stay in Active Directory and never reach \<System Name\>. Service secrets and the signing key are held in a protected store, outside the source repositories and settings files. Everything travels over TLS | Secrets are in settings files in the source repositories (PA-19). Plain HTTP in the test environment (PA-18) |
| h | Require people, and have devices apply, defined controls to protect authenticators | The rules of behaviour: never share a password or second factor, and report a loss at once (\<Security Operating Procedures\>, Part A). Managed devices encrypt their disks | Rules written; not yet signed. Devices not evidenced (EV-IA-01) |
| i | Change the authenticators of group or role accounts when their membership changes | Not applicable: there are no shared, group or role accounts (TR-AC-02 in \<Tailoring Register\>). Service secrets are changed when an administrator who knew them leaves | Not yet used |

**Table 28: IA-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Global administrator, developers |
| Enforced by | Active Directory and AD FS for people; the secret store and procedure PRO-IA-4 for services |
| Rules and procedures | Policy rules R4, R5, R9 (\<Policy\>, section IA.4); PRO-IA-2 to PRO-IA-4, PRO-IA-7 (\<Procedures\> (IA)) |
| Tests | Checks A01, A34 and I07 on the v1.0 build. These checks ran on a build that used its own passwords, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | \<Organisation\>'s password standard; the authenticator inventory and its yearly review; records of each change of a service secret (TPL-6). The inventory exists |
| Status | Partially implemented |
| Risk decision | NC-IA-09, rated High: remediate |
| Open items | PA-19: move the secrets out of source and change them. PA-44 is closed once PA-95 shows AD FS working |

### 4.11 IA-5(1) Password-based Authentication

**Table 29: IA-5(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Keep a list of common, expected and compromised passwords, and update it on a schedule and after a compromise | \<Organisation\>'s corporate standard for Active Directory, which \<System Name\> accepts (D-AC-23) | To be supplied by \<Organisation\> and compared with CSS (EV-IA-04) |
| b | Check new and changed passwords against the list | The same | To be supplied |
| c | Send passwords only over encrypted channels | Passwords are typed into AD FS over TLS, and never into \<System Name\> | To be evidenced |
| d | Store passwords with an approved salted key derivation function | Active Directory stores them. \<System Name\> stores none | To be evidenced |
| e | Require a new password at once after account recovery | \<Organisation\>'s service desk process | To be supplied |
| f | Allow long passwords and passphrases, with spaces and all printable characters | \<Organisation\>'s corporate standard | To be supplied |
| g | Give users automated help to choose a strong password | \<Organisation\>'s corporate standard | To be supplied |
| h | Enforce defined composition and complexity rules | \<Organisation\>'s corporate standard. \<System Name\> sets none of its own | To be supplied |

**Table 30: IA-5(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | Active Directory and AD FS |
| Rules and procedures | Policy rule R3 (\<Policy\>, section IA.4); PRO-IA-5 (\<Procedures\> (IA)) |
| Tests | Checks A02, A05, A06, A33 and I01 to I06 on the v1.0 build tested its own passwords, which the design no longer uses |
| Records an assessor will ask for | \<Organisation\>'s password standard and settings (EV-IA-04) |
| Status | Partially implemented |
| Risk decision | NC-IA-10, rated Medium: remediate |
| Open items | PA-95: obtain \<Organisation\>'s standard and compare it. PA-45, PA-49 and PA-82 are closed once PA-95 shows AD FS working |

### 4.12 IA-5(2) Public Key-based Authentication

**Table 31: IA-5(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Check certificates and map them to accounts, where public key authentication is used | Not applicable: no person or service signs in to \<System Name\> with a certificate (TR-IA-02 in \<Tailoring Register\>). If \<Organisation\>'s AD FS uses a public key second factor, such as a security key, the control applies again, and falls to \<Organisation\> | Not applicable. The independent assessor may test the tailoring decision |

**Table 32: IA-5(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Tailoring decision | TR-IA-02, agreed by the system owner (D-IA-05) |

### 4.13 IA-5(6) Protection of Authenticators

**Table 33: IA-5(6) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Protect authenticators to the level of the information they give access to | The information is rated Moderate. User passwords are protected by Active Directory. The database password and the signing key, which open the whole database, are held in a protected store that only the named administrators and the API's service account can read, with a protected copy at the second site | Not met: the signing key and database password are in settings files in the source repositories (C07; PA-19) |

**Table 34: IA-5(6) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers, administrators |
| Enforced by | The secret store; Windows permissions on each application's settings (\<Access Control Management\>, section 3.6.3) |
| Rules and procedures | Policy rule R5 (\<Policy\>, section IA.4); PRO-IA-4 (\<Procedures\> (IA)) |
| Tests | Check C07 on the v1.0 build showed the gap |
| Records an assessor will ask for | Where each secret is held and who can read it |
| Status | Partially implemented |
| Risk decision | NC-IA-11, rated High: remediate |
| Open items | PA-19 |

### 4.14 IA-6 Authentication Feedback

**Table 35: IA-6 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Hide authentication information as it is entered, so that it cannot be seen or used by others | Passwords and second factors are entered on AD FS's page, which masks them and does not say whether an account exists. \<System Name\> shows no sign-in form | To be evidenced by \<Organisation\>. The tested build's own page masked the password and gave the same answer for a wrong password and an unknown user (A07, A08) |

**Table 36: IA-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | AD FS's sign-in page |
| Rules and procedures | Policy rule R10 (\<Policy\>, section IA.4); no procedure of its own (\<Procedures\> (IA)) |
| Tests | Checks A07 and A08 on the v1.0 build: both passed. These checks ran on a build that used its own passwords, and are to be repeated on the AD FS build (PA-95) |
| Records an assessor will ask for | A sign-in shown on AD FS's page |
| Status | Partially implemented |
| Risk decision | NC-IA-12, rated Low: obtain evidence |
| Open items | PA-95 |

### 4.15 IA-7 Cryptographic Module Authentication

**Table 37: IA-7 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Authenticate to a cryptographic module in a way that meets the applicable laws and standards | \<System Name\> uses the cryptographic modules of Windows Server 2025 and .NET. No person signs in to a module directly: the applications reach them through their service accounts. \<Organisation\> is asked which modules and mode the servers use | Not confirmed. As stated by \<Organisation\>: standard Windows modules, not in CSS-approved cryptographic mode (EV-IA-03, PA-48) |

**Table 38: IA-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | Windows server administrator, \<Organisation\> |
| Enforced by | Windows Server |
| Rules and procedures | Policy rule R10 (\<Policy\>, section IA.4); no procedure of its own (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | The servers' cryptographic settings (EV-IA-03) |
| Status | Not implemented |
| Risk decision | NC-IA-13, rated Low: obtain evidence |
| Open items | PA-48: confirm the modules and mode on the servers |

### 4.16 IA-8 Identification and Authentication (Non-organizational Users)

**Table 39: IA-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Identify and authenticate non-organisational users | Not applicable: only \<Organisation\>'s staff and contractors, with an Active Directory account, may use \<System Name\> (TR-IA-03 in \<Tailoring Register\>) | Not applicable. The independent assessor may test the tailoring decision |

**Table 40: IA-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Tailoring decision | TR-IA-03, agreed by the system owner (D-IA-05) |

### 4.17 IA-8(1) Acceptance of PIV Credentials from Other Agencies

**Table 41: IA-8(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Accept PIV credentials from other federal agencies | Not applicable: there are no non-organisational users (TR-IA-04 in \<Tailoring Register\>) | Not applicable. The independent assessor may test the tailoring decision |

**Table 42: IA-8(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Tailoring decision | TR-IA-04, agreed by the system owner (D-IA-05) |

### 4.18 IA-8(2) Acceptance of External Authenticators

**Table 43: IA-8(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Accept only external authenticators that meet the CSS guidance | Not applicable: there are no non-organisational users (TR-IA-05 in \<Tailoring Register\>) | Not applicable. The independent assessor may test the tailoring decision |

**Table 44: IA-8(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Tailoring decision | TR-IA-05, agreed by the system owner (D-IA-05) |

### 4.19 IA-8(4) Use of Defined Profiles

**Table 45: IA-8(4) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Conform to defined identity management profiles | Not applicable: there are no non-organisational users (TR-IA-06 in \<Tailoring Register\>) | Not applicable. The independent assessor may test the tailoring decision |

**Table 46: IA-8(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Tailoring decision | TR-IA-06, agreed by the system owner (D-IA-05) |

### 4.20 IA-11 Re-authentication

**Table 47: IA-11 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Require users to sign in again in defined circumstances | After 30 minutes idle, and after 8 hours whatever the activity. A change to a person's groups takes effect at their next sign-in, and a global administrator can end a person's sessions at once, which forces one (section 3.7) | Met in the tested build: idle sessions ended at 30 minutes (T44) and all sessions at 8 hours (I08, I11). The servers are not assessable |

**Table 48: IA-11 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers |
| Enforced by | \<System Name\>'s session limits |
| Rules and procedures | Policy rule R7 (\<Policy\>, section IA.4); no procedure of its own (\<Procedures\> (IA)) |
| Tests | Checks T44, I08 and I11 on the v1.0 build: all passed |
| Records an assessor will ask for | The session settings; the test results |
| Status | Partially implemented |
| Risk decision | NC-IA-14, rated Low: obtain evidence |
| Open items | None for the application. The checks are repeated on the servers (PA-95) |

### 4.21 IA-12 Identity Proofing

**Table 49: IA-12 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Prove the identity of users who need an account, to the assurance level required | \<Organisation\>'s HR proves each person's identity in its pre-employment checks, once, before the Active Directory account exists. \<System Name\> does not repeat it | Not evidenced (EV-IA-02, PA-116) |
| b | Resolve each identity to one person | One Active Directory account for each person | Not evidenced |
| c | Collect, validate and verify identity evidence | As stated by \<Organisation\>: photo identification and right-to-work checks for staff, and the same through the agency for contractors | Not evidenced |

**Table 50: IA-12 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\>, system owner |
| Enforced by | \<Organisation\>'s HR process |
| Rules and procedures | Policy rules R1, R8 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s HR process and a blank record (EV-IA-02). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-IA-15, rated Low: obtain evidence |
| Open items | PA-116: obtain \<Organisation\>'s evidence |

### 4.22 IA-12(2) Identity Evidence

**Table 51: IA-12(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Require identity evidence to be presented to the registration authority | \<Organisation\>'s HR sees the evidence in its pre-employment checks | Not evidenced (EV-IA-02) |

**Table 52: IA-12(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s HR process |
| Rules and procedures | Policy rules R1, R8 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s HR process and a blank record (EV-IA-02). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-IA-16, rated Low: obtain evidence |
| Open items | PA-116 |

### 4.23 IA-12(3) Identity Evidence Validation and Verification

**Table 53: IA-12(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Validate and verify the evidence by defined methods | HR checks the evidence during pre-employment checks | Not evidenced (EV-IA-02) |

**Table 54: IA-12(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s HR process |
| Rules and procedures | Policy rules R1, R8 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s HR process and a blank record (EV-IA-02). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-IA-17, rated Low: obtain evidence |
| Open items | PA-116 |

### 4.24 IA-12(5) Address Confirmation

**Table 55: IA-12(5) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Send a registration code or a notice of proofing by a separate channel, to confirm the address on record | A notice of proofing, sent by \<Organisation\>'s HR | Not evidenced (EV-IA-02) |

**Table 56: IA-12(5) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s HR process |
| Rules and procedures | Policy rules R1, R8 (\<Policy\>, section IA.4); PRO-IA-1 (\<Procedures\> (IA)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s HR process and a blank record (EV-IA-02). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-IA-18, rated Low: obtain evidence |
| Open items | PA-116 |

## Appendix A Parameter register

These are the CSS organisation-defined values for the 24 IA entries: 22 in total. They were agreed on 5 and 6 November 2026 (D-IA-P01), and revised on 12 November 2026 for sign-in through AD FS (D-AC-23).

**Table 57: IA parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| IA-01\_ODP\[01\] | Who receives the policy | Everyone who uses or administers \<System Name\> | Not yet shared |
| IA-01\_ODP\[02\] | Who receives the procedures | Everyone who uses or administers \<System Name\> | Not yet shared |
| IA-01\_ODP\[03\] | Level of the policy | System level | Met |
| IA-01\_ODP\[04\] | Official who manages them | System owner | Met |
| IA-01\_ODP\[05\] | Policy review frequency | Every 12 months | Met: reviewed 9 November 2026 |
| IA-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: reviewed after the IA pack review |
| IA-01\_ODP\[07\] | Procedures review frequency | Every 12 months | Met: reviewed 9 November 2026 |
| IA-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: reviewed after the IA pack review |
| IA-02(08)\_ODP | Accounts needing replay resistance | Privileged and non-privileged accounts | To be assessed with AD FS sign-in. In the tested build tokens replayed from another client, and traffic was plain HTTP (PA-46, PA-18) |
| IA-03\_ODP\[01\] | Devices identified | \<Organisation\>'s managed devices | Inherited, unconfirmed (EV-IA-01) |
| IA-03\_ODP\[02\] | Type of connection | Network | Inherited, unconfirmed (EV-IA-01) |
| IA-04\_ODP\[01\] | Who authorises identifiers | \<Organisation\>, for the Active Directory account. Membership of a \<System Name\> group: the system owner, or the project access approver for project access, through the ServiceNow workflow | ServiceNow not set up (PA-20) |
| IA-04\_ODP\[02\] | Time before reuse | Never reused: \<Organisation\>'s rule for Active Directory accounts | To be evidenced by \<Organisation\> |
| IA-04(04)\_ODP | Status shown | Staff or contractor | Shown by \<Organisation\>'s directory; to be evidenced |
| IA-05\_ODP\[01\] | Change period by type | User passwords: \<Organisation\>'s corporate standard for Active Directory and AD FS, which \<System Name\> accepts (D-AC-23). Service account secrets and signing key: every 12 months | Secrets never changed; in settings files (PA-19) |
| IA-05\_ODP\[02\] | Events requiring change | User passwords: \<Organisation\>'s corporate standard for Active Directory and AD FS, which \<System Name\> accepts (D-AC-23), and on suspected compromise. Service secrets and signing key: an administrator leaving | \<Organisation\>'s standard is to be supplied |
| IA-05(01)\_ODP\[01\] | Blocked list refresh | \<Organisation\>'s corporate standard for Active Directory and AD FS, which \<System Name\> accepts (D-AC-23) | To be supplied by \<Organisation\> |
| IA-05(01)\_ODP\[02\] | Composition rules | \<Organisation\>'s corporate standard for Active Directory and AD FS, which \<System Name\> accepts (D-AC-23). This replaces the 15 and 12 character rule of D-IA-P02 | To be supplied by \<Organisation\> |
| IA-08(04)\_ODP | Identity profiles | Not applicable (TR-IA-06) | Not applicable |
| IA-11\_ODP | When to sign in again | After 30 minutes idle and after 8 hours. A change to a person's groups takes effect at their next sign-in | Met in the application (T44, I08, I11) |
| IA-12(03)\_ODP | Validation and verification | Evidence checked by \<Organisation\>'s HR during pre-employment checks | Inherited, unconfirmed (EV-IA-02) |
| IA-12(05)\_ODP | Address confirmation | Notice of proofing | Inherited, unconfirmed (EV-IA-02) |

## Appendix B IA controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some bear on the design, and Table 58 says how.

**Table 58: IA controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| IA-2(5) Individual Authentication with Group Authentication | A person signs in as themselves before using a shared account | Not required. There are no shared accounts |
| IA-2(6) Access to Accounts, Separate Device | The second factor is on a device separate from the one signing in | Not required. Decided by \<Organisation\>'s AD FS, and asked with EV-IA-04 |
| IA-5(7) No Embedded Unencrypted Static Authenticators | No passwords or keys left in code, scripts or settings | Not required. It is what PA-19 puts right: the signing key and database password are in settings files today |
| IA-5(13) Expiration of Cached Authenticators | Cached sign-in details expire | Not required. \<System Name\> caches none: a session ends at 8 hours at most |
| IA-9 Service Identification and Authentication | Services prove who they are to each other | In no baseline. Done in design: the API to the database, and the applications' check of AD FS (section 3.2) |
| IA-10 Adaptive Authentication | Extra checks when a sign-in looks unusual | In no baseline. A matter for \<Organisation\>'s AD FS |
| IA-12(4) In-person Validation and Verification | Identity evidence checked in person | Selected only at High. \<Organisation\>'s HR is asked how it checks (EV-IA-02) |
| IA-13 Identity Providers and Authorization Servers | Controls on the service that vouches for users, and on checking its tokens | In no baseline. It bears directly on \<System Name\>, which relies on AD FS. Section 3.3 sets what \<System Name\> checks in a token, and PA-117 tracks agreeing it |
