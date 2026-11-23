# \<System Name\> Awareness and Training Management

## 1 Purpose

This document is the design of \<System Name\>'s security and privacy awareness and training programme. It covers the Awareness and Training (AT) family of the CSS Moderate baseline, 6 controls and enhancements.

Section 3 is the design: who needs what, the awareness briefing, the role curriculum, the training matrix and timetable, keeping content current, the training register and the measures. The programme is planned, written and given, then measured and improved (sections 3.7 and 3.9).

Training is carried out by people, not by the system, so nothing here is built into \<System Name\>.

## 2 Related documents

Which section of this design meets each control, who is responsible for it and its status are in \<System Security Plan\>, section 7.2 (Table 11). The assessment is in \<Control Assessment Record\> (AT), the risks are in \<Risk List\>, and open work is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (AT), and the steps people follow are in \<Procedures\> (AT).

## 3 The training programme

### 3.1 Principles

1. **Trained before access.** Nobody is given access to \<System Name\> until they have completed awareness training, the \<System Name\> briefing and the rules of behaviour.
2. **Every privileged user is trained for the role.** Anyone who is not a standard user completes the modules for their role before the access is given. That includes the system owner, who authorises privileged roles and manages the role groups.
3. **Repeated every 12 months.** All training is repeated yearly, and after a significant incident or change.
4. **Kept current.** Content is reviewed every 12 months, and each lesson from an incident or exercise is added within 30 days.
5. **Checked and recorded.** Every module ends with a check, and every completion is recorded and kept for 3 years.
6. **No blame.** Reporting is thanked, never blamed. No phishing simulation is run without the agreement of HR and the legal adviser, and then nobody is penalised for clicking: reports are counted, not clicks.

Figure 1 shows the path a person follows.

![Figure 1: Training before and after access](figures/atm-figure-1.png)

**Figure 1: Training before and after access**

### 3.2 Who needs what

**Table 1: What each audience needs to know and do**

| Audience | Main risk they can cause or stop | Behaviours needed | Met by |
| --- | --- | --- | --- |
| All users | Disclosing an item to the wrong person; falling for a request that looks genuine | Check who is asking; export only when needed; report anything odd at once | \<Organisation\>'s course; the \<System Name\> briefing |
| Data Owners and the system owner | Granting access no one needs | Authorise least access in ServiceNow; add and remove group members correctly; review access when due | Modules M2, M9, M7; M8 for the system owner |
| Line managers | Approving a request the person does not need; missing the signs of an insider threat in their team | Confirm the need before approving; report movers and leavers within 1 working day, and a concern about misuse at once; raise a concern early | The \<System Name\> briefing, part B7, given on its own before their first approval if they are not \<System Name\> users |
| Administrators | Misusing the power to change which groups open a schema; careless changes to schemas, their groups or settings | Use the administrator role only for administration; change a schema's groups only with its Data Owner's approval in a change record; follow the joiner, mover and leaver steps | Modules M1, M3, M9, M7, M8 |
| Windows server and database administrators | Unpatched or misconfigured servers; lost backups or keys | Follow the patch timetable, hardening and backup steps; protect keys | Modules M4, M3, M9, M7, M8 |
| Developers | Vulnerable code or components; secrets in code | Secure coding; checked components; changes reviewed | Modules M5, M3, M7 |
| Security officer and auditor | Missing an attack or a misuse | The auditor reviews the audit log weekly and reports anything suspicious to the security officer; the security officer reviews alerts and the central logs, does not read the audit log, and leads incident response | Modules M6, M7, M9; M8 for the security officer |
| Business owners | Approving the disposal of items that should be kept, or keeping items too long | Approve disposal only of items due under the retention schedule (\<System Description\>, FR-074) | The \<System Name\> briefing; module M9 |
| Legal adviser's delegate | Searching or disclosing more than a request needs | Search every schema only for the one person named in a request under data protection law (\<System Description\>, FR-073), and handle the results as the legal adviser directs | Module M9 |
| Everyone who handles personal data in \<System Name\> | Using personal data unlawfully; missing or not reporting a breach | Use it only for its purpose; report a breach within 1 hour; pass requests about a person's data to the legal adviser | The \<System Name\> briefing, part B6 |
| Legal adviser | Deciding late or wrongly whether to report a breach to the ICO and the people affected | Know their part in the incident playbooks and the breach steps, and the 72-hour limit | Module M7 |
| Authorising official | Making a risk decision in an incident or recovery without knowing what it rests on | Know when they will be called, the decisions that are theirs, and the information each needs | Module M10 |
| Information owner | Rating information too low, or letting personal data into a schema that should not hold it | Categorise information correctly; decide what personal data each schema holds | The \<System Name\> briefing; module M9 |

