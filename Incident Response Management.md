# \<System Name\> Incident Response Management

## 1 Purpose

This document shows how security incidents affecting \<System Name\> are prepared for, found, handled and learned from, for each of the 13 Incident Response (IR) controls and enhancements in the CSS Moderate baseline. Section 3 is the incident response plan that IR-8 requires: who does what, how incidents are found, how severe each is and how fast it must be contained, the steps every incident follows, personal data breaches, the playbooks, evidence, and the register. It can be used on its own during an incident. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define, and appendix B holds the contacts. Appendix C lists the IR controls CSS does not select at Moderate.

This is the only place the incident response design is held. Other documents point here. The policy is in \<Policy\> (IR), and the steps people follow are in \<Procedures\> (IR).

An assessor examines the plan, the incident records, the training and exercise records, and the reports made; interviews the incident lead and a sample of users; and may ask to be walked through a past incident or a playbook (CSS). So for each control section 4 gives:

- **each part of the control**, as CSS letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

\<System Name\> has had no operational incident, as it is not in use. One incident is on the register: secrets found in the history of the source repositories, by review (INC-2026-001).

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded once, in \<System Security Plan\>, section 7.8 (Table 17). This section gives only the overall position.

No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

Two IR controls from the privacy baseline are assessed with the PT family, and rest on this plan: breach training, IR-2(3) (NC-PT-10; PA-81, PA-97), and the breach steps of the plan, IR-8(1), which section 3.8 meets.

The plan is written and has been tried once, as a drill in the test environment. What remains is to train the people, hold an exercise, set up ServiceNow for incidents, and agree \<Organisation\>'s part.

## 3 The incident response plan

### 3.1 Principles

1. **Report early.** A suspected incident is reported straight away, and within 1 hour.
2. **Preserve evidence.** Contain the harm, and do not clean up first.
3. **One plan.** Everyone follows the same steps, so handling is consistent.
4. **Tell those who must know.** The legal adviser at once when personal data may be involved; \<Organisation\> and any supplier concerned.
5. **Learn.** Each incident improves the plan, the training and the controls.

These carry out the principles and rules of \<Policy\>, sections IR.3 and IR.4.

### 3.2 Scope

The plan follows CSS, which treats incident response as part of managing cyber risk across the six CSF 2.0 functions: preparation (Govern, Identify, Protect), detection (Detect), and handling and recovery (Respond, Recover). It meets the needs of a Moderate system holding Restricted documents, and HR documents with personal data.

It covers UI application, Admin application, API, the \<System Name\> database, its backups and secrets, and the two VMs at \<Organisation\>. Incidents in \<Organisation\>'s own services, including AD FS and Active Directory, are handled by \<Organisation\>, with this plan for \<System Name\>'s part.

![Figure 1: The steps every incident follows](figures/irm-figure-1.png)

**Figure 1: The steps every incident follows**

### 3.3 How the response is organised

**Table 2: Incident response roles**

| Role | Holder | Deputy | Part in a response |
| --- | --- | --- | --- |
| Incident lead | \[Name\], security officer | \[Name\] | Leads the response, sets the severity, keeps the record, and tells others |
| Decision maker | \[Name\], system owner | \[Name\] | Decides on stopping the service, recovery and outside reporting of crime |
| Risk decision | \[Name\], authorising official | None | Decides on the risk arising from the incident |
| Technical response | \[Name\], \[Name\], and the developers | Each other | Contain, eradicate, recover and preserve evidence |
| Legal | \[Name\] | \[Deputy to be named\] | Decides whether to tell the ICO and the people affected, and makes the reports |
| Support | \[Name\], \<Organisation\>'s security contact | \[Name\] | \<Organisation\>'s monitoring, network and forensic help |

Contact details are in appendix B.

The targets in section 3.6 for Critical and High incidents run in clock hours, so someone must be reachable outside working hours. The system owner decided on 17 November 2026 to keep the targets and to agree a route with \<Organisation\> (D-IR-12). That cover is not yet arranged: \[out of hours route to be agreed with \<Organisation\>\] (PA-118).

### 3.4 Preparation

Preparation covers the CSF 2.0 Govern, Identify and Protect functions as they apply to incidents.

1. **People:** each role holder is trained within 30 days of taking the role and every 12 months (PRO-IR-3). The training covers this plan, the severity levels, the playbooks in section 3.9, preserving evidence, the breach steps in section 3.8, and the contacts.
2. **Exercises:** a tabletop exercise every 12 months, with the contingency plan, the first within 30 days of the VMs being built and before production (PA-81). Each ends with an after-action report on TPL-11.
3. **Assets and baseline:** the components and baseline in \<Configuration Management\>, sections 3.4 and 3.5, show what normal looks like.
4. **Tools:** ServiceNow for incident records (PA-65; TPL-10 until then); the audit records and logs in section 3.10.
5. **Contacts:** appendix B, checked at each review and exercise.
6. **Copies:** each role holder keeps a copy of this plan and the contacts that can still be read if the document store, ServiceNow or email is out of use, such as a printed copy (PA-119).

