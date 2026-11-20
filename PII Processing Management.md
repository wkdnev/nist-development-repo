# \<System Name\> PII Processing Management

## 1 Purpose

This document shows how \<System Name\> processes personal data lawfully, openly and no more than it needs, for each of the 6 Personally Identifiable Information Processing and Transparency (PT) controls that apply and the 16 other controls of the CSS privacy baseline. CSS places none of the PT controls in the Moderate baseline. \<System Name\> applies the privacy baseline because it holds HR documents with personal data, some of it special category data (D-PT-01, D-PT-07).

Section 3 sets out the design: the authority, purposes and lawful basis; every kind of personal data \<System Name\> holds; special category data; the privacy notice; people's rights; minimisation, quality, retention and disposal; the impact assessment; where the privacy controls held in other documents are; and what \<Organisation\> provides. Section 4 takes each control in turn. Appendix A lists every value CSS asks the organisation to define, and appendix B the related enhancements CSS does not select.

The policy is in \<Policy\> (PT), and the steps people follow are in \<Procedures\> (PT). Two documents sit beside this one and are owned by the legal adviser: the privacy plan, \<Privacy Plan\>, which PL-2 calls for, and the data protection impact assessment, \<Data Protection Impact Assessment\>.

UK law decides what is lawful. The CSS controls set out how it is shown. Where a value needs a legal decision, it is a placeholder for the legal adviser.

An assessor examines the inventory and the lawful basis for each kind of data, the impact assessment, the notice, the retention schedule and the records of requests, complaints and disposals; interviews the legal adviser, the business owner and an administrator who would handle a request; and tests what \<System Name\> holds, logs and keeps (CSS). So for each control section 4 gives:

- **each part of the control**, as CSS letters them, with the design that meets it and the position today;
- **who provides it**, and who is responsible;
- **what enforces it**, the rules and procedures that apply, and the tests run;
- **the records an assessor will ask for**, and whether they exist yet;
- **its status**, the risk decision, and what is still open.

**Table 1: Status values**

| Status | Meaning |
| --- | --- |
| Implemented | The design is in place and working |
| Partially implemented | Some of the design is in place; the open items say what is missing |
| Not implemented | None of the design is in place yet |
| Not applicable | The control does not apply, by a recorded decision |

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.14 (Table 23). This section gives only the overall position.

No control in the privacy baseline is missing from the design. Every gap is registered in the Risk List (\<Risk List\>) and the Plan of Action and Milestones (\<Plan of Action and Milestones\>).

Two things matter most. The legal adviser has not yet confirmed the lawful basis and conditions, or completed the impact assessment (PA-72, rated Medium), so the legal footing of the processing is drafted but not decided. And \<System Name\> cannot yet serve people's rights in full: it cannot search every project for one person, it does not audit corrections and deletions in the admin portal (PA-89, Medium), and it cannot keep a document for a set period and then dispose of it (PA-70, Medium). The authorising official decided that both must be fixed before production or before real personal data is held (D-PT-14, D-PT-15).

## 3 The design

### 3.1 Principles

1. **Lawful and known purpose.** Personal data is processed only for a stated purpose, with a recorded lawful basis and, for special category data, a recorded condition.
2. **Only what is needed, only as long as needed.** \<System Name\> holds no more personal data than the purpose requires, for no longer than the retention schedule allows.
3. **People's rights.** People can see, correct and ask to delete their data, and complain, as the law allows.
4. **Assess before relying on it.** The impact assessment comes before production and before any significant change.

These carry out the principles and rules of \<Policy\>, sections PT.3 and PT.4.

![Figure 1: The life of personal data in \<System Name\>](figures/ptm-figure-1.png)

**Figure 1: The life of personal data in \<System Name\>**

### 3.2 Authority, purposes and lawful basis

The authority is UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025 (D-PT-09). Personal data is processed for two purposes only: HR administration, and managing project documents. Processing means storing, finding, displaying, printing and exporting documents, within project permissions.

Each kind of personal data has an Article 6 lawful basis, and special category data an Article 9 condition and, where needed, a Schedule 1 condition. They are recorded in the inventory in section 3.3, and the legal adviser confirms each (D-PT-20). Where a Schedule 1, Part 1 condition is relied on, an appropriate policy document is put in place.

Consent is not the lawful basis for employee data, because employees cannot freely refuse their employer (D-PT-10). So there is no consent tool. \<System Name\> sets only strictly necessary cookies, which need no consent banner (check Q07).

\<System Name\> makes no decision about a person by automated means alone, and does no profiling, so UK GDPR Article 22 does not apply. Personal data is not sold, shared with third parties for their own purposes, or transferred outside the United Kingdom.

### 3.3 Personal data inventory

One row for each kind of personal data. The legal adviser confirms each basis and condition (D-PT-20). No data is transferred outside the UK, and no processor outside \<Organisation\> is used. The inventory must match \<Organisation\>'s record of processing (UK GDPR, Article 30; EV-PM-02).

**Table 2: Personal data inventory**

