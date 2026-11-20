# \<System Name\> Data Protection Impact Assessment

## 1 Purpose and how to complete this assessment

This is the data protection impact assessment for \<System Name\> required before production (\<Policy\> (PT); CSS RA-8). It follows the steps of the ICO's sample DPIA template.

The facts about \<System Name\> are filled in from the design documents. Everything that is a legal judgement is shown in square brackets for the legal adviser: the lawful basis, the special category and Schedule 1 conditions, whether an appropriate policy document is needed, the final risk scores, and the decision.

## 2 Step 1: Why a DPIA is needed

\<System Name\> stores, finds and shows \<Organisation\>'s digital items, kept apart in schemas. It holds the sign-in identities in its audit records, and whatever personal data its information types hold (\<System Description\>, section 3.4): \[for example, employees' personal data in a Human Resources schema, which may include special category data such as health information\]. Where the people concerned are employees, they are in an unequal relationship with their employer, and processing special category data about employees is a factor the ICO lists as likely to need a DPIA. \[Legal adviser: confirm whether a DPIA is mandatory under UK GDPR, Article 35, or carried out as good practice.\]

## 3 Step 2: The processing

**Nature:** items are created or uploaded in bulk or one at a time, described by their catalogue details, searched within one schema at a time, viewed on screen, downloaded, printed on managed printers, and exported in bulk by editors. The full inventory, with each kind of data, is in \<PII Processing Management\>, section 3.3.

**Scope:** \[number of people whose personal data is held\]; \[number of items\]; \[number of schemas\] (\<System Description\>, P-33). Data is kept until disposed of under the retention schedule in \<PII Processing Management\>, section 3.7.

**Context:** users are \<Organisation\> staff and contractors on managed devices in the UK. \<System Name\> runs on two Windows Server 2025 virtual servers in \<Organisation\>'s data centre, with its items in Microsoft SQL Server 2022. No data leaves the UK (\<System Description\>, P-23), and no processor outside \<Organisation\> is used. People sign in through \<Organisation\>'s PingFederate, and the API reads their group memberships from Active Directory. ServiceNow and the starters and leavers process have no connection to \<System Name\>: people act on the access approvals and leaver notices they produce.

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

Consent is not used, because employees cannot freely refuse their employer, as the ICO's employment records guidance advises.

**Minimisation:** \<System Name\> holds whole items, so minimisation depends on what each schema's Data Owner and editors choose to upload (SI-12(1), PRO-PT-5). Test and development use invented data only, which Test-PersonalData.ps1 checks.

**Accuracy:** each schema's Data Owner checks accuracy every 12 months (PRO-PT-5).

**Retention:** periods are in \<PII Processing Management\>, section 3.7, set by the business owner, and items are disposed of at the end of their period, with the disposal recorded (\<System Description\>, FR-074).

**Rights:** requests go to the legal adviser (PRO-PT-1) and are answered within the time in \<System Description\>, P-22, using the search across all schemas (FR-073) as a reasonable and proportionate search, and complaints acknowledged within 30 days, as the Data (Use and Access) Act 2025 requires.

**Transparency:** \<Organisation\>'s employee privacy notice must name \<System Name\> (EV-PT-01). People sign in on \<Organisation\>'s PingFederate page.

**Transfers and processors:** none outside \<Organisation\>, and no data is held outside the UK.

**Automated decisions:** \<System Name\> makes no decision about a person by automated means alone, and does no profiling (UK GDPR, Article 22).

## 6 Step 5: Risks to individuals

Likelihood and severity are proposed by the assessor from the design and the assessment evidence. The legal adviser decides the final scores.

**Table 3: Risks to individuals**

| ID | Risk to people | Source of the risk | Likelihood (proposed) | Severity (proposed) | Overall (proposed) |
| --- | --- | --- | --- | --- | --- |
| \[DP-n\] | \[Risk to people\] | \[Source of the risk\] | \[Likelihood\] | \[Severity\] | \[Overall\] |

## 7 Step 6: Measures to reduce the risks

**Table 4: Measures**

| Risk | Measure | Effect (proposed) | Residual risk (proposed) | Approved? |
| --- | --- | --- | --- | --- |
| \[DP-n\] | \[Measure\] | \[Effect\] | \[Residual risk\] | \[Yes or no\] |

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
| ICO sample DPIA template; ICO guidance on keeping employment records | The structure and the employment context |
| CSS, RA-8, PT-2, PT-3 and PT-7 | The controls this assessment supports |
| \<PII Processing Management\>, \<Privacy Plan\>, \<Policy\> (PT), \<Procedures\> (PT), \<Risk List\> and \<Plan of Action and Milestones\> | Inventory, privacy plan, policy, procedures, risks and fixes |
| Test-PersonalData.ps1, in the PT evidence | The check that test and development hold invented data only |
