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

Each kind of personal data has an Article 6 lawful basis, and special category data an Article 9 condition and, where needed, a Schedule 1 condition. They are recorded in the inventory in section 3.3, and the legal adviser sets each. Where a Schedule 1, Part 1 condition is relied on, an appropriate policy document is put in place.

Consent is not the lawful basis for employee data, because employees cannot freely refuse their employer, as the ICO's guidance on employment records says. So there is no consent tool. \<System Name\> sets only strictly necessary cookies, which need no consent banner.

\<System Name\> makes no decision about a person by automated means alone, and does no profiling, so UK GDPR Article 22 does not apply. Personal data is not sold, shared with third parties for their own purposes, or transferred outside the United Kingdom.

The controls that rest on United States law and federal bodies do not apply: the Privacy Act, Federal Register notices, Social Security numbers, the First Amendment and computer matching. \<Organisation\> operates in the United Kingdom (\<Tailoring Register\>, TR-PT-01).

### 3.3 Personal data inventory

Controls met here: AU-3(3), PT-2, PT-3, PT-7, SI-12(1).

One row for each kind of personal data. The first rows come from the information types in the application profile (\<System Description\>, Table 6); the HR wording is an example. The last rows are held by every application built on the reference system. The legal adviser sets each basis and condition. No data is transferred outside the UK, and no processor outside \<Organisation\> is used. The inventory must match \<Organisation\>'s record of processing (UK GDPR, Article 30; EV-PM-02).

**Table 1: Personal data inventory**

| Kind of data | Where | Source | Purpose | Article 6 basis | Article 9 and Schedule 1 condition | Recipients | Retention |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \[Information type 1\], for example HR records: contract, pay, absence, performance | Items in \[schema\] | Editors' uploads | \[Purpose\] | \[Legal adviser\] | Not applicable | Members of the schema's read and edit groups | Section 3.7, H1 to H4 |
| \[Special category data, if any\], for example health records | Items in \[schema\], marked as special category data | Editors' uploads | \[Purpose\] | \[Legal adviser\] | \[Legal adviser; appropriate policy document if Schedule 1, Part 1 applies\] | Members of that schema's read and edit groups only | Section 3.7, H5 |
| \[Information type 2\], for example names and contact details in other items | Items in \[schema\] | Editors' uploads | \[Purpose\] | \[Legal adviser\] | Not applicable | Members of the schema's read and edit groups | \[Period for the schema\] |
| People who sign in: name and Active Directory account name, and the groups the API reads from Active Directory over LDAPS | Each sign-in, held in the authentication cookie; the audit records; items, such as who created or uploaded an item | PingFederate's signed response (the name) and Active Directory (the groups), at each sign-in | Signing in and accountability | \[Legal adviser\] | Not applicable | Administrators, auditors | Section 3.7, A1 |
| Audit records: username, user ID, IP address and browser | The audit log in the \<System Name\> database (\<Audit and Accountability Management\>, section 3.5) | \<System Name\> | Accountability and security | \[Legal adviser\] | Not applicable | Auditors | Section 3.7, A2 |
| Application log: designed to hold no personal data (no usernames, addresses or cookie values), listed so that any slip is caught | Each application's log on the application server, forwarded to central logging (\<Audit and Accountability Management\>, section 3.10) | \<System Name\> | Troubleshooting | \[Legal adviser\] | Not applicable | Server administrators, auditors | Section 3.7, A3 |
| Export copies | Users' managed devices; the encrypted working area on the application server | Bulk export | Sharing items for work | As the source item | As the source item | The exporting user | 30 days at most on devices (\\<Security Operating Procedures\\>, A28); working copies deleted once downloaded, and always within 24 hours (\<System Description\>, P-20) |

### 3.4 Special category data

Controls met here: PT-7.

Health and other special category data may be held only in schemas the business owner authorises, and only by the members of those schemas' read and edit groups, whom the schema's Data Owner authorises in ServiceNow. The schema access checks enforce this. Each item that holds it is marked as special category data, so that it can be found and handled with care. The conditions that allow the processing are set by the legal adviser (section 3.3).

### 3.5 Transparency

Controls met here: PT-3, PT-5.

\<Organisation\>'s employee privacy notice tells people how their data is used. \<Organisation\> gives it to each employee on joining. It must name \<System Name\> and its purposes, give the authority and lawful basis, be in plain language, and be reviewed every 12 months. People sign in on \<Organisation\>'s PingFederate page, so \<System Name\>'s own pages link to the notice, with a short statement of what \<System Name\> records about its users: their name, the groups they belong to, and what they do. The notice is asked of \<Organisation\> (EV-PT-01).

