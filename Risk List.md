# \<System Name\> Risk List

## 1 Purpose and summary

This list is used by every control family, and this version covers the AC, AU, IA, SC, CM, SI, RA, CA, IR, CP, AT, MA, MP, PE, PL, PS, PT, SA and SR families. The top risks are a stolen password, full database control and interception of traffic. The risk of reading another project's documents has been reduced by the AC-3 fixes. The authorising official confirmed the method on 6 November 2026, only the items in section 3 have been accepted, and residual risk assumes the linked POA&M items are done. Four operational risks were added on 12 November 2026 after the whole-set review: incident handling (R-IR-01), training (R-AT-01), stored data and keys (R-SC-01) and the supply chain (R-SR-01). Their ratings are proposed, and await the authorising official (D-RA-10). \<System Name\> is not in production, and the current stack holds only sample data. It will run on two VMs on \<Organisation\>'s network.

## 2 Risk register

**Table 1: Risk register**

| ID | Risk | Cause | Consequence | Likelihood | Impact | Rating | Treatment | Residual | Owner | POA&M | Status | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-AC-01 | A user reads documents outside their projects | Project checks were missing on page, export and report endpoints (fixed 5 November 2026); Folder export can still write anywhere on the server; bulk export leaves unencrypted copies on the server (P02 to P06) | Confidential documents disclosed | Low, until retested on the VMs | High | Medium | Fix | Low | System owner | PA-26 and PA-86 open; PA-01, 04, 05, 09, 27 fixed | Open; treatment in progress | 11 November 2026 |
| R-AC-02 | A user interferes with another user's session or abuses internal functions | Session and notification endpoints not limited to their owner; diagnostic pages exposed, including ones that write audit records and offer database changes | Possible access beyond role, misleading notifications, false audit records | Medium | High | High | Fix | Low | System owner | PA-02, PA-06, PA-07, PA-29 | Open; treatment in progress | 11 November 2026 |
| R-AC-03 | An outsider degrades the service without signing in | Anonymous cache endpoints | Slower service; stale permissions after a cache clear need checking | Medium | Medium | Medium | Fix | Low | System owner | PA-03 | Open; treatment in progress | 11 November 2026 |
| R-AC-04 | Someone gains full database control | Committed secrets, superuser role, database configured on a public address | All documents, accounts and audit records can be read or changed | Medium | High | High | Fix | Low | System owner | PA-10, PA-19 | Open; treatment in progress | 11 November 2026 |
| R-AC-05 | Credentials or documents are intercepted | No TLS in the Docker stack; not yet set up for the VMs | Passwords, tokens and documents exposed on the network | Medium | High | High before production; low while only on localhost | Fix | Low | System owner | PA-18, PA-34 | Open; treatment in progress | 11 November 2026 |
| R-AC-06 | People keep access they no longer need | No access review, inactivity disable or expiry | Former staff or movers retain access | Medium | Medium | Medium | Fix | Low | System owner | PA-13, PA-16, PA-32 | Open; treatment in progress | 11 November 2026 |
| R-AC-07 | Administrator misuse goes unnoticed | One all-powerful role, gaps in audit of privilege changes, no separate everyday account | Unauthorised changes with no reliable record | Low | High | Medium | Fix | Low | System owner | PA-14, PA-15, PA-17, PA-31, PA-130 | Open; treatment in progress | 11 November 2026 |
| R-AC-08 | An unattended session is used by someone else | Lock screen continues without a password | Access under another person's identity | Medium | Medium | Medium | Fix | Low | System owner | PA-12 | Open; treatment in progress | 11 November 2026 |
| R-AC-09 | Monitoring or legal action is challenged | No system use notice | Weaker position in a dispute | Low | Medium | Low | Fix | Low | System owner | PA-11 | Open; treatment in progress | 11 November 2026 |
| R-AC-10 | A stolen password gives full access | Password-only sign-in, including administrators. On 12 November 2026 the system owner stated that sign-in is through AD FS with multi-factor authentication (D-AC-23), which is not yet tested or evidenced (PA-95) | Account takeover, up to global administrator | Medium | High | High | Accepted to 6 May 2027 (D-GEN-13); end state decided by the authorising official: multi-factor for administrators before production documents, and for all users by 6 May 2027 (D-IA-07) | Low once multi-factor sign-in is in place | \[Name\], authorising official | PA-23, PA-83 | Accepted to 6 May 2027; remediation planned | 11 November 2026 |
| R-AC-11 | The system cannot be authorised | Unapproved policy, unappointed roles, no provider evidence | Delay, or an assessor cannot rely on the evidence | High | Medium | Medium | Fix | Low | System owner | PA-20, PA-21, PA-22, PA-24, PA-25, PA-28, PA-30, PA-33, PA-124, PA-127, PA-129 | Open; treatment in progress | 11 November 2026 |
| R-SI-01 | A known flaw or malicious upload compromises the system | Packages with known advisories (7 in API and UI application, 5 of them High, on 11 November 2026, V01); no malware scan of uploads; nothing scans the images or operating system packages (V02) | Code running on the server, or harmful files reaching users | Medium | High | High | Fix | Low | System owner | PA-56, PA-57, PA-58, PA-62 | Open; treatment in progress | 11 November 2026 |
| R-CP-01 | Documents cannot be recovered after a failure | No backups. The restore test on 9 November showed the default backup is unencrypted and transaction logs are not archived (R02, R09). No confirmed second site | Loss of documents and audit records | Medium | Medium | Medium | Fix | Low | System owner | PA-64, PA-66 | Open; treatment in progress | 11 November 2026 |
| R-PE-01 | Someone reaches the VMs or disks physically, or the site fails | Physical, media and maintenance protection are not evidenced; nothing \<System Name\> produces is marked (PA-87) | Disclosure or loss of documents | Low | Medium | Low | Obtain evidence | Low | System owner | PA-67 | Open; treatment in progress | 11 November 2026 |
| R-PS-01 | Someone unsuitable holds access, or keeps it after moving or leaving | Screening is not evidenced, and the leaver and mover route is not built | Misuse or disclosure of documents | Low | Medium | Low | Obtain evidence | Low | System owner | PA-32 | Open; treatment in progress | 11 November 2026 |
| R-PT-01 | Personal data is misused, kept too long, or relied on when wrong | The impact assessment is only a draft (\<Data Protection Impact Assessment\>), the lawful basis is unconfirmed, and there is no retention, disposal or quality check | Harm to individuals, and a breach of UK GDPR | Medium | Medium | Medium | Fix | Low | Legal adviser | PA-70, PA-71, PA-72 | Open; treatment in progress | 11 November 2026 |
| R-SA-01 | A flaw or unapproved change reaches production | No build pipeline, test gate or enforced change control, and no administrator guide | A control stops working unnoticed, or an administrator configures \<System Name\> wrongly | Medium | Medium | Medium | Fix | Low | System owner | PA-53, PA-68, PA-69, PA-128 | Open; treatment in progress | 11 November 2026 |
| R-AU-01 | Audit records are changed or removed without detection | The chain hash has no key, so it can be rewritten; the newest records can be removed without trace; the chain check cannot pass as built and is not run; the application account can change the table; some events are not logged | Misuse or an incident cannot be investigated or proven | Low | High | Medium | Fix (authorising official, D-AU-06) | Low | System owner | PA-36, PA-37, PA-73, PA-74, PA-76 | Open; treatment in progress | 11 November 2026 |
| R-AU-02 | Personal data and live session IDs are exposed through the application log | Every audit event is repeated in the application log, which has no access limit, review or retention period | A breach of UK GDPR; a live session could be taken over | Medium | Medium | Medium | Fix (authorising official, D-AU-06). Until then the application log is treated as audit information (\<Audit and Accountability Management\>) | Low | System owner | PA-75 | Open; treatment in progress | 11 November 2026 |
| R-CM-01 | \<System Name\> runs software or settings that differ from the approved baseline, and nobody notices | Images built from floating tags (V03); no bill of materials; unused components built in; nothing checks for drift between releases | An unapproved or vulnerable component reaches production, and the record no longer matches the system | Medium | Medium | Medium | Fix (authorising official, D-CM-10) | Low | System owner | PA-77 to PA-80, PA-84, PA-85 | Open; treatment in progress | 11 November 2026 |
| R-IR-01 | An incident is not contained or reported in time | Nobody is trained in the incident plan, no exercise has been held, and incidents cannot yet be tracked in ServiceNow; the plan is approved but has only been tried once, in Docker | More documents are disclosed than need be, evidence is lost, or a personal data breach reaches the ICO after the 72-hour limit | Medium | Medium | Medium | Fix: train, exercise and set up tracking before go-live | Low | Security officer | PA-65, PA-81 | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) | 12 November 2026 |
| R-AT-01 | Someone makes a mistake, or is deceived, because they were not trained | No one has been trained; the \<System Name\> briefing and the role modules are outlined but not written; \<Organisation\>'s course has not been seen | Documents sent to the wrong person, credentials given away, or a privileged error | Medium | Medium | Medium | Fix: no access without the briefing, and no privileged role without its modules (\<Awareness and Training Management\>) | Low | Security officer | PA-96 to PA-100 for the briefing, the modules, the records and the evidence; PA-81 for incident and contingency training | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) | 12 November 2026 |
| R-SC-01 | Stored documents or keys are read from a disk, backup or export copy | In Docker, the database, backups, export copies and the data protection key rings are not encrypted at rest; BitLocker and encrypted backups are planned for the VMs but not built; checksums use MD5 | Documents disclosed without signing in; sessions forged from a copied key ring | Low | High | Medium | Fix | Low | System owner | PA-52, PA-61, PA-86, PA-93 | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) | 12 November 2026 |
| R-SR-01 | A compromised or counterfeit component reaches the build | Most packages are restored straight from nuget.org, with no lock files, trust policy or audit; images are pulled by floating tag; there is no bill of materials; browser files from the CDN have no integrity check (U01 to U04, U06, U07, U09) | Malicious code runs inside \<System Name\> with access to every document | Low | High | Medium | Fix (PA-94 proposed by the system owner; awaits the authorising official) | Low | System owner | PA-34, PA-77, PA-78, PA-92, PA-94, PA-131 | Open; proposed on 12 November 2026, and the rating awaits the authorising official (D-RA-10) | 12 November 2026 |

## 3 Risk acceptance

**Table 2: Risk acceptance**

