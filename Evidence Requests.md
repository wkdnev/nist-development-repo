# \<System Name\> Provider Evidence Request and Responsibility Matrix

## 1 Purpose

\<System Name\> depends on \<Organisation\> for its network, devices, hosting and staff processes. CSS expects the plan to show which parts of a control the provider delivers, and the provider's own details must be available. This document lists the evidence needed and who is responsible for what. Cyber Essentials Plus supports these claims, but it is a different scheme and does not prove a CSS control, so each request asks for the specific service and evidence.

Evidence is enough when it names the service, shows that it covers the two \<System Name\> VMs or the relevant users, is current, and comes from someone accountable for the service. A verbal assurance or a general policy statement is recorded but is not enough on its own.

Requests are numbered EV-XX-nn, where XX is the family code. A request in section 2 is reused wherever it already answers the need, so that \<Organisation\> is not asked twice.

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
| PM Program Management (outside the baseline; inherited) | 15 |
| PS Personnel Security | 16 |
| PT Personally Identifiable Information | 17 |
| RA Risk Assessment | 18 |
| SA System and Services Acquisition | 19 |
| SC System and Communications Protection | 20 |
| SI System and Information Integrity | 21 |
| SR Supply Chain Risk Management | 22 |

### 1.2 Covering request

The requests go to \<Organisation\> as one pack, with this covering note.

1. **To:** \[Name\], \<Organisation\>'s security contact, with \[Name\] as deputy.
2. **From:** \[Name\], system owner.
3. **Date sent:** \[Date\].
4. **Reply needed by:** \[Date\].
5. **What is asked:** the requests in sections 2 to 22. Each has an ID, what is needed and the evidence that is acceptable.
6. **How to reply:** for each request ID, give the document or record, its date and its owner, or say that none exists. One reply can answer several requests.
7. **Where to send it:** \[The restricted records location\].
8. **How it is used:** each reply is recorded against its request. An assessment result changes only when the evidence is accepted.
9. **Why it matters:** the inherited controls, and the determination statements that depend on \<Organisation\>, rest on these replies.

## 2 Cross-family requests

**Table 2: Cross-family requests**

| ID | What is needed | Acceptable evidence |
| --- | --- | --- |
| EV-GEN-01 | \[Name\] is the security contact; \[Name\] is the deputy | Name, role and contact details |
| EV-GEN-02 | Cyber Essentials Plus status and scope | Current certificate, with a statement of whether the scope includes the two VMs and their hosting |
| EV-GEN-03 | The VM hosting service | Service description, who administers the hypervisor and physical hosts, and where they are |
| EV-GEN-04 | The \<Organisation\> policies that apply to \<System Name\> | A list with owners and versions, and copies of the relevant sections |
| EV-GEN-05 | Any CSS-based control statements \<Organisation\> already holds | Existing common control or responsibility documents, or confirmation that none exists |

## 3 Access Control (AC)

### 3.1 Evidence requests

**Table 3: AC evidence requests**

