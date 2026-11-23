# \<System Name\> Incident Response Management

## 1 Purpose

This document is \<System Name\>'s incident response plan: the design for how it prepares for, finds, handles and learns from security incidents. It covers the Incident Response (IR) family of the CSS Moderate baseline, 13 controls and enhancements, and IR-2(3) and IR-8(1) from the privacy baseline.

Section 3 is the plan: the scope, who does what, preparation, how incidents are found, how severe each is and how fast it must be contained, the steps every incident follows, personal data breaches, the playbooks, evidence, reportable incidents, measures and resources, sharing information, the register, what \<Organisation\> provides, and how the plan is kept. It can be used on its own during an incident. Appendix A holds the contacts.

## 2 Related documents

Which section of this design meets each control, who is responsible for it and its status are in \<System Security Plan\>, section 7.8 (Table 17). The assessment is in \<Control Assessment Record\> (IR), the risks are in \<Risk List\>, and open work is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (IR), and the steps people follow are in \<Procedures\> (IR).

## 3 The incident response plan

### 3.1 Principles

1. **Report early.** A suspected incident is reported straight away, and within 1 hour.
2. **Preserve evidence.** Contain the harm, and do not clean up first.
3. **One plan.** Everyone follows the same steps, so handling is consistent.
4. **Tell those who must know.** The legal adviser at once when personal data may be involved; \<Organisation\> and any supplier concerned.
5. **Learn.** Each incident improves the plan, the training and the controls.

These carry out the principles and rules of \<Policy\>, sections IR.3 and IR.4.

### 3.2 Scope

The plan covers preparation, detection, and handling and recovery. It is sized for a Moderate system holding items that include personal data (\<System Description\>, section 3.4), run by a small named team.

It covers the UI application, the Admin application, the API, the \<System Name\> SQL Server database, its backups and secrets, and the two Windows Server 2025 virtual servers at \<Organisation\>. Incidents in \<Organisation\>'s own services, including PingFederate and Active Directory, are handled by \<Organisation\>, with this plan for \<System Name\>'s part.

![Figure 1: The steps every incident follows](figures/irm-figure-1.png)

**Figure 1: The steps every incident follows**

### 3.3 How the response is organised

**Table 1: Incident response roles**

| Role | Holder | Deputy | Part in a response |
| --- | --- | --- | --- |
| Incident lead | \[Name\], security officer | \[Name\] | Leads the response, sets the severity, keeps the record, and tells others |
| Decision maker | \[Name\], system owner | \[Name\] | Decides on stopping the service, recovery and outside reporting of crime |
| Risk decision | \[Name\], authorising official | None | Decides on the risk arising from the incident |
| Technical response | \[Name\], \[Name\], and the developers | Each other | Contain, eradicate, recover and preserve evidence |
| Audit records | \[Name\], auditor | \[Name\], auditor | Searches and exports the audit records the response needs, with a hash, and tells the incident lead what they show. The auditor is the only role that reads the audit log |
| Legal | \[Name\] | \[Deputy to be named\] | Decides whether to tell the ICO and the people affected, and makes the reports |
| Support | \[Name\], \<Organisation\>'s security contact | \[Name\] | \<Organisation\>'s monitoring, network and forensic help |

Contact details are in appendix A.

The security officer, as incident lead, is responsible for incident response, and is the first point of help for every user, giving advice on handling and reporting an incident. \<Organisation\>'s security contact gives monitoring, network and forensic help (section 3.15).

The targets in section 3.6 for Critical and High incidents run in clock hours, so someone must be reachable outside working hours. \<Organisation\> provides that out of hours route: \[out of hours route\].

### 3.4 Preparation

