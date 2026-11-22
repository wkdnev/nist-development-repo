# \<System Name\> Security Procedures

## 1 How to use this document

This document holds the security and privacy procedures for \<System Name\>: 139 procedures in 19 chapters, one chapter for each CSS control family that applies, in CSS order. A procedure says who does what, when, and what record is kept. The rules the procedures carry out are in \<Policy\>, and the design, values and decisions they use are in each family's design document (\<Documentation Map\>, section 2.2).

- **Finding a procedure.** Section 2 lists every procedure. Each procedure is headed by its number, such as PRO-AC-3, which never changes.
- **Reading a chapter.** Most chapters start with a table that summarises each procedure: what starts it, who acts, the time limit, the record and the controls it serves. The steps follow.
- **Manual steps.** A step marked **Manual** is carried out and recorded by a person, without support from the system.
- **Records.** Records use the forms in \<Record Templates\>, TPL-1 to TPL-25, or a ServiceNow record with the same fields.
- **Walk-through.** Each procedure is walked through once on form TPL-4 before go-live.
- **Citing.** Cite a procedure by its number, as \<Procedures\>, PRO-AC-3. Cite a chapter as \<Procedures\> (AC), a section as \<Procedures\>, section AC.2, and a table as \<Procedures\>, Table AC-4.

## 2 Index of procedures

**Table 1: Index of procedures**

| Procedure | Title | Chapter |
| --- | --- | --- |
| PRO-AC-1 | New user (joiner) | AC Access Control |
| PRO-AC-2 | Role change (mover) | AC Access Control |
| PRO-AC-3 | Leaver | AC Access Control |
| PRO-AC-4 | Urgent disable (high-risk individual) | AC Access Control |
| PRO-AC-5 | Schema access | AC Access Control |
| PRO-AC-6 | Privileged access | AC Access Control |
| PRO-AC-7 | Access review | AC Access Control |
| PRO-AC-8 | Inactive accounts | AC Access Control |
| PRO-AC-9 | Locked account | AC Access Control |
| PRO-AC-10 | Forgotten password | AC Access Control |
| PRO-AC-11 | Ending access at once | AC Access Control |
| PRO-AC-12 | First administrator on a new installation | AC Access Control |
| PRO-AC-13 | Changing the system use notice | AC Access Control |
| PRO-AC-14 | Policy and procedure review | AC Access Control |
| PRO-AC-15 | Exception management | AC Access Control |
| PRO-AC-16 | Sharing and export requests | AC Access Control |
| PRO-AC-17 | Non-compliance and risk decisions | AC Access Control |
| PRO-AT-1 | Awareness and the \<System Name\> briefing | AT Awareness and Training |
| PRO-AT-2 | Role training | AT Awareness and Training |
| PRO-AT-3 | Keeping content current | AT Awareness and Training |
| PRO-AT-4 | Records and the register | AT Awareness and Training |
| PRO-AT-5 | Measures and checking | AT Awareness and Training |
| PRO-AU-1 | Weekly review | AU Audit and Accountability |
| PRO-AU-2 | Audit chain check | AU Audit and Accountability |
| PRO-AU-3 | Logging failure | AU Audit and Accountability |
| PRO-AU-4 | Capacity and retention | AU Audit and Accountability |
| PRO-AU-5 | Changing the logged events | AU Audit and Accountability |
| PRO-AU-6 | Auditor access | AU Audit and Accountability |
| PRO-AU-7 | Application log | AU Audit and Accountability |
| PRO-CA-1 | Assessing controls | CA Assessment, Authorization, and Monitoring |
| PRO-CA-2 | Managing connections | CA Assessment, Authorization, and Monitoring |
| PRO-CA-3 | Keeping the plan up to date | CA Assessment, Authorization, and Monitoring |
| PRO-CA-4 | Authorising | CA Assessment, Authorization, and Monitoring |
| PRO-CA-5 | Monitoring | CA Assessment, Authorization, and Monitoring |
| PRO-CA-6 | Deciding whether a change is significant | CA Assessment, Authorization, and Monitoring |
| PRO-CA-7 | Inherited controls | CA Assessment, Authorization, and Monitoring |
| PRO-CM-1 | Making a change | CM Configuration Management |
| PRO-CM-2 | Reviewing the baseline | CM Configuration Management |
| PRO-CM-3 | Secure settings | CM Configuration Management |
| PRO-CM-4 | Software | CM Configuration Management |
| PRO-CM-5 | Reviewing functions and ports | CM Configuration Management |
| PRO-CM-6 | Unauthorised components | CM Configuration Management |
| PRO-CM-7 | Monitoring for drift | CM Configuration Management |
| PRO-CM-8 | Emergency change | CM Configuration Management |
| PRO-CM-9 | Licence review | CM Configuration Management |
| PRO-CP-1 | Taking backups | CP Contingency Planning |
| PRO-CP-2 | Testing a restore | CP Contingency Planning |
| PRO-CP-3 | Recovering | CP Contingency Planning |
| PRO-CP-4 | Training and testing | CP Contingency Planning |
| PRO-CP-5 | Activation and notification | CP Contingency Planning |
| PRO-CP-6 | Reconstitution and deactivation | CP Contingency Planning |
| PRO-CP-7 | Maintaining and sharing the plan | CP Contingency Planning |
| PRO-IA-1 | Identifiers | IA Identification and Authentication |
| PRO-IA-2 | Passwords | IA Identification and Authentication |
| PRO-IA-3 | Suspected compromise, role change, or a lost or stolen authenticator | IA Identification and Authentication |
| PRO-IA-4 | Changing service secrets and the signing key | IA Identification and Authentication |
| PRO-IA-5 | Password rules | IA Identification and Authentication |
| PRO-IA-6 | Enrolling and resetting a second factor | IA Identification and Authentication |
| PRO-IA-7 | Reviewing authenticators and assurance levels | IA Identification and Authentication |
| PRO-IA-8 | Disabling unused identifiers | IA Identification and Authentication |
| PRO-IR-1 | Reporting an incident | IR Incident Response |
| PRO-IR-2 | Handling an incident | IR Incident Response |
| PRO-IR-3 | Training and testing | IR Incident Response |
| PRO-IR-4 | Getting help | IR Incident Response |
| PRO-IR-5 | Handling a personal data breach | IR Incident Response |
| PRO-IR-6 | Preserving evidence | IR Incident Response |
| PRO-IR-7 | Closing an incident and learning | IR Incident Response |
| PRO-MA-1 | Scheduling, approving, checking and recording maintenance | MA Maintenance |
| PRO-MA-2 | Removing equipment | MA Maintenance |
| PRO-MA-3 | Maintenance tools | MA Maintenance |
| PRO-MA-4 | Remote maintenance | MA Maintenance |
| PRO-MA-5 | Maintenance people | MA Maintenance |
| PRO-MA-6 | Preventive maintenance schedule | MA Maintenance |
| PRO-MA-7 | Built-in diagnostics and data leaving for support | MA Maintenance |
| PRO-MP-1 | Printouts | MP Media Protection |
| PRO-MP-2 | Disks, volumes and backups | MP Media Protection |
| PRO-MP-3 | Sanitising media | MP Media Protection |
| PRO-MP-4 | Portable storage and ownerless devices | MP Media Protection |
| PRO-MP-5 | Export copies and users' copies | MP Media Protection |
| PRO-MP-6 | Media inventory | MP Media Protection |
| PRO-PE-1 | Checking \<Organisation\>'s evidence | PE Physical and Environmental Protection |
| PRO-PE-2 | Physical incidents | PE Physical and Environmental Protection |
| PRO-PE-3 | Screens and printers | PE Physical and Environmental Protection |
| PRO-PE-4 | Working from home | PE Physical and Environmental Protection |
| PRO-PE-5 | Site inspection | PE Physical and Environmental Protection |
| PRO-PL-1 | Keeping the plans current | PL Planning |
| PRO-PL-2 | Sharing the plans | PL Planning |
| PRO-PL-3 | Signing the rules | PL Planning |
| PRO-PL-4 | Tailoring | PL Planning |
| PRO-PL-5 | Reviewing the architecture | PL Planning |
| PRO-PL-6 | Protecting the plans | PL Planning |
| PRO-PS-1 | Before access | PS Personnel Security |
| PRO-PS-2 | Leavers | PS Personnel Security |
| PRO-PS-3 | Movers | PS Personnel Security |
| PRO-PS-4 | Reviewing designations and agreements | PS Personnel Security |
| PRO-PS-5 | External people | PS Personnel Security |
| PRO-PS-6 | Sanctions | PS Personnel Security |
| PRO-PS-7 | Checking | PS Personnel Security |
| PRO-PT-1 | Requests from individuals | PT Personally Identifiable Information Processing and Transparency |
| PRO-PT-2 | Complaints | PT Personally Identifiable Information Processing and Transparency |
| PRO-PT-3 | Changes in processing | PT Personally Identifiable Information Processing and Transparency |
| PRO-PT-4 | Impact assessment | PT Personally Identifiable Information Processing and Transparency |
| PRO-PT-5 | Accuracy, retention and disposal | PT Personally Identifiable Information Processing and Transparency |
| PRO-PT-6 | Training and test data | PT Personally Identifiable Information Processing and Transparency |
| PRO-RA-1 | Reviewing risk | RA Risk Assessment |
| PRO-RA-2 | Reviewing the supply chain | RA Risk Assessment |
| PRO-RA-3 | Scanning and analysing | RA Risk Assessment |
| PRO-RA-4 | Responding to an exploited flaw | RA Risk Assessment |
| PRO-RA-5 | Sharing results and receiving reports | RA Risk Assessment |
| PRO-RA-6 | Reviewing critical components | RA Risk Assessment |
| PRO-SA-1 | Developing a change | SA System and Services Acquisition |
| PRO-SA-2 | Testing a release | SA System and Services Acquisition |
| PRO-SA-3 | Buying a product or service | SA System and Services Acquisition |
| PRO-SA-4 | Documentation | SA System and Services Acquisition |
| PRO-SA-5 | Unsupported components | SA System and Services Acquisition |
| PRO-SA-6 | Budgeting and reviews | SA System and Services Acquisition |
| PRO-SA-7 | Adding a third-party component | SA System and Services Acquisition |
| PRO-SC-1 | Setting up and checking TLS | SC System and Communications Protection |
| PRO-SC-2 | Managing certificates | SC System and Communications Protection |
| PRO-SC-3 | Changing keys | SC System and Communications Protection |
| PRO-SC-4 | Changing the boundary | SC System and Communications Protection |
| PRO-SC-5 | Checking page code | SC System and Communications Protection |
| PRO-SC-6 | Responding to denial of service | SC System and Communications Protection |
| PRO-SC-7 | Testing encryption at rest | SC System and Communications Protection |
| PRO-SC-8 | Reviewing the register and boundary | SC System and Communications Protection |
| PRO-SI-1 | Fixing flaws | SI System and Information Integrity |
| PRO-SI-2 | Handling malicious code | SI System and Information Integrity |
| PRO-SI-3 | Reviewing monitoring | SI System and Information Integrity |
| PRO-SI-4 | Responding to an alert | SI System and Information Integrity |
| PRO-SI-5 | Acting on advisories | SI System and Information Integrity |
| PRO-SI-6 | Checking integrity | SI System and Information Integrity |
| PRO-SI-7 | Managing information | SI System and Information Integrity |
| PRO-SI-8 | Testing integrity controls | SI System and Information Integrity |
| PRO-SR-1 | Bringing in a component | SR Supply Chain Risk Management |
| PRO-SR-2 | Reviewing suppliers and the plan | SR Supply Chain Risk Management |
| PRO-SR-3 | Inspecting a release | SR Supply Chain Risk Management |
| PRO-SR-4 | Authenticity and counterfeits | SR Supply Chain Risk Management |
| PRO-SR-5 | Notices and advisories | SR Supply Chain Risk Management |
| PRO-SR-6 | Disposal | SR Supply Chain Risk Management |

## AC Access Control

Procedures PRO-AC-1 to PRO-AC-17.

### AC.1 Purpose

These procedures define how access control activities are performed: the workflows, approval routes, steps, reviews and exception handling. The values they use are in \<Access Control Management\>. Steps marked **Manual** have no support in the system.

### AC.2 Workflows

**Table AC-1: Workflows**

| Workflow | Starts when | Stages | Steps |
| --- | --- | --- | --- |
| Joiner | Someone needs access | Request, approve, sign SyOPS, add to AD groups, first sign-in | PRO-AC-1 |
| Mover | Someone's role changes | Notify, approve new access, change groups | PRO-AC-2 |
| Leaver | Someone leaves or no longer needs access | Notify, deactivate, record | PRO-AC-3 |
| Urgent disable | A concern is raised about someone | Report, disable the account, confirm \<System Name\> refuses it, record | PRO-AC-4 |
| Schema access | Someone needs a schema | Request, approve, change group | PRO-AC-5 |
| Privileged access | Someone needs a privileged role | Request, approve, change role, record | PRO-AC-6 |
| Exception | A rule cannot be met | Request, assess, approve, record, review, end | PRO-AC-15 |
| Sharing or export | Information needs to leave a schema | Request, check recipient, decide, deliver, record | PRO-AC-16 |
| Non-compliance | A control or part is not met | Record, rate, decide, then accept or plan remediation | PRO-AC-17 |

### AC.3 Approval routes

**Table AC-2: Approval routes**

| Request | Raised by | Approved by | Carried out by | Record kept in |
| --- | --- | --- | --- | --- |
| Schema read or edit access, including a new user's first access | The person; their line manager approves | Data Owner authorises | Data Owner, as owner of the schema's groups | ServiceNow request (TPL-2) |
| Change to which groups open a schema, or deactivating, reactivating or deleting a schema | Administrator | The schema's Data Owner | Administrator, in the Admin application | Change record (TPL-6) |
| Administrator, auditor, security officer, business owner or legal adviser's delegate | The person; their line manager approves, and the legal adviser names the legal adviser's delegate | System owner authorises, and cannot authorise their own | System owner, as owner of the five role groups | ServiceNow request (TPL-2) |
| Sharing or export outside a schema | Requesting user | Data Owner | An editor of the schema | Sharing decision record (TPL-25) |
| External system or portable storage use | Requesting user | System owner | Requesting user | Exception (TPL-17) |
| Exception to a rule | Whoever needs it | System owner, or authorising official if above their authority | Role concerned | TPL-17, and \<Risk List\> |
| Urgent disable | Anyone | No prior approval needed; system owner told at once | \<Organisation\>'s service desk | TPL-14, and TPL-10 if it is an incident |
| Change to policy or procedures | Document owner | System owner | Document owner | Document change record |

### AC.4 Review activities

**Table AC-3: Review activities**

| Activity | How often | By | Output | Steps |
| --- | --- | --- | --- | --- |
| Privileged access review | Every 3 months (P-04) | System owner prepares; auditor checks and signs; Head of Cyber reviews the system owner's own memberships and checks the administrators | Signed review | PRO-AC-7 |
| Server and database account review | Every 6 months (P-52) | System owner, security officer | Signed review | PRO-AC-7 |
| All other access review | Every 12 months (P-05) | Data Owners | Signed review | PRO-AC-7 |
| Inactive members | Monthly | Security officer; the groups' owners | Members who have not signed in for 90 days removed from their groups, date recorded | PRO-AC-8 |
| Open exceptions | With each access review | System owner | Exceptions ended or renewed | PRO-AC-15 |
| Policy and procedures | Every 12 months, and after a change | System owner | Updated change record | PRO-AC-14 |
| Audit logs | Weekly | Auditor | Review record | \<Security Operating Procedures\> |