| Risk | Decision | Name | Date | Review date |
| --- | --- | --- | --- | --- |
| NC-14 (R-AC-07): the system does not enforce separate everyday accounts for administrators; they are issued by procedure | Accepted, Low, within the system owner's authority | \[Name\] | 5 November 2026 | 5 November 2027 |
| NC-38 (R-AC-11): nothing in the system assists sharing decisions; the project access approver decides under PRO-AC-16 | Accepted, Low, within the system owner's authority | \[Name\] | 5 November 2026 | 5 November 2027 |
| NC-03 (R-AC-06): account reviews, notices and disabling are not automated; PRO-AC-3 and PRO-AC-8 compensate | Accepted, Medium, for 12 months | \[Name\] | 6 November 2026 | 6 November 2027 |
| NC-11 (R-AC-07): a global administrator holds all rights; the system owner and auditor review every 3 months, with the Head of Cyber's extra check | Accepted, Medium, for 12 months | \[Name\] | 6 November 2026 | 6 November 2027 |
| NC-21 (R-AC-08): the screen lock is a browser overlay; the session ends at 30 minutes, and \<Organisation\>'s device lock compensates | Accepted, Medium, for 12 months | \[Name\] | 6 November 2026 | 6 November 2027 |
| NC-AU-08 (R-AC-07): audit records are not correlated across repositories; a weekly manual comparison is used | Accepted, Low, within the system owner's authority | \[Name\] | 6 November 2026 | 6 November 2027 |
| NC-IA-03 (R-AC-10): global administrators sign in with a password alone; no production documents are held while PA-23 runs | Accepted, High, for 6 months | \[Name\] | 6 November 2026 | 6 May 2027 |
| NC-IA-04 (R-AC-10): other users sign in with a password alone; no production documents are held while PA-23 runs | Accepted, Medium, for 6 months | \[Name\] | 6 November 2026 | 6 May 2027 |
| NC-CM-15 (R-AC-04): software is not technically restricted on the VMs; an approved list and ServiceNow approval are used (PA-55) | Accepted, Medium, for 12 months | \[Name\] | 6 November 2026 | 6 November 2027 |
| NC-CM-16 (R-AC-04): the approved software list is not technically enforced; it is reviewed every 12 months (PA-55) | Accepted, Medium, for 12 months | \[Name\] | 6 November 2026 | 6 November 2027 |
| NC-09, 10, 12, 13, 15, 18, NC-AU-12, NC-IA-09, NC-CM-13: parts other than TLS and secrets (PA-18, PA-19) open in production while their POA&M items are fixed | Accepted, High, until remediated, for no more than 6 months after production | \[Name\] | 6 November 2026 | 6 months after production |

## 4 Risk method

\<System Name\> is not required to meet every control. The organisation takes a risk-based approach: every non-compliance is identified and documented, its risk is understood, and a named person decides what happens to it. A risk that is acceptable may be accepted with a recorded decision. A risk that is too high requires a remediation plan in \<Plan of Action and Milestones\>. Finding a non-compliance does not by itself start a fix.

This method follows the risk response in CSS (tasks R-2 and R-3). The risk model follows CSS: a threat source exploits a weakness, with a likelihood, to cause an impact. The system owner agreed the method, and the authorising official confirmed it on 6 November 2026.

### 4.1 Rating

Likelihood and impact are each rated Low, Medium or High. Impact considers the confidentiality, integrity and availability of the documents \<System Name\> holds, and the effect on \<Organisation\>.

**Table 3: Risk rating**

| Likelihood | Impact Low | Impact Medium | Impact High |
| --- | --- | --- | --- |
| Low | Low | Low | Medium |
| Medium | Low | Medium | High |
| High | Low | Medium | High |

The matrix weights impact more than likelihood on purpose. A High impact can never rate below Medium, and a Low impact never above Low, because \<System Name\>'s harm is driven by what it holds: one disclosure of HR documents matters more than how often an attempt is made. CSS allows the organisation to set this (Appendix I).

**Table 3a: Likelihood scale**

| Level | Meaning |
| --- | --- |
| High | The threat source is motivated and able, the weakness is known or easy to find, and nothing in place stops it; expected within a year |
| Medium | The threat source is able, but something in place makes success less likely, or the weakness needs inside knowledge; possible within a year |
| Low | Needs rare skill, access or a chain of failures, or a compensating control is in place and tested; unlikely within a year |

**Table 3b: Impact scale**

| Level | Meaning |
| --- | --- |
| High | Severe or serious adverse effect (CSS): disclosure or loss of many documents or of special category data, or \<Organisation\> breaching the law |
| Medium | Serious adverse effect on part of the service: some documents disclosed or changed, or a loss of service beyond the 72-hour recovery time |
| Low | Limited adverse effect: no documents disclosed, and a short loss of service within the recovery time |

**Table 3c: Threat sources considered**

| Source (CSS, Table D-2) | Examples for \<System Name\> |
| --- | --- |
| Adversarial | An outsider exploiting a known flaw; an insider reading another project's documents; a supplier's compromised package |
| Accidental | An administrator deleting or misconfiguring; a user sending an export to the wrong person |
| Structural | A disk, VM or database failure; a software flaw; loss of the key or backup |
| Environmental | Loss of power, cooling or the site, provided by \<Organisation\> |

**Assumptions and uncertainty.**

- Ratings assume \<Organisation\>'s inherited controls work as their Cyber Essentials Plus certificate describes, until the evidence in \<Evidence Requests\> is seen.
- Risks are rated for the target design on the two VMs. Today's Docker stack holds sample data only.
- Where the evidence is a single test or a document review, not operation over time, the rating is the higher of the two plausible levels.
- Ratings are reviewed every 12 months, and after a significant change, incident or new test result (\<Procedures\>, PRO-RA-1).

**Table 3d: Provisional ratings**

A rating marked provisional was set before the evidence was seen. Each is settled, and the word removed, when the evidence below arrives.

| Non-compliance | Control | Rating | Settled by |
| --- | --- | --- | --- |
| NC-25 | AC-17 | High, provisional | EV-AC-08: the remote access service and its restrictions |
| NC-26 | AC-17(1) | Medium, provisional | EV-AC-09: monitoring of remote access |
| NC-28 | AC-17(3) | Medium, provisional | EV-AC-11: managed access points |
| NC-29 | AC-17(4) | Medium, provisional | EV-AC-12: whether administration ports can be reached from outside |
| NC-30, NC-31 | AC-18, AC-18(1) | Low, provisional | EV-AC-13: wireless requirements, authentication and encryption |
| NC-32 | AC-18(3) | Low, provisional | EV-AC-14: wireless disabled on the VMs |
| NC-33, NC-34 | AC-19, AC-19(5) | Low, provisional | EV-AC-15: mobile device rules and encryption |
| NC-35 | AC-20 | Medium, provisional | EV-AC-16: how unmanaged devices are kept out |
| NC-37 | AC-20(2) | Medium, provisional | EV-AC-17: portable storage controls |
| NC-SC-21, NC-SC-22 | SC-28, SC-28(1) | Medium, provisional | The VM build: BitLocker, encrypted backups and protected key rings in place and tested (PA-52, PA-93) |

### 4.2 Who may decide

**Table 4: Decision rules by rating**

| Rating | Default position | Who decides | Conditions of acceptance |
| --- | --- | --- | --- |
| Low | May be accepted | System owner | Recorded in this document; reviewed every 12 months |
| Medium | May be accepted or remediated | Authorising official, on the system owner's advice | A compensating measure where one exists; reviewed every 6 months |
| High | Not acceptable by default; a remediation plan is required | Authorising official | Acceptance only for a stated, limited period while the remediation plan runs |

These thresholds are \<System Name\>'s own. They are to be confirmed against \<Organisation\>'s risk management strategy and risk appetite (PM-9, EV-PM-01) by the Head of Cyber (D-PM-03). Until then they stand as agreed by the system owner and authorising official.

### 4.3 Treatments

**Table 5: Treatments**

| Treatment | Meaning | Where it is recorded |
| --- | --- | --- |
| Accept | The risk is understood and tolerated, and the non-compliance remains | Section 3 of this document, and the control's line in \<System Security Plan\>, section 7 |
| Remediate | The non-compliance is to be fixed, on a plan and not immediately | \<Plan of Action and Milestones\>, with milestones |
| Approve | The mechanism exists or no mechanism is needed, and only a decision or value is outstanding | \<Organisation\>'s corporate parameter values |
| Evidence | The control is expected to be inherited, and \<Organisation\> must supply the evidence | \<Evidence Requests\> and the control's line in \<System Security Plan\>, section 7, then rated when the evidence is seen |
| Tailor | The control or part is proposed as not applicable, with a rationale | \<System Security Plan\>, section 5 |

## 5 Non-compliance register

This register has one entry for each control that is not fully satisfied, by family in CSS order. **The authorising official decided some items on 6 November 2026, and chose to remediate TLS and committed secrets (PA-18, PA-19) before production, the other High items within 6 months after production, and the Medium items through the plan. Multi-factor authentication (NC-IA-03, NC-IA-04) is accepted to 6 May 2027 (\<Decision Register\>).** Cause codes are D (a decision or approval is outstanding), G (a gap in the system) and E (evidence is not yet available from the VMs or \<Organisation\>). Ratings marked "provisional" will be set when the evidence is seen.

### 5.1 Access Control (AC)

On 12 November 2026 the system owner stated that \<System Name\> signs users in through \<Organisation\>'s AD FS, with multi-factor authentication, takes roles and project access from Active Directory groups, and holds no accounts or passwords of its own (D-AC-23). The entries below on \<System Name\>'s own passwords, lockout and accounts record what was found on the build tested before that. They and their decisions stand until the family is reassessed with AD FS sign-in (PA-95).

There is one entry for each of the 39 AC controls, because none is yet fully satisfied. The system owner decided the Low items on 5 November 2026 (\<Decision Register\>). The treatment shown for the others is a proposal.