| Kind of data | Where | Source | Purpose | Article 6 basis | Article 9 and Schedule 1 condition | Recipients | Retention |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HR records: contract, pay, absence, performance | HR project documents | HR team uploads | HR administration | \[Legal adviser\] | Not applicable | HR project members | Section 3.7, H1 to H4 |
| Health and other special category data | HR project documents | HR team uploads | HR administration | \[Legal adviser\] | \[Legal adviser; appropriate policy document if Schedule 1, Part 1 applies\] | HR project members only | Section 3.7, H5 |
| Names and contact details | Other project documents | Project uploads | Managing project documents | \[Legal adviser\] | Not applicable | Project members | The project's period |
| People who sign in: name and Active Directory account name, and the AD groups in the sign-in token | Each session; the audit records; document records such as who uploaded or last changed a document | AD FS, at each sign-in | Signing in and accountability | \[Legal adviser\] | Not applicable | Global administrators, auditors | Section 3.7, A1 |
| Audit records: username, user ID, IP address, user agent, session ID | The audit log in the \<System Name\> database (\<Audit and Accountability Management\>, section 3.5) | \<System Name\> | Accountability and security | \[Legal adviser\] | Not applicable | Auditors, security officer | Section 3.7, A2 |
| Application log | Each application's log on the application server (\<Audit and Accountability Management\>, section 3.10) | \<System Name\> | Troubleshooting | \[Legal adviser\] | Not applicable | Administrators | Section 3.7, A3; personal data to be removed (PA-75) |
| Export copies | Users' managed devices; server temporary folder | Bulk export | Sharing documents for work | As the source document | As the source document | The exporting user | 30 days at most (SyOps A28); server copies removed (PA-86) |

### 3.4 Special category data

Health and other special category data may be held only in HR projects the business owner authorises, and only by the people approved for those projects. Each document that holds it is marked as special category data, so that it can be found and handled with care. \<System Name\> cannot yet mark documents in this way (Q01; PA-89), and the conditions that allow the processing are placeholders for the legal adviser (PA-72).

### 3.5 Transparency

\<Organisation\>'s employee privacy notice tells people how their data is used. It must name \<System Name\> and its two purposes, give the authority and lawful basis, be in plain language, and be reviewed every 12 months. People sign in on \<Organisation\>'s AD FS page, so \<System Name\>'s own pages link to the notice, with a short statement of what \<System Name\> records about its users: their name, the groups they belong to, and what they do (PA-90). The notice has not been seen (EV-PT-01).

### 3.6 People's rights

**Table 3: Requests and complaints**

| Request | What happens | Who | Within | Record |
| --- | --- | --- | --- | --- |
| To see their data, and a copy of it | The legal adviser confirms the person's identity, and an administrator the legal adviser names makes a reasonable and proportionate search of every project and the audit records | Legal adviser; a named administrator | One month, extendable as the law allows | TPL-15 |
| To correct or delete their data | The project access approver or an administrator makes the change, and confirms it in writing. Each change is to be audited | Legal adviser; project access approver or administrator | One month | TPL-15; audit records |
| To restrict or object to the use of their data, or to receive it in a portable form | The legal adviser decides whether the right applies and how it is met, for example by limiting a document to fewer people while a dispute about its accuracy is settled | Legal adviser; project access approver | One month | TPL-15 |
| To complain about how their data is handled | The legal adviser acknowledges the complaint, investigates without undue delay, keeps the person informed and tells them the outcome. Any weakness found is raised as a risk | Legal adviser | Acknowledged within 30 days | TPL-22 |

The time allowed starts once the person's identity is confirmed, and pauses while the legal adviser waits for any clarification the request needs, as the Data (Use and Access) Act 2025 allows. When data is corrected, deleted or restricted, the legal adviser tells anyone it was disclosed to, unless that is impossible or would take disproportionate effort (UK GDPR, Article 19).

Until \<System Name\> can search every project for one person in one step, each project is searched in turn and listed. Until the admin portal audits corrections and deletions, the administrator records the document, the field and the change on TPL-15 (PA-89).

### 3.7 Minimisation, quality, retention and disposal

1. **Minimisation.** What personal data is collected is reviewed at design, in each change record, and in the impact assessment. Each project holds only what its documents' purpose requires.
2. **Quality.** Every 12 months each project access approver checks that their project's personal data is accurate, relevant, timely and complete, and records the check on TPL-3. Inaccurate or out-of-date data is corrected or deleted.
3. **Retention.** Each kind of record is kept for the period below, then disposed of. The business owner sets each period with the legal adviser (D-PT-21), guided by the ICO's employment records guidance (February 2025). Row A1 was reworded for sign-in through AD FS and confirmed by the system owner on 18 November 2026 (D-PT-23); its period stays with the business owner.
4. **Disposal.** At the end of its period a document is deleted, the deletion is audited, and the database is vacuumed afterwards so that no readable copy remains. \<System Name\> cannot yet do this (Q03, Q08; PA-70).

**Table 4: Retention schedule**