### AC.5 Procedures

Table AC-4 summarises each procedure: what starts it, who acts, its time limit, the record that proves it was followed, and the controls it serves. Records use the forms in \<Record Templates\>, or a ServiceNow record holding the same fields. Each procedure is walked through once on TPL-4 before go-live.

**Table AC-4: Procedure summary**

| Procedure | Starts when | Who acts | Time limit | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-AC-1 Joiner | Access is requested | The person, line manager, the group's owner (P-37), security officer | Training and signed \<Security Operating Procedures\> before the person is added to a group | ServiceNow request (TPL-2), TPL-9, TPL-21 and the register of signatures | AC-2, PL-4, PS-6, AT-2 |
| PRO-AC-2 Mover | A role changes | Line manager, the groups' owners | Notified within 1 working day (P-06) | ServiceNow request (TPL-2), TPL-14 | AC-2, PS-5 |
| PRO-AC-3 Leaver | The starters and leavers process prompts | \<Organisation\> disables the Active Directory account at once; the groups' owners | Within 5 working days (\<System Description\>, P-06) | TPL-14 | AC-2, AC-2(3), PS-4 |
| PRO-AC-4 Urgent disable | A concern is raised | Anyone, \<Organisation\>'s service desk, system owner | Within 1 hour (P-41) | TPL-14, and TPL-10 if it is an incident | AC-2(13), IR-6 |
| PRO-AC-5 Schema access | Access to a schema is requested, or the groups that open a schema are to change | The person, line manager, Data Owner, administrator | Before access or before the change | ServiceNow request (TPL-2); change record (TPL-6) for a change of groups | AC-2, AC-3, AC-5, AC-6 |
| PRO-AC-6 Privileged access | A privileged role is requested | The person, line manager, system owner | Role modules M1 and M2 (\<Awareness and Training Management\>) passed and signed Part B before access | ServiceNow request (TPL-2), TPL-9 | AC-2, AC-6(5), AT-3 |
| PRO-AC-7 Access review | The review falls due | The groups' owners, system owner, auditor, security officer, Head of Cyber | Every 3 months for the role groups, every 6 months for server and database accounts, every 12 months for schema groups (\<System Description\>, P-04, P-52 and P-05) | TPL-3 | AC-2, AC-6(7) |
| PRO-AC-8 Inactive accounts | Monthly | \<Organisation\>; security officer; the groups' owners | 90 days without signing in, for both the Active Directory account and \<System Name\>'s groups (P-38) | TPL-3 | AC-2(3) |
| PRO-AC-9 Locked account | A user asks | \<Organisation\>'s IT service desk | As P-42 sets | \<Organisation\>'s record | AC-7 |
| PRO-AC-10 Forgotten password | A user asks | \<Organisation\>'s IT service desk | After its identity check | \<Organisation\>'s record | IA-5 |
| PRO-AC-11 Ending access at once | A person's access must end at once | \<Organisation\>'s service desk; the groups' owners | At once; \<System Name\> refuses the person within 5 minutes | Note of the reason; TPL-10 if it is an incident | AC-2, AC-2(13) |
| PRO-AC-12 First administrator | \<System Name\> is first built | Windows server administrator, database administrator, system owner | At build | TPL-6 | AC-2, IA-5 |
| PRO-AC-13 Use notice | The wording changes | System owner, legal adviser, who approves the wording | Through an approved change | TPL-6 | AC-8 |
| PRO-AC-14 Policy and procedure review | The review falls due, or an event | System owner | Every 12 months (\<Policy\>, section 1.1) | Change record; TPL-4 | AC-1 |
| PRO-AC-15 Exception | A rule cannot be met | Requester, security officer, system owner or authorising official | End date no more than 12 months away | TPL-17; \<Risk List\> | AC-1, AC-20, AC-20(2), PL-4, CA-5 |
| PRO-AC-16 Sharing and export | Information must leave a schema | Requester, Data Owner, an editor of the schema | Before anything is shared | TPL-25, the sharing decision record | AC-21 |
| PRO-AC-17 Non-compliance | A gap is found | System owner, authorising official | As set in \<Risk List\> | \<Risk List\>; TPL-1 for an acceptance | CA-5, RA-7 |

#### PRO-AC-1 New user (joiner)

1. The person raises an access request in ServiceNow, naming the schemas and level needed, and the reason. **Manual**
2. Their line manager approves or refuses it. The owner of each group asked for then authorises or refuses it (P-37): the Data Owner for a schema's read or edit group, and the system owner for a role group. Nobody decides their own request. The ServiceNow workflow keeps the record. **Manual**
3. Before the person is added to any group, they complete security and privacy awareness training, receive the \<System Name\> briefing from the system owner (\<Awareness and Training Management\>, section 3.3), and sign Part A of \<Security Operating Procedures\>, and Part B if the access is privileged. The security officer records the training on TPL-9, and the system owner records the signature on TPL-21 and in the register of signatures (\<Planning Management\>, section 3.5). No access is given until this is done.
4. The owner who authorised the request adds the person to the approved AD groups, with \<Organisation\>'s AD tool. No \<System Name\> account is created: the person's Active Directory account is their account. **Manual**
5. The person signs in through PingFederate, and \<System Name\>'s API reads their groups from Active Directory over LDAPS.
6. The owner records the groups granted and the date in the ServiceNow request. **Manual**

#### PRO-AC-2 Role change (mover)

1. The line manager raises a change request in ServiceNow within the time in P-06. **Manual**
2. The approver in P-37 approves the new access in the ServiceNow approval workflow.
3. Each group's owner removes the old membership and adds any new one in Active Directory. The change takes effect within 5 minutes, because \<System Name\>'s API reads the person's groups on every request (\<System Description\>, section 7.2). No sign-in needs to be ended. **Manual**

#### PRO-AC-3 Leaver

1. \<Organisation\> disables the person's Active Directory account at once, which stops them signing in, and \<System Name\>'s API refuses the disabled account within 5 minutes, even if a session is open. The starters and leavers process prompts the owners of the groups the person belongs to. **Manual**
2. Each owner removes the person from their AD group within the time in P-06. **Manual**
3. The owner records the date in the ServiceNow request and on TPL-14. No session needs to be ended by hand: the API's refusal of the disabled account ends it.

#### PRO-AC-4 Urgent disable (high-risk individual)

1. Whoever raises the concern tells the system owner and \<Organisation\>'s service desk.
2. Within the time in P-41, \<Organisation\>'s service desk disables the person's Active Directory account, and ends their PingFederate sign-in so that they cannot start a new one. **Manual**
3. The system owner confirms with the service desk that the account is disabled, and, after 5 minutes, checks \<System Name\>'s audit log or asks the auditor to confirm that the person's requests are being refused.
4. The system owner records the reason and informs anyone who needs to know.

#### PRO-AC-5 Schema access

1. Each schema names one read group and one edit group on its schema definition, which an Administrator sets in the Admin application. A change to them needs a change record (TPL-6) approved by the schema's Data Owner. The administrator enters the record's reference with the change; the change is audited and raises an alert to the security officer (U9). Deactivating, reactivating or deleting a schema follows the same rule. Only an empty schema can be deleted; a schema that still holds items is deactivated, and its items leave only by disposal (\<System Description\>, FR-060, FR-074). **Manual**
2. The person asks for the access in the ServiceNow workflow. Their line manager approves it, and the schema's Data Owner, as owner of the schema's data and its two groups, authorises it. **Manual**
3. The Data Owner adds the person to the schema's read group or edit group in Active Directory, with \<Organisation\>'s AD tool. **Manual**

The API compares the group names on the schema definition with the person's Active Directory groups, which it reads from Active Directory over LDAPS on every request, holding each answer for at most 5 minutes. A schema with no group is closed to everyone, administrators included.

#### PRO-AC-6 Privileged access

1. The person asks for the role in the ServiceNow workflow. Their line manager approves it, and the system owner authorises any membership of the five role groups: \<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners and \<Code\>\_LegalSearch. Only the person the legal adviser names is added to \<Code\>\_LegalSearch, and they hold no other role. The system owner cannot authorise their own. **Manual**
2. The system owner adds the person to the AD group. **Manual**
3. The system owner records the change in the ServiceNow request. **Manual**

#### PRO-AC-7 Access review

1. At the intervals in P-04, P-05 and P-52, each group's owner lists its members from Active Directory. For server and database accounts, the system owner obtains \<Organisation\>'s export of the Windows administrator groups on both servers (EV-AC-02) and the database administrator's list of SQL Server logins and their roles. **Manual**
2. The owner checks each member against the ServiceNow requests, removes anyone who no longer needs the access, and checks that no privileged account is in a schema group (P-45). For server and database accounts, the system owner and the security officer check each against \<Roles and Responsibilities\> and the approved change records, and have anything not needed removed.
3. The result is recorded on TPL-3. A Data Owner signs the review of their schema's groups. For the role groups, the system owner prepares the review and the auditor checks and signs it. The system owner and the security officer sign the server and database review.
4. The Head of Cyber reviews any role-group membership the system owner holds, and checks the administrators' membership, each quarter, and signs TPL-3 for that part. Nobody signs off their own access.

#### PRO-AC-8 Inactive accounts

1. \<Organisation\> disables Active Directory accounts unused for 90 days within 1 working day (P-38).
2. Each month, the security officer runs the last sign-in report in the Admin application (\<System Description\>, FR-085), lists the members of each \<System Name\> group who have not signed in for 90 days, and sends each owner their list. **Manual**
3. The owner removes those members from the group, unless the person is on leave and still needs the access, and records the date on TPL-3. **Manual**

#### PRO-AC-9 Locked account

1. PingFederate and Active Directory lock an account after repeated failed sign-ins, and release it, as P-42 sets: 10 failed attempts in 15 minutes lock the account for 15 minutes. \<System Name\> has no lock of its own.
2. A user who is locked out asks \<Organisation\>'s IT service desk, which checks who they are. **Manual**

#### PRO-AC-10 Forgotten password

1. The user asks \<Organisation\>'s IT service desk, which checks who they are and resets their Active Directory password. \<System Name\> holds no passwords. **Manual**

#### PRO-AC-11 Ending access at once

1. \<Organisation\>'s service desk disables the person's Active Directory account, or the group's owner removes the membership. \<System Name\>'s API refuses the person within 5 minutes, which ends any open session. The service desk may also end the person's PingFederate sign-in, so that they cannot start a new one. **Manual**
2. Whoever asked for it records why. **Manual**

#### PRO-AC-12 First administrator on a new installation

1. No first administrator account is created, because \<System Name\> holds no accounts and its database has no account or password table. The database administrator creates a SQL Server login for the API's group managed service account, using Windows authentication, so no database password is set.
2. At build, the Windows server administrator configures \<System Name\>'s PingFederate connection, as an OpenID Connect client of \<Organisation\>'s PingFederate, allows the application server alone to reach PingFederate over HTTPS on TCP 443 for its metadata, its signing certificate and each sign-in (F10), and records it on TPL-6. **Manual**
3. The Windows server administrator places the OpenID Connect client credential in the key store, readable only by the UI and Admin applications' service accounts. **Manual**
4. The system owner adds the first Administrator to the \<Code\>\_Admins group in Active Directory. There is one Administrator role and no separate global administrator, and it opens no item content. **Manual**

#### PRO-AC-13 Changing the system use notice

The legal adviser and the system owner approve the wording, and a change request updates the system use notice page of the UI application and the Admin application. The page is shown after the person signs in through PingFederate, and nothing else is served until they accept it; the acceptance is written to the audit log.

#### PRO-AC-14 Policy and procedure review

1. At the intervals in \<Policy\>, section 1.1, the system owner reviews both documents.
2. They record the result in each document's change record and update \<Plan of Action and Milestones\>.

#### PRO-AC-15 Exception management

1. The person who needs the exception writes down the rule, reason, duration and any compensating check, and sends it to the system owner. **Manual**
2. The system owner assesses the risk, and sends it to the authorising official if it is above their authority.
3. If it is approved, the system owner sets an end date under the rules in \<Access Control Management\> and adds it to \<Risk List\>.
4. The role concerned makes the change and records it.
5. The system owner checks open exceptions at each access review. On the end date the exception ends and access returns to the normal rule, unless it is renewed through these same steps.

#### PRO-AC-16 Sharing and export requests

1. The requester names the items, recipient and reason. **Manual**
2. The schema's Data Owner checks that the recipient is authorised for that information, and approves or refuses it on TPL-25. **Manual**
3. If approved, an editor of the schema exports the items as a download and delivers them by an approved route.
4. The editor records the date and what was sent on the same TPL-25. **Manual**

Copying \<System Name\> data to portable storage or an external system is not a sharing decision: it is an exception, approved by the system owner on TPL-17 (PRO-AC-15).

#### PRO-AC-17 Non-compliance and risk decisions

1. Whoever finds a non-compliance, whether through an assessment, a review, a test or an incident, reports it to the system owner.
2. The system owner records it in \<Risk List\>, section 5, and rates the risk by the method in \<Risk List\>, section 4.
3. The system owner proposes a treatment: accept, remediate, approve, evidence or tailor.
4. The system owner decides Low risks. The authorising official decides Medium and High risks.
5. **If accepted:** the decision maker records the reason, any compensating measure, the name, the date and the review date in \<Risk List\>, section 3. The non-compliance remains in place.
6. **If remediated:** the system owner adds an item to \<Plan of Action and Milestones\> with a milestone, a resource and a date. The fix follows that plan. It does not start until this decision is made, unless the authorising official directs urgent action.
7. **If approved, evidenced or tailored:** the system owner records the value in \<Access Control Management\>, the evidence request in \<Evidence Requests\>, or the rationale in \<Tailoring Register\>.
8. The system owner reviews accepted risks at the interval in \<Risk List\>, and sooner if the system or the threat changes. A risk that has become too high goes back to step 4.

## AT Awareness and Training

Procedures PRO-AT-1 to PRO-AT-5.

### AT.1 Purpose

These procedures carry out \<Policy\> (AT). Steps marked **Manual** rely on people. The curriculum, briefing outline, training matrix, measures and register are in \<Awareness and Training Management\>.

**Table AT-1: Procedures at a glance**

| Procedure | When | Who | Record | Controls |
| --- | --- | --- | --- | --- |
| PRO-AT-1 Awareness and the \<System Name\> briefing | Before access, and every 12 months | System owner, everyone | TPL-9; TPL-21 | AT-2, AT-2(2), AT-2(3), PL-4 |
| PRO-AT-2 Role training | Before privileged access, or within 30 days for incident and contingency modules; then every 12 months | Security officer, Head of Cyber | TPL-9 | AT-3, AT-3(5), IR-2, CP-3 |
| PRO-AT-3 Keeping content current | Every 12 months, and after a significant incident, exercise or change | Security officer, legal adviser | TPL-6 change record | AT-2c, AT-2d, AT-3b, AT-3c |
| PRO-AT-4 Records and the register | At each completion, and before a role is granted | Security officer, system owner | TPL-9; training register | AT-4, AC-2 |
| PRO-AT-5 Measures and checking | Monthly, and at each review | Security officer, system owner | TPL-8 monthly measures; Test-PlanConsistency.ps1 | AT-1, AT-2, AT-3, CA-7 |

