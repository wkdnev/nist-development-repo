# \<System Name\> Documentation Map

## 1 Scope and assumptions

This set covers the 19 control families of CSS that apply to \<System Name\>: Access Control (AC), Awareness and Training (AT), Audit and Accountability (AU), Assessment, Authorization, and Monitoring (CA), Configuration Management (CM), Contingency Planning (CP), Identification and Authentication (IA), Incident Response (IR), Maintenance (MA), Media Protection (MP), Physical and Environmental Protection (PE), Planning (PL), Personnel Security (PS), Personally Identifiable Information Processing and Transparency (PT), Risk Assessment (RA), System and Services Acquisition (SA), System and Communications Protection (SC), System and Information Integrity (SI) and Supply Chain Risk Management (SR). The Moderate baseline applies, with the CSS privacy baseline for personal data, which makes 316 controls. Program Management (PM) is the twentieth family. Its 37 controls are \<Organisation\>'s programme, not one system's, so they are not among the 316, including the 24 that CSS places in the privacy baseline. \<System Name\> inherits them from \<Organisation\> (\<Tailoring Register\>, section 4). Wherever this set lists the families, it uses CSS order.

- **System:** \<System Name\>, an internal digital library built on the reference system in \<System Description\>: the UI application, the Admin application, the API and the shared library, with a Microsoft SQL Server 2022 database in which each schema is its own database schema.
- **Design described:** \<System Name\> on two Windows Server 2025 VMs at \<Organisation\>, each application a Windows service under its own group managed service account. Development is on developers' computers and testing on a throwaway copy of the whole system built from a tagged release, both with invented data and apart from production.
- **Baseline:** Moderate.
- **Evidence basis:** the record documents are templates. The team that assesses \<System Name\> fills them in from its own tests, interviews and evidence. Nothing in the set is a claim of compliance.
- **Master copy:** the documents are kept as Markdown. Section 4.1 says how they are controlled.

## 2 The document set

The set has 42 documents. \<Guide to the Document Set\> is the place to start. Within the set, each fact is written in one document and the others point to it. Every family has its design in a document of its own, in the same form: access control in \<Access Control Management\>, awareness and training in \<Awareness and Training Management\>, audit and accountability in \<Audit and Accountability Management\>, assessment, authorisation and monitoring in \<Assessment, Authorization, and Monitoring Management\>, configuration management in \<Configuration Management\>, contingency planning in \<Contingency Planning Management\>, identification and authentication in \<Identification and Authentication Management\>, incident response in \<Incident Response Management\>, maintenance in \<Maintenance Management\>, media protection in \<Media Protection Management\>, physical and environmental protection in \<Physical and Environmental Protection Management\>, planning in \<Planning Management\>, program management in \<Program Management\>, personnel security in \<Personnel Security Management\>, personal data in \<PII Processing Management\>, risk assessment in \<Risk Assessment Management\>, system and services acquisition in \<System and Services Acquisition Management\>, system and communications protection in \<System and Communications Protection Management\>, system and information integrity in \<System and Information Integrity Management\>, and supply chain risk management in \<Supply Chain Risk Management\>.

### 2.1 The documents

**Table 1: The documents**

