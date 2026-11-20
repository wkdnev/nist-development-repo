# \<System Name\> Privacy Plan

## 1 Purpose

This plan is the privacy counterpart to \<System Security Plan\>. It relies on that plan, and the documents it names, for the system's boundary, environment and architecture. Everything legal here is a proposal until \[Name\] confirms it.

## 2 Context and boundary

The boundary, operational context and environment are as \<System Security Plan\> and \<Concept of Operations\> describe. \<Organisation\> operates in the UK, and is the controller for its HR data. UK GDPR and the Data Protection Act 2018 apply.

## 3 Roles

**Table 1: Privacy roles**

| Role | Holder | Part |
| --- | --- | --- |
| Plan owner and privacy representative | \[Name\] | Owns this plan, the impact assessment, individuals' requests and complaints, and reports to the ICO |
| Data protection officer | \[Name, or the reason none is required\] | Leads \<Organisation\>'s privacy programme (PM-19; UK GDPR, Articles 37 to 39), advises on this plan and the impact assessment, and is the contact for individuals and the ICO. The legal adviser completes this row (D-PM-04) |
| Risk decisions | \[Name\] | Decides on privacy risk |
| Business and information owner | \[Name\] | Decides what data projects hold, and how long for |
| System owner | \[Name\] | Makes sure \<System Name\> follows this plan |
| Breach response | \[Name\] | Leads the response, following \<Incident Response Management\> |

## 4 Information and categorisation

The information types and impact levels are in \<System Security Plan\>, Table 4. The personal data is listed in \<PII Processing Management\>, section 3.3. HR documents are the main concern: confidentiality Moderate, integrity Moderate and availability Low.

## 5 Threats and privacy risk

The main threats to individuals are someone reading HR documents they shouldn't, data kept too long, inaccurate data being relied on, and a breach not being spotted. The data protection impact assessment is drafted as \<Data Protection Impact Assessment\> \<ver\> for the legal adviser to complete (PA-72, D-PT-20), so this is not yet a privacy risk result. Risks and decisions are in \<Risk List\>, R-PT-01.

## 6 Requirements, baseline and controls

The requirements are UK GDPR and the Data Protection Act 2018. The baseline is the CSS privacy baseline, as tailored by \<Tailoring Register\>. Of its 96 controls, 43 are within Moderate and assessed with their families, 6 PT controls and 16 others are assessed in \<Control Assessment Record\> (PT), 7 are tailored as US-only, and 24 are PM controls held at organisation level.

## 7 Activities to coordinate

**Table 2: Privacy activities**

| Activity | Who | When |
| --- | --- | --- |
| Confirm the lawful basis | Legal adviser | Before production |
| Complete the impact assessment | Legal adviser, system owner, business owner | Before production, and after significant change |
| Set retention periods | Business owner | Before production |
| Build retention and disposal | Developers | Before production, if the authorising official agrees (PA-70) |
| Check the privacy notice names \<System Name\> | System owner, \<Organisation\> | Before production, then every 12 months |

## 8 Architecture

Privacy relies on the Security Architecture, \<Security Architecture\>. Personal data is in the database and audit records on the database VM. Project permissions limit who can read it. Encryption at rest is planned (PA-52). \<System Name\> does not share data with other systems, apart from the planned ServiceNow and Starters/Leavers connections, which carry names and account details only. The plan assumes \<Organisation\>'s notice and contracts cover employees' data.