### AT.2 Procedures

#### PRO-AT-1 Awareness and the \<System Name\> briefing

1. Before a person is given access, they complete \<Organisation\>'s security and privacy awareness course. **Manual** (EV-AT-01)
2. The system owner gives the \<System Name\> briefing (\<Awareness and Training Management\>, section 3.3), and the user passes its short check. **Manual**
3. The user signs \<Security Operating Procedures\> Part A, and Part B if privileged, on TPL-21. **Manual**
4. The security officer records the course, briefing and check on TPL-9, and every 12 months asks each user to repeat them. **Manual**
5. Between courses, the security officer sends a quarterly \<System Name\> security note, built from recent advisories and reports. **Manual**

#### PRO-AT-2 Role training

1. When a role is requested, the system owner looks up its modules in the training matrix (\<Awareness and Training Management\>, section 3.5). **Manual**
2. The person completes the role modules before privileged access is granted, and the incident response and contingency modules within 30 days of taking the role. **Manual**
3. The security officer delivers the modules, and the Head of Cyber delivers them to the security officer and auditor. Each ends with a check, with a pass mark of 80%; anyone below it repeats the module. **Manual**
4. \<Organisation\>'s administrators complete the \<System Name\> modules for their role. \<Organisation\> evidences any general administrator training. **Manual** (EV-AT-01)

#### PRO-AT-3 Keeping content current

1. Every 12 months, the security officer reviews the briefing and each module against the curriculum, recent incidents, exercise reports (TPL-11) and changes. **Manual**
2. After a significant incident, exercise or change, the lesson is added within 30 days. **Manual**
3. The legal adviser reviews the privacy content. Each change is recorded on TPL-6, and the content version goes up. **Manual**

#### PRO-AT-4 Records and the register

1. The security officer records each completion on TPL-9: the content version, the check result and the next due date. **Manual**
2. The security officer adds it to the training register (\<Awareness and Training Management\>, section 3.8). **Manual**
3. Before granting a role, the system owner confirms in the register that its required modules are complete (\<Procedures\>, PRO-AC-6). **Manual**
4. Records are kept for 3 years, as in \<System Name\>'s retention schedule (\<PII Processing Management\>, section 3.7). \<Organisation\> keeps its course records, and provides them on request. **Manual**

#### PRO-AT-5 Measures and checking

1. Each month, the security officer reports the measures in \<Awareness and Training Management\>, section 3.9, with the CA-7 measures on TPL-8. **Manual**
2. Anyone overdue is reminded. Anyone overdue by more than 30 days has privileged access suspended until complete. **Manual**
3. At each review, the system owner runs Test-PlanConsistency.ps1. Check L14 confirms that every security role has its training defined in the matrix. **Manual**
4. No phishing simulation is run unless HR and the legal adviser have agreed it (\<Policy\> (AT), R8). **Manual**

## AU Audit and Accountability

Procedures PRO-AU-1 to PRO-AU-7.

### AU.1 Purpose

These procedures define how audit records are reviewed, protected and retained. The values they use are in \<Audit and Accountability Management\>. Steps marked **Manual** have no support in the system.

### AU.2 Procedure summary

**Table AU-1: Procedure summary**

| Procedure | Activity | How often | Who | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-AU-1 | Review audit records | Weekly | Auditor | TPL-8 Monitoring and integrity report | AU-6, AU-6(1), AU-6(3), AU-7 |
| PRO-AU-2 | Check the audit chain, and respond to suspected tampering | Weekly, and on any alert | Auditor, security officer | TPL-8; incident record | AU-9, AU-9(4) |
| PRO-AU-3 | Respond to a logging failure | On any alert | Windows server administrator, security officer | TPL-8; incident record | AU-5 |
| PRO-AU-4 | Check capacity, retention, the archive and time synchronisation | Monthly | Database administrator, Windows server administrator | TPL-8 | AU-4, AU-8, AU-11 |
| PRO-AU-5 | Review and change the logged events | Every 12 months, and on change | System owner | Updated \<Audit and Accountability Management\>; \<Decision Register\> | AU-2, AU-12 |
| PRO-AU-6 | Give or remove auditor access | On request, and at each quarterly access review | System owner | ServiceNow request; access review record | AU-9(4), AC-2 |
| PRO-AU-7 | Handle the application log | Monthly check | Windows server administrator | TPL-8 | AU-9, AU-11, PT-3 |

### AU.3 Procedures

#### PRO-AU-1 Weekly review

1. The auditor opens the audit log page in the Admin application and filters by date. **Manual**
2. They follow the audit review procedure in \<Security Operating Procedures\>, section 4.2, including its list of unusual activity.
3. They compare changes to schemas and to the AD groups each uses, and \<Organisation\>'s record of changes to the members of \<System Name\>'s groups, with the approved ServiceNow requests, and compare the audit log with the server, database, PingFederate and Active Directory records. **Manual**
4. They report anything suspicious to the security officer, and record the date, period, reviewer and result on TPL-8, Monitoring and integrity report, in \<Record Templates\>. **Manual**
5. If risk rises, for example after an incident or new threat information, the system owner increases how often or how closely records are reviewed. **Manual**

#### PRO-AU-2 Audit chain check

1. The auditor runs the audit chain check.
2. If the chain is broken, or tampering is suspected for any other reason, they alert the security officer and raise a security incident.
3. Before anything is restored or changed, the auditor preserves the evidence: a copy of the audit table and the hash of its newest record, kept where administrators cannot change it, with the copy's own SHA-256 hash recorded on TPL-8. **Manual**
4. The security officer handles the incident under PRO-IR-2.

#### PRO-AU-3 Logging failure

1. The Windows server administrator and security officer are alerted within 1 hour.
2. The system keeps running. The Windows server administrator and database administrator find the cause and restore logging.
3. The security officer records the period without records and tells the system owner.
4. If records may have been lost or changed, the evidence is preserved as in PRO-AU-2, step 3, and the incident is handled under PRO-IR-2.

#### PRO-AU-4 Capacity and retention

1. Each month the database administrator checks the free space and the size of the audit table. **Manual**
2. They raise more storage before records are at risk.
3. Records older than 12 months are moved to an offline archive, and the archive's SHA-256 hash is recorded on TPL-8. Archived records older than 24 months may be deleted only with the system owner's recorded approval. **Manual** Records under a legal hold notified by the legal adviser, or held as incident evidence, are not deleted until released.
4. Each month the Windows server administrator checks that both VMs are within 1 second of UTC from \<Organisation\>'s time source, \[Organisation time source\], and reports any drift over 5 seconds to the security officer. The result is recorded on TPL-8. **Manual**

#### PRO-AU-5 Changing the logged events

1. The system owner decides on any change to the logged events, and reviews the list every 12 months. **Manual**
2. Developers make the change through the normal release process, because the events are built into each release. The list of events is \<Audit and Accountability Management\>, Table 2, and it is changed there first.

#### PRO-AU-6 Auditor access

1. Auditor access is requested through ServiceNow, approved by the line manager and authorised by the system owner (\<Access Control Management\>, section 3.13). An auditor must not hold the Administrator role or any other administration role. **Manual**
2. The system owner, who owns the AD group \<Code\>\_Auditors, adds the person to it and records the change against the ServiceNow request.
3. Auditor access is removed when the person changes role or leaves, under \<Security Operating Procedures\>, section 4.4.
4. The system owner confirms the list of auditors at each quarterly access review. **Manual**

#### PRO-AU-7 Application log

1. The application logs on the VMs hold no audit details, personal data or sign-in identifiers. On the VMs only the server administrators may read them. The security officer reviews them in central logging. **Manual**
2. Application logs are kept for 30 days and then deleted. **Manual**
3. They are forwarded to \<Organisation\>'s central logging, and are not otherwise copied off the VMs, except as incident evidence under PRO-AU-2, step 3.
4. Each month the Windows server administrator checks who can read the logs and how old they are, and records the result on TPL-8. **Manual**

## CA Assessment, Authorization, and Monitoring

Procedures PRO-CA-1 to PRO-CA-7.

### CA.1 Purpose

These procedures carry out \<Policy\> (CA). Steps marked **Manual** have no system support and rely on people.

**Table CA-1: Procedure summary**

| Procedure | Activity | How often | Who | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-CA-1 | Plan, carry out and report an assessment | Every 12 months, and after a significant change | System owner, security assessor, authorising official | Approved plan; TPL-19; \<Security Assessment Report\> | CA-2, CA-2(1) |
| PRO-CA-2 | Approve, review and end connections | Before each connection; every 12 months; when ended | System owner, Windows server administrator | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 | CA-3, CA-9 |
| PRO-CA-3 | Keep the plan of action up to date | Monthly; overdue items quarterly | System owner | \<Plan of Action and Milestones\> change record | CA-5 |
| PRO-CA-4 | Authorise and re-authorise | Before operation; every 12 months; after a significant change | System owner, authorising official | TPL-18 | CA-6 |
| PRO-CA-5 | Monitor and report | Monthly to the system owner; quarterly to the authorising official; yearly independent check | Security officer, system owner, security assessor | TPL-8; TPL-19 | CA-7, CA-7(1), CA-7(4) |
| PRO-CA-6 | Decide whether a change is significant | Each change | System owner, security officer, authorising official | TPL-6; TPL-18 | CA-6, CA-7 |
| PRO-CA-7 | List and accept inherited controls | Before operation; every 12 months | System owner, authorising official, \<Organisation\> | \<Assessment, Authorization, and Monitoring Management\>, section 3.6; TPL-18 | CA-6 |

### CA.2 Procedures

#### PRO-CA-1 Assessing controls

1. Every 12 months the system owner agrees the assessment plan with the assessor, and the authorising official approves it. **Manual**
2. The assessor confirms on TPL-19 that they have had no part in building or running \<System Name\>. **Manual**
3. The assessor assesses the controls, records the results in each family assessment and brings them together in the Security Assessment Report, \<Security Assessment Report\>, which goes to the system owner, authorising official and Head of Cyber. **Manual**

#### PRO-CA-2 Managing connections

1. Before any new connection, the system owner records it in \<Assessment, Authorization, and Monitoring Management\> with its interface, security needs, privacy needs, information, responsibilities, the agreement type under CSS and its review date, and approves it. **Manual**
2. Every 12 months the system owner and the other system's owner review each connection, and end any no longer needed. **Manual**
3. When a connection is no longer needed, or a VM is rebuilt, the Windows server administrator removes it, the system owner records the end date in \<Assessment, Authorization, and Monitoring Management\>, section 3.7, and the other system's owner is told. **Manual**

#### PRO-CA-3 Keeping the plan up to date

1. Each month the system owner updates \<Plan of Action and Milestones\> from assessments, monitoring and audits. **Manual**
2. Once the development phase is scheduled, each open item gets a calendar date within the time limit for its rating in \<Policy\>, section CA.4. **Manual**
3. An item is closed only when the fix has been tested, the evidence is recorded against the item, and the system owner agrees. Items fixed in the test environment are re-tested on the production VMs before they close. **Manual**
4. Each quarter the system owner reports overdue items, and the reason for each, to the authorising official. **Manual**

#### PRO-CA-4 Authorising

1. Before \<System Name\> holds real data, the system owner gives the authorising official the authorisation package listed in \<Assessment, Authorization, and Monitoring Management\>, section 3.5. **Manual**
2. The authorising official decides whether to authorise, accepts the remaining risk by name, and records the decision on TPL-18, with its terms, conditions and end date. **Manual**
3. Every 12 months, and after a significant change, the authorising official reviews the authorisation. **Manual**

#### PRO-CA-5 Monitoring

1. Each month the security officer collects the measures in \<Assessment, Authorization, and Monitoring Management\>, section 3.8, reads them together with the audit review findings, the vulnerability results and the incident records, and looks for a trend across three months. They report on TPL-8 to the system owner, act on any measure past its threshold, and record the action. A measure not put right in the month becomes an item in \<Plan of Action and Milestones\>. **Manual**
2. Each quarter the system owner reports the same measures, and any change in risk, to the authorising official. **Manual**
3. Each year an independent assessor, who has completed TPL-19, checks a sample of the monitoring. **Manual**

#### PRO-CA-6 Deciding whether a change is significant

1. Every change is recorded on TPL-6, and the system owner checks it against the list of significant changes in \<Assessment, Authorization, and Monitoring Management\>, section 3.9. **Manual**
2. If it is significant, the security officer assesses its effect on security and privacy before it is made. **Manual**
3. The authorising official decides whether \<System Name\> must be re-assessed or re-authorised, and records the decision on TPL-18. **Manual**

#### PRO-CA-7 Inherited controls

1. The system owner keeps the list of controls inherited from \<Organisation\> in \<Assessment, Authorization, and Monitoring Management\>, section 3.6, and requests \<Organisation\>'s evidence for them (\<Evidence Requests\>). **Manual**
2. Before \<System Name\> operates, the authorising official accepts the inherited controls on TPL-18, or records which are not accepted. **Manual**
3. Every 12 months the system owner reviews the list with \<Organisation\>'s security contact. **Manual**

## CM Configuration Management

Procedures PRO-CM-1 to PRO-CM-9.

### CM.1 Purpose

These procedures define how \<System Name\>'s configuration is changed and recorded. The values are in \<Configuration Management\>. Steps marked **Manual** have no support in the system.

**Table CM-1: Procedure summary**

| Procedure | Activity | How often | Who | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-CM-1 | Make a change | Each change | Requester, security officer, change control board, developers or administrators | TPL-6, or the ServiceNow change | CM-3, CM-3(2), CM-3(4), CM-4, CM-4(2), CM-5 |
| PRO-CM-2 | Review the baseline and keep previous versions | Every 12 months and each release | System owner, Windows server administrator | TPL-6; the configuration library | CM-2, CM-2(2), CM-2(3) |
| PRO-CM-3 | Apply secure settings | When built, and each change | Windows server, database administrators, developers | TPL-6 for each exception | CM-6 |
| PRO-CM-4 | Approve software and components | On request, and every 12 months | System owner, Windows server administrator, developers | TPL-7; \<Configuration Management\>, section 3.5 | CM-7(2), CM-7(5), CM-8, CM-11 |
| PRO-CM-5 | Review functions, ports and services | Every 12 months | Windows server administrator, developers | TPL-3 | CM-7, CM-7(1) |
| PRO-CM-6 | Deal with unauthorised components | On any alert | Windows server administrator, security officer | TPL-8 | CM-8(3) |
| PRO-CM-7 | Monitor for drift | Monthly | Windows server and database administrators | TPL-8 | CM-2, CM-6, CA-7 |
| PRO-CM-8 | Make an emergency change | When needed | System owner or deputy, change control board | TPL-6 within 1 working day | CM-3 |
| PRO-CM-9 | Review licences | Each release, and every 12 months | Developers, system owner | \<Configuration Management\>, section 3.5; \<Decision Register\> | CM-10 |

### CM.2 Procedures

#### PRO-CM-1 Making a change