### 3.6 People's rights

Controls met here: AC-3(14), SI-18(4).

**Table 2: Requests and complaints**

| Request | What happens | Who | Within | Record |
| --- | --- | --- | --- | --- |
| To see their data, and a copy of it | The legal adviser confirms the person's identity, and the legal adviser's delegate makes a reasonable and proportionate search of every schema, using the audited search across schemas that only that named role may use (\<System Description\>, FR-073). An auditor searches the audit records, which only auditors read | Legal adviser; the legal adviser's delegate; an auditor | One month (\<System Description\>, P-22), extendable as the law allows | TPL-15 |
| To correct or delete their data | On the legal adviser's instruction, an editor of the schema or an administrator makes the change, and the legal adviser confirms it in writing. Each change is audited | Legal adviser; editor or administrator | One month | TPL-15; audit records |
| To restrict or object to the use of their data, or to receive it in a portable form | The legal adviser decides whether the right applies and how it is met, for example by limiting who can reach an item while a dispute about its accuracy is settled | Legal adviser; the schema's Data Owner | One month | TPL-15 |
| To complain about how their data is handled | The legal adviser acknowledges the complaint, investigates without undue delay, keeps the person informed and tells them the outcome. Any weakness found is raised as a risk | Legal adviser | Acknowledged within 30 days | TPL-22 |

The time allowed starts once the person's identity is confirmed, and pauses while the legal adviser waits for any clarification the request needs, as the Data (Use and Access) Act 2025 allows. When data is corrected, deleted or restricted, the legal adviser tells anyone it was disclosed to, unless that is impossible or would take disproportionate effort (UK GDPR, Article 19).

Requests and complaints follow PRO-PT-1.

### 3.7 Minimisation, quality, retention and disposal

Controls met here: SA-8(33), SI-12(1), SI-12(2), SI-12(3), SI-18, SI-19.

1. **Minimisation.** What personal data is collected is reviewed at design, in each change record, and in the impact assessment. Each schema holds only the personal data its items' purpose requires.
2. **Quality.** Every 12 months each Data Owner checks that their schema's personal data is accurate, relevant, timely and complete, and no more than its items' purpose requires, and records the check on TPL-3 (PRO-PT-5). An editor of the schema or an administrator corrects or deletes inaccurate or out-of-date data, and each correction and deletion is audited.
3. **Retention.** Each kind of record is kept for the period below, then disposed of. A retention period is set on each schema or item type, and a scheduled task lists the items due (\<System Description\>, FR-074). Rows H1 to H5 are examples for a schema of HR records, and are replaced by the record types in the application profile. The business owner sets each period with the legal adviser, guided by the ICO's employment records guidance. Row A1 covers names held from sign-in through PingFederate, and its period is set by the business owner.
4. **Disposal.** At the end of its period an item is deleted once the business owner approves its deletion in the UI application (\<System Description\>, FR-074), the deletion is audited, and the space it held in the database is cleared afterwards so that no readable copy remains. Media are sanitised as \<Media Protection Management\>, section 3.6 sets out.
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
| A1 | Names of people held from sign-in, in items, such as who created or uploaded an item | \[Period\] | The person leaves | \[Reason\] | Delete or anonymise |
| A2 | Audit records | 24 months: 12 online and 12 in an offline archive | Record created | AU-11, as set in \<Audit and Accountability Management\> and \<System Description\>, P-07 | Archive, then delete |
| A3 | Application log | 30 days | Log written | As set in \<Audit and Accountability Management\>, section 3.10 | Rotated and deleted |
| A4 | Training records (TPL-9) and the training register | 3 years | Training completed | AT-4, as set in \<Awareness and Training Management\> (AT-04\_ODP) | Delete |
| A5 | Maintenance records (TPL-12) | 3 years | Job completed | MA-2, as set in \<Maintenance Management\>, section 3.3 | Delete |
| A6 | Media records (TPL-13) | 3 years | Action completed | MP-6, as set in \<Media Protection Management\>, section 3.6 | Delete |
| A7 | Signed rules of behaviour (TPL-21) and the register of signatures | While the person has access, and 3 years after | Access ended | PL-4, as set in \<Planning Management\>, section 3.5 | Delete |
| A8 | Personnel security register entries | While the person has access, and 3 years after | Access ended | PS-3, as set in \<Personnel Security Management\>, section 3.9 | Delete |
| A9 | Leaver and mover records (TPL-14) | 3 years | Record completed | PS-4, PS-5, as set in \<Personnel Security Management\>, section 3.9 | Delete |
| A10 | Privacy requests (TPL-15) | 3 years | Request closed | Covers a complaint to the ICO about how a request was handled, and matches the other records | Delete |
| A11 | Data protection complaints (TPL-22) | 3 years | Complaint closed | Covers a complaint to the ICO about how a complaint was handled, and matches the other records | Delete |

