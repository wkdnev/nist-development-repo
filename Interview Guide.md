# \<System Name\> Interview Guide

## 1 Purpose

CSS uses three assessment methods: examine, test and interview. These questions cover the interview method. At Level 1 the system owner may answer them. At Level 2 the assessor asks them of the role holders named in \<Roles and Responsibilities\>. Ask each person how the control works in practice and to show a record. An answer alone is not evidence that a control operates.

After each interview, record it in section 2 and update the matching statements in \<Control Assessment Record\>, section AC.3, or the equivalent for the family.

Questions are numbered INT-XX-nn, where XX is the family code, and each names the statements it supports. The people to interview come from the Interview objects in CSS.

**Table 1: Family coverage**

| Family | Section |
| --- | --- |
| AC Access Control | 3 |
| AT Awareness and Training | 4 |
| AU Audit and Accountability | 5 |
| CA Assessment, Authorization and Monitoring | 6 |
| CM Configuration Management | 7 |
| CP Contingency Planning | 8 |
| IA Identification and Authentication | 9 |
| IR Incident Response | 10 |
| MA Maintenance | 11 |
| MP Media Protection | 12 |
| PE Physical and Environmental Protection | 13 |
| PL Planning | 14 |
| PM Program Management | 15 |
| PS Personnel Security | 16 |
| PT Personally Identifiable Information | 17 |
| RA Risk Assessment | 18 |
| SA System and Services Acquisition | 19 |
| SC System and Communications Protection | 20 |
| SI System and Information Integrity | 21 |
| SR Supply Chain Risk Management | 22 |

## 2 Interview log

**Table 2: Interview log**

| Date | Family | Person and role | Interviewer | Questions covered | Records seen | Notes reference |
| --- | --- | --- | --- | --- | --- | --- |
| \[Date\] | \[Family\] | \[Name\], \[Role\] | \[Name\] | \[INT-XX-nn to nn\] | \[Records seen\] | \[Notes reference\] |

## 3 Access Control (AC)

### 3.1 System owner

**Table 3: Questions for the system owner**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-01 | Who approved the policy and procedures, and how were they shared? | AC-01a, AC-01b | Approval and distribution record |
| INT-AC-02 | When were they last reviewed, and what would trigger another review? | AC-01c | Review record, change record |
| INT-AC-03 | How do you decide who holds privileged roles? | AC-02e, AC-06(05) | The ServiceNow requests (TPL-2) for the five role groups |
| INT-AC-04 | How are duties separated, and where does staffing prevent it? | AC-05a, AC-05b | Roles document, risk acceptance |
| INT-AC-05 | How do you decide whether a non-compliance is accepted or remediated? | All; PRO-AC-17 | Decision register, TPL-1 records |
| INT-AC-06 | What is allowed on external systems and portable storage? | AC-20, AC-20(02) | P-48, any approvals |
| INT-AC-43 | Ask the Head of Cyber: how do you review the role-group memberships the system owner holds, and check the administrators' group, each quarter? | AC-05b, AC-06(07) | TPL-3 with the Head of Cyber's sign-off |
| INT-AC-45 | Show me the last 6-monthly review of the Windows administrator accounts, SQL Server logins and service accounts. What was removed? | AC-02j, AC-06(07) | TPL-3 signed by the system owner and security officer; the exports in EV-AC-02 |

### 3.2 Administrators

**Table 4: Questions for administrators**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-07 | Take me through creating a schema in the Admin application and naming its Active Directory read and edit groups. What do you need before you start, and who owns the two groups? | AC-02c, AC-02e, AC-02f | A recent change record (TPL-6) approved by the Data Owner, and its audit entry |
| INT-AC-08 | How do you learn that someone has left or moved, and how quickly are their Active Directory account and group memberships changed? | AC-02h, AC-02l, AC-02(03) | Recent notice and the change it caused |
| INT-AC-09 | What would you do if told someone is a high risk, right now? | AC-02(13) | PRO-AC-4, last walk-through |
| INT-AC-10 | How are inactive Active Directory accounts and unused group memberships found? | AC-02(03)(d) | PRO-AC-8 records |
| INT-AC-11 | Do you use your administrator account for everyday item work? | AC-06(02) | Your two accounts |
| INT-AC-12 | Who checks your own actions? | AC-05b, AC-06(09) | Auditor's review record |

### 3.3 Data Owners

**Table 5: Questions for Data Owners**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-13 | How do you decide who may read or edit your schema, and how do you authorise a request in ServiceNow? | AC-02i, AC-03 | TPL-2 records and ServiceNow approvals |
| INT-AC-14 | When did you last review the members of your schema's read and edit groups, and what changed? | AC-02j, AC-06(07) | TPL-3 record |
| INT-AC-15 | How do you decide whether an item can be shared with people outside the schema's groups? | AC-21a, AC-21b | TPL-25 sharing decision record |
| INT-AC-40 | When were you last asked to approve a change to which groups open your schema, or to deactivate it? What did you check before approving? | AC-03, AC-05b | The change record (TPL-6), the audit entry carrying its reference, and the U9 alert it raised |