| Document | Group | Purpose | Who reads it |
| --- | --- | --- | --- |
| \<System Security Plan\> | Plans and descriptions | How \<System Name\> implements each of the 316 controls, with the system description, architecture figures, inheritance and responsibilities | Everyone, first |
| \<Privacy Plan\> | Plans and descriptions | How personal data in \<System Name\> is governed: the privacy plan that PL-2 calls for | The legal adviser; an auditor |
| \<System Description\> | Plans and descriptions | One description of the whole system for a person or an AI without the source code: its purpose, users, high-level requirements, architecture, technologies and design, its security family by family, and how an application departs from the reference design | Anyone who needs to understand the system; an auditor, early |
| \<Concept of Operations\> | Plans and descriptions | Why \<System Name\> exists, who uses it, the business workflows it supports and its operational scenarios | The business owner; an auditor, early |
| \<Roles and Responsibilities\> | Plans and descriptions | Who holds each role, so that other documents name roles and not people | Anyone asking who holds a role |
| \<Configuration Management\> | Plans and descriptions | The configuration management design, and the plan CM-9 requires: the configuration items, the baseline, the components, the secure settings, change control, least functionality and the inventory | Whoever works in, or assesses, that family |
| \<Contingency Planning Management\> | Plans and descriptions | The contingency design, and the contingency plan CP-2 requires: the business impact analysis, the roles, activation, recovery and reconstitution, backups, the second site, and testing and training | Whoever works in, or assesses, that family |
| \<System and Communications Protection Management\> | Plans and descriptions | The communications protection design: the boundary and allowed flows with the host firewall allow-lists, the TLS profile and sign-in, the cryptographic and key register and certificates, the page policy, information at rest, denial of service and name resolution, and the values chosen for the controls | Whoever works in, or assesses, that family |
| \<System and Information Integrity Management\> | Plans and descriptions | The integrity design: the upload checks and malware scanning, flaw remediation and advisories, monitoring and the detection use cases, the integrity baseline, error handling, retention | Whoever works in, or assesses, that family |
| \<System and Services Acquisition Management\> | Plans and descriptions | The acquisition design: the development framework, the lifecycle and resources, contracts and design information, documentation, engineering principles, external services, developer configuration management, the developer test plan, the tools, the criticality analysis and unsupported components | Whoever works in, or assesses, that family |
| \<Risk Assessment Management\> | Plans and descriptions | The risk assessment design: the security categorisation, the risk assessment and its method, the supply chain review, what is monitored for vulnerabilities, the vulnerability timetable, how findings are analysed, shared and answered, the critical components | Whoever works in, or assesses, that family |
| \<PII Processing Management\> | Plans and descriptions | The personal data design: the authority, purposes and lawful basis, the personal data inventory, special category data, the privacy notice, people's rights, minimisation and the retention schedule | Whoever works in, or assesses, that family |
| \<Personnel Security Management\> | Plans and descriptions | The personnel security design: the risk designation of every role, the screening standard, the access agreements, joiners, movers and leavers, the time limits, the personnel security register | Whoever works in, or assesses, that family |
| \<Program Management\> | Plans and descriptions | How \<System Name\> relies on \<Organisation\>'s security and privacy programme: who provides each of the 37 Program Management controls, what \<System Name\> adds, and the evidence asked for | Whoever works in, or assesses, that family |
| \<Planning Management\> | Plans and descriptions | The planning design: the register of plans in force, what the plans hold, how they are approved, shared, reviewed and protected, the rules of behaviour and the register of signatures | Whoever works in, or assesses, that family |
| \<Physical and Environmental Protection Management\> | Plans and descriptions | The physical and environmental protection design: the sites, the inheritance matrix, how \<Organisation\>'s evidence is checked, the rules for offices and home working | Whoever works in, or assesses, that family |
| \<Media Protection Management\> | Plans and descriptions | The media protection design: the media inventory, the marking scheme, storage and export copies, transport, the sanitising methods and portable storage | Whoever works in, or assesses, that family |
| \<Maintenance Management\> | Plans and descriptions | The maintenance design: who maintains what, how a job is controlled, the remote maintenance routes, the approved tools and people, what may leave, the security-critical components | Whoever works in, or assesses, that family |
| \<Incident Response Management\> | Plans and descriptions | The incident response design, and the plan IR-8 requires: roles, detection, severity and targets, the steps of handling, personal data breaches, playbooks, evidence and the register | Whoever works in, or assesses, that family |
| \<Supply Chain Risk Management\> | Plans and descriptions | The supply chain risk management plan that SR-2 requires: the system context, the team, the risks at each stage, the supplier register, the risk tolerance and how components come in | Whoever works in, or assesses, that family |
| \<Data Protection Impact Assessment\> | Plans and descriptions | The data protection impact assessment, for the legal adviser to complete | The legal adviser |
| \<Assessment, Authorization, and Monitoring Management\> | Plans and descriptions | The assessment, authorisation and monitoring design: assessment, the plan of action, authorisation, the inherited controls, the interface record, the monitoring strategy and significant change | Whoever works in, or assesses, that family |
| \<Identification and Authentication Management\> | Plans and descriptions | The identification and authentication design: who is identified and how, sign-in through PingFederate, the assurance levels, the authenticator inventory and the settings against CSS | Whoever works in, or assesses, that family |
| \<Audit and Accountability Management\> | Plans and descriptions | The audit design: the sources of audit records, the events logged, what a record holds, storage and protection, time, retention, review and alerts | Whoever works in, or assesses, that family |
| \<Awareness and Training Management\> | Plans and descriptions | The training design: who needs what, the briefing, the role curriculum, the training matrix and register | Whoever works in, or assesses, that family |
| \<Access Control Management\> | Plans and descriptions | The access control design: how \<System Name\> is designed and configured to meet the 39 Access Control controls and enhancements | Whoever works in, or assesses, that family |
| \<Policy\> | Rules and how they are carried out | The security and privacy policy: one chapter of rules for each of the 19 families | Everyone bound by the rules |
| \<Procedures\> | Rules and how they are carried out | The procedures that carry out the policy: one chapter for each family, each step naming who acts and the record kept | Whoever carries out a duty |
| \<Security Operating Procedures\> | Rules and how they are carried out | Rules of behaviour for everyone and for privileged users, and how security is operated day to day, with the record that proves each duty | Every user and administrator, who sign it |
| \<Record Templates\> | Rules and how they are carried out | The forms that show controls operating, TPL-1 to TPL-26 | Whoever carries out a procedure |
| \<Tailoring Register\> | Rules and how they are carried out | The case for each control treated as not applicable, and why Program Management is inherited from \<Organisation\> and not assessed | An assessor |
| \<Control Assessment Record\> | Assessment and authorisation | A template for the Level 1 self-assessment, which the Level 2 team re-determines: the 1,998 determination statements to assess, with space for the finding on each, one chapter for each family | An assessor |
| \<Security Assessment Report\> | Assessment and authorisation | A template for the Level 2 report to the authorising official, on which every authorisation rests: the results of all 19 families, the risk position and the conditions before authorisation, to be filled in from the assessment | The authorising official; an auditor, early |
| \<Risk List\> | Assessment and authorisation | The risk register, with the threat model of the reference system and its risks, and the rating method, with space for each further risk with its rating, treatment and acceptance, and for a non-compliance entry for each control that is not satisfied | The authorising official and system owner |
| \<Plan of Action and Milestones\> | Assessment and authorisation | A template for each weakness with its fix, owner, milestone and latest completion, and for the road to authorisation | The system owner, monthly; an auditor |
| \<Decision Register\> | Assessment and authorisation | A template for recording each approval and decision, who made it, when, and the evidence of it | Anyone checking who approved what |
| \<Evidence Requests\> | Assessment and authorisation | The evidence to ask of \<Organisation\>, and who does what for each control | The system owner and \<Organisation\> |
| \<Interview Guide\> | Assessment and authorisation | The interview questions by role and the statements each supports, with space for the answers | An assessor, and the people interviewed |
| \<Guide to the Document Set\> | Guides and index | The place to start: how the documents relate, a route through them for an auditor, one control followed from end to end, and where each family is documented | Anyone new to the set |
| \<Administrator Guide\> | Guides and index | How administrators set up and run \<System Name\> securely, for the developers to confirm against \<System Name\> | Administrators |
| \<User Guide\> | Guides and index | How users work securely in \<System Name\>, for the developers to confirm against \<System Name\> | Users |
| \<Documentation Map\> | Guides and index | This map: every document, where each family is documented, where each fact about a control is held, and the document standard | Anyone looking for a document or a fact |

