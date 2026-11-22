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
| Everyone given access to \<System Name\> | Part A | Before access, every 12 months, and after a material change to the rules (A55) |
| The system owner, administrators, auditors, the security officer, business owners, the legal adviser's delegate, Windows server and database administrators, and developers with access to a live system | Parts A and B | Before privileged access, every 12 months, and after a material change to the rules (A55) |
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

**A6.** When you sign in, \<System Name\> shows this notice, which you must accept before anything else is shown: "This system is for authorised use only. Activity is monitored, recorded and audited. Unauthorised use may lead to disciplinary or legal action. By continuing you accept these terms."

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

**A32.** Do not copy \<System Name\> information to USB drives or other removable media. USB storage is blocked on managed devices. Where there is a business need, ask for an exception (section 5), and use only encrypted media issued by \<Organisation\>. Use that media only on \<Organisation\>'s managed devices and the external system named in the approval, never connect it to a personal or other unmanaged device, and return it for sanitising when the exception ends (P-48). Never use a USB drive or other portable storage that has no known owner, such as one you find: hand it to the security officer.

**A33.** Print \<System Name\> items only on \<Organisation\>'s managed printers with secure release, and make sure each page carries the \<Classification\> marking. Collect them from the printer straight away, lock them away when not in use, do not take them off site, and cross-cut shred them when finished, to DIN 66399 level P-4 or better.

**A34.** Do not email \<System Name\> items outside \<Organisation\>, and do not set up automatic forwarding of work email to any outside address.

### 2.7 Devices, remote working and travel

**A35.** Use \<System Name\> only on a device managed by \<Organisation\>. Do not use personal computers, phones or tablets. Phones and tablets cannot reach \<System Name\>.

**A36.** Lock your screen whenever you leave your device, even briefly. Use Sign out at the end of each working day, and whenever you leave your device for longer than a short break (P-53). \<System Name\> does not lock the page itself: your device locks its screen after 15 minutes without activity (P-03), and your sign-in ends 8 hours after you signed in (P-02).

**A37.** Keep your desk clear of printed documents and notes, and place your screen so that others cannot read it.

**A38.** Work remotely only from home, unless the system owner has approved another place in writing. Never print \<System Name\> items at home.

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

Part B applies, in addition to Part A, to the system owner, administrators, auditors, the security officer, business owners, the legal adviser's delegate, Windows server and database administrators, and developers with access to a live system. A privileged account can change or expose the whole system, so these rules are stricter. The rules are numbered B1 to B23.

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

**B10.** Do not open items just because your role allows it. Open them only for a task that needs it, and note the reason when it is not obvious. The Administrator role opens no item content: use your everyday account, with the schema access it has been given, for any item work.

**B11.** Protect anything you see in the course of your duties, including other people's personal data, and use it for no other purpose.

### 3.3 Systems, changes and tools

**B12.** Never alter, delete or disable audit records or logging. Report any failure of auditing at once. Treat application and server logs that repeat audit details as audit records: read them only when your role needs it, and never copy them off the VMs except as incident evidence.

**B13.** Change \<System Name\>, its VMs, its database or its settings only through an approved change (section 4.5).

**B14.** Do not change security settings, firewall rules, certificates or keys without an approved change.

**B15.** Do not carry out database maintenance, or run the diagnostics in the Admin application, without an approved change or incident (\<Procedures\>, PRO-MA-7). Both are recorded: SQL Server Audit records direct reads of the item tables, and the audit log records each diagnostics run, and the auditor reviews them weekly. No debug or test page is included in a release: report any you find.

**B16.** Query or change data directly in the database only for an approved change or incident, and record what you did.

**B17.** Do not install, keep or use hacking, scanning or password-cracking tools. The only exception is approved scanning tools used for approved scans.

**B18.** Never introduce or write malicious code.

**B19.** Keep secrets, keys and passwords out of source code, tickets, chat and documents. Hold them only in the approved key store. Report any exposed secret at once.

### 3.4 Maintenance and incidents

**B20.** Use only approved maintenance tools, and connect for remote maintenance only through \<Organisation\>'s approved route (section 4.7). Sign out when you finish, rather than only disconnecting.

**B21.** Never give a supplier, or anyone else not on the list of maintenance people, an account or your credentials. They take part only by watching and guiding over your shared screen, while you drive and supervise the session.

**B22.** Report any suspected security incident, including one you caused, to the security officer at once.

**B23.** Use privileged access from outside the office only for an approved change, maintenance or an incident, and only through the VPN and then the managed administration route, signing in with multi-factor authentication at both (P-54). Record the change or incident reference, and disconnect as soon as the task is done.

## 4 Part C: operating procedures

