# \<System Name\> Review Guide

This guide lists the 44 documents in the set and suggests the order in which to review them. Start with the [Guide to the Document Set](Guide%20to%20the%20Document%20Set.md), which shows how the documents relate and gives a route through them, and the [System Description](System%20Description.md), which describes the whole system in one place. It is a working aid for reviewers. It is not a controlled document, and nothing else in the set depends on it.

Written on 12 November 2026, against the set as it stood that day.

## 1 The short version

1. **Read four short documents first** to learn the system: about one hour.
2. **Review the plan's front half**, then the two documents that set its scope.
3. **Review the rules one family at a time**, reading the same family in three documents side by side.
4. **Review the five standalone plans** and the day-to-day rules.
5. **Review the assessment and its results** last, because they judge everything before them.
6. **Use the registers as reference.** Look things up in them; do not read them end to end.

The whole set is about 286,000 words. A reviewer who follows this path reads about 105,000 of them closely and samples the rest.

## 2 What a reviewer does not need to check

A script, `tests\Test-PlanConsistency.ps1`, checks 24 things every time the set changes, and all 24 pass. So a reviewer can leave these to it and spend their time on substance:

- that every link, section reference and table reference leads somewhere that exists;
- that the totals in the plan and the report match the assessment;
- that every risk entry, fix and decision a document names exists;
- that version numbers quoted in one document match the document they quote;
- that Table 8 of the plan matches its control rows.

What only a person can judge:

- **Is it true?** Does the document describe \<System Name\> and \<Organisation\> as they really are?
- **Is it workable?** Could the named person carry out the step, in the time given, with the record named?
- **Is it complete?** Is anything a reviewer would expect missing?
- **Is it clear?** Would a new reader understand it?

## 3 The suggested order

Each stage builds on the one before. The size column is a rough count of words, to help plan the time.

### Stage 1: Learn the system

Read these straight through. They are short, and everything else assumes them.

| Order | Document | Size | Why now | Look for |
| --- | --- | --- | --- | --- |
| 1 | [Documentation Map](Documentation%20Map.md), sections 1 to 3 | 2,500 of 5,500 | It lists every document and says where each family's material is | Whether the set looks complete for what you expect |
| 2 | [Concept of Operations](Concept%20of%20Operations.md) | 2,700 | Why \<System Name\> exists, who uses it and how | Whether the business picture is right. Several business facts are still placeholders |
| 3 | [Security Architecture](Security%20Architecture.md) | 3,400 | The boundary, the components and the eight data flows | Whether the boundary and flows match what will be built |
| 4 | [Roles and Responsibilities](Roles%20and%20Responsibilities.md) | 2,500 | Every other document names roles, and this one names the people | Whether each holder is right, and the two deputies still to be named |

### Stage 2: The plan and its scope

| Order | Document | Size | Why now | Look for |
| --- | --- | --- | --- | --- |
| 5 | [System Security Plan](System%20Security%20Plan.md), sections 1 to 6 | 6,000 of 20,400 | The central document. These sections describe the system, its information, its laws and who is responsible | Categorisation, the inventory, the laws table and the six figures. Leave section 7 for stage 5 |
| 6 | [Tailoring Register](Tailoring%20Register.md) | 2,800 | It says which controls do not apply, and why. That sets the scope of everything after | Whether each "not applicable" is justified, and the condition that must stay true |

### Stage 3: The rules, one family at a time

This is the largest stage. Three documents hold the rules, and each has one chapter for each control family:

- [Policy](Policy.md): what must be true (24,000 words, 19 chapters);
- [Procedures](Procedures.md): who does what, and the record kept (22,100 words, 139 procedures);
- [Control Implementation Register](Control%20Implementation%20Register.md): now an index only (3,800 words). Every family's design is in a document of its own, and each chapter points to it.

For Access Control, read [Access Control Management](Access%20Control%20Management.md) (23,600 words) in place of the Register chapter. It is the only place the access control design is held: the model, the settings, the status of all 39 AC controls, how the system is built today and the parameter values.

For Awareness and Training, read [Awareness and Training Management](Awareness%20and%20Training%20Management.md) (6,700 words) in the same way. It holds the briefing, the role curriculum, the training matrix and the training register.

For Audit and Accountability, read [Audit and Accountability Management](Audit%20and%20Accountability%20Management.md) (13,500 words) in the same way. It holds the events logged, what a record holds, how records are protected and kept, and how they are reviewed.

For Assessment, Authorization, and Monitoring, read [Assessment, Authorization, and Monitoring Management](Assessment,%20Authorization,%20and%20Monitoring%20Management.md) (9,100 words) in the same way. It holds the assessment and authorisation process, the inherited controls, the interface record and the monitoring strategy.

For Identification and Authentication, read [Identification and Authentication Management](Identification%20and%20Authentication%20Management.md) (11,300 words) in the same way. It holds sign-in through AD FS, the assurance levels and the authenticator inventory.

For Maintenance, read [Maintenance Management](Maintenance%20Management.md) (7,700 words) in the same way. It holds the remote maintenance routes and the lists of approved tools and people.