**Table 6: AC non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-01 | AC-1 | Policy and procedures are approved but not yet shared, the policy approval record has not been seen; the policy was legally reviewed on 12 November 2026 | D | R-AC-11 | Medium | Approve | No system change is needed | PA-20 | Approve |
| NC-02 | AC-2 | Rules are not approved, manager newly named, there is no approval step, and no review or monitoring takes place | D, G, E | R-AC-06 | Medium | Remediate | Review and leaver process are basic safeguards | PA-16, PA-20, PA-32 | Remediate |
| NC-03 | AC-2(1) | Reviews, notifications and disabling are not automated, and there is no directory link | G | R-AC-06 | Medium | Accept | Manual procedures PRO-AC-3 and PRO-AC-8 can compensate at this scale | PA-13, PA-16, PA-32 | Accepted |
| NC-04 | AC-2(2) | Accounts cannot be given an expiry | G | R-AC-06 | Low | Tailor | P-AC-09 prohibits temporary and emergency accounts | PA-13 | Tailored |
| NC-05 | AC-2(3) | Nothing disables accounts automatically; an account unused for 400 days still worked | G, D | R-AC-06 | Medium | Remediate | Monthly PRO-AC-8 is the interim measure | PA-13 | Remediate |
| NC-06 | AC-2(4) | Most account changes are not audited, and API records name "System" | G | R-AC-07 | Medium | Remediate | Administrator actions must be attributable | PA-14 | Remediate |
| NC-07 | AC-2(5) | The value is not approved; server sessions are not assessed | D, E | R-AC-11 | Low | Approve | Mechanism works and was tested | PA-20, PA-30 | Approved |
| NC-08 | AC-2(13) | Time limit and triggering risks are not approved, and PRO-AC-4 has not been walked through | D | R-AC-06 | Low | Approve | Mechanism works and was tested | PA-20 | Approved |
| NC-09 | AC-3 | Session functions, Folder export, and the database role and secrets exceed approved access | G, D, E | R-AC-02, R-AC-04 | High | Remediate | Too high to accept | PA-02, PA-19, PA-25, PA-26 | Remediate |
| NC-10 | AC-4 | Flows are not enforced, browsers load code from an outside service, and no TLS is set up | G, E | R-AC-05 | High | Remediate | Too high to accept once in production | PA-18, PA-26, PA-34 | Remediate |
| NC-11 | AC-5 | A global administrator holds all rights, and duties are not approved | D, G | R-AC-07 | Medium | Accept | Compensating quarterly review by the system owner and auditor, who are different people | PA-15 | Accepted |
| NC-12 | AC-6 | Shared database superuser, open privileged functions and maintenance pages in production | G, E | R-AC-04 | High | Remediate | Too high to accept | PA-10, PA-19, PA-26, PA-31 | Remediate |
| NC-13 | AC-6(1) | Secrets are readable in the repositories; users and projects are visible to any signed-in user; VM functions are unassigned | G, D, E | R-AC-04 | High | Remediate | Too high to accept | PA-07, PA-15, PA-19, PA-30 | Remediate |
| NC-14 | AC-6(2) | The rule is not approved, and everyday accounts are not issued | D, G | R-AC-07 | Low | Accept | Issue separate accounts by procedure; no system enforcement proposed | PA-17 | Accepted |
| NC-15 | AC-6(5) | The application database account is a superuser; privileged roles are not approved | G, D, E | R-AC-04 | High | Remediate | Too high to accept | PA-10, PA-30 | Remediate |
| NC-16 | AC-6(7) | No review of privileges has taken place | D, G | R-AC-06 | Medium | Remediate | Start PRO-AC-7; the access report is optional | PA-16 | Remediate |
| NC-17 | AC-6(9) | Many privileged functions are not logged, and ordinary users can write audit records | G, E | R-AC-07 | Medium | Remediate | The audit log must be reliable | PA-14, PA-29, PA-31 | Remediate |
| NC-18 | AC-6(10) | Ordinary users can run session, notification, cache, audit and migration functions | G | R-AC-02 | High | Remediate | Too high to accept | PA-02, PA-03, PA-06, PA-07, PA-29 | Remediate |
| NC-19 | AC-7 | Values are not approved; the password change path has no failure count; server logons are not assessed | D, G, E | R-AC-10 | Low | Approve | Sign-in mechanism works; path to be tested, and accepted if it needs a prior correct password | PA-20, PA-30, PA-35 | Approved |
| NC-20 | AC-8 | No system use notice is shown | G, D, E | R-AC-09 | Low | Remediate | Inexpensive, and supports monitoring and legal action | PA-11 | Remediate |
| NC-21 | AC-11 | The lock is a browser overlay that continues without a password | G, E | R-AC-08 | Medium | Accept | The session ends at 30 minutes, and \<Organisation\>'s device lock is expected to compensate | PA-12, PA-21 | Accepted |
| NC-22 | AC-11(1) | The overlay has not been observed on screen; workstations are not assessed | E | R-AC-08 | Low | Evidence | A browser check would close the application part | PA-21 | Obtain evidence |
| NC-23 | AC-12 | Values are not approved; one unexplained result on the 8-hour limit; server sessions are not assessed | D, G, E | R-AC-11 | Low | Approve | Mechanism works; T45 to be repeated | PA-20, PA-30, PA-33 | Approved |
| NC-24 | AC-14 | The list is not approved, and cache and diagnostic endpoints work without sign-in | D, G, E | R-AC-03 | Medium | Remediate | Endpoints have no business reason | PA-03, PA-07, PA-28 | Remediate |
| NC-25 | AC-17 | The remote access route is unnamed and no restrictions are documented | D, E | R-AC-05 | High, provisional | Evidence | \<Organisation\>'s service must be named | PA-18 | Obtain evidence |
| NC-26 | AC-17(1) | No evidence of remote access monitoring | E | R-AC-05 | Medium, provisional | Evidence | Expected to be inherited | PA-18, PA-21 | Obtain evidence |
| NC-27 | AC-17(2) | The stack uses plain HTTP; HTTPS and database TLS are not set up | G, E | R-AC-05 | High | Remediate | Too high to accept in production | PA-18 | Remediate |
| NC-28 | AC-17(3) | No evidence of managed access points | E | R-AC-05 | Medium, provisional | Evidence | Expected to be inherited | PA-18, PA-21 | Obtain evidence |
| NC-29 | AC-17(4) | Remote administration has not been decided, and the plan gives no rationale | D, E | R-AC-05 | Medium, provisional | Tailor | Not applicable if remote administration is not allowed | PA-18 | Tailored |
| NC-30 | AC-18 | No evidence for wireless access | E | R-AC-11 | Low, provisional | Evidence | \<System Name\> provides no wireless access of its own | PA-21 | Obtain evidence |
| NC-31 | AC-18(1) | No evidence for wireless authentication and encryption | E | R-AC-11 | Low, provisional | Evidence | Expected to be inherited | PA-21 | Obtain evidence |
| NC-32 | AC-18(3) | Not confirmed that the VMs have no wireless capability | E | R-AC-11 | Low, provisional | Evidence | Confirm on the built VMs | PA-21 | Obtain evidence |
| NC-33 | AC-19 | Mobile use is not decided | D, E | R-AC-11 | Low, provisional | Tailor | Not applicable if mobile use is not allowed | PA-21 | Tailored |
| NC-34 | AC-19(5) | Mobile encryption has no evidence | E | R-AC-11 | Low, provisional | Tailor | As AC-19 | PA-21 | Tailored |
| NC-35 | AC-20 | The rule is not approved, and the system cannot recognise an approved device | D, E | R-AC-11 | Medium, provisional | Approve | P-AC-22 sets the rule; \<Organisation\>'s device controls enforce it | PA-21 | Approve |
| NC-36 | AC-20(1) | No verification or agreement process exists | D | R-AC-11 | Low | Tailor | Not applicable if P-AC-22 forbids external use | PA-21 | Tailored |
| NC-37 | AC-20(2) | Portable storage controls have no evidence | E | R-AC-11 | Medium, provisional | Evidence | Downloads can reach any device the user has | PA-21 | Obtain evidence |
| NC-38 | AC-21 | Nothing assists sharing decisions, and restrictions are not recorded on documents | D, G | R-AC-11 | Low | Accept | The approver's manual decision under PRO-AC-16 is proportionate | PA-22 | Accepted |
| NC-39 | AC-22 | The no-public-content decision is not approved | D | R-AC-11 | Low | Tailor | Not applicable if P-AC-24 is approved | PA-22 | Tailored |

### 5.2 Awareness and Training (AT)

There is one entry for each AT control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 7: AT non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-AT-01 | AT-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-AT-07); procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-AT-02 | AT-2 | The \<System Name\> briefing is outlined (\<Awareness and Training Management\>, section 3.3) but not yet given; \<Organisation\>'s course not seen | E | R-AT-01 | Low | Evidence | Briefing given with the SyOps signature; course expected from \<Organisation\> | EV-AT-01, PA-96, PA-99 | Obtain evidence |
| NC-AT-03 | AT-2(2) | Insider threat scenarios outlined in the briefing; \<Organisation\>'s content not seen | E | R-AT-01 | Low | Evidence | As NC-AT-02 | EV-AT-01, PA-96, PA-99 | Obtain evidence |
| NC-AT-04 | AT-2(3) | Social engineering scenarios outlined in the briefing; \<Organisation\>'s content not seen | E | R-AT-01 | Low | Evidence | As NC-AT-02 | EV-AT-01, PA-96, PA-99 | Obtain evidence |
| NC-AT-05 | AT-3 | Role curriculum set (\<Awareness and Training Management\>, section 3.4); module content not yet written or given | D | R-AT-01 | Low | Approve | The security officer writes it from the curriculum (PRO-AT-2) | PA-97, PA-99, PA-100 | Approve |
| NC-AT-06 | AT-4 | Training register set; no records yet | D | R-AT-01 | Low | Approve | In PRO-AT-4 | PA-98 | Approve |

### 5.3 Audit and Accountability (AU)

There is one entry for each AU control that is not satisfied. AU-3(1) is satisfied in the application, so it has none. The system owner decided the Low items on 6 November 2026 (\<Decision Register\>); the others are proposals.

