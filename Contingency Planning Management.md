# \<System Name\> Contingency Planning Management

## 1 Purpose

This document is \<System Name\>'s contingency plan: the design for how it is recovered after a failure. It covers the Contingency Planning (CP) family of the CSS Moderate baseline, 23 controls and enhancements.

Section 3 is the plan: the principles, scope and assumptions, the business impact analysis, the roles, the three phases of activation and notification, recovery and reconstitution, the backups, the second site and telecommunications, testing, training and exercises, what \<Organisation\> provides, keeping the plan current, and coordination with related plans. With appendix A, which holds the contacts, and appendix B, which lists the associated plans, it can be used on its own in an emergency.

### 1.1 Distribution and protection

Copies go to the people in section 3.4 and the authorising official. \<Organisation\>'s IT service desk receives sections 3.5, 3.6 and 3.9 and appendix A, which it needs to act. The same people are told of every change, with a note of what changed.

The document is marked \<Classification\>. It is kept in the restricted document store (until the store is set up, the private records repository; \<Documentation Map\>, section 4.1) with the other records, where only the people above can read it and only the system owner can change it. The system owner and security officer each keep a current offline copy, so that the plan can be used when \<System Name\> and the document store are down. The offline copy is section 3 with appendices A and B, which together are the whole plan. There is no separate plan document. Each offline copy is held on an encrypted \<Organisation\> managed device, or printed, marked and kept in locked storage, and is replaced whenever the plan changes. The superseded copy is destroyed as \<Media Protection Management\>, section 3.6, sets out.

## 2 Related documents

Which section of this design meets each control, who is responsible for it and its status are in \<System Security Plan\>, section 7.6 (Table 15). The assessment is in \<Control Assessment Record\> (CP), the risks are in \<Risk List\>, and open work is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (CP), and the steps people follow are in \<Procedures\> (CP).

## 3 The contingency plan

### 3.1 Principles

1. **Know what matters.** Recovery objectives come from a business impact analysis, not a guess.
2. **Keep copies apart.** Encrypted backups are held away from the main site, with one copy that an attacker on the network cannot change.
3. **Test recovery.** A backup counts only once it has been restored and checked.
4. **Plan ahead.** People know their part, and how to reach each other, before anything fails.
5. **Coordinate.** This plan works with the incident response plan and \<Organisation\>'s plans.
6. **Return only when safe.** Users come back when the data, the functions and the controls have all been checked.

These carry out the principles and rules of \<Policy\>, sections CP.3 and CP.4.

### 3.2 Scope and assumptions

The plan recovers \<System Name\> in three phases: activation and notification, recovery, and reconstitution. Figure 1 shows them against the time allowed.

![Figure 1: The three phases of recovery](figures/cpm-figure-1.png)

**Figure 1: The three phases of recovery**

**Scope:** the UI application, the Admin application, the API, the Microsoft SQL Server 2022 database that holds every item, file, schema definition and audit record, the secrets they need, and the two Windows Server 2025 VMs at \<Organisation\>. \<Organisation\>'s own sites, network and services, including PingFederate and Active Directory, are covered by its plans (appendix B).

**Assumptions:**

1. \<Organisation\> provides a second site, network, sign-in through PingFederate, directory, name resolution and time.
2. The latest good backup, its transaction logs, the latest system-level backup and the protected copy of the secrets, including the backup encryption certificate, are at the second site.
3. The tagged release and the baseline in \<Configuration Management\>, section 3.4, can be reached to rebuild the applications.
4. At least one holder or deputy of each role in section 3.4 is available.
5. An outage that is also a security incident is handled under the incident response plan as well (section 3.6.2).

### 3.3 Business impact analysis

\<System Name\>'s availability is rated Low: an outage delays work, but no service to the public stops. Losing items or audit records cannot be tolerated.

#### 3.3.1 Impact over time

**Table 1: Impact of an outage, by function**

| Function | 24 hours | 72 hours | 1 to 2 weeks |
| --- | --- | --- | --- |
| Sign in, find and read items (essential) | Staff wait or use paper copies where they exist | The business processes it supports are delayed | Requests with legal deadlines, such as subject access, are at risk. By 2 weeks: deadlines are missed |
| Upload and manage items | New items queue | Backlog grows | Backlog takes days to clear. By 2 weeks: records are incomplete |
| Administration: schemas and the groups that open each | None while \<System Name\> is down | None while \<System Name\> is down | Starters wait for access |
| Reports and bulk export | None | None | Planned reports are late |