### 3.3 Awareness and the \<System Name\> briefing

Awareness has two parts: \<Organisation\>'s general security and privacy course, and the \<System Name\> briefing. \<Organisation\>'s course is expected to cover the general case, including insider threat and social engineering. The system owner gives this 25-minute briefing to every user, whatever their grade, including managers and contractors, before they are given access, together with the signature of \<Security Operating Procedures\>. It ends with a 5-question check, which the person must pass in full; a wrong answer is talked through and asked again.

**Table 2: Briefing outline**

| Part | Content |
| --- | --- |
| B1 What \<System Name\> holds | The items in its schemas, marked \<Classification\>; who may see what; why schemas, their read and edit groups, and roles matter |
| B2 Handling and export | When export is allowed; never forwarding or storing copies outside \<System Name\>; locking the screen |
| B3 Social engineering and social mining | The forms an attempt takes: phishing and targeted phishing, a false story or false identity (pretexting and impersonation), a reply inside a genuine email thread, bait such as a free download or a found USB stick, an offer of help in return for access, a contact through social media, and following someone through a door. Scenario: an email or call asking for an item "for a tribunal" from someone you don't know. Scenario: an emailed sign-in link that looks like \<System Name\>. Social mining: people gather facts about \<Organisation\>, its staff and \<System Name\> from social media, job adverts, out-of-office replies and casual calls, to make a later request convincing. Do not say what \<System Name\> holds, who uses it or how it is reached. Check with the person through a known route, and report it |
| B4 Insider threat | Scenario: a colleague exporting many files before leaving. Signs to notice: long-lasting and strong dissatisfaction with the job; trying to reach information the person does not need for their work; unexplained access to money; bullying or harassment of colleagues; violence at work; and other serious breaches of policy or rules. Seeing a sign is a reason to report through the route in B5, not to accuse. Access is recorded and monitored, as the SyOps explains |
| B5 Reporting | How to report a suspicious message, a mistake or a lost device; reporting is thanked, never blamed |
| B6 Privacy | The privacy training for every user, about 10 minutes. Which schemas hold personal data, and special category data; using it only for the purpose the schema states, and never exporting or copying it outside \<System Name\> without need; recognising a personal data breach, such as an item sent to the wrong person or a lost export, and reporting it to the security officer within 1 hour; passing any request from a person about their data to the legal adviser, without answering it yourself; and where the privacy notice is. The check includes a question on reporting a breach |
| B7 For line managers | Every access request from your people is raised in ServiceNow. Support it only if the person needs it for their work; the schema's Data Owner authorises it. Tell the group's owner at once when someone moves or leaves. The insider threat signs in B4 show first to a manager: raise a concern early with the security officer or HR |

Between courses, awareness is kept up by the system use notice shown at sign-in, \<Organisation\>'s security messages, and a \<System Name\> security note each quarter, written by the security officer from recent advisories and reports.

### 3.4 Role curriculum

Each module ends with a short check of at least 10 questions, with a pass mark of 80%. Anyone below it repeats the module. The security officer writes the content, and Table 3 names who delivers each module. Nobody delivers training to themselves: the Head of Cyber delivers M7 to the security officer, and the security officer gives the system owner the briefing and M8.

**Table 3: Role modules**