1. Whoever needs the change raises a ServiceNow change request, or TPL-6, stating the reason.
2. The security officer assesses the security and privacy impact against the criteria in \<Configuration Management\>, section 3.9, including the significant change test in \<Assessment, Authorization, and Monitoring Management\>, section 3.9, and records it on the change. A significant change goes to the authorising official before it is made. **Manual**
3. The system owner, security officer and Windows server administrator approve or refuse it in ServiceNow, as the change control board under its charter in \<Configuration Management\>, section 3.8.
4. Developers or administrators make the change, and test it before release, using the test scripts where they apply. **Manual**
5. They check that the affected controls still work, and record the result. **Manual**
6. They update the baseline and component inventory in \<Configuration Management\>, sections 3.4 and 3.5, tag the release, record the checksum of each package and produce the bill of materials. They update \<System Security Plan\>, section 3.4, if a server changed. **Manual**

#### PRO-CM-2 Reviewing the baseline

1. Every 12 months and at each release, the system owner and Windows server administrator review the baseline. **Manual**
2. They keep the 3 previous configurations, each as its tagged code, package checksums, settings and bill of materials, in the configuration library (\<Configuration Management\>, section 3.13). **Manual**

#### PRO-CM-3 Secure settings

1. The Windows server administrator and database administrator apply the CIS Benchmarks when the VMs are built, and developers apply the application and hosting settings in \<Configuration Management\>, section 3.6.
2. They record each exception on TPL-6, with a reason, and the system owner approves it. **Manual**

#### PRO-CM-4 Software

1. The Windows server administrator keeps the approved software list and reviews it every 12 months. **Manual**
2. A user who needs software on a VM raises a ServiceNow request, and the system owner approves or refuses it. **Manual**
3. Before a new package, browser library or runtime enters the baseline, the developer records its supplier, version, licence and purpose in \<Configuration Management\>, section 3.5, and checks it on TPL-7 for known vulnerabilities. A licence that is not a standard open source licence goes to the system owner for a decision on \<Decision Register\>. **Manual**

#### PRO-CM-5 Reviewing functions and ports

1. Every 12 months the Windows server administrator and developers review functions, ports, protocols, software and services, and remove what is not needed, including packages the code does not use. The result is recorded on TPL-3. **Manual**

#### PRO-CM-6 Unauthorised components

1. \<Organisation\>'s tools check monthly and alert the Windows server administrator.
2. The Windows server administrator removes the component or disables its network access, tells the security officer, and records it on TPL-8. **Manual**

#### PRO-CM-7 Monitoring for drift

1. Each month the Windows server administrator scans both VMs against the CIS Benchmarks with CIS-CAT or an equivalent tool, and runs Test-ConfigurationManagement.ps1.
2. The database administrator compares the SQL Server settings with the baseline. **Manual**
3. Any difference from \<Configuration Management\>, sections 3.4 to 3.6, is reported to the security officer on TPL-8. **Manual**
4. The difference is put back, or raised as a change under PRO-CM-1 if it should stay. **Manual**

#### PRO-CM-8 Emergency change

1. An emergency change is allowed only to stop or limit an incident or an outage. **Manual**
2. The system owner, or their deputy, approves it by phone or in person before it is made. **Manual**
3. It is recorded on TPL-6 within 1 working day, with the impact analysis done after the event. **Manual**
4. The change control board reviews it at its next meeting, and confirms or reverses it. **Manual**

#### PRO-CM-9 Licence review

1. At each release, the developer checks that every component in \<Configuration Management\>, section 3.5, still has the licence recorded there. **Manual**
2. Every 12 months, the system owner confirms that each licence decision on \<Decision Register\> still applies. **Manual**
3. A component whose licence no longer permits \<System Name\>'s use is replaced, or licensed, through PRO-CM-1. **Manual**

## CP Contingency Planning

Procedures PRO-CP-1 to PRO-CP-7.

### CP.1 Purpose

These procedures carry out \<Policy\> (CP) and \<Contingency Planning Management\>. Steps marked **Manual** have no system support and rely on people.

**Table CP-1: Procedures at a glance**

| Procedure | What it does | When | Who | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-CP-1 | Taking backups | Daily, weekly and at each change | Database and Windows server administrators | Backup job log; TPL-8 | CP-9, CP-9(8), CP-10(2) |
| PRO-CP-2 | Testing a restore | Every 6 months, and after a change to the database or backups | Database administrator, observed by the security officer | TPL-11 | CP-9(1) |
| PRO-CP-3 | Recovering | When the plan is invoked | Administrators, security officer | Activity log; TPL-11 | CP-7, CP-10, CP-10(2) |
| PRO-CP-4 | Training and testing | Training within 30 days and yearly; tests as \<Contingency Planning Management\>, section 3.10 | System owner, security officer | TPL-9; TPL-11 after-action report | CP-3, CP-4, CP-4(1) |
| PRO-CP-5 | Activation and notification | On a failure | Anyone; system owner decides | Activity log | CP-2 |
| PRO-CP-6 | Reconstitution and deactivation | After recovery, before users return | Administrators, security officer, system owner | Activity log; TPL-11 | CP-10 |
| PRO-CP-7 | Maintaining and sharing the plan | Every 12 months, and after a test, activation or change | System owner | Change record; distribution record | CP-2, CP-2(1) |

### CP.2 Procedures

#### PRO-CP-1 Taking backups

1. The database administrator takes a full, encrypted backup of the database every day, which includes every item, stored file and audit record, and sends it to the second site.
2. SQL Server's transaction log is backed up between full backups, encrypted, and copied to the second site.
3. The Windows server administrator backs up each VM's system configuration weekly, encrypted.
4. Copies are kept as \<Contingency Planning Management\>, section 3.8: 14 daily, 8 weekly and 12 monthly, and one copy is offline or immutable.
5. The backup encryption key and the protected copy of the secrets are held apart from the backups, and only the system owner and administrators can reach them.
6. A failed backup alerts the database administrator and the security officer, who fix it within 1 working day.
7. The system owner copies changed documentation to the controlled library. **Manual**
8. Each week the database administrator checks every backup job succeeded, and records it on TPL-8 (\\<Security Operating Procedures\\>, C8). **Manual**

#### PRO-CP-2 Testing a restore

1. Before the backup to be tested is taken, the database administrator exports the row counts of every table and the audit records' identifiers and stored hashes. **Manual**
2. They restore that backup, and its transaction logs, to a separate server with no network access to production.
3. They check that every table has the same row count, every stored file matches its stored SHA-256 checksum, and the audit records and stored hashes match the export. Test-BackupRestore.ps1 makes these checks. **Manual**
4. They record the time taken and the newest record restored, against the recovery time and point objectives, on TPL-11, then remove the test server. **Manual**
5. They also run the audit chain check on the restored records. **Manual**

#### PRO-CP-3 Recovering

1. The Windows server administrator confirms with \<Organisation\> that the site, network and services are available, at the second site if the main one is lost. **Manual**
2. They rebuild the database VM to the baseline in \<Configuration Management\>, sections 3.4 and 3.6. **Manual**
3. The database administrator restores the latest good backup and applies the archived transaction logs to the last consistent point. If a backup fails the checks in PRO-CP-2, they use the one before it.
4. The Windows server administrator restores the secrets from their protected copy, and changes them if a compromise is suspected. **Manual**
5. They rebuild the application VM from the tagged release, and start API, then UI application, then Admin application. **Manual**
6. If the database is not restored 48 hours after the plan was invoked, the system owner tells the authorising official. **Manual**

#### PRO-CP-4 Training and testing

1. The system owner trains each person with a contingency role within 30 days of taking it and every 12 months, using the content in \<Contingency Planning Management\>, section 3.10, and records it on TPL-9 and in the training register (\<Awareness and Training Management\>, section 3.8). This is module M8 in the training matrix (\<Awareness and Training Management\>, section 3.5), with its 80% check. **Manual**
2. The system owner reviews the training content every 12 months, and after a plan change, test or activation. **Manual**
3. The system owner and security officer run the restore test and tabletop exercise in \<Contingency Planning Management\>, section 3.10, with objectives and a scenario set beforehand. The tabletop is held with the incident response plan. **Manual**
4. Within 10 working days of each test or activation, the security officer writes an after-action report on TPL-11: objectives, what happened, time and data lost against the objectives, problems, actions with owners and dates, and plan changes. **Manual**
5. Actions that need a fix go to \<Plan of Action and Milestones\>. **Manual**

#### PRO-CP-5 Activation and notification

1. Whoever finds a failure tells \<Organisation\>'s IT service desk and the security officer. **Manual**
2. Within 4 hours the database and Windows server administrators assess the outage: cause, damage, expected duration, possible data loss and whether it may be a security incident. If it may be, the security officer starts the incident response plan. **Manual**
3. The system owner, or their deputy, invokes \<Contingency Planning Management\> if any criterion in its section 5.1 is met, and records the decision and time. **Manual**
4. The system owner tells the people in \<Contingency Planning Management\>, section 3.4, and \<Organisation\>'s IT service desk, by phone and then in writing, using its contact list (appendix A). **Manual**
5. The system owner tells users through \<Organisation\>'s usual staff channel, and updates them at least daily. **Manual**
6. The security officer keeps an activity log of decisions and actions, with times, until deactivation. **Manual**

#### PRO-CP-6 Reconstitution and deactivation

1. The database administrator runs the checks in PRO-CP-2, step 3, on the recovered database, and records the newest record restored. **Manual**
2. The administrators test the functions: sign in, find and read an item, upload and remove a test item in a test schema, and sign in to the Admin application, checking that each writes an audit record. **Manual**
3. The security officer confirms that the controls match the main site, including encryption in transit, the members of \<System Name\>'s groups against current staff, and audit logging. **Manual**
4. The system owner declares recovery, and tells users and the people in \<Contingency Planning Management\>, section 3.4. **Manual**
5. The database administrator takes a full backup at once, and confirms it reached the second site.
6. Temporary access is removed. A return from the second site to the main site is made as a planned change under \<Configuration Management\>. **Manual**
7. The system owner closes the activation, and the after-action report follows PRO-CP-4, step 4. **Manual**

#### PRO-CP-7 Maintaining and sharing the plan

1. The system owner reviews \<Contingency Planning Management\> every 12 months, and after a test, activation or significant change, with the authorising official. **Manual**
2. They check it still agrees with the incident response plan and \<Organisation\>'s plans in its appendix B. **Manual**
3. Once approved, they send the plan to the people in its section 1.1, tell them what changed, and record who received it. **Manual**
4. They make sure the offline copies held by the system owner and security officer are current. **Manual**

## IA Identification and Authentication

Procedures PRO-IA-1 to PRO-IA-8.

### IA.1 Purpose

These procedures define how identifiers and authenticators are issued, changed and protected. They carry out \<Policy\> (IA) and build on \<Procedures\> (AC), whose PRO-AC-1, PRO-AC-9 and PRO-AC-10 cover new users, locked accounts and forgotten passwords. The values and the authenticator inventory are in \<Identification and Authentication Management\>. Steps marked **Manual** have no support in the system.

**Table IA-1: Procedures at a glance**

| Procedure | What it does | When | Who | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-IA-1 | Identifiers | Each new person | \<Organisation\>; the group's owner | ServiceNow request | IA-2, IA-4, IA-4(4), IA-12 |
| PRO-IA-2 | Passwords | Each new Active Directory account and reset | \<Organisation\>'s IT service desk | \<Organisation\>'s record | IA-5 |
| PRO-IA-3 | Suspected compromise, role change, or a lost or stolen authenticator | When it happens | The person; \<Organisation\>'s service desk; security officer | ServiceNow request; incident record if needed | IA-5, IR-6 |
| PRO-IA-4 | Changing service secrets and the signing key | Every 12 months, and when an administrator leaves | Windows server administrator | TPL-6 | IA-5, IA-5(6) |
| PRO-IA-5 | Password rules | Not done in \<System Name\> | \<Organisation\> | None | IA-5(1) |
| PRO-IA-6 | Enrolling and resetting a second factor | When the person first uses PingFederate; on loss | The person; \<Organisation\>'s service desk | \<Organisation\>'s record | IA-2(1), IA-2(2) |
| PRO-IA-7 | Reviewing authenticators and assurance levels | Every 12 months, and after a significant change | System owner, security officer | \<Identification and Authentication Management\> change record | IA-5, IA-12 |
| PRO-IA-8 | Disabling unused identifiers | Under \<Organisation\>'s standard | \<Organisation\> | \<Organisation\>'s record | AC-2(3), IA-4 |

### IA.2 Procedures

#### PRO-IA-1 Identifiers

1. A person's Active Directory account is their identifier. \<Organisation\> issues it after its pre-employment checks have proved who the person is. \<System Name\> issues no identifiers. **Manual**
2. The ServiceNow approval in PRO-AC-1 authorises the person's membership of a \<System Name\> group: the system owner for privileged roles, and the Data Owner for schema access.
3. Staff or contractor status is shown by \<Organisation\>'s directory.
4. An identifier is never reused. This is \<Organisation\>'s rule, and is to be evidenced. **Manual**

#### PRO-IA-2 Passwords

1. \<System Name\> issues no passwords, temporary or otherwise. Every user signs in through PingFederate with their Active Directory account.
2. \<Organisation\>'s IT service desk issues and resets Active Directory passwords under its own procedure, after checking who the person is. **Manual**

#### PRO-IA-3 Suspected compromise, role change, or a lost or stolen authenticator

1. The person, or whoever notices, tells \<Organisation\>'s IT service desk and the security officer straight away. This includes a password written down or seen, and a lost phone or key used as a second factor. **Manual**
2. The service desk resets the password or the second factor, and ends the person's PingFederate sign-in. **Manual**
3. The security officer decides whether this is a security incident, and if so raises it under \<Procedures\> (IR). **Manual**

#### PRO-IA-4 Changing service secrets and the signing key

1. Every 12 months, and when an administrator leaves, the Windows server administrator changes the secrets in \<Identification and Authentication Management\>, section 3.5: the token signing key and the audit chain key. Each application runs under a group managed service account, whose password Windows sets and changes, and the API connects to SQL Server with Windows authentication, so there is no service account password or database password to change.
2. They update the protected copy at the second site (\<Contingency Planning Management\>, section 3.8).
3. They record the change on TPL-6: the date, who made it and which secret, never the value. Changing the token signing key does not end users' sign-ins, because their cookies are protected by each application's key ring. **Manual**

#### PRO-IA-5 Password rules

1. \<System Name\> sets no password rules and keeps no list of blocked passwords. Both belong to \<Organisation\>'s corporate standard for Active Directory, which \<System Name\> accepts.

#### PRO-IA-6 Enrolling and resetting a second factor

1. Each person enrols their second factor with \<Organisation\>, for PingFederate, under its own procedure. **Manual**
2. If a second factor is lost or replaced, the person tells \<Organisation\>'s IT service desk, which checks who they are and lets them enrol a new one, and ends the person's PingFederate sign-in. **Manual**

#### PRO-IA-7 Reviewing authenticators and assurance levels

1. Every 12 months, and after a significant change, the system owner and security officer check that the authenticator inventory in \<Identification and Authentication Management\>, section 3.5, is complete and that each change period was met. **Manual**
2. They confirm the assurance levels in \<Identification and Authentication Management\>, section 3.4, still fit the information held, and take any change to the authorising official. **Manual**
3. The result is recorded in the change record of \<Identification and Authentication Management\>. **Manual**

