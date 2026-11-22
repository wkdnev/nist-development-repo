# \<System Name\> PII Processing Management

## 1 Purpose

This document sets out how \<System Name\> is designed to process personal data lawfully, openly and no more than it needs, to meet the 6 Personally Identifiable Information Processing and Transparency (PT) controls that apply and the 16 other controls of the CSS privacy baseline. CSS places none of the PT controls in the Moderate baseline. \<System Name\> applies the privacy baseline because it holds personal data: at least the sign-in identities in its audit records, and whatever its information types hold (\<System Description\>, section 3.4), which may include special category data.

Section 3 is the design: the authority, purposes and lawful basis; every kind of personal data \<System Name\> holds; special category data; the privacy notice; people's rights; minimisation, quality, retention and disposal; the impact assessment; where the privacy controls held in other documents are designed; what \<Organisation\> provides; the processing rules and monitoring; and the policy and procedures. Each subsection names the controls it helps to meet.

UK law decides what is lawful. The CSS controls set out how it is shown. Where a value needs a legal decision, it is a placeholder for the legal adviser.



## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.14 (Table 23). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (PT). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (PT), and the steps people follow are in \<Procedures\> (PT). Two documents sit beside this one and are owned by the legal adviser: the privacy plan, \<Privacy Plan\>, which PL-2 calls for, and the data protection impact assessment, \<Data Protection Impact Assessment\>.

## 3 The design

### 3.1 Principles

Controls met here: AC-3(14), PT-2, PT-3, RA-8, SA-8(33).

1. **Lawful and known purpose.** Personal data is processed only for a stated purpose, with a recorded lawful basis and, for special category data, a recorded condition.
2. **Only what is needed, only as long as needed.** \<System Name\> holds no more personal data than the purpose requires, for no longer than the retention schedule allows.
3. **People's rights.** People can see, correct and ask to delete their data, and complain, as the law allows.
4. **Assess before relying on it.** The impact assessment comes before production and before any significant change.

These carry out the principles and rules of \<Policy\>, sections PT.3 and PT.4.

![Figure 1: The life of personal data in \<System Name\>](figures/ptm-figure-1.png)

**Figure 1: The life of personal data in \<System Name\>**

### 3.2 Authority, purposes and lawful basis

Controls met here: PT-2, PT-3, PT-4, PT-5(2), PT-6, PT-6(1), PT-6(2), PT-7(1), PT-7(2), PT-8.

The authority is UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025 (\<System Description\>, P-31). Personal data is processed only for the purposes stated in the application profile (\<System Description\>, sections 3.1 and 3.4): \[Purposes, for example HR administration\], and accountability for the use of \<System Name\>. Processing means storing, finding, displaying, printing and exporting items, within schema access. Each schema's read group and edit group limit who processes its items, and the rules of behaviour on personal data (\<Security Operating Procedures\>, rules A23 to A29) keep processing to what is compatible with the stated purposes.

Each kind of personal data has an Article 6 lawful basis, and special category data an Article 9 condition and, where needed, a Schedule 1 condition. Criminal offence data, such as a conduct record about an offence, also needs a Schedule 1 condition under Article 10 and section 10 of the Data Protection Act 2018, and is handled as special category data is (section 3.4). They are recorded in the inventory in section 3.3, and the legal adviser sets each. Where a Schedule 1, Part 1 condition is relied on, an appropriate policy document is put in place.

Consent is not the lawful basis for employee data, because employees cannot freely refuse their employer, as the ICO's guidance on employment records says. So there is no consent tool. \<System Name\> sets only strictly necessary cookies, which need no consent banner.

\<System Name\> makes no decision about a person by automated means alone, and does no profiling, so UK GDPR Article 22 does not apply. Personal data is not sold, shared with third parties for their own purposes, or transferred outside the United Kingdom. No processor outside \<Organisation\> handles it in normal operation. A supplier sees or receives personal data only to give support, with the legal adviser's agreement, under a contract with UK GDPR Article 28 terms, and holding it in the UK (\<Maintenance Management\>, section 3.7; \<Procedures\>, PRO-MA-7).

The controls that rest on United States law and federal bodies do not apply: the Privacy Act, Federal Register notices, Social Security numbers, the First Amendment and computer matching. \<Organisation\> operates in the United Kingdom (\<Tailoring Register\>, TR-PT-01).