**Table 8: AU non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-AU-01 | AU-1 | Policy and procedures are approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-AU-02 | AU-2 | Most account, group and role changes are not logged, and logging is not coordinated with \<Organisation\> | D, G | R-AC-07 | Medium | Remediate | Administrator actions must be traceable | PA-14, PA-101, PA-103 | Remediate |
| NC-AU-03 | AU-3 | Some API records name "System"; VMs not assessable | G, E | R-AC-07 | Low | Remediate | Fix with PA-14 | PA-14 | Remediate |
| NC-AU-04 | AU-4 | No capacity is planned for 12 months of records | E | R-AC-07 | Low | Evidence | Set when the VMs are built | PA-42 | Obtain evidence |
| NC-AU-05 | AU-5 | Nobody is alerted when logging fails | D, G | R-AC-07 | Medium | Remediate | Silent loss of records would defeat investigation | PA-38 | Remediate |
| NC-AU-06 | AU-6 | The weekly review has not started | D, G | R-AC-07 | Medium | Remediate | Start at go-live with PRO-AU-1 | PA-40 | Remediate |
| NC-AU-07 | AU-6(1) | Nothing integrates review automatically | G | R-AC-07 | Low | Evidence | Depends on \<Organisation\>'s monitoring | PA-40 | Obtain evidence |
| NC-AU-08 | AU-6(3) | Records are not correlated across repositories | G | R-AC-07 | Low | Accept | A manual weekly comparison is proportionate for one system | PA-40 | Accepted |
| NC-AU-09 | AU-7 | No export or report | G | R-AC-07 | Low | Remediate | Needed for investigations | PA-41 | Remediate |
| NC-AU-10 | AU-7(1) | No search by project or document, and no sort choice | G | R-AC-07 | Low | Remediate | Fix with the export | PA-41 | Remediate |
| NC-AU-11 | AU-8 | The VMs' time source is not evidenced | E | R-AC-07 | Low | Evidence | \<Organisation\> provides it | EV-AU-02, PA-102 | Obtain evidence |
| NC-AU-12 | AU-9 | The application's database account can change, delete and empty audit records, and nothing checks the chain or alerts. The chain hash has no key and, as stored, cannot be recomputed (A36, A37) | G | R-AC-07, R-AU-01 | High | Remediate | Records cannot yet be relied on | PA-36, PA-37, PA-73, PA-74 | Remediate |
| NC-AU-13 | AU-9(4) | Global administrators can read audit records | G | R-AC-07 | Medium | Remediate | Agreed value; they are the people being reviewed | PA-39 | Remediate |
| NC-AU-14 | AU-11 | 12-month retention has no capacity or backup behind it | E | R-AC-07 | Low | Evidence | Set when the VMs are built | PA-42 | Obtain evidence |
| NC-AU-15 | AU-12 | PostgreSQL logging is off, events are built into each release, and the PA-14 events are missing | G, E | R-AC-07 | Medium | Remediate | Database changes would leave no trace | PA-14, PA-43, PA-105 | Remediate |
| NC-AU-16 | AU-9, PT-3 | Each audit event is repeated in the application log with the username, IP address and session ID, and that log is not protected, reviewed or kept to a set period (A38) | G | R-AU-02 | Medium | Remediate | Personal data must be kept to what an investigation needs, and audit information protected wherever it is held. Until fixed, \<Audit and Accountability Management\> treats the application log as audit information | PA-75, PA-104 | Remediate (D-AU-06) |
| NC-AU-17 | AU-2, AU-12 | Reading the audit log, start-up and shut-down, changes to logging and chain check results are not logged | G | R-AU-01 | Low | Remediate | Access to the audit log and gaps in logging must themselves be traceable | PA-76 | Remediate (system owner, Low) |

### 5.4 Assessment, Authorization and Monitoring (CA)

There is one entry for each CA control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 9: CA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-CA-01 | CA-1 | Policy and procedures are approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-CA-02 | CA-2 | Level 2 not held; all 19 plans approved (D-GEN-18) | D | R-AC-11 | Low | Approve | Follows Level 1 | PA-106 | Approve |
| NC-CA-03 | CA-2(1) | Independence not yet confirmed | D | R-AC-11 | Low | Approve | Independence statements on TPL-19 from \[Name\]'s team | PA-106 | Approve |
| NC-CA-04 | CA-3 | Connections are planned, not approved | D | R-AC-11 | Low | Approve | When each is built | PA-63 | Approve |
| NC-CA-05 | CA-5 | Monthly updates not started | D | R-AC-11 | Low | Approve | In PRO-CA-3 | PA-108 | Approve |
| NC-CA-06 | CA-6 | \<System Name\> is not authorised; common controls not accepted | D, E | R-AC-11 | Medium | Approve | The authorising official decides before production | EV-CA-01, PA-107 | Decide before production |
| NC-CA-07 | CA-7 | Monitoring not started | D | R-AC-11 | Low | Approve | Starts at go-live | PA-108 | Approve |
| NC-CA-08 | CA-7(1) | Independent monitoring not started | D | R-AC-11 | Low | Approve | Starts at go-live | PA-108 | Approve |
| NC-CA-09 | CA-7(4) | Risk monitoring not started | D | R-AC-11 | Low | Approve | Starts at go-live | PA-108 | Approve |
| NC-CA-10 | CA-9 | The link between the VMs is planned, not approved | D | R-AC-11 | Low | Approve | When the VMs are built | PA-63 | Approve |

### 5.5 Configuration Management (CM)

There is one entry for each CM control. CM-2(7) and CM-3(4) became satisfied once their values were agreed. The decisions are recorded in \<Decision Register\>.

**Table 10: CM non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-CM-01 | CM-1 | Policy and procedures are approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-CM-02 | CM-2 | No baseline for the VMs | E | R-AC-11 | Low | Evidence | Set when the VMs are built | PA-54, PA-80 | Obtain evidence |
| NC-CM-03 | CM-2(2) | Automation value not agreed | D | R-AC-11 | Low | Approve | Git tags are enough at this scale | PA-53 | Approve |
| NC-CM-04 | CM-2(3) | Only v1.0 exists | D | R-AC-11 | Low | Approve | Builds up with releases | PA-53 | Approve |
| NC-CM-05 | CM-2(7) | Kept in scope, with no travel settings defined | D | R-AC-11 | Low | Approve | No device is issued for travel | None | Approve; now satisfied |
| NC-CM-06 | CM-3 | The ServiceNow change workflow is not set up | D, G | R-AC-11 | Medium | Remediate | Needed before go-live | PA-53 | Remediate |
| NC-CM-07 | CM-3(2) | No release gate for testing | G | R-AC-11 | Low | Remediate | With PA-53 | PA-53 | Remediate |
| NC-CM-08 | CM-3(4) | Representatives not fully agreed | D | R-AC-11 | Low | Approve | Value proposed | None | Approve; now satisfied |
| NC-CM-09 | CM-4 | Impact analysis is not yet in use | D | R-AC-11 | Low | Approve | In PRO-CM-1 | PA-53 | Approve |
| NC-CM-10 | CM-4(2) | Verification is not yet in use | D | R-AC-11 | Low | Approve | In PRO-CM-1 | PA-53 | Approve |
| NC-CM-11 | CM-5 | Not assessable until the VMs exist | D, E | R-AC-11 | Low | Evidence | \<Organisation\> and the VMs | EV-CM-01, PA-112 | Obtain evidence |
| NC-CM-12 | CM-6 | Secure settings not yet applied | E | R-AC-04 | Low | Evidence | CIS Benchmarks on the VMs | PA-54, PA-80 | Obtain evidence |
| NC-CM-13 | CM-7 | Diagnostic and maintenance pages remain in production builds | G | R-AC-02 | High | Remediate | Same fix as PA-07 and PA-31 | PA-07, PA-31 | Remediate |
| NC-CM-14 | CM-7(1) | Review is not yet in use | D | R-AC-11 | Low | Approve | In PRO-CM-5 | PA-110 | Approve |
| NC-CM-15 | CM-7(2) | Software is not technically restricted, by decision | G | R-AC-04 | Medium | Accept | Decided by the system owner; the authorising official must accept the risk | PA-55 | Accepted |
| NC-CM-16 | CM-7(5) | No list yet, and not technically enforced, by decision | D, G | R-AC-04 | Medium | Accept | As NC-CM-15; the list itself is still to be written | PA-55 | Accepted |
| NC-CM-17 | CM-8 | Inventory is intended only | E | R-AC-11 | Low | Evidence | Completed when the VMs are built | PA-54 | Obtain evidence |
| NC-CM-18 | CM-8(1) | Updates are not yet in use | D | R-AC-11 | Low | Approve | In PRO-CM-1 | PA-111 | Approve |
| NC-CM-19 | CM-8(3) | Detection is not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-CM-02, PA-112 | Obtain evidence |
| NC-CM-20 | CM-9 | The plan is approved, and moves to SharePoint when all families are done | D | R-AC-11 | Low | Approve | No system change is needed | PA-88 | Approve |
| NC-CM-21 | CM-10 | \<System Name\>'s own components are reviewed in \<Configuration Management\>, section 3.5, and ImageSharp is under the free community licence (D-CM-09); \<Organisation\>'s licences are not yet evidenced | E | R-AC-11 | Low | Evidence | Obtain \<Organisation\>'s licence record; re-check component licences at each release | EV-CM-03, PA-112, PA-113 | Obtain evidence |
| NC-CM-22 | CM-11 | Installation approval is not yet in use | D, E | R-AC-11 | Low | Approve | In PRO-CM-4 | PA-110 | Approve |
| NC-CM-23 | CM-12 | Approved access list not yet built | D | R-AC-11 | Low | Approve | D-AC-14 | PA-111 | Approve |
| NC-CM-24 | CM-12(1) | No automated tools agreed | D | R-AC-11 | Low | Approve | Value proposed; tools confirmed through EV-CM-02 | EV-CM-02, PA-112 | Approve |
| NC-CM-25 | CM-2, CM-2(2) | Images are built from floating tags, so a release cannot be rebuilt exactly (C01, C02) | G | R-CM-01 | Medium | Remediate | The baseline must be reproducible | PA-77 | Remediate (authorising official, D-CM-10) |
| NC-CM-26 | CM-8, CM-8(1) | No bill of materials at release; the component inventory is kept by hand in \<Configuration Management\> (C04) | G | R-CM-01 | Low | Remediate | Keeps the inventory accurate at each release | PA-78 | Remediate (system owner, Low) |
| NC-CM-27 | CM-7 | Unused or development-only packages are in release builds (C05, C06) | G | R-CM-01 | Low | Remediate | Least functionality; a small change | PA-79 | Remediate (system owner, Low) |

### 5.6 Contingency Planning (CP)

There is one entry for each CP control. CP-2(3) and CP-2(8) are now satisfied by the approved plan. The decisions are recorded in \<Decision Register\>.

