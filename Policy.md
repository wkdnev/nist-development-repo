# \<System Name\> Security Policy

## 1 How to use this document

This document is the security and privacy policy for \<System Name\>. It holds one policy for each of the 19 CSS control families that apply, as chapters in CSS order. A policy says what must be true and who is accountable for it. How each rule is carried out is in \<Procedures\>, and the design, values and decisions are in each family's design document (\<Documentation Map\>, section 2.2).

The Head of Cyber approves each policy, and the legal adviser reviews it. The decisions each chapter needs are listed in \<Decision Register\>.

- **Chapters.** Each chapter is named by its family code. Its sections carry the code, so PS.3 is section 3 of the Personnel Security chapter, and its tables are numbered Table PS-1, Table PS-2 and so on.
- **Citing.** Cite a chapter as \<Policy\> (PS), a section as \<Policy\>, section PS.3, and a table as \<Policy\>, Table PS-1.
- **Versions.** The document has one version. A change to any chapter is a new version of the document.

### 1.1 Rules common to every policy

These rules apply to every chapter. They are stated once here. A chapter repeats one only where its rule differs or adds to it.

1. **Ownership:** the system owner manages each policy and its procedures.
2. **Approval:** the Head of Cyber approves each policy, as all policies, and the system owner approves the procedures and the family's design document.
3. **Policy review:** every 12 months, and after a significant incident, audit finding or system change.
4. **Procedures review:** every 12 months, and after a change to the steps.
5. **Compliance and management commitment:** the system owner reviews compliance at each review and records the result.
6. **Records:** the policy and procedures are under version control, and each review is recorded in the change record (\<Documentation Map\>, section 4.1).
7. **Non-compliance:** a control counts as non-compliant until shown otherwise. Each non-compliance is recorded and rated in \<Risk List\>, and a named person decides its treatment: the system owner for Low risks, and the authorising official for Medium and High risks. A fix is made only through \<Plan of Action and Milestones\>. Section 1.2 sets out the approach in full.

### 1.2 Non-compliance and risk acceptance

The organisation takes a risk-based approach to these requirements. No system meets every control, and a non-compliance is acceptable when its risk is understood and has been accepted by the right person.

1. Every non-compliance must be identified, documented and recorded in \<Risk List\>.
2. Its risk must be rated by the method in \<Risk List\>, section 4.
3. A named person must decide its treatment: accept, remediate, approve a value, obtain evidence or tailor the control. The system owner decides Low risks and the authorising official decides Medium and High risks.
4. A risk that is too high to accept requires a remediation plan in \<Plan of Action and Milestones\>. A High risk may be accepted only for a limited period while that plan runs.
5. A remediation is carried out through that plan and its milestones, and does not begin simply because a non-compliance was found.
6. Every acceptance is recorded with the name, date, reason and review date, and is reviewed at the interval in \<Risk List\>. PRO-AC-17 sets out the steps.
7. A vulnerability that cannot be fixed in time is recorded the same way, with its compensating measure.

### 1.3 Terms and references

Terms used in the policies are defined in \<System Description\>, section 12. Each chapter names the laws it must be consistent with in its governance requirements. The family's design document, \<Procedures\> and \<Security Operating Procedures\> carry it out. Table 1 lists the other standards and guidance the policies draw on.

**Table 1: Standards and guidance**

| Reference | Families | Use |
| --- | --- | --- |
| CSS, the NICE Framework | AT | Describing role training |
| NCSC 10 Steps: engagement and training; NCSC phishing guidance | AT | Needs-led training and blame-free reporting |
| ICO data protection audit framework: training and awareness | AT | Privacy training and evidence of understanding |
| CSS, Guide to Computer Security Log Management | AU | Good practice for log management |
| CSS, Risk Management Framework | CA | The assessment and authorisation process |
| CSS, Information Security Continuous Monitoring | CA | The monitoring strategy |
| CSS, Managing the Security of Information Exchanges | CA | Agreements for connections |
| CSS, Security-Focused Configuration Management | CM | The plan structure, board charter and impact analysis |
| CIS Benchmarks | CM | Secure settings for Windows Server and SQL Server |
| Cyber Essentials | CM | \<Organisation\>'s scheme: secure configuration and updates |
| Copyright, Designs and Patents Act 1988 | CM | Software licences |
| CSS, Contingency Planning Guide for Federal Information Systems | CP | The plan structure and business impact analysis |
| CSS, Guide to Test, Training, and Exercise Programs | CP | Testing, exercises and after-action reports |
| CSS, Digital Identity Guidelines | IA | Choosing assurance levels |
| CSS, Authentication and Authenticator Management | IA | Password, multi-factor and reauthentication rules |
| NCSC password guidance | IA | The UK view on password rules |
| ICO guide to personal data breaches | IR | Reporting to the ICO and telling the people affected |
| NCSC incident management guidance | IR | Reporting and handling cyber incidents in the UK |
| CSS and IEEE 2883-2022 | MA, MP | Sanitising equipment and media |
| NCSC Secure System Administration | MA | Trusted devices, multi-factor sign-in and monitoring for administration |
| NCSC Secure sanitisation of storage media | MP | UK guidance on sanitising and disposal |
| DIN 66399 | MP | Shredding levels for paper |
| ISO/IEC 27001:2022, Annex A.7; AICPA SOC 2, CC6.4 | PE | How \<Organisation\> evidences physical controls |
| ASHRAE TC 9.9 thermal guidelines | PE | Data centre temperature and humidity |
| NCSC home working guidance; NPSA physical security guidance | PE | UK guidance for home working and sites |
| CSS, tasks S-2 and S-6 | PL | Tailoring and plan approval |
| HMG Baseline Personnel Security Standard | PS | The four checks used as the minimum in R2 |
| NPSA, Employment screening: a good practice guide; BS 7858:2019 | PS | What a fuller screening standard covers, for comparison with \<Organisation\>'s own |
| ICO guidance: keeping employment records; data protection impact assessments | PT | How the law applies to staff records |
| NCSC vulnerability management guidance | RA | Updating by default, responding to exploitation, and owning the risk of not updating |
| CISA Known Exploited Vulnerabilities catalogue | RA | The list of exploited flaws |
| NCSC secure design principles; CSS privacy engineering objectives | SA | The engineering principles |
| OWASP ASVS 5.0 | SA | The verification depth for the web applications |
| UK Software Security Code of Practice | SA, SR | Peer practice the policy aligns with |
| NCSC, Using TLS to protect data | SC | The TLS profiles |
| Microsoft, SQL Server 2022 documentation, encrypted connections and strict encryption | SC | Database TLS enforcement |
| Microsoft, ASP.NET Core Data Protection key encryption at rest | SC | The key ring protection |
| OWASP File Upload Cheat Sheet | SI | Upload checks |
| NCSC Early Warning; CISA Known Exploited Vulnerabilities catalogue | SI | Advisory sources |
| ICO, Employment practices and data protection: monitoring workers | SI | Monitoring people |
| CSS, update 1 | SR | Supply chain risk management practice and the plan's content |
| NCSC supply chain security principles | SR | Supplier reviews |
| CISA minimum elements for a software bill of materials | SR | What the bill of materials holds |

## AC Access Control

### AC.1 Purpose and scope

This policy sets the organisation's rules and principles for access to \<System Name\>: what is mandatory, and who answers for it. The Head of Cyber approves it, as all policies, and the legal adviser reviews it. The approved decisions and settings that carry it out are in \<Access Control Management\>, and the steps people follow are in \<Procedures\> (AC).

This policy sets who may access \<System Name\>, what they may do, and how that access is controlled, in line with the CSS AC family (AC-1).

It applies to everyone who uses or administers the UI application, the Admin application, the API, the \<System Name\> database and the two Windows Server 2025 VMs they run on at \<Organisation\>, and to any service account they use.

### AC.2 The organisation's position

Items in \<System Name\> are available only to people with an approved need. Convenience never overrides that. The organisation accepts that some access controls depend on \<Organisation\>, and it stays accountable for making sure they are in place and evidenced. The Head of Cyber, for \<Organisation\>'s management, is committed to this policy: to providing the people, time and tools it needs, to reviewing how well it works, and to acting on breaches of it.

### AC.3 Control principles

1. Access is denied unless a role or group grants it.
2. Each person has one named account. Shared accounts are not allowed.
3. People get the least access their job needs, and it is removed when the need ends.
4. Duties that could be misused together are held by different people where staffing allows.
5. Privileged actions are recorded and reviewed.
6. Access routes and information flows are approved in advance.
7. Access is reviewed regularly and corrected when it no longer matches a person's need.

### AC.4 Mandatory requirements

**Table AC-1: Mandatory requirements**

| No. | Requirement | Controls |
| --- | --- | --- |
| R1 | Only named accounts of an allowed type may be used. Shared, guest and anonymous accounts are not allowed | AC-2 |
| R2 | Every account, group membership and privilege must have a recorded approval before it is granted | AC-2, AC-6(5) |
| R3 | Access must change promptly when people join, move or leave. Accounts that are unused, unneeded or a risk must be disabled. Account management must use automated support where the system provides it | AC-2, AC-2(1), AC-2(3), AC-2(13) |
| R4 | Temporary and emergency accounts must not be used (P-39) | AC-2(2) |
| R5 | The system must enforce approved access and deny everything else. Only approved actions may work without signing in | AC-3, AC-14 |
| R6 | People and processes must have only the access their tasks need. Only authorised people may use security functions or see security-relevant information | AC-6, AC-6(1), AC-6(5), AC-6(10) |
| R7 | People with privileged access must use a non-privileged account for everyday work | AC-6(2) |
| R8 | Duties that could be misused together must be separated | AC-5 |
| R9 | Account changes and privileged actions must be recorded against the person who made them | AC-2(4), AC-6(9) |
| R10 | Access and privileges must be reviewed at set intervals | AC-2, AC-6(7) |
| R11 | Repeated failed sign-ins must lock the account, in PingFederate and Active Directory (P-42). An unattended device must lock its screen after a set time without activity (P-03). \<System Name\>'s session is its authentication cookie: it must end at most 8 hours after sign-in (P-02), never outlast PingFederate's sign-in, re-check the person every 5 minutes on an open page, and end when the person signs out. Users must sign out as P-53 sets. A system use notice must be shown at sign-in, and accepted before anything else is shown | AC-2(5), AC-7, AC-8, AC-11, AC-11(1), AC-12 |
| R12 | Information must flow only along approved routes. Remote access must use an approved, managed and encrypted route. Privileged access over remote access is allowed only for the needs in P-54, through the VPN and then the managed administration route | AC-4, AC-17 family |
| R13 | Wireless access, mobile devices, external systems and portable storage must follow approved rules | AC-18, AC-19 and AC-20 families |
| R14 | Information may be shared outside a schema only after a decision by its Data Owner. \<System Name\> does not hold public content | AC-21, AC-22 |

### AC.5 Responsibilities