| ID | Record type | Period | Trigger | Basis for the period | Disposal |
| --- | --- | --- | --- | --- | --- |
| H1 | Employment contract and changes | \[Period\] | End of employment | \[Reason\] | Delete and audit |
| H2 | Pay and pension records | \[Period\] | End of the tax year | \[Reason\] | Delete and audit |
| H3 | Absence and leave records | \[Period\] | End of the absence | \[Reason\] | Delete and audit |
| H4 | Performance, conduct and grievance records | \[Period\] | Close of the matter | \[Reason\] | Delete and audit |
| H5 | Health and occupational health records | \[Period\] | End of employment | \[Reason\] | Delete and audit |
| A1 | Names of people held from sign-in, in document records such as who uploaded or last changed a document | \[Period\] | The person leaves | \[Reason\] | Delete or anonymise |
| A2 | Audit records | 24 months: 12 online and 12 archived | Record created | AU-11, as set in \<Audit and Accountability Management\> | Archive, then delete |
| A3 | Application log | 30 days | Log written | As set in \<Audit and Accountability Management\>, section 3.10 | Rotated and deleted |
| A4 | Training records (TPL-9) and the training register | 3 years | Training completed | AT-4, as set in \<Awareness and Training Management\> (AT-04\_ODP) | Delete |
| A5 | Maintenance records (TPL-12) | 3 years | Job completed | MA-2, as set in \<Maintenance Management\>, section 3.3 (D-MP-11) | Delete |
| A6 | Media records (TPL-13) | 3 years | Action completed | MP-6, as set in \<Media Protection Management\>, section 3.6 (D-MP-11) | Delete |
| A7 | Signed rules of behaviour (TPL-21) and the register of signatures | While the person has access, and 3 years after | Access ended | PL-4, as set in \<Planning Management\>, section 3.5 (D-PL-14) | Delete |
| A8 | Personnel security register entries | While the person has access, and 3 years after | Access ended | PS-3, as set in \<Personnel Security Management\>, section 3.9 (D-PS-12) | Delete |
| A9 | Leaver and mover records (TPL-14) | 3 years | Record completed | PS-4, PS-5, as set in \<Personnel Security Management\>, section 3.9 (D-PS-12) | Delete |
| A10 | Privacy requests (TPL-15) | 3 years | Request closed | Covers a complaint to the ICO about how a request was handled, and matches the other records. Set by the system owner (D-PT-24), for the legal adviser to confirm | Delete |
| A11 | Data protection complaints (TPL-22) | 3 years | Complaint closed | Covers a complaint to the ICO about how a complaint was handled, and matches the other records. Set by the system owner (D-PT-24), for the legal adviser to confirm | Delete |

### 3.8 Impact assessment and changes in processing

The data protection impact assessment, \<Data Protection Impact Assessment\>, follows the ICO's sample template. The legal adviser completes and approves it before production, with the advice of the data protection officer, and reviews it after any significant change in processing and every 12 months. Its measures go into the Plan of Action and Milestones, and its residual risks to the authorising official. If a high risk remains, the legal adviser consults the ICO before processing starts.

Every change record says whether the change affects personal data. If it does, the legal adviser reviews it, and decides whether the inventory, the privacy notice or the impact assessment must change.

### 3.9 Privacy controls held in other documents

Eight of the privacy baseline controls are assessed with this family, but part of their design belongs with another. Each is set out in section 4, and its design is held where the table says.

**Table 5: Where the other privacy controls are designed**

| Control | Where its design is held | What it covers |
| --- | --- | --- |
| AC-3(14) Individual Access | This document, section 3.6 | The route through the legal adviser |
| AT-3(5) Processing PII | \<Awareness and Training Management\>, section 3.4, module M9 | The privacy module |
| AU-3(3) Limit PII Elements | \<Audit and Accountability Management\> | What audit records may hold |
| IR-2(3) Breach | \<Awareness and Training Management\>, modules M7 and M9; \<Incident Response Management\>, section 3.4 | Breach training |
| IR-8(1) Breaches | \<Incident Response Management\>, section 3.8 | The breach steps and the ICO report |
| PE-8(3) Limit PII Elements | \<Physical and Environmental Protection Management\> | What visitor records may hold |
| PL-9 Central Management | \<Planning Management\> | The one document set |
| SC-7(24) PII | This document, section 4 | Processing rules and monitoring |

### 3.10 What \<Organisation\> provides

**Table 6: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked | State |
| --- | --- | --- | --- | --- |
| The employee privacy notice | PT-3, PT-5 | It names \<System Name\> and its purposes, and is reviewed every 12 months | EV-PT-01 | Not sent |
| The record of processing | PT-2 | It lists \<System Name\>'s HR personal data, matching section 3.3 | EV-PM-02 | Not sent |
| The privacy programme and the data protection officer | PT-1, RA-8 | A data protection officer advises on the impact assessment, or the reason none is required is recorded (D-PM-04) | EV-PM-04 | Not sent |
| Visitor records | PE-8(3) | They hold only name, organisation, and the date and time of the visit | EV-PT-02 | Not sent |

**Today:** no request has been sent, and none of this is evidenced.

## 4 Each control and enhancement

The controls are in CSS order: the PT controls first, then the other privacy baseline controls by family. Each has two tables. The first takes each part of the control and gives what CSS requires, the design that meets it, and the position today. The second says who provides and is responsible for the control, what enforces it, the rules and procedures that apply, the tests run, the records an assessor will ask for, its status, the risk decision, and what is still open.

### 4.1 PT-1 Policy and Procedures

**Table 7: PT-1 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a.1 | A personal data processing and transparency policy, shared with defined people, covering purpose, scope, roles, responsibilities, management commitment, coordination and compliance, and consistent with the law | \<Policy\> (PT): a system-level policy, shared with everyone who administers \<System Name\>. The legal adviser reviews it | Version \<ver\> approved by the Head of Cyber (D-PT-02) and legally reviewed on 11 November 2026. The later version awaits the Head of Cyber (D-PT-18). Not yet shared (PA-20) |
| a.2 | Procedures that carry out the policy, shared with defined people | \<Procedures\> (PT): six procedures, PRO-PT-1 to PRO-PT-6. Shared with the same people | Approved by the system owner (D-PT-19). Not yet shared or walked through |
| b | A named official manages the policy and procedures | The system owner | \[Name\] is named in \<Roles and Responsibilities\> |
| c.1 | The policy is reviewed on a schedule and after set events | Every 12 months, and after a significant incident, audit finding, change in the law or system change | Reviewed on 11 November 2026. The first yearly review falls due in November 2027 |
| c.2 | The procedures are reviewed on a schedule and after set events | Every 12 months, and after a change to the steps | As the policy |