| Module | Learning outcomes | Built on | Length | Delivered by |
| --- | --- | --- | --- | --- |
| M1 Privileged access | Use the administrator role only for administration; manage schemas, the read and edit group of each, and system settings safely; recognise misuse | \<Procedures\> (AC); \<Security Operating Procedures\>, Part B | 60 minutes | Security officer |
| M2 Approving access | Authorise least access in the ServiceNow workflow; add and remove members of an Active Directory group correctly; carry out access reviews | \<Procedures\> (AC); \<Access Control Management\>, section 3.13 | 30 minutes | Security officer |
| M3 Configuration and change | Make changes only through change control; keep to the baseline | \<Procedures\> (CM); \<Configuration Management\> | 45 minutes | Security officer |
| M4 Servers and database | Harden, patch to the timetable, scan, back up and protect keys | \<Procedures\> (SI); \<Risk Assessment Management\>, section 3.6; \<Procedures\> (CP); \<System and Communications Protection Management\> | 90 minutes | Security officer |
| M5 Secure development | Secure coding to ASVS 5.0 Level 2; bring components in through the supply chain check, and spot look-alike and counterfeit packages and libraries; keep secrets out of code; review changes | \<System and Services Acquisition Management\>; \<Procedures\> (SA); \<Procedures\> (SR) | 90 minutes | Security officer |
| M6 Monitoring and audit review | Auditors: read and review the audit log weekly, compare it with the server, database, PingFederate and Active Directory records, record the review, and report anything suspicious to the security officer. Security officers: review the alerts and the central logs, and use the detection use cases; they do not read the audit log | \<Audit and Accountability Management\>; \<System and Information Integrity Management\>, section 3.4 | 60 minutes | Head of Cyber |
| M7 Incident response | Recognise, report, contain and record an incident; know your part in the playbooks | \<Incident Response Management\>; \<Procedures\> (IR) | 60 minutes | Security officer |
| M8 Contingency | Know your part in recovery; restore from backup | \<Contingency Planning Management\>; \<Procedures\> (CP) | 45 minutes | System owner |
| M9 Personal data, for the roles in Table 4 | Lawful use of personal data; requests and complaints; breaches | \<PII Processing Management\>; \<Procedures\> (PT) | 45 minutes | Legal adviser |
| M10 Risk decisions in incidents and recovery | For the authorising official: when they are called in an incident or a recovery; the severity levels; the decisions that are theirs (running in a reduced state, going beyond the recovery time objective, the risk arising from an incident); and what each decision needs | \<Incident Response Management\>, sections 3.3 and 3.6; \<Contingency Planning Management\>, sections 3.4 and 3.5 | 20 minutes | Security officer |

### 3.5 Training matrix

Every role with access must complete awareness, the briefing and signing \<Security Operating Procedures\> before access; roles without access take what their row sets. Role modules come before privileged access, or for developers before they first work on the code. M7, M8 and M10, the incident response and contingency training, are taken within 30 days of taking the role. The security officer, the system owner and their deputies take M7 and M8 before taking the role, because they lead the response and the recovery from the first day. All are repeated every 12 months.

**Table 4: Training matrix**

| Role | Awareness and briefing | \<Security Operating Procedures\> | Role modules | Within 30 days |
| --- | --- | --- | --- | --- |
| All users | Yes | Part A | None | None |
| System owner | Yes | Parts A and B | M2, M9 | M7, M8 |
| Data Owner | Yes | Part A | M2, M9 | M7 |
| Administrator | Yes | Parts A and B | M1, M3, M9 | M7, M8 |
| Windows server administrator | Yes | Parts A and B | M4, M3, M9 | M7, M8 |
| Database administrator | Yes | Parts A and B | M4, M3, M9 | M7, M8 |
| Developers | Yes | Part A; Part B only if given access to a live system, which the design does not allow | M5, M3 | M7 |
| Security officer | Yes | Parts A and B | M6, M9 | M7, M8 |
| Auditor | Yes | Parts A and B | M6, M9 | M7 |
| Business owner | Yes | Parts A and B | M9 | None |
| Legal adviser's delegate | Yes | Parts A and B | M9 | None |
| Information owner | Yes | Part A, if they are a \<System Name\> user | M9 | None |
| Legal adviser | \<Organisation\>'s course | None: no access | None (delivers M9) | M7 |
| Authorising official | \<Organisation\>'s course | None: no access | None | M10 |
| Line managers who are not \<System Name\> users | Briefing part B7 only, before their first approval | None: no access | None | None |

**Privacy training.** Every user's privacy training is briefing part B6, given before access and every 12 months. Module M9 is for the roles that make decisions about personal data or can reach it across schemas or outside the application: the system owner, Data Owners, the information owner, administrators, Windows server and database administrators, the security officer, the auditor, the business owner and the legal adviser's delegate.

**Deputies.** A deputy holds the same training as the role they cover (\<Roles and Responsibilities\>, section 5), follows that role's row, and is in the register under it.