Part C sets out how \<System Name\>'s security is run. Each duty has a reference, C1 to C65, so that it can be traced to its CSS control in section 8. Each names the record that proves it was done. Records use the forms in \<Record Templates\>. A ServiceNow record holding the same fields may replace a form. Records are kept for 3 years in \[the restricted records location\], unless a longer period applies. Audit records stay in \<System Name\> for 12 months and then in an offline archive for 12 more; application logs are kept for 30 days (\<Audit and Accountability Management\>).

The detection use cases U1 to U9 in \<System and Information Integrity Management\>, section 3.4, say what raises an alert, including repeated failed sign-ins, a break in the audit chain and a Defender detection, and \<Procedures\>, PRO-SI-4, says how to respond.

### 4.1 Operating calendar

**Table 2: Operating calendar**

| Ref | Duty | Who | How | Record | Controls |
| --- | --- | --- | --- | --- | --- |
| **Daily** |  |  |  |  |  |
| C1 | Check all services are healthy | Administrator | The API health check and each application's start page | Health check log on TPL-8, one line a day | SI-4, CP-2 |
| C2 | Back up the database, which holds every item and file | Database administrator | \<Procedures\>, PRO-CP-1 | Backup job log, checked at C8 | CP-9 |
| C50 | Check the alert of new entries in CISA's Known Exploited Vulnerabilities catalogue, and \<Organisation\>'s alerts, against \<System Name\>'s components; fix or mitigate any match within 3 days | Security officer | \<Procedures\>, PRO-RA-4 | TPL-7 | RA-5, SI-2, SI-5 |
| **Weekly** |  |  |  |  |  |
| C3 | Review the audit log, including refused sign-ins and privileged actions, against the server and database records and the PingFederate and Active Directory records of failed sign-ins and lockouts | Auditor | Section 4.2 | TPL-8 | AC-2, AC-6(9), AC-7, AU-6 |
| C4 | Review the central logs and any alerts, including the security events for each read or export of the audit log. The security officer does not read the audit log | Security officer | \<Procedures\>, PRO-SI-3 and PRO-SI-4 | TPL-8 | SI-4, AU-6 |
| C5 | Check Windows and SQL Server logs, or \<Organisation\>'s report on them | Windows server and database administrators | \[Method set with \<Organisation\>\] | TPL-8 | AU-6, AU-6(3), SI-4 |
| C6 | Back up system-level information: SQL Server's system databases and each VM's configuration | Database administrator, Windows server administrator | \<Procedures\>, PRO-CP-1 | Backup job log, checked at C8 | CP-9 |
| C7 | Act on security advisories as they arrive, and confirm none were missed | Security officer | \<Procedures\>, PRO-SI-5 | TPL-7 | SI-5 |
| C8 | Check every backup job in the week succeeded and reached the second site | Database administrator | Backup job logs; \<Procedures\>, PRO-CP-1 | TPL-8 | CP-9 |
| **Monthly** |  |  |  |  |  |
| C9 | Run the last sign-in report (FR-085), list the members of \<System Name\>'s groups who have not signed in for 90 days, and have the groups' owners remove them | Security officer; the groups' owners | \<Procedures\>, PRO-AC-8 | TPL-3 | AC-2(3) |
| C10 | Scan for vulnerabilities and review patches | Windows server administrator, security officer | \<Procedures\>, PRO-RA-3 | TPL-7 | RA-5, SI-2 |
| C11 | Check packages, lock files, the in-house package feed and support dates, and run Test-SupplyChain.ps1 at each release | Developers | \<Procedures\>, PRO-SR-1 and PRO-SR-3; \<Procedures\>, PRO-SA-5 | TPL-7 | SI-2, SA-22, SR-3 |
| C12 | Check the installed release files against the release record, and review the monthly file checksum check and malware rescan, and the daily audit chain checks | Windows server administrator, security officer | \<Procedures\>, PRO-SI-6 | TPL-8 | SI-3, SI-7, SI-7(1), AU-9 |
| C13 | Report security status to the system owner | Security officer | \<Procedures\>, PRO-CA-5 | TPL-8, monthly measures | CA-7 |
| C14 | Update the plan of action | System owner | \<Procedures\>, PRO-CA-3 | \<Plan of Action and Milestones\> change record | CA-5 |
| C45 | Check audit storage, archive records older than 12 months, including those held in central logging, and check both VMs are within 1 second of UTC | Database administrator, security officer, Windows server administrator | \<Procedures\>, PRO-AU-4 | TPL-8 | AU-4, AU-8, AU-11 |
| C46 | Check who can read the application logs, and delete those older than 30 days | Windows server administrator | \<Procedures\>, PRO-AU-7 | TPL-8 | AU-9, AU-11, PT-3 |
| C47 | Check the running configuration against the baseline, including that App Control for Business is enforced, and report any drift; also at each release | Windows server and database administrators | \<Procedures\>, PRO-CM-7 | TPL-8 | CM-2, CM-6, CM-7(2), CA-7 |
| C48 | Review every maintenance record against its change record; raise any maintenance without one as an incident | Security officer | \<Procedures\>, PRO-MA-1 | TPL-12 | MA-2, MA-4 |
| C49 | Check the encrypted export working area on the application server, and delete any working copy older than 24 hours (each working day; \<System Description\>, P-20) | Windows server administrator | \<Procedures\>, PRO-MP-5 | TPL-8 | MP-4, MP-6 |
| C58 | Hold the change control board: review the month's changes, emergency changes and drift reports | System owner (chair), security officer, Windows server administrator, legal adviser | \<Configuration Management\>, section 3.8 | Board minutes; TPL-6 | CM-3, CM-3(4) |
| **Every 3 months** |  |  |  |  |  |
| C15 | Review privileged access: the system owner prepares the role-group review and the auditor checks and signs it; the Head of Cyber reviews the system owner's own memberships and checks the administrators | System owner, auditor, Head of Cyber | \<Procedures\>, PRO-AC-7 | TPL-3 | AC-2, AC-6(7) |
| C16 | Check the administrators' actions | Head of Cyber | The auditors' review records and their quarterly report on the administrators' actions (\<Procedures\>, PRO-AU-1, step 6) | TPL-8 | AC-6(9), AU-6 |
| C17 | Report security status to the authorising official | Security officer, system owner | \<Procedures\>, PRO-CA-5 | TPL-8 | CA-7 |
| **Every 6 months** |  |  |  |  |  |
| C18 | Test that backups can be restored, with the backup encryption certificate, on the restore test server at the second site, and erase that server afterwards | Database administrator; Windows server administrator for the test server | \<Procedures\>, PRO-CP-2 | TPL-11; TPL-13 | CP-4, CP-9(1) |
| **Every 12 months** |  |  |  |  |  |
| C19 | Review the members of each schema's groups, and the system owner the role groups at C15 | Data Owners | \<Procedures\>, PRO-AC-7 | TPL-3 | AC-2 |
| C20 | Change keys and secrets as \<System Description\>, P-10 sets. The API has no database password | Database administrator, Windows server administrator | \<Procedures\>, PRO-IA-4 and PRO-SC-3 | TPL-6 | IA-5, SC-12 |
| C21 | Exercise the incident response and contingency plans | Security officer, system owner | \<Procedures\>, PRO-IR-3; \<Procedures\>, PRO-CP-4 | TPL-11 | IR-3, CP-4 |
| C22 | Complete awareness and role training | Everyone; the security officer keeps records | \<Procedures\>, PRO-AT-1 to PRO-AT-5 | TPL-9 | AT-2, AT-3, AT-4 |
| C23 | Re-sign Parts A and B | Everyone; the system owner keeps the register of signatures | Section 9 | TPL-21; the register of signatures (\<Planning Management\>, section 3.5) | PL-4, PS-6 |
| C24 | Review functions, ports, software and services, and compare installed software with the approved list | Windows server administrator, developers | \<Procedures\>, PRO-CM-5 | TPL-3 | CM-7(1), CM-11 |
| C25 | Review the boundary and connections | System owner, \<Organisation\>'s security contact | \<Procedures\>, PRO-SC-8; \<Procedures\>, PRO-CA-2 | TPL-3 | SC-7, CA-3, CA-9 |
| C26 | Review the supply chain, external services and suppliers | System owner, developers | \<Procedures\>, PRO-RA-2; \<Procedures\>, PRO-SA-3; \<Procedures\>, PRO-SR-2 | TPL-23 for the supply chain risk assessment; TPL-16 for each supplier | RA-3(1), SA-9, SR-6 |
| C27 | Review the development process, standards and tools, and raise security and privacy costs as a separate line in yearly budgeting | System owner, developers, security officer | \<Procedures\>, PRO-SA-6 | TPL-23 | SA-2, SA-15 |
| C28 | Review maintenance tools and people | Windows server administrator, system owner | \<Procedures\>, PRO-MA-3 and PRO-MA-5 | TPL-12 | MA-3, MA-5 |
| C29 | Check \<Organisation\>'s physical security evidence | System owner | \<Procedures\>, PRO-PE-1 | Response logged in \<Evidence Requests\> | PE-2 to PE-16 |
| C30 | Assess home working controls | Security officer | \<Procedures\>, PRO-PE-4 | TPL-26 | PE-17 |
| C31 | Review risk designations and access agreements | System owner | \<Procedures\>, PRO-PS-4 | TPL-3 | PS-2, PS-6 |
| C32 | Check personal data is accurate, relevant and still needed, and approve the disposal of items due under the retention schedule (\<System Description\>, FR-074) | Data Owners; the business owner approves disposal | \<Procedures\>, PRO-PT-5 | TPL-3 | SI-18, PT-3 |
| C33 | Check, with the legal adviser, that the privacy notices cover every group of people in the inventory, name \<System Name\> and hold what P-73 sets, and that the link on \<System Name\>'s pages works | System owner | \<Procedures\>, PRO-PT-3 | TPL-4 | PT-5 |
| C34 | Review exceptions | System owner | Section 5 | Exception register, TPL-17 | PL-4, CA-5 |
| C35 | Review these SyOps, the plans in the register and the architecture, and the other security documents | System owner | Each document's change record; \<Procedures\>, PRO-PL-1 and PRO-PL-5 | Document change record; plan review record | PL-4c, PL-2, PL-8 |
| C52 | Review the cryptographic and key register, the host firewall allow-lists, each VM's trust stores, external services and exceptions; schedule keys and certificates due for change | System owner, security officer, \<Organisation\> | \<Procedures\>, PRO-SC-8 | TPL-23 | SC-7(4), SC-12, SC-13, SC-17 |
| C53 | Check BitLocker is on for both VMs and that a recovery key works; check backups are encrypted | Windows server administrator, database administrator | \<Procedures\>, PRO-SC-7 | TPL-11 | SC-28, SC-28(1) |
| C54 | Plan and carry out the yearly control assessment, and report it | System owner, security assessor; the authorising official approves the plan | \<Procedures\>, PRO-CA-1 | Approved plan; TPL-19; \<Control Assessment Record\>; \<Security Assessment Report\> | CA-2, CA-2(1) |
| C55 | Review the authorisation before its end date | System owner, authorising official | \<Procedures\>, PRO-CA-4 | TPL-18 | CA-6 |
| C56 | Review the inherited controls with \<Organisation\>'s security contact | System owner | \<Procedures\>, PRO-CA-7 | \<Assessment, Authorization, and Monitoring Management\>, section 3.6; \<Evidence Requests\> | CA-6 |
| C57 | Independent check of the monitoring | Security assessor | \<Procedures\>, PRO-CA-5, step 3 | The assessor's report; TPL-19 | CA-7(1) |
| C59 | Review the baseline, the inventory and the approved access list, also at each release | System owner, Windows server administrator | \<Procedures\>, PRO-CM-2 | Release record; TPL-5 | CM-2, CM-8, CM-12 |
| C60 | Review the approved software list and component licences | Windows server administrator, developers, system owner | \<Procedures\>, PRO-CM-4 and PRO-CM-9 | \<Configuration Management\>, section 3.5; \<Decision Register\> | CM-7(5), CM-10 |
| C61 | Review the contingency plan with the authorising official, check it against the incident response plan and \<Organisation\>'s plans, renew the backup encryption certificate when due, and refresh the offline copies of the plan | System owner, with the database administrator for the certificate | \<Procedures\>, PRO-CP-7 and PRO-CP-1 | Change record; distribution record | CP-2, CP-2(1), CP-9(8) |
| C62 | Review the authenticator inventory, that each change period was met, and the assurance levels, and take any change to the authorising official | System owner, security officer | \<Procedures\>, PRO-IA-7 | \<Identification and Authentication Management\> change record | IA-5, IA-12 |
| C63 | Review the risks, the threat model and the categorisation, check each acceptance against its review date, and share the result with the authorising official and the Head of Cyber | System owner | \<Procedures\>, PRO-RA-1 | TPL-23; \<Risk List\> | RA-2, RA-3, RA-7 |
| **When an event occurs** |  |  |  |  |  |
| C36 | Grant, change or remove access | The groups' owners; \<Organisation\>'s service desk disables accounts | Section 4.4 | TPL-2 (the ServiceNow request), TPL-14 | AC-2, PS-4, PS-5 |
| C37 | Apply updates within the time limits in \<System Description\>, P-11 | Windows server administrator, database administrator, developers | Section 4.3, through approved change | TPL-6, TPL-7 | SI-2, CM-3 |
| C38 | Make a change, including an emergency change | Change control element | Section 4.5 | TPL-6 | CM-3, CM-4, CM-5 |
| C39 | Renew certificates before they expire | Windows server administrator | \<Procedures\>, PRO-SC-2 | TPL-6 | SC-8, SC-17 |
| C40 | Repeat the security tests at each release and after a significant change | Developers | The developer test plan in \<System and Services Acquisition Management\>, section 3.9 (15 scripts, including Test-Protection.ps1 for \<Procedures\>, PRO-SC-1), in the test environment; \<Procedures\>, PRO-SA-2 | Results, with a manifest, in the evidence for each family | CA-2, CM-4(2), SA-11 |
| C41 | Carry out maintenance | Windows server and database administrators | Sections 4.6 and 4.7 | TPL-12 | MA-2, MA-3, MA-3(1), MA-3(2), MA-4, MA-5 |
| C42 | Transport, sanitise or dispose of media, and destroy a retired backup encryption certificate once its backups are removed | \<Organisation\>, Windows server administrator, database administrator | Section 4.8 | TPL-13 | MP-5, MP-6 |
| C43 | Handle a security incident or personal data breach | Security officer | Section 4.9 | TPL-10 | IR-4, IR-5, IR-6 |
| C44 | Handle a request or complaint from a person about their data. Only the legal adviser's delegate runs the search across all schemas (\<System Description\>, FR-073) | Legal adviser; legal adviser's delegate | \<Procedures\>, PRO-PT-1 and PRO-PT-2 | TPL-15, TPL-22 | AC-3(14), SI-18(4) |
| C51 | Have every code change reviewed by another developer and merged through the protected default branch, and sign each release tag | Developers | \<Procedures\>, PRO-SA-1; Test-Development.ps1 at each release | Pull request or change record, TPL-6 | SA-10, CM-3 |
| C64 | Review the risks they affect after a significant change, incident or new test result; review the critical components at each major release and significant change | System owner, developers | \<Procedures\>, PRO-RA-1 and PRO-RA-6 | TPL-23 | RA-3, RA-9 |
| C65 | At each release, confirm \<Administrator Guide\> and \<User Guide\> still match \<System Name\>, update them, and share any change with administrators, the security officer and users | Developers | \<Procedures\>, PRO-SA-4 | The guides' change record | SA-5 |