1. **People:** every user learns their part, which is to recognise and report an incident and a personal data breach within 1 hour, in the \<System Name\> briefing, parts B5 and B6, before access and every 12 months (\<Awareness and Training Management\>, section 3.3). Each role holder in section 3.3, and each other role the training matrix gives it, takes module M7 within 30 days of taking the role, and the security officer, the system owner and their deputies before taking it, and every 12 months. M7 covers this plan, the severity levels, the playbooks in section 3.9, preserving evidence, the breach steps in section 3.8, and the contacts. It is module M7 of the role curriculum (\<Awareness and Training Management\>, sections 3.4 and 3.5), and the training register shows who is trained (\<Awareness and Training Management\>, section 3.8). The authorising official takes module M10, on the risk decisions that are theirs, instead of M7, and \<Organisation\>'s security contact is trained by \<Organisation\>. After a change to the plan, or a system change or significant incident that alters a person's part, that person takes the updated module within 30 days. The training content is reviewed every 12 months, and after a plan change or a significant incident.
2. **Exercises:** a tabletop exercise every 12 months, held with the contingency plan (\<Contingency Planning Management\>, section 3.10), the first within 30 days of the servers being built and before production. \<Organisation\>'s security contact and IT service desk take part. Each exercise walks through one playbook from report to closing, and ends with an after-action report on the exercise and restore test record.
3. **Assets and baseline:** the components and baseline in \<Configuration Management\>, sections 3.4 and 3.5, show what normal looks like.
4. **Tools:** ServiceNow, and the audit records and logs in section 3.10. ServiceNow holds each incident's record, timeline, actions and evidence list, and reminds the owner of each action. A report raises a ticket there, which notifies the security officer. Users raise a request for help there, and see its progress. If ServiceNow is out of use, reports are made by phone or email, users ask the security officer directly for help, and the record is an incident record, kept by hand.
5. **Contacts:** appendix A, checked at each review and exercise.
6. **Copies:** each role holder keeps a copy of this plan and the contacts that can still be read if the document store, ServiceNow or email is out of use, such as a printed copy.

### 3.5 Detection sources

**Table 2: How incidents are found**

| Source | What it shows | Who watches |
| --- | --- | --- |
| User and staff reports | Anything that looks wrong (section 3.11) | Security officer |
| Weekly audit log review (\<Procedures\> (AU)) | Refused access, changes to schemas and their groups, large exports; failed sign-ins and lockouts from \<Organisation\>'s PingFederate and Active Directory records; SQL Server Audit's record of any read of the item tables by a login other than the API's; the daily copies of the newest audit chain hash | The auditor, who reports anything suspicious to the security officer. The security officer does not read the audit log |
| Alerts | The nine alert events, detection use cases U1 to U9 (\<System and Information Integrity Management\>, section 3.4): repeated failed sign-ins; a break in the audit chain; malware detected; a person added to one of the five role groups or to a server's administrators; a bulk export above a set size; an administrator sign-in out of hours; an audit logging failure; an unexpected change to the software or a stored file; and a change to which groups open a schema | Security officer; the auditor also receives a break in the audit chain, and the Windows server administrator malware, a logging failure and an unexpected change |
| Microsoft Defender on both servers | Malicious code | Windows server administrator |
| Backup and integrity checks (\<Security Operating Procedures\>) | Failed backups; a changed stored file, installed release file or release script; malware found by the monthly rescan of stored files | Database and Windows server administrators |
| \<Organisation\>'s monitoring | Network and directory events; unauthorised components found by its discovery tools | \<Organisation\>'s security contact |
| Supplier and NCSC advisories, and NCSC Early Warning | Vulnerabilities in components \<System Name\> uses; incidents and vulnerable services NCSC sees on \<System Name\>'s addresses | Security officer |

### 3.6 Severity and targets

The incident lead sets the severity when the incident is confirmed, and may raise or lower it as facts emerge.

**Table 3: Severity**