**Table 11: CP non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-CP-01 | CP-1 | Policy and procedures are approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-CP-02 | CP-2 | The plan is approved (D-CP-03, D-CP-11); not yet shared | D | R-CP-01 | Low | Approve | \<Contingency Planning Management\> is written | PA-88, PA-114 | Approve |
| NC-CP-03 | CP-2(1) | The plan is not yet coordinated by approval | D | R-AC-11 | Low | Approve | Drafted together with the incident plan | PA-114 | Approve |
| NC-CP-04 | CP-2(3) | Resumption within 72 hours is planned, not in use | D | R-CP-01 | Low | Approve | In \<Contingency Planning Management\> | None | Approve; now satisfied as a plan |
| NC-CP-05 | CP-2(8) | Critical assets are listed, not approved | D | R-AC-11 | Low | Approve | In \<Contingency Planning Management\> | None | Approve; now satisfied |
| NC-CP-06 | CP-3 | Training not started | D | R-AC-11 | Low | Approve | In PRO-CP-4 | PA-81 | Approve |
| NC-CP-07 | CP-4 | No test held | D | R-CP-01 | Low | Approve | In PRO-CP-4 | PA-81 | Approve |
| NC-CP-08 | CP-4(1) | No test held with the incident plan | D | R-AC-11 | Low | Approve | In PRO-CP-4 | PA-81 | Approve |
| NC-CP-09 | CP-6 | Second site for storage is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-10 | CP-6(1) | Separation is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-11 | CP-6(3) | Accessibility is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-12 | CP-7 | Second site for processing is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-13 | CP-7(1) | Separation is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-14 | CP-7(2) | Accessibility is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-15 | CP-7(3) | Priority of service is unconfirmed | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | PA-66, EV-CP-01 | Obtain evidence |
| NC-CP-16 | CP-8 | Alternate telecommunications are unconfirmed | E | R-CP-01 | Low | Evidence | Inherited from \<Organisation\> | EV-CP-02, PA-115 | Obtain evidence |
| NC-CP-17 | CP-8(1) | Priority of service is unconfirmed | E | R-CP-01 | Low | Evidence | Inherited from \<Organisation\> | EV-CP-02, PA-115 | Obtain evidence |
| NC-CP-18 | CP-8(2) | Single points of failure are unconfirmed | E | R-CP-01 | Low | Evidence | Inherited from \<Organisation\> | EV-CP-02, PA-115 | Obtain evidence |
| NC-CP-19 | CP-9 | No backups | G | R-CP-01 | Medium | Remediate | In place before production, as the authorising official decided | PA-64 | Remediate before production |
| NC-CP-20 | CP-9(1) | No backups to test | G | R-CP-01 | Medium | Remediate | With PA-64 | PA-64 | Remediate before production |
| NC-CP-21 | CP-9(8) | No backups to protect, and the default PostgreSQL backup is a plain archive that anyone holding it can read (R02) | G | R-CP-01 | Medium | Remediate | With PA-64 | PA-64 | Remediate before production |
| NC-CP-22 | CP-10 | \<System Name\> cannot be recovered today | G | R-CP-01 | Medium | Remediate | With PA-64 | PA-64 | Remediate before production |
| NC-CP-23 | CP-10(2) | Transaction logs are not archived, so data since the last backup would be lost (R09). Archiving is set up on the VMs with PA-64 | G | R-CP-01 | Medium | Remediate | With PA-64; archiving gives a recovery point of minutes | PA-64 | Remediate before production |
| NC-CP-24 | CP-3, CP-4, CP-4(1) | No contingency training or test has been held, and none is scheduled | D | R-CP-01 | Low | Remediate | The first restore test and tabletop are set for within 30 days of the VMs being built, and before production (D-CP-10) | PA-81 | Remediate (system owner, Low) |

### 5.7 Identification and Authentication (IA)

On 12 November 2026 the system owner stated that \<System Name\> signs users in through \<Organisation\>'s AD FS, with multi-factor authentication, takes roles and project access from Active Directory groups, and holds no accounts or passwords of its own (D-AC-23). The entries below on \<System Name\>'s own passwords, lockout and accounts record what was found on the build tested before that. They and their decisions stand until the family is reassessed with AD FS sign-in (PA-95).

There is one entry for each IA control that is neither satisfied nor tailored out in \<Tailoring Register\>.

**Table 12: IA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-IA-01 | IA-1 | Policy and procedures are approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-IA-02 | IA-2 | VMs not assessable | E | R-AC-11 | Low | Evidence | Application behaviour is tested | PA-25, PA-117 | Obtain evidence |
| NC-IA-03 | IA-2(1) | Global administrators sign in with a password alone | G | R-AC-10 | High | Remediate | Before production documents are held (D-GEN-13) | PA-23, PA-95 | Accepted to 6 May 2027 |
| NC-IA-04 | IA-2(2) | Ordinary users sign in with a password alone | G | R-AC-10 | Medium | Remediate | After privileged accounts (D-GEN-13) | PA-23, PA-95 | Accepted to 6 May 2027 |
| NC-IA-05 | IA-2(8) | Tokens work from another client, and traffic is plain HTTP | G | R-AC-05 | Medium | Remediate | TLS first, then decide on token binding | PA-18, PA-46, PA-117 | Remediate |
| NC-IA-06 | IA-3 | Device identification is not evidenced | E | R-AC-11 | Low | Evidence | Inherited from \<Organisation\> | EV-IA-01, PA-116 | Obtain evidence |
| NC-IA-07 | IA-4 | ServiceNow authorisation is not set up, and deletion frees a username | G | R-AC-06 | Low | Remediate | PRO-AC-3 keeps accounts disabled, which limits this | PA-20, PA-47 | Remediate |
| NC-IA-08 | IA-4(4) | No staff or contractor status | G | R-AC-06 | Low | Remediate | Small field | PA-47 | Remediate |
| NC-IA-09 | IA-5 | Users cannot change their own password, and secrets are committed and never rotated | D, G | R-AC-04 | High | Remediate | Secrets give full database control | PA-19, PA-44 | Remediate |
| NC-IA-10 | IA-5(1) | Blocked list has 15 entries, traffic is plain HTTP, there is no strength tool, and 12 to 14-character passwords are accepted where CSS requires 15 while sign-in is password-only (I02, I03) | G | R-AC-10 | Medium | Remediate | Weak passwords are accepted | PA-18, PA-45, PA-49, PA-82 | Remediate |
| NC-IA-11 | IA-5(6) | Secrets are committed in source | G | R-AC-04 | High | Remediate | With PA-19 | PA-19 | Remediate |
| NC-IA-12 | IA-6 | Windows logon not assessable | E | R-AC-11 | Low | Evidence | Application tested | PA-25 | Obtain evidence |
| NC-IA-13 | IA-7 | Cryptographic modules on the VMs are not confirmed | E | R-AC-11 | Low | Evidence | Confirm on the VMs | PA-48 | Obtain evidence |
| NC-IA-14 | IA-11 | VMs not assessable. The 8-hour limit passed five times in a row on 9 November (I11), closing PA-33 | E | R-AC-11 | Low | Evidence | Application tested | PA-33 | Obtain evidence |
| NC-IA-15 | IA-12 | Identity proofing is not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\>'s HR | EV-IA-02, PA-116 | Obtain evidence |
| NC-IA-16 | IA-12(2) | Identity evidence is not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\>'s HR | EV-IA-02, PA-116 | Obtain evidence |
| NC-IA-17 | IA-12(3) | Validation is not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\>'s HR | EV-IA-02, PA-116 | Obtain evidence |
| NC-IA-18 | IA-12(5) | Notice of proofing is not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\>'s HR | EV-IA-02, PA-116 | Obtain evidence |

### 5.8 Incident Response (IR)

There is one entry for each IR control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 13: IR non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-IR-01 | IR-1 | Policy and procedures are approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-IR-02 | IR-2 | Training not started | D | R-IR-01 | Low | Approve | In PRO-IR-3 | PA-81, PA-97 | Approve |
| NC-IR-03 | IR-3 | No exercise held | D | R-IR-01 | Low | Approve | In PRO-IR-3 | PA-81 | Approve |
| NC-IR-04 | IR-3(2) | No exercise held with the contingency plan | D | R-IR-01 | Low | Approve | In PRO-IR-3 | PA-81 | Approve |
| NC-IR-05 | IR-4 | The plan is approved (D-IR-03), and handling is not yet in use; containment was shown in Docker (D01, D03) | D | R-IR-01 | Low | Approve | In PRO-IR-2 | PA-14, PA-118 | Approve |
| NC-IR-06 | IR-4(1) | ServiceNow is not set up for incidents | G | R-IR-01 | Low | Remediate | With the other ServiceNow workflows | PA-65 | Remediate |
| NC-IR-07 | IR-5 | Tracking is not in use | D | R-IR-01 | Low | Approve | In PRO-IR-2 | PA-65, PA-118 | Approve |
| NC-IR-08 | IR-6 | Reporting is not in use | D | R-IR-01 | Low | Approve | In PRO-IR-1 | EV-IR-01, PA-118 | Approve |
| NC-IR-09 | IR-6(1) | ServiceNow is not set up for incidents | G | R-IR-01 | Low | Remediate | With the other ServiceNow workflows | PA-65 | Remediate |
| NC-IR-10 | IR-6(3) | Supplier reporting is not in use | D | R-IR-01 | Low | Approve | In PRO-IR-1 | PA-118 | Approve |
| NC-IR-11 | IR-7 | Assistance is not in use | D | R-IR-01 | Low | Approve | In PRO-IR-4 | EV-IR-01, PA-118 | Approve |
| NC-IR-12 | IR-7(1) | ServiceNow is not set up for incidents | G | R-IR-01 | Low | Remediate | With the other ServiceNow workflows | PA-65 | Remediate |
| NC-IR-13 | IR-8 | The plan is approved (D-IR-03); not yet shared | D | R-IR-01 | Low | Approve | \<Incident Response Management\> is written | PA-88, PA-119 | Approve |

### 5.9 Maintenance (MA)

There is one entry for each MA control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 14: MA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-MA-01 | MA-1 | Policy \<ver\> awaits the Head of Cyber (D-MA-07); procedures approved, and the design approved as a register chapter at \<ver\>, now in \<Maintenance Management\>; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-MA-02 | MA-2 | Controlled maintenance is not in use, and sanitising isn't evidenced. The built-in maintenance pages leave no audit record (M03), and schema changes are not recorded (M09). The check after maintenance works in Docker (M06 to M08) | D, E, G | R-AC-07 | Low | Remediate | Records, schedule and checklist are in PRO-MA-1 and PRO-MA-6; the code fixes are planned | EV-MA-01; PA-31, PA-84, PA-120 | Remediate |
| NC-MA-03 | MA-3 | A provisional tool list is written (\<Maintenance Management\>). Five built-in maintenance pages are open to global administrators (M01), and the images hold a package manager (M10) | D, G | R-AC-02 | Low | Remediate | The pages are used only under a change record until they are removed | PA-67, PA-31, PA-85 | Remediate |
| NC-MA-04 | MA-3(1) | Tool inspection is not in use | D | R-PE-01 | Low | Approve | In PRO-MA-3 | PA-67, PA-120 | Approve |
| NC-MA-05 | MA-3(2) | Defender isn't yet on the VMs | E | R-PE-01 | Low | Evidence | With PA-58 | PA-58 | Obtain evidence |
| NC-MA-06 | MA-3(3) | Removal control is not in use. The rule now also covers copies of data and logs taken for support (D-MA-06) | D | R-PE-01 | Low | Approve | In PRO-MA-3 and PRO-MA-7 | PA-120 | Approve |
| NC-MA-07 | MA-4 | Remote maintenance is not in use, and \<Organisation\>'s route isn't evidenced. The admin portal is published on every network interface (M04) and is password-only, and the settings point at a public database address (M05). Sign-out does end an admin session (M12) | D, E, G | R-AC-10 | Medium | Remediate | Restrict the admin portal to the managed route; multi-factor sign-in by the PA-23 milestone | EV-MA-02; PA-83, PA-19, PA-23, PA-120 | Remediate, proposed by the system owner; awaits the authorising official |
| NC-MA-08 | MA-5 | A provisional list of maintenance people, with screening, Part B and accounts, is written (\<Maintenance Management\>); not yet confirmed at VM build | D | R-PE-01 | Low | Approve | Confirm at VM build | PA-67 | Approve |
| NC-MA-09 | MA-6 | Support and parts within 24 hours aren't evidenced. .NET 10 and PostgreSQL 18 are supported versions (M11) | E | R-CP-01 | Low | Evidence | Expected from \<Organisation\> | EV-MA-01; PA-120 | Obtain evidence |

