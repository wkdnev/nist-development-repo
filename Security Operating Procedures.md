# \<System Name\> Security Operating Procedures

## 1 Purpose and how to use this document

These are the security operating procedures (SyOps) for \<System Name\>. They have three parts:

- **Part A** (section 2) holds the rules of behaviour that everyone must read and sign before getting access, as CSS control PL-4 requires.
- **Part B** (section 3) adds the rules for privileged users.
- **Part C** (section 4) sets out how \<System Name\>'s security is operated: each duty, who does it, how often, and the record that proves it was done.

Sections 5 to 9 cover exceptions, contacts, definitions, the link from each rule to its CSS control, and acknowledgement.

Frequencies and time limits are those set in the family documents, and the values are set at corporate level by \<Organisation\>. Role holders are named in \<Roles and Responsibilities\>. Items in square brackets are placeholders for the system owner to complete.

**Table 1: Who reads which part**

| Who | Reads and signs | When |
| --- | --- | --- |
| Everyone given access to \<System Name\> | Part A | Before access, every 12 months, and when the rules change |
| Administrators, auditors, the security officer, Windows server and database administrators, and developers with access to a live system | Parts A and B | Before privileged access, every 12 months, and when the rules change |
| Holders of the roles in Part C | Their duties in Part C | Covered by role-based training (AT-3), with no separate signature |

## 2 Part A: rules for everyone

"You" means anyone who uses \<System Name\>. The rules are numbered A1 to A55 so that each can be traced to its CSS control in section 8.

### 2.1 Your responsibilities and the law

**A1.** Follow these rules, \<Organisation\>'s information security policies, and the \<System Name\> policies and procedures that apply to your role.

**A2.** You are accountable for everything done with your account.

**A3.** Do not try to get round, disable or test any security control, and do not try to reach anything you have not been given access to.

**A4.** Breaking these rules may lead to loss of access and to disciplinary action under \<Organisation\>'s disciplinary policy. Misuse can also be a criminal offence. This includes unauthorised access to or modification of computer material under the Computer Misuse Act 1990, and knowingly or recklessly obtaining or disclosing personal data without the controller's consent under section 170 of the Data Protection Act 2018. \[Legal adviser to confirm this wording.\]

**A5.** If a rule is unclear, or you cannot follow it, ask the security officer before you act. Exceptions are granted only in writing (section 5).

### 2.2 Monitoring and privacy

**A6.** When you sign in, \<System Name\> shows this notice, which you must accept before going further: "This system is for authorised use only. Activity is monitored and recorded. Unauthorised use may lead to disciplinary or legal action. By continuing you accept these terms."

**A7.** Everything you do in \<System Name\> is recorded, including sign-ins, searches, items viewed and downloaded, changes and exports. Authorised auditors review these records every week and report anything suspicious to the security officer. The records may be used in investigations, and in disciplinary or legal proceedings.

**A8.** You have no expectation of privacy in your use of \<System Name\>. By signing these rules you agree to this monitoring. It is carried out only for security, audit and legal compliance.

### 2.3 Your account and password

**A9.** Use only your own account. Never share your password, let anyone else use your sign-in, or use someone else's account.

**A10.** Sign in to \<System Name\> with your \<Organisation\> account, through single sign-on with multi-factor authentication. \<System Name\> has no password of its own. Follow \<Organisation\>'s rules for that account's password (\<Policy\> (IA), R3).

**A11.** Do not write your password down, keep it in a file, email or chat, or let a browser save it. An \<Organisation\> approved password manager may be used.

**A12.** Nobody, including administrators and the service desk, will ever ask for your password. Never give it to anyone.

**A13.** If you think anyone else knows your password, or you lose your second factor, tell \<Organisation\>'s IT service desk and the security officer at once.

**A14.** Repeated failed sign-ins lock your \<Organisation\> account. Report any lockout you did not cause.

**A15.** When working remotely, connect through \<Organisation\>'s VPN with multi-factor authentication. Never approve a sign-in prompt you did not start.

### 2.4 Using \<System Name\> and its items

**A16.** Use \<System Name\> only for \<Organisation\> business. Personal use is not allowed.

**A17.** Open, search for and download only the items your current work needs, even if you can see more.

**A18.** If you can see a schema or item you should not, stop, do not explore further, and report it to the security officer.

**A19.** Do not alter, delete, hide or falsify any item or record, except as your role and an approved process allow.

**A20.** Use the fault report to report a faulty or wrong item or file.

**A21.** Do not use \<System Name\> to store, view or share anything illegal, offensive, harassing or discriminatory, or anything you have no right to use under copyright or licence.

**A22.** Do not share items outside their schema, or with anyone outside \<Organisation\>, unless the schema's Data Owner has agreed and the recipient has a business need.

### 2.5 Personal data

\<System Name\> holds personal data: at least the sign-in identities in its audit records, and whatever its information types hold (\<System Description\>, section 3.4). UK GDPR, the Data Protection Act 2018 and the Data (Use and Access) Act 2025 apply, and the privacy plan is \<Privacy Plan\>.

**A23.** Look at personal data only when your current task needs it, and use it only for the purposes it is held for, as set in \<PII Processing Management\>.

**A24.** Copy, export or print only the minimum personal data the task needs.