#### PRO-IA-8 Disabling unused identifiers

1. \<Organisation\> disables Active Directory accounts unused for 90 days within 1 working day (\<System Description\>, P-38; \<Access Control Management\>, section 3.14).
2. A disabled identifier is never deleted or reused (PRO-IA-1, step 4). **Manual**

## IR Incident Response

Procedures PRO-IR-1 to PRO-IR-7.

### IR.1 Purpose

These procedures carry out \<Policy\> (IR) and \<Incident Response Management\>. Steps marked **Manual** have no system support and rely on people.

**Table IR-1: Procedures at a glance**

| Procedure | What it does | When | Who | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-IR-1 | Reporting an incident | Within 1 hour of noticing | Anyone; security officer | TPL-10 | IR-6, IR-6(1), IR-6(3) |
| PRO-IR-2 | Handling an incident | Each incident, to the targets in \<Incident Response Management\>, section 3.6 | Security officer; administrators | TPL-10 | IR-4, IR-4(1), IR-5 |
| PRO-IR-3 | Training and testing | Within 30 days of a role, every 12 months; tabletop every 12 months | Security officer | TPL-9; TPL-11 | IR-2, IR-3, IR-3(2) |
| PRO-IR-4 | Getting help | As needed | Users; security officer | ServiceNow request | IR-7, IR-7(1) |
| PRO-IR-5 | Handling a personal data breach | When personal data may be involved | Security officer; legal adviser | TPL-10; \<Incident Response Management\>, section 3.14 | IR-6 |
| PRO-IR-6 | Preserving evidence | Before anything is changed | Administrators | TPL-10 | IR-4, AU-9 |
| PRO-IR-7 | Closing an incident and learning | Within 10 working days of containment | Security officer; system owner | TPL-10 | IR-4, IR-8 |

### IR.2 Procedures

#### PRO-IR-1 Reporting an incident

1. Anyone who suspects an incident tells the security officer within 1 hour, by phone if ServiceNow or email may be affected (\<Incident Response Management\>, appendix A). **Manual**
2. The security officer opens a record on TPL-10, or a ServiceNow ticket, and sets the severity (\<Incident Response Management\>, section 3.6).
3. The security officer tells the people in the severity table, \<Organisation\>'s security contact, and any affected supplier. **Manual**
4. If personal data may be involved, the security officer starts PRO-IR-5 at once. **Manual**
5. If a crime or a significant cyber attack is suspected, the system owner reports it to the NCSC or to Report Fraud, which replaced Action Fraud. **Manual**

#### PRO-IR-2 Handling an incident

1. The security officer leads the steps in \<Incident Response Management\>, section 3.7, using the playbook in its section 3.9 that fits. **Manual**
2. The administrators preserve evidence first, under PRO-IR-6. **Manual**
3. They contain the incident to the target for its severity, for example by disabling an account or ending a person's PingFederate sign-in. **Manual**
4. If recovery is needed, the system owner invokes \<Contingency Planning Management\>; the incident plan leads while the outage may be an incident. **Manual**
5. The security officer records each action and time on TPL-10. **Manual**

#### PRO-IR-3 Training and testing

1. The security officer trains each person with an incident role within 30 days of taking it, every 12 months and after a plan change, and records it on TPL-9 and in the training register (\<Awareness and Training Management\>, section 3.8). This is module M7 in the training matrix (\<Awareness and Training Management\>, section 3.5), with its 80% check. The content is the plan, the severity levels, the playbooks, preserving evidence, the breach steps and the contacts. **Manual**
2. The security officer reviews the content every 12 months, and after a plan change or an incident. **Manual**
3. Every 12 months the security officer runs a tabletop exercise with the people named in \<Incident Response Management\> and \<Contingency Planning Management\>, rotating through the playbooks, and writes an after-action report on TPL-11. **Manual**

#### PRO-IR-4 Getting help

1. Users get advice from the security officer, and through a ServiceNow request.
2. The security officer gets help from \<Organisation\>'s security contact. **Manual**

#### PRO-IR-5 Handling a personal data breach

1. The security officer tells the legal adviser as soon as personal data may be involved, with what is known. **Manual**
2. The legal adviser assesses the risk to people. If it is likely, the legal adviser reports to the ICO within 72 hours of the organisation becoming aware, with the reasons for any delay. **Manual**
3. If the risk to people is high, the legal adviser tells them without undue delay, unless the data could not be read. **Manual**
4. The security officer records every breach in \<Incident Response Management\>, section 3.14: the facts, effects, action taken, and the reason if not reported. **Manual**

#### PRO-IR-6 Preserving evidence

1. Before anything is changed, the database administrator exports the audit records and records the SHA-256 hash. **Manual**
2. The Windows server administrator copies the application, Windows and SQL Server logs, and records their hashes. For ransomware, the VM is isolated through \<Organisation\> but not powered off. **Manual**
3. They note each system's clock against a trusted time source. **Manual**
4. Each item is listed on TPL-10 with who holds it, where, and each hand-over. **Manual**

#### PRO-IR-7 Closing an incident and learning

1. Within 10 working days of containment, the security officer records the root cause, the time to report, contain and recover against the targets, and the lessons, on TPL-10. **Manual**
2. The system owner updates \<Incident Response Management\>, \<Risk List\> and \<Plan of Action and Milestones\> with the changes, and the training content if needed. **Manual**
3. The system owner closes the record and the register entry. **Manual**

## MA Maintenance

Procedures PRO-MA-1 to PRO-MA-7.

### MA.1 Purpose

These procedures carry out \<Policy\> (MA), rules R1 to R12. The lists, routes and values they use are in \<Maintenance Management\>. Steps marked **Manual** have no system support and rely on people.

### MA.2 Summary

**Table MA-1: Procedures at a glance**

| Procedure | What it does | Who | When | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-MA-1 | Schedules, approves, checks and records maintenance, and reviews the records | Administrators, security officer | Each job; records monthly (C48) | Change record, TPL-12 | MA-2 |
| PRO-MA-2 | Removes equipment safely | System owner, \<Organisation\> | When equipment leaves | TPL-12, TPL-13 | MA-2(c), MA-2(d) |
| PRO-MA-3 | Controls and inspects maintenance tools | Windows server administrator | Before use; list every 12 months (C28) | TPL-12 | MA-3, MA-3(1), MA-3(2) |
| PRO-MA-4 | Runs remote maintenance over an approved route | Administrators, \<Organisation\> | Each remote job; logs weekly | TPL-12, session log | MA-4 |
| PRO-MA-5 | Controls who may maintain \<System Name\> | System owner, Windows server administrator | Before access; list every 12 months (C28) | \<Maintenance Management\>, TPL-12 | MA-5 |
| PRO-MA-6 | Runs preventive maintenance to a schedule | Administrators, developers, \<Organisation\> | As in Table MA-3 | TPL-12, TPL-8 | MA-2(a), MA-6 |
| PRO-MA-7 | Controls the built-in diagnostics and data leaving for support | Administrator, system owner | Each use | Change record, TPL-12, TPL-13 | MA-2, MA-3, MA-3(3) |

### MA.3 Procedures

#### PRO-MA-1 Scheduling, approving, checking and recording maintenance

1. The administrator raises a change record, following \<Procedures\> (CM). It names the component, the work, who will do it, the tools, the route and any downtime. **Manual**
2. The change is approved before work starts. Emergency maintenance follows the emergency change rule in \<Security Operating Procedures\>, section 4.5, and is recorded within 1 working day. **Manual**
3. If users are affected, the system owner tells them at least 2 working days before planned maintenance. **Manual**
4. The administrator watches any work done by someone who is not on the list of maintenance people (PRO-MA-5). **Manual**
5. When the work is finished, the administrator runs the checklist in Table MA-2 and records the result on TPL-12. In the test environment, the maintenance test script runs the first three checks. **Manual**
6. The security officer reviews and signs the checklist result within 1 working day. **Manual**
7. Each month, the security officer reviews every TPL-12 against its change record (C48). Maintenance with no change record is raised as a security incident. **Manual**

**Table MA-2: Checklist after maintenance**

| Check | How | Expected |
| --- | --- | --- |
| Services are healthy | The API health check and each application's start page (C1) | All answer |
| Anonymous access is refused | An API call with no token, and an Admin application page | The call is refused, and the page sends the person to PingFederate to sign in |
| Sign-in works and is audited | Sign in through PingFederate, then look at the audit log | A new sign-in record |
| Audit records are intact | The audit chain check (\<Procedures\>, PRO-AU-2), and records without a hash | None broken; none without a hash |
| Items are intact | File checksum check (\<Procedures\>, PRO-SI-6) | All match |
| Defender is running | Defender status on both VMs | On, and up to date |
| Backups still run | The last backup job (C8) | Succeeded |
| Time is right | Both VMs against UTC (C45) | Within 1 second |
| Settings are unchanged | Drift check (\<Procedures\>, PRO-CM-7) | No unapproved difference |

#### PRO-MA-2 Removing equipment

1. The system owner approves the removal of any equipment in the change record. **Manual**
2. \<Organisation\> sanitises it first by the method in \<Media Protection Management\>, section 3.6 (CSS and IEEE 2883-2022), following \<Procedures\>, PRO-MP-3, and confirms in writing with a certificate (EV-MA-01). **Manual**
3. The administrator records the removal, the approval and the certificate on TPL-12, and any media on TPL-13. **Manual**

#### PRO-MA-3 Maintenance tools

1. The Windows server administrator keeps the approved tool list in \<Maintenance Management\>, section 3.5, and reviews it with the system owner every 12 months (C28). A new tool needs the system owner's approval before first use. **Manual**
2. Tools are inspected before use for changes that are not expected: the version, publisher and file hash are compared with the list, and the result is recorded on TPL-12. **Manual**
3. Media holding diagnostic or test programs are scanned by Defender before use.
4. No tool outside the approved tool list is installed or used on the servers. **Manual**
5. Equipment that holds \<System Name\> data leaves only under PRO-MA-2, or PRO-MA-7 for data sent for support. **Manual**

#### PRO-MA-4 Remote maintenance

1. The system owner approves remote work in the change record, naming the route from \<Maintenance Management\>, section 3.4. **Manual**
2. The person connects only through that route, with multi-factor sign-in and a named account (EV-MA-02). Server and database administration reaches the two servers only from the administrators' managed devices over the managed administration route (F11), and the Admin application is reached only through that route.
3. A supplier's session is watched by an administrator. Each session is logged as set in \<Maintenance Management\>, section 3.4. **Manual**
4. When the work is finished, the session and network connection are ended, and any temporary account is disabled. **Manual**
5. The administrator records the job on TPL-12 with the session reference. The security officer reviews the session logs weekly (C4, C5). **Manual**

#### PRO-MA-5 Maintenance people

1. The system owner approves the list of maintenance organisations and people in \<Maintenance Management\>, section 3.6. **Manual**
2. Before giving access, the administrator checks the person is on the list, is screened, has signed Part B of \<Security Operating Procedures\> and has a named account. **Manual**
3. A supplier gets a temporary account limited to the job, disabled when the job ends. **Manual**
4. Anyone not on the list is escorted and supervised by someone who is, and has no access to \<System Name\>'s data. **Manual**
5. The Windows server administrator checks the list when someone leaves, and every 12 months (C28). **Manual**

#### PRO-MA-6 Preventive maintenance schedule

Flaw fixes (SI-2) and releases (CM-3) follow their own procedures. They are listed here so that all routine work is in one place.

**Table MA-3: Preventive maintenance schedule**

| Task | Component | Who | How often | Record |
| --- | --- | --- | --- | --- |
| Check database integrity, update statistics and maintain indexes | SQL Server | Database administrator | Monthly | TPL-12 |
| Check disk space and growth | Both VMs and the database | Windows server and database administrators | Monthly | TPL-8 |
| Apply updates (SI-2) | Windows, SQL Server, .NET | As \<Security Operating Procedures\>, section 4.3 | Monthly, and within the fix times | TPL-7 |
| Renew certificates | Both VMs | Windows server administrator | 30 days before expiry (C39) | TPL-6 |
| Clear old application logs | Application VM | Windows server administrator | Monthly (C46) | TPL-8 |
| Build each release on the patched .NET runtime (CM-3) | Applications | Developers | Each release, checked monthly (C11) | TPL-6 |
| Check support end dates | Components in \<Maintenance Management\>, section 3.8 | Developers, Windows server administrator | Monthly (C11) | TPL-7 |
| Maintain hardware and hypervisor | Hosts | \<Organisation\> | \<Organisation\>'s schedule | \<Organisation\>'s report (EV-MA-01) |

#### PRO-MA-7 Built-in diagnostics and data leaving for support

1. The fixed diagnostics page in the Admin application (\<Maintenance Management\>, section 3.5), which reads no item content, is used only under an approved change record that names the reason. No other diagnostic or test page is included in a release. **Manual**
2. An Administrator opens it with a second person present: the security officer or the system owner. **Manual**
3. The database's structure is never changed from a page. Before a release changes it, which the database administrator applies under an approved change, a backup is taken and checked (\<Procedures\>, PRO-CP-1). **Manual**
4. The diagnostics run, or the structure change, and the outcome are recorded on TPL-12. **Manual**
5. Before any data, dump, log or screenshot is sent for maintenance or support, the system owner approves it. **Manual**
6. It is cut to the minimum, with personal data removed where possible, encrypted, and sent by an approved route. **Manual**
7. It is recorded on TPL-12 or TPL-13, and the receiver confirms deletion when it is no longer needed. **Manual**

## MP Media Protection

Procedures PRO-MP-1 to PRO-MP-6.

### MP.1 Purpose

These procedures carry out \<Policy\> (MP), rules R1 to R12. The media inventory, values and methods they use are in \<Media Protection Management\>. Steps marked **Manual** have no system support and rely on people.

### MP.2 Summary

**Table MP-1: Procedures at a glance**

| Procedure | What it does | Who | When | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-MP-1 | Marks and protects printouts | Everyone | Each printout | None; shredding on TPL-13 if bulk | MP-2, MP-3, MP-4 |
| PRO-MP-2 | Protects disks, volumes and backups, and moves them only by exception | \<Organisation\>, administrators | Always; transport when approved | TPL-13 | MP-2, MP-4, MP-5 |
| PRO-MP-3 | Sanitises media by the method for its type, and checks certificates | \<Organisation\>, administrators, system owner | Before reuse, release or disposal; check every 12 months | TPL-13 | MP-6 |
| PRO-MP-4 | Controls portable storage and ownerless devices | \<Organisation\>, system owner, security officer | Always; exceptions when asked | TPL-17, TPL-13 | MP-7 |
| PRO-MP-5 | Controls export copies on the server and users' copies | Windows server administrator, everyone | Each working day (C49); each export | TPL-8 | MP-2, MP-4, MP-6 |
| PRO-MP-6 | Keeps the media inventory up to date | System owner | Every 12 months, and after a change | \<Media Protection Management\> change record | MP-2, MP-4 |

### MP.3 Procedures

#### PRO-MP-1 Printouts

