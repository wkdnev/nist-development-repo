# \<System Name\> Tailoring Register

## 1 Purpose

CSS (task S-2) allows a baseline to be tailored to the system, and expects each tailoring choice to have a rationale and an approval. This register holds the case for every control, part or parameter proposed as not applicable. Tailoring is not a way to avoid a control that is merely difficult. Every entry states the condition that makes it valid, and it ends if that condition stops being true. All entries are proposals.

Entries are numbered TR-XX-nn, where XX is the family code. Section 8 lists the controls outside the baseline that the design already meets in part, for every family in one table.

**Table 1: Family coverage**

| Family | Section |
| --- | --- |
| AC Access Control | 2 |
| AT Awareness and Training | None |
| AU Audit and Accountability | None |
| CA Assessment, Authorization, and Monitoring | None |
| CM Configuration Management | None |
| CP Contingency Planning | None |
| IA Identification and Authentication | 3 |
| IR Incident Response | None |
| MA Maintenance | None |
| MP Media Protection | None |
| PE Physical and Environmental Protection | None |
| PL Planning | None |
| PM Program Management | 4 |
| PS Personnel Security | None |
| PT Personally Identifiable Information Processing and Transparency | 5 |
| RA Risk Assessment | None |
| SA System and Services Acquisition | 5 |
| SC System and Communications Protection | 6 |
| SI System and Information Integrity | 7 |
| SR Supply Chain Risk Management | None |

## 2 Access Control (AC)

### 2.1 Tailoring proposals

**Table 2: AC tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-AC-01 | AC-2(2) | Not applicable | Temporary and emergency accounts are prohibited (P-39), and the system cannot expire accounts | Each access review confirms that no such account exists | The system must first be able to disable them automatically |
| TR-AC-02 | AC-2k | Not applicable | Shared and group accounts are prohibited (P-36) | \<System Name\> holds no accounts of its own: every account is a person's own Active Directory account, and there is no built-in or default account | A process for changing shared authenticators is needed |
| TR-AC-03 | AC-8a.01 | Replace the statement with one naming \<Organisation\> | \<System Name\> is not a U.S. Government system, so the statement would be untrue | The notice names \<Organisation\>, and a legal adviser agrees the wording | Applies again if \<System Name\> serves a U.S. Government customer |
| TR-AC-04 | AC-8c | Not applicable | \<System Name\> is not publicly accessible | Items and functions need sign-in, except the list in P-51 | AC-8c applies in full |
| TR-AC-05 | AC-17(4) | Not applicable | CSS defines remote access as access through external networks. Administration is to take place only from inside \<Organisation\>'s network | Administration uses only \<Organisation\>'s managed administration route, for the Admin application (F2) and for server and database administration (F11), and external routes to the VMs' administration ports are blocked (EV-AC-12) | AC-17(4) applies, with defined needs and logging |
| TR-AC-06 | AC-19, AC-19(5) | Not applicable | Phones and tablets are not to be used with \<System Name\> in the first release | \<Organisation\>'s device controls prevent or govern this. \<System Name\> cannot identify a device, so a rule alone is weak evidence (EV-AC-15) | Both apply, with \<Organisation\>'s mobile controls as evidence |
| TR-AC-07 | AC-20(1) | Not applicable | P-48 does not allow external systems to reach or hold \<System Name\> data without the system owner's approval, and none is proposed | No such approval is given | Verification of controls and retained agreements are needed for each approval |
| TR-AC-08 | AC-22 | Not applicable | \<System Name\> holds no public content (P-50) | Items and functions need sign-in, except the list in P-51 | AC-22 applies in full |
| TR-AC-09 | AC-07\_ODP\[05\], \[06\] | Not selected | The account lock is the chosen action, so no delay algorithm or other action is needed | The lock remains in place | Define the value that is then selected |
| TR-AC-10 | AC-20\_ODP\[03\] | Not selected | Terms and conditions are used, not asserted controls | P-48 remains the rule | Define the asserted controls |

### 2.2 Considered and not proposed

These controls may look unnecessary but are not proposed for tailoring, so that their risk stays visible.

**Table 3: AC controls considered and kept**

| Control | Reason it stays |
| --- | --- |
| AC-18, AC-18(1) | \<System Name\> provides no wireless access, but users may reach it over \<Organisation\>'s wireless network, so the control is inherited and needs evidence |
| AC-18(3) | It needs confirming on the built VMs and workstation builds |
| AC-17, AC-17(1) to (3) | Approved users may work remotely through \<Organisation\>'s service |
| AC-20, AC-20(2) | Downloads can reach any device the user has, so the rule and its enforcement remain relevant |
| AC-2(5), AC-11, AC-11(1), AC-12 | \<System Name\> has no session management of its own: no idle lock, idle timeout, session limit or sign-out. The controls are not tailored out but are provided by \<Organisation\> and inherited (\<System Description\>, section 7.3). AC-11 and AC-11(1) come from the screen lock on \<Organisation\>'s managed devices (\<System Description\>, P-03); AC-12 and AC-2(5) come from the sign-in lifetime set in PingFederate (P-02), which the application's authentication cookie never outlasts |