### 3.4 Auditors and security officers

**Table 6: Questions for auditors and security officers**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-16 | How do you monitor account use, and how often? Auditors review the audit log weekly; security officers review alerts and the central logs, and do not read the audit log | AC-02g | The auditor's weekly review record; the security officer's TPL-8 review record |
| INT-AC-17 | Which privileged actions do you look for, and what would you do on finding a problem? An auditor reports anything suspicious to the security officer | AC-06(09) | Review record, escalation |
| INT-AC-18 | Are there actions you cannot see in the audit log or the central logs? | AC-02(04), AC-06(09) | Known gaps |
| INT-AC-41 | Auditors: how do you check and sign the system owner's role-group review, and how do you review SQL Server Audit's record of item reads by logins other than the API's? | AC-06(07), AC-06(09) | Signed TPL-3; the weekly review record (TPL-8) covering SQL Server Audit in central logging |
| INT-AC-42 | Security officers: show me the monthly last sign-in report. How did the groups' owners remove members who had not signed in for 90 days? | AC-02(03)(d) | The report (FR-085) and its audit entry; TPL-3 with the removals |

### 3.5 Windows server and database administrators

**Table 7: Questions for Windows server and database administrators**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-19 | Who has administrator rights on each VM and in the database? | AC-06(01), AC-06(05) | Group and role listings |
| INT-AC-20 | What rights do the group managed service accounts of the three applications have, on the server, in SQL Server and in Active Directory? | AC-06 | Service account settings, SQL Server logins and database role grants |
| INT-AC-21 | From where, and how, do you administer the VMs? When may you do it from outside the office (P-54)? | AC-17, AC-17(04) | Administration route (flow F11 in \<System Description\>, section 6.5); firewall rules |
| INT-AC-22 | What are the logon lockout, banner and screen lock settings? | AC-07, AC-08, AC-11 | Policy export |
| INT-AC-23 | How are your privileged actions logged? | AC-06(09) | Sample log |
| INT-AC-44 | When did you last do privileged work from outside the office? Show me the reason and the record of the session | AC-17(04)(a), AC-17(04)(b) | The change or incident record; the VPN and administration route connection logs; the Windows, SQL Server or audit log entries |

### 3.6 Developers

**Table 8: Questions for developers**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-24 | How do you make sure a new page or API function needs the right access? | AC-03, AC-06(10) | Code review practice, test checks |
| INT-AC-25 | Do you have any access to production? | AC-05a, AC-06 | The server and database account review (TPL-3, P-52) |
| INT-AC-26 | How are diagnostic and test pages kept out of a release? | AC-06(10), AC-14 | Build settings |

### 3.7 \<Organisation\> security contact

**Table 9: Questions for \<Organisation\>'s security contact**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-27 | Does the Cyber Essentials Plus scope include these VMs and their hosting? | Inherited controls | EV-GEN-02 |
| INT-AC-28 | Who controls firewalls, and how are rule changes approved? | AC-04 | EV-AC-03 |
| INT-AC-29 | How do people reach internal systems remotely, and how is that monitored? | AC-17, AC-17(01) to (03) | EV-AC-08 to EV-AC-11 |
| INT-AC-30 | How are wireless, mobile devices and USB storage controlled? | AC-18, AC-19, AC-20(02) | EV-AC-13 to EV-AC-17 |
| INT-AC-31 | How do leavers and movers reach the system owner and the Data Owners, and how quickly is a leaver's Active Directory account disabled? | AC-02h, AC-02l | EV-AC-01 |

### 3.8 Sample users

**Table 10: Questions for sample users**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-32 | Have you read the rules of behaviour, and did you sign them? | AC-01a, AC-02c | Signed acknowledgement |
| INT-AC-33 | What do you do if you can see an item you should not? | AC-03 | None |
| INT-AC-34 | Do you use \<System Name\> from a phone, or a personal device, or copy items to USB? | AC-19, AC-20 | None |
| INT-AC-39 | When do you sign out of \<System Name\>, and what happens if you leave it open all day? | AC-02(05), AC-12 | Sign-out entries in the audit log; the cookie and re-check settings (P-02, NFR-102) |

### 3.9 Business owner

**Table 11: Questions for the business owner**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-35 | How were you given the business owner role, who owns the \<Code\>\_BusinessOwners group, and what else can you do in \<System Name\>? | AC-02c, AC-02e, AC-06 | TPL-2 record; the group's members |
| INT-AC-36 | Show me how you approve the disposal of items due under the retention schedule (\<System Description\>, FR-074). What stops anyone else approving it? | AC-03, AC-05b, AC-06 | A disposal approval and its audit entry |