### 3.3 Personal data inventory

Controls met here: AU-3(3), PT-2, PT-3, PT-7, SI-12(1).

One row for each kind of personal data. The first rows come from the information types in the application profile (\<System Description\>, Table 6); the HR wording is an example. The other rows are held by every application built on the reference system. The legal adviser sets each basis and condition. No data is transferred outside the UK, and no processor outside \<Organisation\> is used, except a supplier giving support under the terms in section 3.2. The inventory must match \<Organisation\>'s record of processing (UK GDPR, Article 30; EV-PM-02).

**Table 1: Personal data inventory**

| Kind of data | Where | Source | Purpose | Article 6 basis | Article 9 and Schedule 1 condition | Recipients | Retention |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \[Information type 1\], for example HR records: contract, pay, absence, performance | Items in \[schema\] | Editors' uploads | \[Purpose\] | \[Legal adviser\] | Not applicable | Members of the schema's read and edit groups | Section 3.7, H1 to H4 |
| \[Special category data, if any\], for example health records | Items in \[schema\], marked as special category data | Editors' uploads | \[Purpose\] | \[Legal adviser\] | \[Legal adviser; appropriate policy document if Schedule 1, Part 1 applies\] | Members of that schema's read and edit groups only | Section 3.7, H5 |
| \[Information type 2\], for example names and contact details in other items | Items in \[schema\] | Editors' uploads | \[Purpose\] | \[Legal adviser\] | Not applicable | Members of the schema's read and edit groups | \[Period for the schema\] |
| People who sign in: name and Active Directory account name, and the groups the API reads from Active Directory over LDAPS | Each sign-in, held in the authentication cookie; the audit records; items, such as who created or uploaded an item | PingFederate's signed response (the name) and Active Directory (the groups), at each sign-in | Signing in and accountability | \[Legal adviser\] | Not applicable | Readers and editors of the schema, for the names on its items; auditors, for the audit records; the security officer, for the usernames and dates in the last sign-in report (\<System Description\>, FR-085). Administrators see neither item content nor the audit log | Section 3.7, A1 and A2 |
| Audit records: username, user ID, IP address and browser | The audit log in the \<System Name\> database (\<Audit and Accountability Management\>, section 3.5) | \<System Name\> | Accountability and security | \[Legal adviser\] | Not applicable | Auditors; the security officer sees only the usernames and dates in the last sign-in report (FR-085) | Section 3.7, A2 |
| Application log: the username in the short security events, and no other personal data (no addresses or cookie values), listed so that any slip is caught | Each application's log on the application server, forwarded to central logging (\<Audit and Accountability Management\>, section 3.10) | \<System Name\> | Troubleshooting and security alerts | \[Legal adviser\] | Not applicable | Server administrators on the server; the auditor and the security officer in central logging | Section 3.7, A3 |
| Personnel security records of people with access: name, role, risk designation, who confirmed screening and the dates, agreement and signature dates, and leaver and mover records | The personnel security register, the register of signatures, TPL-14 and TPL-21, kept by the system owner with the other records (\<Record Templates\>) | The person, \<Organisation\> (the confirmation only) and the system owner | Personnel security and the rules of behaviour (PS-2 to PS-6, PL-4) | \[Legal adviser\] | Not applicable: no screening result or criminal record data is held (\<Policy\> (PS), R4) | System owner; assessors | Section 3.7, A7 to A9 |
| Fault reports and notifications: the reporter's name and the description they write, and each person's own notifications | Fault reports in each schema (\<System Description\>, FR-026 to FR-029); notifications (FR-053 to FR-055) | Readers, and \<System Name\> | Managing faulty items; telling people of their own jobs | \[Legal adviser\] | Not applicable | Readers and editors of the schema, for its fault reports; the person alone, for their notifications | Section 3.7, A13 and A14 |
| Records of privacy requests and complaints: the person's identity and contact details, what they asked or complained of, what was found and the reply | TPL-15 and TPL-22, kept by the legal adviser | The person, and the legal adviser's work | Meeting people's rights and handling complaints | \[Legal adviser\] | \[Legal adviser: any condition, if a request or complaint reveals special category data\] | Legal adviser; the legal adviser's delegate for the search; assessors | Section 3.7, A10 and A11 |
| Incident and breach records: the people involved or affected, and what happened | TPL-10 in ServiceNow, and the incident and breach register (\<Incident Response Management\>, sections 3.8 and 3.14) | Reporters, the security officer and the legal adviser | Handling incidents and breaches, and recording every breach (UK GDPR, Article 33(5)) | \[Legal adviser\] | \[Legal adviser, if a record holds special category or criminal offence data\] | The incident roles; the ICO and the people affected, through the legal adviser | Section 3.7, A15 |
| Other operating records that name people: training, maintenance and media records, access reviews, exceptions, sharing decisions, home working checks and sign-off sheets (TPL-3, TPL-9, TPL-12, TPL-13, TPL-17, TPL-24, TPL-25 and TPL-26) | The restricted records store, kept by the system owner (\<Record Templates\>) | The people named, and the role holders who keep each record | Running and evidencing the controls | \[Legal adviser\] | Not applicable | The role holders who keep each record; assessors | Section 3.7, A4 to A6 and A16 |
| Database backups, holding every item and audit record, including items since deleted | \<Organisation\>'s backup service, at both sites, with one copy offline or immutable (\<Contingency Planning Management\>, section 3.8) | \<System Name\> | Recovery | As the source data | As the source data | Nobody reads them: they are encrypted and restored only for recovery or a restore test | Section 3.7, A12 |
| Support copies: a log, screenshot or data copy sent to a supplier, only where personal data cannot be removed | The supplier's systems, in the UK | \<System Name\> | Support | As the source data | As the source data | The supplier, under a contract with UK GDPR Article 28 terms | Until no longer needed; the supplier confirms deletion (PRO-MA-7) |
| Export copies | Users' managed devices; the encrypted working area on the application server | Bulk export | Sharing items for work | As the source item | As the source item | The exporting user | 30 days at most on devices (\<Security Operating Procedures\>, A28); working copies deleted once downloaded, and always within 24 hours (\<System Description\>, P-20) |