### 3.5 Detection sources

**Table 3: How incidents are found**

| Source | What it shows | Who watches | State |
| --- | --- | --- | --- |
| User and staff reports | Anything that looks wrong (section 3.11) | Security officer | Ready |
| Weekly audit log review (\<Procedures\> (AU)) | Refused access, changes to access, large exports; failed sign-ins and lockouts from \<Organisation\>'s AD FS record | The auditor, who reports to the security officer | Manual; audit chain check not yet reliable (PA-74) |
| Alerts | Repeated failed sign-ins, audit chain breaks, Defender detections | Security officer | Not built (PA-59) |
| Microsoft Defender on both VMs | Malicious code | Windows server administrator | VMs not built |
| Backup and integrity checks (SyOps C8, C12) | Failed backups, changed documents or release packages | Database and Windows server administrators | Not built (PA-64) |
| \<Organisation\>'s monitoring | Network and directory events | \<Organisation\>'s security contact | Unconfirmed (EV-IR-01) |
| Supplier and NCSC advisories | Vulnerabilities in components \<System Name\> uses | Security officer | Manual |

### 3.6 Severity and targets

The incident lead sets the severity when the incident is confirmed, and may raise or lower it as facts emerge.

**Table 4: Severity**

| Severity | Examples | Work starts within | Contained within | Who is told |
| --- | --- | --- | --- | --- |
| Critical | Personal data breach likely to harm people; ransomware; a privileged account compromised | 1 hour | 4 hours | System owner, authorising official, legal adviser, \<Organisation\>'s security contact |
| High | A user account compromised; a secret exposed; access to documents someone should not see | 4 hours | 1 working day | System owner, \<Organisation\>'s security contact; legal adviser if personal data is involved |
| Medium | Malware stopped by Defender; repeated failed sign-ins; a supplier advisory affecting \<System Name\> | 1 working day | 5 working days | System owner |
| Low | A single policy breach with no data exposed | 5 working days | As planned | Recorded only |

The containment targets were agreed by the system owner on 10 November 2026 (D-IR-06).

### 3.7 Handling an incident

Every incident follows these steps, so that handling is consistent. Greater severity means more people and faster targets, not a different process.

1. **Detect and analyse:** the incident lead confirms whether a report is an incident, sets its severity, and opens a record on TPL-10.
2. **Contain:** limit the harm, for example by ending sessions, disabling an account, or isolating a VM. Preserve evidence first (section 3.10).
3. **Eradicate:** remove the cause, for example by fixing a flaw or changing secrets.
4. **Recover:** restore normal service, invoking \<Contingency Planning Management\> if needed. The incident plan leads while the outage may be an incident (\<Contingency Planning Management\>, section 3.6.2).
5. **Close and learn:** within 10 working days, record the root cause and lessons, and update this plan, \<Risk List\> and \<Plan of Action and Milestones\> (PRO-IR-7).

### 3.8 Personal data breaches

A personal data breach is any security incident that leads to the accidental or unlawful loss, change, disclosure of, or access to personal data.

1. **Tell the legal adviser at once.** The security officer tells the legal adviser as soon as personal data may be involved.
2. **72 hours from becoming aware.** If the breach is likely to put people's rights and freedoms at risk, the legal adviser tells the ICO within 72 hours of the organisation becoming aware of it, even if not all details are known. A later report gives the reasons for the delay.
3. **Assess and reduce the harm.** The legal adviser and the security officer judge how the breach could harm the people concerned, such as distress, discrimination, fraud or the loss of confidentiality, and what would reduce it: getting copies back or deleted, changing access, and telling people what to watch for.
4. **Tell the people affected** without undue delay when the risk to them is high, unless the data was protected, for example by encryption, so that it cannot be read.
5. **Record every breach** in the register in section 3.14, whether or not it is reported: the facts, the effects, the action taken, and, if not reported, why.
6. **What the ICO report holds:** what happened, the kinds and rough numbers of people and records, the likely effects, what is being done, and the contact details of the data protection officer, or of the legal adviser if no officer is required (UK GDPR, Article 33(3)(b); D-PM-04).

### 3.9 Playbooks

**Table 5: Playbooks**