### 4.2 Audit review procedure (C3)

1. The auditor opens the audit log page in the Admin application and filters to the period since the last review.
2. They look for refused sign-in responses, failed Active Directory lookups, disabled accounts, refused access, sign-ins at unusual times, schema and group administration without a Data Owner's approval reference, privileged functions, runs of the last sign-in report, large exports, deletions, disposals, searches across every schema, uploads refused for malware, configuration changes, reading of the audit log, failed chain checks, gaps in the records, including those shown by start-up, shut-down and logging failure records, and records under unknown names or "System".
3. They compare changes to \<System Name\>'s Active Directory groups, from \<Organisation\>'s records, with the requests authorised in ServiceNow (TPL-2).
4. They check the Windows and SQL Server logs, including SQL Server Audit's record of reads of the item tables by any login other than the API's, through \<Organisation\>'s central logging (they have no sign-in to the servers), and \<Organisation\>'s record of PingFederate sign-ins, failed sign-ins and lockouts, and of changes to \<System Name\>'s Active Directory groups, or get \<Organisation\>'s report on them.
5. They run the audit chain check, and compare the daily copies of the newest hash in central logging with the audit log (\<Procedures\>, PRO-AU-2). If tampering is suspected, they preserve the evidence before anything is changed (PRO-AU-2, step 4), and raise it, and anything else unexplained, as a security incident (section 4.9).
6. They record the date, the period covered, the reviewer and the result on TPL-8, and report anything suspicious to the security officer.

