# \<System Name\> Contingency Planning Management

## 1 Purpose

This document shows how \<System Name\> is recovered after a failure, for each of the 23 Contingency Planning (CP) controls and enhancements in the CSS Moderate baseline. Section 3 is the contingency plan that CP-2 requires: the business impact analysis, the roles, and the three phases of activation and notification, recovery, and reconstitution, with backups, the second site, and testing and training. It can be used on its own in an emergency. Section 4 takes each control in turn. Appendix A records what the tested build showed. Appendix B lists every value CSS asks the organisation to define. Appendix C holds the contacts, and appendix D the associated plans. Appendix E lists the CP controls CSS does not select at Moderate.

The policy is in \<Policy\> (CP), and the steps people follow are in \<Procedures\> (CP).

An assessor examines the plan, the business impact analysis, the backup and restore records, and the test and training records; interviews the people with contingency roles; and may ask to see a restore (CSS). So for each control section 4 gives:

- **each part of the control**, as CSS letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Nothing in the plan can yet be carried out.** There are no servers, no backups and no confirmed second site (PA-64, PA-66). The restore procedure has been shown to work in the test environment only.

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |

### 1.1 Distribution and protection

Copies go to the people in section 3.4 and the authorising official. \<Organisation\>'s IT service desk receives sections 3.5, 3.6 and 3.9 and appendix C, which it needs to act (CP-02\_ODP\[04\]). The same people are told of every change, with a note of what changed (CP-2f).

The document is Restricted. It is kept in the restricted document store with the other records (D-GEN-15), where only the people above can read it and only the system owner can change it (CP-2h). The system owner and security officer each keep a current offline copy, so that the plan can be used when \<System Name\> and the document store are down. The offline copy is section 3 with appendices C and D, which together are the whole plan: the system owner decided against a separate plan document (D-CP-15).

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.6 (Table 15). This section gives only the overall position.

No control in the baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

The most serious gap is that \<System Name\> has no backups, so nothing could be recovered today (PA-64, rated Medium, to be in place before production). Ten of the 23 controls are \<Organisation\>'s to provide, and none of them is confirmed (PA-66, PA-115).

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

**Scope:** UI application, Admin application, API, the PostgreSQL database that holds every document page and audit record, the secrets they need, and the two Windows Server 2025 VMs at \<Organisation\>. \<Organisation\>'s own sites, network and services, including AD FS and Active Directory, are covered by its plans (appendix D).

**Assumptions:**

1. \<Organisation\> provides a second site, network, sign-in through AD FS, directory, name resolution and time (EV-CP-01, EV-CP-02). Unconfirmed.
2. The latest good backup, its transaction logs and the protected copy of the secrets are at the second site.
3. The tagged release and the baseline in \<Configuration Management\>, section 3.4, can be reached to rebuild the applications.
4. At least one holder or deputy of each role in section 3.4 is available.
5. An outage that is also a security incident is handled under the incident response plan as well (section 3.6.2).

### 3.3 Business impact analysis

This analysis follows CSS, Appendix B. \<System Name\>'s availability is rated Low: an outage delays work, but no service to the public stops. Losing documents or audit records cannot be tolerated.

#### 3.3.1 Impact over time

**Table 2: Impact of an outage, by function**

| Function | 24 hours | 72 hours | 1 week | 2 weeks |
| --- | --- | --- | --- | --- |
| Sign in, find and read documents (essential) | Staff wait or use paper copies where they exist | HR and finance requests are delayed | Requests with legal deadlines, such as subject access, are at risk | Deadlines are missed |
| Upload and index documents | New documents queue | Backlog grows | Backlog takes days to clear | Records are incomplete |
| Administration: projects and the groups each uses | None while \<System Name\> is down | None while \<System Name\> is down | Starters wait for access | Starters wait for access |
| Reports and bulk export | None | None | Planned reports are late | Planned reports are late |

While \<System Name\> is down nobody can use it, so an outage does not leave leavers with access. The members of \<System Name\>'s AD groups are checked against current staff before users return (section 3.7).

#### 3.3.2 Recovery objectives

**Table 3: Recovery objectives**

| Function | Maximum tolerable downtime | Recovery time objective | Recovery point objective | Priority |
| --- | --- | --- | --- | --- |
| Sign in, find and read documents | 120 hours | 72 hours | 24 hours; minutes once transaction logs are archived (PA-64) | 1 |
| Upload and index documents | 14 days | 7 days | As above | 2 |
| Administration | 14 days | 7 days | As above | 2 |
| Reports and bulk export | 14 days | 7 days | Not applicable: produced from the database | 3 |

The recovery time objective includes reconstitution (section 3.7), so users return within 72 hours. That leaves 48 hours within the maximum tolerable downtime for a failed first attempt, such as a damaged backup. These values were agreed by the system owner on 9 November 2026 (D-CP-10).

#### 3.3.3 Components, dependencies and order of recovery

**Table 4: Order of recovery**

| Order | Component | Needed for | Depends on | Recovered from |
| --- | --- | --- | --- | --- |
| 1 | \<Organisation\>'s network, AD FS sign-in, directory, name resolution, time and certificates | Everything | \<Organisation\> | \<Organisation\>'s plans (appendix D) |
| 2 | Database VM and PostgreSQL 18.6 | Every function | 1 | \<Configuration Management\> baseline, then the latest good backup and transaction logs |
| 3 | Secrets: the database password and the token signing key | Starting API | 1 | The protected copy at the second site (section 3.8) |
| 4 | Application VM: API | Every function | 2, 3 | The tagged release and \<Configuration Management\> |
| 5 | UI application | Finding and reading documents | 4 | The tagged release |
| 6 | Admin application | Administration | 4 | The tagged release |