| Incident | Contain | Eradicate and recover | Usual severity |
| --- | --- | --- | --- |
| Stolen or guessed password | End the user's sessions (D01); ask \<Organisation\>'s service desk to disable the Active Directory account; check the audit records for what was read or exported | \<Organisation\>'s service desk resets the password and second factor under PRO-IA-3; access returns once identity is checked | High; Critical for a global administrator |
| Exposed secret (signing key, database password) | Change the secret; changing the signing key ends every session | Find where it was exposed and remove it; check the audit records for misuse since | High |
| Compromise of AD FS or of Active Directory accounts, reported by \<Organisation\> | End the sessions of every person affected, or of everyone if \<Organisation\> cannot say who; ask \<Organisation\> which accounts and groups were touched | Check the audit records for what those accounts did; check the members of \<System Name\>'s groups against the approved requests; let people back in once \<Organisation\> confirms the accounts are safe | High; Critical for a privileged account. Adopted by the system owner on 17 November 2026 (D-IR-11) |
| Ransomware or destructive attack on a VM | Isolate the VM through \<Organisation\>; do not power off before evidence is taken | Rebuild and restore from a backup taken before the compromise (\<Contingency Planning Management\>, section 3.6.2); change every secret | Critical |
| Bulk export or download misuse | End the user's sessions; the group's owner removes the person from the project's AD group, or \<Organisation\>'s service desk disables the account | Work out what left, with the export audit records; treat as a personal data breach if HR documents were included | High; Critical if personal data |
| Audit record tampering | Export the audit records with a hash before anything changes (D07); restrict database access | Compare with the last exported copy and backups; fix the cause (PA-73, PA-74) | High |
| Malicious file uploaded | Remove access to the document; stop further uploads if needed | Scan, remove, and check who opened it (PA-58) | Medium; High if opened |
| Document in the wrong place: filed in the wrong project, or sent or shown to the wrong person | Remove access to the document; find who viewed or exported it, from the audit records | Ask anyone who received a copy to delete it and confirm; file the document correctly; treat it as a personal data breach if it holds personal data (section 3.8) | Medium; High if the document is Restricted or holds personal data. Adopted by the system owner on 17 November 2026 (D-IR-12) |
| Lost or stolen laptop, phone or printout | \<Organisation\> locks or wipes the device; end the user's sessions (D01); for a printout, find out which documents it held | Confirm the device was encrypted; check the audit records for what the user viewed or exported; treat personal data as a possible breach (section 3.8) | Medium; High if unencrypted or holding personal data |
| Physical intrusion, fire, flood or power loss at a data centre | \<Organisation\> secures the site and tells the security officer (\<Procedures\>, PRO-PE-2); take evidence before anything is moved | Invoke the contingency plan if the site is lost (\<Contingency Planning Management\>); after an intrusion, check the VMs and disks for tampering, and change secrets | High |

### 3.10 Evidence and forensic readiness

**Table 6: Evidence sources**

| Source | Where it is kept | Kept for | Notes |
| --- | --- | --- | --- |
| Audit records | The \<System Name\> database, table dbo.AuditLog | 12 months online and 12 months archived (\<Audit and Accountability Management\>) | Times stored in UTC (D05). The chain cannot yet be checked (PA-74) |
| Application logs | Each application's log on the application VM | 30 days (\<Audit and Accountability Management\>, section 3.10) | Repeat audit details with personal data until PA-75 is fixed (D08) |
| Windows and PostgreSQL logs | The VMs, and \<Organisation\>'s central service if agreed (EV-AU-01) | As \<Organisation\> sets; 12 months is expected (\<Audit and Accountability Management\>, section 3.7) | Not built (PA-43) |
| AD FS and Active Directory records | \<Organisation\> | As \<Organisation\> sets (EV-AU-05) | Sign-in attempts and changes to group members. No route to them is agreed yet (PA-101) |
| Backups | The second site (\<Contingency Planning Management\>, section 3.8) | 14 daily, 8 weekly, 12 monthly | A snapshot of the state before an incident |

1. **Before changing anything,** export the evidence and record its SHA-256 hash, as in D07, and note it on TPL-10 with who took it and when.
2. **Time:** all times are UTC. Check each system's clock against a trusted source before building a timeline; the Docker test stack drifted 187 seconds (D06), and the VMs take time from \<Organisation\> (EV-AU-02).
3. **Custody:** each piece of evidence is listed on TPL-10 with who holds it, where, and each hand-over.
4. **Personal data in evidence** is handled as Restricted and kept only as long as the incident needs.

### 3.11 Reportable incidents

An event is anything seen in \<System Name\> or reported about it. It becomes an incident when the incident lead confirms that it harms, or may harm, the confidentiality, integrity or availability of \<System Name\> or its information, or breaks a security rule. People report what they suspect; they do not wait to be sure.

These must be reported: suspected account misuse; access to documents by someone who should not have it; an exposed password or secret; malicious code; an attack on the system; loss or unexpected change of documents or audit records; and a failure of logging or backups. Anything else that looks wrong should be reported too.

### 3.12 Measures and resources

**Table 7: Measures**

| Measure | Target |
| --- | --- |
| Time from noticing to reporting | Within 1 hour |
| Time from reporting to containment | As section 3.6 for the severity |
| Time to recover | Within the contingency plan's recovery time objective of 72 hours |
| Incidents closed with lessons recorded within 10 working days | All |
| Repeat incidents with the same root cause | None |