1. Anyone who prints an item from \<System Name\> uses only an \<Organisation\> managed printer with secure release, and keeps the classification marking that \<System Name\> puts on each printed page. **Manual**
2. They collect it at once, keep it locked away when not in use, and share it only with people authorised to read that schema. **Manual**
3. It does not leave the site without the system owner's approval (PRO-MP-2). **Manual**
4. They cross-cut shred it to DIN 66399 level P-4 or better when it is no longer needed, and within 30 days if it holds personal data. **Manual**

#### PRO-MP-2 Disks, volumes and backups

1. VM disks and database and key volumes stay in \<Organisation\>'s data centres, encrypted with BitLocker, reachable only by the roles in \<Media Protection Management\>. **Manual** (EV-MP-01)
2. Backups are encrypted before they leave the database VM, and copied to the second site over an encrypted connection (SC-8, CP-6).
3. Physical media are moved only by exception, with the system owner's approval, encrypted or sealed, by an authorised courier with tracking, and recorded on TPL-13. **Manual** (EV-MP-01)

#### PRO-MP-3 Sanitising media

1. Before any media is reused, released or disposed of, the person responsible sanitises it by the method set for its type in \<Media Protection Management\>, section 3.6, following CSS and IEEE 2883-2022. **Manual** (EV-MP-02)
2. For encrypted virtual disks and backups, every copy of the keys is destroyed, including recovery keys and the copy at the second site (cryptographic erase), and \<Organisation\> deletes the volumes. Each copy of the key is listed on TPL-13. **Manual**
3. \<Organisation\> purges or destroys physical disks and gives a certificate. **Manual** (EV-MP-02)
4. Each action is recorded on TPL-13 with the item, serial, method, tool, verification and certificate. **Manual**
5. Every 12 months, the system owner checks a sample of \<Organisation\>'s certificates against TPL-13. **Manual**

#### PRO-MP-4 Portable storage and ownerless devices

1. USB and other portable storage are blocked on users' devices, and no USB device is passed through to the VMs. **Manual** (EV-AC-17, EV-MP-03)
2. The system owner approves any exception on TPL-17, for a stated purpose and time, using only encrypted media issued by \<Organisation\>. **Manual**
3. Anyone who finds portable storage with no identifiable owner does not use it, and hands it to the security officer, who records it on TPL-13. **Manual**

#### PRO-MP-5 Export copies and users' copies

1. Only an editor of a schema, or an Administrator, can export its items.
2. \<System Name\> deletes each export copy after the download, and a background task removes any left past 24 hours. Each working day, the Windows server administrator checks the encrypted export working area on the application VM, deletes anything older than 24 hours, and records it on TPL-8 (C49). **Manual**
3. Users save exports and downloads only in approved \<Organisation\> locations: \[approved locations\], on a managed device, and delete them within 30 days once no longer needed (\<Security Operating Procedures\>, A28 and A30 to A35). **Manual**
4. Export files carry the classification marking that \<System Name\> applies, and the user who keeps them does not remove it. **Manual**

#### PRO-MP-6 Media inventory

1. The system owner reviews the media inventory in \<Media Protection Management\>, section 3.2, every 12 months and after a change that creates a new copy of \<System Name\> information. **Manual**
2. Any new place is added, with its protection, access and sanitising method, before it is used. **Manual**

## PE Physical and Environmental Protection

Procedures PRO-PE-1 to PRO-PE-5.

### PE.1 Purpose

These procedures carry out \<Policy\> (PE), rules R1 to R10. The values, inheritance matrix and site details they use are in \<Physical and Environmental Protection Management\>. Steps marked **Manual** have no system support and rely on people.

### PE.2 Summary

**Table PE-1: Procedures at a glance**

| Procedure | What it does | Who | When | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-PE-1 | Obtains and reviews \<Organisation\>'s evidence for both sites | System owner | Every 12 months, and after a change of site | \<Evidence Requests\>; \<Physical and Environmental Protection Management\>, section 3.3 | PE-2 to PE-16 |
| PRO-PE-2 | Handles physical incidents | Security officer, \<Organisation\> | When one occurs | TPL-10 | PE-6, IR-4 |
| PRO-PE-3 | Protects screens and printouts | Everyone | Always | None | PE-5 |
| PRO-PE-4 | Controls home working | Everyone, security officer | Always; checked every 12 months (C30) | TPL-4 | PE-17 |
| PRO-PE-5 | Inspects the site once | Independent assessor or \<Organisation\>'s auditor | At Level 2, and after a change of site | TPL-20 | PE-2 to PE-16 |

### PE.3 Procedures

#### PRO-PE-1 Checking \<Organisation\>'s evidence

1. The system owner asks \<Organisation\> first for its ISO/IEC 27001 certificate, Statement of Applicability and latest audit findings for Annex A.7, or a SOC 2 report covering physical access (CC6.4) and the availability criteria (A1.2), for both the data centre and the second site (EV-PE-01). **Manual**
2. Where those do not cover a control, the system owner asks for the facility evidence in EV-PE-01 to EV-PE-05. **Manual**
3. The system owner records what was received against each control in the inheritance matrix (\<Physical and Environmental Protection Management\>, section 3.3), and confirms that \<Organisation\>'s corporate parameter values are met. **Manual**
4. Any shortfall is raised in \<Risk List\>. **Manual**
5. The system owner repeats this every 12 months, and after a change of site or a significant incident at a site. **Manual**

#### PRO-PE-2 Physical incidents

1. Anyone who loses a device or printout, or sees a physical security problem, reports it to the security officer at once. **Manual**
2. \<Organisation\>'s security contact tells the security officer of any physical incident at a site that affects \<System Name\>, including fire, flood and power loss, within 24 hours. **Manual** (EV-PE-01)
3. The security officer handles it with the physical incident playbook in \<Incident Response Management\>, section 3.9, and calls the contingency plan if a site is lost. **Manual**

#### PRO-PE-3 Screens and printers

1. Users print items from \<System Name\> only on \<Organisation\>'s managed printers with secure release: \[managed printers\]. **Manual** (EV-PE-05)
2. They release and collect printouts at once, and keep the classification marking that \<System Name\> prints on each page (\<Procedures\>, PRO-MP-1). **Manual**
3. Users lock their screen when they leave it, place it so that others cannot read it, and keep their desk clear of printed documents. \<Organisation\>'s managed devices also lock the screen after the inactivity period in \<System Description\>, P-03. **Manual**

#### PRO-PE-4 Working from home

1. People work remotely only from home, unless the system owner has approved another place in writing, on \<Organisation\>'s managed devices and route. **Manual** (EV-PE-05)
2. They do not print items from \<System Name\> at home unless the system owner has approved it, and they work where others in the home cannot see the screen. **Manual**
3. Anyone working from home reports any concern or incident to the security officer at once, using the contacts in \<Security Operating Procedures\>, section 6. **Manual**
4. Every 12 months, the security officer puts a short checklist to every person who works from home (managed device, VPN, screen privacy, no printing, reporting) and records the answers on TPL-4 (C30). **Manual**

#### PRO-PE-5 Site inspection

1. At Level 2, the independent assessor, or \<Organisation\>'s auditor if the assessor cannot visit, inspects each data centre once, the main site and the second site, using TPL-20. **Manual**
2. The inspection covers entry control and logs, visitors, keys and cards, cabling, power and emergency shutoff, lighting, fire, environment, water and deliveries. **Manual**
3. The system owner records the result in the inheritance matrix and raises any shortfall in \<Risk List\>. The inspection is repeated after a change of site. **Manual**

## PL Planning

Procedures PRO-PL-1 to PRO-PL-6.

### PL.1 Purpose

These procedures carry out \<Policy\> (PL). Steps marked **Manual** have no system support and rely on people. Each procedure names the record it leaves, so that an assessor can see it was followed.

**Table PL-1: Procedures at a glance**

| Procedure | When | Who | Record | Controls |
| --- | --- | --- | --- | --- |
| PRO-PL-1 Keeping the plans current | After an assessment, significant change or problem in use, and every 12 months | System owner | Plan review record and change record in each plan; Test-PlanConsistency.ps1 results | PL-2c, PL-2d |
| PRO-PL-2 Sharing the plans | When a plan is approved or changed | System owner | Plan review record entry naming the recipients | PL-2b |
| PRO-PL-3 Signing the rules | Before access, every 12 months, and after a material change | System owner, everyone | TPL-21; register of signatures in \<Planning Management\>, section 3.5 | PL-4b, PL-4d |
| PRO-PL-4 Tailoring | When a control or part is proposed as not applicable | Proposer, system owner, authorising official | Entry in \<Tailoring Register\> and \<Decision Register\> | PL-11 |
| PRO-PL-5 Reviewing the architecture | Every 12 months, and after a significant change | System owner | Change record and review record in \<System Description\>, section 6 | PL-8b, PL-8c |
| PRO-PL-6 Protecting the plans | Always; checked at each review | System owner | Access list of the restricted SharePoint area | PL-2e |

### PL.2 Procedures

#### PRO-PL-1 Keeping the plans current

1. After each assessment, significant change or problem found in use, the system owner updates the affected plans and adds a line to each change record. **Manual**
2. The system owner runs the plan consistency test on the document set and corrects every gap before issuing the plans.
3. Every 12 months, the system owner reviews each plan in the register in \<Planning Management\>, section 3.2, and records the review in its plan review record: who, their role, the date, the outcome and actions. **Manual**
4. The SSP goes to the Head of Cyber for concurrence and to the authorising official to accept as an accurate record. **Manual**

#### PRO-PL-2 Sharing the plans

1. When the SSP, privacy plan or supply chain plan is approved or changed, the system owner sends a link to the restricted copy to the Head of Cyber, administrators and \<Organisation\>'s security contact. **Manual**
2. The system owner records the recipients and the date in the plan review record. **Manual**

#### PRO-PL-3 Signing the rules

1. Before access, the system owner gives the person \<Security Operating Procedures\>: Part A for everyone, and Parts A and B for administrators. **Manual**
2. The person signs the declaration that they have read and understood the rules and agree to follow them, on paper or electronically, and the system owner completes TPL-21. **Manual**
3. The system owner adds the signature to the register in \<Planning Management\>, section 3.5. The access request (TPL-2) checks the register before access is given. **Manual**
4. When SyOps changes, the system owner decides whether the change is material, as defined in \<Policy\> (PL), R7, and records the answer in the change record of \<Security Operating Procedures\>. If it is, everyone signs again within 30 days, or loses access. **Manual**
5. Every 12 months, everyone signs again. **Manual**

#### PRO-PL-4 Tailoring

1. Anyone proposing to tailor a control records the rationale, the condition that must hold and what happens if it changes, in \<Tailoring Register\>. **Manual**
2. The system owner decides, records the decision in \<Decision Register\> and updates the SSP applicability table. The authorising official accepts the register as a record. **Manual**
3. Each condition is checked at the yearly review. **Manual**

#### PRO-PL-5 Reviewing the architecture

1. Every 12 months, and after a significant change, the system owner reviews \<System Description\>, section 6, against the running system. **Manual**
2. Changes are carried into the SSP, the privacy plan, the ConOps, the critical components list in \<Risk Assessment Management\>, section 3.9 and any procurement, and each is noted in the review record. **Manual**
3. New open questions go to \<Decision Register\> or \<Plan of Action and Milestones\>, not into the architecture. **Manual**

#### PRO-PL-6 Protecting the plans

1. Plans and assessment evidence are kept only in the restricted SharePoint area. Only named people have access. **Manual**
2. Working copies are never kept in a code repository or a folder that syncs to one. **Manual**
3. At each review, the system owner checks the area's access list against \<Roles and Responsibilities\> and records the check in the plan review record. **Manual**

## PS Personnel Security

Procedures PRO-PS-1 to PRO-PS-7.

### PS.1 Purpose

These procedures carry out \<Policy\> (PS). Steps marked **Manual** rely on people. The designations, screening standard, time limits and register are in \<Personnel Security Management\>.

**Table PS-1: Procedures at a glance**

| Procedure | When | Who | Time limit | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| PRO-PS-1 Before access | Access or a role is requested | System owner, \<Organisation\> | Before access is given | TPL-2; TPL-21; personnel security register | PS-2, PS-3, PS-6 |
| PRO-PS-2 Leavers | Someone leaves, or no longer needs \<System Name\> | \<Organisation\>, the groups' owners, system owner | 5 working days; 1 hour for a higher-risk leaver | TPL-14 | PS-4 |
| PRO-PS-3 Movers | Someone changes role | Line manager, system owner, the groups' owners | 1 working day | TPL-14 | PS-5 |
| PRO-PS-4 Reviewing designations and agreements | Every 12 months, and when a role's access changes | System owner | Within the 12 months | TPL-3; TPL-21 | PS-2, PS-6 |
| PRO-PS-5 External people | A contract is let or renewed; then every 12 months | System owner | 1 working day for supplier notices | TPL-16 | PS-7 |
| PRO-PS-6 Sanctions | A formal sanction involves \<System Name\> | \<Organisation\>, system owner | 1 working day to tell the system owner | TPL-10 if it is an incident | PS-8 |
| PRO-PS-7 Checking | At each review | System owner | At each review | Test-PlanConsistency.ps1, check L17 | PS-1, PS-2 |

### PS.2 Procedures

#### PRO-PS-1 Before access

1. The system owner looks up the role's risk designation in \<Personnel Security Management\>, section 3.2. **Manual**
2. The system owner asks \<Organisation\> to confirm that the person has passed its screening, and that it covers the minimum in \<Personnel Security Management\>, section 3.3. For a higher risk role, the confirmation must be less than 5 years old. **Manual** (EV-PS-01)
3. The system owner records the confirmation on TPL-2 and in the personnel security register: who confirmed it and the date only. No screening result is recorded. **Manual**
4. The person signs \<Organisation\>'s confidentiality agreement, and \<Security Operating Procedures\> Part A, and Part B if privileged, on TPL-21. **Manual**
5. Only then is the person added to the \<System Name\> groups for their role (\<Procedures\>, PRO-AC-1). **Manual**

#### PRO-PS-2 Leavers

1. \<Organisation\> disables the person's Active Directory account at once, which ends their access to \<System Name\>. The starters and leavers process tells the system owner and the owners of the person's groups, who remove the memberships within 5 working days (\<Procedures\>, PRO-AC-3).
2. For a higher-risk leaver, a dismissal or suspected misuse, anyone who knows tells the system owner and \<Organisation\>'s service desk. Within 1 hour, the service desk disables the Active Directory account and ends the person's PingFederate sign-in, and the system owner confirms that both are done and that \<System Name\> refuses the person within 5 minutes (\<Procedures\>, PRO-AC-4). **Manual**
3. Disabling the Active Directory account revokes the person's password and second factor. The system owner has any service secret the person knew changed (\<Procedures\>, PRO-IA-4). **Manual**
4. \<Organisation\> holds the exit interview, including confidentiality duties, and recovers equipment. **Manual** (EV-PS-02)
5. The system owner confirms that the items the person managed stay available, and completes TPL-14. **Manual**

#### PRO-PS-3 Movers

1. The person's line manager tells the system owner within 1 working day.
2. The system owner reviews whether the current access is still needed, and asks the owners of the person's groups for any change, within 1 working day. **Manual**
3. If the new role is higher risk, the system owner asks \<Organisation\> to confirm screening again before the role is granted. **Manual**
4. The system owner records this on TPL-14 and updates the personnel security register. **Manual**