### 5.10 Media Protection (MP)

There is one entry for each MP control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 15: MP non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-MP-01 | MP-1 | Policy \<ver\> awaits the Head of Cyber (D-MP-07); procedures approved, and the design approved as a register chapter at \<ver\>, now in \<Media Protection Management\>; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-MP-02 | MP-2 | Access to disks and backup media isn't evidenced; the paper rule is not in use. Only editors can create exports (P01) | D, E | R-PE-01 | Low | Evidence | \<Organisation\>, and PRO-MP-1 | EV-MP-01; PA-121 | Obtain evidence |
| NC-MP-03 | MP-3 | Nothing \<System Name\> shows or produces is marked RESTRICTED (P04, P07); printouts are marked by hand | D, G | R-PE-01 | Low | Remediate | Manual marking (PRO-MP-1) until the system marks | PA-87 | Remediate |
| NC-MP-04 | MP-4 | Bulk export leaves full, unencrypted copies on the application server after download and after a restart (P02, P05, P06, P09); disk and backup storage isn't evidenced; the paper rule is not in use | D, E, G | R-AC-01 | Medium | Remediate | A check each working day of the export folder (C49) until PA-86 is fixed | EV-MP-01; PA-86, PA-26, PA-52, PA-88, PA-121 | Remediate, proposed by the system owner; awaits the authorising official |
| NC-MP-05 | MP-5 | Physical transport, by exception only, isn't evidenced; network backup copies are not yet encrypted (R02) | E | R-PE-01 | Low | Evidence | Expected from \<Organisation\>; backups encrypted under PA-64 | EV-MP-01; PA-64, PA-121 | Obtain evidence |
| NC-MP-06 | MP-6 | Sanitising isn't evidenced; methods by media type are now set to CSS and IEEE 2883-2022, with cryptographic erase for virtual disks | E | R-PE-01 | Low | Evidence | Expected from \<Organisation\>; cryptographic erase relies on PA-52 | EV-MP-02; PA-52, PA-121 | Obtain evidence |
| NC-MP-07 | MP-7 | USB blocking on users' devices and the VMs isn't evidenced | E | R-PE-01 | Low | Evidence | Expected from \<Organisation\> | EV-AC-17, EV-MP-03; PA-121 | Obtain evidence |

### 5.11 Physical and Environmental Protection (PE)

There is one entry for each PE control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 16: PE non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-PE-01 | PE-1 | Policy \<ver\> legally reviewed and awaits the Head of Cyber (D-PE-09); procedures approved, and the design approved as a register chapter at \<ver\>, now in \<Physical and Environmental Protection Management\>; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-PE-02 | PE-2 | Access list isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-01; PA-122 | Obtain evidence |
| NC-PE-03 | PE-3 | Access control isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-01; PA-122 | Obtain evidence |
| NC-PE-04 | PE-4 | Protection of lines isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-01; PA-122 | Obtain evidence |
| NC-PE-05 | PE-5 | Office controls and secure print release on managed printers aren't evidenced; the printers are not yet listed | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-05; PA-122 | Obtain evidence |
| NC-PE-06 | PE-6 | Access monitoring isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-01; PA-122 | Obtain evidence |
| NC-PE-07 | PE-6(1) | Alarms and surveillance aren't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-01; PA-122 | Obtain evidence |
| NC-PE-08 | PE-8 | Visitor records aren't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-01; PA-122 | Obtain evidence |
| NC-PE-09 | PE-9 | Power protection isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-02; PA-122 | Obtain evidence |
| NC-PE-10 | PE-10 | Emergency shutoff isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-02; PA-122 | Obtain evidence |
| NC-PE-11 | PE-11 | Backup power isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-02; PA-122 | Obtain evidence |
| NC-PE-12 | PE-12 | Emergency lighting isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-02; PA-122 | Obtain evidence |
| NC-PE-13 | PE-13 | Fire protection isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-03; PA-122 | Obtain evidence |
| NC-PE-14 | PE-13(1) | Automatic notification isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-03; PA-122 | Obtain evidence |
| NC-PE-15 | PE-14 | Environmental controls aren't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-03; PA-122 | Obtain evidence |
| NC-PE-16 | PE-15 | Water protection isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-03; PA-122 | Obtain evidence |
| NC-PE-17 | PE-16 | Delivery and removal control isn't evidenced | E | R-PE-01 | Low | Evidence | Inherited from \<Organisation\> | EV-PE-04; PA-122 | Obtain evidence |
| NC-PE-18 | PE-17 | Home working controls are not yet assessed (C30 checklist) or evidenced; no printing at home unless approved | D, E | R-PE-01 | Low | Approve; obtain evidence | In PRO-PE-4 | EV-PE-05; PA-122 | Approve |

### 5.12 Planning (PL)

There is one entry for each PL control not yet satisfied. PL-10 and PL-11 are satisfied. PL-4(1) is now satisfied by the approved rules. The decisions are recorded in \<Decision Register\>.

**Table 17: PL non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-PL-01 | PL-1 | Policy \<ver\> legally reviewed and awaits the Head of Cyber (D-PL-07); procedures approved, and the design approved as a register chapter at \<ver\>, now in \<Planning Management\>; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-PL-02 | PL-2 | The plan isn't yet shared; privacy risk results aren't ready; \<Organisation\>'s enterprise architecture is unseen | D, E | R-AC-11 | Low | Approve | \<Privacy Plan\> is approved; results follow PA-72 | EV-PL-01; PA-123 | Approve |
| NC-PL-03 | PL-4 | Rules are approved; none signed yet; TPL-21 and the register of signatures are ready | D | R-AC-11 | Low | Approve | In PRO-PL-2 | PA-123 | Approve |
| NC-PL-04 | PL-4(1) | The social media rule awaits approval | D | R-AC-11 | Low | Approve | In \<Security Operating Procedures\> \<ver\> | None | Approve; now satisfied |
| NC-PL-05 | PL-8 | First yearly architecture review not yet due; no procurement yet | D | R-AC-11 | Low | Approve | Security approach in \<Security Architecture\> \<ver\>; critical components in \<Risk Assessment Management\>, section 3.9 | PA-123 | Approve |
| NC-PL-06 | PL-2e | The plans and evidence are not yet in the restricted store. Since 12 November 2026 the Git working copy whose remote is GitHub ignores them, and they are kept in a private local repository with no remote | D | R-AC-11 | Medium | Remediate | Nothing has been committed to the code repository, and the folders are now ignored by it | PA-88 | Move to SharePoint (D-GEN-15, D-PL-06) |

### 5.13 Personnel Security (PS)

There is one entry for each PS control, as none is yet satisfied. The decisions are recorded in \<Decision Register\>.

**Table 18: PS non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-PS-01 | PS-1 | Policy \<ver\> awaits the Head of Cyber and legal review (D-PS-08); version \<ver\> is approved and legally reviewed; procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-PS-02 | PS-2 | Every role is designated (\<Personnel Security Management\>, section 3.2); \<Organisation\>'s screening criteria aren't evidenced, and the first scheduled review isn't due | D, E | R-PS-01 | Low | Approve | In \<Personnel Security Management\> | EV-PS-01; PA-125 | Approve |
| NC-PS-03 | PS-3 | A minimum is set (\<Personnel Security Management\>, section 3.3); \<Organisation\>'s screening isn't evidenced | E | R-PS-01 | Low | Evidence | Expected from \<Organisation\> | EV-PS-01; PA-125 | Obtain evidence |
| NC-PS-04 | PS-4 | The leaver route isn't built, including the 1-hour route for a higher-risk leaver; exit process isn't evidenced | D, E | R-PS-01 | Low | Remediate | With PA-32 | PA-32, PA-125, EV-PS-02 | Remediate |
| NC-PS-05 | PS-5 | The mover route isn't built | D | R-PS-01 | Low | Remediate | With PA-32 | PA-32 | Remediate |
| NC-PS-06 | PS-6 | Agreements exist; none signed | D | R-PS-01 | Low | Approve | In PRO-PS-1 | PA-123, PA-125 | Approve |
| NC-PS-07 | PS-7 | Contract terms aren't evidenced | D, E | R-PS-01 | Low | Evidence | Expected from \<Organisation\> | EV-PS-03; PA-125 | Obtain evidence |
| NC-PS-08 | PS-8 | Sanctions process isn't evidenced | D, E | R-PS-01 | Low | Evidence | Expected from \<Organisation\> | EV-PS-02; PA-125 | Obtain evidence |
| NC-PS-09 | PS-9 | \<System Name\>'s role duties are in \<Roles and Responsibilities\>; \<Organisation\>'s job descriptions haven't been seen | E | R-PS-01 | Low | Evidence | Expected from \<Organisation\> | EV-PS-02; PA-125 | Obtain evidence |

### 5.14 Personally Identifiable Information (PT)

There is one entry for each PT control and other privacy baseline control not yet satisfied. SI-19 does not apply. The decisions are recorded in \<Decision Register\>.