### 3.10 Legal adviser's delegate

**Table 12: Questions for the legal adviser's delegate**

| ID | Question | Statements | Ask to see |
| --- | --- | --- | --- |
| INT-AC-37 | Who named you to the \<Code\>\_LegalSearch group, and do you hold any other role in \<System Name\>? | AC-02e, AC-05b, AC-06 | The legal adviser's naming in a TPL-2 record; the group's members |
| INT-AC-38 | When did you last search every schema for one person's items (\<System Description\>, FR-073)? Who asked, and how did you keep the search to that request? | AC-03, AC-06 | TPL-15 request record; the search's audit entry |

## 4 Awareness and Training (AT)

**Table 13: AT questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-AT-01 | System owner | How do you know each user completed training before getting access? | AT-02, AT-04 | TPL-9 records |
| INT-AT-02 | Security officer | What role training has been given, and how is its content kept up to date? | AT-03, AT-04 | \<Awareness and Training Management\> (role curriculum and training matrix), module content and TPL-9 records |
| INT-AT-03 | A sample of users | How would you recognise and report social engineering or an insider threat? | AT-02(02), AT-02(03) | The \<System Name\> briefing scenarios (\<Awareness and Training Management\>, section 3.3) |
| INT-AT-04 | Security officer | How do you know the training works, and what changed after the last incident or review? | AT-01, AT-02, AT-03 | Training measures on TPL-8 (\<Awareness and Training Management\>, section 3.9) |
| INT-AT-05 | One holder of each role in the training matrix | Which modules did you take before you were given your role, and what did they teach you to do differently? | AT-03, AT-03(05) | The person's TPL-9 records and the register |
| INT-AT-06 | A line manager | What do you check before you approve an access request, and what would make you raise a concern about someone in your team? | AT-02, AT-02(02) | Briefing part B7 and the manager's TPL-9 record |

## 5 Audit and Accountability (AU)

**Table 14: AU questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-AU-01 | System owner | How do you decide which events are logged, and why are they enough? | AU-02d, AU-12b | \<Audit and Accountability Management\>, review record |
| INT-AU-02 | Auditor | Show me your last weekly review. What did you find, and whom did you tell? | AU-06a, AU-06b | Review record |
| INT-AU-03 | Auditor | How do you know the audit records have not been changed or removed? | AU-09a, AU-09b | Chain check result |
| INT-AU-04 | Windows server administrator | What happens when logging fails? Who is told, and how quickly? | AU-05 | An alert and its response |
| INT-AU-05 | Database administrator | How long are records kept, and how is capacity checked? | AU-04, AU-11 | Capacity record, backup |
| INT-AU-06 | \<Organisation\>'s security contact | Is there central monitoring, and which time source do the VMs use? | AU-06(01), AU-06(03), AU-08 | EV-AU-01, EV-AU-02 |
| INT-AU-07 | Security officer | How do you know what the auditor read or exported, and who would see it if they misused the log? | AU-06a, AU-09(04) | Central logging view of the audit-read security events |

## 6 Assessment, Authorization and Monitoring (CA)

**Table 15: CA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-CA-01 | Security assessor | Have you had any part in designing, building, running or administering \<System Name\>, or do you report to anyone responsible for it? | CA-02(01), CA-07(01) | TPL-19 independence statement |
| INT-CA-02 | Authorising official | What did you rely on to authorise \<System Name\>, and which risks did you accept? | CA-06c | TPL-18 authorisation decision, and \<Security Assessment Report\> |
| INT-CA-03 | System owner | How is the plan kept up to date, and when did it last change? | CA-05b | \<Plan of Action and Milestones\> history |
| INT-CA-04 | Security officer | Show me the last monitoring report on TPL-8, and any measure past its threshold. Who received it? | CA-07 | Monitoring report |
| INT-CA-05 | System owner | Which of \<Organisation\>'s services does \<System Name\> connect to, and how do you know no other system connects to it? | CA-03, CA-09 | Interface record; the flows in \<System Description\>, section 6.5 |
| INT-CA-06 | Authorising official | Which assessment plan did you approve, and when, against the date the assessment started? Whose independence statements did you accept? | CA-02c, CA-02(01) | The approved plan in \<Control Assessment Record\>; TPL-19 with your acceptance |
| INT-CA-07 | \<Organisation\>'s common control official | Have you authorised the controls \<System Name\> inherits, and how would you tell it if one changed? | CA-06b, CA-06d | EV-CA-01 authorisation record |
| INT-CA-08 | System owner | Show me the last change you judged significant, and what the authorising official decided | CA-06e, CA-07 | TPL-6 with the significant change decision |
| INT-CA-09 | Legal adviser | How do you learn the privacy status of \<System Name\>, and when did you last receive it? | CA-07g | TPL-8 privacy measures sent to you |