\<System Name\> cannot be used while AD FS is unavailable, because nobody can sign in. \<Organisation\>'s recovery time for AD FS and Active Directory therefore sets a floor under \<System Name\>'s own. It is not yet known, and is asked for with EV-CP-01 (D-CP-15, PA-114). If it is longer than 72 hours, the system owner takes the recovery objectives back to the authorising official.

#### 3.3.4 Essential assets

**Table 5: Essential assets (CP-2(8))**

| Asset | Why it is essential | Recovery |
| --- | --- | --- |
| The database | Holds every document page, project, group mapping and audit record | Rebuild the VM, then restore the latest good backup and transaction logs |
| The application VM | Runs API, UI application and Admin application | Rebuild from the tagged release and \<Configuration Management\> |
| Backups and transaction logs | The only way back after a loss | Held encrypted at the second site, with one offline or immutable copy |
| Secrets | Without them API cannot start or reach the database | A protected copy held apart from the backups. Today they are in the settings files (PA-19) |

The ASP.NET Data Protection keys are not essential. They protect sign-in cookies and forms only: if they are lost, users simply sign in again. They are not restored.

### 3.4 Roles

**Table 6: Contingency roles**

| Role | Holder | Deputy | Part in recovery |
| --- | --- | --- | --- |
| Decides to invoke | \[Name\], system owner | \[Name\] | Invokes this plan, tells the people below, and declares recovery complete |
| Risk decision | \[Name\], authorising official | None | Decides on running in a reduced state, or beyond the recovery time objective |
| Coordination | \[Name\], security officer | \[Name\] | Keeps the activity log, coordinates with any incident, and confirms controls before users return |
| Database | \[Name\], database administrator | \[Name\] | Restores backups and transaction logs, and runs the data checks |
| Servers | \[Name\], Windows server administrator | \[Name\] | Rebuilds the VMs and restores the secrets |
| Service | \<Organisation\>'s IT service desk | Its own rota | Provides the second site and connectivity |

Deputies were agreed on 6 November 2026 (D-CP-09). Contact details are in appendix C.

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

Recovery follows PRO-CP-3 in the order of recovery in section 3.3.3, at the second site if the main one is lost:

1. Confirm \<Organisation\>'s services and the site are available, including AD FS, without which nobody can sign in.
2. Rebuild the database VM to the baseline in \<Configuration Management\>, sections 3.4 and 3.6.
3. Restore the latest good backup, then apply the archived transaction logs up to the last consistent point (CP-10(2)). If a backup fails its checks, use the one before it.
4. Restore the secrets from their protected copy. Change them if a compromise is suspected.
5. Rebuild the application VM from the tagged release, with each application under its own service account, and start API, then UI application, then Admin application.
6. Move to reconstitution (section 3.7).

#### 3.6.2 Recovery during a security incident

If the outage may be an incident, the incident response plan leads and this plan supports it. Evidence is kept before anything is rebuilt. The restore uses a backup taken before the compromise, and every secret is changed.

#### 3.6.3 Running in a reduced state

There is no manual alternative for reading documents. If full recovery would take longer than 72 hours, the system owner may restore sign-in, finding and reading first, with uploads and administration turned off, once the authorising official accepts the risk. Security controls stay in force throughout.

#### 3.6.4 Escalation

If the database has not been restored 48 hours after the plan is invoked, the system owner tells the authorising official, with a new estimate and the options.

### 3.7 Reconstitution

Users return only when every step below is done.

1. **Validate the data:** the database administrator runs the checks in PRO-CP-2: row counts against the last known counts, each document page against its stored checksum, and the audit records' stored hashes against the export taken with the backup. The newest audit record shows how much data was lost, against the recovery point objective.
2. **Validate the functions:** sign in, find and read a document, upload a test document to a test project and remove it, and sign in to Admin application. Audit records must be written for each.
3. **Confirm the controls:** the security officer checks that the controls match the main site, including encryption in transit, the members of \<System Name\>'s AD groups against current staff, and audit logging.
4. **Declare recovery:** the system owner declares \<System Name\> recovered, and tells users and the people in section 4.
5. **Back up at once:** a full backup is taken and confirmed at the second site before normal work resumes.
6. **Clean up:** temporary access is removed. If running at the second site, the return to the main site is a planned change under \<Configuration Management\>.
7. **Deactivate and learn:** the system owner closes the plan's activation. Within 10 working days an after-action report is written on TPL-11, and this plan is updated (CP-2g).
8. **Restart monitoring, and check the authorisation:** the security officer confirms that the monitoring duties have restarted. If the recovery changed the system in a way that counts as a significant change, such as a move to the second site, the authorising official decides whether \<System Name\> must be assessed or authorised again (\<Assessment, Authorization, and Monitoring Management\>, section 3.9).

### 3.8 Backups

**Table 7: Backups**

| What | How often | Kept | Where | Protection |
| --- | --- | --- | --- | --- |
| The database, including documents and audit records | Daily, full | 14 daily, 8 weekly and 12 monthly copies | The second site, and one offline or immutable copy | Encrypted. The key is held apart from the backups. Its SHA-256 value is recorded when taken |
| Transaction logs | Continuously | Until the oldest daily copy is removed | The second site | Encrypted |
| Each VM's system configuration | Weekly | 8 copies | The second site | Encrypted |
| Secrets | At each change | Every version for 12 months | A protected copy at the second site, held apart from the backups | Encrypted, with access limited to the system owner and administrators |
| This plan and the records | At each change | As each record's retention | The controlled library (D-GEN-15) | Access controlled |
| Code and releases | Each release | Every release | The Git host, and the tag recorded in \<Configuration Management\> | Access controlled |