### 3.8 Impact assessment and changes in processing

Controls met here: PT-3, RA-8, SA-8(33).

The data protection impact assessment, \<Data Protection Impact Assessment\>, follows the ICO's sample template. The legal adviser completes and approves it before production, with the advice of the data protection officer, and reviews it after any significant change in processing and every 12 months. Its measures go into the Plan of Action and Milestones, and its residual risks to the authorising official. If a high risk remains, the legal adviser consults the ICO before processing starts.

Every change record says whether the change affects personal data, through change control (\<Configuration Management\>, section 3.7). If it does, the legal adviser reviews it, and decides whether the inventory, the privacy notice or the impact assessment must change, and whether the change, such as a new collection of personal data, needs a new or revised impact assessment (PRO-PT-3, PRO-PT-4).

### 3.9 Privacy controls held in other documents

Controls met here: AT-3(5), AU-3(3), IR-2(3), IR-8(1), PE-8(3), PL-9, SC-7(24).

Eight of the privacy baseline controls are assessed with this family, but part of their design belongs with another. Table 4 says where the design of each is held.

**Table 4: Where the other privacy controls are designed**

| Control | Where its design is held | What it covers |
| --- | --- | --- |
| AC-3(14) Individual Access | This document, section 3.6 | The route through the legal adviser |
| AT-3(5) Processing PII | \<Awareness and Training Management\>, section 3.4, module M9 | The privacy module, for everyone who handles items holding personal data and all administrators, before access and every 12 months |
| AU-3(3) Limit PII Elements | \<Audit and Accountability Management\> | What audit records may hold: username, user ID, IP address and browser, with free text built from fixed wording and identifiers, and no personal data in the application log |
| IR-2(3) Breach | \<Awareness and Training Management\>, modules M7 and M9; \<Incident Response Management\>, section 3.4 | Breach training: module M7 for incident roles, and module M9 for everyone who handles items holding personal data, on recognising a breach, reporting it within 1 hour (\<System Description\>, P-21), and the breach steps |
| IR-8(1) Breaches | \<Incident Response Management\>, section 3.8 | The breach steps: the legal adviser and the security officer judge the harm and what would reduce it, and the legal adviser decides whether to tell the ICO and the people affected. UK GDPR Articles 33 and 34 apply: a report to the ICO within 72 hours of becoming aware, telling people when the risk to them is high, and recording every breach |
| PE-8(3) Limit PII Elements | \<Physical and Environmental Protection Management\> | What visitor records may hold: name, organisation, and the date and time of the visit |
| PL-9 Central Management | \<Planning Management\> | The one document set: policies, plans, registers and records under one owner, checked by one consistency test, and kept in the restricted store |
| SC-7(24) PII | This document, section 3.11 | Processing rules and monitoring |

### 3.10 What \<Organisation\> provides

Controls met here: PE-8(3), PT-1, PT-2, PT-3, PT-5, RA-8.

**Table 5: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| The employee privacy notice | PT-3, PT-5 | It names \<System Name\> and its purposes, and is reviewed every 12 months | EV-PT-01 |
| The record of processing | PT-2 | It lists the personal data \<System Name\> holds, matching section 3.3 | EV-PM-02 |
| The privacy programme and the data protection officer | PT-1, RA-8 | A data protection officer advises on the impact assessment, or the reason none is required is recorded | EV-PM-04 |
| Visitor records | PE-8(3) | They hold only name, organisation, and the date and time of the visit | EV-PT-02 |

### 3.11 Processing rules and monitoring

Controls met here: SC-7(24).

1. **Processing rules.** Schema access, through each schema's read group and edit group, and the measures in the impact assessment, are the rules for processing personal data. \<System Name\>'s schema access checks and audit records enforce them.
2. **Monitoring.** Exports and downloads are audited, and the auditors review the audit log weekly (\<System Description\>, P-08) and report anything suspicious to the security officer. An export above a set size raises an alert. The impact assessment decides what further monitoring is needed at external interfaces and key internal boundaries.
3. **Exceptions.** Each processing exception is approved and recorded in the exception register (\<Security Operating Procedures\>, section 5). Exceptions are reviewed at each access review, and removed when they are no longer supported.

### 3.12 Policy and procedures

Controls met here: PT-1.

\<Policy\> (PT) and \<Procedures\> (PT) meet PT-1. Who they are shared with is in \<Policy\>, section PT.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