### 4.3 Vulnerability management (C10, C11, C37, C50)

What is checked for vulnerabilities, by whom and how often is in \<Risk Assessment Management\>, section 3.5. Each fix is made within the time for its severity in \<System Description\>, P-11: 3 days if exploited, as an emergency change; 14 days Critical or High; 30 days Medium; 90 days Low. New entries in CISA's Known Exploited Vulnerabilities catalogue raise an alert, which the security officer checks with \<Organisation\>'s alerts each working day (C50).

A fix that cannot be made in time is entered in \<Risk List\> as a non-compliance, with its compensating measure, and decided under \<Policy\>, section 1.2; a remediation then goes into \<Plan of Action and Milestones\> (\<Risk Assessment Management\>, sections 3.6 and 3.8). Updates are tested first, as \<Procedures\>, PRO-SI-1 requires. The clock and the severity are as \<Risk Assessment Management\>, section 3.6, sets out.

### 4.4 Joiners, movers and leavers (C36)

1. **Joiner.** The person asks for access in ServiceNow. Their line manager approves it, and the group's owner authorises it: the system owner for a role, or the Data Owner for a schema. Before the person is added to a group, \<Organisation\> confirms their screening, and they sign \<Organisation\>'s confidentiality agreement, complete training (A54), and sign Part A, and Part B if privileged (\<Procedures\>, PRO-PS-1). The owner adds them to the fewest Active Directory groups the role needs. No \<System Name\> account is created.
2. **Mover.** The person's manager tells the system owner and the owners of the person's groups within 1 working day of a role change. Access no longer needed is removed and recorded on TPL-14. Access for the new role is given only once its training is done, and, for a higher risk role, the screening repeated (\<Procedures\>, PRO-PS-3).
3. **Leaver.** \<Organisation\> disables the person's Active Directory account at once, and \<System Name\> refuses them within 5 minutes, even while a sign-in is open. The owners of their groups remove the memberships within 5 working days. Any exported files or paper are recovered or destroyed, and recorded on TPL-14.
4. **Higher-risk leaver, dismissal or misuse.** \<Organisation\>'s service desk disables the Active Directory account within 1 hour of notice, which ends access to \<System Name\> within 5 minutes, and ends the person's PingFederate sign-in so that they cannot start a new one. The account stays disabled for at least 8 hours, and the system owner confirms that \<System Name\> refuses the person (\<Procedures\>, PRO-AC-4, PRO-PS-2).
5. **Inactive members.** Members of \<System Name\>'s groups who have not signed in for 90 days are removed from them each month (C9). \<Organisation\> disables Active Directory accounts unused for 90 days within 1 working day (P-38).