#### PRO-PS-4 Reviewing designations and agreements

1. Every 12 months, and when a role's access changes, the system owner reviews the risk designations against \<Roles and Responsibilities\> and records the review on TPL-3. **Manual**
2. The system owner reviews the access agreements at the same time. **Manual**
3. Everyone signs their agreements again every 12 months, and after a material change to the rules, on TPL-21. **Manual**

#### PRO-PS-5 External people

1. The system owner makes sure each contract states security duties, and that the supplier must report leavers and movers within 1 working day. **Manual** (EV-PS-03)
2. External people, including any member of the independent assessment team who is not \<Organisation\>'s staff, are screened and sign the agreements as in PRO-PS-1 before any access, or before the evidence is shared with them. **Manual**
3. The system owner checks each supplier's compliance every 12 months, and records it on TPL-16. **Manual**

#### PRO-PS-6 Sanctions

1. \<Organisation\> follows its disciplinary process. **Manual** (EV-PS-02)
2. \<Organisation\> tells the system owner within 1 working day when a formal sanction involves \<System Name\>. **Manual**
3. If the breach is a security incident, the security officer records it on TPL-10 (\<Procedures\> (IR)). The system owner decides whether access must end at once under PRO-PS-2, step 2. **Manual**

#### PRO-PS-7 Checking

1. At each review, the system owner runs Test-PlanConsistency.ps1 and confirms that check L17 passes: every role in \<Roles and Responsibilities\> has a risk designation. **Manual**
2. The system owner compares a sample of the members of \<System Name\>'s groups with the personnel security register, and records the result with the review. **Manual**

## PT Personally Identifiable Information Processing and Transparency

Procedures PRO-PT-1 to PRO-PT-6.

### PT.1 Purpose

These procedures carry out \<Policy\> (PT). Steps marked **Manual** have no system support and rely on people. Each procedure names the record it leaves.

**Table PT-1: Procedures at a glance**

| Procedure | When | Who | Record | Controls |
| --- | --- | --- | --- | --- |
| PRO-PT-1 Requests from individuals | A request about a person's data: to see, correct, delete, restrict, object or receive it in a portable form | Legal adviser and their delegate, auditor, editors, Administrators | TPL-15 | AC-3(14), SI-18(4), PT-2 |
| PRO-PT-2 Complaints | A complaint about how data is handled | Legal adviser | TPL-22 | PT-2, PM-26 |
| PRO-PT-3 Changes in processing | A change that affects personal data | System owner, legal adviser | TPL-6 change record | PT-3, SA-8(33) |
| PRO-PT-4 Impact assessment | Before production; after a significant change; every 12 months | Legal adviser, system owner, business owner | \<Data Protection Impact Assessment\> | RA-8, PT-7 |
| PRO-PT-5 Accuracy, retention and disposal | Every 12 months; at the end of each retention period | Business owner, Data Owners, Administrators | TPL-3 review; audit record of each disposal | SI-12, SI-12(1), SI-12(3), SI-18 |
| PRO-PT-6 Training and test data | Before access and every 12 months; every test or training session | System owner, developers, trainers | TPL-9 | AT-3(5), IR-2(3), SI-12(2) |

### PT.2 Procedures

#### PRO-PT-1 Requests from individuals

1. Anyone who receives a request from a person about their data passes it to the legal adviser at once. **Manual**
2. The legal adviser logs it on TPL-15, confirms the person's identity, and sets the deadline: one month from that confirmation, extendable as the law allows, and paused while waiting for any clarification needed. **Manual**
3. The legal adviser's delegate makes a reasonable and proportionate search of every schema with the search across schemas (\<System Description\>, FR-073), and an auditor searches the audit records. What was found is listed on TPL-15. **Manual**
4. Corrections and deletions are made by an editor of the schema or an Administrator, on the legal adviser's instruction, and confirmed in writing on TPL-15. **Manual**
5. For a request to restrict processing, to object, or to receive the data in a portable form, the legal adviser decides whether the right applies and how it is met. **Manual**
6. When data is corrected, deleted or restricted, the legal adviser tells anyone it was disclosed to, unless that is impossible or would take disproportionate effort, and records it on TPL-15. **Manual**
7. The legal adviser answers the person and closes TPL-15. **Manual**

#### PRO-PT-2 Complaints

1. Anyone who receives a complaint about how personal data in \<System Name\> is handled passes it to the legal adviser at once. **Manual**
2. The legal adviser acknowledges it within 30 days, and records it on TPL-22. **Manual**
3. The legal adviser investigates without undue delay, keeps the person informed, and tells them the outcome. **Manual**
4. Any weakness found is raised in \<Risk List\>. **Manual**

#### PRO-PT-3 Changes in processing

1. Each change record (TPL-6) says whether the change affects personal data. **Manual**
2. If it does, the legal adviser reviews it and decides whether the inventory (\<PII Processing Management\>, section 3.3), the privacy notice or the impact assessment must change. **Manual**
3. The system owner asks \<Organisation\> to keep the privacy notice current, and reviews it every 12 months (EV-PT-01). **Manual**

#### PRO-PT-4 Impact assessment

1. The legal adviser completes \<Data Protection Impact Assessment\> before production, with the system owner, the business owner and the data protection officer's advice. **Manual**
2. Measures go into \<Plan of Action and Milestones\>, and residual risks go to the authorising official. If a high risk remains, the legal adviser consults the ICO before processing. **Manual**
3. The assessment is reviewed after a significant change in processing, and every 12 months. **Manual**

#### PRO-PT-5 Accuracy, retention and disposal

1. The business owner sets each retention period in \<PII Processing Management\>, section 3.7. **Manual**
2. Every 12 months each Data Owner checks that their schema's personal data is accurate, relevant, timely and complete, and records the check on TPL-3. **Manual**
3. A scheduled task lists the items past their retention period, which are deleted once the business owner, a member of \<Code\>\_BusinessOwners, approves their disposal in the UI application (\<System Description\>, FR-074), and each deletion is audited.

#### PRO-PT-6 Training and test data

1. Everyone who handles items holding personal data, and all administrators, complete privacy training before access and every 12 months. The module covers the purposes, the rules in \<Security Operating Procedures\>, A23 to A29, recognising and reporting a breach within an hour, requests and complaints. It is recorded on TPL-9. **Manual**
2. Developers use only invented data for testing, and trainers use only invented data for training. Real personal data is never used there. Test-PersonalData.ps1 checks this in each test environment. **Manual**

## RA Risk Assessment

Procedures PRO-RA-1 to PRO-RA-6.

### RA.1 Purpose

These procedures carry out \<Policy\> (RA). Steps marked **Manual** have no system support and rely on people. Each procedure names the record it leaves.

**Table RA-1: Procedures at a glance**

| Procedure | When | Who | Record | Controls |
| --- | --- | --- | --- | --- |
| PRO-RA-1 Reviewing risk | Every 12 months; after a significant change, incident or new test result | System owner, authorising official | TPL-23; \<Risk List\> and \<Decision Register\> updated | RA-3, RA-7 |
| PRO-RA-2 Reviewing the supply chain | Every 12 months; before adding a supplier or a new kind of component | System owner, developers | TPL-23 | RA-3(1), SR-6 |
| PRO-RA-3 Scanning and analysing | Monthly and at each release | Windows server administrator, developers, security officer | TPL-7 | RA-5, RA-5(2), RA-5(5), SI-2 |
| PRO-RA-4 Responding to an exploited flaw | When a flaw affecting \<System Name\> is listed in CISA's catalogue or confirmed exploited | Security officer, developers, system owner | TPL-7; TPL-6 emergency change | RA-5d, SI-2, CM-3 |
| PRO-RA-5 Sharing results and receiving reports | After each scan; on any report | Security officer | TPL-7 | RA-5e, RA-5(11) |
| PRO-RA-6 Reviewing critical components | At each major release and significant change | System owner, developers | \<Risk Assessment Management\>, section 3.9; TPL-23 | RA-9 |

### RA.2 Procedures

#### PRO-RA-1 Reviewing risk

1. Every 12 months, and after a significant change, incident or new test result, the system owner reviews each risk in \<Risk List\> against the method in its section 4, and updates its rating, status and last-reviewed date. **Manual**
2. They check that each acceptance in section 3 is within its review date, and that Medium and High risks have a decision. Test-Vulnerability.ps1, checks V05 to V07, does this mechanically. **Manual**
3. They record the review on TPL-23 and share it with the authorising official and the Head of Cyber. **Manual**
4. The system owner decides Low risks, and the authorising official decides Medium and High risks, recording them in \<Decision Register\>. **Manual**
5. At each review the system owner checks that the categorisation in \<System Security Plan\>, section 3.3, still fits the information \<System Name\> holds, and puts any change to the authorising official. **Manual**

#### PRO-RA-2 Reviewing the supply chain

1. Every 12 months, before adding a supplier or a new kind of component, and after a significant change to the system or where it runs, the system owner and developers review packages, browser libraries, suppliers and the VMs for origin, support, known problems and end of support. **Manual**
2. They use \<Supply Chain Risk Management\>, section 3.4, the latest package check, and the CM bill of materials. **Manual**
3. They record the result on TPL-23, and any new risk in \<Risk List\>. **Manual**

#### PRO-RA-3 Scanning and analysing

1. The administrator updates the scanner's definitions before each scan.
2. Monthly and at each release, the Windows server administrator runs a credentialed scan of both VMs, using an account approved for that purpose.
3. At each release, developers run Test-Vulnerability.ps1, which checks the packages and browser libraries. **Manual**
4. At each release, developers run a web application scan of the UI application, the Admin application and the API.
5. Within 5 working days, the security officer reviews the results on TPL-7. For each finding they record its severity under \<Risk Assessment Management\>, section 3.6, whether \<System Name\> uses the affected part, and the due date. **Manual**
6. A finding that does not apply, such as a flaw in a feature \<System Name\> does not call, is marked as a false positive on TPL-7 with the reason, and checked again at the next scan. **Manual**
7. The people responsible fix or mitigate each finding within its time. A fix that cannot meet its time goes to a risk decision, with its compensating measure. **Manual**

#### PRO-RA-4 Responding to an exploited flaw

1. The security officer checks CISA's Known Exploited Vulnerabilities catalogue and \<Organisation\>'s alerts at least weekly against the components in \<System Security Plan\>, section 3.4. **Manual**
2. A listed flaw in a \<System Name\> component is recorded on TPL-7 the same day, with a due date 3 days away. **Manual**
3. Developers or the administrator apply the fix, or a mitigation such as disabling the feature or blocking its route, as an emergency change (\<Procedures\> (CM)). **Manual**
4. The security officer confirms the fix or mitigation, and tells the system owner. If it cannot be done in 3 days, the authorising official decides at once. **Manual**

#### PRO-RA-5 Sharing results and receiving reports

1. After each scan the security officer shares the findings that apply with the developers and the Windows server administrator, so that the same flaw is fixed everywhere it occurs, and passes to \<Organisation\>'s security contact any that may affect its other systems (RA-5e). **Manual**
2. \<Organisation\>'s security contact, published with terms that authorise research in good faith (EV-RA-01), passes any report about \<System Name\> to the security officer, who records it on TPL-7 and handles it as in PRO-RA-3. **Manual**
3. A flaw found in another party's package or browser library is reported to its maintainer through their published route, and noted on TPL-7. **Manual**

#### PRO-RA-6 Reviewing critical components

1. At each major release and significant change, the system owner and developers review the critical components in \<Risk Assessment Management\>, section 3.9, using its method. **Manual**
2. They update the list, check each component is in \<System Security Plan\> (Test-Vulnerability.ps1, V08), and record the review on TPL-23. **Manual**

## SA System and Services Acquisition

Procedures PRO-SA-1 to PRO-SA-7.

### SA.1 Purpose

These procedures carry out \<Policy\> (SA). Steps marked **Manual** have no system support and rely on people. Each procedure names the record it leaves.

**Table SA-1: Procedures at a glance**

| Procedure | When | Who | Record | Controls |
| --- | --- | --- | --- | --- |
| PRO-SA-1 Developing a change | Every change | Developers, security officer | TPL-6 change record; the merge review | SA-3, SA-8, SA-10, SA-15 |
| PRO-SA-2 Testing a release | Each release | Developers, security officer | Test results with a README and a manifest, in the evidence for each family | SA-11 |
| PRO-SA-3 Buying a product or service | Each purchase; every 12 months for each external service | System owner | TPL-16 supplier review | SA-4, SA-9, SA-9(2) |
| PRO-SA-4 Documentation | Each release | Developers, system owner | \<Administrator Guide\> and \<User Guide\> change record | SA-5 |
| PRO-SA-5 Unsupported components | Monthly, and 6 months before support ends | Developers, authorising official | TPL-7; \<Maintenance Management\>, section 3.8 | SA-22, MA-6 |
| PRO-SA-6 Budgeting and reviews | Every 12 months | System owner, developers, security officer | TPL-23 | SA-2, SA-15 |
| PRO-SA-7 Adding a third-party component | Before a new package, browser library or script is added | Developers | TPL-6 change record | SA-4, SR-3, RA-3(1) |

### SA.2 Procedures

#### PRO-SA-1 Developing a change

1. Developers plan and design the change under \<Organisation\>'s corporate SDLC, against the CSS practices in \<System and Services Acquisition Management\>, section 3.2, and note its security and privacy effect on TPL-6. **Manual**
2. The security officer checks significant designs against the principles in \<System Description\>, section 6.8, and developers update the critical components in \<Risk Assessment Management\>, section 3.9, at each major change. **Manual**
3. Another developer reviews and approves the change before it merges through the protected branch.
4. The change follows \<Procedures\> (CM).

#### PRO-SA-2 Testing a release

1. A build pipeline runs unit, integration and security tests at each release, with the package vulnerability audit on.
2. Developers also run the test scripts in the developer test plan (\<System and Services Acquisition Management\>, section 3.9) in the test environment, a throwaway copy of the whole system built from the tagged release with invented data. **Manual**
3. Developers keep the results with a README and a manifest, in the evidence for the family, and raise each flaw in \<Risk List\> and \<Plan of Action and Milestones\>. **Manual**
4. The security officer confirms that each fixed flaw passes when the test is run again. **Manual**
5. Before go-live, and at each major release, the developers verify the web applications to OWASP ASVS 5.0 Level 2 (\<System Description\>, P-28), and record the result.

#### PRO-SA-3 Buying a product or service

1. The system owner uses \<Organisation\>'s standard contract, adding security and privacy requirements, documentation, responsibilities and acceptance criteria. **Manual** (EV-SA-01)
2. The contract or service terms state the controls, the provider's functions, ports, protocols and services, and the service levels with how they are measured and the remedies when they are missed. **Manual** (EV-SA-02, EV-SA-03)
3. Every 12 months the system owner reviews each external service in \<System and Services Acquisition Management\>, section 3.7, including the source repositories and the package feed, and records the review on TPL-16. **Manual**

#### PRO-SA-4 Documentation

1. At each release, developers confirm that \<Administrator Guide\> and \<User Guide\> still match \<System Name\>, and update them. **Manual**
2. The guides are shared with administrators, the security officer and users. **Manual**
3. The system owner records any missing supplier document, and chases it. **Manual**

#### PRO-SA-5 Unsupported components