**Table AC-2: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves all policies, including this one |
| System owner | Owns this policy and the five role groups (\<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners and \<Code\>\_LegalSearch); authorises privileged access and adds each member; approves exceptions and accepts risk within their authority |
| Authorising official | Accepts residual risk and authorises operation |
| Data Owner | Owns a schema's data and its read and edit groups; as the group's owner, authorises, through the ServiceNow access approval workflow, who may read or edit the schema; approves any change to the groups a schema uses; and decides whether its information may be shared |
| Line manager | Approves their people's access requests in ServiceNow, confirming the need |
| Administrator | Manages schemas, the AD groups each schema uses (a change only with the Data Owner's approval), and system settings, in the Admin application. Sees no item content. Cannot add anyone to a group |
| Auditor | Reads the audit log and reviews it weekly, including privileged activity, and reports anything suspicious to the security officer. Holds no administration role |
| Security officer | Monitors security information, reviews alerts and the central logs, and leads incident response. Runs the monthly check of members who have not signed in for 90 days (P-38). Does not read the audit log. Holds no administration role |
| Business owner | Approves, in the UI application, the disposal of items due under the retention schedule (FR-074). Member of \<Code\>\_BusinessOwners |
| Legal adviser's delegate | Searches every schema, in the UI application, for one person's items to answer a request under data protection law (FR-073). Member of \<Code\>\_LegalSearch, named by the legal adviser. Holds no other role |
| Windows server and database administrators | Keep to these requirements on the servers and in SQL Server |
| \<Organisation\> security contact | Provides evidence for the controls \<System Name\> inherits |
| Every user | Follows the Security Operating Procedures (\<Security Operating Procedures\>) |

The people holding each role are named in \<Roles and Responsibilities\>.

### AC.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review and records the result. Breaches may lead to loss of access and to disciplinary action. They may also be offences under the Computer Misuse Act 1990 or the Data Protection Act 2018, as \<Security Operating Procedures\>, rule A4, explains.
3. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how inherited controls, leavers and incidents are handled, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS.
5. **Exceptions:** an exception needs written approval from the system owner, a stated end date and an entry in \<Risk List\>. \<Access Control Management\> sets the rules, and PRO-AC-15 sets the steps.

## AT Awareness and Training

### AT.1 Purpose and scope

This policy sets the organisation's rules for security and privacy awareness and training for \<System Name\>, in line with the CSS AT family (AT-1). It stands alone, as each family has its own policy. The curriculum, briefing, training matrix, measures and register are in \<Awareness and Training Management\>, and the steps people follow are in \<Procedures\> (AT).

It applies to everyone who uses, administers or develops \<System Name\>, including \<Organisation\>'s staff who hold a \<System Name\> role, and to the other roles named in the training matrix for the security or privacy duties they hold: the legal adviser, the authorising official, the information owner and line managers. It covers the training other families require: incident response (IR-2), contingency (CP-3), privacy (AT-3(5)) and the rules of behaviour (PL-4).

### AT.2 The organisation's position

\<System Name\> holds Moderate-impact information, including personal data, so the people who use and run it are part of its protection. \<Organisation\>'s general course gives everyone the basics; \<System Name\> adds what is specific to it, and trains each role in the duties it actually performs. Training that cannot be shown, or that people did not understand, does not count.

### AT.3 Control principles

1. **Train before access:** no access without awareness training, and no privileged role without role training.
2. **Train for the job:** role training follows the \<System Name\> procedures the role runs.
3. **Check understanding:** each module ends with a short check.
4. **Make reporting safe:** people are thanked, not blamed, for reporting a mistake or a suspicious message.
5. **Keep records:** training that cannot be shown did not happen.

### AT.4 Mandatory requirements

1. **R1 Awareness:** all users must complete \<Organisation\>'s security and privacy awareness course and the \<System Name\> briefing before getting access, and every 12 months.
2. **R2 Briefing content:** the \<System Name\> briefing must cover the classification of its items and the export rules, insider threat and social engineering scenarios specific to \<System Name\>, privacy and how to recognise and report a personal data breach, and how to report.
3. **R3 Rules of behaviour:** all users must sign \<Security Operating Procedures\> Part A, and privileged users Part B, before access.
4. **R4 Role training:** each role in the training matrix must complete its modules before privileged access, and every 12 months. Incident response and contingency training must be completed within 30 days of taking the role.
5. **R5 Privacy training:** all users must receive privacy training in the \<System Name\> briefing before access and every 12 months. The roles the training matrix names for it, including all administrators and the auditor, must also complete the privacy module (M9) before access and every 12 months.
6. **R6 Updates:** content must be reviewed every 12 months, and after a significant incident, exercise or change, with the lessons added.
7. **R7 Checks and measures:** each module must end with a check, with a pass mark of 80%. The measures in \<Awareness and Training Management\>, section 3.9, must be reported monthly by the security officer and reviewed by the system owner.
8. **R8 Phishing simulations:** none may be run without the agreement of HR and the legal adviser. If run, no one is penalised for clicking, and the measure is reports, not clicks.
9. **R9 Records:** every completion must be recorded on TPL-9 and in the training register, and kept for 3 years.
10. **R10 Checking:** Test-PlanConsistency.ps1 must show that every security role has its training defined, at each review.

### AT.5 Responsibilities

**Table AT-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies; delivers module M6 to the security officer and auditor, and M7 to the security officer |
| Authorising official | Decides Medium and High risks; completes module M10 |
| System owner | Owns this policy, the curriculum and the matrix; gives the \<System Name\> briefing; checks the register before granting a role |
| Security officer | Writes and updates role training content, delivers the modules \<Awareness and Training Management\>, Table 3 gives them, keeps the register and reports the measures |
| Legal adviser | Reviews privacy training content and agrees any phishing simulation; completes module M7 |
| Line managers | Complete briefing part B7 before their first approval of an access request, and make sure their staff complete training on time |
| Everyone | Completes training, and reports anything suspicious |
| \<Organisation\> | Provides the general course and its records, and evidences its administrators' role training |

### AT.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses, administers or develops \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews the measures monthly and compliance at each review, and records the result.
3. **Coordination:** the system owner agrees with \<Organisation\> how its course and its administrators' training are evidenced, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS.

## AU Audit and Accountability

### AU.1 Purpose and scope

This policy sets the organisation's rules for recording and reviewing activity in \<System Name\>, so that actions can be traced to a person and incidents can be investigated, in line with the CSS AU family (AU-1). The settings that carry it out are in \<Audit and Accountability Management\>, and the steps people follow are in \<Procedures\> (AU).

It applies to the UI application, the Admin application, the API, the \<System Name\> database and the two Windows Server 2025 VMs they run on at \<Organisation\>, and to everyone who administers or reviews them.

### AU.2 The organisation's position

Every security-relevant action in \<System Name\> must leave a reliable record that names the person responsible. Records exist to support investigation and accountability, and are not used for any other purpose without the system owner's approval.

### AU.3 Control principles

1. **Complete:** the agreed events are recorded every time they occur.
2. **Attributable:** each record shows what happened, when, where, from where, the outcome and who was involved.
3. **Protected:** nobody can change or delete a record, except under the retention rule in section AU.4, and access to records is limited to those who review them.
4. **Reviewed:** records are examined regularly by someone who does not administer the system.
5. **Retained:** records are kept long enough to investigate an incident.

### AU.4 Mandatory requirements

1. **R1 Events:** the events in \<Audit and Accountability Management\> must be logged by each component it names.
2. **R2 Retention:** records must be kept for 12 months online and a further 12 months in an offline archive whose hash is recorded (P-07), with storage sized to match. This applies to the application audit log, and to the SQL Server Audit records, Windows logs and application security events held in central logging. After 24 months they may be deleted, only with the system owner's recorded approval.
3. **R3 Time:** time stamps must be in UTC to the nearest second, from \<Organisation\>'s time source, and within 1 second of UTC (P-09).
4. **R4 Protection:** auditors alone read audit records, except that the security officer's last sign-in report shows each member's username and last sign-in date and nothing else (FR-085), and the database administrator reaches them only to archive them. Nobody may change or delete them, except as R2 allows.
5. **R5 Review:** the auditor must review the audit log weekly (P-08, NFR-027), compare it with the server, database, PingFederate and Active Directory records, record the review, and report anything suspicious to the security officer. Nobody else reviews the audit log. The auditor's own reads and exports are reviewed by the security officer, from central logging.
6. **R6 Logging failure:** a logging failure must alert the Windows server administrator and security officer within 1 hour. Any action that cannot be recorded is refused until logging is restored (P-61).
7. **R7 Tampering:** suspected tampering must alert the security officer and auditor.
8. **R8 Content of records:** records must not contain passwords, keys, tokens or cookie values, and must hold only the personal data an investigation needs.
9. **R9 Other logs:** any other log that repeats audit information, such as an application or server log, is audit information under this policy: it is protected, limited to those who need it, and kept only for the period set in \<Audit and Accountability Management\>.

### AU.5 Responsibilities

**Table AU-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy, decides which events are logged, and receives review findings |
| Authorising official | Decides Medium and High risks |
| Auditor | Reviews records weekly and reports findings |
| Security officer | Receives the auditors' reports of anything suspicious and the alerts, reviews the central logs, and handles incidents. Does not read the audit log |
| Windows server administrator | Receives logging failure alerts, and restores logging on the VMs |
| Database administrator | Protects and retains the audit data in SQL Server |
| Developers | Build logging into the application |

### AU.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers or reviews \<System Name\>, and whenever they change.
2. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how logs from inherited services are shared, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR and the Data Protection Act 2018 for personal data in records, the Computer Misuse Act 1990 for misuse of the system and the use of records as evidence, \<Organisation\>'s policies and CSS.

## CA Assessment, Authorization, and Monitoring

### CA.1 Purpose and scope

This policy sets the organisation's rules for assessing \<System Name\>'s controls, authorising it to operate and monitoring it afterwards, in line with the CSS CA family (CA-1). It stands alone, as each family has its own policy. The settings that carry it out are in \<Assessment, Authorization, and Monitoring Management\>, and the steps people follow are in \<Procedures\> (CA).

It applies to the UI application, the Admin application, the API, the \<System Name\> database, the two Windows Server 2025 VMs they run on at \<Organisation\>, and their connections to other systems.

### CA.2 The organisation's position

\<System Name\> must not hold real data until the authorising official has authorised it. Authorisation rests on an honest assessment, including an independent one, and continues only while monitoring shows the risk stays acceptable.

### CA.3 Control principles

1. **Two levels:** the system owner self-assesses at Level 1, and an independent team assesses at Level 2 before each authorisation.
2. **Authorise knowingly:** the authorising official accepts the remaining risk by name.
3. **Track what is open:** weaknesses stay on the plan until fixed.
4. **Know the connections:** each connection to another system is recorded and approved.

### CA.4 Mandatory requirements

1. **R1 Assessment:** controls must be assessed every 12 months, with results given to the system owner, authorising official and Head of Cyber, and the privacy results to the legal adviser.
2. **R2 Independence:** every authorisation must rest on an independent assessment, carried out every 12 months by assessors who have had no part in designing, building, running or administering \<System Name\> (Level 2). The system owner's self-assessment (Level 1) prepares for it and never replaces it.
3. **R3 Connections:** each exchange with another system (PingFederate, Active Directory over LDAPS, and \<Organisation\>'s time, logging, proxy and backup services: flows F6 to F8 and F10 in \<System Description\>, section 6.5), and each internal connection between \<System Name\>'s own components (flows F3 to F5), must be recorded with its security and privacy needs, approved, reviewed every 12 months, and encrypted. ServiceNow and the starters and leavers process have no connection to \<System Name\>: people carry their decisions across (F9).
4. **R4 Plan of action:** \<Plan of Action and Milestones\> must be updated monthly. Each open item must be fixed within the time set for its rating, counted from go-live or from the date the item is raised, whichever is later: High items within the time the authorising official sets, Medium within 180 days and Low within 365 days. Overdue items are reported to the authorising official each quarter.
5. **R5 Authorisation:** the authorising official must authorise \<System Name\> before it holds real data, and review the authorisation every 12 months (P-25).
6. **R6 Monitoring:** the security and privacy measures in \<Assessment, Authorization, and Monitoring Management\>, section 3.8, must be reported monthly to the system owner, with the privacy measures also to the legal adviser, and quarterly to the authorising official.
7. **R7 Significant change:** a significant change must be assessed before it is made, and the authorising official decides whether \<System Name\> must be re-assessed or re-authorised.
8. **R8 Authorisation package:** the authorising official receives the authorisation package listed in \<Assessment, Authorization, and Monitoring Management\>, section 3.5, and records each decision on TPL-18, with its terms, conditions and end date.
9. **R9 Inherited controls:** the controls inherited from \<Organisation\> must be listed, and accepted by the authorising official, before \<System Name\> operates.

### CA.5 Responsibilities

**Table CA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies, and receives assessment results |
| System owner | Owns this policy, runs Level 1, and keeps the plan up to date |
| Authorising official | Authorises \<System Name\>, and decides Medium and High risks |
| Security assessor | Leads the independent Level 2 assessment |
| Security officer | Produces the monitoring report |
| Windows server administrator | Keeps connections to what is approved |
| \<Organisation\> | Provides the inherited controls, and agrees the connections it owns |

### CA.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\>, and whenever they change.
2. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how inherited controls are provided, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR and the Data Protection Act 2018, \<Organisation\>'s policies and CSS.

## CM Configuration Management

### CM.1 Purpose and scope

This policy sets the organisation's rules for controlling how \<System Name\> is configured and changed, in line with the CSS CM family (CM-1). It stands alone, as each family has its own policy. \<Configuration Management\> holds the design, and is the Configuration Management Plan that CM-9 requires. \<Procedures\> (CM) holds the steps.

It applies to the UI application, the Admin application, the API, the \<System Name\> database and the two Windows Server 2025 VMs they run on at \<Organisation\>.

### CM.2 The organisation's position

\<System Name\> must run from a known, recorded configuration, and every change must be approved, tested and traceable.

### CM.3 Control principles

1. **Known baseline:** the approved configuration is recorded and versioned.
2. **Controlled change:** no change happens without approval and testing.
3. **Least functionality:** anything not needed is turned off.
4. **Accurate inventory:** every component is recorded, and unauthorised ones are detected.

### CM.4 Mandatory requirements

1. **R1 Baselines:** baselines must be reviewed every 12 months and at each release, keeping the 3 previous configurations (\<System Description\>, P-63).
2. **R2 Change control:** every change needs a change request, in ServiceNow or on TPL-6, decided by the change control board under its charter in \<Configuration Management\>, section 3.8, and tested before release. Nobody approves a change they requested or made. The board meets monthly, and records are kept for 3 years (P-64). An emergency change is allowed only to stop or limit an incident or an outage, is approved first by the system owner or their deputy, and is confirmed or reversed by the board at its next meeting.
3. **R3 Settings:** settings follow the CIS Benchmarks for Windows Server 2025 and SQL Server 2022, with exceptions recorded.
4. **R4 Routes:** only the flows in \<System Description\>, section 6.5, are open: HTTPS to the UI application on TCP 443 (F1); the Admin application only over \<Organisation\>'s managed administration route (F2); the API on the application server's loopback address only (F3, F4); SQL Server on TCP 1433 from the application server only (F5); users' browsers to PingFederate (F6); LDAPS on TCP 636 from the application server to Active Directory (F7); both servers to \<Organisation\>'s time, logging, proxy and backup services (F8); HTTPS on TCP 443 from the application server only to PingFederate, for its OpenID Connect metadata and signing certificate and to complete each sign-in (F10); and server and database administration from the administrators' managed devices to both servers only over the administration route, with multi-factor authentication, using named accounts (F11). Everything else is off, and this is reviewed every 12 months (P-65).
5. **R5 Approved software:** an approved software list is kept and reviewed every 12 months, and what is installed on the servers is compared with it every 12 months (P-65). Only software on the list may run on the servers: Windows App Control for Business denies everything else.
6. **R6 Installing software:** only the named Windows server administrators may install software on the servers, and only with the system owner's approval of a request. Nobody else has the rights to install it. Software on users' devices is governed by \<Organisation\>'s policy.
7. **R7 Inventory:** the server inventory in \<System Security Plan\> and the software component inventory in \<Configuration Management\> are updated at each change, with each component's version, supplier and licence, and reviewed every 12 months and at each release (P-63). \<Organisation\>'s tools detect unauthorised components monthly and alert the Windows server administrator, who removes the component or disables its network access and tells the security officer (P-66).
8. **R8 Reproducible releases:** each release must be reproducible: code at a signed tag, and every package and component at a pinned version, with its checksum, recorded in the baseline.
9. **R9 Licences:** every component's licence must be known and permit \<System Name\>'s use before it enters the baseline; the system owner records any licence decision in \<Decision Register\>.
10. **R10 Every layer:** secure settings apply to every layer: Windows Server, SQL Server, the Windows services that host the applications and the applications themselves, as set in \<Configuration Management\>.
11. **R11 Impact analysis:** every change has a recorded security and privacy impact analysis against the criteria in \<Configuration Management\>, including the significant change test in \<Assessment, Authorization, and Monitoring Management\>, section 3.9.
12. **R12 Drift:** the running configuration is compared with the baseline every month and at each release (P-29), and any drift is reported to the security officer and corrected or approved through change control.

### CM.5 Responsibilities

**Table CM-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the plan, chairs the change control board, and approves emergency changes |
| Authorising official | Decides Medium and High risks, and significant and High impact changes |
| Security officer | Analyses the impact of each change, and represents security on the change control board |
| Legal adviser | Represents privacy on the change control board, and decides on each change that touches personal data |
| Windows server administrator | Sits on the change control board, and manages VM settings and software |
| Database administrator | Manages SQL Server settings |
| Developers | Build, test and release changes |
| \<Organisation\> | Provides detection tools and the ServiceNow service desk |

### CM.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who changes or administers \<System Name\>, and whenever they change.
2. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how changes on its services are coordinated, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including the Copyright, Designs and Patents Act 1988 for software licences, \<Organisation\>'s policies and CSS.

## CP Contingency Planning

### CP.1 Purpose and scope

This policy sets the organisation's rules for keeping \<System Name\> recoverable, in line with the CSS CP family (CP-1). It stands alone, as each family has its own policy. The plan that carries it out is \<Contingency Planning Management\>, and the steps people follow are in \<Procedures\> (CP).

It applies to the UI application, the Admin application, the API, the \<System Name\> database, its backups, the secrets the applications need, and the two Windows Server 2025 VMs they run on at \<Organisation\>.

### CP.2 The organisation's position

\<System Name\>'s availability is rated Low, so a short outage can be tolerated. Losing its items or audit records cannot, so encrypted backups and tested recovery are required before \<System Name\> holds real data.

### CP.3 Control principles

1. **P1 Know what matters:** recovery objectives come from a business impact analysis, not a guess.
2. **P2 Keep copies apart:** encrypted backups are held away from the main site, with one copy that an attacker on the network cannot change.
3. **P3 Test recovery:** a backup counts only once it has been restored and checked.
4. **P4 Plan ahead:** people know their part, and how to reach each other, before anything fails.
5. **P5 Coordinate:** this plan works with the incident response plan and \<Organisation\>'s plans.
6. **P6 Return only when safe:** users come back when the data, the functions and the controls have all been checked.

### CP.4 Mandatory requirements

1. **R1 Recovery objectives:** recovery objectives must be set by a business impact analysis, reviewed every 12 months. Essential functions must be back within 72 hours of the outage starting (P-12), within a maximum tolerable downtime of 120 hours (P-14), losing no more than 24 hours of data (P-13).
2. **R2 Backups:** the database, which holds the items, their files and the audit records, must be backed up daily with its transaction logs backed up between the daily backups; system-level information, including SQL Server's system databases and each VM's configuration, weekly and after each change to it; the secrets and documentation at each change.
3. **R3 Where and how:** backups must be encrypted, and held at a second \<Organisation\> site that does not share the main site's hazards.
4. **R4 Restore tests:** a restore must be tested every 6 months (P-16), and after a change to the database or backups, by restoring a backup and its encryption certificate from the second site onto a throwaway server there, and checking the restored data against counts and hashes taken when the backup was made. The test server must have no route to production and be erased afterwards.
5. **R5 Second site:** the VMs must be able to be rebuilt at that second site if the main one is lost.
6. **R6 Plan tests:** the plan must be tested every 12 months by tabletop exercise and restore test, coordinated with the incident response plan and \<Organisation\>'s plans.
7. **R7 Training:** people with a contingency role must be trained within 30 days of taking it and every 12 months.
8. **R8 The plan:** the plan must be approved by the system owner and authorising official, reviewed every 12 months and after a test or activation, shared with the people it names, and protected from disclosure and change.
9. **R9 Retention:** at least 14 daily, 8 weekly and 12 monthly backups must be kept, and one copy must be offline or immutable (P-15).
10. **R10 Keys and secrets:** the backup encryption certificate, with its private key, and the protected copy of the secrets must be held apart from the backups, and only the system owner and the Windows server and database administrators may reach them. A retired backup encryption certificate must be kept until the last backup it encrypted is removed.
11. **R11 Return and learning:** users return after a recovery only when the data, functions and controls have been checked, and any item deleted since the backup restored has been deleted again. Each test or activation must end with an after-action report within 10 working days.

### CP.5 Responsibilities

**Table CP-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the plan, decides when to invoke it, declares recovery, and trains the role holders |
| Authorising official | Approves the plan, and decides Medium and High risks, including running in a reduced state |
| Security officer | Coordinates the plan with incident handling, keeps the activity log, confirms controls before users return, writes after-action reports, and keeps the contingency training content current |
| Database administrator | Runs backups, holds the backup encryption certificate, tests restores and restores the database |
| Windows server administrator | Backs up system configuration, rebuilds the VMs, builds and removes the restore test server, and restores the secrets |
| Business owner and legal adviser | After a recovery from an older backup, list the items disposed of or deleted since, so that they are deleted again |
| \<Organisation\> | Provides the second site, the backup service with its offline or immutable copy, network services and telecommunications |

### CP.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Ownership:** the system owner manages this policy, the plan and the procedures.
2. **Approval:** the Head of Cyber approves this policy, as all policies; the system owner and authorising official approve the plan; and the system owner approves the procedures.
3. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\>, and whenever they change.
4. **Policy review:** every 12 months, and after a significant incident, audit finding, system change, contingency test or activation.
5. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how the second site, network and telecommunications are provided, and records it.
6. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Article 32(1)(b) and (c), which require resilience and the ability to restore personal data in a timely manner, and the Data Protection Act 2018; \<Organisation\>'s policies; and CSS.

## IA Identification and Authentication

### IA.1 Purpose and scope

This policy sets the organisation's rules for proving who is using \<System Name\>, in line with the CSS IA family (IA-1). The settings that carry it out are in \<Identification and Authentication Management\>, and the steps people follow are in \<Procedures\> (IA).

It applies to everyone who uses or administers the UI application, the Admin application, the API, the \<System Name\> database and the two Windows Server 2025 VMs they run on at \<Organisation\>, and to every service account and secret they use.

### IA.2 The organisation's position

Every action in \<System Name\> must be traceable to one known person. Access depends on a proven identity and a protected authenticator, at the assurance level set in \<Identification and Authentication Management\>, and privileged access needs stronger proof than ordinary access.

### IA.3 Control principles

1. **P1 Unique:** each person has one named identifier, which is never reused.
2. **P2 Proven:** a person's identity is established before an account is issued.
3. **P3 Strong:** authenticators are hard to guess or steal, and every sign-in needs more than a password.
4. **P4 Protected:** authenticators are never stored or sent in the clear, and secrets are not kept in source code.
5. **P5 Current:** authenticators change whenever they may be compromised.

### IA.4 Mandatory requirements

1. **R1 Who may have access:** only \<Organisation\>'s staff and contractors, who hold an Active Directory account and whose identity \<Organisation\>'s HR has checked. Non-organisational users are not allowed.
2. **R2 Identifiers:** a person's Active Directory account name is their identifier. It is unique and named, is never reused, and shows staff or contractor status. \<System Name\> issues no identifiers of its own.
3. **R3 Sign-in:** every user must sign in through \<Organisation\>'s single sign-on service, PingFederate. \<System Name\> must hold no passwords and no accounts of its own. Password rules are those of \<Organisation\>'s corporate standard, which \<System Name\> accepts.
4. **R4 Password changes:** follow \<Organisation\>'s corporate standard. Anyone who thinks their password is known must report it at once to \<Organisation\>'s service desk and the security officer. The account is disabled before the password is reset, because a password change alone does not end a \<System Name\> sign-in (\<Procedures\>, PRO-IA-3).
5. **R5 Secrets:** the secrets, the token signing key, the audit chain key and the OpenID Connect client credential, must be held in a key store outside source code and settings files, changed as P-10 sets and when an administrator who could read them leaves, and never recorded in clear. Each application runs under its own group managed service account, whose password the operating system sets and changes. The API connects to SQL Server with Windows authentication, so no database password exists.
6. **R6 Multi-factor:** every user must sign in with multi-factor authentication, which PingFederate provides.
7. **R7 Signing in again:** when the application's sign-in ends, 8 hours after sign-in at most and never later than PingFederate's sign-in (\<System Description\>, P-02), or when the person signs out. \<System Name\> has no idle timeout, idle lock or limit on sign-ins. The API reads a person's groups and whether their account is enabled from Active Directory over LDAPS on every request, holding each answer for at most 5 minutes, so a change takes effect within 5 minutes.
8. **R8 Assurance levels:** the identity and authenticator assurance levels in \<Identification and Authentication Management\>, section 3.4, must be met for each user group, and reviewed every 12 months.
9. **R9 Authenticator inventory:** every authenticator must be listed in \<Identification and Authentication Management\>, section 3.5, with its owner, storage and change period, and reviewed every 12 months.
10. **R10 Protection:** authenticators and tokens must travel only over encrypted connections, and \<System Name\> must accept only a sign-in response that PingFederate has signed. A user's access is ended by disabling their AD account or removing their group membership; the API refuses them within 5 minutes, even while a sign-in is open. Ending the PingFederate sign-in alone does not end access, so a suspected compromise starts with disabling the account.
11. **R11 Loss:** a lost, stolen or exposed authenticator must be reported straight away to \<Organisation\>'s service desk and the security officer, and replaced or reset.

### IA.5 Responsibilities

**Table IA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy, authorises privileged roles and manages the members of their AD groups, and reviews the assurance levels and authenticator inventory |
| Authorising official | Accepts the assurance levels, and decides Medium and High risks, including multi-factor sign-in |
| Data Owner | Authorises access to their schema, and manages the members of its AD groups |
| Administrator | Issues no identifiers, accounts or passwords: \<System Name\> holds none |
| Windows server and database administrators | Hold and change the secrets in the key store: the token signing key, the audit chain key and, with \<Organisation\>'s PingFederate team, the OpenID Connect client credential |
| \<Organisation\> | Proves identity through pre-employment checks; provides the Active Directory accounts, PingFederate sign-in with multi-factor authentication, and password and second factor resets; identifies devices on its network |
| Everyone with an account | Protects their authenticators and reports loss or suspected compromise |

### IA.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review and records the result. Breaches may lead to loss of access and disciplinary action.
3. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how identity proofing, device identification and sign-in through PingFederate are provided, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Article 32, which requires appropriate security of personal data, and the Computer Misuse Act 1990; \<Organisation\>'s policies; and CSS.

## IR Incident Response

### IR.1 Purpose and scope

This policy sets the organisation's rules for handling security incidents affecting \<System Name\>, in line with the CSS IR family (IR-1) and CSS. It stands alone, as each family has its own policy. The plan that carries it out is \<Incident Response Management\>, and the steps people follow are in \<Procedures\> (IR).

It applies to the UI application, the Admin application, the API, the \<System Name\> database, its backups and secrets, the two Windows Server 2025 VMs they run on at \<Organisation\>, and everyone who uses or administers them.

### IR.2 The organisation's position

Incidents are reported at once, without blame. \<System Name\> holds Moderate-impact information, including personal data, so a delay can cause harm and can breach the law.

### IR.3 Control principles

1. **P1 Report early:** a suspected incident is reported straight away.
2. **P2 Preserve evidence:** contain the harm, and do not clean up first.
3. **P3 One plan:** everyone follows the same plan, so handling is consistent.
4. **P4 Learn:** each incident improves the plan, training and controls.

### IR.4 Mandatory requirements

1. **R1 Reporting:** everyone must report a suspected incident to the security officer within 1 hour (P-21).
2. **R2 Severity and targets:** the security officer must set each incident's severity, and contain it within the target in \<Incident Response Management\>, section 3.6.
3. **R3 Others told:** the security officer must tell \<Organisation\>'s security contact of every confirmed incident, and any supplier whose product or service is involved.
4. **R4 Personal data breaches:** the legal adviser must tell the ICO within 72 hours of the organisation becoming aware of a reportable breach, and tell the people affected without undue delay when the risk to them is high. Every breach must be recorded, with the reason if it is not reported.
5. **R5 Records:** incidents are tracked and recorded on TPL-10, or in a ServiceNow record that holds the same fields.
6. **R6 Evidence:** evidence must be preserved, hashed and its custody recorded before anything is changed.
7. **R7 Training:** every user must be trained to recognise and report an incident and a personal data breach before access and every 12 months; people with an incident role must be trained within 30 days of taking it, every 12 months, and after a plan change or a system change that alters their part (P-24, P-56).
8. **R8 Testing:** the plan must be tested by tabletop exercise every 12 months, coordinated with the contingency plan.
9. **R9 The plan:** the plan must be approved by the Head of Cyber, reviewed every 12 months and after an incident, and protected from disclosure and change.
10. **R10 Crime:** a suspected crime or significant cyber attack must be reported by the system owner to the NCSC or to Report Fraud, the national police reporting service that replaced Action Fraud.

### IR.5 Responsibilities

**Table IR-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies, and the plan |
| System owner | Owns this policy, decides on recovery, and reports crime |
| Authorising official | Decides on the risk arising from an incident |
| Security officer | Owns and updates the plan, leads incident handling, and keeps the register |
| Legal adviser | Decides on and makes reports to the ICO and to the people affected |
| Windows server and database administrators | Contain, recover and preserve evidence |
| Everyone | Reports suspected incidents at once |
| \<Organisation\> | Receives reports, and helps through its security contact |

### IR.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Approval:** the Head of Cyber approves this policy, as all policies, and the plan; the system owner approves the procedures.
2. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\>, and whenever they change.
3. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how incidents are shared, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Articles 33 and 34, the Data Protection Act 2018 and the Computer Misuse Act 1990; \<Organisation\>'s policies; and CSS.

## MA Maintenance

### MA.1 Purpose and scope

This policy sets the organisation's rules for maintaining \<System Name\>, in line with the CSS MA family (MA-1). It stands alone, as each family has its own policy. The settings, lists and routes that carry it out are in \<Maintenance Management\>, and the steps people follow are in \<Procedures\> (MA).

It applies to the hardware and hypervisor, the two Windows Server 2025 VMs, SQL Server, the UI application, the Admin application and the API, including the diagnostics built into the Admin application. It applies to everyone who maintains them: administrators, developers, \<Organisation\>'s engineers and any supplier.

Maintenance means preventive and corrective work, repair and replacement, done on site or remotely. Fixing flaws (SI-2) and releasing new versions (CM-3) follow their own policies, but use the same change records.

### MA.2 The organisation's position

Maintenance gives people powerful access, often at short notice. \<System Name\> has no page that changes its database's structure or resets its data: such changes come only in a release. Maintenance must still be approved, done by known people with known tools over known routes, checked afterwards and recorded.

### MA.3 Control principles

1. **P1 Approve first:** no maintenance happens without approval.
2. **P2 Known people, tools and routes:** only those on the approved lists are used.
3. **P3 Protect data:** nothing leaves with \<System Name\>'s data on it unless approved and protected.
4. **P4 Check and record:** controls are checked after the work, and every job is recorded and reviewed.

### MA.4 Mandatory requirements

1. **R1 Change record:** all maintenance must be scheduled and approved in a change record before work starts. Emergency maintenance follows the emergency change rule and is recorded within 1 working day.
2. **R2 Records:** every maintenance job must be recorded on TPL-12, with the fields set in \<Maintenance Management\>. The security officer reviews the records every month against the change records.
3. **R3 Check afterwards:** after every job, the administrator must run the checklist in \<Procedures\> (MA), and the security officer must review and sign the result.
4. **R4 Approved tools:** only tools on the approved list in \<Maintenance Management\> may be used. The list is reviewed every 12 months. Tools are inspected before use, and media holding diagnostic or test programs are scanned for malicious code first.
5. **R5 Built-in maintenance functions:** the only maintenance function built into \<System Name\> is the fixed diagnostics page in the Admin application, which reads no item content and is used only by administrators. No page changes the database's structure: structure changes are scripts in a release, applied by the database administrator under an approved change record. No diagnostic or test page is included in a release.
6. **R6 Remote (nonlocal) maintenance:** remote maintenance must use only the routes in \<Maintenance Management\>, with multi-factor sign-in, be logged, and be ended as soon as the work is finished. The Admin application must be reachable only through \<Organisation\>'s managed administration route, and server and database administration only from the administrators' managed devices over that route, with multi-factor authentication, using named accounts (F11).
7. **R7 Maintenance people:** only people on the approved list may maintain \<System Name\> without an escort. They must be screened, have signed Part B of \<Security Operating Procedures\> and use a named account. Supplier accounts are temporary, limited to the job and disabled afterwards. Anyone else must be escorted and supervised by someone on the list.
8. **R8 Equipment removal:** the system owner must approve removing any equipment, and it must be sanitised first.
9. **R9 Data leaving for maintenance or support:** no copy of \<System Name\> data, database backup, log or screenshot may leave the servers for maintenance or support without the system owner's approval. It must be kept to the minimum, encrypted, recorded and deleted when no longer needed.
10. **R10 Timely maintenance:** support and parts for the hardware and hypervisor must be available within 24 hours of a failure. Software must stay on supported versions, with a replacement planned at least 6 months before support ends.
11. **R11 Schedule and notice:** preventive maintenance follows the schedule in \<Procedures\> (MA). Users are given 2 working days' notice of planned maintenance that affects them.
12. **R12 Remote maintenance records:** the events of each remote maintenance connection must be logged and reviewed weekly.

### MA.5 Responsibilities

**Table MA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy; approves the lists of people and tools, equipment removal and any data leaving for support |
| Security officer | Reviews maintenance records monthly and remote maintenance logs weekly; reviews and signs the check after maintenance |
| Windows server administrator | Maintains the VMs, keeps the tool list and runs the check after maintenance |
| Database administrator | Maintains the database, applies structure changes from a release, and runs the check after database maintenance |
| Developers | Maintain the applications through releases only |
| Administrator | Runs the fixed diagnostics in the Admin application (R5) |
| \<Organisation\> | Maintains the hardware and hypervisor, provides support and parts within 24 hours, provides the managed route, and sanitises equipment |

### MA.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who maintains \<System Name\>, and whenever they change.
2. **Coordination:** the system owner agrees with \<Organisation\> how its maintenance, routes and support are carried out and evidenced, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Article 32, and Article 28 where a supplier handles personal data during maintenance or support, and the Computer Misuse Act 1990; \<Organisation\>'s policies; and CSS.

## MP Media Protection

### MP.1 Purpose and scope

This policy sets the organisation's rules for protecting media that hold \<System Name\>'s information, in line with the CSS MP family (MP-1). It stands alone, as each family has its own policy. The media inventory, values and methods that carry it out are in \<Media Protection Management\>, and the steps people follow are in \<Procedures\> (MP).

It applies to every place \<System Name\> information is held outside the running application: the VMs' disks, database and key volumes, export files, application logs, backups, the audit archive, the secret store, support copies, incident evidence, the document set, users' managed devices and approved locations, managed printers, test PCs and paper. It applies to everyone who uses, administers or maintains \<System Name\>, and to \<Organisation\> for the media it handles.

### MP.2 The organisation's position

\<System Name\> has no removable media of its own, but its items leave the application as exports, downloads, backups, logs and printouts. Each copy must be protected as the items themselves are, marked, kept only as long as needed and sanitised when it is no longer needed.

### MP.3 Control principles

1. **P1 Same protection:** every copy gets the protection of the information it holds.
2. **P2 Know where it is:** every place \<System Name\> information is held is listed, and copies are kept only as long as needed.
3. **P3 Marked:** \<System Name\> information is marked \<Classification\> wherever it goes.
4. **P4 Nothing left behind:** media are sanitised, by an approved method, before reuse, release or disposal.

### MP.4 Mandatory requirements

1. **R1 Media inventory:** every place \<System Name\> information is held must be listed in \<Media Protection Management\>, with its protection and sanitising method, and the list reviewed every 12 months.
2. **R2 Access:** digital media may be reached only by the roles named in \<Media Protection Management\>. Only editors of a schema, and administrators, may create exports of it.
3. **R3 Marking:** all \<System Name\> information is marked \<Classification\>, with the item's own classification alongside. \<System Name\> marks printed pages and export files with their classification. No media is exempt.
4. **R4 Storage:** digital media must be stored encrypted in controlled areas: \<Organisation\>'s data centres, or a managed device. Printouts are locked away when not in use.
5. **R5 Export copies:** an export copy on the server must be held in the encrypted working area, and removed once downloaded, and within 24 hours at most (P-20). \<System Name\> deletes it after the download, and a background task removes any left past the limit.
6. **R6 Users' copies:** exports and downloads may be saved only in approved \<Organisation\> locations on a managed device, kept to the minimum, and deleted within 30 days once no longer needed (\<Security Operating Procedures\>, A28 and A30 to A35).
7. **R7 Transport:** media are physically transported only by exception, approved by the system owner, encrypted or sealed, tracked and recorded on TPL-13. Network copies, such as backups to the second site, are protected under SC-8 and CP-6 and must be encrypted first. Printouts do not leave the site without approval.
8. **R8 Sanitising:** media must be sanitised before reuse, release or disposal following CSS and IEEE 2883-2022, using the method set for each media type in \<Media Protection Management\>. Cryptographic erase is used for encrypted virtual disks and backups. Paper is cross-cut shredded to DIN 66399 level P-4 or better.
9. **R9 Records:** each sanitising action is recorded on TPL-13 with the item, method, verification and certificate. The system owner checks a sample of \<Organisation\>'s certificates every 12 months.
10. **R10 Portable storage:** USB and other portable storage are blocked on users' devices unless an exception is approved. No USB device is passed through to the VMs.
11. **R11 Ownerless devices:** portable storage with no identifiable owner must not be used, and must be handed to the security officer.
12. **R12 Support copies:** data sent for maintenance or support follows \<Procedures\>, PRO-MA-7.

### MP.5 Responsibilities

**Table MP-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the media inventory; approves portable storage exceptions and physical transport; checks sanitising certificates |
| Windows server administrator | Protects the VM disks and the export working area, and checks the export working area each working day |
| Database administrator | Protects the database volumes and backups |
| Security officer | Receives ownerless devices and reports media incidents |
| Everyone | Follows the rules for exports, downloads and printouts, and marks and shreds printouts |
| \<Organisation\> | Stores, moves and sanitises physical disks and backup media, manages users' devices and blocks USB |

### MP.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<System Name\>, and whenever they change.
2. **Coordination:** the system owner agrees with \<Organisation\> how it handles media and evidences that, and records it.
3. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR Articles 5(1)(f) and 32 and the Data Protection Act 2018; \<Organisation\>'s policies; and CSS.

## PE Physical and Environmental Protection

### PE.1 Purpose and scope

This policy sets the organisation's rules for the physical and environmental protection of \<System Name\>, in line with the CSS PE family (PE-1). It stands alone, as each family has its own policy. The values, inheritance matrix and site details that carry it out are in \<Physical and Environmental Protection Management\>, and the steps people follow are in \<Procedures\> (PE).

It applies to the data centre that hosts the two VMs, the second site that holds backups and is used for recovery, the offices where \<System Name\> is used and printed, and the homes of people who work remotely.

### PE.2 The organisation's position

\<Organisation\> runs the buildings and data centres, so \<System Name\> inherits most of their protection. The organisation does not run the sites, but it must know that they meet its requirements. It treats each inherited control as not shown until \<Organisation\> has evidenced it, and it protects the parts it does run: screens, printouts and home working.

### PE.3 Control principles

1. **P1 Inherit with evidence:** a physical control counts only once \<Organisation\> has evidenced it.
2. **P2 Same protection everywhere:** the second site meets the same requirements as the main one.
3. **P3 Protect what users see:** screens and printouts are protected by the people who use them.
4. **P4 Report physical events:** physical incidents are handled as security incidents.

### PE.4 Mandatory requirements

1. **R1 Inheritance matrix:** each PE control must be listed in \<Physical and Environmental Protection Management\> with \<Organisation\>'s part, \<System Name\>'s part and the evidence that closes it, and reviewed every 12 months.
2. **R2 Evidence:** \<Organisation\> must evidence the data centres' physical and environmental protection, preferably by its ISO/IEC 27001 certificate, Statement of Applicability and audit findings for Annex A.7, or a SOC 2 report. The system owner reviews it every 12 months and after a change of site.
3. **R3 Requirements:** the data centres must meet the values in \<Physical and Environmental Protection Management\>, including temperature and humidity within the ASHRAE TC 9.9 recommended envelope.
4. **R4 Second site:** the second site must meet the same requirements as the main data centre.
5. **R5 Site inspection:** each data centre, the main site and the second site, is inspected once, at Level 2, by the independent assessor or \<Organisation\>'s auditor using TPL-20, and again after a change of site.
6. **R6 Printing:** \<System Name\> items may be printed only on \<Organisation\>'s managed printers with secure release, and collected at once.
7. **R7 Screens:** screens must be locked when left and placed so that others cannot read them.
8. **R8 Home working:** remote working is allowed only from home, unless the system owner approves another place, on \<Organisation\>'s managed devices and route. \<System Name\> items must not be printed at home unless approved, and must be worked on where others in the home cannot see them.
9. **R9 Physical incidents:** the loss or theft of a device or printout, unauthorised entry to a data centre, and fire, flood or power loss affecting \<System Name\> must be reported to the security officer at once and handled under \<Incident Response Management\>.
10. **R10 Physical access compensation:** VM disks must be encrypted, so that physical access to the hosts does not expose \<System Name\> information.

### PE.5 Responsibilities

**Table PE-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| System owner | Owns this policy and the inheritance matrix; reviews \<Organisation\>'s evidence; approves remote work away from home and printing at home |
| Security officer | Assesses home working controls every 12 months; receives physical incident reports |
| Independent assessor | Completes the site inspection at Level 2 |
| Everyone | Protects screens and printouts, and reports physical incidents |
| \<Organisation\> | Provides and evidences physical and environmental protection at both sites, the managed printers and the managed devices |

### PE.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who uses or administers \<System Name\>, and whenever they change.
2. **Policy review:** every 12 months, and after a significant incident, audit finding or change of site.
3. **Coordination:** the system owner agrees with \<Organisation\> how physical protection is evidenced at both sites, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, including the Regulatory Reform (Fire Safety) Order 2005 and UK GDPR Article 32; \<Organisation\>'s policies; and CSS.

## PL Planning

### PL.1 Purpose and scope

This policy sets the organisation's rules for security and privacy planning for \<System Name\>, in line with the CSS PL family (PL-1). It stands alone, as each family has its own policy. The register of plans and the values that carry it out are in \<Planning Management\>, and the steps people follow are in \<Procedures\> (PL).

It applies to every system plan for \<System Name\>: the System Security Plan, the privacy plan and the supply chain risk management plan, which CSS calls the system plans. It also covers the plans and documents they rely on, the rules of behaviour, the security architecture and the choice and tailoring of the baseline.

### PL.2 The organisation's position

\<System Name\>'s security and privacy are planned and written down before they are relied on. The plans describe what is in place and what is planned, without claiming compliance that has not been shown. Approving a plan does not authorise the system: only the authorising official's decision on TPL-18 does that.

### PL.3 Control principles

1. **P1 One current set:** the SSP is the single statement of how controls are met, and every plan it relies on is listed in one register.
2. **P2 Rules before access:** nobody gets access without signing the rules.
3. **P3 Plans change with the system:** plans change when the system, its risks or an assessment changes, and every review and change is recorded.
4. **P4 Plans are protected:** plans describe weaknesses, carry the set's marking (\<Classification\>) and must be protected like the system itself.

### PL.4 Mandatory requirements

1. **R1 Register of plans:** every plan in force must be listed in \<Planning Management\>, section 3.2, with its owner, version, approver and next review.
2. **R2 Approval:** the System Security Plan must be approved by the system owner, with the Head of Cyber's concurrence, and accepted by the authorising official as an accurate record. The privacy plan must be approved by the legal adviser and the authorising official. The supply chain plan is approved by the system owner.
3. **R3 Review and change records:** each system plan must keep a plan review record (who reviewed, their role, the date, the outcome and actions) separate from its change record. Plans are reviewed every 12 months and after an assessment, significant change or problem found in use.
4. **R4 Sharing:** the SSP and its changes must be shared with the Head of Cyber, administrators and \<Organisation\>'s security contact, and each issue recorded in the plan review record.
5. **R5 Protection:** plans and assessment evidence are marked \<Classification\>. They must be kept in the restricted SharePoint area, never in a code repository or a public location, and only people who need them may read or change them.
6. **R6 Rules of behaviour:** the Security Operating Procedures are the rules of behaviour. Part A applies to everyone, and Part B, the privileged rules, to administrators, auditors, security officers, business owners, the legal adviser's delegate and the Windows server and database administrators as well. Everyone signs before access, and the signature is recorded on TPL-21 and in the register of signatures.
7. **R7 Signing again:** everyone signs again every 12 months, and after a material change to the rules: a new or stricter rule, a changed consequence, new monitoring or a new privileged duty. The system owner decides whether a change is material and records it in the change record of \<Security Operating Procedures\>.
8. **R8 Social media:** \<System Name\> information must not be placed on social media or external sites, and work credentials must not be used on them.
9. **R9 Architecture:** \<System Description\>, section 6, must state the security approach, trust zones, layers of defence, and assumptions and dependencies, and be reviewed every 12 months and after a significant change. Its changes must be reflected in the SSP, the privacy plan, the ConOps, the critical components list and procurement.
10. **R10 Baseline and tailoring:** CSS Moderate, with the privacy baseline, is the baseline. It may be tailored only through \<Tailoring Register\>, with a rationale, a condition and a recorded decision.

### PL.5 Responsibilities

**Table PL-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies, and concurs with the SSP |
| Authorising official | Accepts the SSP as an accurate record, approves the privacy plan, accepts the tailoring register as a record, and makes the authorisation decision |
| System owner | Owns this policy, the plans and the register of plans; keeps the review records, the signed rules and the register of signatures; decides whether a change to the rules is material |
| Legal adviser | Reviews this policy and approves the privacy plan |
| Administrators, auditors, security officers, and Windows server and database administrators | Sign Parts A and B of the rules |
| Everyone | Signs Part A of the rules, and follows them |

### PL.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-PlanConsistency.ps1, and records the result in the plan review record.
3. **Coordination:** the system owner coordinates the plans with the Head of Cyber, administrators, the legal adviser and \<Organisation\>'s security contact.
4. **Laws and standards:** this policy must be consistent with applicable law, including UK GDPR and the Data Protection Act 2018 for the privacy plan; \<Organisation\>'s policies; and CSS.

## PS Personnel Security

### PS.1 Purpose and scope

This policy sets the organisation's rules for personnel security for \<System Name\>, in line with the CSS PS family (PS-1). It stands alone, as each family has its own policy. The designations, screening standard, time limits and register are in \<Personnel Security Management\>, and the steps people follow are in \<Procedures\> (PS).

It applies to everyone who uses, administers or develops \<System Name\>, including external people and \<Organisation\>'s staff who hold a \<System Name\> role.

### PS.2 The organisation's position

\<System Name\> holds Moderate-impact information, including personal data, so the people trusted with it matter as much as its technical controls. \<Organisation\> employs most of them, so its screening, HR and disciplinary processes are used, and it must evidence them. \<System Name\> adds what is specific to it: a risk designation for every role, a minimum it expects of screening, signed agreements, and time limits when people move or leave.

### PS.3 Control principles

1. **Check first:** people are screened and sign their agreements before getting access.
2. **Match the risk:** roles with more power carry a higher risk designation, and more is asked of them.
3. **Act on change:** access follows people's roles when they move or leave, and fastest where the risk is highest.
4. **Hold only what is needed:** \<System Name\> records that a check was passed, never the result of the check.

### PS.4 Mandatory requirements

1. **R1 Risk designations:** every role in \<Roles and Responsibilities\> must have a risk designation in \<Personnel Security Management\>, either higher risk or standard. The designations must be reviewed every 12 months, and when a role's access changes.
2. **R2 Screening before access:** nobody may be given access to \<System Name\> until \<Organisation\> has confirmed that they passed its pre-employment screening. That screening must cover at least identity, the right to work, employment history and a basic criminal record check.
3. **R3 Rescreening:** screening must be confirmed again before someone moves into a higher risk role, and every 5 years for anyone in one.
4. **R4 Screening data:** \<System Name\> must record only that screening was confirmed, by whom and when. Screening results and criminal record data stay with \<Organisation\> and must never be stored in \<System Name\> or its records.
5. **R5 Leavers:** a leaver's Active Directory account is disabled by \<Organisation\> at once, which ends their \<System Name\> access, and their group memberships must be removed within 5 working days (\<System Description\>, P-06). Their credentials must be revoked, any secret they knew must be changed, and the items they managed must stay available.
6. **R6 Higher-risk leavers:** access must be disabled within 1 hour of notice when the person holds a higher risk role, is dismissed, or is suspected of misuse.
7. **R7 Movers:** a mover's access must be reviewed, and the system owner told, within 1 working day.
8. **R8 Access agreements:** everyone must sign \<Organisation\>'s confidentiality agreement and \<Security Operating Procedures\> before access, and sign again every 12 months and after a material change to the rules.
9. **R9 External people:** contracts with external people must state their security duties. Suppliers must report leavers and movers within 1 working day, and their compliance must be checked every 12 months.
10. **R10 Sanctions:** a breach of the rules is handled through \<Organisation\>'s disciplinary process. The system owner must be told within 1 working day of a formal sanction that involves \<System Name\>.
11. **R11 Role descriptions:** the security and privacy duties of every \<System Name\> role must be stated in \<Roles and Responsibilities\>, and \<Organisation\>'s job descriptions must refer to them.
12. **R12 Records and checking:** each of these steps must be recorded on the forms named in \<Procedures\> (PS). Test-PlanConsistency.ps1 must show that every role has a designation, at each review.

### PS.5 Responsibilities

**Table PS-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy; keeps the designations, the personnel security register and the signed agreements; checks screening is confirmed before access; monitors external people |
| Data Owners | Remove a leaver's or mover's memberships of their schema groups within the time limits; the system owner does the same for the role groups. A leaver's access ends within 5 minutes of \<Organisation\> disabling their AD account, because the API checks the account on every request |
| Line managers | Report movers and leavers within 1 working day |
| Legal adviser | Reviews this policy and the laws it names |
| \<Organisation\> | Screens people and holds the results; runs HR and disciplinary processes; holds exit interviews and recovers equipment; disables the network account of a leaver at once; provides job descriptions |

### PS.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\> and every line manager of a \<System Name\> user, and whenever they change.
2. **Coordination:** the system owner agrees with \<Organisation\> how its screening, HR and disciplinary processes are used and evidenced, and records it (EV-PS-01 to EV-PS-03).
3. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS. The laws that bear on it are below. \<Organisation\>, as the employer, carries out the screening and holds its records, so these laws apply to it first. The legal adviser confirms this list at each review of the policy.

**Table PS-2: Laws that bear on personnel security**

| Law | Why it matters here |
| --- | --- |
| UK GDPR, Article 10, and the Data Protection Act 2018, Schedule 1 | Criminal record data may be processed only under these conditions, which is why \<System Name\> holds none (R4) |
| Rehabilitation of Offenders Act 1974 | Limits what may be asked about spent convictions, and so the level of criminal record check |
| Immigration, Asylum and Nationality Act 2006 | The employer's duty to check the right to work |
| Equality Act 2010 | Screening and sanctions must not discriminate |
| Employment Rights Act 1996, and the Acas Code of Practice on disciplinary and grievance procedures | How sanctions and dismissals are handled |

## PT Personally Identifiable Information Processing and Transparency

### PT.1 Purpose and scope

This policy sets the organisation's rules for processing personal data in \<System Name\>, in line with the CSS PT family (PT-1) and UK data protection law. It stands alone, as each family has its own policy. The inventory, retention schedule and values that carry it out are in \<PII Processing Management\>, the impact assessment is \<Data Protection Impact Assessment\>, the privacy plan is \<Privacy Plan\>, and the steps people follow are in \<Procedures\> (PT).

It applies to all personal data in \<System Name\>: the items in every schema, the names held from sign-in, audit records, logs and export copies.

### PT.2 The organisation's position

\<Organisation\> operates in the UK and is the controller of the personal data in \<System Name\>. UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025 apply. \<System Name\> may hold items that contain special category data, as its information types in \<System Description\>, section 3.4, show, so personal data gets the same care as any other information at its classification, and more where the law requires it.

### PT.3 Control principles

1. **P1 Lawful and known purpose:** personal data is processed only for a stated purpose, with a recorded lawful basis and, for special category data, a recorded condition.
2. **P2 Only what is needed, only as long as needed:** \<System Name\> holds no more personal data than the purpose requires, for no longer than the retention schedule allows.
3. **P3 People's rights:** people can see, correct and ask to delete their data, and complain, as the law allows.
4. **P4 Assess before relying on it:** the impact assessment comes before production and before any significant change.

### PT.4 Mandatory requirements

1. **R1 Purposes:** personal data may be processed only for the purposes stated in the application profile (\<System Description\>, section 3) and \<PII Processing Management\>.
2. **R2 Basis and conditions:** each kind of personal data must have an Article 6 lawful basis recorded in \<PII Processing Management\>, section 3.3, confirmed by the legal adviser. Special category data must also have an Article 9 condition and, where needed, a Schedule 1 condition. Where a Schedule 1, Part 1 condition is relied on, an appropriate policy document must be in place. Consent is not used for employee data.
3. **R3 Inventory and record of processing:** \<PII Processing Management\>, section 3.3 must list every kind of personal data, and match \<Organisation\>'s record of processing (UK GDPR, Article 30; EV-PM-02).
4. **R4 Impact assessment:** \<Data Protection Impact Assessment\> must be completed and approved by the legal adviser, with the data protection officer's advice, before production and after any significant change in processing.
5. **R5 Special category data:** special category data may be held only in schemas the business owner authorises, and those items must be marked as such.
6. **R6 Retention:** personal data must be kept only for the period in \<PII Processing Management\>, section 3.7, then disposed of, with the disposal audited.
7. **R7 Rights and complaints:** requests from individuals must go to the legal adviser and be met by a reasonable and proportionate search of every schema, using the search across schemas (FR-073), which only the legal adviser's delegate runs, within one month (P-22). Complaints about how data is handled must be acknowledged within 30 days, investigated, and answered with the outcome.
8. **R8 Transparency:** \<Organisation\>'s employee privacy notice must name \<System Name\> and its purposes, be reviewed every 12 months, and be linked from \<System Name\>'s pages.
9. **R9 Breaches:** personal data breaches must be handled under \<Incident Response Management\>, section 3.8, including the 72-hour report to the ICO, harm to the people affected and the breach register.
10. **R10 Training and test data:** everyone who handles personal data in items and all administrators must complete privacy training before access and every 12 months. Real personal data must not be used for testing, training or research.
11. **R11 Accuracy:** personal data must be kept accurate and up to date. Each schema's personal data must be checked every 12 months, and anything inaccurate or out of date corrected or deleted.

### PT.5 Responsibilities

**Table PT-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Legal adviser | Owns the privacy plan and the impact assessment; confirms each lawful basis and condition and the appropriate policy document; handles requests, complaints and reports to the ICO |
| Data protection officer | Advises on the impact assessment and is the contact for individuals and the ICO, or the legal adviser records why none is required |
| System owner | Owns this policy and the inventory, and makes sure \<System Name\> follows it |
| Information owner | Decides what personal data each schema holds |
| Business owner | Authorises the schemas that may hold special category data, sets retention periods, and approves the disposal of items due under the retention schedule (FR-074) |
| Legal adviser's delegate | Named by the legal adviser; searches every schema for one person's items to answer a request (FR-073), and holds no other role |
| Data Owners | Make sure their schema holds only the personal data it needs |
| \<Organisation\> | Provides the employee privacy notice and the record of processing |

### PT.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\>, and whenever they change.
2. **Policy review:** every 12 months, and after a significant incident, audit finding, change in the law or change in processing.
3. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-PersonalData.ps1 in the test environment, and records the result.
4. **Coordination:** the system owner works with the legal adviser, the data protection officer and \<Organisation\>, and records what is agreed.
5. **Laws and standards:** this policy must be consistent with UK GDPR, the Data Protection Act 2018, the Data (Use and Access) Act 2025, \<Organisation\>'s policies and CSS.

## RA Risk Assessment

### RA.1 Purpose and scope

This policy sets the organisation's rules for understanding and responding to risk in \<System Name\>, in line with the CSS RA family (RA-1). It stands alone, as each family has its own policy. The values that carry it out are in \<Risk Assessment Management\>, the steps people follow are in \<Procedures\> (RA), and the risks themselves are in \<Risk List\>.

It applies to the UI application, the Admin application, the API, the \<System Name\> database, the backups and the two Windows Server 2025 VMs they run on at \<Organisation\>.

### RA.2 The organisation's position

\<System Name\> is not required to meet every control. Every non-compliance is identified and documented, its risk is understood, and a named person decides what happens to it. Finding a non-compliance does not by itself start a fix.

### RA.3 Control principles

1. **Risk-based:** decisions follow the rated risk, assessed by a stated method.
2. **Named decisions:** a named person decides each risk, at the level set for its rating.
3. **Keep looking:** vulnerabilities are looked for continually, not only at assessment.
4. **Exploited first:** a flaw being exploited in the wild is dealt with ahead of everything else.
5. **Know what matters most:** critical components get closest attention.

### RA.4 Mandatory requirements

1. **R1 Risk record:** \<Risk List\> is the record of risk assessment. It must use the method in its section 4, which follows CSS, and give each risk a status and the date it was last reviewed.
2. **R2 Risk review:** the risk assessment must be reviewed every 12 months, and after a significant change, incident or new test result, and shared with the system owner, the authorising official and the Head of Cyber.
3. **R3 Categorisation:** the system must keep a security categorisation under CSS, with its rationale, approved by the authorising official.
4. **R4 Organisational risk:** system risk decisions must respect \<Organisation\>'s risk management strategy and risk appetite.
5. **R5 Supply chain:** supply chain risk from packages, browser libraries, suppliers and the servers must be reviewed every 12 months, and recorded on TPL-23.
6. **R6 Scanning:** vulnerability scans must run as P-30 sets: servers monthly, with credentialed scans of both VMs, and packages and code at each release, with definitions updated before each scan. The packages, the browser libraries, \<System Name\>'s own applications, and both servers' operating system, SQL Server and other installed software must all be covered.
7. **R7 Response times:** each vulnerability must be fixed or mitigated within the time in \<Risk Assessment Management\>, section 3.6, for its severity, counted from the fix's release, or from detection if that is later. Critical and High within 14 days, Medium within 30 days, Low within 90 days (P-11). Severity is the vendor's rating, or else the CVSS base score.
8. **R8 Exploited flaws:** a flaw listed in CISA's Known Exploited Vulnerabilities catalogue, or confirmed by its vendor as exploited, must be fixed or mitigated within 3 days as an emergency change. A fix that cannot meet any time goes to a risk decision under section 1.2.
9. **R9 Reports:** vulnerability reports must be received through \<Organisation\>'s security contact, which must be published with terms that authorise research in good faith, and flaws found in another party's component must be reported to its maintainer.
10. **R10 Critical components:** critical components must be identified by the method in \<Risk Assessment Management\>, section 3.9, and reviewed at each major release and significant change.

### RA.5 Responsibilities

**Table RA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies; confirms the risk thresholds against \<Organisation\>'s risk appetite |
| System owner | Owns this policy and the risk list, decides Low risks, holds the risk and supply chain reviews, and approves critical components |
| Authorising official | Approves the categorisation, and decides Medium and High risks |
| Information owner | Confirms the information types and their impact levels |
| Security officer | Reviews scan results, tracks them to closure, and receives vulnerability reports |
| Windows server administrator | Runs scans of the VMs |
| Developers | Check packages and browser libraries at each release, and fix flaws in \<System Name\>'s code |
| \<Organisation\> | Provides the security contact, and any shared scanning service |

### RA.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Vulnerability.ps1, and records the result.
3. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how inherited protections and vulnerability reports are handled, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies, the Cyber Essentials requirements \<Organisation\> holds, and CSS.

## SA System and Services Acquisition

### SA.1 Purpose and scope

This policy sets the organisation's rules for buying and building \<System Name\>, in line with the CSS SA family (SA-1). It stands alone, as each family has its own policy. The values that carry it out are in \<System and Services Acquisition Management\>, and the steps people follow are in \<Procedures\> (SA).

It applies to \<System Name\>'s in-house development and build environment, and to every product, component and service bought or used from outside, including the source repositories and the in-house package feed.

### SA.2 The organisation's position

\<System Name\> is built in-house, so its developers carry most of these duties. Security and privacy are planned from the start, not added at the end. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SA.3 Control principles

1. **A named framework:** development follows \<Organisation\>'s corporate SDLC, whose security practices meet CSS, practice by practice.
2. **Known changes only:** only reviewed and approved changes reach a release.
3. **Test before release:** every security function is tested at each release, to a stated depth.
4. **Know what you depend on:** every third-party component and external service is known, assessed and supported.

### SA.4 Mandatory requirements

1. **R1 Framework:** \<System Name\> must be developed under \<Organisation\>'s corporate software development life cycle (SDLC), which is inherited and whose security practices meet CSS, with each practice mapped to how it is met in \<System and Services Acquisition Management\>, section 3.2.
2. **R2 Resources:** the system owner must raise security and privacy costs in yearly budgeting, and record them.
3. **R3 Contracts:** contracts must use \<Organisation\>'s standard terms, with security and privacy requirements, documentation, responsibilities and acceptance criteria added.
4. **R4 Design information:** design and the functions, ports, protocols and services \<System Name\> needs must be documented, and kept current with each change.
5. **R5 Documentation:** administrator and user guides covering secure installation, configuration, operation and use must be kept with the code and confirmed at each release.
6. **R6 Principles:** design must follow the NCSC secure design principles and the CSS privacy engineering objectives, as mapped in \<System Description\>, section 6.8.
7. **R7 Change control:** code, configuration and documents must be held in Git, with each default branch protected, at least one approving review before a change merges, dependency alerts on, and release tags signed. Test scripts must be under version control.
8. **R8 Build and test:** each release must pass unit, integration and security tests covering every security function, to the depth in \<System and Services Acquisition Management\>, section 3.9, and to the verification standard in P-28. Builds must not turn package vulnerability checks off.
9. **R9 Third parties:** each new third-party component must be checked for origin, licence, support and known vulnerabilities before it is added. External services, including the source repositories and the sources behind the in-house package feed, must state their controls and be reviewed every 12 months.
10. **R10 Support:** components must be replaced before support ends, with a replacement planned at least 6 months before. Any exception needs the authorising official's approval.

### SA.5 Responsibilities

**Table SA-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Approves exceptions for unsupported components |
| System owner | Owns this policy, raises security costs, controls the repositories' settings, and reviews external services |
| Developers | Follow the framework, review each other's changes, test, fix flaws and keep the guides current |
| Security officer | Checks security at each stage, and reviews the tests and principles at each release |

### SA.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with developers and administrators, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Development.ps1, and records the result.
3. **Coordination:** the system owner agrees contract terms with \<Organisation\>, and records them.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS, and aligns with the UK Software Security Code of Practice.

## SC System and Communications Protection

### SC.1 Purpose and scope

This policy sets the organisation's rules for protecting \<System Name\>'s communications, boundaries, keys and stored information, in line with the CSS SC family (SC-1). It stands alone, as each family has its own policy. The values, cryptographic register and allow-lists that carry it out are in \<System and Communications Protection Management\>, and the steps people follow are in \<Procedures\> (SC).

It applies to the UI application, the Admin application, the API, the \<System Name\> database, their backups and keys, and the two Windows Server 2025 VMs they run on at \<Organisation\>.

### SC.2 The organisation's position

Information in \<System Name\> must be protected wherever it travels or rests. \<System Name\> relies on \<Organisation\>'s network protections, and must also protect itself: its own listening addresses, host firewalls, transport encryption, keys and pages are \<System Name\>'s responsibility. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SC.3 Control principles

1. **Deny by default:** only the agreed flows are allowed, at \<Organisation\>'s firewalls and on each VM.
2. **Encrypt everything that moves:** every flow uses TLS, including those that stay inside a VM.
3. **Know every key:** every key and cryptographic use is recorded, owned, protected and changed on time.
4. **Separate:** administration and the API are kept apart from everyday use.

### SC.4 Mandatory requirements

1. **R1 Flows:** only the flows F1 to F11 in \<System Description\>, section 6.5, as set out in \<System Security Plan\>, section 3.7, Table 7, and \<System Description\>, section 6.5, are allowed. Traffic is denied by default at \<Organisation\>'s firewalls and at each VM's host firewall, using the allow-lists in \<System and Communications Protection Management\>, section 3.2.
2. **R2 Listening addresses:** the UI application listens on TCP 443 only. The Admin application is reachable only over \<Organisation\>'s managed administration route. The API listens only on the application server's loopback address. SQL Server accepts connections on TCP 1433 only from the application server. Only the application server reaches PingFederate, on TCP 443 (F10). Server and database administration reaches both servers only from the administrators' managed devices over the managed administration route (F11).
3. **R3 Transport:** every flow must use TLS under NCSC's profiles. TLS 1.3 is preferred, with hybrid post-quantum key exchange where the platform supports it. TLS 1.2 is allowed only with the GCM profiles. SSL, TLS 1.0 and 1.1, compression and TLS 1.3 early data (0-RTT) must be off.
4. **R4 Web traffic and cookies:** the apps must serve HTTPS only and redirect HTTP, send HSTS with a maximum age of at least 1 year, and mark every cookie Secure, HttpOnly and SameSite. The authentication cookie is \<System Name\>'s session: it has an absolute lifetime of 8 hours with no sliding extension, never longer than PingFederate's sign-in (\<System Description\>, P-02), and holds no groups.
5. **R5 Database:** SQL Server 2022 must accept network connections only over TLS 1.2 or later with strict encryption. The API must connect with Windows authentication under its group managed service account, so no database password exists, and with full certificate and server name checking.
6. **R6 Cryptography:** only the algorithms in the cryptographic register may be used: NCSC's TLS profiles, XTS-AES 256 for disk encryption, AES-256 for backups, SHA-256 for file and release checksums, and HMAC-SHA-256 with a random key of at least 256 bits for the tokens between the applications and for the audit chain. No MD5 or SHA-1 is used for protection, and no cryptography is written in-house. \<System Name\> holds no passwords. Validation of cryptographic modules to a United States standard is not required.
7. **R7 Keys:** every key must be in the register, with an owner, a protected store and a cryptoperiod based on CSS, and be changed as P-10 sets. Keys must never be held in source code, settings files, tickets, chat or documents. Each key is changed at the end of its cryptoperiod, when someone who held it leaves, and at once if it may be compromised. The data protection key rings are protected with Windows DPAPI and are not backed up; if one may be compromised, every key in it is revoked.
8. **R8 Certificates:** certificates are issued under \<Organisation\>'s certificate policy, use ECDSA P-256 or RSA 2048-bit with SHA-256, and are renewed at least 30 days before they expire. Only \<Organisation\>'s approved trust anchors are trusted.
9. **R9 Data at rest:** both VMs must use BitLocker with XTS-AES 256 and the TPM. Backups must be encrypted. Export copies must be held in an encrypted working area and deleted once downloaded (P-20). Recovery keys are held in \<Organisation\>'s protected store and tested every 12 months.
10. **R10 Mobile code:** pages may run only JavaScript and WebAssembly served by \<System Name\> itself. Every script and style, including browser libraries, is packaged with the application; no content delivery service is used. Each app must send a page security policy with no inline scripts, no eval and no outside hosts, that limits where forms may be sent and upgrades insecure requests. Any exception is approved by the system owner and recorded.
11. **R11 Availability and remote access:** each app must limit request rates, on top of \<Organisation\>'s denial-of-service protection. Split tunnelling is not allowed. Outbound traffic from the VMs goes through \<Organisation\>'s authenticated proxy, or is blocked.
12. **R12 Change and checking:** a new flow, port, external service, key or certificate goes through change control and updates the register and allow-lists first. Test-Protection.ps1 is run at each release, after a significant change and at each review.

### SC.5 Responsibilities

**Table SC-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks, and any exception to R3 or R6 |
| System owner | Owns this policy and the cryptographic register; approves new flows and mobile code exceptions; reviews the boundary with \<Organisation\> every 12 months |
| Windows server administrator | Sets TLS, certificates, host firewall rules, BitLocker and key ring protection on the VMs |
| Database administrator | Sets strict TLS encryption in SQL Server, limits connections to the application server, gives the API's managed service account a Windows-authenticated login with rights on the application's database only, and encrypts backups |
| Developers | Build secure cookies and page policies; keep keys out of the code; configure the key rings and rate limits; run Test-Protection.ps1 |
| Security officer | Checks the register and test results at each review |
| \<Organisation\> | Provides firewalls, proxy, DNS, certificates and denial-of-service protection |

### SC.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers or develops \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Protection.ps1 and checks the register, and records the result.
3. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how inherited protections are provided, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS, and follows NCSC's guidance on TLS.

## SI System and Information Integrity

### SI.1 Purpose and scope

This policy sets the organisation's rules for keeping \<System Name\> free of known flaws and malicious code, watching it for misuse, and showing that its software and records have not been changed without authority, in line with the CSS SI family (SI-1). It stands alone, as each family has its own policy. The values, detection use cases and retention table that carry it out are in \<System and Information Integrity Management\>, and the steps people follow are in \<Procedures\> (SI).

It applies to the UI application, the Admin application, the API, the \<System Name\> database, the items and records it holds, and the two Windows Server 2025 VMs they run on at \<Organisation\>.

### SI.2 The organisation's position

\<System Name\> holds Moderate-impact information, including personal data. It must be patched promptly, keep malicious files out, notice misuse quickly, and be able to prove that its software and records are unchanged. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SI.3 Control principles

1. **One timetable:** every flaw is fixed to the same risk-based timetable.
2. **Nothing unchecked comes in:** every input and upload is validated, and every upload is scanned.
3. **Watch and respond:** defined events raise alerts that reach a named person.
4. **Prove integrity:** software and records are checked against a recorded baseline.
5. **Say little in errors:** detail goes only to those who need it.

### SI.4 Mandatory requirements

1. **R1 Flaw remediation:** flaws must be fixed to the one timetable in \<Risk Assessment Management\>, section 3.6: 3 days for a flaw known to be exploited, 14 days for Critical and High, 30 days for Medium, and 90 days for Low (P-11), counted from the fix's release or its detection if later. Updates are tested first and installed through change control.
2. **R2 Update status:** Test-Vulnerability.ps1 must run monthly and at each release, dependency alerts must be on for every repository, and Windows Update status must be reported from both VMs.
3. **R3 Malicious code:** Microsoft Defender must run on both VMs, with real-time protection, daily updates and a weekly full scan. Every upload must be passed to Defender through the Windows Antimalware Scan Interface (AMSI) before it is stored. A flagged file is refused, recorded in the audit trail and reported to the security officer.
4. **R4 Upload checks:** only the file types in P-19 may be uploaded. Each file's type and signature must match its extension, its size must be within the limit for the user's role (P-17), a batch must be within P-18, and its name must not contain a path.
5. **R5 Monitoring:** application, Windows and SQL Server logs must be forwarded to \<Organisation\>'s central logging and reviewed weekly (P-08). The detection use cases in \<System and Information Integrity Management\>, section 3.4, which include the nine events in P-27, must raise alerts to the security officer.
6. **R6 Monitoring people:** users must be monitored only after the legal adviser's opinion, only as far as needed, and with staff told what is monitored and why.
7. **R7 Advisories:** advisories must be received from NCSC (including Early Warning), CISA's Known Exploited Vulnerabilities catalogue (weekly), and the vendors of every component, including Microsoft for Windows Server, .NET and SQL Server, and passed to the people who act on them.
8. **R8 Integrity:** release packages and stored files must be protected with SHA-256 checksums, and audit records with the HMAC-SHA-256 chain, and checked against the recorded baseline at start-up, at each release and monthly (P-29). An unexpected change is handled as an incident.
9. **R9 Input validation:** all API inputs, uploads and search terms must be validated on the server, and database queries must use parameters.
10. **R10 Errors:** users and API callers must receive general error messages. Exception detail goes only to the logs, for administrators and developers.
11. **R11 Retention:** information must be kept and disposed of under \<System Name\>'s retention schedule (\<PII Processing Management\>, section 3.7): audit records for 12 months online and 12 archived (P-07), application logs for 30 days, and export copies deleted once downloaded (P-20).
12. **R12 Checking:** Test-Integrity.ps1 must run at each release, after a significant change and at each review.

### SI.5 Responsibilities

**Table SI-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy and the detection use cases |
| Security officer | Reviews the central logs and alerts, but not the audit log, runs the advisory process, and leads the response to detections |
| Windows server administrator | Patches the VMs, runs Defender and forwards Windows logs |
| Database administrator | Patches SQL Server and forwards its logs |
| Developers | Update packages, build upload scanning, validation and safe errors, and run Test-Integrity.ps1 |
| Legal adviser | Advises on monitoring users and on retention periods |
| \<Organisation\> | Monitors network traffic, provides central logging, and registers \<System Name\>'s addresses with NCSC Early Warning |

### SI.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with everyone who administers or develops \<System Name\>, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-Integrity.ps1, and records the result.
3. **Coordination:** the system owner agrees with \<Organisation\>'s security contact how monitoring, logging and firmware updates are provided, and records it.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS.

## SR Supply Chain Risk Management

### SR.1 Purpose and scope

This policy sets the organisation's rules for managing the risk that \<System Name\> is harmed through what it is built from, where it is hosted, and who supplies it, in line with the CSS SR family (SR-1). It stands alone, as each family has its own policy. The plan, supplier register and values are in \<Supply Chain Risk Management\>, and the steps people follow are in \<Procedures\> (SR).

It applies to the software packages and browser libraries \<System Name\> is built from, the tools that build it, the hosting, network and hardware \<Organisation\> provides, and the services \<System Name\> depends on.

### SR.2 The organisation's position

\<System Name\> is mostly made of other people's code. A compromise of any supplier could reach \<System Name\>, so what comes in is chosen, checked, fixed and watched. Where a rule here is not yet met, the gap is recorded in \<Plan of Action and Milestones\> rather than described as done.

### SR.3 Control principles

1. **Know the supply chain:** every supplier is named, with its criticality.
2. **One way in:** every package comes through one checked source.
3. **Fix and verify:** a release is built from exactly the components recorded for it, and can be shown to be so.
4. **Hear about problems:** suppliers and advisories tell us when something goes wrong.
5. **Nothing left behind:** \<System Name\> data is removed before anything leaves.

### SR.4 Mandatory requirements

1. **R1 Plan and team:** a supply chain plan with a supplier register must be kept in \<Supply Chain Risk Management\> and reviewed every 12 months by the supply chain team: the system owner, the security officer, a developer and \<Organisation\>'s IT service desk.
2. **R2 Tolerance:** no critical component may be used without a known source and a SHA-256 record.
3. **R3 Approved suppliers:** hardware, hosting and services must come from suppliers \<Organisation\> has approved. A new critical supplier must be reviewed before use.
4. **R4 One package source:** every software package, including those pulled in by others, must be restored only from the in-house checked package feed (the offline feed), after the PRO-SR-1 check. nuget.org may be used only as a source of vulnerability data.
5. **R5 Fixed and trusted restores:** every .NET project in the source code must use a lock file in locked mode, and restores must accept only packages signed by trusted signers.
6. **R6 Browser libraries:** every script and style a page loads must be packaged with \<System Name\> and served by it. No page loads anything from another host or a content delivery service.
7. **R7 Monitoring components:** packages and browser libraries must be checked for known flaws monthly and at each release, with NuGet's audit on in every build.
8. **R8 Bill of materials:** each release must have a bill of materials that lists every component with its version, hash and licence.
9. **R9 Inspection:** each release must be inspected against its recorded SHA-256 values before installation, and when tampering is suspected. \<Organisation\> must inspect hardware.
10. **R10 Supplier reviews and notices:** critical suppliers must be reviewed every 12 months on TPL-16. \<Organisation\> must report a compromise to the security officer within 24 hours, and open-source suppliers' advisories must be watched (\<System and Information Integrity Management\>, section 3.3).
11. **R11 Authenticity:** a suspected counterfeit or look-alike component, hardware or software, must be refused and reported to the security officer, \<Organisation\> and, where it applies, the package registry and the NCSC.
12. **R12 Disposal and checking:** components must be disposed of following \<Procedures\>, PRO-MP-3, and Test-SupplyChain.ps1 must run at each release, after a significant change and at each review.

### SR.5 Responsibilities

**Table SR-1: Responsibilities**

| Role | Responsibility |
| --- | --- |
| Head of Cyber | Approves this policy, as all policies |
| Authorising official | Decides Medium and High risks |
| System owner | Owns this policy, the plan and the supplier register, and leads supplier reviews |
| Security officer | Receives notices of compromise and reports of counterfeits, and watches supplier advisories |
| Developers | Check and mirror packages, keep lock files, produce the bill of materials, and run Test-SupplyChain.ps1 |
| \<Organisation\> | Approves suppliers, inspects hardware, trains its buyers, controls equipment under repair and disposes of equipment |

### SR.6 Governance requirements

The rules in section 1.1 apply to this policy. It adds these.

1. **Communication:** this policy and the procedures must be shared with developers and administrators, and whenever they change.
2. **Compliance and management commitment:** the system owner reviews compliance at each review, runs Test-SupplyChain.ps1, and records the result.
3. **Coordination:** the supply chain team coordinates with \<Organisation\>, and records what is agreed.
4. **Laws and standards:** this policy must be consistent with applicable law, \<Organisation\>'s policies and CSS.