**A25.** Do not disclose personal data to anyone who does not need it for their work, and never to the public, the media or on social media.

**A26.** If personal data is wrong, out of date or in the wrong schema, tell the schema's Data Owner so it can be put right.

**A27.** Pass any request from a person about their data, such as to see, correct or delete it, or to restrict or object to its use, and any complaint about how their data is handled, to the legal adviser the same working day. Do not answer it yourself.

**A28.** Delete exported or printed personal data securely once you no longer need it, and within 30 days at the latest.

**A29.** Report any loss, theft, misdirected message or unauthorised access involving personal data to the security officer at once, and within 1 hour. The legal adviser decides whether to report it to the ICO, which must be done within 72 hours of \<Organisation\> becoming aware.

### 2.6 Exports, printing, copies and removable media

**A30.** Export, download or print only when your work needs it. Bulk export is only for the roles allowed it.

**A31.** Save exported files only in approved \<Organisation\> locations: \[approved locations\]. Never save them on personal devices, in personal cloud storage or in personal email.

**A32.** Do not copy \<System Name\> information to USB drives or other removable media. USB storage is blocked on managed devices. Where there is a business need, ask for an exception (section 5), and use only encrypted media issued by \<Organisation\>.

**A33.** Print \<System Name\> items only on \<Organisation\>'s managed printers with secure release, and make sure each page carries the \<Classification\> marking. Collect them from the printer straight away, lock them away when not in use, do not take them off site, and cross-cut shred them when finished, to DIN 66399 level P-4 or better.

**A34.** Do not email \<System Name\> items outside \<Organisation\>, and do not set up automatic forwarding of work email to any outside address.

### 2.7 Devices, remote working and travel

**A35.** Use \<System Name\> only on a device managed by \<Organisation\>. Do not use personal computers, phones or tablets. Phones and tablets cannot reach \<System Name\>.

**A36.** Lock your screen whenever you leave your device, even briefly, and close the browser when you finish. \<System Name\> does not lock the page or sign you out itself: your device locks its screen after the inactivity period set by \<Organisation\>, and your sign-in lasts as long as PingFederate allows.

**A37.** Keep your desk clear of printed documents and notes, and place your screen so that others cannot read it.

**A38.** Work remotely only from home, unless the system owner has approved another place in writing. Do not print \<System Name\> items at home, unless the system owner has approved it in writing.

**A39.** When remote, connect to \<Organisation\>'s VPN before opening \<System Name\>. Do not disable the VPN or send traffic around it.

**A40.** Use public Wi-Fi only with the VPN connected before anything else. Never use public or shared computers.

**A41.** Do not use \<System Name\> from outside the UK, or take a device that can reach it abroad, without written approval from the system owner and security officer first (section 5).

**A42.** Report a lost or stolen device to \<Organisation\>'s service desk and the security officer at once, and within 1 hour.

### 2.8 Email, social media, external sites and AI

**A43.** Do not post or discuss \<System Name\> information, items or how the system works on social media, forums or any public website.

**A44.** Do not use your work email address or username to create accounts on outside sites or services, except those \<Organisation\> has approved for business use. Never reuse a work password on them.

**A45.** Do not put \<System Name\> information into any generative AI tool, translation site, file converter or other outside service unless the system owner has approved that tool in writing (section 5).

**A46.** Be wary of emails, messages or calls that ask for items, passwords or system details, or press you to act fast. Do not click links or open attachments you did not expect. Check the sender by a separate route, and report suspected phishing.

### 2.9 Software and changes

**A47.** Do not install software, browser extensions or plug-ins, or change security settings, on the device you use for \<System Name\> unless \<Organisation\> has approved them.

**A48.** Do not connect unapproved hardware to an \<Organisation\> device or network.

**A49.** Do not use tools that scan, test or bypass security, or that hide your activity, such as anonymising services.

### 2.10 Spotting and reporting

**A50.** Report any of these to the security officer within 1 hour:

- a password or account you think is compromised
- items you should not be able to see
- personal data that is lost, sent to the wrong person, or seen by someone who should not see it
- a lost or stolen device
- unexpected pop-ups, slowness or software installing itself
- a request for passwords or items from someone you cannot verify
- someone using \<System Name\> who should not be
- any breach of these rules

**A51.** Report by phone or email to the security officer: \[business phone and email\]. ServiceNow may also be used. If the security officer cannot be reached, contact the deputy or \<Organisation\>'s security contact (section 6).

**A52.** Do not investigate yourself, delete evidence or warn anyone involved. Leave anything relevant as it is.

**A53.** You will not be penalised for reporting in good faith, including reporting your own mistakes.

### 2.11 Training

**A54.** Complete \<Organisation\>'s security and privacy awareness training before you get access and every 12 months, together with the \<System Name\> briefing on these rules (\<Awareness and Training Management\>, section 3.3). Answer the 5-question check at the end of the briefing.

**A55.** Read these rules again and sign them again every 12 months, and after a material change: a new or stricter rule, a changed consequence, new monitoring or a new privileged duty. The system owner tells you when, and each signature is recorded on TPL-21 (\<Policy\> (PL), R6 and R7).

## 3 Part B: rules for privileged users