## 3 Identification and Authentication (IA)

IA-5i is covered by TR-AC-02.

**Table 4: IA tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-IA-01 | IA-2(12) | Not applicable | PIV credentials are a US federal scheme, and \<Organisation\> is a UK company | \<Organisation\> does not serve a US federal customer through \<System Name\> | IA-2(12) applies |
| TR-IA-02 | IA-5(2) | Not applicable | \<System Name\> does not use public key sign-in | Users do not sign in to \<System Name\> with a public key: PingFederate decides the factors | IA-5(2) applies. A public key second factor would bring it back |
| TR-IA-03 | IA-8 | Not applicable | Only \<Organisation\>'s staff and contractors hold accounts | Each access review confirms no outside user holds an account | IA-8 applies |
| TR-IA-04 | IA-8(1) | Not applicable | As TR-IA-01 and TR-IA-03 | As TR-IA-03 | IA-8(1) applies |
| TR-IA-05 | IA-8(2) | Not applicable | No external authenticators are accepted | As TR-IA-03 | IA-8(2) applies |
| TR-IA-06 | IA-8(4) | Not applicable | No external identity profiles are used | As TR-IA-03 | IA-8(4) applies |

## 4 Program Management (PM)

TR-PM-01 isn't tailoring in the strict sense, as PM has no controls in the Moderate baseline. It is recorded here so that all 20 families are accounted for. PT also has no controls in that baseline, and is assessed against the privacy baseline instead.

**Table 5: PM proposal**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-PM-01 | The whole PM family | Outside the baseline; not assessed for \<System Name\> | PM controls cover an organisation's whole security programme, not one system, and CSS does not allocate them to a baseline. \<System Name\> still inherits them as common controls (CSS, task P-5), as listed in \<Program Management\>, section 3.3 | The organisation's programme stays with \<Organisation\> and the Head of Cyber, and \<System Name\>'s owner or authorising official doesn't ask for it to be assessed | Assess the PM controls |

### 4.1 PM controls \<System Name\> inherits

The list of PM controls that \<System Name\> inherits, with the provider and the evidence for each, is held in \<Program Management\>, section 3.3. It is not repeated here.

## 5 PT and SA

The PT controls are in the CSS privacy baseline, not Moderate, and are assessed against it.

**Table 6: PT and SA proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-PT-01 | PT-5(2), PT-6, PT-6(1), PT-6(2), PT-7(1), PT-7(2), PT-8 | Not applicable | These rest on US law and federal bodies: the Privacy Act, Federal Register notices, Social Security numbers, the First Amendment and computer matching. \<Organisation\> operates in the UK | \<System Name\> processes no data under those US laws. The legal adviser checks this | Assess those controls |
| TR-SA-01 | SA-4(10) | Not applicable | It requires US government PIV identity products, which \<System Name\> doesn't use | \<System Name\> doesn't use PIV cards | Assess SA-4(10) |

## 6 System and Communications Protection (SC)

No CM control is tailored, and CM-2(7) stays in scope.

**Table 7: SC tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-SC-01 | SC-15 | Not applicable | \<System Name\> has no collaborative computing devices or applications | None is added to the system | SC-15 applies |

## 7 System and Information Integrity (SI)

No RA or CA control is tailored.

**Table 8: SI tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-SI-01 | SI-8, SI-8(2) | Not applicable | \<System Name\> sends and receives no email, so it has no entry or exit point for spam | \<System Name\> does not add email | SI-8 and SI-8(2) apply |

## 8 Controls outside the baseline

CSS does not select the controls in Table 9 at Moderate, so they are not assessed. Each is listed because \<System Name\>'s design already goes some way towards it, so that an assessor or a future application at a higher baseline can see what is in place. Controls CSS does not select and the design does not touch, and withdrawn controls, are not listed.

**Table 9: Controls outside the baseline that the design meets in part**