### 2.2 Where each family is documented

Table 2 gives, for each family, the chapter or section of every document that holds its material. The design column gives the section that holds the family's design. Each of its subsections names the controls it helps to meet.

**Table 2: Where each family is documented**

| Family | Policy and procedures | Design | \<System Security Plan\> | Assessment | \<Evidence Requests\> | \<Interview Guide\> | Test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AC Access Control | \<Policy\> (AC) and \<Procedures\> (AC) | \<Access Control Management\>, section 3 | Section 7.1 | \<Control Assessment Record\> (AC) | Section 3 | Section 3 | Test-AccessControl.ps1 |
| AT Awareness and Training | \<Policy\> (AT) and \<Procedures\> (AT) | \<Awareness and Training Management\>, section 3 | Section 7.2 | \<Control Assessment Record\> (AT) | Section 4 | Section 4 | Test-PlanConsistency.ps1 |
| AU Audit and Accountability | \<Policy\> (AU) and \<Procedures\> (AU) | \<Audit and Accountability Management\>, section 3 | Section 7.3 | \<Control Assessment Record\> (AU) | Section 5 | Section 5 | Test-AuditAndAuth.ps1 |
| CA Assessment, Authorization, and Monitoring | \<Policy\> (CA) and \<Procedures\> (CA) | \<Assessment, Authorization, and Monitoring Management\>, section 3 | Section 7.4 | \<Control Assessment Record\> (CA) | Section 6 | Section 6 | Test-PlanConsistency.ps1 |
| CM Configuration Management | \<Policy\> (CM) and \<Procedures\> (CM) | \<Configuration Management\>, section 3 | Section 7.5 | \<Control Assessment Record\> (CM) | Section 7 | Section 7 | Test-ConfigurationManagement.ps1 |
| CP Contingency Planning | \<Policy\> (CP) and \<Procedures\> (CP) | \<Contingency Planning Management\>, section 3 | Section 7.6 | \<Control Assessment Record\> (CP) | Section 8 | Section 8 | Test-BackupRestore.ps1 |
| IA Identification and Authentication | \<Policy\> (IA) and \<Procedures\> (IA) | \<Identification and Authentication Management\>, section 3 | Section 7.7 | \<Control Assessment Record\> (IA) | Section 9 | Section 9 | Test-AuditAndAuth.ps1 and Test-Identification.ps1 |
| IR Incident Response | \<Policy\> (IR) and \<Procedures\> (IR) | \<Incident Response Management\>, section 3 | Section 7.8 | \<Control Assessment Record\> (IR) | Section 10 | Section 10 | Test-IncidentReadiness.ps1 |
| MA Maintenance | \<Policy\> (MA) and \<Procedures\> (MA) | \<Maintenance Management\>, section 3 | Section 7.9 | \<Control Assessment Record\> (MA) | Section 11 | Section 11 | Test-Maintenance.ps1 |
| MP Media Protection | \<Policy\> (MP) and \<Procedures\> (MP) | \<Media Protection Management\>, section 3 | Section 7.10 | \<Control Assessment Record\> (MP) | Section 12 | Section 12 | Test-MediaProtection.ps1 |
| PE Physical and Environmental Protection | \<Policy\> (PE) and \<Procedures\> (PE) | \<Physical and Environmental Protection Management\>, section 3 | Section 7.11 | \<Control Assessment Record\> (PE) | Section 13 | Section 13 | None: provided by \<Organisation\> |
| PL Planning | \<Policy\> (PL) and \<Procedures\> (PL) | \<Planning Management\>, section 3 | Section 7.12 | \<Control Assessment Record\> (PL) | Section 14 | Section 14 | Test-PlanConsistency.ps1 |
| PM Program Management | None: inherited from \<Organisation\> | \<Program Management\>, section 3.3 | None: section 5 says why PM is not among the 316 controls | Not assessed | Section 15 | Section 15 | None: not assessed |
| PS Personnel Security | \<Policy\> (PS) and \<Procedures\> (PS) | \<Personnel Security Management\>, section 3 | Section 7.13 | \<Control Assessment Record\> (PS) | Section 16 | Section 16 | Test-PlanConsistency.ps1 |
| PT Personally Identifiable Information Processing and Transparency | \<Policy\> (PT) and \<Procedures\> (PT) | \<PII Processing Management\>, section 3; \<Privacy Plan\>; \<Data Protection Impact Assessment\> | Section 7.14 | \<Control Assessment Record\> (PT) | Section 17 | Section 17 | Test-PersonalData.ps1 |
| RA Risk Assessment | \<Policy\> (RA) and \<Procedures\> (RA) | \<Risk Assessment Management\>, section 3 | Section 7.15 | \<Control Assessment Record\> (RA) | Section 18 | Section 18 | Test-Vulnerability.ps1 |
| SA System and Services Acquisition | \<Policy\> (SA) and \<Procedures\> (SA) | \<System and Services Acquisition Management\>, section 3 | Section 7.16 | \<Control Assessment Record\> (SA) | Section 19 | Section 19 | Test-Development.ps1 |
| SC System and Communications Protection | \<Policy\> (SC) and \<Procedures\> (SC) | \<System and Communications Protection Management\>, section 3 | Section 7.17 | \<Control Assessment Record\> (SC) | Section 20 | Section 20 | Test-Protection.ps1 |
| SI System and Information Integrity | \<Policy\> (SI) and \<Procedures\> (SI) | \<System and Information Integrity Management\>, section 3 | Section 7.18 | \<Control Assessment Record\> (SI) | Section 21 | Section 21 | Test-Integrity.ps1 and Test-Vulnerability.ps1 |
| SR Supply Chain Risk Management | \<Policy\> (SR) and \<Procedures\> (SR) | \<Supply Chain Risk Management\>, section 3 | Section 7.19 | \<Control Assessment Record\> (SR) | Section 22 | Section 22 | Test-SupplyChain.ps1 |