While \<System Name\> is down nobody can use it, so an outage does not leave leavers with access. The members of \<System Name\>'s AD groups are checked against current staff before users return (section 3.7).

#### 3.3.2 Recovery objectives

**Table 2: Recovery objectives**

| Function | Maximum downtime; recovery time objective | Recovery point objective | Priority |
| --- | --- | --- | --- |
| Sign in, find and read items | 120 hours; 72 hours | 24 hours from the daily backup; less with the archived transaction logs | 1 |
| Upload and manage items | 14 days; 7 days | As above | 2 |
| Administration | 14 days; 7 days | As above | 2 |
| Reports and bulk export | 14 days; 7 days | Not applicable: produced from the database | 3 |

Every time in Table 2 is counted from the start of the outage, not from when the plan is invoked. The recovery time objective includes reconstitution (section 3.7), so 72 hours is the time for both recovery and reconstitution, and users return within 72 hours of the outage starting. The plan is invoked at the latest 24 hours in (section 3.5.1), so the essential functions resume within 72 hours of activation, and normally well within it. That leaves 48 hours within the maximum tolerable downtime for a failed first attempt, such as a damaged backup.

#### 3.3.3 Components, dependencies and order of recovery

**Table 3: Order of recovery**

| Order | Component | Needed for | Recovered from |
| --- | --- | --- | --- |
| 1, provided by \<Organisation\> | \<Organisation\>'s network, PingFederate sign-in, directory, name resolution, time and certificates | Everything | \<Organisation\>'s plans (appendix B) |
| 2, after 1 | Database VM and SQL Server 2022, with its server-level settings: the API's login, SQL Server Audit and the backup jobs | Every function | \<Configuration Management\> baseline, checked against the latest system-level backup (section 3.8) |
| 3, after 1 | Secrets: the backup encryption certificate and its private key, with the retired certificates still needed for the backups kept; the token signing key; the audit chain key, with its retired versions kept for checking; and the OpenID Connect client credential. There is no database password: the API connects with Windows authentication | Restoring the database, and starting the API | The protected copy at the second site (section 3.8) |
| 4, after 2 and 3 | The \<System Name\> database: items, files, schema definitions and audit records | Every function | The latest good backup and transaction logs |
| 5, after 3 and 4 | Application VM: API | Every function | The tagged release and \<Configuration Management\> |
| 6, after 5 | UI application | Finding and reading items | The tagged release |
| 7, after 5 | Admin application | Administration | The tagged release |

\<System Name\> cannot be used while PingFederate is unavailable, because nobody can sign in. \<Organisation\>'s recovery time for PingFederate and Active Directory therefore sets a floor under \<System Name\>'s own. If it is longer than 72 hours, the system owner takes the recovery objectives back to the authorising official.

#### 3.3.4 Essential assets

**Table 4: Essential assets**

| Asset | Why it is essential | Recovery |
| --- | --- | --- |
| The database | Holds every item, file, schema definition, the read and edit group of each schema, and every audit record | Rebuild the VM, then restore the latest good backup and transaction logs |
| The application VM | Runs the API, the UI application and the Admin application | Rebuild from the tagged release and \<Configuration Management\> |
| Backups and transaction logs | The only way back after a loss | Held encrypted at the second site, with one offline or immutable copy |
| Secrets | Without the backup encryption certificate no backup can be restored. Without the others the API cannot start, accept calls from the other two applications or chain audit records, and nobody can sign in | A protected copy held apart from the backups |

The applications' key rings are not essential. They protect the authentication cookie and anti-forgery tokens only: if they are lost, users simply sign in again through PingFederate. They are protected by Windows for the server they were made on, so they could not be read on a rebuilt server, and they are not backed up or restored.

### 3.4 Roles

**Table 5: Contingency roles**

| Role | Holder | Deputy | Part in recovery |
| --- | --- | --- | --- |
| Decides to invoke | \[Name\], system owner | \[Name\] | Invokes this plan, tells the people below, and declares recovery complete |
| Risk decision | \[Name\], authorising official | None | Decides on running in a reduced state, or beyond the recovery time objective |
| Coordination | \[Name\], security officer | \[Name\] | Keeps the activity log, coordinates with any incident, and confirms controls before users return |
| Database | \[Name\], database administrator | \[Name\] | Restores backups and transaction logs, and runs the data checks |
| Servers | \[Name\], Windows server administrator | \[Name\] | Rebuilds the VMs and restores the secrets |
| Service | \<Organisation\>'s IT service desk | Its own rota | Provides the second site and connectivity |