Part B applies, in addition to Part A, to administrators, auditors, the security officer, business owners, the legal adviser's delegate, Windows server and database administrators, and developers with access to a live system. A privileged account can change or expose the whole system, so these rules are stricter. The rules are numbered B1 to B22.

### 3.1 Before and while you hold privileged access

**B1.** Complete the role-based security training for your role before you receive privileged access, and every 12 months.

**B2.** Use your privileged account only for the privileged task in hand. Use a separate ordinary account for everyday work.

**B3.** Never use a privileged account to browse the web, read email, join meetings or chat.

**B4.** Never share privileged credentials, secrets or keys. Each administrator has their own named account. Service accounts are managed by the operating system, and nobody signs in with them.

**B5.** Tell the system owner the same day when you no longer need privileged access, for example when your role changes.

**B6.** Do not hold duties that conflict, such as approving and making the same change, or reviewing your own actions. Tell the system owner if it happens.

### 3.2 Managing accounts and access

**B7.** Change schemas, or the groups a schema uses, only with the approval that \<Procedures\> (AC) requires, and keep the record. Only a group's owner changes its members, and only on a request authorised in ServiceNow: by the Data Owner for a schema's group, or the system owner for a role group.

**B8.** Never raise your own privileges. Another approved person must make any change to your own access, and nobody's privileges may be raised without approval.

**B9.** Confirm a person's identity by a separate route before you restore any access. Password resets and unlocks are done by \<Organisation\>'s IT service desk, not in \<System Name\>.

**B10.** Do not open items just because your role allows it. Open them only for a task that needs it, and note the reason when it is not obvious.

**B11.** Protect anything you see in the course of your duties, including other people's personal data, and use it for no other purpose.

### 3.3 Systems, changes and tools

**B12.** Never alter, delete or disable audit records or logging. Report any failure of auditing at once. Treat application and server logs that repeat audit details as audit records: read them only when your role needs it, and never copy them off the VMs except as incident evidence.

**B13.** Change \<System Name\>, its VMs, its database or its settings only through an approved change (section 4.5).

**B14.** Do not change security settings, firewall rules, certificates or keys without an approved change.

**B15.** Do not carry out database maintenance on a live system without an approved change, and then only with a second person present (\<Procedures\>, PRO-MA-7). No debug or test page is included in a release: report any you find.

**B16.** Query or change data directly in the database only for an approved change or incident, and record what you did.

**B17.** Do not install, keep or use hacking, scanning or password-cracking tools. The only exception is approved scanning tools used for approved scans.

**B18.** Never introduce or write malicious code.

**B19.** Keep secrets, keys and passwords out of source code, tickets, chat and documents. Hold them only in the approved key store. Report any exposed secret at once.

### 3.4 Maintenance and incidents

**B20.** Use only approved maintenance tools, and connect for remote maintenance only through \<Organisation\>'s approved route (section 4.7).

**B21.** Escort and supervise anyone doing maintenance who does not hold \<System Name\> access.

**B22.** Report any suspected security incident, including one you caused, to the security officer at once.

## 4 Part C: operating procedures

Part C sets out how \<System Name\>'s security is run. Each duty has a reference, C1 to C53, so that it can be traced to its CSS control in section 8. Each names the record that proves it was done. Records use the forms in \<Record Templates\>. A ServiceNow record holding the same fields may replace a form. Records are kept for 3 years in \[the restricted records location\], unless a longer period applies. Audit records stay in \<System Name\> for 12 months and then in an offline archive for 12 more; application logs are kept for 30 days (\<Audit and Accountability Management\>).

The detection use cases U1 to U8 in \<System and Information Integrity Management\>, section 3.4, say what raises an alert, including repeated failed sign-ins, a break in the audit chain and a Defender detection, and \<Procedures\>, PRO-SI-4, says how to respond.

### 4.1 Operating calendar

**Table 2: Operating calendar**