### 3.4 Special category data

Controls met here: PT-7.

Health and other special category data may be held only in schemas the business owner authorises, and only by the members of those schemas' read and edit groups, whom the schema's Data Owner authorises in ServiceNow. The schema access checks enforce this. Each item that holds it is marked as special category data (\<System Description\>, FR-035), so that it can be found and handled with care. Criminal offence data is handled in the same way: kept only in schemas the business owner authorises for it, and its items given the same marking. The conditions that allow the processing are set by the legal adviser (section 3.3), with an appropriate policy document where Schedule 1, Part 1 or Part 3 needs one.

### 3.5 Transparency

Controls met here: PT-3, PT-5.

\<Organisation\>'s privacy notices tell people how their data is used. Each group of people whose data \<System Name\> holds must be covered by one: employees by the employee privacy notice, given to each on joining; contractors and agency staff by the notice \<Organisation\> gives them; and anyone else an information type holds data about, such as former employees or people named in documents, by the notice the legal adviser names for them, or a recorded reason under UK GDPR, Article 14(5) why none is given. Each notice must name \<System Name\> and its purposes, give the authority and lawful basis, hold the information UK GDPR, Articles 13 and 14 require, including how to make a request or complaint and the right to complain to the ICO, be in plain language, and be reviewed every 12 months (\<System Description\>, P-73).

People sign in on \<Organisation\>'s PingFederate page, so \<System Name\>'s home page and About page link to the notice, with a short statement of what \<System Name\> records about its users: their name, the groups they belong to, and what they do (\<System Description\>, FR-010). The notice is therefore available when a person joins and every time they use \<System Name\>. The notices are asked of \<Organisation\> (EV-PT-01).

### 3.6 People's rights

Controls met here: AC-3(14), SI-18(4).

**Table 2: Requests and complaints**