**Roles without access.** Role training is for everyone with a security or privacy duty for \<System Name\>, not only those with access to it. The legal adviser, the authorising official, the information owner and line managers are in the matrix for the duties they hold, though most have no access: the legal adviser's part in incident response, the authorising official's risk decisions in an incident or a recovery, the information owner's categorisation, and the line manager's approval of access requests. Four roles stay out of the matrix. Three rely on \<Organisation\>'s own training: the Head of Cyber, who approves the policies, delivers module M6 and reviews the administrators' group; the data protection officer, who leads \<Organisation\>'s privacy programme; and \<Organisation\>'s security contact, who works in its security team. The security assessor is independent of \<System Name\> and is not trained by it; their independence is confirmed on the assessor independence statement.

### 3.6 When training happens

**Table 5: Training timetable**

| When | What | Who checks |
| --- | --- | --- |
| Before any access | \<Organisation\>'s course, the \<System Name\> briefing and its check, and the signature of \<Security Operating Procedures\> | The security officer records it; the group's owner adds no one before it is recorded |
| Before privileged access | The role modules in the matrix, each with its check, and Part B signed | The system owner checks the training register and the register of signatures: before authorising a role group, and before asking \<Organisation\> for a Windows server or database administrator's access |
| Before a developer first works on \<System Name\> code | Modules M5 and M3 | The system owner, before the developer is given access to the code |
| Before a line manager's first approval of an access request | Briefing part B7, if they are not already a \<System Name\> user | Security officer, from ServiceNow's list of approvers |
| Within 30 days of taking a role | Incident response (M7), contingency (M8) and, for the authorising official, risk decisions (M10) | Security officer |
| Every 12 months | All of the above, repeated | Security officer, who asks each person |
| After a significant incident, exercise or change | The updated briefing or module, for those it affects | Security officer |
| More than 30 days overdue | Privileged access is suspended until the training is complete. A standard user is reminded each month and keeps access; that risk is R-AT-01 in \<Risk List\>, accepted by the system owner (D-AT-01) | System owner |

### 3.7 Keeping content current

1. Every 12 months, the security officer reviews the briefing and each module against the curriculum and changes, and reads the incident records and exercise reports of the year, inside and outside \<Organisation\>, adding each lesson to the briefing or module it concerns.
2. After a significant incident, exercise or change, the lesson is added within 30 days.
3. The legal adviser reviews the privacy content.
4. Each change is recorded on the change record, citing the incident record or exercise report the lesson came from, and the content version goes up. Each training record names the version given.

### 3.8 Training register

The security officer keeps this register from the training records. The system owner checks it before authorising a role. Records are kept for 3 years, which holds each person's last three yearly completions. Each record names the person, the role, the training and its content version, the date, the result of the check, who gave it and the next due date. \<Organisation\> keeps its own course records and provides them on request. The layout stays here. Once the records store is set up, the live register, with its names and dates, is kept there.

**Table 6: Training register**

| Person | Role | Awareness and briefing | Role modules | Within 30 days | Next due |
| --- | --- | --- | --- | --- | --- |
| \[Name\] | Administrator | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | Windows server administrator | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | Database administrator | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\], \[Name\], \[Name\] | Developers | \[dates\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | Security officer | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | Auditor | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | System owner | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | Data Owner | \[date\] | \[dates\] | \[dates\] | \[date\] |
| \[Name\] | Business owner | \[date\] | \[dates\] | None | \[date\] |
| \[Name\] | Legal adviser's delegate | \[date\] | \[dates\] | None | \[date\] |
| \[Name\] | Information owner | \[date\] | \[dates\] | None | \[date\] |
| \[Name\] | Legal adviser | \[date\] | None | \[dates\] | \[date\] |
| \[Name\] | Authorising official | \[date\] | None | \[dates\] | \[date\] |
| \[Names\] | Line managers | \[dates\] | None | None | \[date\] |
| \[Name\] | Deputies, each under the role they cover | \[date\] | \[dates\] | \[dates\] | \[date\] |

### 3.9 Measures

The security officer reports these monthly with the continuous monitoring measures on the monitoring and integrity report, and the system owner reviews them (\<Policy\>, section AT.6). Anyone overdue is reminded, and privileged access is suspended after 30 days overdue (Table 5).

**Table 7: Training measures**

| Measure | Target |
| --- | --- |
| People trained before access | 100% |
| First-attempt pass rate on checks | 90% |
| People overdue for a refresher | 0 |
| Suspicious messages reported each month | Rising; reports, not clicks, are counted |
| Content reviewed within 12 months and after each significant incident | 100% |

### 3.10 Policy and procedures

\<Policy\> (AT) and \<Procedures\> (AT) are the policy and procedures for this family. Who they are shared with is in \<Policy\>, section AT.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.