## 7 Configuration Management (CM)

**Table 16: CM questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-CM-01 | System owner | How is a change approved, who reviews it, and how are records kept? | CM-03, CM-04 | A ServiceNow change record |
| INT-CM-02 | Developers | How is a release tested and verified before it goes live? | CM-03(02), CM-04(02) | A release test record |
| INT-CM-03 | Windows server administrator | What is the baseline for each VM, and which secure settings are applied? | CM-02, CM-06 | Baseline, CIS Benchmark result |
| INT-CM-04 | Windows server administrator | Who can make changes to the VMs, and how is that restricted? | CM-05 | Access list, EV-CM-01 |
| INT-CM-05 | Developers | Which functions have been removed or turned off, and when was that last reviewed? | CM-07, CM-07(01) | Functions review record |
| INT-CM-06 | Windows server administrator | How is software approved and installed, how is the list kept up to date, and how does App Control stop anything else running? | CM-07(02), CM-07(05), CM-11 | Approved software list, an approval, the App Control policy and its blocked events |
| INT-CM-07 | Windows server administrator | How is the inventory kept accurate, and when was it last reviewed? | CM-08, CM-08(01) | Inventory, the last baseline review |
| INT-CM-08 | \<Organisation\>'s security contact | How are unauthorised components found, how are licences tracked, how are the VMs hardened, and what happens to a laptop taken to a high-risk location? | CM-02(07), CM-06, CM-08(03), CM-10, CM-12(01) | EV-CM-02 to EV-CM-05 |
| INT-CM-09 | Security officer | How do you analyse a change's impact, and how do you hear about drift? | CM-04, CM-06d | A TPL-6 impact analysis, a TPL-8 drift report |
| INT-CM-10 | Legal adviser | Which changes do you see as the board's privacy representative, and what did you decide on the last one? | CM-03(04), CM-04\[02\] | A TPL-6 for a change touching personal data |
| INT-CM-11 | System owner | Where is \<System Name\>'s information held, who has access to it, and when did you last approve the configuration management plan? | CM-09, CM-12 | TPL-5, \<Configuration Management\> approval |

## 8 Contingency Planning (CP)

**Table 17: CP questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-CP-01 | System owner | When would you invoke the plan, who would you tell, and from when is the 72 hours counted? | CP-02, CP-02(03) | \<Contingency Planning Management\>, sections 3.3 and 3.5; the activity log of the last exercise |
| INT-CP-02 | Database administrator | How are backups taken, encrypted and sent to the second site, where is the backup encryption certificate kept, and when was the last restore test? | CP-09, CP-09(01), CP-09(08), CP-10(02) | Backup log, the key register entry K10, the last TPL-11 |
| INT-CP-03 | Windows server administrator | How would you rebuild the VMs at the second site, in what order, and how long would it take? | CP-07, CP-10 | \<Contingency Planning Management\>, Table 3; test record |
| INT-CP-04 | \<Organisation\>'s security contact | Where is the second site, how do backups reach it, what keeps one copy offline or immutable, and what connects both sites? | CP-06, CP-06(01), CP-06(03), CP-07(01) to CP-07(03), CP-08 | EV-CP-01, EV-CP-02 |
| INT-CP-05 | Security officer | How is recovery coordinated with incident response, how do you confirm the controls before users return, and what came out of the last exercise? | CP-02c, CP-04, CP-04(01), CP-10 | The last after-action report on TPL-11 |
| INT-CP-06 | Authorising official | What decisions would you make in a recovery, and when were you last told the plan had changed? | CP-02a.07, CP-02f | Plan approval (D-CP-02); M10 on TPL-9 |
| INT-CP-07 | Each contingency role holder | What is your part in recovery, and when were you last trained? | CP-03 | TPL-9; the training register |
| INT-CP-08 | Legal adviser | If an older backup were restored, how would items deleted since be found and deleted again? | CP-02a.05, CP-10 | TPL-15; \<PII Processing Management\>, section 3.7 |

## 9 Identification and Authentication (IA)