For Media Protection, read [Media Protection Management](Media%20Protection%20Management.md) (6,500 words) in the same way. It holds the media inventory, the marking scheme and the sanitising methods.

For Physical and Environmental Protection, read [Physical and Environmental Protection Management](Physical%20and%20Environmental%20Protection%20Management.md) (9,300 words) in the same way. It holds the sites and the inheritance matrix.

For Planning, read [Planning Management](Planning%20Management.md) (6,800 words) in the same way. It holds the register of plans in force and the register of signatures.

For Program Management, read [Program Management](Program%20Management.md) (4,700 words). It is shorter than the others, because these controls are \<Organisation\>'s to provide: it shows who provides each, and what \<System Name\> adds.

For Personnel Security, read [Personnel Security Management](Personnel%20Security%20Management.md) (7,300 words) in the same way. It holds the risk designations, the screening standard and the personnel security register.

For personal data, read [PII Processing Management](PII%20Processing%20Management.md) (10,400 words) in the same way, with the Privacy Plan and the Data Protection Impact Assessment beside it. It holds the personal data inventory and the retention schedule.

For risk assessment, read [Risk Assessment Management](Risk%20Assessment%20Management.md) (9,600 words) in the same way, with the Risk List beside it. It holds the vulnerability timetable, what is monitored and the critical components.

For system and services acquisition, read [System and Services Acquisition Management](System%20and%20Services%20Acquisition%20Management.md) (10,800 words) in the same way. It holds the development framework, the external services and the developer test plan.

For system and communications protection, read [System and Communications Protection Management](System%20and%20Communications%20Protection%20Management.md) (10,600 words) in the same way. It holds the allow-lists, the TLS profile, the key register and the page policy.

For system and information integrity, read [System and Information Integrity Management](System%20and%20Information%20Integrity%20Management.md) (8,600 words) in the same way. It holds the upload checks, the detection use cases and the integrity baseline.

For supply chain risk management, read [Supply Chain Risk Management](Supply%20Chain%20Risk%20Management.md) (7,400 words) in the same way. Its section 3 is the supply chain plan, with the supplier register.

**Review them across, not down.** For each family, read its Policy chapter, then its Procedures chapter, then its Register chapter. That way a rule, the steps that carry it out and the values they use are all in mind at once, and gaps between them show. Reading one whole document and then the next loses that.

A good order for the families puts the ones others depend on first:

| Group | Families | Why together |
| --- | --- | --- |
| A | PL Planning, PS Personnel Security, AT Awareness and Training | People and plans. Short, and they introduce the rules of behaviour and the training everyone else relies on |
| B | AC Access Control, IA Identification and Authentication, AU Audit and Accountability | Who can get in, how they prove who they are, and what is recorded. AC is the largest chapter in every document |
| C | CM Configuration Management, MA Maintenance, SA System and Services Acquisition, SR Supply Chain Risk Management | How \<System Name\> is built, changed and supplied |
| D | SC System and Communications Protection, SI System and Information Integrity, RA Risk Assessment | Technical protection, flaws and risk |
| E | IR Incident Response, CP Contingency Planning | What happens when something goes wrong |
| F | MP Media Protection, PE Physical and Environmental Protection | Mostly provided by \<Organisation\> |
| G | PT Personally Identifiable Information Processing and Transparency | Personal data. Best reviewed with the legal adviser |
| H | CA Assessment, Authorization, and Monitoring | How the set itself is assessed and kept current. Easier once the rest is known |

Then the two documents people will actually hold in their hands:

| Order | Document | Size | Why now | Look for |
| --- | --- | --- | --- | --- |
| 7 | [Security Operating Procedures](Security%20Operating%20Procedures.md) | 9,300 | The rules everyone signs, and the security duties of each role | Whether a user could follow Part A, and whether each duty in Part C has an owner and a record |
| 8 | [Record Templates](Record%20Templates.md) | 5,700 | The 24 forms the procedures call for | Whether each form captures what its procedure needs. Skim it; check a form when a procedure names it |

### Stage 4: The standalone plans

Each is short and can go to a different reviewer. Review each straight after its family in stage 3 if that is easier.

| Order | Document | Size | Goes with | Look for |
| --- | --- | --- | --- | --- |
| 9 | [Configuration Management](Configuration%20Management.md) | 14,500 | CM | Baselines, the change route and the settings for each layer |
| 10 | [Incident Response Management](Incident%20Response%20Management.md) | 10,000 | IR | Severity targets, playbooks, and the contacts still to be filled in |
| 11 | [Contingency Planning Management](Contingency%20Planning%20Management.md) | 12,700 | CP | Recovery times against the business need, and who invokes the plan |
| 12 | [Supply Chain Risk Management](Supply%20Chain%20Risk%20Management.md) | 7,400 | SR | The supply chain plan, the supplier register and each SR control |
| 13 | [Privacy Plan](Privacy%20Plan.md) | 1,400 | PT | Whether it matches how personal data will really be handled |
| 14 | [Data Protection Impact Assessment](Data%20Protection%20Impact%20Assessment.md) | 2,400 | PT | A draft for the legal adviser to complete. Most of its placeholders are theirs |