Each role has a deputy, as Table 5 shows. Contact details are in appendix A.

### 3.5 Activation and notification

#### 3.5.1 When the plan is invoked

The system owner, or their deputy, invokes this plan when any of these is true:

1. The essential functions have been unavailable for 24 hours, or are expected to be.
2. The database or its backups are lost, damaged, or cannot be trusted, including after ransomware or a compromise.
3. The main site, or a VM, is lost or unusable.
4. \<Organisation\> declares a disaster that affects the VMs.

Shorter outages are handled as normal operations or incidents. Invoking at 24 hours leaves time to recover within the 72-hour objective.

#### 3.5.2 Outage assessment

Within 4 hours of a report, the database and Windows server administrators assess the outage and tell the system owner: the cause if known, what is damaged, the expected duration, whether data may be lost or altered, and whether it may be a security incident. If it may be, the security officer starts the incident response plan at the same time.

#### 3.5.3 Notification

1. Whoever finds the failure tells \<Organisation\>'s IT service desk and the security officer.
2. The security officer tells the system owner, and starts the activity log.
3. The system owner decides whether to invoke, and tells the database and Windows server administrators, the authorising official and \<Organisation\>'s IT service desk, by phone first and then in writing.
4. The system owner tells users that \<System Name\> is unavailable and when it is expected back, through \<Organisation\>'s usual staff channel, and updates them at least daily.

### 3.6 Recovery

#### 3.6.1 Order of recovery

Recovery follows the order of recovery in section 3.3.3, at the second site if the main one is lost:

1. Confirm \<Organisation\>'s services and the site are available, including PingFederate, without which nobody can sign in, and that the firewall allows every flow F1 to F11 in \<System Description\>, section 6.5, including the application server's route to PingFederate (flow F10) and the administrators' managed administration route (flow F11), and the infrastructure rules for DNS, the domain controllers and the certificate authority (\<System and Communications Protection Management\>, section 3.2).
2. Rebuild the database VM to the baseline in \<Configuration Management\>, sections 3.4 and 3.6, including its server-level settings: the API's login, SQL Server Audit and the backup jobs. Check them against the latest system-level backup (section 3.8).
3. Restore the secrets from their protected copy. First restore the backup encryption certificate and its private key into SQL Server, with any retired certificate that the chosen backup needs: without it the backup cannot be read.
4. Restore the latest good backup, then apply the archived transaction logs up to the last consistent point. If a backup fails its checks, use the one before it.
5. Rebuild the application VM from the tagged release, with each application as a Windows service under its own group managed service account, and start the API, then the UI application, then the Admin application.
6. If a compromise is suspected, change every secret, and create a new backup encryption certificate for the backups that follow, keeping the old one until the backups it encrypted are removed.
7. Move to reconstitution (section 3.7).

#### 3.6.2 Recovery during a security incident

If the outage may be an incident, the incident response plan leads and this plan supports it. Evidence is kept before anything is rebuilt. The restore uses a backup taken before the compromise, and every secret is changed.

#### 3.6.3 Running in a reduced state

There is no manual alternative for reading items. If full recovery would take longer than 72 hours, the system owner may restore sign-in, finding and reading first, with uploads and administration turned off, once the authorising official accepts the risk. Security controls stay in force throughout.

#### 3.6.4 Escalation

As soon as it is clear that users will not be back within 72 hours of the outage starting, and in any case if the database has not been restored 24 hours after the plan is invoked, the system owner tells the authorising official, with a new estimate and the options, including running in a reduced state (section 3.6.3). This leaves the authorising official time to decide before the recovery time objective is missed.

### 3.7 Reconstitution

Users return only once steps 1 to 6 are done, and steps 7 to 9 follow straight after.