**Table 8: PT-1 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner, Head of Cyber |
| Enforced by | Not a system function. The documents are under version control |
| Rules and procedures | The whole policy; all six procedures (\<Procedures\>) |
| Tests | None. Examined from the documents |
| Records an assessor will ask for | The policy and procedures with their approvals; proof they were shared; review records. The approvals exist |
| Status | Partially implemented |
| Risk decision | NC-PT-01, rated Low: approve |
| Open items | PA-20: share the policy and procedures. The Head of Cyber's approval of the later version (D-PT-18) |

### 4.2 PT-2 Authority to Process Personally Identifiable Information

**Table 9: PT-2 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Determine and document the legal authority that permits the processing of personal data | UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025. For each kind of data, the inventory records the Article 6 lawful basis and, for special category data, the Article 9 and Schedule 1 condition (section 3.3) | The authority is named (D-PT-09). Each basis and condition is a placeholder for the legal adviser (D-PT-20; PA-72) |
| b | Restrict processing to what that authority permits | Storing, finding, displaying, printing and exporting HR and project documents, within project permissions | Project permissions limit who processes each project's documents. What the legal adviser permits is not yet recorded |

**Table 10: PT-2 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Legal adviser |
| Enforced by | Project permissions in \<System Name\> |
| Rules and procedures | Policy rules R2, R3 (\<Policy\>, section PT.4); PRO-PT-3, PRO-PT-4 (\<Procedures\>) |
| Tests | Check Q07 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): only strictly necessary cookies are set before sign-in. It passed |
| Records an assessor will ask for | Each lawful basis and condition, confirmed by the legal adviser; the completed impact assessment. Neither exists yet |
| Status | Not implemented |
| Risk decision | NC-PT-02, rated Medium: remediate |
| Open items | PA-72: the legal adviser confirms each basis and condition |

### 4.3 PT-3 Personally Identifiable Information Processing Purposes

**Table 11: PT-3 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Identify and document the purposes for processing personal data | HR administration, and managing project documents | Stated (D-PT-09). The legal adviser has not confirmed them |
| b | Describe the purposes in public privacy notices and policies | \<Organisation\>'s employee privacy notice names \<System Name\> and both purposes (section 3.5) | The notice has not been seen (EV-PT-01) |
| c | Restrict processing to what is compatible with those purposes | Project permissions, and the rules of behaviour on personal data (\<Security Operating Procedures\>, rules A23 to A29) | Project permissions work in the tested build. The rules are not yet signed |
| d | Monitor changes in processing, and make sure they meet the requirements | Every change record says whether personal data is affected. The legal adviser reviews those that are, and decides whether the inventory, the notice or the impact assessment must change (PRO-PT-3) | Not yet used |

**Table 12: PT-3 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Legal adviser, system owner |
| Enforced by | Project permissions; change control (\<Configuration Management\>, section 3.7) |
| Rules and procedures | Policy rule R1 (\<Policy\>, section PT.4); PRO-PT-3 (\<Procedures\>) |
| Tests | Check Q05 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): the application log repeats personal data the audit trail already holds, beyond the purpose |
| Records an assessor will ask for | The purposes; the notice (EV-PT-01); change records that say whether personal data is affected |
| Status | Not implemented |
| Risk decision | NC-PT-03, rated Low: approve |
| Open items | PA-126: the legal adviser confirms the purposes, and \<Organisation\>'s notice is seen. PA-75: the application log |

### 4.4 PT-4 Consent

**Table 13: PT-4 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Provide tools for individuals to consent to the processing of their personal data | None. Consent is not the lawful basis for employee data, as employees cannot freely refuse their employer (D-PT-10), which is the ICO's guidance on employment records. Only strictly necessary cookies are set, so no cookie consent is needed | The position awaits the legal adviser's confirmation |

**Table 14: PT-4 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Legal adviser |
| Enforced by | Not applicable: no tool |
| Rules and procedures | Policy rule R2 (\<Policy\>, section PT.4); no procedure of its own (\<Procedures\>) |
| Tests | Check Q07 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): only strictly necessary cookies. It passed |
| Records an assessor will ask for | The legal adviser's written position on consent |
| Status | Not implemented |
| Risk decision | NC-PT-04, rated Low: approve |
| Open items | PA-126: the legal adviser confirms the position |

### 4.5 PT-5 Privacy Notice

**Table 15: PT-5 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Give notice when people first interact with the organisation, and at a defined frequency | \<Organisation\> gives its employee privacy notice on joining, and reviews it every 12 months. \<System Name\>'s pages link to it | The notice has not been seen (EV-PT-01). No page of the tested build linked to it (Q06; PA-90) |
| b | Make the notice clear, easy to understand and in plain language | \<Organisation\>'s notice, with a short statement on \<System Name\>'s pages of what \<System Name\> records about its users | Not seen. The statement is not written (PA-90) |
| c | Identify the authority for the processing | The notice names UK GDPR and the lawful basis | Not seen (EV-PT-01) |
| d | Identify the purposes | The notice names \<System Name\> and its two purposes | Not seen (EV-PT-01) |
| e | Include defined information | As \<Organisation\>'s notice, naming \<System Name\> and its purposes | Not seen (EV-PT-01) |

**Table 16: PT-5 responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\>, system owner |
| Enforced by | \<Organisation\>'s notice; a link from \<System Name\>'s pages, once built |
| Rules and procedures | Policy rule R8 (\<Policy\>, section PT.4); PRO-PT-3, step 3 (\<Procedures\>) |
| Tests | Check Q06 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): neither page linked to the notice |
| Records an assessor will ask for | The notice (EV-PT-01); \<System Name\>'s pages showing the link |
| Status | Not implemented |
| Risk decision | NC-PT-05, rated Low: obtain evidence |
| Open items | PA-90: link the notice from \<System Name\>'s pages. EV-PT-01: obtain the notice |