**Table 19: PT non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-PT-01 | PT-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-PT-18); procedures approved, and the design approved as a register chapter at \<ver\>, now in \<PII Processing Management\>; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-PT-02 | PT-2 | The lawful basis and conditions for each kind of data aren't confirmed; placeholders are ready in the inventory and draft DPIA | D | R-PT-01 | Medium | Remediate | The legal adviser confirms it before production | PA-72 | Remediate |
| NC-PT-03 | PT-3 | Purposes await approval; the notice hasn't been seen | D, E | R-PT-01 | Low | Approve | In \<Policy\> (PT) | EV-PT-01; PA-126 | Approve |
| NC-PT-04 | PT-4 | The position on consent isn't confirmed | D | R-PT-01 | Low | Approve | The legal adviser confirms it | PA-126 | Approve |
| NC-PT-05 | PT-5 | The privacy notice hasn't been seen, and \<System Name\>'s pages do not link to it (Q06) | E | R-PT-01 | Low | Evidence | Expected from \<Organisation\> | EV-PT-01, PA-90 | Obtain evidence |
| NC-PT-06 | PT-7 | Conditions for special categories aren't confirmed, and HR documents aren't marked as personal data (Q01) | D | R-PT-01 | Medium | Remediate | Follows the impact assessment, before production | PA-72, PA-89 | Remediate |
| NC-PT-07 | AC-3(14) | No complete search across projects for one person (Q02); the route is in PRO-PT-1 | D | R-PT-01 | Low | Approve | In PRO-PT-1 | PA-89 | Approve |
| NC-PT-08 | AT-3(5) | Privacy training hasn't been given | D | R-PT-01 | Low | Approve | Given before access | PA-97 | Approve |
| NC-PT-09 | AU-3(3) | Audit free text holds no extra personal data (Q04), but the application log repeats usernames and IP addresses (Q05) | D | R-PT-01 | Low | Remediate | A small check | PA-71, PA-75 | Remediate |
| NC-PT-10 | IR-2(3) | Breach training hasn't been given | D | R-PT-01 | Low | Approve | With incident response training | PA-81, PA-97 | Approve |
| NC-PT-11 | IR-8(1) | Now covered in \<Incident Response Management\>, section 3.8: harm, telling people and the breach register | D | R-PT-01 | Low | Approve | Added at the next review of \<Incident Response Management\> | None | Approve; now satisfied |
| NC-PT-12 | PE-8(3) | Visitor records haven't been seen | E | R-PT-01 | Low | Evidence | Expected from \<Organisation\> | EV-PT-02; PA-122 | Obtain evidence |
| NC-PT-13 | PL-9 | Documents aren't yet in the Restricted store | D | R-AC-11 | Low | Approve | Move to SharePoint now (D-GEN-15, PA-88) | PA-88 | Approve |
| NC-PT-14 | RA-8 | No impact assessment has been done | D | R-PT-01 | Medium | Remediate | Before production | PA-72 | Remediate |
| NC-PT-15 | SA-8(33) | Minimisation awaits approval | D | R-PT-01 | Low | Approve | Reviewed in the impact assessment | PA-72 | Approve |
| NC-PT-16 | SC-7(24) | Permitted processing isn't monitored | D, G | R-PT-01 | Low | Remediate | Scope decided by the impact assessment | PA-71 | Remediate |
| NC-PT-17 | SI-12(1) | Personal data in projects hasn't been reviewed | D | R-PT-01 | Low | Approve | In PRO-PT-5 | PA-126 | Approve |
| NC-PT-18 | SI-12(2) | The rule for research and training awaits approval | D | R-PT-01 | Low | Approve | Testing already uses sample data | PA-126 | Approve |
| NC-PT-19 | SI-12(3) | No retention or disposal exists: no retention field (Q08), and deleted pages stay until the database is vacuumed (Q03) | G | R-PT-01 | Medium | Remediate | Needed before real personal data is held | PA-70 | Remediate |
| NC-PT-20 | SI-18 | Quality checks await approval | D | R-PT-01 | Low | Approve | In PRO-PT-5 | PA-126 | Approve |
| NC-PT-21 | SI-18(4) | Corrections in the admin portal aren't audited (Q10); the route is in PRO-PT-1 | D | R-PT-01 | Low | Approve | In PRO-PT-1 | PA-89 | Approve |
| NC-PT-22 | AU-2, SI-18(4) | Deleting or correcting a document in the admin portal writes no audit record (Q03, Q10) | G | R-PT-01 | Medium | Remediate | Only global administrators can delete; the pages show who last modified a document | PA-89 | Remediate |

### 5.15 Risk Assessment (RA)

There is one entry for each RA control except RA-2, which is satisfied. RA-9 became satisfied when the critical components list, now in \<Risk Assessment Management\>, section 3.9, was approved. The first supply chain review was held on 11 November 2026 (D-RA-09), and the RA findings were checked with Test-Vulnerability.ps1. The decisions are recorded in \<Decision Register\>.

**Table 20: RA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-RA-01 | RA-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-RA-06); procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-RA-02 | RA-3 | First review not due; results not shared with the Head of Cyber; not reviewed after the changes to sign-in and hosting of 12 and 13 November 2026 | D, E | R-AC-11 | Low | Approve | In PRO-RA-1 | EV-RA-01; PA-127 | Approve |
| NC-RA-03 | RA-3(1) | First supply chain review held on 11 November 2026 (TPL-23, D-RA-09); the first yearly update is not yet due; the update called for by the changes to sign-in and hosting of 12 and 13 November 2026 has not been held | D | R-SI-01 | Low | Approve | In PRO-RA-2 | PA-127 | Approve |
| NC-RA-04 | RA-5 | Nothing scans the images or operating system packages (V02), and 7 package advisories are open, 5 of them High (V01); nothing scans \<System Name\>'s own applications | G | R-SI-01 | Medium | Remediate | Needed before go-live | PA-56, PA-62 | Remediate |
| NC-RA-05 | RA-5(2) | No scanner | G | R-SI-01 | Low | Remediate | With PA-62 | PA-62 | Remediate |
| NC-RA-06 | RA-5(5) | Not assessable until the VMs exist | E | R-AC-11 | Low | Evidence | On the VMs | PA-62 | Obtain evidence |
| NC-RA-07 | RA-5(11) | Route not yet agreed with \<Organisation\>; the route's published terms are not set | D | R-AC-11 | Low | Approve | Value agreed | EV-RA-01; PA-127 | Approve |
| NC-RA-08 | RA-7 | Only assessment findings have arisen | D | R-AC-11 | Low | Approve | In PRO-RA-1 | PA-127 | Approve |
| NC-RA-09 | RA-9 | None: the list is approved, extended and reviewed (\<Risk Assessment Management\>) | D | R-AC-11 | Low | Approve | In \<Risk Assessment Management\> | None | Approve; now satisfied |

### 5.16 System and Services Acquisition (SA)

There is one entry for each assessed SA control. SA-4(1), SA-4(2), SA-4(9), SA-15(3) and SA-22 became satisfied on 11 November 2026, and stay listed for traceability. SA-4(10) is tailored (TR-SA-01). The decisions are recorded in \<Decision Register\>.

**Table 21: SA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-SA-01 | SA-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-SA-16); procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-SA-02 | SA-2 | Security and privacy costs aren't yet raised in budgeting; the yearly review now records them (TPL-23) | D | R-AC-11 | Low | Approve | At the next yearly budgeting | PA-128 | Approve |
| NC-SA-03 | SA-3 | The lifecycle follows CSS \<ver\>, mapped in \<System and Services Acquisition Management\>, section 3.2; not yet in routine use | D | R-SA-01 | Low | Approve | In PRO-SA-1 | PA-128 | Approve |
| NC-SA-04 | SA-4 | Contract terms haven't been seen | E | R-SA-01 | Low | Evidence | Expected from \<Organisation\> | EV-SA-01; PA-128 | Obtain evidence |
| NC-SA-05 | SA-4(1) | None: the SSP, section 7, and the family design documents describe each control's functional properties | None | R-SA-01 | Low | Approve | Now satisfied | None | Approve; now satisfied |
| NC-SA-06 | SA-4(2) | None: \<Security Architecture\> and the SSP figures give the design information | None | R-SA-01 | Low | Approve | Now satisfied | None | Approve; now satisfied |
| NC-SA-07 | SA-4(9) | None: the functions, ports, protocols and services are in \<System Security Plan\>, section 3.7 | None | R-SA-01 | Low | Approve | Now satisfied | None | Approve; now satisfied |
| NC-SA-08 | SA-5 | No approved administrator or user guide; drafts \<Administrator Guide\> and \<User Guide\> \<ver\> await the developers (S10) | D, G | R-SA-01 | Low | Remediate | Confirmed before go-live | PA-69 | Remediate |
| NC-SA-09 | SA-8 | Principles mapped for specification and design in \<Security Architecture\>; development, implementation and changes not yet checked against them | D | R-SA-01 | Low | Approve | Applied from now on | PA-128 | Approve |
| NC-SA-10 | SA-9 | Providers' compliance hasn't been seen; service levels are not recorded | D, E | R-SA-01 | Low | Evidence | Expected from \<Organisation\> and GitHub | EV-SA-02, EV-SA-03; PA-128 | Obtain evidence |
| NC-SA-11 | SA-9(2) | Providers' lists haven't been seen, including GitHub's | E | R-SA-01 | Low | Evidence | Expected from the providers | EV-SA-02, EV-SA-03; PA-128 | Obtain evidence |
| NC-SA-12 | SA-10 | No repository protects its default branch, requires review or alerts on dependencies; the v1.0 release had no reviewed merge or signed tag; 10 test scripts aren't in Git (S01 to S07) | D, G | R-SA-01 | Medium | Remediate | Before production (D-SA-14) | PA-53, PA-91 | Remediate |
| NC-SA-13 | SA-11 | No build pipeline, test gate or unit tests; the build turns the package audit off; the test scripts are run by hand (S06, S08); the web applications are not verified to OWASP ASVS 5.0 Level 2 | D, G | R-SA-01 | Medium | Remediate | Before production (D-SA-14) | PA-68, PA-92 | Remediate |
| NC-SA-14 | SA-15 | Process and tools documented in \<System and Services Acquisition Management\>, sections 3.2 and 3.10; not yet reviewed against the requirements | D | R-SA-01 | Low | Approve | In PRO-SA-6 | PA-128 | Approve |
| NC-SA-15 | SA-15(3) | None: criticality is analysed in \<Risk Assessment Management\>, section 3.9 | None | R-SA-01 | Low | Approve | Now satisfied | None | Approve; now satisfied |
| NC-SA-16 | SA-22 | None: no component is within 6 months of the end of its support (S09) | None | R-SI-01 | Low | Approve | Now satisfied | None | Approve; now satisfied |

### 5.17 System and Communications Protection (SC)