| Ref | Duty | Who | How | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| **Daily** |  |  |  |  |  |
| C1 | Check all services are healthy | Administrator | The API health check and each application's start page | Health check log on TPL-8, one line a day | SI-4, CP-2 |
| C2 | Back up the database, which holds every item and file | Database administrator | \<Procedures\>, PRO-CP-1 | Backup job log, checked at C8 | CP-9 |
| **Weekly** |  |  |  |  |  |
| C3 | Review the audit log, including failed sign-ins, lockouts and privileged actions, against the server, database, PingFederate and Active Directory records | Auditor | Section 4.2 | TPL-8 | AC-2, AC-6(9), AC-7, AU-6 |
| C4 | Review the central logs and any alerts. The security officer does not read the audit log | Security officer | \<Procedures\>, PRO-SI-3 and PRO-SI-4 | TPL-8 | SI-4, AU-6 |
| C5 | Check Windows and SQL Server logs, or \<Organisation\>'s report on them | Windows server and database administrators | \[Method set with \<Organisation\>\] | TPL-8 | AU-6, AU-6(3), SI-4 |
| C6 | Back up system configuration | Windows server administrator | \<Procedures\>, PRO-CP-1 | Backup job log, checked at C8 | CP-9 |
| C7 | Act on security advisories as they arrive, and confirm none were missed | Security officer | \<Procedures\>, PRO-SI-5 | TPL-7 | SI-5 |
| C8 | Check every backup job in the week succeeded | Database administrator | Backup job logs | TPL-8 | CP-9 |
| **Monthly** |  |  |  |  |  |
| C9 | List the members of \<System Name\>'s groups who have not signed in for 90 days, and have the groups' owners remove them | Administrator; the groups' owners | \<Procedures\>, PRO-AC-8 | TPL-3 | AC-2(3) |
| C10 | Scan for vulnerabilities and review patches | Windows server administrator, security officer | \<Procedures\>, PRO-RA-3 | TPL-7 | RA-5, SI-2 |
| C11 | Check packages, lock files, the in-house package feed and support dates, and run Test-SupplyChain.ps1 at each release | Developers | \<Procedures\>, PRO-SR-1 and PRO-SR-3; \<Procedures\>, PRO-SA-5 | TPL-7 | SI-2, SA-22, SR-3 |
| C12 | Check release packages, file checksums and the audit chain | Windows server administrator, security officer | \<Procedures\>, PRO-SI-6 | TPL-8 | SI-7, SI-7(1), AU-9 |
| C13 | Report security status to the system owner | Security officer | \<Procedures\>, PRO-CA-5 | TPL-8, monthly measures | CA-7 |
| C14 | Update the plan of action | System owner | \<Procedures\>, PRO-CA-3 | \<Plan of Action and Milestones\> change record | CA-5 |
| C45 | Check audit storage, archive records older than 12 months, and check both VMs are within 1 second of UTC | Database administrator, Windows server administrator | \<Procedures\>, PRO-AU-4 | TPL-8 | AU-4, AU-8, AU-11 |
| C46 | Check who can read the application logs, and delete those older than 30 days | Windows server administrator | \<Procedures\>, PRO-AU-7 | TPL-8 | AU-9, AU-11, PT-3 |
| C47 | Check the running configuration against the baseline, and report any drift | Windows server and database administrators | \<Procedures\>, PRO-CM-7 | TPL-8 | CM-2, CM-6, CA-7 |
| C48 | Review every maintenance record against its change record; raise any maintenance without one as an incident | Security officer | \<Procedures\>, PRO-MA-1 | TPL-12 | MA-2, MA-4 |
| C49 | Check the encrypted export working area on the application server, and delete any working copy older than 24 hours (each working day; \<System Description\>, P-20) | Windows server administrator | \<Procedures\>, PRO-MP-5 | TPL-8 | MP-4, MP-6 |
| C50 | Each week, check CISA's Known Exploited Vulnerabilities catalogue and \<Organisation\>'s alerts against \<System Name\>'s components; fix or mitigate any match within 3 days | Security officer | \<Procedures\>, PRO-RA-4 | TPL-7 | RA-5, SI-2, SI-5 |
| **Every 3 months** |  |  |  |  |  |
| C15 | Review privileged access | System owner, auditor | \<Procedures\>, PRO-AC-7 | TPL-3 | AC-2, AC-6(7) |
| C16 | Check the administrators' actions | Head of Cyber | The auditors' review records and their report on the administrators' actions | TPL-8 | AC-6(9), AU-6 |
| C17 | Report security status to the authorising official | Security officer, system owner | \<Procedures\>, PRO-CA-5 | TPL-8 | CA-7 |
| **Every 6 months** |  |  |  |  |  |
| C18 | Test that backups can be restored | Database administrator | \<Procedures\>, PRO-CP-2 | TPL-11 | CP-9(1) |
| **Every 12 months** |  |  |  |  |  |
| C19 | Review the members of each schema's groups, and the system owner the role groups at C15 | Data Owners | \<Procedures\>, PRO-AC-7 | TPL-3 | AC-2 |
| C20 | Change keys and secrets as \<System Description\>, P-10 sets. The API has no database password | Database administrator, Windows server administrator | \<Procedures\>, PRO-IA-4 and PRO-SC-3 | TPL-6 | IA-5, SC-12 |
| C21 | Exercise the incident response and contingency plans | Security officer, system owner | \<Procedures\>, PRO-IR-3; \<Procedures\>, PRO-CP-4 | TPL-11 | IR-3, CP-4 |
| C22 | Complete awareness and role training | Everyone; the security officer keeps records | \<Procedures\>, PRO-AT-1 to PRO-AT-5 | TPL-9 | AT-2, AT-3, AT-4 |
| C23 | Re-sign Parts A and B | Everyone; the system owner keeps the register of signatures | Section 9 | TPL-21; the register of signatures (\<Planning Management\>, section 3.5) | PL-4, PS-6 |
| C24 | Review functions, ports, software and services | Windows server administrator, developers | \<Procedures\>, PRO-CM-5 | TPL-3 | CM-7(1) |
| C25 | Review the boundary and connections | System owner, \<Organisation\>'s security contact | \<Procedures\>, PRO-SC-8; \<Procedures\>, PRO-CA-2 | TPL-3 | SC-7, CA-3, CA-9 |
| C26 | Review the supply chain, external services and suppliers | System owner, developers | \<Procedures\>, PRO-RA-2; \<Procedures\>, PRO-SA-3; \<Procedures\>, PRO-SR-2 | TPL-16 | RA-3(1), SA-9, SR-6 |
| C27 | Review development tools and standards | Developers, security officer | \<Procedures\>, PRO-SA-6 | TPL-23 | SA-15 |
| C28 | Review maintenance tools and people | Windows server administrator, system owner | \<Procedures\>, PRO-MA-3 and PRO-MA-5 | TPL-12 | MA-3, MA-5 |
| C29 | Check \<Organisation\>'s physical security evidence | System owner | \<Procedures\>, PRO-PE-1 | Response logged in \<Evidence Requests\> | PE-2 to PE-16 |
| C30 | Assess home working controls | Security officer | \<Procedures\>, PRO-PE-4 | TPL-4 | PE-17 |
| C31 | Review risk designations and access agreements | System owner | \<Procedures\>, PRO-PS-4 | TPL-3 | PS-2, PS-6 |
| C32 | Check personal data is accurate, relevant and still needed, and approve the disposal of items due under the retention schedule (\<System Description\>, FR-074) | Data Owners; the business owner approves disposal | \<Procedures\>, PRO-PT-5 | TPL-3 | SI-18, PT-3 |
| C33 | Check the privacy notice names \<System Name\> | System owner | \<Procedures\>, PRO-PT-3 | TPL-4 | PT-5 |
| C34 | Review exceptions | System owner | Section 5 | Exception register, TPL-17 | PL-4, CA-5 |
| C35 | Review these SyOps and the other security documents | System owner | Each document's change record | Document change record | PL-4c, PL-2 |
| C52 | Review the cryptographic and key register, the host firewall allow-lists, external services and exceptions; schedule keys and certificates due for change | System owner, security officer, \<Organisation\> | \<Procedures\>, PRO-SC-8 | TPL-23 | SC-7(4), SC-12, SC-13 |
| C53 | Check BitLocker is on for both VMs and that a recovery key works; check backups are encrypted | Windows server administrator, database administrator | \<Procedures\>, PRO-SC-7 | TPL-11 | SC-28, SC-28(1) |
| **When an event occurs** |  |  |  |  |  |
| C36 | Grant, change or remove access | The groups' owners; \<Organisation\>'s service desk ends PingFederate sign-ins | Section 4.4 | TPL-2, TPL-14 | AC-2, PS-4, PS-5 |
| C37 | Apply updates within the time limits in Table 4 | Windows server administrator, database administrator, developers | Section 4.3, through approved change | TPL-6, TPL-7 | SI-2, CM-3 |
| C38 | Make a change, including an emergency change | Change control element | Section 4.5 | TPL-6 | CM-3, CM-4, CM-5 |
| C39 | Renew certificates before they expire | Windows server administrator | \<Procedures\>, PRO-SC-2 | TPL-6 | SC-8, SC-17 |
| C40 | Repeat the security tests at each release and after a significant change | Developers | The developer test plan in \<System and Services Acquisition Management\>, section 3.9 (15 scripts, including Test-Protection.ps1 for \<Procedures\>, PRO-SC-1), in the test environment; \<Procedures\>, PRO-SA-2 | Results, with a manifest, in the evidence for each family | CA-2, CM-4(2), SA-11 |
| C41 | Carry out maintenance | Windows server and database administrators | Sections 4.6 and 4.7 | TPL-12 | MA-2, MA-4 |
| C42 | Transport, sanitise or dispose of media | \<Organisation\>, Windows server administrator | Section 4.8 | TPL-13 | MP-5, MP-6 |
| C43 | Handle a security incident or personal data breach | Security officer | Section 4.9 | TPL-10 | IR-4, IR-5, IR-6 |
| C44 | Handle a request or complaint from a person about their data. Only the legal adviser's delegate runs the search across all schemas (\<System Description\>, FR-073) | Legal adviser; legal adviser's delegate | \<Procedures\>, PRO-PT-1 and PRO-PT-2 | TPL-15, TPL-22 | AC-3(14), SI-18(4) |
| C51 | Have every code change reviewed by another developer and merged through the protected default branch, and sign each release tag | Developers | \<Procedures\>, PRO-SA-1; Test-Development.ps1 at each release | Pull request or change record, TPL-6 | SA-10, CM-3 |