### 4.5 Change control (C38)

1. **Normal change.** It is raised on TPL-6, or in ServiceNow. The security officer assesses its security impact, and the legal adviser its privacy impact if it touches personal data, and it is tested in the test environment. The change control board decides on it under its charter: the system owner or their deputy and the security officer must be present, with the legal adviser for a change touching personal data, and nobody approves a change they requested or made. After it is made, it is checked to confirm the security functions still work. The documents, the inventory and the App Control policy it affects are updated.
2. **Emergency change.** This is allowed only to stop or limit an incident or an outage. The system owner, or their deputy, approves it by phone or in person before it is made. It is recorded on TPL-6 within 1 working day, and reviewed by the change control board at its next meeting (PRO-CM-8).
3. **Prohibited.** There are no changes without a record, no changes by anyone outside the approved roles, and no changes that switch off auditing or security functions.

The security officer analyses each change's impact against the criteria in \<Configuration Management\>, section 3.9, and the change control board decides under its charter in \<Configuration Management\>, section 3.8. The system owner also checks every change against the list of significant changes in \<Assessment, Authorization, and Monitoring Management\>, section 3.9 (\<Procedures\>, PRO-CA-6). A significant change goes to the authorising official before it is made, who decides whether \<System Name\> must be re-assessed or re-authorised. The full process is in \<Procedures\> (CM) and \<Configuration Management\>.