### Stage 5: The assessment and its results

Review these after the rules, because each one judges or acts on what came before. Start with the summary and work down into detail only where it matters.

| Order | Document | Size | Why now | Look for |
| --- | --- | --- | --- | --- |
| 15 | [Security Assessment Report](Security%20Assessment%20Report.md) | 4,500 | The results of all 19 families in a few pages | Whether the conclusion is fair, and the conditions before authorisation |
| 16 | [System Security Plan](System%20Security%20Plan.md), section 7 | 14,500 | One line for each of the 316 controls | Sample it. Take five controls you know well and check the line is true |
| 17 | [Control Assessment Record](Control%20Assessment%20Record.md) | 79,800 | The finding behind every line: 1,998 statements | Do not read it through. For each family, read the summary and the result table, then sample ten findings |
| 18 | [Risk List](Risk%20List.md), sections 1 to 4 | 4,000 of 16,500 | The 24 risks, how they are rated and who may accept them | Whether the ratings are right. Section 5 is reference |
| 19 | [Plan of Action and Milestones](Plan%20of%20Action%20and%20Milestones.md) | 20,000 | The 94 fixes, and the road to authorisation in section 5 | Owners, effort and order. The milestone dates are still to be set |

### Stage 6: Reference documents

Look things up in these. Reading them end to end is poor use of a reviewer's time.

| Document | Size | Use it to |
| --- | --- | --- |
| [Decision Register](Decision%20Register.md) | 27,100 | Check who decided something and when. Each approver should review only the decisions in their own name, against their sign-off sheet |
| [Evidence Requests](Evidence%20Requests.md) | 7,900 | See what \<Organisation\> is asked for. \<Organisation\> should review this one in full |
| [Interview Guide](Interview%20Guide.md) | 12,700 | Prepare the Level 2 interviews. The security assessor should review it |
| [Risk List](Risk%20List.md), section 5 | 12,500 | Find the entry for one control that is not met |

### Stage 7: The guides

| Order | Document | Size | Why last | Look for |
| --- | --- | --- | --- | --- |
| 20 | [Administrator Guide](Administrator%20Guide.md) | 2,200 | A draft, written from the documents and not yet checked against the code | The developers should confirm every step |
| 21 | [User Guide](User%20Guide.md) | 1,100 | The same | The same |

## 4 Who should review what

One person need not review everything. Splitting by role is faster, and puts each document in front of the person who can judge it.

| Reviewer | Review in full | Sample or skim |
| --- | --- | --- |
| System owner | Stages 1 and 2, Security Operating Procedures, Plan of Action and Milestones | Everything else |
| Head of Cyber | Policy, Incident Response Management | System Security Plan, Risk List |
| Authorising official | Security Assessment Report, Risk List sections 1 to 4, System Security Plan sections 1 to 6 | Plan of Action and Milestones, Contingency Planning Management |
| Legal adviser | Privacy Plan, Data Protection Impact Assessment, the PT chapter of Policy, Procedures and the Register | The laws table in the System Security Plan, and the monitoring rules in Security Operating Procedures |
| Business and information owner | Concept of Operations, the retention schedule in the Register (section PT.4) | Contingency Planning Management, for the recovery times |
| Developers | Security Architecture, Access Control Management, Administrator Guide, User Guide, the CM, SA, SC and SI chapters of the Register | Plan of Action and Milestones, for the fixes that are theirs |
| Security officer | Incident Response Management, Security Operating Procedures Part C, the AU, IR and SI chapters of Procedures | Record Templates |
| \<Organisation\>'s security contact | Evidence Requests | The inherited controls in the Register (section CA.7) |
| Security assessor | Control Assessment Record, Interview Guide, Security Assessment Report | System Security Plan section 7 |

## 5 Three shorter paths

Not every review needs the whole set.

| If the reviewer has | Read |
| --- | --- |
| One hour | Security Assessment Report, then System Security Plan sections 1 to 3 |
| Half a day | Stage 1, System Security Plan sections 1 to 6, Security Assessment Report, Risk List sections 1 to 4, and the road to authorisation in Plan of Action and Milestones section 5 |
| One family to review | That family's chapter in Policy, Procedures and the Register, then its section in the System Security Plan (7.1 to 7.19), its chapter in the Control Assessment Record, and its part of Risk List section 5. Table 2 of the Documentation Map lists all of these for each family |

## 6 Handling review comments

1. Give each comment the document name, the section or table number, and what should change. Section and table numbers are stable within a version.
2. Change one document at a time, and say what changed.
3. After any change, run `tools\issue.py`. It gives the changed document a new version, brings every reference and total that depends on it up to date, and rebuilds the map. `tools\README.md` explains how.
4. Run the consistency test. If all 24 checks pass, the change has not broken anything elsewhere.

Changes made in this order cause the least rework: stages 1 and 2 first, then the rules, then the assessment. A change to a rule can change a finding, so settle the rules before reviewing the findings that judge them.
