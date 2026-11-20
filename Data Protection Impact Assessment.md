# \<System Name\> Data Protection Impact Assessment

## 1 Purpose and how to complete this draft

This is the data protection impact assessment for \<System Name\> required before production (\<Policy\> (PT); PA-72; CSS RA-8). It follows the steps of the ICO's sample DPIA template.

The facts about \<System Name\> are filled in from the documents and tests. Everything that is a legal judgement is shown in square brackets for the legal adviser: the lawful basis, the special category and Schedule 1 conditions, whether an appropriate policy document is needed, the final risk scores, and the decision. Nothing in square brackets has been decided.

## 2 Step 1: Why a DPIA is needed

\<System Name\> stores, finds and shows \<Organisation\>'s project documents, including a Human Resources project. HR documents hold employees' personal data and may hold special category data, such as health information. The people concerned are employees, who are in an unequal relationship with their employer. Processing special category data about employees is a factor the ICO lists as likely to need a DPIA. \[Legal adviser: confirm whether a DPIA is mandatory under UK GDPR, Article 35, or carried out as good practice.\]

## 3 Step 2: The processing

**Nature:** documents are uploaded in bulk or one at a time, indexed by metadata, searched within a project, viewed on screen, printed on managed printers, and exported in bulk by editors. The full inventory, with each kind of data, is in \<PII Processing Management\>, section 3.3.

**Scope:** \[number of employees and former employees whose HR documents are held\]; \[number of documents\]; three projects at present, including Human Resources. Data is kept until disposed of under the retention schedule in \<PII Processing Management\>, section 3.7, which \<System Name\> cannot yet apply (PA-70).

**Context:** users are \<Organisation\> staff on managed devices in the UK. \<System Name\> runs on two VMs in \<Organisation\>'s data centre. No data leaves the UK, and no processor outside \<Organisation\> is used. Planned links to ServiceNow and the Starters/Leavers system carry names and account details only.

**Purposes:** HR administration, and managing project documents (\<Policy\> (PT)).

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
| HR records (contract, pay, absence, performance) | \[For example, contract or legal obligation\] | Not applicable | Not applicable | No |
| Health and other special category data in HR records | \[Basis\] | \[For example, Article 9(2)(b), employment\] | \[For example, paragraph 1\] | \[Yes or no\] |
| Names and contact details in project documents | \[For example, legitimate interests\] | Not applicable | Not applicable | No |
| Names and groups held from sign-in through AD FS | \[For example, legitimate interests\] | Not applicable | Not applicable | No |
| Audit records and logs | \[For example, legal obligation or legitimate interests\] | Not applicable | Not applicable | No |

Consent is not used, because employees cannot freely refuse their employer (D-PT-10), as the ICO's employment records guidance advises.

**Minimisation:** \<System Name\> holds whole documents, so minimisation depends on what projects choose to upload (SI-12(1), PRO-PT-5). Test stacks use sample data only (Test-PersonalData.ps1, Q09).

**Accuracy:** project access approvers check accuracy every 12 months (PRO-PT-5). Corrections in the admin portal are not yet audited (PA-89).

**Retention:** periods are in \<PII Processing Management\>, section 3.7, for the business owner to set (D-PT-21). \<System Name\> has no retention field and no disposal job yet (PA-70).

**Rights:** requests go to the legal adviser (PRO-PT-1), with a reasonable and proportionate search and complaints acknowledged within 30 days, as the Data (Use and Access) Act 2025 requires. \<System Name\> cannot yet search all projects for one person in one step (PA-89).

**Transparency:** \<Organisation\>'s employee privacy notice must name \<System Name\> (EV-PT-01). \<System Name\>'s pages don't link to it yet (PA-90). People sign in on \<Organisation\>'s AD FS page.

**Transfers and processors:** none outside \<Organisation\>.

**Automated decisions:** \<System Name\> makes no decision about a person by automated means alone, and does no profiling (UK GDPR, Article 22).