**Table 18: IA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-IA-01 | \<Organisation\>'s IT service desk | How do you check who someone is before resetting their password or second factor? | IA-05a, IA-05d | PRO-IA-2 record |
| INT-IA-02 | \<Organisation\>'s IT service desk | What happens to an Active Directory account name when someone leaves? Is it ever given to another person? | IA-04d | \<Organisation\>'s record (EV-AC-01) |
| INT-IA-03 | Sample user | What would you do if you thought your password was known? | IA-05f, IA-05h | None |
| INT-IA-04 | Windows server administrator | How are the key that signs the tokens between the applications and the audit chain key changed, and when were they last changed? | IA-05f, IA-05(06) | Rotation record |
| INT-IA-05 | \<Organisation\>'s security contact | How are devices identified on the network? | IA-03 | EV-IA-01 |
| INT-IA-06 | \<Organisation\>'s HR | What identity evidence do you check, how do you validate and verify it, and how are people told at their address of record? | IA-12, IA-12(02), IA-12(03), IA-12(05) | EV-IA-02 |
| INT-IA-07 | Developers, with \<Organisation\>'s security contact | Show me a sign-in through PingFederate from start to finish. What does \<System Name\> check in the OpenID Connect response, how does the API then read the person's groups from Active Directory over LDAPS, and what happens if I present the same response twice? | IA-02, IA-02(01), IA-02(08) | The trust settings (\<Identification and Authentication Management\>, section 3.3); a test record |
| INT-IA-08 | Security officer, with \<Organisation\>'s IT service desk | Walk me through the last suspected password compromise. When was the account disabled, when were the password and second factor reset, and when was the account enabled again? Why is ending the PingFederate sign-in not enough? | IA-05d, IA-05f, IA-11 | PRO-IA-3 record; TPL-14 |
| INT-IA-09 | Developers | When the UI or Admin application calls the API for a signed-in person, how does the API learn who that person is, and what stops one application, or anything else on the server, from naming another person? | IA-02\[02\] | \<Identification and Authentication Management\>, Table 1; a test record |

## 10 Incident Response (IR)

**Table 19: IR questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-IR-01 | Security officer | Talk me through what happens when someone reports an incident | IR-04, IR-05, IR-08 | \<Incident Response Management\>, and an incident ticket |
| INT-IR-02 | Security officer | When was the last exercise, and what changed as a result? | IR-03, IR-03(02), IR-04c | Exercise record |
| INT-IR-03 | Legal adviser | How do you decide whether to tell the ICO, and how quickly can you? | IR-06 | Reporting record |
| INT-IR-04 | \<Organisation\>'s security contact | How do reports reach you, out of hours too, and what help do you give? How does your severity scale compare with \<System Name\>'s? | IR-06, IR-07, IR-04d | EV-IR-01 |
| INT-IR-05 | Windows server administrator | A user's account is compromised and \<Organisation\> cannot say whose. Show me how you would end every \<System Name\> sign-in at once, and why ending the PingFederate sign-ins is not enough | IR-04a.\[04\] | \<Incident Response Management\>, section 3.9; TPL-6 |
| INT-IR-06 | Auditor | Show me how you would export the audit records as evidence for an incident, record the hash, and check them against the daily chain hash in central logging | IR-04a.\[03\], IR-05 | \<Procedures\>, PRO-AU-2 and PRO-IR-6; TPL-10 |
| INT-IR-07 | Security officer | Who holds a copy of the plan, and who can read the incident records in ServiceNow? How were the last plan changes told to them? | IR-08b, IR-08d, IR-08e | \<Incident Response Management\>, section 3.16; EV-IR-02 |

## 11 Maintenance (MA)

**Table 20: MA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-MA-01 | Windows server administrator | Show me the record for the last maintenance. Who approved it, and who checked the controls afterwards? | MA-02 | Change record and TPL-12 |
| INT-MA-02 | Windows server administrator | Which tools are approved, how is a new one added to App Control for Business, and how is a tool from outside the baseline checked before use? | MA-03, MA-03(01), MA-03(02) | Tool list; App Control policy |
| INT-MA-03 | System owner | How does remote maintenance get approved, watched and ended? | MA-04 | Change record and remote maintenance logs |
| INT-MA-04 | System owner | Who may maintain \<System Name\>? When a supplier helps, how do they see the session without an account, and who drives it? | MA-05, MA-04c | Approved list; screen-sharing settings |
| INT-MA-05 | \<Organisation\>'s IT service desk | How quickly can support and parts arrive? Who approves removing host hardware, how is it sanitised, and how is the system owner told? | MA-02c, MA-02d, MA-06 | EV-MA-01 |
| INT-MA-06 | Security officer | How do you review the maintenance records and the remote maintenance logs, and what happens when a job has no change record? | MA-02a, MA-04a | TPL-12 reviews; remote maintenance logs |
| INT-MA-07 | Administrator | When did you last run the diagnostics in the Admin application? Which job or incident was it for, and where is it recorded? | MA-03a | Change or incident record, TPL-12 and the audit log |
| INT-MA-08 | Security officer | After the last maintenance job, which checks did you run, and how did you confirm that sign-in still works without reading the audit log? | MA-02e | TPL-12; last sign-in report |

## 12 Media Protection (MP)