There is one entry for each SC control that is neither satisfied nor tailored out. SC-2 is satisfied in the application. The decisions are recorded in \<Decision Register\>.

**Table 22: SC non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-SC-01 | SC-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-SC-06); procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-SC-02 | SC-4 | Not assessable until the VMs exist; bulk export leaves document copies in a shared temporary folder (PA-86) | E | R-AC-11 | Low | Evidence | Windows Server | PA-54, PA-86 | Obtain evidence |
| NC-SC-03 | SC-5 | Network protections are not evidenced, and there is no rate limiter | G, E | R-AC-03 | Low | Evidence | \<Organisation\> first, then decide | PA-50 | Obtain evidence |
| NC-SC-04 | SC-7 | Boundary protection is not evidenced; \<System Name\>'s own part (host firewalls, listening addresses) is not set, and the admin portal and API listen on every interface (PA-83, N07) | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-02, PA-83 | Obtain evidence |
| NC-SC-05 | SC-7(3) | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-02; PA-129 | Obtain evidence |
| NC-SC-06 | SC-7(4) | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-02; PA-129 | Obtain evidence |
| NC-SC-07 | SC-7(5) | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-AC-03, PA-83 | Obtain evidence |
| NC-SC-08 | SC-7(7) | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-03; PA-129 | Obtain evidence |
| NC-SC-09 | SC-7(8) | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-03; PA-129 | Obtain evidence |
| NC-SC-10 | SC-8 | Web and database traffic is plain | G | R-AC-05 | High | Remediate | Too high to accept in production | PA-18 | Remediate |
| NC-SC-11 | SC-8(1) | Web and database traffic is not encrypted | G | R-AC-05 | High | Remediate | With PA-18 | PA-18 | Remediate |
| NC-SC-12 | SC-10 | Network disconnect is not evidenced | E | R-AC-11 | Low | Evidence | Application sessions end at 30 minutes | EV-SC-01; PA-129 | Obtain evidence |
| NC-SC-13 | SC-12 | Keys are committed in source, with no store or rotation, and the data protection key rings are unencrypted (N08, N09) | G | R-AC-04 | High | Remediate | With PA-19 and PA-93 | PA-19, PA-93 | Remediate |
| NC-SC-14 | SC-13 | TLS, disk and key ring encryption are not in place, and document checksums use MD5 | G | R-SC-01 | Medium | Remediate | With PA-18 and PA-52 | PA-18, PA-52, PA-61, PA-93 | Remediate |
| NC-SC-15 | SC-17 | Certificates are not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-04; PA-129 | Obtain evidence |
| NC-SC-16 | SC-18 | UI application and Admin application send no page policy (their security headers are switched off in the code); the configured policy allows inline scripts, eval and outside hosts (N04, N10, N12) | D, G | R-AC-02 | Medium | Remediate | Reduces script injection risk | PA-34, PA-51 | Remediate |
| NC-SC-17 | SC-20 | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-05; PA-129 | Obtain evidence |
| NC-SC-18 | SC-21 | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-05; PA-129 | Obtain evidence |
| NC-SC-19 | SC-22 | Not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SC-05; PA-129 | Obtain evidence |
| NC-SC-20 | SC-23 | The session cookie is not Secure over HTTP | G | R-AC-05 | Medium | Remediate | Follows from TLS | PA-18 | Remediate |
| NC-SC-21 | SC-28 | Documents in PostgreSQL, backups, export copies and key rings are not encrypted at rest in Docker; VMs not built | E | R-SC-01 | Medium, provisional | Remediate | Set on the VMs | PA-52, PA-86, PA-93 | Remediate |
| NC-SC-22 | SC-28(1) | As SC-28 | E | R-SC-01 | Medium, provisional | Remediate | Set on the VMs | PA-52 | Remediate |
| NC-SC-23 | SC-39 | Not assessable until the VMs exist | E | R-AC-11 | Low | Evidence | Windows Server | PA-54 | Obtain evidence |

### 5.18 System and Information Integrity (SI)

There is one entry for each SI control that is not tailored out (SI-8, SI-8(2): TR-SI-01). The decisions are recorded in \<Decision Register\>.

**Table 23: SI non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-SI-01 | SI-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-SI-06); procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-SI-02 | SI-2 | 7 advisories are open in two packages, and the process is not in use; SI now follows the one timetable in \<Risk Assessment Management\>, section 3.6 | D, G, E | R-SI-01 | High | Remediate | Before production, as agreed by the system owner | PA-56 | Remediate |
| NC-SI-03 | SI-2(2) | Update status is checked by hand | G | R-SI-01 | Medium | Remediate | Simple once the VMs exist | PA-57, PA-91 | Remediate |
| NC-SI-04 | SI-3 | Uploads are not scanned; Defender is not yet in place | G, E | R-SI-01 | Medium | Remediate | Scan at upload, as agreed by the system owner | PA-58 | Remediate |
| NC-SI-05 | SI-4 | Monitoring is not started or evidenced | D, E | R-AC-07 | Low | Evidence | \<Organisation\> and the VMs | EV-SI-01; PA-130 | Obtain evidence |
| NC-SI-06 | SI-4(2) | No automated analysis | G | R-AC-07 | Medium | Remediate | With PA-59 | PA-59 | Remediate |
| NC-SI-07 | SI-4(4) | Traffic monitoring is not evidenced | E | R-AC-11 | Low | Evidence | \<Organisation\> | EV-SI-01; PA-130 | Obtain evidence |
| NC-SI-08 | SI-4(5) | Nothing raises an alert (H12); detection use cases are set in \<System and Information Integrity Management\>, section 3.4 | G | R-AC-07 | Medium | Remediate | Attacks would go unnoticed | PA-59 | Remediate |
| NC-SI-09 | SI-5 | Sources extended to CISA's exploited list and NCSC Early Warning; not started | D | R-AC-11 | Low | Approve | In PRO-SI-5 | PA-130 | Approve |
| NC-SI-10 | SI-7 | MD5 checksums, and no release checksum | G, E | R-AC-07 | Low | Remediate | Move to SHA-256 | PA-61, PA-74 | Remediate |
| NC-SI-11 | SI-7(1) | Checks do not run | G, E | R-AC-07 | Low | Remediate | With PA-61 | PA-61 | Remediate |
| NC-SI-12 | SI-7(7) | Not yet in use | D | R-AC-11 | Low | Approve | In PRO-SI-6 | None | Approve; now satisfied |
| NC-SI-13 | SI-10 | Validation and upload checks tested: injection-style input refused, and wrong signatures, disguised executables, unknown types and paths rejected (H03 to H07) | E | R-AC-02 | Low | Evidence | Test on a throwaway stack | None | None; now satisfied |
| NC-SI-14 | SI-11 | About 29 API responses return the exception message (H01) | G | R-AC-02 | Medium | Remediate | Generic messages, as agreed by the system owner | PA-60 | Remediate |
| NC-SI-15 | SI-12 | \<System Name\>'s retention schedule is set (\<PII Processing Management\>, section 3.7, with placeholders); not yet applied | D | R-AC-11 | Low | Approve | In PRO-SI-7 | PA-70 | Approve |
| NC-SI-16 | SI-16 | .NET managed memory and non-root containers in place; Windows protections not assessable until the VMs exist | E | R-AC-11 | Low | Evidence | Windows Server | PA-54 | Obtain evidence |

### 5.19 Supply Chain Risk Management (SR)

There is one entry for each SR control, as none is yet satisfied. The entries were restated on 12 November 2026 from Test-SupplyChain.ps1 (U01 to U10), after the SR pack review (D-SR-11). The decisions are recorded in \<Decision Register\>.

**Table 24: SR non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-SR-01 | SR-1 | Policy \<ver\> is legally reviewed and awaits the Head of Cyber (D-SR-12); procedures approved; not yet shared | D | R-AC-11 | Low | Approve | No system change is needed | PA-20 | Approve |
| NC-SR-02 | SR-2 | Plan \<ver\> approved, with a supplier register; not yet in use, and not yet in the restricted store | D | R-SR-01 | Low | Approve | \<Supply Chain Risk Management\> \<ver\> | PA-88 | Approve |
| NC-SR-03 | SR-2(1) | The team isn't confirmed by \<Organisation\>, and hasn't met | D | R-SR-01 | Low | Approve | Named in \<Supply Chain Risk Management\> | PA-131 | Approve |
| NC-SR-04 | SR-3 | Only the OfflineModules packages come through the offline feed; the rest (50 of 59 for API) come straight from nuget.org, with no lock files or signed-package trust policy (U01 to U03) | G | R-SR-01 | Medium | Remediate | Route every package through the feed, add lock files and a trust policy | PA-94 | Remediate (proposed by the system owner; awaits the authorising official) |
| NC-SR-05 | SR-5 | Packages are acquired from nuget.org unchecked, and NuGet's audit is off in the build (U01, U04) | G | R-SR-01 | Low | Remediate | With PA-94 and PA-92 | PA-94, PA-92 | Remediate |
| NC-SR-06 | SR-6 | No supplier review has been held with TPL-16 | D | R-SR-01 | Low | Approve | In PRO-SR-2 | PA-131 | Approve |
| NC-SR-07 | SR-8 | \<Organisation\>'s notification terms haven't been seen; open-source suppliers notify through advisories (\<System and Information Integrity Management\>, section 3.3) | E | R-SR-01 | Low | Evidence | Expected from \<Organisation\> | EV-SR-01; PA-131 | Obtain evidence |
| NC-SR-08 | SR-10 | Release images and assemblies match the baseline (U08), but releases have no checksums or bill of materials, and images are not pinned (U06, U07) | G | R-AC-07 | Low | Remediate | With PA-61, PA-77 and PA-78 | PA-61, PA-77, PA-78 | Remediate |
| NC-SR-09 | SR-11 | Software steps approved; no trust policy, and CDN files have no integrity check (U03, U09) | G | R-SR-01 | Low | Remediate | With PA-94 and PA-34 | PA-94, PA-34 | Remediate |
| NC-SR-10 | SR-11(1) | Buyers' training hasn't been seen | E | R-SR-01 | Low | Evidence | Expected from \<Organisation\> | EV-SR-02; PA-131 | Obtain evidence |
| NC-SR-11 | SR-11(2) | Repair process hasn't been seen | E | R-SR-01 | Low | Evidence | Expected from \<Organisation\> | EV-SR-02; PA-131 | Obtain evidence |
| NC-SR-12 | SR-12 | Disposal hasn't been seen | E | R-SR-01 | Low | Evidence | Expected from \<Organisation\> | EV-SR-02; PA-131 | Obtain evidence |