| Family | Control | What it adds | \<System Name\>'s position |
| --- | --- | --- | --- |
| AU | AU-5(1) Storage Capacity Warning | A warning before audit storage fills | Not required. Done in design: a disk-space alert warns before storage fills (\<Audit and Accountability Management\>, section 3.7) |
| AU | AU-5(2) Real-time Alerts | Alerts at once for defined failures | Not required. The design alerts within 1 hour |
| AU | AU-6(5), AU-6(6) Integrated Analysis; Correlation with Physical Monitoring | Joining audit review with scanning, performance and physical access data | Not required, and not done |
| AU | AU-9(2) Store on Separate Physical Systems | Audit records kept on a different system from the one audited | Not required. Done in part: the newest chain hash is copied daily to a separate store, and the archive is offline |
| AU | AU-9(3) Cryptographic Protection | Cryptography to protect the integrity of audit information | Not required. Done in design: the keyed chain hash (\<Audit and Accountability Management\>, section 3.5) |
| AU | AU-10 Non-repudiation | Proof that a person carried out an action | Not required at Moderate. Records name the person PingFederate authenticated |
| AU | AU-12(1), AU-12(3) System-wide Audit Trail; Changes by Authorised Individuals | One time-ordered trail across components; changing what is logged at run time | Not required. The weekly comparison by time stands in for the first |
| AU | AU-13, AU-14, AU-16 Monitoring for Disclosure; Session Audit; Cross-organisational Logging | Further capabilities | In no baseline. Not done |
| AU | AU-3(3) Limit Personally Identifiable Information Elements | Only the personal data needed in records | In the privacy baseline. Assessed with the PT family; design in \<Audit and Accountability Management\>, section 3.4 |
| CA | CA-2(2) Specialized Assessments | In-depth monitoring, scanning and testing as part of assessment | Not required. Vulnerability scanning is done under RA-5 |
| CA | CA-2(3) Leveraging Results from External Organizations | Accepting another organisation's assessment | Not required. \<Organisation\>'s evidence is examined, not accepted unseen |
| CA | CA-3(6), CA-3(7) Transfer Authorizations; Transitive Information Exchanges | Checks on what the other system may do with the information | Not required, and not done |
| CA | CA-7(3) Trend Analyses | Using trends to adjust monitoring | Not required. Done in part: the monthly analysis looks across three months |
| CA | CA-7(5), CA-7(6) Consistency Analysis; Automation Support | Further assurance and automation of monitoring | Not required, and not done |
| CA | CA-8 Penetration Testing | Penetration testing of the system | Selected only at High, so not required. One is commissioned anyway, before go-live: by a tester independent of the build, on the servers, covering the two user-facing applications, the API and sign-in through PingFederate, with each finding rated in the Risk List. Tester: \[Name\] |
| CA | CA-9(1) Compliance Checks | Security checks on a component before it connects | Not required, and not done |
| CM | CM-3(1) Automated Documentation, Notification, and Prohibition of Changes | A workflow that records each change, tells the approvers, and blocks a change until approved | Not required. Done in part by the ServiceNow workflow |
| CM | CM-3(6) Cryptography Management | Cryptographic mechanisms under configuration management | Not required. Keys and certificates are in the key register (\<System and Communications Protection Management\>, section 3.4), and a new key or certificate goes through change control |
| CM | CM-4(1) Separate Test Environments | Changes analysed in a separate test environment | Not required. Done: \<Configuration Management\>, appendix A |
| CM | CM-5(1) Automated Access Enforcement and Audit Records | Automated enforcement of who may change the system, with audit records | Not required. Done in part: Windows and database permissions enforce it, and their logs record it |
| CM | CM-6(1), CM-6(2) Automated Management and Verification; Respond to Unauthorized Changes | Automated checking of settings, and a set response to an unauthorised change | Not required. Done in part in design: the monthly benchmark scan, and the drift procedure |
| CM | CM-7(4) Unauthorized Software, Deny-by-exception | A list of software that must not run | Not required. \<System Name\> uses the stricter alternative, CM-7(5), an approved list, though it is not enforced by the system |
| CM | CM-8(2), CM-8(4) Automated Maintenance; Accountability Information | An inventory kept by automated means, naming who is accountable for each component | Not required. Each entry names an owner. The bill of materials will keep the software list by automated means |
| CM | CM-13 Data Action Mapping | A map of what the system does with personal data | In no security baseline. The personal data inventory is in \<PII Processing Management\>, section 3.3 |
| CM | CM-14 Signed Components | Components installed only if signed with an approved certificate | In no baseline. Release tags are to be signed, and packages checked for their signature |
| CP | CP-2(2) Capacity Planning | Capacity planned for processing, telecommunications and support during a contingency | Not required. The second site is asked to run both servers at their normal size (EV-CP-01) |
| CP | CP-2(5) Continue Mission and Business Functions | Functions continue with little or no loss of continuity | Not required. Availability is rated Low, and 72 hours to recover is enough |
| CP | CP-3(1) Simulated Events | Training that simulates a real event | Not required. The tabletop exercise walks through a scenario |
| CP | CP-4(2) Alternate Processing Site | Testing the plan at the second site | Not required, and not planned. The first restore test is on the main servers |
| CP | CP-6(2) Recovery Time and Recovery Point Objectives | The storage site set up to meet the recovery objectives | Not required. Done in design: transaction log backups go to the second site between the daily backups |
| CP | CP-7(4) Preparation for Use | The second site kept ready to use | Not required. The servers are rebuilt there when needed |
| CP | CP-8(3), CP-8(4) Separation of Providers; Provider Contingency Plan | Alternate services from a separate provider, who has a contingency plan | Not required. \<Organisation\>'s plans are asked for with EV-CP-01 |
| CP | CP-9(2), CP-9(3), CP-9(5) Test Restoration Using Sampling; Separate Storage for Critical Information; Transfer to Alternate Storage Site | Further assurance for backups | Not required. Done in design: every restore test restores the whole database; one copy is offline or immutable; backups and transaction log backups go to the second site |
| CP | CP-10(4) Restore Within Time Period | Components restored from configuration-controlled images within a set time | Not required. Done in design: the servers are rebuilt from the baseline and the tagged release (\<Configuration Management\>, section 3.4) |
| IA | IA-2(5) Individual Authentication with Group Authentication | A person signs in as themselves before using a shared account | Not required. There are no shared accounts |
| IA | IA-2(6) Access to Accounts, Separate Device | The second factor is on a device separate from the one signing in | Not required. Set by \<Organisation\>'s PingFederate, and asked with EV-IA-04 |
| IA | IA-5(7) No Embedded Unencrypted Static Authenticators | No passwords or keys left in code, scripts or settings | Not required. Done in design: the token signing key and the audit chain key are held in the key store, outside the source repositories and settings files, and the API has no database password (\<Identification and Authentication Management\>, section 3.5) |
| IA | IA-5(13) Expiration of Cached Authenticators | Cached sign-in details expire | Not required. \<System Name\> caches no authenticators: it holds the sign-in only in its authentication cookie, for no longer than PingFederate's sign-in lifetime (P-02) |
| IA | IA-9 Service Identification and Authentication | Services prove who they are to each other | In no baseline. Done in design: the UI application and the Admin application to the API with a signed token; the API to the database and to Active Directory with its managed service account; and the applications' check of PingFederate's signed response (\<Identification and Authentication Management\>, section 3.2) |
| IA | IA-10 Adaptive Authentication | Extra checks when a sign-in looks unusual | In no baseline. A matter for \<Organisation\>'s PingFederate |
| IA | IA-12(4) In-person Validation and Verification | Identity evidence checked in person | Selected only at High. \<Organisation\>'s HR is asked how it checks (EV-IA-02) |
| IA | IA-13 Identity Providers and Authorization Servers | Controls on the service that vouches for users, and on checking its tokens | In no baseline. It bears directly on \<System Name\>, which relies on PingFederate. Section 3.3 sets what \<System Name\> checks in a sign-in response |
| IR | IR-2(1), IR-2(2) Simulated Events; Automated Training Environments | Training that simulates an incident, in an automated environment | Not required. The tabletop exercise walks through a playbook |
| IR | IR-2(3) Breach | Training on finding, handling and reporting a personal data breach | Privacy baseline, so it applies. Covered by modules M7 and M9, and assessed with the PT family |
| IR | IR-3(1), IR-3(3) Automated Testing; Continuous Improvement | Automated tests of the capability, and measures used to improve it | Not required. Done in part: the measures in \<Incident Response Management\>, section 3.12 and each after-action report feed the plan |
| IR | IR-4(2), IR-4(3), IR-4(5), IR-4(9) Dynamic Reconfiguration; Continuity of Operations; Automatic Disabling of System; Dynamic Response Capability | The system changes itself, or is shut down, in response to an incident | Not required. Nothing is automatic: people decide, to the targets in \<Incident Response Management\>, section 3.6 |
| IR | IR-4(4) Information Correlation | Incident information correlated across the organisation | Not required. Done in part: the monthly review reads the incident records with the audit findings and the vulnerability results (\<Procedures\>, PRO-CA-5) |
| IR | IR-4(6), IR-4(7) Insider Threats | A capability for incidents caused by insiders, coordinated across the organisation | Not required. Done in part: the playbook for bulk export or download misuse, and \<Organisation\>'s disciplinary process |
| IR | IR-4(8), IR-4(10) Correlation with External Organizations; Supply Chain Coordination | Handling coordinated with outside bodies and suppliers | Not required. Reports to suppliers are covered by IR-6(3) |
| IR | IR-4(11) Integrated Incident Response Team | A team that can be sent out within a set time | Not required. The roles in \<Incident Response Management\>, section 3.3 are a small named team |
| IR | IR-4(12), IR-4(13) Malicious Code and Forensic Analysis; Behavior Analysis | Analysis of malicious code and of attackers' behaviour | Not required. Any such work would be done by \<Organisation\> or an outside firm (\<Incident Response Management\>, section 3.12) |
| IR | IR-4(14) Security Operations Center | A security operations centre | Not required. \<Organisation\> is asked what monitoring it provides (EV-IR-01) |
| IR | IR-4(15) Public Relations and Reputation Repair | Managing public relations after an incident | Not required. Section 3.13 says who may speak to the press and the public |
| IR | IR-5(1) Automated Tracking, Data Collection, and Analysis | Incidents tracked and analysed automatically | Not required. ServiceNow gives part of it |
| IR | IR-6(2) Vulnerabilities Related to Incidents | Weaknesses found through incidents are reported | Not required. Done in design: closing an incident updates the Risk List and the POA&M (PRO-IR-7) |
| IR | IR-7(2) Coordination with External Providers | A working relationship with outside providers of protection | Not required. \<Organisation\> is the only provider (\<Incident Response Management\>, section 3.15) |
| IR | IR-8(1) Breaches | The plan covers personal data breaches: whether to notify, the harm to people, and the law that applies | Privacy baseline, so it applies. Met by \<Incident Response Management\>, section 3.8, and assessed with the PT family |
| IR | IR-9, IR-9(2), IR-9(3), IR-9(4) Information Spillage Response | Handling information that reaches a system or person not cleared for it | Not required. Done in part: the playbook for an item in the wrong place (\<Incident Response Management\>, section 3.9) |
| MA | MA-2(2) Automated Maintenance Activities | Maintenance scheduled, done and recorded by automated means | Not required. The maintenance record is a form |
| MA | MA-3(4), MA-3(5) Restricted Tool Use; Execution with Privilege | Tools limited to authorised people, and their privileged use monitored | Not required. Done in part: each tool in \<Maintenance Management\>, section 3.5 is tied to a role, and the diagnostics page is limited to administrators |
| MA | MA-3(6) Software Updates and Patches | Maintenance tools kept up to date | Not required. Done in part: the Windows and SQL Server tools are updated with the servers |
| MA | MA-4(1) Logging and Review | Remote maintenance sessions logged, and the logs reviewed | Not required. Done in design: \<Maintenance Management\>, section 3.4 says what each session logs, and the security officer reviews the logs weekly |
| MA | MA-4(3) Comparable Security and Sanitization | Remote maintenance done only from a system as secure as the one maintained | Not required. Administrators use \<Organisation\>'s managed devices and route (EV-MA-02) |
| MA | MA-4(4) Authentication and Separation of Maintenance Sessions | Maintenance sessions kept apart from other network sessions | Not required. Done in part: the servers are administered through a management interface on \<Organisation\>'s managed route |
| MA | MA-4(5) Approvals and Notifications | Each remote session approved by named people, who are told when it is planned | Not required. Done in design: the system owner approves remote work in the change record |
| MA | MA-4(6), MA-4(7) Cryptographic Protection; Disconnect Verification | Remote sessions encrypted, and their end verified | Not required. Done in part: the VPN and TLS protect the session. The end of a session is not verified separately |
| MA | MA-5(1) Individuals Without Appropriate Access | Rules for maintenance people who lack the access authorisations | Not required. Done in part: they are escorted and supervised, have a temporary account, and have no access to \<System Name\>'s data |
| MA | MA-5(2), MA-5(3), MA-5(4) Security Clearances; Citizenship; Foreign Nationals | Clearance and nationality rules for classified systems | Not required. \<System Name\> holds no classified information |
| MA | MA-5(5) Non-system Maintenance | Rules for people who maintain the building and its services near the system | Not required. \<Organisation\> controls its data centres (\<Physical and Environmental Protection Management\>) |
| MA | MA-6(1), MA-6(2), MA-6(3) Preventive Maintenance; Predictive Maintenance; Automated Support for Predictive Maintenance | Maintenance done before a failure, by schedule or by prediction | Not required. Done in design for preventive work: the schedule in \<Procedures\>, PRO-MA-6. Nothing is predictive |
| MA | MA-7 Field Maintenance | Limits on maintenance done away from a trusted facility | Not required. The servers stay at \<Organisation\>'s data centres |
| MP | MP-4(2) Automated Restricted Access | Access to media storage areas restricted and logged by automated means | Not required. \<Organisation\> is asked how access to its data centres is controlled (\<Physical and Environmental Protection Management\>) |
| MP | MP-5(3) Custodians | A named custodian for media in transport | Not required. Done in part: the system owner approves each move, and an authorised courier carries it with tracking |
| MP | MP-6(1) Review, Approve, Track, Document, and Verify | Sanitising and disposal reviewed, approved, tracked, documented and verified | Not required. Done in part: each action is recorded on TPL-13 with its verification, and the system owner checks a sample of certificates every 12 months |
| MP | MP-6(2) Equipment Testing | Sanitising equipment and procedures tested on a schedule | Not required. \<Organisation\> is asked how each action is verified (EV-MP-02) |
| MP | MP-6(3) Nondestructive Techniques | Portable storage sanitised before it is first connected | Not required. Portable storage is blocked, and an exception uses only encrypted media issued by \<Organisation\> |
| MP | MP-6(8) Remote Purging or Wiping of Information | Devices purged or wiped from a distance | Not required. Done in part: \<Organisation\> can lock or wipe a lost managed device (\<Incident Response Management\>, section 3.9) |
| MP | MP-7(2) Prohibit Use of Sanitization-resistant Media | Media that cannot be sanitised are not used | Not required. Every kind of media in \<Media Protection Management\>, section 3.2 has a method in \<Media Protection Management\>, section 3.6 |
| MP | MP-8, MP-8(1) to MP-8(4) Media Downgrading | A process for lowering the classification of media | Not required. No media is downgraded: everything stays marked \<Classification\> until sanitised |
| PE | PE-2(1), PE-2(2), PE-2(3) Access by Position or Role; Two Forms of Identification; Restrict Unescorted Access | Tighter rules for who may enter | Not required. No \<System Name\> role enters a data centre |
| PE | PE-3(1) System Access | Entry to the room holding the system controlled separately from entry to the building | Not required. \<Organisation\>'s evidence may show it (A.7.1, A.7.2) |
| PE | PE-3(2), PE-3(3), PE-3(4), PE-3(5), PE-3(7), PE-3(8) Facility and Systems; Continuous Guards; Lockable Casings; Tamper Protection; Physical Barriers; Access Control Vestibules | Further physical barriers and checks | Not required. Done in part in design: the server disks are encrypted, so that reaching a host does not expose the items (\<Physical and Environmental Protection Management\>, section 3.8) |
| PE | PE-5(2) Link to Individual Identity | Output released only to the person who asked for it | Not required. Done in design: managed printers with secure release (\<Physical and Environmental Protection Management\>, section 3.5) |
| PE | PE-6(2), PE-6(3), PE-6(4) Automated Intrusion Recognition and Responses; Video Surveillance; Monitoring Physical Access to Systems | More monitoring, some of it automated | Not required. CCTV is already required under PE-6(1) |
| PE | PE-8(3) Limit Personally Identifiable Information Elements | Visitor records hold only defined personal data | Privacy baseline, so it applies. The data allowed is the name, the organisation, and the date and time of the visit. Assessed with the PT family (EV-PT-02) |
| PE | PE-11(1), PE-11(2) Alternate Power Supply | Long-term backup power that keeps the system running | Not required. Availability is rated Low, and an orderly shutdown is enough. \<Organisation\> is asked how long its backup power lasts (EV-PE-02) |
| PE | PE-13(2), PE-13(4) Suppression Systems, Automatic Activation and Notification; Inspections | Fire suppression that works and notifies automatically, and fire inspections | Not required. \<Organisation\>'s evidence may show them (A.7.5) |
| PE | PE-14(1), PE-14(2) Automatic Controls; Monitoring with Alarms and Notifications | Environmental levels controlled automatically, with alarms | Not required. Done in part in design: the levels are monitored continuously |
| PE | PE-18 Location of System Components | Components placed to limit damage from hazards and from unauthorised access | Not required. The second site is asked not to share the main site's hazards (\<Contingency Planning Management\>, section 3.9) |
| PL | PL-7 Concept of Operations | A concept of operations that says how the organisation means to operate the system, reviewed on a schedule | Not required. Done: \<Concept of Operations\> is in the register of plans, and is reviewed every 12 months |
| PL | PL-8(1) Defense in Depth | Controls placed in layers, so that one failure does not expose the system | Not required. Done in design: the layers of defence in \<System Description\>, section 6.8 |
| PL | PL-9 Central Management | Defined controls and processes managed centrally | Privacy baseline, so it applies. The whole document set is managed as one, by one owner, with one consistency test. Assessed with the PT family |
| PS | PS-3(1), PS-3(2), PS-6(2) Classified Information; Formal Indoctrination; Classified Information Requiring Special Protection | Clearance, briefing and agreements for access to classified information | Not required. \<System Name\> holds no classified information |
| PS | PS-3(3) Information Requiring Special Protective Measures | Extra screening for access to information that needs special protection | Not required. Items that hold special category data are protected by limiting each schema to the people its Data Owner authorises, not by further screening |
| PS | PS-3(4) Citizenship Requirements | Citizenship checks for defined roles | Not required. The right to work check covers lawful employment in the United Kingdom |
| PS | PS-4(1), PS-6(3) Post-employment Requirements | People are told of, and bound by, duties that continue after they leave | Not required. Done in part: the exit interview covers continuing confidentiality duties. Whether \<Organisation\>'s confidentiality agreement continues after employment is asked with EV-PS-02 |
| PS | PS-4(2) Automated Actions | Automated notice of a leaver, and automated disabling of access | In the High baseline only. Done in design: disabling the Active Directory account ends access to \<System Name\> at once, and \<Organisation\>'s starters and leavers process prompts the group owners through ServiceNow |
| PT | PT-2(1), PT-3(1), SI-18(2) Data Tagging; Data Tags | Tags on personal data that carry its permitted processing, purposes or quality | Not required. Done in part in design: items that hold special category data are marked as such (\<PII Processing Management\>, section 3.4) |
| PT | PT-2(2), PT-3(2), SI-18(1) Automation; Automation Support | Processing limits and quality checks enforced by automated means | Not required. Schema access limits who processes each schema's items |
| PT | PT-4(1), PT-4(2), PT-4(3) Tailored Consent; Just-in-time Consent; Revocation | Ways to give, refine and withdraw consent | Not required. Consent is not the lawful basis (\<PII Processing Management\>, section 3.2) |
| PT | PT-5(1) Just-in-time Notice | Notice given at the moment data is collected | Not required. Done in part in design: the short statement on \<System Name\>'s pages (\<PII Processing Management\>, section 3.5) |
| PT | SI-18(3) Collection | Personal data collected directly from the person where possible | Not required. The business teams that own each schema collect the data; \<System Name\> stores the items |
| PT | SI-18(5) Notice of Correction or Deletion | People to whom data was disclosed are told of a correction or deletion | Not required. Done in design: the legal adviser tells them, as UK GDPR Article 19 requires (\<PII Processing Management\>, section 3.6) |
| PT | SI-19(1) to SI-19(8) | Ways of de-identifying data | Not applicable. No dataset is de-identified (SI-19) |
| RA | RA-2(1) Impact-level Prioritization | Ranks systems within one impact level | Not required. \<System Name\> is one system |
| RA | RA-3(2) Use of All-source Intelligence | Draws on all sources of threat intelligence | Not required. \<Organisation\>'s threat awareness programme (PM-16) and the advisory sources in \<System and Information Integrity Management\>, section 3.3, feed the risk assessment |
| RA | RA-3(3) Dynamic Threat Awareness | Assesses the current threat continuously | Not required. Done in part: CISA's exploited list and \<Organisation\>'s alerts are checked weekly (PRO-RA-4) |
| RA | RA-5(3) Breadth and Depth of Coverage | Defines how widely and deeply scans look | Not required. Done in part in design: \<Risk Assessment Management\>, section 3.5 says which components are checked, how and how often |
| RA | RA-5(4) Discoverable Information | Finds what an adversary could learn about the system, and acts on it | Not required: selected at High only. The penetration test before go-live looks for it |
| RA | RA-5(6) Automated Trend Analyses | Compares scan results over time automatically | Not required. Done in part by hand: the monthly monitoring analysis looks for a trend over three months (\<Assessment, Authorization, and Monitoring Management\>, section 3.8) |
| RA | RA-6 Technical Surveillance Countermeasures Survey | Surveys premises for eavesdropping devices | Not required. \<System Name\> has no premises of its own |
| RA | RA-8 Privacy Impact Assessments | Assesses the effect on people's privacy | In the CSS privacy baseline. Designed and assessed with the personal data controls in \<PII Processing Management\> |
| RA | RA-10 Threat Hunting | Searches actively for threats that have evaded other controls | Not required. Any threat hunting is \<Organisation\>'s security operations |
| SA | SA-3(1) Manage Preproduction Environment | Protects the development and test environments | Not required. Done in part: the test environment is a separate throwaway copy of the system |
| SA | SA-3(2) Use of Live or Operational Data | Limits the use of real data in development and testing | Not required. Done in design: the test and development environments hold invented data only (\<PII Processing Management\>) |
| SA | SA-3(3) Technology Refresh | Plans the replacement of technology | Not required. Done in part: replacements are planned 6 months before support ends (\<System and Services Acquisition Management\>, section 3.12) |
| SA | SA-4(3) Development Methods, Techniques, and Practices | Requires a stated development method | Not required. Done in design: CSS \<ver\> (\<System and Services Acquisition Management\>, section 3.2) |
| SA | SA-4(8) Continuous Monitoring Plan for Controls | Requires the developer to plan monitoring of the controls | Not required. The monitoring plan is in \<Assessment, Authorization, and Monitoring Management\>, section 3.8 |
| SA | SA-4(12) Data Ownership | States that the organisation owns its data | Not required. \<Organisation\> owns the data \<System Name\> holds |
| SA | SA-8(1) to SA-8(32) | Individual security engineering principles | Not required. The NCSC secure design principles cover the same ground (\<System and Services Acquisition Management\>, section 3.6) |
| SA | SA-8(33) Minimization | The privacy principle of minimisation | In the CSS privacy baseline. Designed and assessed in \<PII Processing Management\> |
| SA | SA-9(1) Risk Assessments and Organizational Approvals | Assesses risk and approves before an external service is used | Not required. Done in part: a new supplier or component is reviewed before use (PRO-RA-2, PRO-SA-7) |
| SA | SA-9(3) to SA-9(8) | Trust relationships, consistent interests, location, the organisation's own keys and integrity checks, and United States jurisdiction | Not required. Done in part: each external service's basis of trust is recorded (\<System and Services Acquisition Management\>, section 3.7) |
| SA | SA-10(1) to SA-10(7) | Integrity checks, trusted generation and distribution, and other forms of developer configuration management | Not required. Done in part in design: signed tags and release checksums |
| SA | SA-11(1) to SA-11(9) | Static and dynamic analysis, threat modelling, code review, penetration testing and other developer tests | Not required. Done in part in design: the kinds of analysis in \<System and Services Acquisition Management\>, section 3.9 |
| SA | SA-15 enhancements other than SA-15(3) | Quality metrics, tracking tools, attack surface reduction, continuous improvement, automated analysis and others | Not required. Done in part: the yearly process review (PRO-SA-6) |
| SA | SA-16 Developer-provided Training | Training from the developer on the controls | Not required: selected at High only. Administrators' training is in \<Awareness and Training Management\> |
| SA | SA-17 Developer Security and Privacy Architecture and Design | A formal security architecture from the developer | Not required: selected at High only. Done in part: \<System Description\>, section 6 |
| SA | SA-20 Customized Development of Critical Components | Builds critical components in-house | Not required. \<System Name\>'s own applications are written in-house |
| SA | SA-21 Developer Screening | Screens the developers | Not required: selected at High only. Developers are screened as their risk designation requires (\<Personnel Security Management\>) |
| SC | SC-7(10) Prevent Exfiltration | Stops data leaving by unauthorised routes | Not required. Done in part: outbound traffic only through \<Organisation\>'s proxy (\<System and Communications Protection Management\>, section 3.2) |
| SC | SC-7(12) Host-based Protection | A firewall on each host | Not required. Done in design: each server's host firewall (\<System and Communications Protection Management\>, section 3.2) |
| SC | SC-7(18) Fail Secure | The boundary fails closed | Not required. Done in design: deny by default |
| SC | SC-7(21) Isolation of System Components | Separates components by boundary | Not required. Done in design: separate application and database servers |
| SC | SC-12(1) to SC-12(3) | Key availability and symmetric and asymmetric key production | Not required. Keys are recorded with their store and owner (\<System and Communications Protection Management\>, section 3.4) |
| SC | SC-23(1), SC-23(3), SC-23(5) | Invalidate session identifiers at sign-out, unique identifiers, allowed certificate authorities | Not required. \<System Name\> has no session identifiers of its own. Done in design: only PingFederate's signed response is accepted, and the sign-in is held only in the protected authentication cookie, whose lifetime is no longer than PingFederate's (\<System and Communications Protection Management\>, section 3.3) |
| SC | SC-28(2), SC-28(3) | Offline storage of information at rest; protected key storage | Not required. Done in part: encrypted backups with the key held apart (K10) |
| SC | SC-45 System Time Synchronization | Synchronises clocks with an authoritative source | Not selected at Moderate in the SC family. Done in design: \<Organisation\>'s time service (rule O1; \<Audit and Accountability Management\>) |
| SI | SI-2(5), SI-2(6) | Automatic updates; removing previous versions after an update | Not required. Done in part: updates go through change control (\<System and Information Integrity Management\>, section 3.3) |
| SI | SI-4(1), SI-4(10), SI-4(11) | System-wide intrusion detection; visibility of encrypted traffic; analysis of outbound traffic | Not required. Done in part: \<Organisation\>'s network monitoring (\<System and Information Integrity Management\>, section 3.4) |
| SI | SI-4(12), SI-4(14), SI-4(20) | Automated organisation alerts; wireless intrusion detection; privileged user monitoring | Not required: selected at High only, or not applicable. Done in part: use cases U4 and U6 watch privileged changes and administrator sign-ins |
| SI | SI-4(22), SI-4(23) | Unauthorised network services; host-based monitoring | Not required. Done in part: Defender on both servers |
| SI | SI-6 Security and Privacy Function Verification | Checks that security functions work | Not required: selected at High only. Done in part: the test scripts (\<System and Services Acquisition Management\>, section 3.9) |
| SI | SI-7(2), SI-7(5), SI-7(15) | Automated notification and response to integrity failures; code authentication | Not required: selected at High only. Done in part: signed release tags |
| SI | SI-10(3) Predictable Behavior | Behaves predictably on invalid input | Not required. Done in design: invalid input is refused |
| SR | SR-3(1) to SR-3(3) | Diverse supply base; limiting harm; flowing controls down to sub-tier suppliers | Not required. Done in part: the risk tolerance limits harm (\<Supply Chain Risk Management\>, section 3.6) |
| SR | SR-4 Provenance | Records where each component came from and every change to it | Not required. Done in part in design: the in-house package feed's SHA-256 records and the bill of materials |
| SR | SR-5(1), SR-5(2) | Adequate supply; assessments before selection | Not required. Done in part: the PRO-SR-1 check before a component is used |
| SR | SR-6(1) Testing and Analysis | Tests what suppliers provide | Not required. Done in part: release inspection (\<Supply Chain Risk Management\>, section 3.8) |
| SR | SR-7 Supply Chain Operations Security | Hides supply chain information from adversaries | Not required. The plan and the register are restricted |
| SR | SR-9 Tamper Resistance and Detection | Resists and detects tampering | Not required: selected at High only. Done in part: SHA-256 checks of each release |

Notes by family:

- **IR:** Two are in the CSS privacy baseline and apply because \<System Name\> holds personal data: they are assessed with the PT family.
- **PE:** One is in the CSS privacy baseline and applies because visitor records hold personal data: it is assessed with the PT family.
- **PL:** One is in the CSS privacy baseline, and is assessed with the PT family.
- **PT:** The United States privacy controls that the baseline does select are tailored out in \<PII Processing Management\>, section 3.2.
- **SC:** SC-15 is tailored out (TR-SC-01), and SC-7(24) is a privacy baseline control set out in \<PII Processing Management\>.
- **SI:** SI-8 and SI-8(2) are tailored out (TR-SI-01), and SI-12(1) to SI-12(3), SI-18, SI-18(4) and SI-19 are privacy baseline controls set out in \<PII Processing Management\>.