### 4.6 Secure start-up, shut-down and recovery (C41)

1. **Start-up.** Start the database VM first, then the application VM. Confirm the time is synchronised, run the start-up integrity check of the installed release files, confirm the API's start-up audit chain check passed (\<Procedures\>, PRO-SI-6), then confirm every service is healthy (C1).
2. **Shut-down.** A planned shut-down is an approved change. Tell users at least 2 working days beforehand, confirm the latest backups succeeded, stop the UI application and the Admin application, then the API, then SQL Server, and record it.
3. **Loss of power.** If a data centre cannot keep power, \<Organisation\>'s hosting staff shut both servers down cleanly through the hypervisor, the application server first, before the backup power runs out, and tell the Windows server administrator (\<Physical and Environmental Protection Management\>, section 3.7). When power returns, the administrators start the servers as in step 1 and confirm that SQL Server recovered each database cleanly. The security officer records it on TPL-10 as a physical incident.
4. **Recovery.** Follow \<Contingency Planning Management\>. Restore the backup encryption certificate, then the latest good backup, run the checks in PRO-CP-2 (row counts, file checksums and the audit chain) and \<Contingency Planning Management\>, section 3.7, delete again any item disposed of or deleted since the backup was taken, and change secrets if a compromise is suspected. Check the members of \<System Name\>'s groups against current staff, and confirm the security functions work, before users return, and record the recovery on TPL-11, or on TPL-10 if it followed an incident.

### 4.7 Remote maintenance (C41)

1. Remote maintenance is done only over a route in \<Maintenance Management\>, section 3.4, from the administrators' managed devices through \<Organisation\>'s managed administration route (F11), with multi-factor authentication and a named account, for an approved change or an incident. From outside the office, connect to the VPN first (P-54, B23).
2. The connection is logged, limited to the task, and ended as soon as it is finished.
3. Afterwards the server or database administrator runs their checks in the checklist after maintenance (\<Procedures\>, Table MA-2) and records the work on TPL-12, with the connection log reference. Within 1 working day, the security officer runs the sign-in, audit chain and checksum checks, then reviews and signs the result.
4. Outside maintenance staff hold no account: they watch and guide over the administrator's shared screen, and the administrator drives and supervises the session (B21).
5. When the work is finished, the administrator signs out of Windows and SQL Server rather than only disconnecting, closes the route connection and ends any screen sharing.

### 4.8 Media sanitisation and disposal (C42)

Media and paper are sanitised, shredded and recorded as \<Procedures\>, PRO-MP-1 and PRO-MP-3, set out, by the method for each type in \<Media Protection Management\>, section 3.6. Exported files are deleted securely from wherever they were saved.

