# \<System Name\> Data Protection Impact Assessment

## 1 Purpose and how to complete this assessment

This is the data protection impact assessment for \<System Name\> required before production (\<Policy\> (PT); CSS RA-8). It follows the steps of the ICO's sample DPIA template.

The facts about \<System Name\> are filled in from the design documents. Everything that is a legal judgement is shown in square brackets for the legal adviser: the lawful basis, the special category and Schedule 1 conditions, whether an appropriate policy document is needed, the final risk scores, and the decision.

## 2 Step 1: Why a DPIA is needed

\<System Name\> stores, finds and shows \<Organisation\>'s digital items, kept apart in schemas. It holds the sign-in identities in its audit records, and whatever personal data its information types hold (\<System Description\>, section 3.4): \[for example, employees' personal data in a Human Resources schema, which may include special category data such as health information\]. Where the people concerned are employees, they are in an unequal relationship with their employer, and processing special category data about employees is a factor the ICO lists as likely to need a DPIA. \[Legal adviser: confirm whether a DPIA is mandatory under UK GDPR, Article 35, or carried out as good practice.\]

## 3 Step 2: The processing

**Nature:** items are created or uploaded in bulk or one at a time, described by their catalogue details, searched within one schema at a time (except that the legal adviser's delegate searches every schema for one person's items to answer a request, FR-073), viewed on screen, downloaded, printed on managed printers, and exported in bulk by editors. Copies are also held in the encrypted backups, at \<Organisation\>'s backup service and second site, and the username in each security event goes to \<Organisation\>'s central logging. The role holders keep records that name people: requests, complaints, incidents, training, personnel security and other control records. The full inventory, with each kind of data, is in \<PII Processing Management\>, section 3.3.

**Scope:** \[number of people whose personal data is held\]; \[number of items\]; \[number of schemas\]. Data is kept until disposed of under the retention schedule in \<PII Processing Management\>, section 3.7.

**Context:** users are \<Organisation\> staff and contractors on managed devices in the UK. \<System Name\> runs on two Windows Server 2025 virtual servers in \<Organisation\>'s data centre, with its items in Microsoft SQL Server 2022. No data leaves the UK, and no processor outside \<Organisation\> is used in normal operation (see Transfers and processors below). People sign in through \<Organisation\>'s PingFederate, and the API reads their group memberships from Active Directory. ServiceNow and the starters and leavers process have no connection to \<System Name\>: people act on the access approvals and leaver notices they produce.

**Purposes:** \[the purposes set in the application profile and \<PII Processing Management\>\], and managing \<System Name\>'s items (\<Policy\> (PT)).

## 4 Step 3: Consultation

**Table 1: Consultation**

| Who | How | When | Outcome |
| --- | --- | --- | --- |
| Business and information owner, \[Name\] | Review of the inventory and retention schedule | \[Date\] | \[Outcome\] |
| Head of Cyber, \[Name\] | Review of the security measures | \[Date\] | \[Outcome\] |
| Data protection officer | Advice on the whole assessment | \[Date\] | \[Outcome\] |
| Employees or their representatives | \[Whether and how they are consulted, or why not\] | \[Date\] | \[Outcome\] |

## 5 Step 4: Necessity and proportionality

**Table 2: Lawful basis and conditions**

| Kind of data | Article 6 basis | Article 9 condition | DPA 2018, Schedule 1 condition | Appropriate policy document needed? |
| --- | --- | --- | --- | --- |
| \[Information type from the profile, for example HR records (contract, pay, absence, performance)\] | \[For example, contract or legal obligation\] | Not applicable | Not applicable | No |
| \[Special category data, if any, for example health data in HR records\] | \[Basis\] | \[For example, Article 9(2)(b), employment\] | \[For example, paragraph 1\] | \[Yes or no\] |
| Names and contact details in items | \[For example, legitimate interests\] | Not applicable | Not applicable | No |
| Names from sign-in through PingFederate, and groups read from Active Directory | \[For example, legitimate interests\] | Not applicable | Not applicable | No |
| Audit records and logs | \[For example, legal obligation or legitimate interests\] | Not applicable | Not applicable | No |
| \[Criminal offence data, if any, for example a conduct record about an offence\] | \[Basis\] | Not applicable (Article 10) | \[For example, paragraph 1 or Part 3\] | \[Yes or no\] |
| Fault reports and notifications: the reporter's name and description, and each person's own notifications | \[For example, legitimate interests\] | Not applicable | Not applicable | No |
| Records of privacy requests, complaints, incidents and breaches | \[For example, legal obligation\] | \[If a record reveals special category data\] | \[Condition, if needed\] | \[Yes or no\] |
| Other operating records that name people: training, maintenance, media, access reviews, exceptions, sharing decisions, home working checks and sign-off sheets | \[For example, legitimate interests\] | Not applicable | Not applicable | No |
| Personnel security records of people with access: dates of screening confirmation and agreements, and leaver and mover records, with no screening result or criminal record data (\<Policy\> (PS), R4) | \[For example, legitimate interests or contract\] | Not applicable | Not applicable | No |