| Severity | Examples | Work starts; contained within | Who is told |
| --- | --- | --- | --- |
| Critical | Personal data breach likely to harm people; ransomware; a privileged account compromised | 1 hour; 4 hours | System owner, authorising official, legal adviser, \<Organisation\>'s security contact, and the Data Owner of any schema whose items are involved |
| High | A user account compromised; a secret exposed; access to items someone should not see | 4 hours; 1 working day | System owner, \<Organisation\>'s security contact, and the Data Owner of any schema whose items are involved; legal adviser if personal data is involved |
| Medium | Malware stopped by Defender; repeated failed sign-ins; a supplier advisory affecting \<System Name\> | 1 working day; 5 working days | System owner, \<Organisation\>'s security contact |
| Low | A single policy breach with no data exposed | 5 working days; as planned | \<Organisation\>'s security contact, through the record |

\<Organisation\>'s security contact is told of every confirmed incident, as \<Organisation\>'s incident response capability, and any supplier whose product or service is involved is told whatever the severity (section 3.13). The legal adviser is told at once whenever personal data may be involved (section 3.8).

### 3.7 Handling an incident

Every incident follows these steps, the same severity table and the same record, the incident record, so that handling is consistent. Greater severity means more people and faster targets, not a different process.

1. **Detect and analyse:** the incident lead confirms whether a report is an incident, sets its severity, and opens a record on the incident record.
2. **Contain:** limit the harm, for example by disabling an account, which \<System Name\> refuses within 5 minutes, and ending the person's PingFederate sign-in, removing a group membership, or isolating a server. Ending the PingFederate sign-in alone does not end \<System Name\>'s cookie, so an account is always disabled first, and after a suspected compromise it stays disabled for 8 hours unless every key in the key rings is revoked. Preserve evidence first (section 3.10).
3. **Eradicate:** remove the cause, for example by fixing a flaw or changing secrets.
4. **Recover:** restore normal service, invoking \<Contingency Planning Management\> if needed. The incident plan leads while the outage may be an incident, with the contingency plan in support, and recovery uses a backup taken before the compromise (\<Contingency Planning Management\>, section 3.6.2).
5. **Close and learn:** within 10 working days of containment, the incident lead records the root cause and lessons, and updates this plan, the training and the exercise scenarios; the system owner updates \<Risk List\> and \<Plan of Action and Milestones\>.

### 3.8 Personal data breaches

A personal data breach is any security incident that leads to the accidental or unlawful loss, change, disclosure of, or access to personal data. The privacy requirements that apply are UK GDPR Article 33, reporting to the ICO, Article 34, telling the people affected, and Article 33(5), recording every breach, with the Data Protection Act 2018 and the Data (Use and Access) Act 2025.

1. **Tell the legal adviser at once.** The security officer tells the legal adviser as soon as personal data may be involved.
2. **72 hours from becoming aware.** If the breach is likely to put people's rights and freedoms at risk, the legal adviser tells the ICO within 72 hours of the organisation becoming aware of it, even if not all details are known. A later report gives the reasons for the delay.
3. **Assess and reduce the harm.** The legal adviser and the security officer judge how the breach could harm the people concerned, such as distress, embarrassment, inconvenience, unfairness, discrimination, fraud or the loss of confidentiality, taking account of the kind of data, including special category data, how many people and records, and whether the data could be read, and what would reduce it: getting copies back or deleted, changing access, and telling people what to watch for.
4. **Tell the people affected** without undue delay when the risk to them is high, unless the data was protected, for example by encryption, so that it cannot be read. The legal adviser also decides whether any other organisation must be told, such as another controller whose data it is, or the police (section 3.13).
5. **Record every breach** in the register in section 3.14, whether or not it is reported: the facts, the effects, the action taken, and, if not reported, why.
6. **What the ICO report holds:** what happened, the kinds and rough numbers of people and records, the likely effects, what is being done, and the contact details of the data protection officer, or of the legal adviser if no officer is required (UK GDPR, Article 33(3)(b)).

### 3.9 Playbooks

**Table 4: Playbooks**