| ID | Controls | What is needed | Acceptable evidence |
| --- | --- | --- | --- |
| EV-AC-01 | AC-2h, AC-2l, AC-2(13) | How Active Directory accounts are created, changed and disabled for starters, movers and leavers, and how quickly; who owns each \<System Name\> AD group (the system owner owns the five role groups, \<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners and \<Code\>\_LegalSearch, and each Data Owner owns their schema's read and edit groups) and how a change to its members is recorded; and how \<System Name\>'s system owner is told about leavers, movers and high-risk individuals; confirmation that Active Directory accounts unused for 90 days are disabled within 1 working day (\<System Description\>, P-38) | Process document; the starters and leavers prompt and ServiceNow workflow set up for \<System Name\>; proof that corporate network accounts are disabled immediately, and that \<System Name\> cannot be reached without one |
| EV-AC-02 | AC-2, AC-6(5) | How Windows administrator accounts on the VMs, and SQL Server administrator logins on the database server, are created, approved and removed | Process, and the group membership for the VMs and SQL Server once built |
| EV-AC-03 | AC-4 | Firewall and network controls for flows F1 to F8, F10 and F11 in \<System Description\>, section 6.5, and how changes are approved. F10 runs from the application server only to \<Organisation\>'s PingFederate over HTTPS, TCP 443; F11 runs from server and database administrators' managed devices to both servers, only over the managed administration route. F9 is carried by people and has no network connection to \<System Name\> | Rule set or export for the VMs; change process |
| EV-AC-04 | AC-6(1) | Who holds security functions on the network, hypervisor and firmware | Named roles and access lists |
| EV-AC-05 | AC-7 | Windows logon lockout settings on the VMs | Group policy report or settings export |
| EV-AC-06 | AC-8 | Windows logon banner on the VMs | Group policy report and a screenshot |
| EV-AC-07 | AC-11, AC-11(1) | Screen lock on workstations and servers after 15 minutes without activity (\<System Description\>, P-03), or \<Organisation\>'s setting if different, and that it hides the display. \<System Name\> has no page lock of its own | Group policy or device management settings |
| EV-AC-08 | AC-17 | The remote access service: its name, usage restrictions, connection requirements, guidance and authorisation route | Service description and policy |
| EV-AC-09 | AC-17(1) | Automated monitoring and control of remote access | Tool name, sample log or report |
| EV-AC-10 | AC-17(2) | Encryption of remote access sessions | Configuration showing the protocol and cipher settings |
| EV-AC-11 | AC-17(3) | Remote access routed through managed access points | Network diagram and gateway list |
| EV-AC-12 | AC-17(4) | That the VMs' administration ports cannot be reached from external networks except through the VPN and then the approved administration route (flow F11 in \<System Description\>, section 6.5), with multi-factor authentication at both and named accounts; and how VPN and administration route connections are logged, so that privileged remote access can be matched to its change or incident record (\<System Description\>, P-54) | Firewall rules and a written confirmation |
| EV-AC-13 | AC-18, AC-18(1) | Wireless network requirements, authorisation, authentication and encryption | Wireless policy and configuration |
| EV-AC-14 | AC-18(3) | That the VMs and standard builds have wireless disabled when not needed | Build standard; check on the built VMs |
| EV-AC-15 | AC-19, AC-19(5) | That managed laptops are the only mobile devices that can reach \<System Name\>, that they are encrypted with BitLocker full-device encryption, and that a phone, tablet or unmanaged device cannot reach it (\<System Description\>, P-47) | Mobile policy; device management settings |
| EV-AC-16 | AC-20 | How unmanaged or personal devices are prevented from reaching internal systems | Network access control or policy, with its enforcement |
| EV-AC-17 | AC-20(2) | USB and portable storage controls | Device control settings or policy |

### 3.2 Responsibility matrix

This matrix is proposed to \<Organisation\>.

**Table 4: AC responsibility matrix**

| Control | \<System Name\> application | Organisation (system owner and role holders) | \<Organisation\> | Request |
| --- | --- | --- | --- | --- |
| AC-1 | None | Policy, procedures and review | Coordination on inherited controls | EV-GEN-04 |
| AC-2 | No accounts of its own: roles and schema access from Active Directory groups, read by the API over LDAPS | Data Owners' approval in ServiceNow, group reviews and role holders | Active Directory accounts and groups; leaver and mover notice; Windows accounts | EV-AC-01, EV-AC-02 |
| AC-2(1) | Group and account-state lookup on every request, held for at most 5 minutes; last sign-in report (FR-085) | Manual procedures where none exist | Active Directory and the ServiceNow workflow | EV-AC-01 |
| AC-2(2) | None | Prohibition and periodic check | None | None |
| AC-2(3) | Refuses a disabled AD account within 5 minutes; last sign-in report (FR-085) | PRO-AC-3, PRO-AC-4 and PRO-AC-8; the security officer's monthly check | Disabling the AD account, and unused accounts after 90 days (P-38); leaver notice | EV-AC-01 |
| AC-2(4) | Audit records | Reviewing them | None | None |
| AC-2(5) | Sign out (FR-084), ending the cookie and the PingFederate sign-in | The sign-out rule (P-53) | Device screen lock; PingFederate sign-out | EV-AC-07, EV-IA-04 |
| AC-2(13) | Refuses a disabled AD account within 5 minutes, even while a sign-in is open | PRO-AC-4 | Reporting a significant risk; disabling the AD account | EV-AC-01 |
| AC-3 | Access enforcement by role and schema on every request | Data Owners authorise access in ServiceNow | Windows and network permissions | EV-AC-02, EV-AC-03 |
| AC-4 | Limits on its own connections | Approving the flows | Firewalls and network | EV-AC-03 |
| AC-5 | Role separation | Duties and staffing | Separation of its own administrators | EV-AC-04 |
| AC-6 | Roles and groups | Least-privilege decisions | VM and hosting privileges | EV-AC-02, EV-AC-04 |
| AC-6(1) | Application security functions | Who is authorised | Hardware, firmware, network and hosting functions | EV-AC-04 |
| AC-6(2) | None | Separate everyday accounts | None | None |
| AC-6(5) | Administrator role from the \<Code\>\_Admins group | Who holds privileged roles | Administrators it provides | EV-AC-02 |
| AC-6(7) | Assignment report | Carrying out the review | None | None |
| AC-6(9) | Audit records | Reviewing them | Server logging, if centralised | EV-AC-02 |
| AC-6(10) | Blocking ordinary users | List of privileged functions | Windows and network functions | EV-AC-04 |
| AC-7 | None: no sign-in of its own to lock | Approving the values (P-42) | PingFederate and Active Directory lockout; Windows logon lockout | EV-AC-05, EV-IA-04 |
| AC-8 | Sign-in notice, accepted before anything else is shown | Wording, approved by the legal adviser | Windows logon banner; any PingFederate banner | EV-AC-06, EV-IA-04 |
| AC-11 | None: no page lock of its own | Setting the value (P-03) | Device and server lock | EV-AC-07 |
| AC-11(1) | None | None | Device lock screen | EV-AC-07 |
| AC-12 | The authentication cookie ends 8 hours after sign-in; an open page re-checks every 5 minutes (P-02, NFR-102) | Approving the values | PingFederate sign-in lifetime, at least as long as P-02 | EV-IA-04 |
| AC-14 | Limits actions without sign-in | Approving the list | Anonymous access on the VMs | EV-AC-03 |
| AC-17 | None | Who may work remotely | Remote access service | EV-AC-08 |
| AC-17(1) | None | None | Monitoring and control | EV-AC-09 |
| AC-17(2) | HTTPS for its own traffic | None | Remote access encryption | EV-AC-10 |
| AC-17(3) | None | None | Managed access points | EV-AC-11 |
| AC-17(4) | Audits privileged functions in the Admin application | Defined needs and their records (P-54) | VPN and administration route, with multi-factor authentication and logging | EV-AC-12 |
| AC-18 | None | None | Wireless controls | EV-AC-13 |
| AC-18(1) | None | None | Wireless controls | EV-AC-13 |
| AC-18(3) | None | None | VM and device builds | EV-AC-14 |
| AC-19 | None | Managed laptops only (P-47) | Mobile device management | EV-AC-15 |
| AC-19(5) | None | None | Device encryption | EV-AC-15 |
| AC-20 | None | Terms and approvals | Device and network rules | EV-AC-16 |
| AC-20(1) | None | Approvals, if any are given | None | None |
| AC-20(2) | None | Rule | USB controls | EV-AC-17 |
| AC-21 | Schema groups | Sharing decisions (TPL-25) | None | None |
| AC-22 | Requires sign-in | No-public-content decision | None | None |

## 4 Awareness and Training (AT)

**Table 5: AT evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-AT-01 | AT-2, AT-2(2), AT-2(3), AT-3, AT-4 | What \<Organisation\>'s security training covers, including privacy, insider threat and social engineering, how often it is taken, how it is updated, and who has completed it; and the role training \<Organisation\> gives its own administrators of the \<System Name\> servers, with its records | Training content showing the insider threat and social engineering parts, and sample completion records for users and administrators |
| EV-AT-02 | AT-3 | The security and privacy training \<Organisation\> gives the Head of Cyber and the data protection officer for their roles, and how often | The course or programme each has completed, with dates |

## 5 Audit and Accountability (AU)

**Table 6: AU evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-AU-01 | AU-2, AU-6(1), AU-6(3) | Whether \<Organisation\> has central log monitoring, and what it needs from \<System Name\> and the VMs, including the short security events the API writes to its application log for the alert use cases U5, U6 and U9, and SQL Server Audit records of reads of the item tables by logins other than the API's; that central logging keeps each of these for at least 12 months and lets the security officer export them each month for the offline archive (P-07), and that nobody in \<System Name\>'s team can change or delete them there; and how the auditor and security officer are given read access to the Windows, SQL Server and application logs there, without a sign-in to the servers | Service description and scope |
| EV-AU-02 | AU-8 | The time source for the VMs, and evidence that they stay within 1 second of UTC | Time service configuration |
| EV-AU-03 | AU-4, AU-11 | Storage and backup for the VMs, to hold 12 months of records online and 12 months in an offline archive | Service description and backup schedule |
| EV-AU-04 | AU-12 | Which Windows Server events are logged and kept on the VMs | Audit policy and a sample log |
| EV-AU-05 | AU-2, AU-6, AU-6(3), AU-12 | Which PingFederate and Active Directory events are logged for \<System Name\>: sign-in attempts, failed sign-ins, lockouts, and changes to \<System Name\>'s groups and their members. How long they are kept, and how \<System Name\>'s auditor receives them each week or on request | Audit settings, a sample record and the agreed route |

## 6 Assessment, Authorization and Monitoring (CA)

**Table 7: CA evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-CA-01 | CA-6 | Who authorises the common controls \<System Name\> inherits | Name, and the authorisation record |
| EV-CA-02 | CA-3 | The agreement for each exchange in \<Assessment, Authorization, and Monitoring Management\>, Table 6: the owner of PingFederate and Active Directory, central logging, the time service, the backup site and the authenticated proxy each confirms and signs that service's row. A hosting and services agreement, if one exists, is welcome as support. ServiceNow and the starters and leavers process have no connection to \<System Name\> (flow F9), so nothing is asked for them | Each agreement, with its date and review date |

## 7 Configuration Management (CM)

**Table 8: CM evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-CM-01 | CM-5 | Physical and logical restrictions on changing the VMs and hosting | Access lists and change process |
| EV-CM-02 | CM-8(3), CM-12(1) | Tools that detect unauthorised components, and any that locate information | Tool names, and a sample report |
| EV-CM-03 | CM-10 | Licences for the software on the VMs and hosting, and peer-to-peer controls. \<System Name\>'s own components are recorded in \<Configuration Management\>, section 3.5 | Licence record and policy |

## 8 Contingency Planning (CP)

**Table 9: CP evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-CP-01 | CP-6, CP-6(1), CP-6(3), CP-7, CP-7(1), CP-7(2), CP-7(3) | Whether a second site is available and separate from the main one, with room for 14 daily, 8 weekly and 12 monthly encrypted backups and one offline or immutable copy (\<Contingency Planning Management\>, section 3.8), whether it can hold encrypted backups and run rebuilt VMs with equivalent controls, how it is reached in a wide-area failure, and what priority of service applies. Also \<Organisation\>'s disaster recovery and business continuity plans: who declares a disaster, and the recovery times of the network, PingFederate, Active Directory, name resolution and time, on which \<System Name\>'s 72 hours depends | Site details, and the service agreement |
| EV-CP-02 | CP-8, CP-8(1), CP-8(2) | What alternate telecommunications exist, what priority of service applies, and whether main and alternate services share a single point of failure | Service agreements |

## 9 Identification and Authentication (IA)

**Table 10: IA evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-IA-01 | IA-3, IA-5h | How devices are identified on \<Organisation\>'s network, and how they protect credentials | Network access control description and build standard |
| EV-IA-02 | IA-12, IA-12(2), IA-12(3), IA-12(5) | What identity evidence HR collects and checks in pre-employment checks, for staff and contractors, and how people are told | HR process and a blank record |
| EV-IA-03 | IA-7 | Whether the VMs use validated cryptographic modules | Build standard and settings |
| EV-IA-04 | IA-2(1), IA-2(2), IA-2(8) | How PingFederate signs users in to \<System Name\>: the multi-factor methods it requires, its lockout and password standard, and how its OpenID Connect response is signed. Also the settings of \<System Name\>'s PingFederate connection: the OpenID Connect client settings, the sign-in lifetime, which must be at least as long as \<System Name\>'s own 8-hour session (\<System Description\>, P-02), whether PingFederate's sign-out endpoint is enabled for \<System Name\>'s Sign out (FR-084), whether PingFederate shows its own system use banner and its wording, confirmation of the lockout setting in P-42 (10 failed attempts in 15 minutes, locked for 15 minutes), how the application server alone reaches PingFederate to fetch its OpenID Connect metadata and signing certificate and to complete each sign-in (flow F10, HTTPS, TCP 443), what the response carries (it names the person and carries no groups), how the signing certificate is renewed, and whether the settings meet federation assurance level 2 of CSS | Service description; the OpenID Connect client settings for \<System Name\>; the password and lockout policy |
| EV-IA-05 | IA-2, IA-9, AC-3, SC-8 | How \<System Name\>'s API reads group membership from Active Directory over LDAPS (flow F7, TCP 636): the domain controllers it may query, their certificates and the chain that validates them, and the read-only rights of the API's group managed service account | Directory connection settings, the certificate chain, and the service account's rights |

## 10 Incident Response (IR)

**Table 11: IR evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-IR-01 | IR-3(2), IR-4, IR-6, IR-6(3), IR-7, IR-7(1) | \<Organisation\>'s incident process, how the security contact takes reports from \<System Name\>, and what help it gives: monitoring, forensic help, isolating a server, disabling an account, and locking or wiping a device. How it is reached outside working hours. How soon it tells \<System Name\> of a compromise on its side; 24 hours is asked. Who speaks to the press. Whether it will take part in the yearly exercise. | The process, and the contact route |

## 11 Maintenance (MA)

**Table 12: MA evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-MA-01 | MA-2, MA-3(3), MA-5, MA-6 | How hardware and the hypervisor are maintained, how equipment is sanitised before it leaves, with sanitising certificates, and whether support and parts for the hardware and hypervisor arrive within 24 hours. How its engineers are screened. Whether it tells the system owner before work on the hosts, PingFederate, Active Directory, the network, the time service or the backup store that affects \<System Name\> | Maintenance process, and the service agreement |
| EV-MA-02 | MA-4 | The tool and protocol used over the managed route (route R1 in \<Maintenance Management\>), whether it uses multi-factor sign-in, what each session logs, whether sessions and connections end when finished, and the firewall rule that limits the Admin application to the route | Route settings and sample logs |

## 12 Media Protection (MP)

**Table 13: MP evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-MP-01 | MP-2, MP-4, MP-5 | Who can reach disks and backup media, where they are stored, and how they are protected, tracked and carried in transport. Where the offline audit archive and the copy of the secrets are held. What lockable storage and cross-cut shredders its offices provide for printouts | Media handling process, and sample transport records |
| EV-MP-02 | MP-6 | How disks and backup media are sanitised, whether it follows CSS and IEEE 2883-2022, how virtual disks are erased when a VM is removed, and how each action is verified | Process, and a sample certificate |
| EV-MP-03 | MP-4, MP-6, MP-7 | How USB and portable storage are blocked on users' devices, that no USB device is passed through to the VMs, how exceptions work, and that users' devices are disk-encrypted. How print jobs are held, released and cleared on its managed printers, and how a printer's storage is sanitised | Device control settings |

## 13 Physical and Environmental Protection (PE)

**Table 14: PE evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-PE-01 | PE-2, PE-3, PE-4, PE-6, PE-6(1), PE-8 | Who can enter the data centre, how entry is controlled and logged, how visitors, keys and lines are managed, how access is monitored, and how incidents reach \<System Name\>'s security officer. Also confirm the values in \<Physical and Environmental Protection Management\>. First choice of evidence: \<Organisation\>'s ISO/IEC 27001 certificate, Statement of Applicability and latest audit findings for Annex A.7, or a SOC 2 report covering physical access (CC6.4) and the availability criteria (A1.2), for both the main data centre and the second site (\<Physical and Environmental Protection Management\>, section 3.3). How soon the security contact tells \<System Name\>'s security officer of a physical incident; 24 hours is asked. The name, address and facilities contact of each site | Physical security policy, and audit or certification report |
| EV-PE-02 | PE-9, PE-10, PE-11, PE-12 | How power is protected, whether there is an emergency shutoff, whether backup power allows an orderly shutdown, and what emergency lighting exists, and how the shutoff is guarded against accidental or unauthorised use. How long the backup power lasts, and how \<System Name\>'s administrators are warned that a site is on backup power | Facilities description, and maintenance records |
| EV-PE-03 | PE-13, PE-13(1), PE-14, PE-15 | What fire detection and suppression exist, who they notify, what temperature and humidity levels apply, how they are monitored, and how water damage is prevented | Facilities description, and maintenance records |
| EV-PE-04 | PE-16 | How hardware and media are authorised and recorded when entering or leaving | Process, and sample records |
| EV-PE-05 | PE-5, PE-17 | What office controls protect printers and screens, which managed printers have secure (pull) print release, and what controls apply to managed devices and the route at home | Office security rules, and remote working policy |

## 14 Planning (PL)

**Table 15: PL evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-PL-01 | PL-2, PL-8, PM-7, PM-7(1) | Whether \<Organisation\> has an enterprise architecture that \<System Name\>'s plan must fit; and whether \<Organisation\> runs the VM hypervisor, and whether it is inside the Cyber Essentials Plus scope | The relevant architecture standards; the hypervisor's owner and the CE+ scope statement |

## 15 Program Management (PM)

PM is outside \<System Name\>'s baseline (TR-PM-01), but \<System Name\> inherits PM controls as common controls. These requests ask \<Organisation\> to show the programme exists. The full list of PM controls and what relies on each is in \<Program Management\>, section 3.3.

**Table 16: PM evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-PM-01 | PM-1, PM-2, PM-3, PM-8, PM-9, PM-11, PM-12, PM-13, PM-15, PM-16, PM-16(1), PM-28, PM-29, PM-32 | Whether \<Organisation\> has an information security programme plan, a risk management strategy with a stated risk appetite, and named programme leaders. Who the senior accountable official for risk management is (PM-29). First choice of evidence: \<Organisation\>'s ISO/IEC 27001 certificate, with its scope statement and Statement of Applicability, showing that the services \<System Name\> uses are within scope | The programme plan, risk management strategy and risk appetite statement, and the roles that lead them |
| EV-PM-02 | PM-5, PM-5(1) | Whether \<System Name\> is in \<Organisation\>'s system inventory, and its personal data in a personal data inventory or record of processing | The inventory entries for \<System Name\>, and the record of processing (UK GDPR, Article 30) |
| EV-PM-03 | PM-6, PM-10, PM-14, PM-30, PM-31 | How \<Organisation\> authorises systems, tests and monitors them, measures performance, and manages supply chain risk | The authorisation process, continuous monitoring strategy, supply chain risk management strategy and performance measures |
| EV-PM-04 | PM-18 to PM-23, PM-20(1), PM-25 to PM-27 | Whether \<Organisation\> has a privacy programme, who leads it, and whether a data protection officer is appointed | The privacy programme plan, the data protection officer's name or the reason none is required, and the complaint and reporting processes |

## 16 Personnel Security (PS)

**Table 17: PS evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-PS-01 | PS-2, PS-3 | What pre-employment screening is done, against what standard, whether it covers identity, right to work, employment history and a basic criminal record check (\<Personnel Security Management\>, section 3.3), whether it is repeated, and when | Screening policy or standard, and confirmation, with the date only, for each person with \<System Name\> access |
| EV-PS-02 | PS-4, PS-6, PS-8, PS-9 | How exit interviews, returned equipment and disciplinary action work, and whether job descriptions refer to security duties. A copy of the confidentiality agreement each person signs, and when it is signed | HR processes, and sample job descriptions |
| EV-PS-03 | PS-7 | What contracts require of external people, and how suppliers report leavers and movers, and, if the independent assessment team are not \<Organisation\>'s staff, the terms of their engagement | Standard contract terms |

## 17 Personally Identifiable Information (PT)

**Table 18: PT evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-PT-01 | PT-3, PT-5 | Whether the employee privacy notice names \<System Name\> and its purposes, how people get it, and how often it is reviewed | The notice, and how it is given to employees |
| EV-PT-02 | PE-8(3) | What personal data visitor records hold | A blank visitor record |

## 18 Risk Assessment (RA)

**Table 19: RA evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-RA-01 | RA-3, RA-5(11) | Agreement to use the security contact for vulnerability reports about \<System Name\>, and whether \<Organisation\> offers a shared scanning service or a list of exploited flaws it tracks. How organisational risk feeds into system risk is asked in EV-PM-01. Where the security contact is published, and its terms: that research in good faith is authorised, how long a reporter is asked to wait for a fix before disclosing (\<System Name\> proposes 90 days), and that indefinite secrecy is not required (CSS RA-5(11)). Whether findings that may affect \<Organisation\>'s other systems should be sent to the security contact (RA-5e) | Risk statement, and written agreement; the published contact and its terms |

## 19 System and Services Acquisition (SA)

**Table 20: SA evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-SA-01 | SA-4 | What the standard contract says about security and privacy requirements, documentation, responsibilities and acceptance | Standard contract terms |
| EV-SA-02 | SA-9, SA-9(2) | What controls \<Organisation\>'s hosting, network, ServiceNow, PingFederate, Active Directory and starters and leavers services use, and which functions, ports, protocols and services they rely on. \<System Name\> relies on them for running, changes, sign-in and access. The service levels for each, how they are measured, and the remedies when they are missed | Service descriptions, and a list of ports and services |
| EV-SA-03 | SA-9, SA-9(2) | What security controls the source repository service provided under the corporate SDLC applies to private repositories, and what settings \<System Name\>'s repositories have (protected branches, alerts and secret scanning) | The service's published security and compliance reports, and the repositories' settings |
| EV-SA-04 | SA-3, SA-8, SA-11, SA-15, SR-3 | \<Organisation\>'s corporate SDLC, which \<System Name\> is built under and inherits: how it provides threat modelling, a second developer's review through a protected branch, a pipeline with automated tests and package, code and secret scans, releases from a signed tag with recorded checksums, one checked package feed with lock files, and a software bill of materials for each release (\<System Description\>, section 7.12) | The SDLC standard, and the records it produces for a sample release |

## 20 System and Communications Protection (SC)

**Table 21: SC evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-SC-01 | SC-5, SC-10 | Denial-of-service protection, and network session disconnect | Service description and settings |
| EV-SC-02 | SC-7, SC-7(3), SC-7(4) | Managed interfaces, external connections, flow policy and exceptions | Network diagram, rule set and exception list; the address ranges and ports needed to complete the host firewall allow-lists in \<System and Communications Protection Management\>, section 3.2 |
| EV-SC-03 | SC-7(7), SC-7(8) | Split tunnelling, and the authenticated proxy for the VMs | VPN and proxy configuration |
| EV-SC-04 | SC-17 | The certificate policy and trust anchors | Certificate policy and trust store list; the certificate authority's chain, the key types and lifetimes it issues (ECDSA P-256 or RSA 2048 with SHA-256 needed), and how to request and revoke a certificate |
| EV-SC-05 | SC-20, SC-21, SC-22 | DNS authentication, integrity, fault tolerance and role separation | DNS service description and settings |

## 21 System and Information Integrity (SI)

**Table 22: SI evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-SI-01 | SI-4, SI-4(2), SI-4(4) | Network monitoring, its criteria, and how it is reported; whether central logging can receive \<System Name\>'s application, Windows and SQL Server logs and the audit events that raise alerts, and how they are sent (\<System and Information Integrity Management\>, section 3.4). Since sign-in is through PingFederate, whether PingFederate failed sign-in events and changes to \<System Name\>'s administrators' group (\<Code\>\_Admins) can be sent to the security officer, for detection use cases U1 and U4; and whether the application security events for U5, U6 and U9 can raise alerts (\<System and Information Integrity Management\>, section 3.4) | Service description and a sample report; the central logging connection details |
| EV-SI-02 | SI-2, SI-7, SI-7(1) | Firmware updates and integrity checks for the VM hosting | Process and a sample record |
| EV-SI-03 | SI-5 | Whether \<Organisation\> is registered for the NCSC Early Warning service and receives CISA or NCSC alerts for its networks, and how alerts that affect \<System Name\> reach the security officer (\<System and Information Integrity Management\>, section 3.3) | Registration confirmation and the forwarding route |

## 22 Supply Chain Risk Management (SR)

**Table 23: SR evidence requests**

| ID | Control | What we need to know | Evidence to provide |
| --- | --- | --- | --- |
| EV-SR-01 | SR-2(1), SR-3, SR-6, SR-8 | Who the approved suppliers are, and how they report a compromise; confirmation that the IT service desk sits on \<System Name\>'s supply chain team and will take part in the yearly supplier review (\<Supply Chain Risk Management\>, section 3.5); the contract term for reporting a compromise to the security officer within 24 hours | The approved supplier list, and notification terms |
| EV-SR-02 | SR-10, SR-11(1), SR-11(2), SR-12 | How hardware is inspected, how buyers are trained, how equipment is controlled during repair, and how it is disposed of | Procedures, a training record and a sample disposal record |

## 23 Expected answers

The table records the answer \<Organisation\> is expected to give to a request, where one is known before the records arrive. An expected answer is a statement, not evidence, so assessment results do not change until the records arrive.

**Table 24: \<Organisation\>'s expected answers**

| Requests | Expected answer |
| --- | --- |
| \[EV-XX-nn\] | \[Expected answer\] |