### 4.6 PT-7 Specific Categories of Personally Identifiable Information

**Table 17: PT-7 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Apply defined conditions to specific categories of personal data | Special category data is held only in projects the business owner authorises, under the Article 9 and Schedule 1 conditions in the inventory, with an appropriate policy document where Schedule 1, Part 1 is relied on. Those documents are marked as special category data (section 3.4) | Projects can be limited. The conditions are placeholders for the legal adviser (PA-72), and documents cannot yet be marked (Q01; PA-89) |

**Table 18: PT-7 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Business owner, legal adviser |
| Enforced by | Project permissions; a document marking, once built |
| Rules and procedures | Policy rules R2, R5 (\<Policy\>, section PT.4); PRO-PT-4 (\<Procedures\>) |
| Tests | Check Q01 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): HR documents carry no personal data marking |
| Records an assessor will ask for | The conditions and any appropriate policy document; the list of authorised special category projects |
| Status | Partially implemented |
| Risk decision | NC-PT-06, rated Medium: remediate |
| Open items | PA-72: confirm the conditions. PA-89: mark the documents |

### 4.7 AC-3(14) Individual Access

**Table 19: AC-3(14) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Give individuals a way to access their personal data | A request to the legal adviser, met within one month by a reasonable and proportionate search of every project and the audit records, recorded on TPL-15 (section 3.6) | The route is written. \<System Name\> cannot search every project for one person in one step, so each project is searched in turn (Q02; PA-89) |

**Table 20: AC-3(14) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Legal adviser |
| Enforced by | Not a system function today; a search across projects, once built |
| Rules and procedures | Policy rule R7 (\<Policy\>, section PT.4); PRO-PT-1 (\<Procedures\>) |
| Tests | Check Q02 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): no single search across projects |
| Records an assessor will ask for | TPL-15 for a sample of requests. None exist yet |
| Status | Partially implemented |
| Risk decision | NC-PT-07, rated Low: approve |
| Open items | PA-89: a complete, audited search across projects |

### 4.8 AT-3(5) Processing Personally Identifiable Information

**Table 21: AT-3(5) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Train defined people in protecting personal data, at first and at a defined frequency | Everyone who handles HR documents, and all administrators: before access and every 12 months. Module M9 of the role curriculum (\<Awareness and Training Management\>, section 3.4) | No training given. The module is not written (PA-97) |

**Table 22: AT-3(5) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function. The training register |
| Rules and procedures | Policy rule R10 (\<Policy\>, section PT.4); PRO-PT-6 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-9 records of module M9. None exist yet |
| Status | Not implemented |
| Risk decision | NC-PT-08, rated Low: approve |
| Open items | PA-97: write module M9 and train |

### 4.9 AU-3(3) Limit Personally Identifiable Information Elements