| Request | What happens | Who | Within | Record |
| --- | --- | --- | --- | --- |
| To see their data, and a copy of it | The legal adviser confirms the person's identity, and the legal adviser's delegate makes a reasonable and proportionate search of every schema, using the audited search across schemas that only that named role may use (\<System Description\>, FR-073). An auditor searches the audit records, which only auditors read | Legal adviser; the legal adviser's delegate; an auditor | One month (\<System Description\>, P-22), extendable as the law allows | TPL-15 |
| To correct or delete their data | On the legal adviser's instruction, an editor of the schema makes the change with the correct and delete functions (\<System Description\>, FR-075), and the legal adviser confirms it in writing. Administrators see no item content, so cannot. Each change is audited | Legal adviser; an editor of the schema | One month | TPL-15; audit records |
| To restrict or object to the use of their data, or to receive it in a portable form | The legal adviser decides whether the right applies and how it is met, for example by limiting who can reach an item while a dispute about its accuracy is settled | Legal adviser; the schema's Data Owner | One month | TPL-15 |
| To complain about how their data is handled | The legal adviser acknowledges the complaint, investigates without undue delay, keeps the person informed and tells them the outcome. Any weakness found is raised as a risk | Legal adviser | Acknowledged within 30 days | TPL-22 |

The time allowed starts once the person's identity is confirmed, and pauses while the legal adviser waits for any clarification the request needs, as the Data (Use and Access) Act 2025 allows. When data is corrected, deleted or restricted, the legal adviser tells anyone it was disclosed to, unless that is impossible or would take disproportionate effort (UK GDPR, Article 19). The recipients outside a schema are found from the Data Owners' sharing decisions (TPL-25), which record what was shared, with whom and why, and the same records give the recipients a reply to a request must name. The export and download audit records show who took copies, from which schema and how many items, but not which items, so they narrow the search rather than settle it.

Requests and complaints follow PRO-PT-1.

### 3.7 Minimisation, quality, retention and disposal

Controls met here: SA-8(33), SI-12(1), SI-12(2), SI-12(3), SI-18, SI-19.

1. **Minimisation.** What personal data is collected is reviewed at design, in each change record, and in the impact assessment. Each schema holds only the personal data its items' purpose requires.
2. **Quality.** Every 12 months each Data Owner checks that their schema's personal data is accurate, relevant, timely and complete, and no more than its items' purpose requires, and records the check on TPL-3 (PRO-PT-5). An editor of the schema corrects or deletes inaccurate or out-of-date data (FR-036, FR-038), and each correction and deletion is audited. Administrators see no item content, so take no part.
3. **Retention.** Each kind of record is kept for the period below, then disposed of. A retention period is set on each schema or item type, and a scheduled task lists the items due (\<System Description\>, FR-074). Rows H1 to H5 are examples for a schema of HR records, and are replaced by the record types in the application profile. The business owner sets each period with the legal adviser, guided by the ICO's employment records guidance. Row A1 covers the names held from sign-in in items, which stay with the item for accountability and are disposed of with it.
4. **Disposal.** At the end of its period an item is deleted once the business owner approves its deletion in the UI application (\<System Description\>, FR-074), the deletion is audited, and the space it held in the database is cleared afterwards so that no readable copy remains in the live database. Copies remain in the encrypted backups until they expire, at most 12 months later (row A12). They are beyond use there: the backups are held apart, encrypted, and restored only for recovery or a restore test, and a recovery deletes the item again before users return (\<Contingency Planning Management\>, section 3.7). The same applies to an item deleted after a person's request, and the legal adviser says so in the reply where it matters to the person. Media are sanitised as \<Media Protection Management\>, section 3.6 sets out.
5. **Testing, training and research.** Testing and training use invented data only, loaded into each test environment, and no real personal data is used for research.
6. **De-identification.** No dataset is de-identified or released, so there is nothing to remove identifiers from.

**Table 3: Retention schedule**