### 4.9 Security incidents and personal data breaches (C43)

Each incident is given a severity, from Low to Critical, which sets how fast the security officer starts work and who is told (\<Incident Response Management\>, section 3.6).

**Table 3: First actions**

| Event | First action | Who |
| --- | --- | --- |
| Suspected account misuse | Have the account disabled, which ends access within 5 minutes, and the person's PingFederate sign-in ended; the account stays disabled for 8 hours unless every key in the key rings is revoked (\<Procedures\>, PRO-AC-4) | Security officer, through \<Organisation\>'s service desk |
| Exposed password or second factor | Report it to \<Organisation\>'s service desk and the security officer at once. The account is disabled before the password or factor is reset, as a password change alone does not end a \<System Name\> sign-in, and stays disabled for 8 hours (\<Procedures\>, PRO-IA-3) | Whoever finds it; security officer, through \<Organisation\>'s service desk |
| Exposed service secret or key | Report it to the security officer; its owner changes it at once: the Windows server administrator for the key store's secrets and the key rings, revoking every key in an exposed key ring, and the database administrator for the backup encryption certificate (\<Procedures\>, PRO-IA-4 and PRO-SC-3; \<Incident Response Management\>, section 3.9) | Whoever finds it; Windows server administrator; database administrator |
| Access to data someone should not see | Stop, and report to the security officer | Whoever finds it |
| Personal data breach | Report to the security officer at once. The security officer tells the legal adviser, who decides on telling the ICO within 72 hours of becoming aware and the people affected, and records every breach (\<Incident Response Management\>, section 3.8) | Whoever finds it; security officer; legal adviser |
| Lost or stolen device | Report to the service desk and security officer; \<Organisation\> locks or wipes it | Whoever loses it |
| Supplier compromise or advisory | Assess the effect on \<System Name\>, and report to the security officer; tell \<Organisation\>'s security contact | Developers, security officer |
| Audit or service failure | Report to the security officer | Administrator |
| Suspected malware or attack | Report to the security officer, who tells \<Organisation\>'s security contact | Whoever finds it |

1. **Report:** tell the security officer within 1 hour. The security officer tells \<Organisation\>'s security contact of every confirmed incident, and any supplier whose product or service is involved. If personal data may be involved, the security officer tells the legal adviser at once.
2. **Contain:** limit the harm, for example by disabling accounts, which \<System Name\> refuses within 5 minutes, preserving the evidence first (step 3; \<Procedures\>, PRO-IR-6).
3. **Preserve:** keep logs and evidence, and do not clean up first.
4. **Investigate:** establish what happened, when, and what data was involved.
5. **Recover:** fix the cause and restore normal service (section 4.6).
6. **Learn:** record the incident on TPL-10; the security officer updates the plan and training, and the system owner \<Risk List\> and \<Plan of Action and Milestones\> (\<Procedures\>, PRO-IR-7).

The full plan is \<Incident Response Management\>, and the procedures are in \<Procedures\> (IR).

## 5 Exceptions

Some rules allow an exception, such as access from abroad (A41), removable media (A32), an outside service or AI tool (A45), or working away from home (A38). Any other rule may be excepted only where the risk is accepted.

1. The person asks on TPL-17, giving the rule, the reason, the period and any compensating measure.
2. The security officer assesses the risk. The system owner approves or refuses in writing. An exception above the system owner's authority goes to the authorising official.
3. Every exception has an end date no more than 12 months away, and ends then unless it is renewed.
4. Approved exceptions are entered in the exception register and in \<Risk List\> where they leave a risk. They are reviewed at each access review (C34).
5. Nobody may act on an exception before it is approved.

## 6 Contacts

Who holds each role, and their phone number and email, are in \<Roles and Responsibilities\>, section 6.

**Table 4: Contacts**

| For | Who |
| --- | --- |
| Reporting incidents, and questions on these rules | The security officer |
| When the security officer is away | The security officer's deputy (\<Roles and Responsibilities\>, Table 4) |
| Exceptions, and decisions on access | The system owner |
| Personal data, breaches and requests from individuals | The legal adviser |
| Access to a schema, or to a role in \<System Name\> | The schema's Data Owner; the system owner, for a role |
| Devices, VPN, lost devices and passwords for the network | \<Organisation\>'s IT service desk |
| \<Organisation\>'s security team | \<Organisation\>'s security contact and their deputy |

## 7 Definitions

**Table 5: Definitions**

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

Table 6 shows where each control that these SyOps serve is met. It lets an auditor test from the control to the rule or duty, or the other way.

**Table 6: Controls and where they are met**