**Table 21: MP questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-MP-01 | A sample of users | What do you do with a printed page from an item marked \<Classification\>? | MP-02, MP-03, MP-04, MP-06 | Locked storage and shredder |
| INT-MP-02 | Database administrator | Where do backups go, and who can reach them? How are expired backups removed at both sites, and when do you destroy a retired backup encryption certificate? | MP-02, MP-04, MP-05, MP-06 | EV-MP-01, EV-CP-01; TPL-13 |
| INT-MP-03 | \<Organisation\>'s IT service desk | How are disks and backup media sanitised, and how is USB blocked? | MP-06, MP-07 | EV-MP-02, EV-MP-03 |
| INT-MP-04 | Windows server administrator | Show me the encrypted export working area on the application server and your last check. What do you do with a copy older than 24 hours? | MP-04, MP-06 | TPL-8 |
| INT-MP-05 | System owner | When did you last review the media inventory, and check a sample of sanitising certificates against the media records? | MP-02, MP-06 | Inventory review; TPL-13 |

## 13 Physical and Environmental Protection (PE)

**Table 22: PE questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PE-01 | \<Organisation\>'s security contact | Who can enter the data centre and the second site, how are they monitored, are both covered by your ISO/IEC 27001 certificate (Annex A.7) or SOC 2 report, how are cabling, deliveries and removals controlled, and how would \<System Name\>'s security officer hear about an incident? | PE-02, PE-03, PE-04, PE-06, PE-08, PE-16 | EV-PE-01, EV-PE-04 |
| INT-PE-02 | \<Organisation\>'s security contact | What happens at the data centre and the second site in a power failure, fire or flood, and who shuts the \<System Name\> servers down if power cannot be kept? | PE-09 to PE-15 | EV-PE-02, EV-PE-03 |
| INT-PE-03 | Security officer | How are home working controls assessed each year with TPL-26, is anyone printing at home, and how do people raise concerns? | PE-17 | Assessment record |
| INT-PE-04 | \<Organisation\>'s facilities contact | Which managed printers with secure release can \<System Name\> users print to, and where are they? | PE-05 | EV-PE-05 |
| INT-PE-05 | A sample of people who work from home | Where do you work when at home? What would you do if you needed to print, or if your laptop was lost? | PE-05, PE-17 | Home working check (TPL-26) |

## 14 Planning (PL)

**Table 23: PL questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PL-01 | System owner | When was the plan last reviewed, and who received it? | PL-02b, PL-02c | The plan review record, naming the recipients, in the change record |
| INT-PL-02 | A sample of users | Which rules did you sign, and when? | PL-04 | Signed acknowledgement |
| INT-PL-03 | System owner | How do you decide whether a control can be tailored? | PL-11 | \<Tailoring Register\> |
| INT-PL-04 | A sample of users and an administrator | Which version of the rules did you sign, and when? Can you name two rules that apply to you? Have you been asked to sign again after a change? | PL-4b, PL-4d, PL-4(1) | TPL-21 and the register of signatures in \<Planning Management\>, section 3.5 |
| INT-PL-05 | Head of Cyber | Have you seen the System Security Plan, and do you concur with it? How are you told when it changes? | PL-02a.15, PL-02b | The plan's approval in \<Decision Register\> and the plan review record |
| INT-PL-06 | Authorising official | Did you review and approve the System Security Plan and the privacy plan before they were put into effect? Did you select the baseline and approve each tailoring entry? | PL-02a.15, PL-10, PL-11 | D-PL-01 to D-PL-03 and the tailoring decisions in \<Decision Register\>, with their sign-off sheets |
| INT-PL-07 | Legal adviser | How is the privacy plan kept current, and how is its architecture checked when the system changes? | PL-02a.15, PL-02c, PL-08a.02, PL-08c | D-PL-02, and the plan review record |

## 15 Program Management (PM)

PM is inherited from \<Organisation\>'s programme and is not assessed for \<System Name\> (\<Tailoring Register\>, TR-PM-01). These questions check that what \<System Name\> inherits from \<Organisation\>'s programme is in place.

**Table 24: PM questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PM-01 | Head of Cyber | Where is \<Organisation\>'s security programme written down, what is its risk appetite, is \<System Name\> in the system inventory, and who is the data protection officer? Do \<System Name\>'s risk thresholds fit the appetite? | PM-1, PM-2, PM-5, PM-9, PM-19 (inherited; \<Program Management\>, section 3.3) | EV-PM-01, EV-PM-02, EV-PM-04 |
| INT-PM-02 | Legal adviser | Is there a privacy programme plan, and who leads it? Where is \<System Name\>'s personal data in the record of processing? How do complaints and breaches reach the people who must be told? | PM-5(1), PM-18, PM-19, PM-26, PM-27 (inherited; \<Program Management\>, section 3.3) | EV-PM-02, EV-PM-04 |

## 16 Personnel Security (PS)