\<Risk List\>, \<Decision Register\> and \<Plan of Action and Milestones\> hold each family's entries as rows of one table, with a Family column and the family code in each identifier.

### 2.3 Records outside the documents

**Table 3: Records outside the documents**

| Record | Where | What it shows |
| --- | --- | --- |
| Test evidence | \<evidence\> | The results of each test, with a note that explains them and a list of hashes that fixes their content |
| Figures | With the documents | The architecture figures used in \<System Security Plan\> and \<System Description\> |
| Change record | The private records repository described in section 4.1 | Every change to the documents and evidence, with its date |
| Sign-off sheets | The restricted store, or the private records repository until it is set up (\<Decision Register\>, section 5) | Each approver's signature for the decisions recorded for them |

## 3 Following a control

Each fact about a control is held in one document, and the others point to it. To follow one control from its requirement to its fix, start at its row in \<System Security Plan\>, section 7, which names the risk entry and the fix. Table 4 says where each fact is held.

**Table 4: Where each fact about a control is held**

| Fact | Held in |
| --- | --- |
| What the control is, its type, how far it is implemented, and where its gap is registered | \<System Security Plan\>, section 7 |
| The rule and the procedure | The family's chapter of \<Policy\> and \<Procedures\> |
| The design and the setting | The family's design document (Table 2), and the parameters in \<System Description\>, section 4 |
| Each control's result, and the finding for each determination statement | The family's chapter of \<Control Assessment Record\>, counted up in \<Security Assessment Report\> |
| The threats to the system and the risks they lead to | \<Risk List\>, section 2 |
| What is not met, its cause, risk, rating and treatment | \<Risk List\>, section 5 |
| The fix, its owner and its timing | \<Plan of Action and Milestones\>, section 3 |
| Evidence asked of \<Organisation\> | \<Evidence Requests\> |
| Why a control does not apply | \<Tailoring Register\> |
| Who decided, and when | \<Decision Register\> |