Consent is not used, because employees cannot freely refuse their employer, as the ICO's employment records guidance advises.

**Minimisation:** \<System Name\> holds whole items, so minimisation depends on what each schema's Data Owner and editors choose to upload (SI-12(1), PRO-PT-5). Test and development use invented data only, which Test-PersonalData.ps1 checks. The personal data allowed in records about people's use of \<System Name\> is set here, as the privacy risk assessment that AU-3(3) and PE-8(3) refer to: audit records hold the username, user ID, IP address and browser, and no further personal data in free text or in the record of a change or deletion (\<Audit and Accountability Management\>, section 3.4); the data centres' visitor records hold the visitor's name and organisation and the date and time of the visit (\<Physical and Environmental Protection Management\>, section 3.10). The values are in \<System Description\>, section 4.

**Accuracy:** each schema's Data Owner checks accuracy every 12 months (PRO-PT-5).

**Retention:** periods are in \<PII Processing Management\>, section 3.7, set by the business owner, and items are disposed of at the end of their period, once the business owner approves the disposal in the UI application, with the disposal recorded (\<System Description\>, FR-074). A deleted item stays in the encrypted backups for up to 12 months, beyond use, and is deleted again if a backup is ever restored (\<Contingency Planning Management\>, sections 3.7 and 3.8).

**Rights:** requests go to the legal adviser (PRO-PT-1) and are answered within one month of confirming the person's identity, extendable as UK GDPR allows, using the search across all schemas (FR-073) as a reasonable and proportionate search, run by the legal adviser's delegate, who is named by the legal adviser and holds no other role, and complaints acknowledged within 30 days, as the Data (Use and Access) Act 2025 requires.

**Transparency:** \<Organisation\>'s privacy notices for employees, contractors and agency staff must name \<System Name\> and its purposes (EV-PT-01), and are linked from \<System Name\>'s pages, as people sign in on \<Organisation\>'s PingFederate page (FR-010). \[Legal adviser: name the notice that covers anyone else the information types hold data about, or record why none is given under UK GDPR, Article 14(5).\]

**Transfers and processors:** none outside \<Organisation\> in normal operation, and no data is held outside the UK. A supplier who sees personal data on an administrator's shared screen, or receives a support copy that still holds it, does so only with the legal adviser's agreement and under a contract with UK GDPR Article 28 terms (\<Maintenance Management\>, sections 3.6 and 3.7; \<Procedures\>, PRO-MA-7).

**Automated decisions:** \<System Name\> makes no decision about a person by automated means alone, and does no profiling (UK GDPR, Article 22).

## 6 Step 5: Risks to individuals

Likelihood and severity are proposed by the assessor from the design and the assessment evidence, using the scales in \<Risk List\>, section 4.1. The legal adviser decides the final risks and scores, and may add, change or remove any row.

**Table 3: Risks to individuals**