**Table 25: PS questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PS-01 | \<Organisation\>'s HR | What screening is done before someone starts, and when is it repeated? | PS-02b, PS-03 | EV-PS-01 |
| INT-PS-02 | Data Owner, with the system owner | Show me the last leaver and the last mover. When were you told, and when were the Active Directory account disabled, the group memberships changed and the PingFederate sign-in ended? | PS-04, PS-05 | TPL-14 and audit records |
| INT-PS-03 | System owner | Show me the signed agreements for a sample of people, and how you check them before access is given | PS-06 | TPL-21, the register of signatures and the personnel security register |
| INT-PS-04 | \<Organisation\>'s HR | How are exit interviews and disciplinary action handled, and do job descriptions state security duties? | PS-04c, PS-08, PS-09 | EV-PS-02 |
| INT-PS-05 | System owner | How do you check that external people meet their contract terms? | PS-07 | EV-PS-03 |
| INT-PS-06 | A line manager | When one of your people changes role or leaves, whom do you tell, how, and how quickly? | PS-04, PS-05 | TPL-14 |
| INT-PS-07 | System owner | How was each role's risk designation decided, when were they last reviewed, and how do you know when someone in a higher risk role is due to be rescreened? | PS-02, PS-03b | \<Personnel Security Management\>, Table 1; TPL-3; the personnel security register |
| INT-PS-08 | System owner | When were you last told of a supplier's leaver or mover, or of a sanctions process, and what did you do? | PS-07d, PS-08b | TPL-16; TPL-14 |

## 17 Personally Identifiable Information (PT)

**Table 26: PT questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-PT-01 | Legal adviser | What is the lawful basis, and is consent ever relied on? | PT-02, PT-04 | The written position |
| INT-PT-02 | Legal adviser | Where is the impact assessment, and what does it say about special category data? | RA-08, PT-07 | The assessment |
| INT-PT-03 | Legal adviser | Show me a request from an individual. How was it handled? | AC-03(14), SI-18(04) | A request record |
| INT-PT-04 | Business owner | What personal data do schemas hold, for how long, and who checks it is correct? | PT-03, SI-12(01), SI-18 | Retention periods and the last check |
| INT-PT-05 | Developers | What personal data is in audit records and test data? | AU-03(03), SI-12(02) | A sample of each |
| INT-PT-06 | Legal adviser | Show me a data protection complaint. Was it acknowledged within 30 days, and how was it resolved? | PT-01, PM-26 | A complaint record (TPL-22) |
| INT-PT-07 | Legal adviser's delegate who would handle a request | Show me how you would find every item about one person across all schemas, and how you would record a correction or deletion | AC-03(14), SI-18(04) | TPL-15; audit records |
| INT-PT-08 | Data protection officer | What advice did you give on the impact assessment, and what changed as a result? | RA-08, PT-02 | The impact assessment |

## 18 Risk Assessment (RA)

**Table 27: RA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-RA-01 | System owner | How is risk reviewed, and who sees the result? | RA-03d, RA-03e | Review record |
| INT-RA-02 | Authorising official | How did you reach the Moderate categorisation? | RA-02 | \<System Security Plan\>, section 3.3 |
| INT-RA-03 | Windows server administrator | Show me the last scan. How quickly were findings fixed? | RA-05, RA-05(05) | Scan report |
| INT-RA-04 | Security officer | How would someone report a vulnerability, and what happens next? | RA-05(11) | Route, a sample report |
| INT-RA-05 | Developers | How do you judge the risk of a new package? | RA-03(01) | Supply chain review |
| INT-RA-06 | Security officer | A flaw in a component \<System Name\> uses was added to CISA's exploited list today. Walk me through the next 3 days | RA-05d, SI-02 | A TPL-7 record and the emergency change |
| INT-RA-07 | System owner | Show me the critical components and how they were chosen. What would make the list change? | RA-09 | \<Risk Assessment Management\>, section 3.9; TPL-23 |
| INT-RA-08 | Authorising official | How do you decide whether to accept a risk, and how do you know the decision fits \<Organisation\>'s risk appetite? | RA-07, RA-03b | \<Risk List\>, sections 3 and 4.2; \<Decision Register\> |

## 19 System and Services Acquisition (SA)

