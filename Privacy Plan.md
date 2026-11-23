# \<System Name\> Privacy Plan

## 1 Purpose

This plan is the privacy counterpart to \<System Security Plan\>. It relies on that plan, and the documents it names, for the system's boundary, environment and architecture. The legal adviser completes its legal content.

## 2 Context and boundary

The boundary, operational context and environment are as \<System Security Plan\> and \<Concept of Operations\> describe. \<Organisation\> operates in the UK, and is the controller for the personal data \<System Name\> holds. These laws apply: UK GDPR, the Data Protection Act 2018, the Data (Use and Access) Act 2025 and the Computer Misuse Act 1990.

## 3 Roles

**Table 1: Privacy roles**

| Role | Holder | Part |
| --- | --- | --- |
| Plan owner and privacy representative: the legal adviser | \[Name\] | Owns this plan, the impact assessment, individuals' requests and complaints, and reports to the ICO |
| Data protection officer | \[Name, or the reason none is required\] | Leads \<Organisation\>'s privacy programme (PM-19; UK GDPR, Articles 37 to 39), advises on this plan and the impact assessment, and is the contact for individuals and the ICO. The legal adviser completes this row |
| Risk decisions | \[Name\] | Decides on privacy risk |
| Business and information owner | \[Name\] | Decides what data schemas hold, and how long for, and approves the disposal of items due under the retention schedule in the UI application (\<System Description\>, FR-074) |
| Legal adviser's delegate | \[Name, named by the legal adviser\] | Searches every schema for one person's items to answer a request under data protection law (\<System Description\>, FR-073). Holds no other role |
| Data Owners | \[Names, one for each schema\] | Authorise who may read or edit each schema, in ServiceNow, and keep its personal data accurate |
| System owner | \[Name\] | Makes sure \<System Name\> follows this plan |
| Breach response | \[Name\], security officer; \[Name\], legal adviser | The security officer leads the response and keeps the breach register; the legal adviser judges the harm and decides on telling the ICO within 72 hours and the people affected (\<Incident Response Management\>, sections 3.3 and 3.8) |

## 4 Information and categorisation

The information types and impact levels are in \<System Security Plan\>, Table 4. The personal data is listed in \<PII Processing Management\>, section 3.3. Every application holds sign-in identities and audit records, and the profile adds its own information types (\<System Description\>, section 3.4). The reference categorisation is confidentiality Moderate, integrity Moderate and availability Low.

## 5 Threats and privacy risk

The main threats to individuals are someone reading items holding personal data they should not, data kept too long, inaccurate data being relied on, and a breach not being spotted. The privacy risk assessment is \<Data Protection Impact Assessment\>, which the legal adviser completes. Privacy risks are rated by the same method and recorded in \<Risk List\>, whose threat model carries the main one, misuse of access to a schema, as R-RA-04 (section 2.1).

## 6 Requirements, baseline and controls

The requirements are the data protection laws: UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025. The baseline is the CSS privacy baseline, as tailored by \<Tailoring Register\>. Of its 96 controls, 43 are within Moderate and assessed with their families, 5 PT controls and 15 others are assessed in \<Control Assessment Record\> (PT), 9 are tailored out (7 as US-only, PT-4 as consent is not used, and SI-19 as nothing is de-identified), and 24 are PM controls held at organisation level: inherited from \<Organisation\>'s privacy programme and not assessed for \<System Name\>, with PM-17 and PM-24 of them not applicable (TR-PM-01; \<Program Management\>, section 3.4). This plan follows \<Organisation\>'s privacy programme plan (PM-18), requested in EV-PM-04, and is changed to match it where the two differ.

## 7 Activities to coordinate

**Table 2: Privacy activities**

| Activity | Who | When |
| --- | --- | --- |
| Confirm the lawful basis | Legal adviser | Before production |
| Complete the impact assessment | Legal adviser, system owner, business owner | Before production, and after significant change |
| Set retention periods | Business owner | Before production |
| Build retention and disposal | Developers | Before production |
| Check the privacy notices cover every group of people in the inventory and name \<System Name\> | System owner, legal adviser, \<Organisation\> | Before production, then every 12 months |

## 8 Architecture

Privacy relies on the security architecture in \<System Description\>, section 6, and fits \<Organisation\>'s enterprise architecture in the same way (\<System Description\>, section 10; EV-PL-01).

- **Where personal data is.** In items, fault reports, notifications and audit records in the Microsoft SQL Server database on the database server; in the encrypted export working copies until they are deleted; in the authentication cookie while a person is signed in; and in the records the role holders keep, such as requests, complaints and personnel security records. Each schema's read and edit groups limit who can read its items. Data at rest is encrypted. Every kind is listed in \<PII Processing Management\>, section 3.3.
- **Where it goes.** \<System Name\> receives a signed response naming the person from PingFederate at sign-in (flows F6 and F10), and reads their group memberships from Active Directory (F7). Sign-in identities and the applications' security events go to \<Organisation\>'s central logging, and encrypted backups of the database, which hold items and audit records, go to \<Organisation\>'s backup site and second site (F8). Users may download and export items to the approved locations in \<Security Operating Procedures\>, A31. \<System Name\> shares no data with any other system. ServiceNow and the starters and leavers process have no connection to it: people act on what they produce (flow F9).
- **How privacy risk is kept low.** Only the personal data each purpose needs is held (\<PII Processing Management\>; SA-8(33), SI-12(1)); it is disposed of under the retention schedule (\<PII Processing Management\>, section 3.7); test and development use invented data only (SI-12(2)); and the audit log holds no extra personal data in free text (AU-3(3)).
- **Assumptions.** \<Organisation\>'s privacy notices and contracts cover the data of employees, contractors and agency staff, and the legal adviser names a notice, or records why none is given, for anyone else the items describe; a supplier gets personal data only for support, under a contract with UK GDPR Article 28 terms and holding it in the UK (\<Maintenance Management\>, section 3.7); its central logging and backup services keep the data in the United Kingdom only and for no longer than \<System Name\>'s retention periods (EV-AU-01 to EV-AU-03, EV-CP-01).

This architecture is reviewed with the security architecture (\<Procedures\>, PRO-PL-5).