1. **Validate the data:** the database administrator checks row counts against the last known counts, each stored file against its SHA-256 checksum, and the audit chain from end to end. The newest audit record shows how much data was lost, against the recovery point objective.
2. **Re-apply deletions:** if the database could not be brought forward to the moment of the failure, items disposed of under the retention schedule, or deleted after a person's request, since the backup was taken would be back. The business owner and the legal adviser check their records of disposals and requests since that time, and the items are deleted again before users return (\<PII Processing Management\>, section 3.7).
3. **Validate the functions:** sign in, find and read an item, upload a test item to a test schema and remove it, and sign in to the Admin application. Audit records must be written for each.
4. **Confirm the controls:** the security officer checks that the controls match the main site, including encryption in transit, the members of \<System Name\>'s AD groups against current staff, and audit logging.
5. **Back up at once:** a full backup is taken and confirmed at the second site.
6. **Declare recovery:** the system owner declares \<System Name\> recovered, and tells users and the people in section 3.4.
7. **Clean up:** temporary access is removed. If running at the second site, the return to the main site is a planned change under \<Configuration Management\>.
8. **Deactivate and learn:** the system owner closes the plan's activation. Within 10 working days an after-action report is written on the exercise and restore test record, and this plan is updated.
9. **Restart monitoring, and check the authorisation:** the security officer confirms that the monitoring duties have restarted. If the recovery changed the system in a way that counts as a significant change, such as a move to the second site, the authorising official decides whether \<System Name\> must be assessed or authorised again (\<Assessment, Authorization, and Monitoring Management\>, section 3.9).

### 3.8 Backups

**Table 6: Backups**

| What | How often, and how long kept | Where | Protection |
| --- | --- | --- | --- |
| The \<System Name\> database, including items, files and audit records | Daily, full SQL Server backup, with checksums. Kept: 14 daily, 8 weekly and 12 monthly copies | \<Organisation\>'s backup service, which copies it to the second site and keeps one offline or immutable copy | Encrypted. The key is held apart from the backups. Its SHA-256 value is recorded when taken |
| SQL Server transaction log backups | Between the daily backups, \[interval\]. Kept: until the oldest daily copy is removed | As above | Encrypted |
| System-level information: SQL Server's system databases (master and msdb), which hold the logins, SQL Server Audit settings and backup jobs, and each VM's Windows configuration and list of installed software | Weekly, and after each change to them. Kept: 8 copies | As above | Encrypted |
| Secrets, including the backup encryption certificate and its private key | At each change. Kept: every version for 12 months, and each retired backup encryption certificate until the last backup it encrypted is removed | A protected copy at the second site, held apart from the backups | Encrypted, with access limited to the system owner and administrators |
| This plan and the records | At each change. Kept: as each record's retention | The controlled library | Access controlled |
| Code and releases | Each release. Kept: every release | The Git host, and the tag recorded in \<Configuration Management\> | Access controlled |

The database administrator's backup jobs write each encrypted backup to \<Organisation\>'s backup service, which copies it to the second site and keeps one copy offline or immutable, so that an attacker on the network cannot change it. A failed backup alerts the database administrator and the security officer, and the week's backups are checked to confirm every job succeeded and reached the second site (\<Security Operating Procedures\>). The system-level backup is not used to restore a server: the servers are rebuilt from the baseline, and the system-level backup is used to check the rebuild and to recover a setting the baseline missed.

**Restore tests.** Restores are tested every 6 months, and after a change to the database or the backup method. Each test restores real data, so it runs on a throwaway virtual server at the second site, built to the database server's baseline, with no network route to production, reached only over the administration route by the database administrator and the security officer, and removed once the test is recorded, its virtual disk erased by method M1 (\<Media Protection Management\>, section 3.6) (D-CP-01). The test fetches the backup and the protected copy of the secrets from the second site, so it also proves that both can be retrieved and used there.

**Encryption.** Every backup is encrypted by SQL Server's backup encryption, with AES-256, before it leaves the database server, so that nobody who holds a copy, including the second site's staff, can read or change it. The key that protects it is a backup encryption certificate in the database server's master database (K10 in the key register, \<System and Communications Protection Management\>, section 3.4). The certificate and its private key are exported, protected by a strong password that is itself held as a secret, apart from the export, to the key store and its protected copy at the second site, held apart from the backups, where only the system owner and the administrators can reach them. A backup cannot be restored on a rebuilt server, or on the restore test server, without that certificate, so every restore starts by restoring it (section 3.6.1). A new certificate is made every 12 months, and each retired certificate is kept until the last backup it encrypted is removed, and then every copy of it is destroyed (\<Media Protection Management\>, section 3.6, method M2). The SHA-256 value recorded when a backup is taken is checked before it is restored.