| Incident, and its usual severity | Contain | Eradicate and recover |
| --- | --- | --- |
| Stolen or guessed password. Usually High; Critical for an administrator | Ask \<Organisation\>'s service desk to disable the Active Directory account and end the person's PingFederate sign-in, so that \<System Name\> refuses them within 5 minutes, even while a sign-in is open; check the audit records for what was read or exported | \<Organisation\>'s service desk resets the password and second factor; access returns once identity is checked, and no sooner than 8 hours after the account was disabled unless every key in the key rings has been revoked |
| Exposed secret: the token signing key, the audit chain key, the OpenID Connect client credential, a data protection key ring or the backup encryption certificate. Usually High; Critical if backups may have been read | Change the secret at once. For a key ring, revoke every key in it, not only add a new one, as old keys still read existing cookies; every user of that application then signs in again. Change the OpenID Connect client credential with \<Organisation\>'s PingFederate team. For the backup encryption certificate, make a new one for the backups that follow, and ask \<Organisation\> whether any backup copy was reached. There is no database password: the API uses Windows authentication | Find where it was exposed and remove it; check the audit records for misuse since. For the audit chain key, compare the audit log with the daily copies of the newest chain hash in central logging since the exposure |
| Compromise of PingFederate, Active Directory or accounts in them, reported by \<Organisation\>. Usually High; Critical for a privileged account or for PingFederate itself | Ask \<Organisation\> to disable the accounts affected, which \<System Name\> refuses within 5 minutes, and end their PingFederate sign-ins; ask which accounts and groups were touched. If \<Organisation\> cannot say who, have the Windows server administrator revoke every key in the UI and Admin applications' key rings, which ends every \<System Name\> sign-in, as ending PingFederate sign-ins does not. If PingFederate itself or the groups in Active Directory cannot be trusted, the system owner decides whether to stop the service until \<Organisation\> confirms they are safe | Check the audit records for what those accounts did; check the members of \<System Name\>'s groups against the requests authorised in ServiceNow; if PingFederate's signing key may be exposed, have \<Organisation\> replace it and change the OpenID Connect client credential; let people back in once \<Organisation\> confirms the accounts are safe, and no sooner than 8 hours after they were disabled unless the key rings' keys were revoked |
| Ransomware or destructive attack on a server. Usually Critical | Isolate the server through \<Organisation\>; do not power off before evidence is taken | Rebuild and restore from a backup taken before the compromise (\<Contingency Planning Management\>, section 3.6.2); change every secret, make a new backup encryption certificate for the backups that follow, and start the rebuilt applications with new key rings |
| Bulk export or download misuse. Usually High; Critical if personal data | The schema's Data Owner removes the person from the schema's Active Directory group, or \<Organisation\>'s service desk disables the account and ends the person's PingFederate sign-in | Work out what left, with the export audit records; treat as a personal data breach if items holding personal data were included |
| Audit record tampering, or a break in the audit chain (U2). Usually High | Export the audit records with a hash before anything changes; restrict database access | Compare with the daily copies of the newest chain hash in central logging, the last exported copy and backups; fix the cause |
| Someone reads items they should not, including a database administrator reading the item tables outside an approved change or incident (\<Risk List\>, R-AC-01). Usually High; Critical for a privileged account or special category data | Preserve the audit records and SQL Server Audit's records first; have the person removed from the schema's group by its Data Owner, or have \<Organisation\> disable the named account | Work out which items were read, from the audit records or SQL Server Audit; treat it as a personal data breach if they hold personal data (section 3.8) |
| Unexpected change to the software, release files or stored files (U8). Usually High; Critical if malicious | Preserve the changed files and their checksums; isolate the application server through \<Organisation\> if the change may be malicious | Reinstall from the release tag, checking its checksums; compare stored files' checksums with the database and backups; find how the change was made |
| Malicious file uploaded, despite the scan before storing. Usually Medium; High if opened | Record the file's checksum and the audit records; an editor of the schema deletes the item (\<System Description\>, FR-038); to stop further uploads, the Data Owner removes the uploader from the schema's edit group | Scan the servers, and check from the audit records who viewed or downloaded the file |
| Item in the wrong place: filed in the wrong schema, or sent or shown to the wrong person. Usually Medium; High if the item is Restricted or holds personal data | Remove access to the item; find who viewed or exported it, from the audit records | Ask anyone who received a copy to delete it and confirm; file the item in the right schema; treat it as a personal data breach if it holds personal data (section 3.8) |
| Lost or stolen laptop, printout, or phone used for the second factor. Usually Medium; High if unencrypted or holding personal data | \<Organisation\> locks or wipes the device and ends the person's PingFederate sign-in; if the laptop may have been unlocked while a \<System Name\> sign-in was open, or the phone is with someone who may know the password, also have the account disabled, as ending the PingFederate sign-in does not end \<System Name\>'s cookie; for a printout, find out which items it held | Confirm the device was encrypted; check the audit records for what the user viewed or exported; treat personal data as a possible breach (section 3.8) |
| Physical intrusion, fire, flood or power loss at a data centre. Usually High | \<Organisation\> secures the site and tells the security officer; if power cannot be kept, \<Organisation\>'s hosting staff shut the servers down cleanly through the hypervisor (\<Physical and Environmental Protection Management\>, section 3.7); take evidence before anything is moved | Invoke the contingency plan if the site is lost (\<Contingency Planning Management\>); after a power loss, run the start-up checks (\<Security Operating Procedures\>, section 4.6); after an intrusion, check the servers and disks for tampering, and change secrets |