**Table 23: AU-3(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Limit the personal data in audit records to the elements identified in the privacy risk assessment | Username, user ID, IP address, user agent and session ID, and none in the application log (\<Audit and Accountability Management\>) | Audit free text holds no extra personal data (Q04). The application log repeats usernames and IP addresses (Q05; PA-75). The impact assessment that confirms the elements is a draft (PA-72) |

**Table 24: AU-3(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers, auditor |
| Enforced by | \<System Name\>'s audit service |
| Rules and procedures | The audit policy (\<Policy\> (AU)); no procedure of its own (\<Procedures\>) |
| Tests | Checks Q04 and Q05 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): Q04 passed; Q05 showed the gap |
| Records an assessor will ask for | A sample of audit records and application log lines |
| Status | Partially implemented |
| Risk decision | NC-PT-09, rated Low: remediate |
| Open items | PA-75: remove personal data from the application log. PA-71: review the audit free text |

### 4.10 IR-2(3) Breach

**Table 25: IR-2(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Include in incident response training how to identify and respond to a breach, and how to report it | Module M7 for incident roles, and module M9 for everyone who handles HR documents: recognising a breach, reporting it within 1 hour, and the steps in \<Incident Response Management\>, section 3.8 | Not given (PA-81, PA-97) |

**Table 26: IR-2(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer |
| Enforced by | Not a system function |
| Rules and procedures | Policy rules R9, R10 (\<Policy\>, section PT.4); PRO-PT-6, PRO-IR-3 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-9 records of modules M7 and M9. None exist yet |
| Status | Not implemented |
| Risk decision | NC-PT-10, rated Low: approve |
| Open items | PA-81, PA-97: write the modules and train |

### 4.11 IR-8(1) Breaches

**Table 27: IR-8(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Include in the incident response plan a process to decide whether to notify individuals or other organisations | The legal adviser decides whether to tell the ICO and the people affected (\<Incident Response Management\>, section 3.8) | Met: written and approved |
| b | Include an assessment of the harm, embarrassment, inconvenience or unfairness to the people affected, and how to reduce it | The legal adviser and the security officer judge the harm and what would reduce it (\<Incident Response Management\>, section 3.8, step 3) | Met |
| c | Identify the privacy requirements that apply | UK GDPR Articles 33 and 34: a report to the ICO within 72 hours of becoming aware, telling people when the risk to them is high, and recording every breach | Met |

**Table 28: IR-8(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Security officer, legal adviser |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R9 (\<Policy\>, section PT.4); PRO-PT-6; PRO-IR-5 (\<Procedures\>) |
| Tests | None. Examined from the plan |
| Records an assessor will ask for | \<Incident Response Management\>, section 3.8; the breach register in its section 3.14 |
| Status | Implemented |
| Risk decision | NC-PT-11, rated Low: approve; now satisfied |
| Open items | None |

### 4.12 PE-8(3) Limit Personally Identifiable Information Elements

**Table 29: PE-8(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Limit the personal data in visitor records to defined elements | Name, organisation, and the date and time of the visit (\<Physical and Environmental Protection Management\>) | Not seen (EV-PT-02; PA-122) |

**Table 30: PE-8(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<Organisation\> |
| Responsible | \<Organisation\> |
| Enforced by | \<Organisation\>'s visitor records |
| Rules and procedures | The physical protection policy (\<Policy\> (PE)); no procedure of its own (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | A blank visitor record (EV-PT-02) |
| Status | Not implemented |
| Risk decision | NC-PT-12, rated Low: obtain evidence |
| Open items | PA-122: obtain \<Organisation\>'s evidence |

### 4.13 PL-9 Central Management

**Table 31: PL-9 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Centrally manage defined controls and related processes | Policies, plans, registers and records are held in one document set, under one owner, checked by one consistency test, and kept in the restricted store (\<Planning Management\>) | One set and one test. Not yet in the restricted store (PA-88) |

**Table 32: PL-9 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | System owner |
| Enforced by | The plan consistency test |
| Rules and procedures | The planning policy (\<Policy\> (PL)), rule R5; PRO-PL-1, PRO-PL-6 (\<Procedures\>) |
| Tests | The plan consistency test, 24 checks on the whole set: all pass |
| Records an assessor will ask for | The document set; the access list of the restricted store |
| Status | Partially implemented |
| Risk decision | NC-PT-13, rated Low: approve |
| Open items | PA-88: move the set to the restricted store |

### 4.14 RA-8 Privacy Impact Assessments

**Table 33: RA-8 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Assess privacy impact before developing or procuring technology that processes personal data | \<Data Protection Impact Assessment\>, completed by the legal adviser with the data protection officer's advice, before production and after any significant change in processing, and reviewed every 12 months (section 3.8) | A draft exists. It is not complete (D-PT-20; PA-72) |
| b | Assess it before starting a new collection of personal data | The change check in PRO-PT-3 decides whether a change needs a new or revised assessment | Not yet used |

**Table 34: RA-8 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Legal adviser |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R4 (\<Policy\>, section PT.4); PRO-PT-4 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The completed and approved impact assessment, with its measures and residual risks |
| Status | Partially implemented |
| Risk decision | NC-PT-14, rated Medium: remediate |
| Open items | PA-72: complete the assessment |

### 4.15 SA-8(33) Minimization

**Table 35: SA-8(33) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Apply the privacy principle of minimisation, using defined processes | What is collected is reviewed at design, in each change record, and in the impact assessment | Not yet in use |

**Table 36: SA-8(33) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Developers, legal adviser |
| Enforced by | Not a system function |
| Rules and procedures | Principle P2 (\<Policy\>, section PT.3); PRO-PT-3 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | Change records showing the personal data question answered; the impact assessment |
| Status | Not implemented |
| Risk decision | NC-PT-15, rated Low: approve |
| Open items | PA-72: the impact assessment reviews it |

### 4.16 SC-7(24) Personally Identifiable Information

**Table 37: SC-7(24) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Apply defined processing rules to personal data | Project access permissions, and the measures in the impact assessment | Project permissions work in the tested build. The impact assessment is a draft |
| b | Monitor for permitted processing at external interfaces and key internal boundaries | Exports and downloads are audited, and the auditor reviews them each week. What further monitoring is needed is decided by the impact assessment | Not decided (PA-71) |
| c | Document each processing exception | Each exception is approved and recorded in the exception register (\<Security Operating Procedures\>, section 5) | Not yet used |
| d | Review and remove exceptions that are no longer supported | At each access review | Not yet used |

**Table 38: SC-7(24) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers, security officer |
| Enforced by | \<System Name\>'s project permissions and audit records |
| Rules and procedures | Policy rules R1, R2 (\<Policy\>, section PT.4); no procedure of its own (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | The processing rules; the exception register; the monitoring the impact assessment calls for |
| Status | Not implemented |
| Risk decision | NC-PT-16, rated Low: remediate |
| Open items | PA-71: decide the monitoring with the impact assessment |

### 4.17 SI-12(1) Limit Personally Identifiable Information Elements

**Table 39: SI-12(1) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Limit the personal data processed across the information life cycle to defined elements | Only what each document's purpose requires, as in the inventory. Each project access approver reviews the personal data in their project every 12 months (PRO-PT-5) | No project has been reviewed |

**Table 40: SI-12(1) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Business owner |
| Enforced by | Not a system function |
| Rules and procedures | Policy rule R3; principle P2 (\<Policy\>, section PT.4); PRO-PT-5 (\<Procedures\>) |
| Tests | None |
| Records an assessor will ask for | TPL-3 records of the yearly review |
| Status | Not implemented |
| Risk decision | NC-PT-17, rated Low: approve |
| Open items | PA-126: hold the first review |

### 4.18 SI-12(2) Minimize Personally Identifiable Information in Testing, Training, and Research

**Table 41: SI-12(2) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use defined techniques to minimise personal data in research, testing and training | Sample data only for testing and training, and no real personal data for research | Test stacks hold sample data only (Q09). The rule for training and research is not yet in use |

**Table 42: SI-12(2) responsibility and evidence**

| | |
| --- | --- |
| Provided by | Shared: \<System Name\> and \<Organisation\> |
| Responsible | Developers |
| Enforced by | The sample data loaded into each test stack |
| Rules and procedures | Policy rule R10 (\<Policy\>, section PT.4); PRO-PT-6 (\<Procedures\>) |
| Tests | Check Q09 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): sample data only. It passed |
| Records an assessor will ask for | The test results; the training material |
| Status | Partially implemented |
| Risk decision | NC-PT-18, rated Low: approve |
| Open items | PA-126: bring the rule into use for training |

### 4.19 SI-12(3) Information Disposal

**Table 43: SI-12(3) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Use defined techniques to dispose of, destroy or erase information after its retention period | At the end of its retention period (section 3.7) a document is deleted, the deletion is audited, and the database is vacuumed so that no readable copy remains. Media are sanitised by \<Media Protection Management\>, section 3.6 | Not built. No document can carry a retention period (Q08), and deleted pages stay until the database is vacuumed (Q03; PA-70). Most periods are not yet set (D-PT-21) |

**Table 44: SI-12(3) responsibility and evidence**

| | |
| --- | --- |
| Provided by | \<System Name\>: built into the system |
| Responsible | Developers, business owner |
| Enforced by | \<System Name\>, once retention and disposal are built |
| Rules and procedures | Policy rule R6 (\<Policy\>, section PT.4); PRO-PT-5 (\<Procedures\>) |
| Tests | Checks Q03 and Q08 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): both showed gaps |
| Records an assessor will ask for | The retention schedule; audit records of each disposal |
| Status | Not implemented |
| Risk decision | NC-PT-19, rated Medium: remediate |
| Open items | PA-70: build retention and disposal. D-PT-21: set the periods |

### 4.20 SI-18 Personally Identifiable Information Quality Operations

**Table 45: SI-18 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| a | Check the accuracy, relevance, timeliness and completeness of personal data at a defined frequency | Every 12 months each project access approver checks their project's personal data, and records it on TPL-3 (PRO-PT-5) | Not yet used. Policy rule R11 requires it, and awaits the Head of Cyber with the later version of the policy (D-PT-18) |
| b | Correct or delete personal data that is inaccurate or out of date | The project access approver or an administrator corrects or deletes it, and each correction and deletion is audited | Corrections and deletions in the admin portal write no audit record (Q03, Q10; PA-89) |

**Table 46: SI-18 responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Project access approvers |
| Enforced by | Not a system function today |
| Rules and procedures | Policy rule R11 (\<Policy\>, section PT.4); principle P3; PRO-PT-5 (\<Procedures\>) |
| Tests | Checks Q03 and Q10 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): corrections and deletions are not audited |
| Records an assessor will ask for | TPL-3 records of the yearly check; audit records of corrections |
| Status | Not implemented |
| Risk decision | NC-PT-20, rated Low: approve |
| Open items | PA-126: hold the first check. PA-89: audit corrections |

### 4.21 SI-18(4) Individual Requests

**Table 47: SI-18(4) design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | Correct or delete personal data when the person asks | Through the legal adviser (PRO-PT-1). The project access approver or an administrator makes the correction or deletion, and it is confirmed in writing on TPL-15. The legal adviser tells anyone the data was disclosed to (UK GDPR, Article 19) | The route is written. Corrections in the admin portal are not audited (Q10; PA-89) |

**Table 48: SI-18(4) responsibility and evidence**

| | |
| --- | --- |
| Provided by | People, following the procedures |
| Responsible | Legal adviser |
| Enforced by | Not a system function today |
| Rules and procedures | Policy rule R7 (\<Policy\>, section PT.4); PRO-PT-1 (\<Procedures\>) |
| Tests | Check Q10 (Test-PersonalData.ps1 on the v1.0 build, 11 November 2026): showed the gap |
| Records an assessor will ask for | TPL-15 for a sample of requests; audit records of each change |
| Status | Partially implemented |
| Risk decision | NC-PT-21, rated Low: approve; NC-PT-22, rated Medium: remediate |
| Open items | PA-89: audit corrections and deletions |

### 4.22 SI-19 De-identification

**Table 49: SI-19 design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | As CSS sets out for the control | Not applicable: No dataset is de-identified or released, so there is nothing to remove identifiers from | Not applicable |

**Table 50: SI-19 responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Decision | Not applicable, as assessed |

### 4.23 PT-5(2), PT-6, PT-6(1), PT-6(2), PT-7(1), PT-7(2), PT-8: United States requirements

**Table 51: United States requirements design**

| Part | CSS requires | Design | Today |
| --- | --- | --- | --- |
| All | As CSS sets out for the control | Not applicable: These rest on United States law and federal bodies: the Privacy Act, Federal Register notices, Social Security numbers, the First Amendment and computer matching. \<Organisation\> operates in the United Kingdom (\<Tailoring Register\>, TR-PT-01) | Not applicable |

**Table 52: United States requirements responsibility and evidence**

| | |
| --- | --- |
| Provided by | Not applicable |
| Status | Not applicable |
| Decision | TR-PT-01 |

## Appendix A Parameter register

These are the CSS organisation-defined values for the 6 assessed PT entries and the 16 other privacy controls: 41 in total. They were agreed on 6 November 2026 and restated as requirements on 11 November 2026 (D-PT-P01). Seven more PT entries are tailored as United States only (\<Tailoring Register\>, TR-PT-01).

**Table 53: Privacy parameter register**

| CSS identifier | What must be defined | Value |
| --- | --- | --- |
| PT-01\_ODP\[01\] | Who receives the policy | Everyone who administers \<System Name\> |
| PT-01\_ODP\[02\] | Who receives the procedures | Everyone who administers \<System Name\> |
| PT-01\_ODP\[03\] | Level of the policy | System level |
| PT-01\_ODP\[04\] | Official who manages them | System owner |
| PT-01\_ODP\[05\] | Policy review frequency | Every 12 months |
| PT-01\_ODP\[06\] | Events requiring policy review | Significant incident, audit finding, change in the law or system change |
| PT-01\_ODP\[07\] | Procedures review frequency | Every 12 months |
| PT-01\_ODP\[08\] | Events requiring procedures review | A change to the steps |
| PT-02\_ODP\[01\] | Authority | UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025, with the lawful basis and conditions for each kind of data in section 3.3 |
| PT-02\_ODP\[02\] | Processing permitted | Storing, finding, displaying, printing and exporting HR and project documents |
| PT-02\_ODP\[03\] | Processing restricted | To the purposes in PT-03\_ODP\[01\], within project permissions |
| PT-03\_ODP\[01\] | Purposes | HR administration and managing project documents |
| PT-03\_ODP\[02\] | Processing restricted to those purposes | Storing, finding, displaying, printing and exporting documents |
| PT-03\_ODP\[03\] | How changes are controlled | Each change record says whether personal data is affected; the legal adviser reviews those that are (PRO-PT-3) |
| PT-03\_ODP\[04\] | Requirements changes must meet | UK GDPR, \<Policy\> (PT) and \<Data Protection Impact Assessment\> |
| PT-04\_ODP | Consent tools | None, as consent is not the lawful basis for employee data |
| PT-05\_ODP\[01\] | Notice review frequency | Every 12 months |
| PT-05\_ODP\[02\] | Information in the notice | As \<Organisation\>'s employee privacy notice, naming \<System Name\> and its purposes, linked from \<System Name\>'s pages, as people sign in on \<Organisation\>'s AD FS page (PA-90) |
| PT-07\_ODP | Conditions for special categories | Only in projects the business owner authorises, with the Article 9 and Schedule 1 conditions in section 3.3 and the impact assessment |
| AC-03(14)\_ODP\[01\] | How individuals get access | A request to the legal adviser, met by a reasonable and proportionate search of every project within one month; complaints acknowledged within 30 days (PRO-PT-1) |
| AC-03(14)\_ODP\[02\] | What they can see | Their personal data in \<System Name\> documents, document records and audit records |
| AT-03(05)\_ODP\[01\] | Who gets privacy training | Everyone who handles HR documents, and all administrators |
| AT-03(05)\_ODP\[02\] | Frequency | Before access, and every 12 months |
| AU-03(03)\_ODP | Personal data allowed in audit records | Username, user ID, IP address, user agent and session ID; none in the application log (PA-75) |
| PE-08(03)\_ODP | Personal data allowed in visitor records | Name, organisation, and date and time of visit |
| PL-09\_ODP | What is centrally managed | Policies, plans, registers and records in this document set, in the restricted SharePoint area (PA-88) |
| SA-08(33)\_ODP | How data is minimised | What is collected is reviewed at design, in each change record, and in the impact assessment |
| SC-07(24)\_ODP | Processing rules | Project access permissions, and the measures in \<Data Protection Impact Assessment\> |
| SI-12(01)\_ODP | Elements processed | Only what each document's purpose requires, as in section 3.3 |
| SI-12(02)\_ODP\[01\] | Technique for research | No real personal data is used |
| SI-12(02)\_ODP\[02\] | Technique for testing | Sample data only |
| SI-12(02)\_ODP\[03\] | Technique for training | Sample data only |
| SI-12(03)\_ODP\[01\] | How information is disposed of | Deleted at the end of its retention period (section 3.7), with the deletion audited and the database vacuumed (PRO-PT-5) |
| SI-12(03)\_ODP\[02\] | How information is destroyed | \<Procedures\>, PRO-MP-3 |
| SI-12(03)\_ODP\[03\] | How information is erased | \<Procedures\>, PRO-MP-3 |
| SI-18\_ODP\[01\] | Accuracy check frequency | Every 12 months |
| SI-18\_ODP\[02\] | Relevance check frequency | Every 12 months |
| SI-18\_ODP\[03\] | Timeliness check frequency | Every 12 months |
| SI-18\_ODP\[04\] | Completeness check frequency | Every 12 months |
| SI-19\_ODP\[01\] | Elements removed | None, as no dataset is de-identified |
| SI-19\_ODP\[02\] | Evaluation frequency | Not applicable |

## Appendix B Privacy controls outside the privacy baseline

CSS does not select these enhancements in its privacy baseline, so they are not assessed. Some of the design goes some way towards them, and Table 54 says where. The United States controls that the baseline does select are tailored out in section 4.

**Table 54: Related enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| PT-2(1), PT-3(1), SI-18(2) Data Tagging; Data Tags | Tags on personal data that carry its permitted processing, purposes or quality | Not required. Done in part in design: HR documents are to be marked as personal or special category data (PA-89) |
| PT-2(2), PT-3(2), SI-18(1) Automation; Automation Support | Processing limits and quality checks enforced by automated means | Not required. Project permissions limit who processes each project's documents |
| PT-4(1), PT-4(2), PT-4(3) Tailored Consent; Just-in-time Consent; Revocation | Ways to give, refine and withdraw consent | Not required. Consent is not the lawful basis (D-PT-10) |
| PT-5(1) Just-in-time Notice | Notice given at the moment data is collected | Not required. Done in part in design: the short statement on \<System Name\>'s pages (PA-90) |
| SI-18(3) Collection | Personal data collected directly from the person where possible | Not required. HR collects employees' data from them; \<System Name\> stores the documents |
| SI-18(5) Notice of Correction or Deletion | People to whom data was disclosed are told of a correction or deletion | Not required. Done in design: the legal adviser tells them, as UK GDPR Article 19 requires (section 3.6) |
| SI-19(1) to SI-19(8) | Ways of de-identifying data | Not applicable. No dataset is de-identified (SI-19) |