## 4 Document standard

Every \<System Name\> document follows this standard, so that readers can navigate, cite and audit them in the same way.

### 4.1 Master copy and change record

The documents are kept as Markdown, one file for each document, named by its title. That set is the master copy. Figures and the replaced documents are kept with it. No Word or PDF copies are issued. A copy in another format can be made when one is needed, but it is not a controlled copy.

Every change to the documents and the test evidence is recorded in a private records repository on the system owner's computer. It has no remote copy and is separate from the code repositories. Each change is dated, and each issue of the set is marked, so any earlier state can be shown. The set moves to \<Organisation\>'s restricted store when that is set up. Until then the repository is the change record, and a list of hashes fixes the content of each issue.

### 4.2 Parts of every document

**Table 5: Parts of every document**

| Order | Part | Contents |
| --- | --- | --- |
| 1 | Title | The document's full title, as the top-level heading |
| 2 | Section 1 Purpose | Why the document exists and what it covers |
| 3 | Numbered sections | The document's content |

Documents carry no contents list, section links, document control section, approval table or change history. Versions and changes are kept in the change record (section 4.1), and decisions in \<Decision Register\>.

A combined document uses its section 1 to explain its chapters, and then has one chapter for each family (section 4.4).

### 4.3 Titles and references

Each document is known by its title. In the text a document is cited by its title in angle brackets, as in \<Procedures\>.

