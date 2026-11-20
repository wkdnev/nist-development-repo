# \<System Name\> Privacy Plan

## 1 Purpose

This plan is the privacy counterpart to \<System Security Plan\>. It relies on that plan, and the documents it names, for the system's boundary, environment and architecture. The legal adviser completes its legal content.

## 2 Context and boundary

The boundary, operational context and environment are as \<System Security Plan\> and \<Concept of Operations\> describe. \<Organisation\> operates in the UK, and is the controller for the personal data \<System Name\> holds. The laws in \<System Description\>, P-31 apply: UK GDPR, the Data Protection Act 2018, the Data (Use and Access) Act 2025 and the Computer Misuse Act 1990.

## 3 Roles

**Table 1: Privacy roles**

| Role | Holder | Part |
| --- | --- | --- |
| Plan owner and privacy representative | \[Name\] | Owns this plan, the impact assessment, individuals' requests and complaints, and reports to the ICO |
| Data protection officer | \[Name, or the reason none is required\] | Leads \<Organisation\>'s privacy programme (PM-19; UK GDPR, Articles 37 to 39), advises on this plan and the impact assessment, and is the contact for individuals and the ICO. The legal adviser completes this row |
| Risk decisions | \[Name\] | Decides on privacy risk |
| Business and information owner | \[Name\] | Decides what data schemas hold, and how long for, and approves the disposal of items due under the retention schedule in the Admin application (\<System Description\>, FR-074) |
| Legal adviser's delegate | \[Name, named by the legal adviser\] | Searches every schema for one person's items to answer a request under data protection law (\<System Description\>, FR-073). Holds no other role |
| Data Owners | \[Names, one for each schema\] | Authorise who may read or edit each schema, in ServiceNow, and keep its personal data accurate |
| System owner | \[Name\] | Makes sure \<System Name\> follows this plan |
| Breach response | \[Name\] | Leads the response, following \<Incident Response Management\> |

## 4 Information and categorisation

The information types and impact levels are in \<System Security Plan\>, Table 4. The personal data is listed in \<PII Processing Management\>, section 3.3. Every application holds sign-in identities and audit records, and the profile adds its own information types (\<System Description\>, section 3.4). The reference categorisation is confidentiality Moderate, integrity Moderate and availability Low (P-01).

## 5 Threats and privacy risk

The main threats to individuals are someone reading items holding personal data they should not, data kept too long, inaccurate data being relied on, and a breach not being spotted. The privacy risk assessment is \<Data Protection Impact Assessment\>, which the legal adviser completes. Privacy risks are recorded in \<Risk List\>.

## 6 Requirements, baseline and controls

The requirements are the data protection laws in \<System Description\>, P-31. The baseline is the CSS privacy baseline, as tailored by \<Tailoring Register\>. Of its 96 controls, 43 are within Moderate and assessed with their families, 6 PT controls and 16 others are assessed in \<Control Assessment Record\> (PT), 7 are tailored as US-only, and 24 are PM controls held at organisation level.

## 7 Activities to coordinate

**Table 2: Privacy activities**

| Activity | Who | When |
| --- | --- | --- |
| Confirm the lawful basis | Legal adviser | Before production |
| Complete the impact assessment | Legal adviser, system owner, business owner | Before production, and after significant change |
| Set retention periods | Business owner | Before production |
| Build retention and disposal | Developers | Before production |
| Check the privacy notice names \<System Name\> | System owner, \<Organisation\> | Before production, then every 12 months |

## 8 Architecture

Privacy relies on the Security Architecture, \<Security Architecture\>. Personal data is in items and audit records in the Microsoft SQL Server database on the database server. Each schema's read and edit groups limit who can read it. Data at rest is encrypted. \<System Name\> receives a person's name from PingFederate at sign-in (flow F10) and reads their group memberships from Active Directory, and shares no data with any other system. ServiceNow and the starters and leavers process have no connection to it: people act on what they produce (flow F9). The plan assumes \<Organisation\>'s notice and contracts cover employees' data.