**Table 28: SA questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SA-01 | Developers | Walk me through a recent change, from plan to release, under \<Organisation\>'s corporate SDLC | SA-03, SA-10, SA-15 | The change record and pull request |
| INT-SA-02 | Developers | What tests run at a release, and where are the results? | SA-11 | The latest results |
| INT-SA-03 | System owner | How are security and privacy costs raised and funded? | SA-02 | The budget request |
| INT-SA-04 | System owner | How do you check that providers keep to their contracts? | SA-04, SA-09 | The last review |
| INT-SA-05 | Developers | How do you know a component is nearing the end of its support? | SA-22 | The monthly check |
| INT-SA-06 | Developers | Show me how the default branch is protected, and the review on the last change merged to it | SA-10, CM-3 | The repository's branch protection settings and the latest release check results |
| INT-SA-07 | \<Organisation\>'s contract owner | Show me the security and privacy terms in the agreement for \<System Name\>'s hosting and services, and how \<Organisation\> shows it keeps to them | SA-04, SA-09 | The agreement; service level reports |
| INT-SA-08 | Security officer | Which designs have you checked against the engineering principles, and what changed as a result? | SA-03d, SA-08 | TPL-6 records of design checks |

## 20 System and Communications Protection (SC)

**Table 29: SC questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SC-01 | Developers | Which traffic is encrypted, and how are certificates renewed? | SC-08, SC-08(01), SC-23 | VM configuration, certificate record |
| INT-SC-02 | Developers | Where are keys held, who can reach them, and how are they rotated? | SC-12 | Key record |
| INT-SC-03 | Developers | Which scripts can pages load, how do you know each is served by \<System Name\> itself and none from a content delivery service, and how would you notice an unapproved one? | SC-18 | Page policy and the packaged browser libraries |
| INT-SC-04 | Windows server administrator | Is disk encryption on, and how are recovery keys protected? | SC-28, SC-28(01) | BitLocker status on both VMs |
| INT-SC-05 | \<Organisation\>'s security contact | What protects the boundary, and how are exceptions approved? | SC-07, SC-07(03), SC-07(04), SC-07(05) | EV-SC-02 |
| INT-SC-06 | \<Organisation\>'s security contact | What protects against denial of service, and how is DNS protected? | SC-05, SC-20, SC-21, SC-22 | EV-SC-01, EV-SC-05 |
| INT-SC-07 | Windows server administrator | Show me where each key in the register is kept, when it was last changed, and how the data protection key rings are protected | SC-12, SC-13 | \<System and Communications Protection Management\>, section 3.4, and the TPL-6 records of key changes |
| INT-SC-08 | Windows server administrator | Show me each server's host firewall rules, and how they match the allow-lists | SC-07, SC-07(05) | The host firewall rules; \<System and Communications Protection Management\>, section 3.2 |

## 21 System and Information Integrity (SI)

**Table 30: SI questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SI-01 | Developers | How do you find out a package has a flaw, and how quickly is it fixed? | SI-02a, SI-02c | Package check, change record |
| INT-SI-02 | Windows server administrator | How are updates tested, and is Defender running on both VMs? | SI-02b, SI-03 | Update and Defender records |
| INT-SI-03 | Security officer | Show me your last review of alerts and the central logs. Which detection use case would raise an alert, who is told, and what did you do about the last one? | SI-04d, SI-04(05) | TPL-8 review record, an alert and its PRO-SI-4 response |
| INT-SI-04 | Security officer | Which advisories do you receive, and what did you do about the last one? | SI-05 | Advisory record |
| INT-SI-05 | Developers | How are inputs checked, and what does a user see when something fails? | SI-10, SI-11 | Test results |
| INT-SI-06 | \<Organisation\>'s security contact | What monitors traffic, and how are firmware updates handled? | SI-04(04), SI-02c | EV-SI-01, EV-SI-02 |
| INT-SI-07 | Security officer | Show me the integrity baseline for the running release. How would you know a release package, a stored file or an audit record had been changed? | SI-07a, SI-07(01), SI-07(07) | \<System and Information Integrity Management\>, section 3.5; the integrity baseline; a TPL-8 integrity check |
| INT-SI-08 | Developers | Upload the EICAR test file and show me what happens, and where it is recorded | SI-03 | The refused upload; the audit record; the alert |

## 22 Supply Chain Risk Management (SR)

**Table 31: SR questions**

| ID | For | Question | Statements | Ask to see |
| --- | --- | --- | --- | --- |
| INT-SR-01 | System owner | Who is on the supply chain team, and when did it last meet? | SR-02, SR-02(01) | Minutes |
| INT-SR-02 | Developers | Where does each package come from, and how do you know the restore got exactly what the lock file records? | SR-03, SR-05 | A recent example |
| INT-SR-03 | Security officer | What happens when a supplier reports a compromise? | SR-08 | EV-SR-01 |
| INT-SR-04 | \<Organisation\>'s IT service desk | How is hardware inspected, repaired and disposed of? | SR-10, SR-11(02), SR-12 | EV-SR-02 |
| INT-SR-05 | Developers | Show me the bill of materials for the release I am looking at, and how you checked that release against it before installation | SR-03b, SR-10 | The bill of materials; the release check results |
| INT-SR-06 | System owner | Show me the last review of \<Organisation\> as a supplier, and what changed as a result | SR-06, SR-02(01) | TPL-16 |