## 6 Step 5: Risks to individuals

Likelihood and severity are proposed by the assessor from the test evidence. The legal adviser decides the final scores.

**Table 3: Risks to individuals**

| ID | Risk to people | Source of the risk | Likelihood (proposed) | Severity (proposed) | Overall (proposed) |
| --- | --- | --- | --- | --- | --- |
| DP-1 | Someone without a need reads an employee's HR record | Global administrators can read every project (REC-4); HR documents aren't marked as personal data (PA-89) | Possible | Significant | Medium |
| DP-2 | Copies of HR documents are left where others can find them | Export copies stay unencrypted on the server (PA-86) | Probable | Significant | High |
| DP-3 | Records are kept longer than needed | No retention or disposal (PA-70) | Probable | Minimal | Medium |
| DP-4 | A decision is based on wrong or out-of-date data | Corrections aren't audited; no accuracy check yet (PA-89) | Possible | Significant | Medium |
| DP-5 | A person can't get all their data, or have it deleted | No complete search across projects; deleted pages remain until the database is vacuumed (PA-89) | Possible | Significant | Medium |
| DP-6 | A breach isn't noticed | Monitoring is by hand; alerts are planned (PA-59) | Possible | Severe | High |
| DP-7 | Personal data spreads into logs | The application log repeats usernames and IP addresses (PA-75) | Probable | Minimal | Medium |
| DP-8 | Stolen disks expose HR documents | No encryption at rest (PA-52) | Remote | Severe | Medium |
| DP-9 | People don't know \<System Name\> holds their data | Notice not seen; no link at sign-in (EV-PT-01, PA-90) | Possible | Minimal | Low |

## 7 Step 6: Measures to reduce the risks

**Table 4: Measures**

| Risk | Measure | Effect (proposed) | Residual risk (proposed) | Approved? |
| --- | --- | --- | --- | --- |
| DP-1 | Limit administrators' access to documents (REC-4); mark HR documents; review project access every 3 months | Reduced | Low | \[Yes or no\] |
| DP-2 | Remove server copies and encrypt exports (PA-86); a check of the export folder each working day (SyOps C49) | Reduced | Low | \[Yes or no\] |
| DP-3 | Set periods (D-PT-21) and build disposal (PA-70) | Reduced | Low | \[Yes or no\] |
| DP-4 | Audit corrections (PA-89); yearly accuracy check (PRO-PT-5) | Reduced | Low | \[Yes or no\] |
| DP-5 | Audited search across projects for requests, and vacuum after deletion (PA-89) | Reduced | Low | \[Yes or no\] |
| DP-6 | Alerts (PA-59); breach procedure in \<Incident Response Management\>, section 3.8 | Reduced | Medium | \[Yes or no\] |
| DP-7 | Remove the audit lines from the application log (PA-75) | Eliminated | Low | \[Yes or no\] |
| DP-8 | Full-disk encryption on both VMs (PA-52) | Reduced | Low | \[Yes or no\] |
| DP-9 | Notice names \<System Name\> (EV-PT-01); link at sign-in (PA-90) | Reduced | Low | \[Yes or no\] |

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
| UK GDPR, Articles 5, 6, 9, 30, 35 and 36; Data Protection Act 2018, Schedule 1 | The law this assessment applies |
| Data (Use and Access) Act 2025 | Complaints to the controller, and reasonable and proportionate searches |
| ICO sample DPIA template; ICO guidance on keeping employment records (February 2025) | The structure and the employment context |
| CSS, RA-8, PT-2, PT-3 and PT-7 | The controls this assessment supports |
| \<PII Processing Management\>, \<Privacy Plan\>, \<Policy\> (PT), \<Procedures\> (PT), \<Risk List\> and \<Plan of Action and Milestones\> | Inventory, privacy plan, policy, procedures, risks and fixes |
| the PT evidence | Test-PersonalData.ps1 results |