The measures are reported monthly under \<Procedures\>, PRO-CA-5. The resources are the people in section 3.3, ServiceNow (PA-65), and the evidence sources in section 3.10. No budget is set aside for outside forensic help; \<Organisation\>'s security contact is the first route \[to be confirmed, EV-IR-01\]. One decision is still to be made: \[whether an outside forensic firm is kept on call\]. Until it is, the plan relies on \<Organisation\> alone, and that reliance is recorded as a gap (PA-118).

### 3.13 Sharing information

Information is shared with \<Organisation\>'s security contact, any affected supplier, and the ICO and the people affected through the legal adviser. Crime or a significant cyber attack is reported by the system owner to the NCSC or to Report Fraud, the national police reporting service that replaced Action Fraud in December 2025. Anything else goes through the system owner. Only \[\<Organisation\> communications contact\] speaks to the press or the public about an incident, with the system owner's agreement. If ServiceNow or email may be compromised, use the phone numbers in appendix B. This document is Restricted, and moves to the restricted document store with the other records (D-GEN-15).

### 3.14 Incident and breach register

Until ServiceNow is set up, incidents and personal data breaches are listed here, each with its TPL-10 record.

**Table 8: Incident and breach register**

| Reference | Opened | Summary | Severity | Personal data breach | Status |
| --- | --- | --- | --- | --- | --- |
| INC-2026-001 | 10 November 2026 | The database password, JWT signing key and an old AD FS secret are committed in git history (PA-19). Found by review, not by misuse. No production data is held, and the database is not reachable from outside the host | Medium (D-IR-09) | No: no personal data exposed | Open until every secret is replaced on the VMs (PA-19) and \<Organisation\> confirms the AD FS secret is revoked \[date of \<Organisation\>'s confirmation\], asked for with EV-IR-01 |

### 3.15 What \<Organisation\> provides

**Table 9: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| Its own incident process, and a route for \<System Name\>'s reports | IR-6, IR-6(3) | The security contact takes a report at any time, and tells \<System Name\>'s security officer of a compromise on its side within 24 hours | EV-IR-01, EV-SR-01 | Not sent |
| Help during an incident | IR-7, IR-4 | Monitoring, network and forensic help; isolating a server; disabling an account; locking or wiping a device | EV-IR-01 | Not sent |
| ServiceNow, for incident records and reports | IR-4(1), IR-6(1), IR-7(1) | A workflow built to \<System Name\>'s design | None: tracked by PA-65 | Not built |
| Its monitoring of the network, AD FS and Active Directory | IR-4 | Events that show an attack on \<System Name\> reach the security officer | EV-AU-01, EV-AU-05 | Not sent |

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 IR-1 Policy and Procedures

**Table 10: IR-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | An incident response policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (IR): a system-level policy, shared with everyone who administers \<System Name\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-IR-01) and legally reviewed on 10 November 2026. The later version awaits the Head of Cyber (D-IR-07). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (IR): seven procedures, PRO-IR-1 to PRO-IR-7. Shared with the same people | Approved by the system owner (D-IR-08). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 10 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 11: IR-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy (\<Policy\>, section IR.4); all seven procedures (\<Procedures\> (IR)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals of version \<ver\> exist |
| Status | Partially implemented |
| Risk decision | NC-IR-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-IR-07) |

### 4.2 IR-2 Incident Response Training

**Table 12: IR-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | Train people in their incident role within a defined time of taking it | Within 30 days. It covers this plan, the severity levels, the playbooks, preserving evidence, the breach steps and the contacts (section 3.4). It is module M7 of the role curriculum (\<Awareness and Training Management\>, section 3.4) | No training has been given (PA-81) |
| a.2 | Train them again when the system changes | After a change to the plan that alters a person's part, that person is briefed on it | Not yet used |
| a.3 | Train them again on a schedule | Every 12 months | Not yet due |
| b | Review and update the training content on a schedule and after defined events | Every 12 months, and after a plan change or an incident | The content is outlined in section 3.4. The module itself is not written (PA-97) |

**Table 13: IR-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function. The training register shows who is trained (\<Awareness and Training Management\>, section 3.8) |
| Rules and procedures | Policy rule R7 (\<Policy\>, section IR.4); PRO-IR-3 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The training content; completion records on TPL-9 for each role holder. None exist yet |
| Status | Not implemented |
| Risk decision | NC-IR-02, rated Low: approve |
| Open items | PA-81: train the role holders. PA-97: write module M7 |

### 4.3 IR-3 Incident Response Testing

**Table 14: IR-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Test the incident response capability on a schedule, with defined tests | A tabletop exercise every 12 months, the first within 30 days of the servers being built and before production. Each walks through one playbook from report to closing, and ends with an after-action report on TPL-11 | No exercise has been held (PA-81). The containment and evidence steps were tried in the test environment on 10 November 2026 (D01 to D08) |