### 4.2 Audit review procedure (C3)

1. The auditor opens the audit log page in the Admin application and filters to the period since the last review.
2. They look for refused sign-in responses, failed Active Directory lookups, refused access, sign-ins at unusual times, schema and group administration, privileged functions, large exports, configuration changes, reading of the audit log, gaps in the records, and records under unknown names or "System".
3. They compare changes to \<System Name\>'s Active Directory groups, from \<Organisation\>'s records, with the requests authorised in ServiceNow (TPL-2).
4. They check the Windows and SQL Server logs, and \<Organisation\>'s record of PingFederate sign-ins, failed sign-ins and lockouts, and of changes to \<System Name\>'s Active Directory groups, or get \<Organisation\>'s report on them.
5. They run the audit chain check (\<Procedures\>, PRO-AU-2). If tampering is suspected, they preserve the evidence before anything is changed (PRO-AU-2, step 3), and raise it, and anything else unexplained, as a security incident (section 4.9).
6. They record the date, the period covered, the reviewer and the result on TPL-8, and report anything suspicious to the security officer.

### 4.3 Vulnerability management (C10, C11, C37, C50)

**Table 3: Components checked for vulnerabilities, summarised from \<Risk Assessment Management\>, section 3.5**

| Component | How it is checked | Who | How often |
| --- | --- | --- | --- |
| Windows Server 2025 | Vendor updates and a credentialed scan, \<Procedures\>, PRO-RA-3 | Windows server administrator | Monthly, and at each release |
| Microsoft SQL Server 2022 | Vendor updates and security announcements | Database administrator | Monthly |
| .NET and NuGet packages, through the in-house package feed | Package vulnerability report at each build | Developers | Each build, and monthly |
| Browser libraries | Vendor security announcements | Developers | Monthly |
| \<System Name\>'s own applications | Web application scan | Developers | Each release |
| Server and database settings | Configuration scan against the baseline | Windows server administrator, database administrator | Monthly |
| All components, for exploited flaws | CISA's Known Exploited Vulnerabilities catalogue and \<Organisation\>'s alerts, \<Procedures\>, PRO-RA-4 | Security officer | Weekly (C50) |