### 3.10 Evidence and forensic readiness

**Table 5: Evidence sources**

| Source | Where it is kept | Kept for | Notes |
| --- | --- | --- | --- |
| Audit records | The \<System Name\> database, table dbo.AuditLog | 12 months online and 12 months in an offline archive (\<Audit and Accountability Management\>) | Times stored in UTC; each record is chained to the one before, and the newest chain hash is copied daily to central logging |
| Application logs | Each application's log on the application server, forwarded to central logging | 30 days on the server; the security events in central logging for 12 months, then 12 months in the offline archive (\<Audit and Accountability Management\>, sections 3.7 and 3.10) | Errors, and the security events that add to the audit records; no personal data beyond the username in a security event |
| Windows and SQL Server logs, including SQL Server Audit | The servers, and \<Organisation\>'s central logging | 12 months in central logging, then 12 months in the offline archive | Operating system and database events, including any read of the item tables by a login other than the API's |
| PingFederate and Active Directory records | \<Organisation\> | As \<Organisation\> sets | Sign-in attempts and changes to group members |
| Backups | The second site (\<Contingency Planning Management\>, section 3.8) | 14 daily, 8 weekly, 12 monthly | A snapshot of the state before an incident, including the audit log; encrypted, and protected as audit information |

1. **Before changing anything,** export the evidence and record its SHA-256 hash, and note it on the incident record with who took it and when.
2. **Time:** all times are UTC. Check each system's clock against a trusted source before building a timeline; the servers take time from \<Organisation\>, within 1 second of UTC.
3. **Custody:** each piece of evidence is listed on the incident record with who holds it, where, and each hand-over.
4. **Personal data in evidence** is handled as \<Classification\> and kept only as long as the incident needs.

### 3.11 Reportable incidents

An event is anything seen in \<System Name\> or reported about it. It becomes an incident when the incident lead confirms that it harms, or may harm, the confidentiality, integrity or availability of \<System Name\> or its information, or breaks a security rule. People report what they suspect; they do not wait to be sure. Everyone reports a suspected incident to the security officer within 1 hour, and the rules of behaviour repeat this (\<Security Operating Procedures\>, Part A).

These must be reported: suspected account misuse; access to items by someone who should not have it; an exposed password or secret; malicious code; an attack on the system; loss or unexpected change of items, stored files or audit records; and a failure of logging or backups. Anything else that looks wrong should be reported too.

### 3.12 Measures and resources

**Table 6: Measures**

| Measure | Target |
| --- | --- |
| Time from noticing to reporting | Within 1 hour |
| Time from reporting to containment | As section 3.6 for the severity |
| Time to recover | Within the contingency plan's recovery time objective of 72 hours |
| Incidents closed with lessons recorded within 10 working days | All |
| Repeat incidents with the same root cause | None |