**Table 15: IR-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R8 (\<Policy\>, section IR.4); PRO-IR-3 (\<Procedures\> (IR)) |
| Tests | Checks D01 to D08 on the v1.0 build, 10 November 2026. A suspect user's sessions were ended and a disabled account was locked out at once (D01, D03), and audit records were exported with a repeatable hash (D07). Gaps: ending sessions is not audited (D02; PA-14), and the application log repeats personal data (D08; PA-75) |
| Records an assessor will ask for | Exercise plans and after-action reports on TPL-11. One drill record exists, from the test environment |
| Status | Not implemented |
| Risk decision | NC-IR-03, rated Low: approve |
| Open items | PA-81: hold the first tabletop exercise |

### 4.4 IR-3(2) Coordination with Related Plans

**Table 16: IR-3(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Test the capability together with those responsible for related plans | The tabletop exercise is held with the contingency plan (\<Contingency Planning Management\>, section 3.10), and \<Organisation\>'s security contact and IT service desk take part | Not held (PA-81) |

**Table 17: IR-3(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer, system owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R8 (\<Policy\>, section IR.4); PRO-IR-3 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The exercise report naming who took part |
| Status | Not implemented |
| Risk decision | NC-IR-04, rated Low: approve |
| Open items | PA-81 |

### 4.5 IR-4 Incident Handling

**Table 18: IR-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Handle incidents in line with the plan: preparation, detection and analysis, containment, eradication and recovery | Section 3.4 is preparation, section 3.5 detection, and section 3.7 the five steps every incident follows. The playbooks in section 3.9 give the first actions for ten kinds of incident, and section 3.6 the time allowed | Written. Not in use, as \<System Name\> is not in use. One incident is on the register, INC-2026-001 |
| b | Coordinate incident handling with contingency planning | An outage that may be an incident is led by this plan, with the contingency plan in support; recovery uses a backup taken before the compromise (\<Contingency Planning Management\>, section 3.6.2) | Written into both plans. Not exercised (PA-81) |
| c | Build lessons from incidents into the procedures, training and testing, and make the changes | Within 10 working days of containment the incident lead records the root cause and lessons, and updates this document, the training, the Risk List and the POA&M (PRO-IR-7) | Not yet used |
| d | Make the rigour, intensity, scope and results of handling comparable and predictable | Every incident follows the same five steps, the same severity table and the same record, TPL-10. Greater severity means more people and faster targets, not a different process | Written |

**Table 19: IR-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function. The administration pages let a global administrator end sessions at once; \<Organisation\> disables accounts and isolates servers |
| Rules and procedures | Policy rules R2, R6 (\<Policy\>, section IR.4); PRO-IR-2, PRO-IR-6, PRO-IR-7 (\<Procedures\> (IR)) |
| Tests | Checks D01 to D07, as IR-3 |
| Records an assessor will ask for | Incident records on TPL-10, each with its timeline, evidence and lessons; the register. The register and one record exist |
| Status | Partially implemented |
| Risk decision | NC-IR-05, rated Low: approve |
| Open items | PA-118: bring handling into use, with \<Organisation\>'s part agreed. PA-14: audit the ending of sessions |

### 4.6 IR-4(1) Automated Incident Handling Processes

**Table 20: IR-4(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Support incident handling with defined automated means | ServiceNow, once set up for incidents (D-IR-05): it holds each incident's record, timeline, actions and evidence list, and reminds the owner of each action. Until then the record is form TPL-10, kept by hand | Not set up (PA-65) |

**Table 21: IR-4(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Security officer, \<Organisation\> |
| Enforced by | ServiceNow |
| Rules and procedures | Policy rule R5 (\<Policy\>, section IR.4); PRO-IR-2 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The ServiceNow incident workflow; a sample record |
| Status | Not implemented |
| Risk decision | NC-IR-06, rated Low: remediate |
| Open items | PA-65: set up ServiceNow for incidents |

### 4.7 IR-5 Incident Monitoring

**Table 22: IR-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Track and document incidents | Every incident and personal data breach is on the register in section 3.14, each with its TPL-10 record: what happened, the severity, the timeline, the evidence, the actions and the lessons. The measures in section 3.12 are reported each month | The register exists, with INC-2026-001. Tracking is not otherwise in use (PA-118) |

**Table 23: IR-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R5 (\<Policy\>, section IR.4); PRO-IR-2 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The register; each TPL-10 record; the monthly measures |
| Status | Not implemented |
| Risk decision | NC-IR-07, rated Low: approve |
| Open items | PA-118. PA-65: ServiceNow |

### 4.8 IR-6 Incident Reporting

**Table 24: IR-6 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Require people to report suspected incidents to the incident response capability within a defined time | Everyone reports a suspected incident to the security officer within 1 hour. Section 3.11 says what must be reported, and the rules of behaviour repeat it (\<Security Operating Procedures\>, Part A). If ServiceNow or email may be compromised, the phone numbers in appendix B are used | Written. The rules are not yet signed, and the contacts are placeholders |
| b | Report incident information to defined authorities | The security officer tells \<Organisation\>'s security contact. The legal adviser tells the ICO within 72 hours of becoming aware of a reportable personal data breach, and the people affected when the risk to them is high (section 3.8). The system owner reports a crime or a significant cyber attack to the NCSC or to Report Fraud, which replaced Action Fraud | Not yet used. \<Organisation\>'s route for reports is not confirmed (EV-IR-01) |

**Table 25: IR-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Everyone, security officer, legal adviser |
| Enforced by | Not a system function |
| Rules and procedures | Policy rules R1, R4, R10 (\<Policy\>, section IR.4); PRO-IR-1, PRO-IR-5 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | Incident records showing when each report was made, and to whom; any ICO report |
| Status | Partially implemented |
| Risk decision | NC-IR-08, rated Low: approve |
| Open items | PA-118: confirm \<Organisation\>'s route (EV-IR-01) |

### 4.9 IR-6(1) Automated Reporting

**Table 26: IR-6(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Report incidents by defined automated means | ServiceNow, once set up for incidents (D-IR-05): a report raises a ticket, which notifies the security officer. Until then reports are made by phone or email and recorded on form TPL-10 | Not set up (PA-65) |

**Table 27: IR-6(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Security officer, \<Organisation\> |
| Enforced by | ServiceNow |
| Rules and procedures | Policy rule R5 (\<Policy\>, section IR.4); PRO-IR-1 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The ServiceNow report form; a sample ticket |
| Status | Not implemented |
| Risk decision | NC-IR-09, rated Low: remediate |
| Open items | PA-65 |

### 4.10 IR-6(3) Supply Chain Coordination

**Table 28: IR-6(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Give incident information to the provider of the product or service, and to others in the supply chain | The security officer tells \<Organisation\>'s security contact, and any other supplier whose product or service is involved, using the supplier register (\<Supply Chain Risk Management\>, section 3.5). \<Organisation\> in turn reports a compromise on its side to the security officer within 24 hours | Not yet used. \<Organisation\>'s terms are not seen (EV-IR-01, EV-SR-01) |

**Table 29: IR-6(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R3 (\<Policy\>, section IR.4); PRO-IR-1 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | Incident records showing the supplier told; \<Organisation\>'s reports |
| Status | Not implemented |
| Risk decision | NC-IR-10, rated Low: approve |
| Open items | PA-118 |

### 4.11 IR-7 Incident Response Assistance

**Table 30: IR-7 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Provide a support resource, as part of the capability, that gives users advice and help in handling and reporting incidents | The security officer is the first point of help for every user. \<Organisation\>'s security contact gives monitoring, network and forensic help. No outside forensic firm is retained | Not yet used. What \<Organisation\> will provide is not confirmed (EV-IR-01). Help outside working hours is not arranged (PA-118) |

**Table 31: IR-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Security officer, \<Organisation\> |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R3 (\<Policy\>, section IR.4); PRO-IR-4 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The contacts; \<Organisation\>'s description of its help (EV-IR-01) |
| Status | Not implemented |
| Risk decision | NC-IR-11, rated Low: approve |
| Open items | PA-118 |

### 4.12 IR-7(1) Automation Support for Availability of Information and Support

**Table 32: IR-7(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Make incident information and support more available by defined automated means | ServiceNow, once set up for incidents (D-IR-05): users raise a request for help there, and see its progress. Until then users ask the security officer directly | Not set up (PA-65) |

**Table 33: IR-7(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | ServiceNow |
| Rules and procedures | Policy rule R3 (\<Policy\>, section IR.4); PRO-IR-4 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | The ServiceNow request form |
| Status | Not implemented |
| Risk decision | NC-IR-12, rated Low: remediate |
| Open items | PA-65 |

### 4.13 IR-8 Incident Response Plan

**Table 34: IR-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A plan that gives the organisation a roadmap for its incident response capability | Section 3 is the plan. It follows CSS: preparation, detection, handling and recovery, and learning | Written |
| a.2 | It describes the structure and organisation of the capability | Section 3.3: six roles, each with a holder and a deputy | Written. One deputy is still to be named |
| a.3 | It says how the capability fits into the organisation | Section 3.2: \<System Name\>'s team handles \<System Name\>'s part, and \<Organisation\> handles incidents in its own services | Written |
| a.4 | It meets the organisation's own needs: its mission, size, structure and functions | It is written for one Moderate system holding Restricted HR documents, run by a small named team | Written |
| a.5 | It defines reportable incidents | Section 3.11 | Written |
| a.6 | It gives measures of the capability | Section 3.12: five measures, reported monthly | Written. None measured yet |
| a.7 | It defines the resources and management support needed | Section 3.12: the people in section 3.3, ServiceNow, and the evidence sources. No budget is set for outside forensic help | Written |
| a.8 | It says how incident information is shared | Section 3.13 | Written |
| a.9 | It is reviewed and approved by defined people on a schedule | The Head of Cyber, every 12 months and after an incident | Version \<ver\> approved (D-IR-03). The later version awaits the Head of Cyber (D-IR-07) |
| a.10 | It names who is responsible for incident response | The security officer, as incident lead | Named |
| b | Copies go to defined people and parts of the organisation | The security officer, the system owner, the administrators and the authorising official; and \<Organisation\>'s security contact. Each keeps a copy that can be read when the document store is out of use | Not yet shared, and no such copy is held (PA-119) |
| c | The plan is updated for changes to the system and for problems met in use or testing | After each incident and exercise (PRO-IR-7), and when a system change affects it | Updated on 17 November 2026 for sign-in through AD FS |
| d | Changes are told to the same people | With the change record | Not yet shared (PA-119) |
| e | The plan is protected from unauthorised disclosure and change | It is Restricted, and kept in the restricted document store, where only the people in part b can read it and only the security officer can change it | Not yet in the restricted store (PA-88) |

**Table 35: IR-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer, Head of Cyber |
| Enforced by | Not a system function. Version control records every change |
| Rules and procedures | Policy rule R9 (\<Policy\>, section IR.4); PRO-IR-7 (\<Procedures\> (IR)) |
| Tests | None |
| Records an assessor will ask for | This document with its approval; the distribution record; review records |
| Status | Partially implemented |
| Risk decision | NC-IR-13, rated Low: approve |
| Open items | PA-119: obtain the Head of Cyber's approval, fill in the contacts, and share the plan. PA-88: the restricted store |

## Appendix A Parameter register

These are the CSS organisation-defined values for the 13 IR entries: 26 in total. They were agreed on 6 November 2026 (D-IR-P01), and IR-06\_ODP\[02\] was revised on 10 November 2026 (D-IR-P02).

**Table 36: IR parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| IR-01\_ODP\[01\] | Who receives the policy | Everyone who administers \<System Name\> | Not yet shared |
| IR-01\_ODP\[02\] | Who receives the procedures | Everyone who administers \<System Name\> | Not yet shared |
| IR-01\_ODP\[03\] | Level of the policy | System level | Met |
| IR-01\_ODP\[04\] | Official who manages them | System owner | Met |
| IR-01\_ODP\[05\] | Policy review frequency | Every 12 months | Met: reviewed 10 November 2026 |
| IR-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: reviewed after the IR pack review |
| IR-01\_ODP\[07\] | Procedures review frequency | Every 12 months | Met: reviewed 10 November 2026 |
| IR-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: reviewed after the IR pack review |
| IR-02\_ODP\[01\] | Time to train after taking a role | 30 days | Content written (section 3.4); no training yet (PA-81) |
| IR-02\_ODP\[02\] | Training frequency | Every 12 months | No training yet (PA-81) |
| IR-02\_ODP\[03\] | Content review frequency | Every 12 months | Content written 10 November 2026 |
| IR-02\_ODP\[04\] | Events requiring content review | A plan change, or an incident | Content written 10 November 2026 |
| IR-03\_ODP\[01\] | Test frequency | Every 12 months | First tabletop within 30 days of the VMs being built (PA-81) |
| IR-03\_ODP\[02\] | Tests | Tabletop exercise | Containment shown in Docker (D01, D03); no tabletop yet |
| IR-04(01)\_ODP | Automated mechanisms | ServiceNow | Not set up (PA-65) |
| IR-06\_ODP\[01\] | Time to report | Within 1 hour | Not yet in use |
| IR-06\_ODP\[02\] | Authorities | Security officer; \<Organisation\>'s security contact; the ICO within 72 hours of becoming aware of a reportable personal data breach; the people affected without undue delay when the risk to them is high; and the NCSC or Report Fraud, which replaced Action Fraud in December 2025, for a crime or a significant cyber attack (D-IR-P02; the change of name confirmed by D-IR-12) | Not yet in use |
| IR-06(01)\_ODP | Automated mechanisms | ServiceNow | Not set up (PA-65) |
| IR-07(01)\_ODP | Automated mechanisms | ServiceNow | Not set up (PA-65) |
| IR-08\_ODP\[01\] | Who reviews and approves the plan | Head of Cyber | Version \<ver\> pending (D-IR-07) |
| IR-08\_ODP\[02\] | Review frequency | Every 12 months | Met |
| IR-08\_ODP\[03\] | Who is given responsibility for incident response | Security officer | Met (section 3.3) |
| IR-08\_ODP\[04\] | Personnel who receive copies | Security officer, system owner, administrators and authorising official | Not yet shared |
| IR-08\_ODP\[05\] | Elements that receive copies | \<Organisation\>'s security contact | Not yet shared |
| IR-08\_ODP\[06\] | Personnel told of changes | As IR-08\_ODP\[04\] | Not yet shared |
| IR-08\_ODP\[07\] | Elements told of changes | As IR-08\_ODP\[05\] | Not yet shared |

## Appendix B Contacts

Use the phone if ServiceNow or email may be compromised.

**Table 37: Contacts**

| Contact | Name | Phone | Email or route |
| --- | --- | --- | --- |
| Security officer | \[Name\] | \[phone to add\] | \[email to add\] |
| System owner | \[Name\] | \[phone to add\] | \[email to add\] |
| Authorising official | \[Name\] | \[phone to add\] | \[email to add\] |
| Legal adviser | \[Name\] | \[phone to add\] | \[email to add\] |
| Windows server administrator | \[Name\] | \[phone to add\] | \[email to add\] |
| Database administrator | \[Name\] | \[phone to add\] | \[email to add\] |
| \<Organisation\>'s security contact | \[Name\]; deputy \[Name\] | \[phone to add\] | \[email to add\] |
| \<Organisation\>'s IT service desk | \[name to add\] | \[phone to add\] | \[email to add\] |
| Information Commissioner's Office | Breach reporting | \[number to confirm\] | ICO online breach report form |
| National Cyber Security Centre | Incident reporting | \[number to confirm\] | NCSC online incident report |
| Report Fraud, which replaced Action Fraud | Cyber crime and fraud reporting | 0300 123 2040 | Report Fraud online report |

## Appendix C IR controls outside the Moderate baseline

CSS does not select these in the Moderate security baseline, so they are not assessed in this family. Two are in the CSS privacy baseline and apply because \<System Name\> holds personal data: they are assessed with the PT family. Some of the design goes further than the baseline, and Table 38 says where.

**Table 38: IR controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| IR-2(1), IR-2(2) Simulated Events; Automated Training Environments | Training that simulates an incident, in an automated environment | Not required. The tabletop exercise walks through a playbook |
| IR-2(3) Breach | Training on finding, handling and reporting a personal data breach | Privacy baseline, so it applies. Covered by modules M7 and M9, and assessed with the PT family. Not yet given (NC-PT-10; PA-81, PA-97) |
| IR-3(1), IR-3(3) Automated Testing; Continuous Improvement | Automated tests of the capability, and measures used to improve it | Not required. Done in part: the measures in section 3.12 and each after-action report feed the plan |
| IR-4(2), IR-4(3), IR-4(5), IR-4(9) Dynamic Reconfiguration; Continuity of Operations; Automatic Disabling of System; Dynamic Response Capability | The system changes itself, or is shut down, in response to an incident | Not required. Nothing is automatic: people decide, to the targets in section 3.6 |
| IR-4(4) Information Correlation | Incident information correlated across the organisation | Not required. Done in part: the monthly review reads the incident records with the audit findings and the vulnerability results (\<Procedures\>, PRO-CA-5) |
| IR-4(6), IR-4(7) Insider Threats | A capability for incidents caused by insiders, coordinated across the organisation | Not required. Done in part: the playbook for bulk export or download misuse, and \<Organisation\>'s disciplinary process |
| IR-4(8), IR-4(10) Correlation with External Organizations; Supply Chain Coordination | Handling coordinated with outside bodies and suppliers | Not required. Reports to suppliers are covered by IR-6(3) |
| IR-4(11) Integrated Incident Response Team | A team that can be sent out within a set time | Not required. The roles in section 3.3 are a small named team |
| IR-4(12), IR-4(13) Malicious Code and Forensic Analysis; Behavior Analysis | Analysis of malicious code and of attackers' behaviour | Not required. Any such work would be done by \<Organisation\> or an outside firm (section 3.12) |
| IR-4(14) Security Operations Center | A security operations centre | Not required. \<Organisation\> is asked what monitoring it provides (EV-IR-01) |
| IR-4(15) Public Relations and Reputation Repair | Managing public relations after an incident | Not required. Section 3.13 says who may speak to the press and the public |
| IR-5(1) Automated Tracking, Data Collection, and Analysis | Incidents tracked and analysed automatically | Not required. ServiceNow would give part of it (PA-65) |
| IR-6(2) Vulnerabilities Related to Incidents | Weaknesses found through incidents are reported | Not required. Done in design: closing an incident updates the Risk List and the POA&M (PRO-IR-7) |
| IR-7(2) Coordination with External Providers | A working relationship with outside providers of protection | Not required. \<Organisation\> is the only provider (section 3.15) |
| IR-8(1) Breaches | The plan covers personal data breaches: whether to notify, the harm to people, and the law that applies | Privacy baseline, so it applies. Met by section 3.8, and assessed with the PT family as satisfied (NC-PT-11) |
| IR-9, IR-9(2), IR-9(3), IR-9(4) Information Spillage Response | Handling information that reaches a system or person not cleared for it | Not required. Done in part: the playbook for a document in the wrong place (section 3.9) |
| IR-9(1), IR-10 | Withdrawn by CSS | Not applicable |