| ID | Risk to people | Source of the risk | Likelihood (proposed) | Severity (proposed) | Overall (proposed) |
| --- | --- | --- | --- | --- | --- |
| DP-1 | Someone reads items about a person that they have no need to see, including special category data | A member of a schema's groups browsing beyond their task; a database administrator querying the item tables (\<Risk List\>, R-AC-01) | Low | High | Medium |
| DP-2 | Special category or criminal offence data is seen by more people than need it | An item filed in a schema not authorised for that data, or not marked | Medium | High | High |
| DP-3 | Data is kept longer than needed | Retention periods not yet set; deleted items staying in backups for up to 12 months; users' exports kept on devices | Medium | Medium | Medium |
| DP-4 | An inaccurate record is relied on in a decision about a person | Items not corrected; the yearly check missed | Low | Medium | Low |
| DP-5 | A person's request is answered incompletely | The search across schemas finds an item only by what it can read, so a person named only inside a scanned image may be missed | Medium | Medium | Medium |
| DP-6 | Exported copies leave \<Organisation\>'s control and are lost or sent to the wrong person | A user's mistake with an export or download | Low | High | Medium |
| DP-7 | People do not know that \<System Name\> holds their data, or how to use their rights | A privacy notice that does not name \<System Name\>, or no notice for people named in documents who are not staff | Medium | Low | Low |
| DP-8 | A breach is not spotted, or reported late | Misuse that looks like normal work | Low | High | Medium |

## 7 Step 6: Measures to reduce the risks

**Table 4: Measures**

| Risk | Measure | Effect (proposed) | Residual risk (proposed) | Approved? |
| --- | --- | --- | --- | --- |
| DP-1 | Schema groups authorised by each Data Owner and reviewed every 12 months; rules A23 to A25; every view audited and the log reviewed weekly; SQL Server Audit on the item tables; administrators see no item content | Reduced | Low | \[Yes or no\] |
| DP-2 | Only schemas the business owner authorises may hold it; items marked (FR-035); the Data Owner's yearly check (PRO-PT-5); privacy training B6 and M9 | Reduced | Medium | \[Yes or no\] |
| DP-3 | Retention schedule and disposal built in (FR-074); backups beyond use and deletions re-applied after a restore; exports deleted within 30 days (A28) and working copies within 24 hours | Reduced | Low | \[Yes or no\] |
| DP-4 | The yearly accuracy check; people's right to correction (PRO-PT-1) | Reduced | Low | \[Yes or no\] |
| DP-5 | A reasonable and proportionate search with the search across schemas (FR-073), which the Data (Use and Access) Act 2025 allows. \[Legal adviser: decide whether the delegate also asks each schema's Data Owner where the person's data is likely to be\] | Reduced | Low | \[Yes or no\] |
| DP-6 | Export only by editors, audited, with an alert above a set size (FR-052); approved locations only (A31); marked copies; breach playbook | Reduced | Low | \[Yes or no\] |
| DP-7 | The notices checked every 12 months to name \<System Name\> (PRO-PT-3); the link and statement on every page (FR-010) | Reduced | Low | \[Yes or no\] |
| DP-8 | Weekly audit review and alerts; reporting within 1 hour; breach training B6, M7 and M9; the breach steps in \<Incident Response Management\>, section 3.8 | Reduced | Low | \[Yes or no\] |

## 8 Step 7: Sign-off and outcomes

**Table 5: Sign-off**

| Item | Name and date | Notes |
| --- | --- | --- |
| Measures approved by | \[Legal adviser and system owner\] | Integrate the measures into \<Plan of Action and Milestones\> with dates |
| Residual risks approved by | \[Authorising official\] | If a high risk remains, consult the ICO before processing |
| Data protection officer's advice provided | \[Name and date\] | \[Summary of advice\] |
| Advice accepted or overruled | \[Name and date\] | If overruled, give the reasons |
| Consultation responses reviewed by | \[Name and date\] | \[Summary\] |
| This DPIA kept under review by | Legal adviser | Before production, after a significant change, and every 12 months |

## 9 References

**Table 6: References**

| Reference | Use |
| --- | --- |
| UK GDPR, Articles 5, 6, 9, 10, 13 to 22, 28, 30, 33 to 36; Data Protection Act 2018, section 10 and Schedule 1 | The law this assessment applies |
| Data (Use and Access) Act 2025 | Complaints to the controller, and reasonable and proportionate searches |
| ICO sample DPIA template; ICO guidance on keeping employment records | The structure and the employment context |
| CSS, RA-8, PT-2, PT-3, PT-7, AU-3(3) and PE-8(3) | The controls this assessment supports |
| \<PII Processing Management\>, \<Privacy Plan\>, \<Policy\> (PT), \<Procedures\> (PT), \<Risk List\> and \<Plan of Action and Milestones\> | Inventory, privacy plan, policy, procedures, risks and fixes |
| Test-PersonalData.ps1, in the PT evidence | The check that test and development hold invented data only |