A failed backup alerts the database administrator and the security officer, and the week's backups are checked under \<Security Operating Procedures\>, duty C8. Restores are tested every 6 months (PRO-CP-2), and after a change to the database or the backup method. None of this exists yet (PA-64).

### 3.9 Second site and telecommunications

\<Organisation\> is expected to provide a second site, far enough from the main one not to share its hazards, that holds encrypted backups and can run rebuilt VMs with equivalent controls. It is also expected to provide priority of service and separate telecommunications without a shared single point of failure. If a wide-area disruption makes the second site hard to reach, \<Organisation\>'s plans say how it is reached (CP-6(3), CP-7(2)).

None of this is confirmed (EV-CP-01, EV-CP-02, PA-66). If it is not available, the system owner takes the risk to the authorising official.

### 3.10 Testing, training and exercises

This follows CSS. The first restore test and tabletop exercise take place within 30 days of the VMs being built, and before production (D-CP-10, PA-81).

**Table 8: Test, training and exercise schedule**

| Activity | When | Who | Objective | Record |
| --- | --- | --- | --- | --- |
| Role training | Within 30 days of taking a role, and every 12 months | Everyone in section 3.4 | Each person knows this plan, their steps in PRO-CP, the call tree and where the offline copy is | TPL-9 |
| Restore test | First within 30 days of the VMs being built; then every 6 months | Database administrator, observed by the security officer | Restore the latest backup to a separate server within the recovery time objective, and pass the checks in PRO-CP-2 | TPL-11 |
| Tabletop exercise, with the incident response plan | First within 30 days of the VMs being built; then every 12 months | Everyone in section 3.4, and \<Organisation\>'s IT service desk | Walk through one scenario from activation to deactivation | TPL-11 |
| Plan review | Every 12 months, and after each test or activation | System owner and authorising official | Keep the plan current and build in what was learned | Change record |

Tabletop scenarios rotate through: ransomware on the database VM; loss of the main site; a backup that fails its checks; a key person being unavailable; and AD FS being unavailable. Training content covers the activation criteria, the call tree, each role's steps and the checks before return; it is reviewed every 12 months and after a plan change, test or activation.

Each test or activation ends with an after-action report on TPL-11: the objectives, what happened, the time to recover and data lost against the objectives, what went wrong, the actions with owners and dates, and the changes made to this plan.

### 3.11 What \<Organisation\> provides

**Table 9: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| A second site for backups and for rebuilt servers | CP-6, CP-6(1), CP-6(3), CP-7, CP-7(1), CP-7(2), CP-7(3) | A site that does not share the main site's hazards, holds the encrypted backups with one offline or immutable copy, can run both servers within 72 hours, and can be reached in a wide-area disruption | EV-CP-01 | Not sent |
| Alternate telecommunications | CP-8, CP-8(1), CP-8(2) | An alternate service with no single point of failure shared with the main one, and a stated priority | EV-CP-02 | Not sent |
| Its own disaster recovery and business continuity plans | CP-2(1), CP-4(1) | Who declares a disaster, and the recovery times of the network, AD FS, Active Directory, name resolution and time | EV-CP-01 | Not sent |

## 4 Each control and enhancement

The controls are in CSS order. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 CP-1 Policy and Procedures

**Table 10: CP-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A contingency planning policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (CP): a system-level policy. Purpose and scope are in section CP.1, responsibilities in CP.5, and commitment, coordination and compliance in CP.6. It is shared with everyone who administers \<System Name\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-CP-12). Legally reviewed on 9 November 2026. Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (CP): seven procedures, PRO-CP-1 to PRO-CP-7, each naming who acts, when and the record. Shared with the same people | Approved by the system owner (D-CP-13). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding or system change | Reviewed on 9 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 11: CP-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control, and each review is recorded in the change record |
| Rules and procedures | The whole policy (\<Policy\>, section CP.4); all seven procedures (\<Procedures\> (CP)) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; walk-through records on TPL-4; review records. The approvals exist; the rest do not yet |
| Status | Partially implemented |
| Risk decision | NC-CP-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures, and walk through each procedure |

### 4.2 CP-2 Contingency Plan

**Table 12: CP-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A plan that identifies the essential functions and the contingency needs that go with them | Section 3.3.1: four functions, of which signing in, finding and reading documents is essential | Written |
| a.2 | It gives recovery objectives, the order of restoration, and measures | Section 3.3.2 gives the maximum tolerable downtime, recovery time and recovery point for each function, and its priority. Section 3.3.3 gives the order. Each test and activation measures the time to recover and the data lost against them (section 3.10) | Written, and agreed by the system owner (D-CP-10) |
| a.3 | It gives the contingency roles and responsibilities, and the people with their contact details | Section 3.4 names each role, its holder and deputy. Appendix C holds the contact details | Roles and deputies are named (D-CP-09). Every phone number and email is still a placeholder (PA-114) |
| a.4 | It says how the essential functions are kept going despite a disruption | There is no manual alternative for reading documents. Section 3.6.3 allows a reduced service: sign-in, finding and reading first, with uploads and administration off, once the authorising official accepts the risk | Written |
| a.5 | It provides for full restoration in the end, with the planned controls still in force | Section 3.7: users return only when the data, the functions and the controls have all been checked, and a full backup is taken at once | Written |
| a.6 | It says how contingency information is shared | Section 3.5.3: who tells whom, by phone first and then in writing, and daily updates to users | Written |
| a.7 | It is reviewed and approved by defined people | The system owner and the authorising official | Version \<ver\> approved by both (D-CP-11). This restructured version awaits their approval |
| b | Copies go to defined key people and parts of the organisation | Section 1.1: the role holders and the authorising official receive the whole plan; \<Organisation\>'s IT service desk receives the parts it needs to act | Not yet shared (PA-114) |
| c | Contingency planning is coordinated with incident handling | An outage that may be an incident is led by the incident response plan, with this plan in support (section 3.6.2). The two are exercised together | Written into both plans. Not yet exercised (PA-81) |
| d | The plan is reviewed on a schedule | Every 12 months, and after each test or activation | Reviewed on 9 November 2026 and 15 November 2026 |
| e | The plan is updated for changes to the system and for problems met in use or testing | A change to the system that affects recovery updates the plan as part of the change (\<Configuration Management\>, section 3.9). Each after-action report lists the changes made to the plan | Updated on 15 November 2026 for sign-in through AD FS and the service accounts. No test or activation has yet been held |
| f | Changes are told to defined key people and parts of the organisation | The same people as part b, with the change record (PRO-CP-7) | Not yet shared (PA-114) |
| g | Lessons from testing, training and real events are built into testing and training | Each after-action report, on TPL-11, ends with actions and the changes made to the plan and to the training content (section 3.10) | Not yet used |
| h | The plan is protected from unauthorised disclosure and change | It is Restricted, kept in the restricted document store where only the people in part b can read it and only the system owner can change it. The system owner and security officer each keep a current offline copy | Not yet in the restricted store (PA-88). No offline copy has been placed (PA-114) |