| ID | Record type | Period | Trigger | Basis for the period | Disposal |
| --- | --- | --- | --- | --- | --- |
| H1 | \[Record type 1\], for example employment contract and changes | \[Period\] | End of employment | \[Reason\] | Delete and audit |
| H2 | \[Record type 2\], for example pay and pension records | \[Period\] | End of the tax year | \[Reason\] | Delete and audit |
| H3 | \[Record type 3\], for example absence and leave records | \[Period\] | End of the absence | \[Reason\] | Delete and audit |
| H4 | \[Record type 4\], for example performance, conduct and grievance records | \[Period\] | Close of the matter | \[Reason\] | Delete and audit |
| H5 | \[Special category record type, if any\], for example health and occupational health records | \[Period\] | End of employment | \[Reason\] | Delete and audit |
| A1 | Names of people held from sign-in, in items, such as who created or uploaded an item | As the item that holds it | The item's own trigger | Accountability for the item, which outlasts the person's employment (FR-040) | Deleted with the item (FR-074) |
| A2 | Audit records | 24 months: 12 online and 12 in an offline archive | Record created | AU-11, as set in \<Audit and Accountability Management\> and \<System Description\>, P-07 | Archive, then delete |
| A3 | Application log | 30 days | Log written | As set in \<Audit and Accountability Management\>, section 3.10 | Rotated and deleted |
| A4 | Training records (TPL-9) and the training register | 3 years | Training completed | AT-4, as set in \<Awareness and Training Management\> (AT-04\_ODP) | Delete |
| A5 | Maintenance records (TPL-12) | 3 years | Job completed | MA-2, as set in \<Maintenance Management\>, section 3.3 (P-67) | Delete |
| A6 | Media records (TPL-13) | 3 years | Action completed | MP-6, as set in \<Media Protection Management\>, section 3.6 | Delete |
| A7 | Signed rules of behaviour (TPL-21) and the register of signatures | While the person has access, and 3 years after | Access ended | PL-4, as set in \<Planning Management\>, section 3.5 | Delete |
| A8 | Personnel security register entries | While the person has access, and 3 years after | Access ended | PS-3, PS-6, as set in \<Personnel Security Management\>, section 3.9 | Delete |
| A9 | Leaver and mover records (TPL-14) | 3 years | Record completed | PS-4, PS-5, as set in \<Personnel Security Management\>, section 3.9 | Delete |
| A10 | Privacy requests (TPL-15) | 3 years | Request closed | Covers a complaint to the ICO about how a request was handled, and matches the other records | Delete |
| A11 | Data protection complaints (TPL-22) | 3 years | Complaint closed | Covers a complaint to the ICO about how a complaint was handled, and matches the other records | Delete |
| A12 | Database backups, holding every item, including items since deleted | 14 daily, 8 weekly and 12 monthly copies | Backup taken | CP-9, as set in \<Contingency Planning Management\>, section 3.8, and \<System Description\>, P-15 | Expired copies deleted at both sites by \<Organisation\>'s backup service; at the end of the system, method M2 |
| A13 | Fault reports, with the reporter's name | As the item the report concerns | The item's own trigger | Kept while the item is | Deleted with the item. \[Developers to confirm that FR-038 and FR-074 remove an item's fault reports\] |
| A14 | Notifications | \[Period\] | Notification created | Only as long as the person needs it | Removed by the scheduled task (FR-055) |
| A15 | Incident records (TPL-10) and the incident and breach register | \[Period, set by the legal adviser\] | Incident closed | Shows what happened and that every breach was recorded (UK GDPR, Article 33(5)) | Delete |
| A16 | Other operating records that name people (TPL-3, TPL-17, TPL-24, TPL-25 and TPL-26) | \[Period, set by the system owner; 3 years proposed, to match the other records\] | Record completed or superseded | Evidence of the controls for the assessment cycle | Delete |

### 3.8 Impact assessment and changes in processing

Controls met here: PT-3, RA-8, SA-8(33).

The data protection impact assessment, \<Data Protection Impact Assessment\>, follows the ICO's sample template. The legal adviser completes and approves it before production, with the advice of the data protection officer, and reviews it after any significant change in processing and every 12 months. Its measures go into the Plan of Action and Milestones, and its residual risks to the authorising official. If a high risk remains, the legal adviser consults the ICO before processing starts.

Every change record says whether the change affects personal data, through change control (\<Configuration Management\>, section 3.7). If it does, the legal adviser reviews it, and decides whether the inventory, the privacy notice or the impact assessment must change, and whether the change, such as a new collection of personal data, needs a new or revised impact assessment (\<Configuration Management\>, section 3.9; PRO-PT-3, PRO-PT-4).

### 3.9 Privacy controls held in other documents

Controls met here: AT-3(5), AU-3(3), IR-2(3), IR-8(1), PE-8(3), PL-9, SC-7(24).

Eight of the privacy baseline controls are assessed with this family, but part of their design belongs with another. Table 4 says where the design of each is held.

**Table 4: Where the other privacy controls are designed**

| Control | Where its design is held | What it covers |
| --- | --- | --- |
| AC-3(14) Individual Access | This document, section 3.6 | The route through the legal adviser |
| AT-3(5) Processing PII | \<Awareness and Training Management\>, sections 3.3 to 3.5: briefing part B6 and module M9 | Privacy training for every user in briefing part B6, and the privacy module M9 for the roles in the training matrix, including all administrators and the auditor; each before access and every 12 months |
| AU-3(3) Limit PII Elements | \<Audit and Accountability Management\>, section 3.4, with the elements named in the impact assessment | What audit records may hold: username, user ID, IP address and browser, with free text built from fixed wording and identifiers; data-change records name the fields changed but never their values, and deletion records hold none of the item's content; and no personal data in the application log beyond the username in a security event |
| IR-2(3) Breach | \<Awareness and Training Management\>, briefing part B6 and modules M7 and M9; \<Incident Response Management\>, section 3.4 | Breach training: module M7 for incident roles, module M9 for the roles in the training matrix, and briefing part B6 for every user, on recognising a breach, reporting it within 1 hour (\<System Description\>, P-21), and the breach steps |
| IR-8(1) Breaches | \<Incident Response Management\>, section 3.8 | The breach steps: the legal adviser and the security officer judge the harm and what would reduce it, and the legal adviser decides whether to tell the ICO and the people affected. UK GDPR Articles 33 and 34 apply: a report to the ICO within 72 hours of becoming aware, telling people when the risk to them is high, and recording every breach |
| PE-8(3) Limit PII Elements | \<Physical and Environmental Protection Management\>, section 3.10, with the elements named in the impact assessment | What visitor records may hold: name, organisation, and the date and time of the visit |
| PL-9 Central Management | \<Planning Management\> | The one document set: policies, plans, registers and records under one owner, checked by one consistency test, and kept in the restricted store (until the store is set up, the private records repository; \<Documentation Map\>, section 4.1) |
| SC-7(24) PII | This document, section 3.11 | Processing rules and monitoring |

### 3.10 What \<Organisation\> provides

Controls met here: PE-8(3), PT-1, PT-2, PT-3, PT-5, RA-8.

**Table 5: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| The privacy notices for employees, contractors and agency staff | PT-3, PT-5 | Each names \<System Name\> and its purposes, gives the lawful basis and the information in UK GDPR, Articles 13 and 14, is given on joining, and is reviewed every 12 months | EV-PT-01 |
| The record of processing | PT-2 | It lists the personal data \<System Name\> holds, matching section 3.3 | EV-PM-02 |
| The privacy programme and the data protection officer | PT-1, RA-8 | A data protection officer advises on the impact assessment, or the reason none is required is recorded | EV-PM-04 |
| Visitor records | PE-8(3) | They hold only name, organisation, and the date and time of the visit | EV-PT-02 |

### 3.11 Processing rules and monitoring

Controls met here: SC-7(24).

1. **Processing rules.** Schema access, through each schema's read group and edit group, and the measures in the impact assessment, are the rules for processing personal data. \<System Name\>'s schema access checks and audit records enforce them.
2. **Monitoring.** Permitted processing is monitored at the external interfaces, where data leaves \<System Name\>: every view, download and export by a user's browser is audited, an export above a set size raises an alert (FR-052), and the logs sent to central logging carry no personal data beyond the username in a security event. It is monitored at the key internal boundaries: the API, the only route to the data, checks schema access and audits every item access; and SQL Server Audit records any read of the item tables by a login other than the API's. The auditors review the audit log and those records weekly (\<System Description\>, P-08) and report anything suspicious to the security officer. The impact assessment decides whether further monitoring is needed.
3. **Exceptions.** Each processing exception is approved and recorded in the exception register (\<Security Operating Procedures\>, section 5). Exceptions are reviewed at each access review, and removed when they are no longer supported.

### 3.12 Policy and procedures

Controls met here: PT-1.

\<Policy\> (PT) and \<Procedures\> (PT) meet PT-1. Who they are shared with is in \<Policy\>, section PT.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