### 4.4 Combined documents and chapters

\<Policy\>, \<Procedures\> and \<Control Assessment Record\> each hold one chapter for each control family, in CSS order. A chapter is named by its family code. Its sections carry the code, as in PS.3, and its tables are numbered Table PS-1, Table PS-2 and so on. Each of these documents has one version for the whole document. In \<Procedures\> each procedure is headed by its own number, such as PRO-PS-2.

**Table 6: How to cite a combined document**

| To cite | Write |
| --- | --- |
| A chapter | \<Policy\> (PS) |
| A chapter at a version of the document | \<Policy\> (PS) \<ver\> |
| A section | \<Policy\>, section PS.3 |
| A table | \<Policy\>, Table PS-1 |
| A rule | \<Policy\> (PS), R3 |
| A procedure | \<Procedures\>, PRO-PS-2 |

### 4.5 Versions and changes

1. Versions start at 0.1 and go to 1.0 on first approval.
2. Any change is a new version. What changed is recorded in the change record (section 4.1), not in the document.
3. A change that alters no rule, value, finding or decision is editorial. Renumbering and a corrected reference are editorial.
4. Any other change needs the decision of the document's approver, recorded in \<Decision Register\>.
5. A change to one chapter of a combined document is a new version of the document.
6. Moving a document into a combined document changes no content.
7. Records are not rewritten. Decided entries in \<Decision Register\> keep the names, section numbers and versions of their date.
8. Where a live statement cites another document at a version, the citation is kept at the current version.
9. Proof of each approval is the approver's signed sheet (\<Record Templates\>, TPL-24), listed in \<Decision Register\>, section 5.
### 4.6 Order of families

Wherever a document has a part for each family, the families are in CSS order: AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR. A new family takes its place in that order, and the sections and tables after it are renumbered, with every reference to them.

### 4.7 Live documents

\<Decision Register\>, \<Tailoring Register\>, \<Evidence Requests\>, \<Record Templates\> and \<Interview Guide\> are live documents, which grow as decisions are made and evidence arrives. Each live document follows these rules:

1. Where its entries for each family have content of their own, as in \<Evidence Requests\> and \<Interview Guide\>, it has one numbered section for each family, in CSS order, with cross-family content in its own section, and a family coverage table showing the state of every family.
2. Where its entries are rows of the same kind, as in \<Decision Register\>, it holds one table for each kind of entry, with a Family column, in place of a section for each family.
3. Its identifiers carry the family code, such as D-AU-nn, so that adding an entry never renumbers an existing one.
4. Each addition increases the version number and is recorded in the change record.
5. This map is updated at the same time.

### 4.8 Headings and numbering

**Table 7: Heading layers**

| Layer | Number | Markdown | Used for |
| --- | --- | --- | --- |
| Title | None | `#` | The document title |
| Section | 1 | `##` | Main sections |
| Subsection | 1.1 | `###` | Topics in a section |
| Sub-subsection | 1.1.1 | `####` | Individual items, such as one control |
| Chapter | PS | `##` | One family in a combined document. Its sections are one layer lower, so PS.1 is `###` |

Do not go deeper than three numbered layers below a section or chapter. Create a subsection only when there are at least two at that level. Section numbers use Arabic numerals with no full stop after the last.

Use numbered lists for steps and for rules that are cited, and bullets for items with no order. Numbered lists restart in each section unless the numbering must carry on, as in the rules in \<Security Operating Procedures\>.

### 4.9 Tables and figures