SQL Server's transaction log backups are taken between the daily backups and copied to the second site, so that a restore can be brought forward to the last consistent point before the failure (section 3.6.1). The database uses SQL Server's full recovery model, which these log backups need. That keeps data loss well within the 24-hour recovery point objective.

**Deleted items in backups.** An item deleted from the database, at the end of its retention period or after a person's request, stays in the encrypted backups until they expire, at most 12 months for a monthly copy. It is beyond use there: the backups are encrypted, held apart and restored only for recovery or a restore test. A recovery re-applies the deletions before users return (section 3.7), and a restore test server is removed after the test. Expired backups are deleted at both sites by \<Organisation\>'s backup service, including the offline or immutable copy once its lock ends (\<Media Protection Management\>, section 3.6, method M2).

The system documentation, including this plan and the other security and privacy documents, is under version control, and each change is kept in the restricted document store (until the store is set up, the private records repository; \<Documentation Map\>, section 4.1).

### 3.9 Second site and telecommunications

**Second site.** \<Organisation\> is expected to provide a second site, far enough from the main one not to share its hazards, such as flood, power supply or a single building. The same site serves for storing backups and for processing.

- **Storage.** It holds the encrypted backups, with one copy offline or immutable, under the same physical and access controls as the main site. Backups are encrypted before they leave the database server, so the site's staff cannot read them.
- **Processing.** If the main site is lost, both servers are rebuilt there, on virtual servers that \<Organisation\> provides, and the essential functions resume within 72 hours of the outage starting (section 3.6.1). \<System Name\> needs nothing else there but its backups, its secrets and the tagged release. The servers are rebuilt to the same baseline (\<Configuration Management\>, section 3.4) by \<System Name\>'s Windows server and database administrators, and the security officer confirms the controls before users return (section 3.7). \<Organisation\> provides the site, the virtual servers and the agreement, and \<System Name\> provides the rebuild and the equivalent controls.
- **Priority.** \<Organisation\> is asked what priority \<System Name\> has at the second site. Availability is rated Low, with 72 hours to recover, so a modest priority is enough.
- **Reaching it.** If a wide-area disruption makes the second site hard to reach, \<Organisation\>'s plans say how the site and its backups are reached. \<System Name\> asks for that part of its plans.

**Telecommunications.** Alternate telecommunications are inherited from \<Organisation\>. Its network connects users to both sites. The alternate service must let the essential functions resume within 72 hours of the outage starting, whether the main service fails at the main site or the second site. \<Organisation\> is asked what alternate service exists, how quickly it takes over, and what priority its main and alternate agreements give. The alternate service must not share a route, a building entry or a provider with the main one. Telecommunications Service Priority is a United States scheme, so \<Organisation\> is asked whether it uses any UK equivalent.

### 3.10 Testing, training and exercises

The first restore test and tabletop exercise take place within 30 days of the VMs being built, and before production.

**Table 7: Test, training and exercise schedule**

| Activity | When | Who | Objective and record |
| --- | --- | --- | --- |
| Role training | Within 30 days of taking a role, and every 12 months. The system owner, the security officer and their deputies take it before taking the role | Everyone in section 3.4: module M8, delivered by the system owner (the security officer delivers it to the system owner), or M10 for the authorising official. \<Organisation\>'s IT service desk is trained by \<Organisation\> | Each person knows this plan, their steps in \<Procedures\> (CP), the call tree and where the offline copy is. Record: training record |
| Restore test | First within 30 days of the VMs being built; then every 6 months | Database administrator, observed by the security officer | Restore the latest backup, with its certificate, to the restore test server at the second site (section 3.8) within the recovery time objective, and pass the data checks in section 3.7, step 1. Record: exercise and restore test record |
| Tabletop exercise, with the incident response plan | First within 30 days of the VMs being built; then every 12 months | Everyone in section 3.4, and \<Organisation\>'s IT service desk | Walk through one scenario from activation to deactivation. Record: exercise and restore test record |
| Plan review | Every 12 months, and after each test or activation | System owner and authorising official | Keep the plan current and build in what was learned. Record: change record |