**Table 4: Time limits for fixes, summarised from \<Risk Assessment Management\>, section 3.6**

| Severity | Fix within |
| --- | --- |
| Critical or high | 14 days, matching Cyber Essentials Plus |
| Medium | 30 days |
| Low | 90 days |
| Exploited (in CISA's catalogue, or confirmed by the vendor) | 3 days, as an emergency change |

A fix that cannot be made in time goes through PRO-AC-15 and into \<Plan of Action and Milestones\>. Updates are tested first, as \<Procedures\>, PRO-SI-1 requires. These times are the timetable in \<Risk Assessment Management\>, section 3.6, counted from the fix's release, or from detection if later; severity is the vendor's rating, or else the CVSS base score.

### 4.4 Joiners, movers and leavers (C36)

1. **Joiner.** The person asks for access in ServiceNow. Their line manager approves it, and the group's owner authorises it: the system owner for a role, or the Data Owner for a schema. Before the person is added to a group, they complete training (A54), sign Part A, and Part B if privileged. The owner adds them to the fewest Active Directory groups the role needs. No \<System Name\> account is created.
2. **Mover.** The person's manager tells the system owner and the owners of the person's groups within 1 working day of a role change. Access no longer needed is removed and recorded on TPL-14.
3. **Leaver.** \<Organisation\> disables the person's Active Directory account at once, which ends their access, and the owners of their groups remove the memberships within 5 working days. Any exported files or paper are recovered or destroyed, and recorded on TPL-14.
4. **High-risk leaver or misuse.** \<Organisation\>'s service desk disables the Active Directory account and ends the person's PingFederate sign-in within 1 hour of notice (\<Procedures\>, PRO-AC-4).
5. **Inactive members.** Members of \<System Name\>'s groups who have not signed in for 90 days are removed from them each month (C9). \<Organisation\> disables unused Active Directory accounts under its own standard.

### 4.5 Change control (C38)

1. **Normal change.** It is raised on TPL-6, or in ServiceNow. The security officer assesses its security impact, and it is tested in the test environment. The change control board approves it: the system owner, the security officer and the Windows server administrator. After it is made, it is checked to confirm the security functions still work. The documents it affects are updated.
2. **Emergency change.** This is allowed only to stop or limit an incident or an outage. The system owner, or their deputy, approves it by phone or in person before it is made. It is recorded on TPL-6 within 1 working day, and reviewed by the change control board at its next meeting (PRO-CM-8).
3. **Prohibited.** There are no changes without a record, no changes by anyone outside the approved roles, and no changes that switch off auditing or security functions.

The security officer analyses each change's impact against the criteria in \<Configuration Management\>, section 3.9, and the change control board decides under its charter in \<Configuration Management\>, section 3.8. The system owner also checks every change against the list of significant changes in \<Assessment, Authorization, and Monitoring Management\>, section 3.9 (\<Procedures\>, PRO-CA-6). A significant change goes to the authorising official before it is made, who decides whether \<System Name\> must be re-assessed or re-authorised. The full process is in \<Procedures\> (CM) and \<Configuration Management\>.

### 4.6 Secure start-up, shut-down and recovery (C41)

1. **Start-up.** Start the database VM first, then the application VM. Confirm the time is synchronised, run the start-up checks of release packages, file checksums and the audit chain (\<Procedures\>, PRO-SI-6), then confirm every service is healthy (C1).
2. **Shut-down.** A planned shut-down is an approved change. Tell users at least 2 working days beforehand, confirm the latest backups succeeded, stop the UI application and the Admin application, then the API, then SQL Server, and record it.
3. **Emergency shut-down.** If \<Organisation\> warns that the data centre is on backup power, the Windows server and database administrators shut down at once in the same order, without the notice, and before the backup power runs out. It is recorded on TPL-10 as a physical incident.
4. **Recovery.** Follow \<Contingency Planning Management\>. Restore from the latest good backup, run the checks in PRO-CP-2 (row counts, file checksums and the audit chain) and \<Contingency Planning Management\>, section 3.7, and change secrets if a compromise is suspected. Check the members of \<System Name\>'s groups against current staff, and confirm the security functions work, before users return, and record the recovery on TPL-11, or on TPL-10 if it followed an incident.

### 4.7 Remote maintenance (C41)

1. Remote maintenance is done only over a route in \<Maintenance Management\>, section 3.4, from the administrators' managed devices through \<Organisation\>'s managed administration route (F11), with multi-factor authentication and a named account, for an approved change or an incident.
2. The connection is logged, limited to the task, and ended as soon as it is finished.
3. Afterwards the server or database administrator runs the checklist after maintenance (\<Procedures\>, Table MA-2) and records the work on TPL-12, with the connection log reference. The security officer reviews and signs the result within 1 working day.
4. Outside maintenance staff work only under the supervision of a \<System Name\> administrator (B21).

### 4.8 Media sanitisation and disposal (C42)

1. Media are sanitised before reuse or disposal by the method for their type in \<Media Protection Management\>, section 3.6, following CSS and IEEE 2883-2022: cryptographic erase for encrypted virtual disks and backups, and purge or destruction with a certificate for \<Organisation\>'s physical disks.
2. Paper is cross-cut shredded to DIN 66399 level P-4 or better. Exported files are deleted securely from wherever they were saved.
3. Transport, sanitising and any exception are recorded on TPL-13.

### 4.9 Security incidents and personal data breaches (C43)

**Table 5: Incident severity, summarised from \<Incident Response Management\>, section 3.6, which also sets the containment targets and playbooks**

| Severity | Examples | Security officer starts work within | Who is told |
| --- | --- | --- | --- |
| Critical | Personal data breach likely to harm people; ransomware; compromise of a privileged account | 1 hour | System owner, authorising official, legal adviser, \<Organisation\>'s security contact |
| High | Compromised user account; exposed secret; access to items someone should not see | 4 hours | System owner, \<Organisation\>'s security contact; legal adviser if personal data is involved |
| Medium | Malware stopped by Defender; repeated failed sign-ins; a supplier advisory affecting \<System Name\> | 1 working day | System owner |
| Low | A single policy breach with no data exposed | 5 working days | Recorded only |

**Table 6: First actions**

| Event | First action | Who |
| --- | --- | --- |
| Suspected account misuse | Have the account disabled and the person's PingFederate sign-in ended (\<Procedures\>, PRO-AC-4) | Security officer, through \<Organisation\>'s service desk |
| Exposed password or secret | Change it and report it to the security officer | Whoever finds it |
| Access to data someone should not see | Stop, and report to the security officer | Whoever finds it |
| Personal data breach | Report to the security officer at once. The security officer tells the legal adviser, who decides on telling the ICO within 72 hours of becoming aware and the people affected, and records every breach (\<Incident Response Management\>, section 3.8) | Whoever finds it; security officer; legal adviser |
| Lost or stolen device | Report to the service desk and security officer; \<Organisation\> locks or wipes it | Whoever loses it |
| Supplier compromise or advisory | Assess the effect on \<System Name\>, and report to the security officer; tell \<Organisation\>'s security contact | Developers, security officer |
| Audit or service failure | Report to the security officer | Administrator |
| Suspected malware or attack | Report to the security officer, who tells \<Organisation\>'s security contact | Whoever finds it |

1. **Report:** tell the security officer within 1 hour. The security officer tells \<Organisation\>'s security contact and any affected supplier. If personal data is involved, the security officer tells the legal adviser at once.
2. **Contain:** limit the harm, for example by disabling accounts or ending PingFederate sign-ins.
3. **Preserve:** keep logs and evidence, and do not clean up first.
4. **Investigate:** establish what happened, when, and what data was involved.
5. **Recover:** fix the cause and restore normal service (section 4.6).
6. **Learn:** record the incident on TPL-10, update \<Risk List\> and \<Plan of Action and Milestones\>, and tell anyone who must be told.

The full plan is \<Incident Response Management\>, and the procedures are in \<Procedures\> (IR).

## 5 Exceptions

Some rules allow an exception, such as access from abroad (A41), removable media (A32), an outside service or AI tool (A45), or working away from home (A38). Any other rule may be excepted only where the risk is accepted.

1. The person asks on TPL-17, giving the rule, the reason, the period and any compensating measure.
2. The security officer assesses the risk. The system owner approves or refuses in writing. An exception above the system owner's authority goes to the authorising official.
3. Every exception has an end date no more than 12 months away, and ends then unless it is renewed.
4. Approved exceptions are entered in the exception register and in \<Risk List\> where they leave a risk. They are reviewed at each access review (C34).
5. Nobody may act on an exception before it is approved.

## 6 Contacts

The phone number and email of each contact are in \<Roles and Responsibilities\>, section 6.

**Table 7: Contacts**

| For | Who |
| --- | --- |
| Reporting incidents, and questions on these rules | \[Name\], security officer |
| When the security officer is away | \[Name\], system owner, as deputy (\<Roles and Responsibilities\>, Table 4) |
| Exceptions, and decisions on access | \[Name\], system owner |
| Personal data, breaches and requests from individuals | \[Name\], legal adviser |
| Access to a schema, or to a role in \<System Name\> | The schema's Data Owner; \[Name\], system owner, for a role |
| Devices, VPN, lost devices and passwords for the network | \<Organisation\>'s IT service desk |
| \<Organisation\>'s security team | \[Name\]; deputy \[Name\] |

## 7 Definitions

**Table 8: Definitions**

| Term | Meaning |
| --- | --- |
| Approved change | A change raised, assessed, tested and approved under section 4.5 |
| Audit record | \<System Name\>'s record of an action, such as a sign-in, item view, change or export |
| Exception | Written permission to depart from a rule for a set period (section 5) |
| Export | Any copy of \<System Name\> information taken out of \<System Name\>, including downloads, bulk exports, screenshots and prints |
| Generative AI tool | Any service that produces text, images or code from what you give it, such as chat assistants and AI writing or translation tools |
| Managed device | A computer that \<Organisation\> issues and controls, with disk encryption, screen lock and USB blocking |
| Personal data | Information about a living person who can be identified, as defined in UK GDPR |
| Personal data breach | A breach of security that leads to personal data being lost, destroyed, changed, disclosed or accessed without authority |
| Privileged user | Anyone whose access lets them change schemas, groups, settings, security functions, servers or the database, read audit records, approve disposals or search every schema (Part B) |
| Removable media | USB drives, external disks, memory cards and similar storage |
| \<Classification\> | The protective marking for \<System Name\> information and printouts, shown by \<System Name\> on what it displays, prints and exports |
| Security incident | Anything that harms, or could harm, the confidentiality, integrity or availability of \<System Name\> or its information, or that breaks these rules |
| VPN | \<Organisation\>'s virtual private network, used to reach the corporate network from outside the office |

## 8 Traceability to CSS

Table 9 shows where each control that these SyOps serve is met. It lets an auditor test from the control to the rule or duty, or the other way.

**Table 9: Controls and where they are met**

| Control | Rules and duties |
| --- | --- |
| PL-4 Rules of Behavior | Sections 1, 2, 3 and 9; A55; C23, C35 |
| PL-4(1) Social Media and External Site Use | A43, A44, A45 |
| AC-2 Account Management | A9; B5, B7; C3, C9, C15, C19, C36; section 4.4 |
| AC-5 Separation of Duties | B6, B8 |
| AC-6 Least Privilege, with AC-6(2) and AC-6(9) | A17; B2, B3, B10; C3, C16 |
| AC-7 Unsuccessful Logon Attempts | A14; C3 |
| AC-8 System Use Notification | A6, A7, A8 |
| AC-11 Device Lock | A36 |
| AC-17 Remote Access | A15, A39, A40; B20; section 4.7 |
| AC-18, AC-19 Wireless Access and Mobile Devices | A35, A40 |
| AC-20, AC-20(2) External Systems and Portable Storage | A31, A32, A35, A45 |
| AC-21 Information Sharing | A22, A25 |
| AT-2, AT-3, AT-4 Training | A54; B1; C22 |
| AU-6, AU-9 Audit Review and Protection | B12; C3, C4, C5, C12, C16, C46; section 4.2 |
| CA-5, CA-7 POA&M and Continuous Monitoring | C13, C14, C17 |
| CM-2(7) High-risk Travel | A41 |
| CM-3, CM-4, CM-5 Change Control | B13, B14, B15; C37, C38; section 4.5 |
| CM-7(1), CM-11 Least Functionality and User-installed Software | A47, A48, A49; B17; C24 |
| CP-4, CP-9, CP-10 Contingency | C2, C6, C8, C18, C21; section 4.6 |
| IA-2, IA-5 Authentication | A9 to A15; B4, B9, B19; C20 |
| IR-4, IR-5, IR-6 Incidents | A29, A42, A50 to A53; B22; C43; section 4.9 |
| MA-2, MA-3, MA-4, MA-5 Maintenance | B15, B20, B21; C28, C41, C48; section 4.7 |
| MP-2 to MP-7 Media | A28, A30 to A35; C42, C49; section 4.8 |
| PE-5, PE-17 Output Devices and Alternate Work Site | A33, A36, A37, A38 to A42; C30 |
| PS-6, PS-8 Access Agreements and Sanctions | A4; C23, C31; section 9 |
| PT-2, PT-3, SI-12, SI-18 Personal Data | A23 to A28; C32, C33, C44 |
| RA-5, SI-2, SI-5 Vulnerabilities and Advisories | C7, C10, C11, C37, C50; section 4.3 |
| SA-9, SR-6 External Services and Suppliers | C26 |
| SA-10, SA-11, SA-15 Developer Change Control, Testing and Tools | B19; C11, C27, C40, C51 |
| SC-12 Key Management | B19; C20 |
| SC-8, SC-13, SC-18, SC-28 Transport, Cryptography, Page Code and Data at Rest | B19; C39, C40, C52, C53 |
| SI-4, SI-7 Monitoring and Integrity | C1, C4, C12 |

## 9 Acknowledgement

Everyone signs Part A, and privileged users also sign Part B, before getting access, every 12 months and when these rules change. Electronic signature is accepted. The security officer keeps the register for 3 years.

**Part A.** I have read and understood Part A of \<Security Operating Procedures\>, version \<ver\>. I agree to follow it, and I consent to the monitoring described in rules A6 to A8.

**Part B.** I have read and understood Part B of \<Security Operating Procedures\>, version \<ver\>, and I agree to follow it as well as Part A.

**Table 10: Acknowledgement register**

| Name | Account | Part A or B | Version | Signature | Date |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