The security officer reports these measures monthly on the monitoring and integrity report, with the monitoring measures. The resources are the people in section 3.3, ServiceNow, and the evidence sources in section 3.10. \<Organisation\>'s security contact is the first route for forensic help. \[Whether an outside forensic firm is kept on call, and its budget\]. Management support comes from the system owner, who gives the role holders the time to train, exercise and respond, and from the Head of Cyber, who approves the plan and reviews it after each incident (section 3.16).

### 3.13 Sharing information

Information is shared with \<Organisation\>'s security contact, any affected supplier, and the ICO and the people affected through the legal adviser. The security officer tells \<Organisation\>'s security contact of every confirmed incident, and any other supplier whose product or service is involved, using the supplier register (\<Supply Chain Risk Management\>, section 3.5). \<Organisation\> in turn reports a compromise on its side to the security officer within 24 hours. Crime or a significant cyber attack is reported by the system owner to the NCSC or to Report Fraud, the national police reporting service that replaced Action Fraud. Anything else goes through the system owner. Only \[\<Organisation\> communications contact\] speaks to the press or the public about an incident, with the system owner's agreement. If ServiceNow or email may be compromised, use the phone numbers in appendix A. This document is marked \<Classification\>, and is kept in the restricted document store with the other records.

### 3.14 Incident and breach register

Incidents and personal data breaches are listed here, each with its incident record: what happened, the severity, the timeline, the evidence, the actions and the lessons. The measures in section 3.12 are reported each month.

**Table 7: Incident and breach register**

| Reference | Opened | Summary | Severity, breach and status |
| --- | --- | --- | --- |
| \[Incident reference\] | \[date opened\] | \[what happened\] | \[severity\]; personal data breach: \[yes or no\]; \[status\] |

### 3.15 What \<Organisation\> provides

**Table 8: Provided by \<Organisation\>**

| Provided | What \<System Name\> relies on |
| --- | --- |
| Its own incident process, and a route for \<System Name\>'s reports | The security contact takes a report at any time, and tells \<System Name\>'s security officer of a compromise on its side within 24 hours |
| Help during an incident | Monitoring, network and forensic help; isolating a server; disabling an account; locking or wiping a device |
| ServiceNow, for incident records and reports | A workflow built to \<System Name\>'s design: the incident record fields, a notice to the security officer when a report is raised, reminders to each action's owner, and records readable only by the role holders in section 3.3, as they hold Restricted information |
| Its monitoring of the network, PingFederate and Active Directory | Events that show an attack on \<System Name\> reach the security officer |

### 3.16 Keeping the plan

1. **Review and approval.** The Head of Cyber reviews and approves the plan every 12 months and after an incident.
2. **Copies.** Copies go to every role holder in section 3.3 and their deputies: the security officer, the system owner, the authorising official, the technical response team, the auditor and the legal adviser; and to the administrators, the Head of Cyber and \<Organisation\>'s security contact. Each keeps a copy that can be read when the document store is out of use (section 3.4).
3. **Updates.** The security officer updates the plan after each incident and exercise, and when a system or organisational change affects it. Changes are told to the same people, with the change record. Version control records every change.
4. **Protection.** The plan is marked \<Classification\>, and kept in the restricted document store (until the store is set up, the private records repository; \<Documentation Map\>, section 4.1), where only the people in item 2 can read it and only the security officer can change it.

### 3.17 Policy and procedures

\<Policy\> (IR) and \<Procedures\> (IR) are the policy and procedures for this family. Who they are shared with is in \<Policy\>, section IR.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.

## Appendix A Contacts

Use the phone if ServiceNow or email may be compromised.

**Table 9: Contacts**

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
| Information Commissioner's Office | Breach reporting | \[phone to add\] | ICO online breach report form |
| National Cyber Security Centre | Incident reporting | \[phone to add\] | NCSC online incident report |
| Report Fraud, which replaced Action Fraud | Cyber crime and fraud reporting | 0300 123 2040 | Report Fraud online report |