Tabletop scenarios rotate through: ransomware on the database VM; loss of the main site; a backup that fails its checks; a key person being unavailable; and PingFederate being unavailable. Training content covers the activation criteria, the call tree, each role's steps and the checks before return. The security officer writes it and reviews it every 12 months and after a plan change, test or activation. Role training is module M8 of the role curriculum (\<Awareness and Training Management\>, section 3.4), and the training register shows who is trained (\<Awareness and Training Management\>, section 3.8). After a change to the plan that alters a person's steps, that person is briefed on the change.

Each test has objectives and a scenario set beforehand. Each test or activation ends with an after-action report on the exercise and restore test record, written within 10 working days: the objectives, what happened, the time to recover and data lost against the objectives, what went wrong, the actions with owners and dates, and the changes made to this plan and to the training content. An action that is not done within the month becomes an item in \<Plan of Action and Milestones\>.

### 3.11 What \<Organisation\> provides

**Table 8: Provided by \<Organisation\>**

| Provided | What \<System Name\> relies on |
| --- | --- |
| A second site for backups and for rebuilt servers | A site that does not share the main site's hazards, holds the encrypted backups with one offline or immutable copy, runs the restore test server, meets the same physical and environmental requirements as the main site (\<Physical and Environmental Protection Management\>, section 3.10), can run both servers within 72 hours, and can be reached in a wide-area disruption. \<Organisation\> provides the site and \<System Name\> the rebuild |
| A backup service | Copying each encrypted backup to the second site, keeping one copy offline or immutable, deleting expired copies, and holding the protected copy of the secrets apart from the backups |
| Alternate telecommunications | An alternate service with no single point of failure shared with the main one, and a stated priority |
| Its own disaster recovery and business continuity plans | Who declares a disaster, and the recovery times of the network, PingFederate, Active Directory, name resolution and time |

### 3.12 Keeping the plan current

1. **Review and approval.** The system owner and the authorising official review the plan every 12 months, and after each test or activation, and approve each new version.
2. **Update.** A change to the system that affects recovery updates the plan as part of the change (\<Configuration Management\>, section 3.9). Each after-action report lists the changes made to the plan (section 3.10).
3. **Telling people.** The people who hold copies (section 1.1) are told of each change, with a note of what changed from the change record.
4. **Record.** The plan is under version control, which records every change.

### 3.13 Coordination with related plans

Appendix B lists the related plans. This plan and the incident response plan each cite the other. Their tabletop exercise is held together, and \<Organisation\>'s IT service desk takes part (section 3.10). \<Organisation\>'s disaster recovery and business continuity plans provide the network, PingFederate, the second site and telecommunications. The system owner agrees with \<Organisation\> how the plans fit: who declares a disaster, and the recovery times of the services \<System Name\> depends on (section 3.3.3).

### 3.14 Policy and procedures

\<Policy\> (CP) and \<Procedures\> (CP) are the policy and procedures for this family. Who they are shared with is in \<Policy\>, section CP.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.

## Appendix A Contacts

**Table 9: Contacts**

| Role | Name | Phone | Email |
| --- | --- | --- | --- |
| System owner | \[Name\] | \[phone to add\] | \[email to add\] |
| Authorising official | \[Name\] | \[phone to add\] | \[email to add\] |
| Security officer | \[Name\] | \[phone to add\] | \[email to add\] |
| Database administrator | \[Name\] | \[phone to add\] | \[email to add\] |
| Windows server administrator | \[Name\] | \[phone to add\] | \[email to add\] |
| \<Organisation\>'s IT service desk | \[name to add\] | \[phone to add\] | \[email to add\] |
| \<Organisation\>'s security contact | \[name to add\] | \[phone to add\] | \[email to add\] |

## Appendix B Associated plans and records

**Table 10: Associated plans**

| Plan or record | Owner | How it relates |
| --- | --- | --- |
| \<Incident Response Management\> Incident response plan | Security officer | Leads when an outage may be an incident (section 3.6.2); exercised together |
| \<Organisation\>'s disaster recovery and business continuity plans \[names to add\] | \<Organisation\> | Provide the network, second site and telecommunications |
| \<Configuration Management\>, the configuration management plan | System owner | The baseline the VMs and applications are rebuilt to |
| \<Security Operating Procedures\> Security Operating Procedures | System owner | The routine backup, test and review steps and planned shutdown |
| Training record and the exercise and restore test record in \<Record Templates\> | System owner | Training records, test records and after-action reports |
| \<System Security Plan\>, sections 3.4 and 4 | System owner | The inventory and diagrams of what is rebuilt |