**Table 13: CP-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, authorising official |
| Enforced by | Not a system function. Version control records every change to the plan |
| Rules and procedures | Policy rules R1, R8 (\<Policy\>, section CP.4); PRO-CP-3, PRO-CP-5, PRO-CP-7 (\<Procedures\> (CP)) |
| Tests | None for the plan itself. The restore test of 9 November 2026 tested its recovery steps in the test environment (R01 to R09) |
| Records an assessor will ask for | The plan with its approvals; the distribution record; the offline copies; review records; after-action reports. The plan and approvals of version \<ver\> exist |
| Status | Partially implemented |
| Risk decision | NC-CP-02, rated Low: approve |
| Open items | PA-114: share the plan, fill in the contacts, place the offline copies and coordinate with \<Organisation\>'s plans. PA-88: move the document set to the restricted store |

### 4.3 CP-2(1) Coordinate with Related Plans

**Table 14: CP-2(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Develop the plan together with those responsible for related plans | Appendix D lists the related plans. This plan and the incident response plan were written together, and each cites the other. \<Organisation\>'s disaster recovery and business continuity plans provide the network, AD FS, the second site and telecommunications, and the system owner agrees with \<Organisation\> how the plans fit: who declares a disaster, and the recovery times of the services \<System Name\> depends on | The incident response plan is aligned. \<Organisation\>'s plans have not been seen, and their names are placeholders (PA-114) |

**Table 15: CP-2(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R6 (\<Policy\>, section CP.4); PRO-CP-7 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | The related plans; a record of the agreement with \<Organisation\>; joint exercise reports |
| Status | Not implemented |
| Risk decision | NC-CP-03, rated Low: approve |
| Open items | PA-114: obtain \<Organisation\>'s plans and recovery times, and record how the plans fit |

### 4.4 CP-2(3) Resume Mission and Business Functions

**Table 16: CP-2(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Plan to resume defined functions within a defined time of the plan being invoked | The essential functions resume within 72 hours, including reconstitution, within a maximum tolerable downtime of 120 hours (section 3.3.2). The other functions resume within 7 days | Met as a plan (D-CP-10). It cannot be achieved until backups exist (PA-64) |

**Table 17: CP-2(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R1 (\<Policy\>, section CP.4); PRO-CP-3 (\<Procedures\> (CP)) |
| Tests | The restore test showed a restore in seconds in the test environment (R04). It does not show the 72 hours on servers |
| Records an assessor will ask for | The business impact analysis; test reports showing the time taken |
| Status | Implemented |
| Risk decision | NC-CP-04, rated Low: approve; now satisfied as a plan |
| Open items | PA-64: backups. PA-81: the first restore test on the servers |

### 4.5 CP-2(8) Identify Critical Assets

**Table 18: CP-2(8) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Identify the system assets that the defined functions depend on | Section 3.3.4: the database, the application server, the backups and transaction logs, and the secrets. Section 3.3.3 adds what they depend on from \<Organisation\>, including AD FS | Met |

**Table 19: CP-2(8) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R1 (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | The list of essential assets, and its review with the business impact analysis |
| Status | Implemented |
| Risk decision | NC-CP-05, rated Low: approve; now satisfied |
| Open items | None |

### 4.6 CP-3 Contingency Training

**Table 20: CP-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | Train people in their contingency role within a defined time of taking it | Within 30 days. Everyone in section 3.4 learns the plan, their own steps, the call tree and where the offline copy is. It is module M8 of the role curriculum (\<Awareness and Training Management\>, section 3.4) | No training has been given (PA-81) |
| a.2 | Train them again when the system changes | After a change to the plan that alters a person's steps, that person is briefed on the change | Not yet used |
| a.3 | Train them again on a schedule | Every 12 months | Not yet due |
| b | Review and update the training content on a schedule and after defined events | Every 12 months, and after a plan change, a test or an activation | Content is outlined in section 3.10. None is written |

**Table 21: CP-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | Not a system function. The training register shows who is trained (\<Awareness and Training Management\>, section 3.8) |
| Rules and procedures | Policy rule R7 (\<Policy\>, section CP.4); PRO-CP-4 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | The training content; completion records on TPL-9 for each role holder. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CP-06, rated Low: approve; NC-CP-24, rated Low: remediate (system owner, Low) |
| Open items | PA-81: train the role holders. PA-97: write module M8 |

### 4.7 CP-4 Contingency Plan Testing

**Table 22: CP-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Test the plan on a schedule, with defined tests, to judge how well it works and how ready people are | A restore test every 6 months and a tabletop exercise every 12 months, the first of each within 30 days of the servers being built and before production (section 3.10). Each has objectives and a scenario set beforehand | No test of the plan has been held (PA-81). The restore procedure was shown in the test environment on 9 November 2026 |
| b | Review the results | Each test ends with an after-action report on TPL-11 within 10 working days: objectives, what happened, time to recover and data lost against the objectives, and what went wrong | Not yet used |
| c | Start corrective action where needed | Each action has an owner and a date. One that is not done within the month becomes an item in \<Plan of Action and Milestones\> | Not yet used |

**Table 23: CP-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, database administrator |
| Enforced by | Not a system function |
| Rules and procedures | Policy rules R6, R11 (\<Policy\>, section CP.4); PRO-CP-4 (\<Procedures\> (CP)) |
| Tests | Checks R01 to R09 on the v1.0 build, 9 November 2026: a full backup restored to a fresh server with every row, document page checksum and audit hash intact. Two gaps: the default backup is unencrypted (R02), and transaction logs are not archived (R09) |
| Records an assessor will ask for | Test plans; after-action reports on TPL-11; the actions raised. One test record exists, from the test environment |
| Status | Not implemented |
| Risk decision | NC-CP-07, rated Low: approve; NC-CP-24, rated Low: remediate (system owner, Low) |
| Open items | PA-81: hold the first restore test and tabletop exercise |

### 4.8 CP-4(1) Coordinate with Related Plans

**Table 24: CP-4(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Test the plan together with those responsible for related plans | The tabletop exercise is held with the incident response plan, and \<Organisation\>'s IT service desk takes part | Not held (PA-81) |

**Table 25: CP-4(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R6 (\<Policy\>, section CP.4); PRO-CP-4 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | The exercise report naming who took part |
| Status | Not implemented |
| Risk decision | NC-CP-08, rated Low: approve; NC-CP-24, rated Low: remediate (system owner, Low) |
| Open items | PA-81 |

### 4.9 CP-6 Alternate Storage Site

**Table 26: CP-6 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Set up a second site for storing backups, with the agreements needed to store and retrieve them | Encrypted backups are held at a second \<Organisation\> site, with one copy offline or immutable (D-CP-06) | Not confirmed: \<Organisation\> has not been asked (EV-CP-01, PA-66) |
| b | The second site gives controls equal to the main site's | The same physical and access controls as the main site. Backups are encrypted before they leave the database server, so the site's staff cannot read them | Not confirmed |

**Table 27: CP-6 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s site and agreement |
| Rules and procedures | Policy rule R3 (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-09, rated Low: obtain evidence |
| Open items | PA-66: confirm the site with \<Organisation\>, or take the risk to the authorising official |

### 4.10 CP-6(1) Separation from Primary Site

**Table 28: CP-6(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The second site is far enough from the main one not to share its threats | \<Organisation\> is asked to show that the two sites do not share the same hazards, such as flood, power supply or a single building | Not confirmed (EV-CP-01) |

**Table 29: CP-6(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R3 (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-10, rated Low: obtain evidence |
| Open items | PA-66 |

### 4.11 CP-6(3) Accessibility

**Table 30: CP-6(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Identify what could make the second site hard to reach in a wide-area disruption, and say what would be done | \<Organisation\>'s plans say how the site and its backups are reached if the area is disrupted. \<System Name\> asks for that part of its plans | Not confirmed (EV-CP-01) |

**Table 31: CP-6(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R3 (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-11, rated Low: obtain evidence |
| Open items | PA-66 |

### 4.12 CP-7 Alternate Processing Site

**Table 32: CP-7 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Set up a second site for processing, with the agreements needed to move and resume defined operations within a defined time | If the main site is lost, both servers are rebuilt at the second \<Organisation\> site, and the essential functions resume within 72 hours (D-CP-07; section 3.6.1) | Not confirmed (EV-CP-01, PA-66) |
| b | The equipment and supplies needed are at the site, or contracts are in place to deliver them in time | \<Organisation\> provides the virtual servers. \<System Name\> needs nothing else there but its backups, its secrets and the tagged release | Not confirmed |
| c | The second site gives controls equal to the main site's | The servers are rebuilt to the same baseline (\<Configuration Management\>, section 3.4), and the security officer confirms the controls before users return (section 3.7) | Not confirmed |

**Table 33: CP-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\>, Windows server administrator |
| Enforced by | \<Organisation\>'s site and agreement; the baseline |
| Rules and procedures | Policy rule R5 (\<Policy\>, section CP.4); PRO-CP-3 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-12, rated Low: obtain evidence |
| Open items | PA-66 |

### 4.13 CP-7(1) Separation from Primary Site

**Table 34: CP-7(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The second processing site is far enough from the main one not to share its threats | As CP-6(1): the same site holds the backups and runs the rebuilt servers | Not confirmed (EV-CP-01) |

**Table 35: CP-7(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R5 (\<Policy\>, section CP.4); PRO-CP-3 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-13, rated Low: obtain evidence |
| Open items | PA-66 |

### 4.14 CP-7(2) Accessibility

**Table 36: CP-7(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Identify what could make the second processing site hard to reach in a wide-area disruption, and say what would be done | As CP-6(3) | Not confirmed (EV-CP-01) |

**Table 37: CP-7(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R5 (\<Policy\>, section CP.4); PRO-CP-3 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-14, rated Low: obtain evidence |
| Open items | PA-66 |

### 4.15 CP-7(3) Priority of Service

**Table 38: CP-7(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The agreement for the second site gives priority of service that matches the availability needed | \<Organisation\> is asked what priority \<System Name\> has at the second site. Availability is rated Low, with 72 hours to recover, so a modest priority is enough | Not confirmed (EV-CP-01) |

**Table 39: CP-7(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | Policy rule R5 (\<Policy\>, section CP.4); PRO-CP-3 (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s description of the site and its agreement (EV-CP-01). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-15, rated Low: obtain evidence |
| Open items | PA-66 |

### 4.16 CP-8 Telecommunications Services

**Table 40: CP-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Set up alternate telecommunications, with the agreements needed to resume defined operations within a defined time when the main service fails | Inherited from \<Organisation\> (D-CP-08): its network connects users to both sites, and it is asked what alternate service exists and how quickly it takes over | Not confirmed (EV-CP-02, PA-115) |

**Table 41: CP-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | No policy rule of its own (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s service agreements (EV-CP-02). Not yet asked for |
| Status | Not implemented |
| Risk decision | NC-CP-16, rated Low: obtain evidence |
| Open items | PA-115: obtain \<Organisation\>'s evidence (EV-CP-02) |

### 4.17 CP-8(1) Priority of Service Provisions

**Table 42: CP-8(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | The main and alternate service agreements give priority of service that matches the availability needed | \<Organisation\> is asked what priority its agreements give | Not confirmed (EV-CP-02) |
| b | Ask for Telecommunications Service Priority where a common carrier provides the service | Telecommunications Service Priority is a United States scheme. \<Organisation\> is asked whether it uses any UK equivalent | Not confirmed (EV-CP-02) |

**Table 43: CP-8(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | No policy rule of its own (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s service agreements (EV-CP-02) |
| Status | Not implemented |
| Risk decision | NC-CP-17, rated Low: obtain evidence |
| Open items | PA-115 |

### 4.18 CP-8(2) Single Points of Failure

**Table 44: CP-8(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | The alternate service does not share a single point of failure with the main one | \<Organisation\> is asked to show that the two do not share a route, a building entry or a provider | Not confirmed (EV-CP-02) |

**Table 45: CP-8(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\> |
| Rules and procedures | No policy rule of its own (\<Policy\>, section CP.4); no procedure of its own (\<Procedures\> (CP)) |
| Tests | None |
| Records an assessor will ask for | \<Organisation\>'s service agreements and network description (EV-CP-02) |
| Status | Not implemented |
| Risk decision | NC-CP-18, rated Low: obtain evidence |
| Open items | PA-115 |

### 4.19 CP-9 System Backup

**Table 46: CP-9 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Back up user-level information on defined components on a schedule | The database, which holds the documents and audit records, is backed up in full every day, and its transaction logs are archived continuously (section 3.8) | No backups exist (PA-64) |
| b | Back up system-level information on a schedule | Each server's system configuration, weekly. The secrets, at each change | No backups exist |
| c | Back up the system documentation, including the security and privacy documents, on a schedule | At each change: the document set is under version control, and moves to the restricted document store | One copy only: a private local records repository on the system owner's computer, with every change recorded. There is no second copy, so the documentation could be lost with that computer (PA-64, PA-88) |
| d | Protect the confidentiality, integrity and availability of the backups | Backups are encrypted, with the key held apart from them. The SHA-256 value of each backup is recorded when it is taken and checked before it is restored. They are kept at the second site, with one copy offline or immutable. 14 daily, 8 weekly and 12 monthly copies are kept. A failed backup alerts the database administrator and the security officer | Nothing exists. The default PostgreSQL backup is unencrypted (R02) |

**Table 47: CP-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Database and Windows server administrators |
| Enforced by | The backup jobs and their alerts; the weekly check (\<Security Operating Procedures\>, duty C8) |
| Rules and procedures | Policy rules R2, R9 (\<Policy\>, section CP.4); PRO-CP-1 (\<Procedures\> (CP)) |
| Tests | Checks R01 to R09, as CP-4. They test the restore procedure in the test environment, not backups of the servers |
| Records an assessor will ask for | Backup job logs; the retention of copies; the alert on a failed job; the weekly checks on TPL-8. None exist yet |
| Status | Not implemented |
| Risk decision | NC-CP-19, rated Medium: remediate before production |
| Open items | PA-64: encrypted backups with archived transaction logs, in place before production |

### 4.20 CP-9(1) Testing for Reliability and Integrity

**Table 48: CP-9(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Test the backups on a schedule, to show the media are reliable and the information intact | Every 6 months, and after a change to the database or the backup method, the database administrator restores the latest backup to a separate server and checks it: row counts against the last known counts, each document page against its stored checksum, and the audit records' hashes against the export taken with the backup (PRO-CP-2). The security officer observes | Shown in the test environment on 9 November 2026: the restore worked (R03, R04) and the data was intact (R05 to R07). There are no backups of the servers to test (PA-64) |

**Table 49: CP-9(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Database administrator |
| Enforced by | The restore test |
| Rules and procedures | Policy rule R4 (\<Policy\>, section CP.4); PRO-CP-2 (\<Procedures\> (CP)) |
| Tests | Checks R03 to R07 passed |
| Records an assessor will ask for | Restore test reports on TPL-11. One exists, from the test environment |
| Status | Not implemented |
| Risk decision | NC-CP-20, rated Medium: remediate before production |
| Open items | PA-64, then PA-81: the first restore test on the servers |

### 4.21 CP-9(8) Cryptographic Protection

**Table 50: CP-9(8) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use cryptography to stop backups being read or changed without authority | Every backup is encrypted before it leaves the database server. The key is held apart from the backups, where only the system owner and the administrators can reach it, and is listed in the key register (\<System and Communications Protection Management\>, section 3.4) | Not built. The default PostgreSQL backup is a plain archive that anyone holding it can read (R02; PA-64) |

**Table 51: CP-9(8) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Database administrator |
| Enforced by | The backup tool's encryption; the key store |
| Rules and procedures | Policy rules R3, R10 (\<Policy\>, section CP.4); PRO-CP-1 (\<Procedures\> (CP)) |
| Tests | Check R02 showed the gap |
| Records an assessor will ask for | The backup settings showing encryption; the key register entry; who can reach the key |
| Status | Not implemented |
| Risk decision | NC-CP-21, rated Medium: remediate before production |
| Open items | PA-64 |

### 4.22 CP-10 System Recovery and Reconstitution

**Table 52: CP-10 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Recover the system and bring it back to a known state within a defined time after a disruption, compromise or failure | Sections 3.6 and 3.7. The servers are rebuilt to the baseline, the latest good backup is restored, and users return only when the data, the functions and the controls have been checked. Monitoring is restarted, and a recovery that amounts to a significant change goes to the authorising official. Recovery and reconstitution together take no more than 72 hours, losing no more than 24 hours of data | \<System Name\> cannot be recovered today: there are no servers and no backups. The restore itself took seconds in the test environment (R04) |

**Table 53: CP-10 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Administrators, system owner |
| Enforced by | The backups; the baseline; the checks before users return |
| Rules and procedures | Policy rules R1, R11 (\<Policy\>, section CP.4); PRO-CP-3, PRO-CP-6 (\<Procedures\> (CP)) |
| Tests | Checks R04 to R07 passed in the test environment |
| Records an assessor will ask for | Activity logs and after-action reports of any recovery or test. None exist for the servers |
| Status | Not implemented |
| Risk decision | NC-CP-22, rated Medium: remediate before production |
| Open items | PA-64: backups. PA-81: the first test on the servers |

### 4.23 CP-10(2) Transaction Recovery

**Table 54: CP-10(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Provide transaction recovery for systems that are based on transactions | PostgreSQL's transaction logs are archived continuously to the second site, so that a restore can be brought forward to the last consistent point before the failure. That gives a recovery point of minutes | Not built: the logs are not archived (R09; PA-64) |

**Table 55: CP-10(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Database administrator |
| Enforced by | PostgreSQL's log archiving |
| Rules and procedures | Policy rule R2 (\<Policy\>, section CP.4); PRO-CP-3 (\<Procedures\> (CP)) |
| Tests | Check R09 showed the gap |
| Records an assessor will ask for | The archiving settings; a restore test that replays the logs |
| Status | Not implemented |
| Risk decision | NC-CP-23, rated Medium: remediate before production |
| Open items | PA-64 |

## Appendix A How recovery was built in the tested build

The Docker stack keeps data in named volumes and has no backup or restore tooling, and PostgreSQL's transaction logs are not archived.

On 9 November 2026 Test-BackupRestore.ps1 showed, on a throwaway stack at the v1.0 tag, that a full database backup restores to a fresh server in about 4 seconds with every row, document page checksum and audit hash intact. It also showed two gaps: the default backup is unencrypted (R02), and transaction logs are not archived (R09). Both are part of PA-64. The evidence is in the CP evidence. It proves the procedure, not a backup of the VMs.

## Appendix B Parameter register

These are the CSS organisation-defined values for the 23 CP entries: 38 in total. They were agreed on 6 November 2026 (D-CP-P01), and CP-09\_ODP\[01\] was revised on 9 November 2026 (D-CP-P02). State now says whether each is in place today.

**Table 56: CP parameter register**

| CSS identifier | What must be defined | Value | State now |
| --- | --- | --- | --- |
| CP-01\_ODP\[01\] | Who receives the policy | Everyone who administers \<System Name\> | Not yet shared |
| CP-01\_ODP\[02\] | Who receives the procedures | Everyone who administers \<System Name\> | Not yet shared |
| CP-01\_ODP\[03\] | Level of the policy | System level | Met |
| CP-01\_ODP\[04\] | Official who manages them | System owner | Met |
| CP-01\_ODP\[05\] | Policy review frequency | Every 12 months | Met: reviewed 9 November 2026 |
| CP-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding or system change | Met: reviewed after the CP pack review |
| CP-01\_ODP\[07\] | Procedures review frequency | Every 12 months | Met: reviewed 9 November 2026 |
| CP-01\_ODP\[08\] | Events requiring procedures review | A change to the steps | Met: reviewed after the CP pack review |
| CP-02\_ODP\[01\] | Who reviews the plan | System owner and authorising official | Met: version \<ver\> approved 9 November 2026 |
| CP-02\_ODP\[02\] | Who approves the plan | System owner and authorising official | Met: version \<ver\> approved 9 November 2026 |
| CP-02\_ODP\[03\] | Key personnel who receive copies | System owner, administrators and security officer | Not yet shared |
| CP-02\_ODP\[04\] | Elements who receive copies | \<Organisation\>'s IT service desk | Not yet shared |
| CP-02\_ODP\[05\] | Review frequency | Every 12 months | Met |
| CP-02\_ODP\[06\] | Key personnel told of changes | As CP-02\_ODP\[03\] | Not yet shared |
| CP-02\_ODP\[07\] | Elements told of changes | As CP-02\_ODP\[04\] | Not yet shared |
| CP-02(03)\_ODP\[01\] | Functions resumed | Essential | Planned (section 3.3) |
| CP-02(03)\_ODP\[02\] | Time to resume | Within 72 hours | Planned; cannot be met until PA-64 |
| CP-02(08)\_ODP | Functions supported | Essential | Met (section 3.3.4) |
| CP-03\_ODP\[01\] | Time to train after taking a role | 30 days | No training yet (PA-81) |
| CP-03\_ODP\[02\] | Training frequency | Every 12 months | No training yet (PA-81) |
| CP-03\_ODP\[03\] | Content review frequency | Every 12 months | Content outlined in section 3.10 |
| CP-03\_ODP\[04\] | Events requiring content review | A plan change, a test or an activation | Content outlined in section 3.10 |
| CP-04\_ODP\[01\] | Test frequency | Every 12 months | No test yet (PA-81) |
| CP-04\_ODP\[02\] | Tests of effectiveness | Tabletop exercise and restore test | Restore procedure shown in Docker on 9 November 2026; not on the VMs |
| CP-04\_ODP\[03\] | Tests of readiness | Tabletop exercise and restore test | No test yet (PA-81) |
| CP-07\_ODP\[01\] | Operations transferred | Essential functions | Second site unconfirmed (PA-66) |
| CP-07\_ODP\[02\] | Time to transfer | Within 72 hours | Second site unconfirmed (PA-66) |
| CP-08\_ODP\[01\] | Operations resumed | Essential functions | Unconfirmed (EV-CP-02) |
| CP-08\_ODP\[02\] | Time to resume | Within 72 hours | Unconfirmed (EV-CP-02) |
| CP-09\_ODP\[01\] | Components backed up | The database, which holds the documents and audit records; each VM's system configuration; and the secrets needed to run \<System Name\> (D-CP-P02) | No backups (PA-64) |
| CP-09\_ODP\[02\] | User-level backup frequency | Daily, with transaction logs archived continuously | No backups (PA-64) |
| CP-09\_ODP\[03\] | System-level backup frequency | Weekly | No backups (PA-64) |
| CP-09\_ODP\[04\] | Documentation backup frequency | At each change | Library copy only; moves to SharePoint (D-GEN-15) |
| CP-09(01)\_ODP\[01\] | Reliability test frequency | Every 6 months | Shown in Docker on 9 November 2026 (R03, R04) |
| CP-09(01)\_ODP\[02\] | Integrity test frequency | Every 6 months | Shown in Docker on 9 November 2026 (R05 to R07) |
| CP-09(08)\_ODP | Information protected | All backups | Default backups are unencrypted (R02, PA-64) |
| CP-10\_ODP\[01\] | Recovery time | Within 72 hours, losing no more than 24 hours of data | Not possible until PA-64 |
| CP-10\_ODP\[02\] | Reconstitution time | Within 72 hours, losing no more than 24 hours of data | Not possible until PA-64 |

## Appendix C Contacts

**Table 57: Contacts**

| Role | Name | Phone | Email |
| --- | --- | --- | --- |
| System owner | \[Name\] | \[phone to add\] | \[email to add\] |
| Authorising official | \[Name\] | \[phone to add\] | \[email to add\] |
| Security officer | \[Name\] | \[phone to add\] | \[email to add\] |
| Database administrator | \[Name\] | \[phone to add\] | \[email to add\] |
| Windows server administrator | \[Name\] | \[phone to add\] | \[email to add\] |
| \<Organisation\>'s IT service desk | \[name to add\] | \[phone to add\] | \[email to add\] |
| \<Organisation\>'s security contact | \[name to add\] | \[phone to add\] | \[email to add\] |

## Appendix D Associated plans and records

**Table 58: Associated plans**

| Plan or record | Owner | How it relates |
| --- | --- | --- |
| \<Incident Response Management\> Incident response plan | Security officer | Leads when an outage may be an incident (section 3.6.2); exercised together (CP-4(1)) |
| \<Organisation\>'s disaster recovery and business continuity plans \[names to add\] | \<Organisation\> | Provide the network, second site and telecommunications (EV-CP-01, EV-CP-02) |
| \<Configuration Management\>, the configuration management plan | System owner | The baseline the VMs and applications are rebuilt to |
| \<Security Operating Procedures\> Security Operating Procedures | System owner | The routine backup and check steps (C2, C6, C8, C18, C21) and planned shutdown |
| TPL-9 and TPL-11 in \<Record Templates\> | System owner | Training records, test records and after-action reports |
| \<System Security Plan\>, sections 3.4 and 4 | System owner | The inventory and diagrams of what is rebuilt |

## Appendix E CP controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. Some of the design goes further than the baseline, and Table 59 says where.

**Table 59: CP controls not selected at Moderate**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| CP-2(2) Capacity Planning | Capacity planned for processing, telecommunications and support during a contingency | Not required. The second site is asked to run both servers at their normal size (EV-CP-01) |
| CP-2(5) Continue Mission and Business Functions | Functions continue with little or no loss of continuity | Not required. Availability is rated Low, and 72 hours is accepted |
| CP-3(1) Simulated Events | Training that simulates a real event | Not required. The tabletop exercise walks through a scenario |
| CP-4(2) Alternate Processing Site | Testing the plan at the second site | Not required, and not planned. The first restore test is on the main servers |
| CP-6(2) Recovery Time and Recovery Point Objectives | The storage site set up to meet the recovery objectives | Not required. Done in design: transaction logs go to the second site continuously, for a recovery point of minutes |
| CP-7(4) Preparation for Use | The second site kept ready to use | Not required. The servers are rebuilt there when needed |
| CP-8(3), CP-8(4) Separation of Providers; Provider Contingency Plan | Alternate services from a separate provider, who has a contingency plan | Not required. \<Organisation\>'s plans are asked for with EV-CP-01 |
| CP-9(2), CP-9(3), CP-9(5) Test Restoration Using Sampling; Separate Storage for Critical Information; Transfer to Alternate Storage Site | Further assurance for backups | Not required. Done in design: every restore test restores the whole database; one copy is offline or immutable; backups and logs go to the second site |
| CP-10(4) Restore Within Time Period | Components restored from configuration-controlled images within a set time | Not required. Done in design: the servers are rebuilt from the baseline and the tagged release (\<Configuration Management\>, section 3.4) |