1. The monthly check (\\<Security Operating Procedures\\>, C11) compares each component in \<Maintenance Management\>, section 3.8, with its vendor's support dates, and checks that each package and browser library is still maintained, is not deprecated, and has no known flaw without a fix. **Manual**
2. Developers plan a replacement at least 6 months before support ends. **Manual**
3. Any exception goes to the authorising official, with the risk stated. **Manual**

#### PRO-SA-6 Budgeting and reviews

1. Every 12 months the system owner raises security and privacy costs in yearly budgeting, and records them on TPL-23. **Manual**
2. Developers and the security officer review the tools, standards and CSS table, and record the result on TPL-23. **Manual**

#### PRO-SA-7 Adding a third-party component

1. Before adding a package, browser library or script, a developer checks its origin, licence, maintainer activity, support period and known vulnerabilities. **Manual**
2. The developer records the check on TPL-6, and pins the version in the lock file. **Manual**
3. The component is added to \<System Security Plan\>, section 3.4, and to the bill of materials. **Manual**

## SC System and Communications Protection

Procedures PRO-SC-1 to PRO-SC-8.

### SC.1 Purpose

These procedures carry out \<Policy\> (SC). The values, cryptographic register and allow-lists are in \<System and Communications Protection Management\>. Steps marked **Manual** have no support in the system.

**Table SC-1: Procedures at a glance**

| Procedure | When | Who | Record |
| --- | --- | --- | --- |
| PRO-SC-1 Setting up and checking TLS | When a VM is built, at each release, and every 12 months | Windows server administrator, database administrator, developers | TPL-6, TPL-8 |
| PRO-SC-2 Managing certificates | At issue, 30 days before expiry, and on compromise | Windows server administrator | TPL-6 |
| PRO-SC-3 Changing keys | At each key's cryptoperiod, when a holder leaves, and on suspected compromise | Windows server administrator, developers | TPL-6 |
| PRO-SC-4 Changing the boundary | Before a new flow, port, service or listening address | System owner, Windows server administrator | TPL-6, TPL-17 |
| PRO-SC-5 Checking page code | At each release | Developers | TPL-8 |
| PRO-SC-6 Responding to denial of service | When service is degraded by traffic | Security officer, \<Organisation\> | TPL-10 |
| PRO-SC-7 Testing encryption at rest | When a VM is built, and every 12 months | Windows server administrator, database administrator | TPL-11 |
| PRO-SC-8 Reviewing the register and boundary | Every 12 months | System owner, security officer, \<Organisation\> | TPL-23 |

### SC.2 Procedures

#### PRO-SC-1 Setting up and checking TLS

1. The Windows server administrator installs the certificates (PRO-SC-2) and configures the apps to serve HTTPS only, with TLS 1.3 preferred, TLS 1.2 limited to NCSC's GCM profiles, and SSL, TLS 1.0, TLS 1.1, compression and 0-RTT off (\<System and Communications Protection Management\>, section 3.3).
2. Developers make sure each app redirects HTTP, sends HSTS for at least 1 year, marks every cookie Secure, and calls API on the loopback address over HTTPS.
3. The database administrator sets SQL Server to strict encryption, with TLS 1.2 or later on TCP 1433, and to accept connections only from the application server. The API connects with Windows authentication, with full certificate and server name checking.
4. Developers run Test-Protection.ps1 against the VMs, and an outside TLS check against the web address, and file the results on TPL-8. **Manual**

#### PRO-SC-2 Managing certificates

1. The Windows server administrator requests each certificate from \<Organisation\>'s certificate authority, using ECDSA P-256 or RSA 2048-bit with SHA-256, and records it in the register. **Manual**
2. Renewal starts 30 days before expiry (\\<Security Operating Procedures\\>, C39), and the new certificate is installed through change control. **Manual**
3. A certificate whose key may be compromised is revoked and replaced at once, and the event is handled as an incident. **Manual**

#### PRO-SC-3 Changing keys

1. The register lists each key's cryptoperiod. When one is due, when a holder leaves, or when compromise is suspected, the owner changes the key and records the date, never the value, on TPL-6. **Manual**
2. The token signing key and the audit chain key are held only in the key store, never in source code or settings files.
3. Each app keeps its data protection key ring in its own folder, readable only by its service account and protected with Windows DPAPI at machine level. The folder is included in the server backup. Old keys are kept until every cookie they protected has expired.

#### PRO-SC-4 Changing the boundary

1. Anyone needing a new flow, port, external service or listening address raises a change on TPL-6, with its business need. **Manual**
2. The system owner approves it, updates \<System Security Plan\>, section 3.7, \<System Description\>, section 6.5, and the allow-lists in \<System and Communications Protection Management\>, section 3.2, before the rule is made. **Manual**
3. A temporary exception is recorded on TPL-17, with an end date, and removed when no longer needed. **Manual**
4. The Windows server administrator applies the host firewall rule, and \<Organisation\> applies any network rule.

#### PRO-SC-5 Checking page code

1. Developers serve every script and style from \<System Name\> itself.
2. Each app sends its security headers, with the page policy in \<System and Communications Protection Management\>, section 3.5.
3. At each release, developers run Test-Protection.ps1 (N04, N05, N10) and file the result on TPL-8. Any new mobile code needs the system owner's approval first. **Manual**

#### PRO-SC-6 Responding to denial of service

1. When the service slows or fails under traffic, the administrator on duty reports it to the security officer and to \<Organisation\>'s service desk. **Manual**
2. \<Organisation\> applies its network protections; the security officer records the incident on TPL-10 and checks the apps' rate limits.

#### PRO-SC-7 Testing encryption at rest

1. The Windows server administrator turns on BitLocker with XTS-AES 256 and the TPM on both VMs, and stores the recovery keys in \<Organisation\>'s protected store.
2. The database administrator encrypts backups and confirms that export copies are deleted.
3. Every 12 months, the administrators check that BitLocker is on and that a recovery key opens a test volume, and record it on TPL-11. **Manual**

#### PRO-SC-8 Reviewing the register and boundary

1. Every 12 months the system owner, the security officer and \<Organisation\>'s security contact review the cryptographic register, the allow-lists, the external services and any exceptions, and record the result on TPL-23. **Manual**
2. Keys or certificates near the end of their cryptoperiod, and algorithms that NCSC no longer recommends, are scheduled for change. **Manual**

## SI System and Information Integrity

Procedures PRO-SI-1 to PRO-SI-8.

### SI.1 Purpose

These procedures carry out \<Policy\> (SI). The values, detection use cases and retention table are in \<System and Information Integrity Management\>. Steps marked **Manual** have no support in the system.

**Table SI-1: Procedures at a glance**

| Procedure | When | Who | Record |
| --- | --- | --- | --- |
| PRO-SI-1 Fixing flaws | Monthly, at each release, and when an advisory applies | Developers, Windows server administrator, database administrator | TPL-7, TPL-6 |
| PRO-SI-2 Handling malicious code | Continuously, and on each detection | Windows server administrator, developers | TPL-10 |
| PRO-SI-3 Reviewing monitoring | Weekly | Security officer | TPL-8 |
| PRO-SI-4 Responding to an alert | On each alert | Security officer | TPL-10 |
| PRO-SI-5 Acting on advisories | Weekly, and as advisories arrive | Security officer | TPL-7 |
| PRO-SI-6 Checking integrity | At start-up, at each release and monthly | Windows server administrator, security officer | TPL-8 |
| PRO-SI-7 Managing information | As each retention period ends | System owner, database administrator | TPL-13 and the audit trail |
| PRO-SI-8 Testing integrity controls | At each release, after a significant change and at each review | Developers | TPL-8 |

### SI.2 Procedures

#### PRO-SI-1 Fixing flaws

1. Each month and at each release, developers run Test-Vulnerability.ps1, and the Windows server administrator reviews the Windows Update report from both VMs. **Manual**
2. The security officer records each flaw, its severity and its clock start on TPL-7. **Manual**
3. The person responsible tests the update in the test environment for its effect and side effects. **Manual**
4. They install it through the change process in \<Procedures\> (CM), within the timetable in \<Risk Assessment Management\>, section 3.6. **Manual**

#### PRO-SI-2 Handling malicious code

1. Defender updates daily, scans weekly and scans in real time on both VMs.
2. \<System Name\> passes each upload to Defender through AMSI before storing it, and refuses and audits anything flagged.
3. Defender quarantines what it finds on disk and alerts the Windows server administrator and security officer, who follow PRO-SI-4.
4. The Windows server administrator records false positives and how they were resolved on TPL-10. **Manual**

#### PRO-SI-3 Reviewing monitoring

1. Each week the security officer reviews the central logs, the forwarded application, Windows and SQL Server logs, and the alerts raised, but not the application audit log, which only auditors read (PRO-AU-1), apart from the last sign-in report (FR-085), against the detection use cases in \<System and Information Integrity Management\>, section 3.4.
2. They record what was reviewed and anything found on TPL-8. **Manual**
3. The system owner raises monitoring when risk rises, and takes the legal adviser's opinion before monitoring users in a new way. **Manual**

#### PRO-SI-4 Responding to an alert

1. The security officer acknowledges the alert within one working day, and within one hour for a malware detection or an audit chain break. **Manual**
2. They decide whether it is an incident. If so, they follow \<Incident Response Management\>; if not, they record why on TPL-10. **Manual**
3. A false alarm that recurs leads to a change to the use case, through change control. **Manual**

#### PRO-SI-5 Acting on advisories

1. The security officer receives advisories from NCSC (including Early Warning), CISA, Microsoft for Windows Server, SQL Server and .NET, and the vendors of every other component, and checks CISA's Known Exploited Vulnerabilities catalogue weekly (\\<Security Operating Procedures\\>, C50). **Manual**
2. For each one that applies, they write an internal advisory note on TPL-7 and pass it to the administrators and developers. **Manual**
3. The fix follows PRO-SI-1. **Manual**

#### PRO-SI-6 Checking integrity

1. At start-up, at each release and monthly, the Windows server administrator checks release packages against the baseline in \<System and Information Integrity Management\>, section 3.5.
2. The security officer runs the audit chain check and the file checksum check at the same times.
3. An unexpected change is handled as an incident, and the item is restored from a trusted copy. **Manual**

#### PRO-SI-7 Managing information

1. The system owner applies \<System Name\>'s retention schedule (\<PII Processing Management\>, section 3.7) to items and outputs.
2. The database administrator keeps audit records for 12 months online and 12 months archived, and application logs for 30 days.
3. Disposal is recorded on TPL-13 and in the audit trail. **Manual**

#### PRO-SI-8 Testing integrity controls

1. Developers run Test-Integrity.ps1 in the test environment at each release, after a significant change and at each review, and file the result on TPL-8. **Manual**
2. Any new gap goes to \<Risk List\> and \<Plan of Action and Milestones\>. **Manual**

## SR Supply Chain Risk Management

Procedures PRO-SR-1 to PRO-SR-6.

### SR.1 Purpose

These procedures carry out \<Policy\> (SR). Steps marked **Manual** rely on people. The values, supplier register and team are in \<Supply Chain Risk Management\>.

**Table SR-1: Procedures at a glance**

| Procedure | When | Who | Record | Controls |
| --- | --- | --- | --- | --- |
| PRO-SR-1 Bringing in a component | Before a package or browser library is added or updated | Developers | TPL-6 change record | SR-3, SR-5, SR-11 |
| PRO-SR-2 Reviewing suppliers and the plan | Every 12 months, and before a new critical supplier is used | System owner, supply chain team | TPL-16 supplier review | SR-2, SR-2(1), SR-6 |
| PRO-SR-3 Inspecting a release | At each release, and when tampering is suspected | Developers, security officer | Test-SupplyChain.ps1 results; TPL-6 | SR-10, SR-3 |
| PRO-SR-4 Authenticity and counterfeits | When a component is suspected | Anyone; security officer | TPL-10 incident record | SR-11, SR-11(1), SR-11(2) |
| PRO-SR-5 Notices and advisories | When a supplier reports a compromise or publishes an advisory | Security officer | TPL-7 vulnerability and patch review | SR-8 |
| PRO-SR-6 Disposal | Before a component leaves \<System Name\>'s control | Windows server administrator; \<Organisation\> | PRO-MP-3 sanitisation record; \<Organisation\>'s disposal confirmation | SR-12 |

### SR.2 Procedures

#### PRO-SR-1 Bringing in a component

1. A developer checks the component's origin, publisher, licence, maintainer activity, support period and known vulnerabilities, as \<Procedures\>, PRO-SA-7 requires, and checks the package ID against look-alikes. **Manual**
2. The developer adds the package and everything it pulls in to the in-house checked package feed, which records its SHA-256 value, and restores only from the feed.
3. The developer updates the lock file, and confirms the restore passes the signed-package trust policy and NuGet's audit.
4. A browser library is packaged with \<System Name\> and served by it, never from a content delivery service or other outside host.
5. The developer records the change on TPL-6, and the system owner adds any new supplier to the register in \<Supply Chain Risk Management\>, section 3.5. **Manual**

#### PRO-SR-2 Reviewing suppliers and the plan

1. Every 12 months, and before a new critical supplier is used, the supply chain team reviews each critical supplier with TPL-16: the questions cover how it builds and protects what it supplies, how it reports problems, and its support period. **Manual**
2. For \<Organisation\>, the team uses the evidence in EV-SR-01 and EV-SR-02. For open-source suppliers, it uses their published security policy and advisory history. **Manual**
3. The team updates the supplier register and the plan, and records any new risk in \<Risk List\>. **Manual**
4. The system owner approves the updated plan and keeps it in the restricted store. **Manual**

#### PRO-SR-3 Inspecting a release

1. A developer produces the release's bill of materials, with each component's version, supplier, hash and licence.
2. A developer runs Test-SupplyChain.ps1, which checks the package sources, lock files, trust policy, feed index and bill of materials, confirms that no page loads a script or style from an outside host, and compares the release packages and assemblies with the recorded SHA-256 baseline (\<System and Information Integrity Management\>, section 3.5). **Manual**
3. Before installation, the Windows server administrator checks the release's SHA-256 values against the release record.
4. The security officer reviews any mismatch as a suspected incident under \<Procedures\> (IR). **Manual**

#### PRO-SR-4 Authenticity and counterfeits

1. Anyone who suspects a counterfeit or look-alike component, hardware or software, stops using it and tells the security officer. **Manual**
2. The security officer records it on TPL-10, tells \<Organisation\>, and for software reports it to the package's publisher or registry, such as NuGet, and, if serious, to the NCSC. **Manual**
3. \<Organisation\> inspects hardware, trains its buyers yearly, and keeps control of equipment sent for repair. **Manual** (EV-SR-02)

#### PRO-SR-5 Notices and advisories

1. \<Organisation\> reports a compromise to the security officer within 24 hours. **Manual** (EV-SR-01)
2. For open-source suppliers, the security officer treats their published advisories as notice, through the sources in \<System and Information Integrity Management\>, section 3.3. **Manual**
3. The security officer records each notice that applies on TPL-7, and follows \<Procedures\> (IR) for a compromise. **Manual**

#### PRO-SR-6 Disposal

1. \<System Name\> data is removed following \<Procedures\>, PRO-MP-3, before anything leaves. **Manual**
2. \<Organisation\> disposes of the component, and confirms in writing. **Manual** (EV-SR-02)