Number tables and figures separately, each from 1 in every document and in order of appearance, independent of section numbers. In a combined document each chapter numbers its own. When adding or removing one, renumber those that follow, with every reference to them. A table added between two others without renumbering takes a letter, as in Table 3a.

**Table 8: Captions**

| Item | Format | Position |
| --- | --- | --- |
| Table | **Table 1: Short title**, in bold | Directly above the table |
| Figure | **Figure 1: Short title**, in bold | Directly below the image |

Every table has a caption and a header row. A figure is a PNG image in the `figures` folder, with alternative text, and the text beside it says what the figure shows, so that nothing depends on the image alone. Give a cell a colour or a mark only when it means something, and always say the meaning in words too.

### 4.10 Fixed identifiers

These identifiers do not change when a document is renumbered or moved, so citations of them stay valid.

**Table 9: Fixed identifiers**

| Identifier | What it names | Where it is defined |
| --- | --- | --- |
| R1 | A policy rule, numbered in each chapter | \<Policy\> |
| PRO-AC-1 | A procedure | \<Procedures\> |
| P-01 | A parameter: a value the controls depend on | \<System Description\>, section 4 |
| AC-02\_ODP\[01\], AC-02a. | The CSS own identifier for a parameter or a determination statement | \<Control Assessment Record\> |
| D-AC-nn | A decision. D-AC-Pnn is the approval of parameter values | \<Decision Register\> |
| NC-AU-nn | A non-compliance entry | \<Risk List\>, section 5 |
| R-AC-nn | A risk | \<Risk List\>, section 2 |
| PA-nn | A POA&M item | \<Plan of Action and Milestones\>, section 3 |
| REC-n | A step on the road to authorisation | \<Plan of Action and Milestones\>, section 5 |
| TR-AC-01 | A tailoring entry | \<Tailoring Register\> |
| EV-AC-01 | An evidence request | \<Evidence Requests\> |
| INT-AC-01 | An interview question | \<Interview Guide\> |
| TPL-1 | A record template | \<Record Templates\> |
| A1, B1, C1 | A rule or duty in the operating procedures | \<Security Operating Procedures\> |
| Tnn, Ann, Lnn | A test check. The letter shows the script | \<Security Assessment Report\>, section 7 |

### 4.11 Checks on the set

An automatic check reads the whole set and confirms that the documents agree with each other, from the totals in the plan and the report to the links, the references between documents and the count of facts still to be supplied. Its results are kept as \<evidence\>. A gap it reports is a real inconsistency, which is corrected in the documents.

### 4.12 Sources used

No single standard sets a required layout, so this standard combines the sources in the table below.

**Table 10: Sources used**

| Source | What it supports here |
| --- | --- |
| [ISO 2145](https://en.wikipedia.org/wiki/ISO_2145) | Decimal section numbers with Arabic numerals and no full stop after them |
| [ISO/IEC Directives Part 2](https://www.iso.org/sites/directives/current/part2/index.xhtml), clauses 22, 28 and 29 | Limited subdivision, subsections only in twos or more, and tables and figures numbered continuously and separately from sections |
| [ISO/IEC 27001 clause 7.5](https://advisera.com/iso27001/clause-7-5-documented-information/) | Documents identified with title, date, author or reference number, consistent format, review and approval |
| CSS | What a system plan contains, and how its approval, reviews and changes are recorded |

ISO 2145 and ISO/IEC 27001 were read through secondary summaries, because the standards are paid for. Check them directly before relying on this standard for an external audit.

## 5 Open questions

1. Is Moderate the right security categorisation? The authorising official approves the categorisation (\<System Security Plan\>, section 3.3).
2. Who are the authorising official, administrators, auditors, security officers, business owners, the legal adviser's delegate and the Data Owner of each schema? \[Names, in \<Roles and Responsibilities\>\].
3. Which \<Organisation\> services and evidence cover the inherited controls, and does the Cyber Essentials Plus scope include the two VMs? \[Answer, from the evidence asked for in \<Evidence Requests\>\].
4. What target dates should High POA&M items have? \[Dates, set by the authorising official (\<Plan of Action and Milestones\>, section 2.1)\].