| Control | Rules and duties |
| --- | --- |
| PL-4 Rules of Behavior | Sections 1, 2, 3 and 9; A55; C23, C35 |
| PL-4(1) Social Media and External Site Use | A25, A43, A44, A45 |
| PL-2, PL-8 Plans and Architecture | C35 |
| AC-2 Account Management | A9; B5, B7; C3, C9, C15, C19, C36; section 4.4 |
| AC-5 Separation of Duties | B6, B8 |
| AC-6 Least Privilege, with AC-6(2) and AC-6(9) | A17; B2, B3, B10; C3, C16 |
| AC-7 Unsuccessful Logon Attempts | A14; C3 |
| AC-8 System Use Notification | A6, A7, A8 |
| AC-2(5) Inactivity Logout, AC-11 Device Lock, AC-12 Session Termination | A36 |
| AC-17 Remote Access | A15, A39, A40; B20, B23; section 4.7 |
| AC-18, AC-19 Wireless Access and Mobile Devices | A35, A40 |
| AC-20, AC-20(2) External Systems and Portable Storage | A31, A32, A35, A45 |
| AC-21 Information Sharing | A22, A25 |
| AT-2, AT-3, AT-4 Training | A54; B1; C22 |
| AU-6, AU-9 Audit Review and Protection | B12; C3, C4, C5, C12, C16, C46; section 4.2 |
| CA-2, CA-2(1) Control Assessments and Independent Assessors | C54 |
| CA-3, CA-9 Information Exchange and Internal Connections | C25 |
| CA-5, CA-7 POA&M and Continuous Monitoring | C13, C14, C17 |
| CA-6 Authorization | C55, C56 |
| CA-7(1) Independent Assessment | C57 |
| CM-2, CM-6, CM-8, CM-12 Baseline, Settings, Inventory and Information Location | C47, C59 |
| CM-2(7) High-risk Travel | A41 |
| CM-3, CM-4, CM-5 Change Control | B13, B14, B15; C37, C38, C58; section 4.5 |
| CM-7(1), CM-7(5), CM-10, CM-11 Least Functionality, Authorised Software, Licences and User-installed Software | A47, A48, A49; B17; C24, C60 |
| CP-2, CP-4, CP-9, CP-10 Contingency | C2, C6, C8, C18, C21, C61; section 4.6 |
| IA-2, IA-5, IA-12 Authentication | A9 to A15; B4, B9, B19; C20, C62; section 4.9 |
| IR-4, IR-5, IR-6 Incidents | A29, A42, A50 to A53; B22; C43; section 4.9 |
| MA-1 to MA-6 Maintenance | B15, B20, B21; C11, C28, C41, C48; sections 4.6 and 4.7 |
| MP-2 to MP-7 Media | A28, A30 to A35; C42, C49; section 4.8 |
| PE-5, PE-17 Output Devices and Alternate Work Site | A33, A35 to A42; C30 |
| PE-6, PE-11 Physical incidents and loss of power | A42; sections 4.6 and 4.9 |
| PS-2, PS-6 Risk Designations and Access Agreements | C23, C31; section 9 |
| PS-4, PS-5 Leavers and Movers | B5; C36; section 4.4 |
| PS-8 Personnel Sanctions | A4 |
| PT-2, PT-3, SI-12, SI-18 Personal Data | A23 to A28; C32, C33, C44 |
| RA-2, RA-3, RA-3(1), RA-7, RA-9 Risk, Supply Chain and Critical Components | C26, C63, C64 |
| RA-5, SI-2, SI-5 Vulnerabilities and Advisories | C7, C10, C11, C37, C50; section 4.3 |
| SA-9, SR-6 External Services and Suppliers | C26 |
| SA-2, SA-5, SA-22 Resources, Guides and Unsupported Components | C11, C27, C65 |
| SA-10, SA-11, SA-15 Developer Change Control, Testing and Tools | B19; C11, C27, C40, C51 |
| SC-12 Key Management | B19; C20 |
| SC-7, SC-17 Boundary and Certificates | C25, C39, C52 |
| SC-8, SC-13, SC-18, SC-28 Transport, Cryptography, Page Code and Data at Rest | B19; C39, C40, C52, C53 |
| SI-3, SI-4, SI-7 Malicious Code, Monitoring and Integrity | C1, C4, C12; section 4.6 |

## 9 Acknowledgement

Everyone signs Part A, and privileged users also sign Part B, before getting access, every 12 months and after a material change to these rules (A55). Electronic signature is accepted. Each signature is recorded on TPL-21, and the system owner keeps the register of signatures in \<Planning Management\>, section 3.5, for as long as the person has access and for 3 years after.

**Part A.** I have read and understood Part A of \<Security Operating Procedures\>, version \<ver\>. I agree to follow it, I consent to the monitoring described in rules A6 to A8, and I confirm that I remain bound by \<Organisation\>'s confidentiality agreement.

**Part B.** I have read and understood Part B of \<Security Operating Procedures\>, version \<ver\>, and I agree to follow it as well as Part A.
