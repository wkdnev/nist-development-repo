# \<System Name\> Provider Evidence Request and Responsibility Matrix

## 1 Purpose

\<System Name\> depends on \<Organisation\> for its network, devices, hosting and staff processes. NIST SP 800-37 Rev 2 expects the plan to show which parts of a control the provider delivers, and the provider's own details must be available. This document lists the evidence needed and who is responsible for what. Cyber Essentials Plus supports these claims, but it is a different scheme and does not prove a NIST control, so each request asks for the specific service and evidence.

Evidence is enough when it names the service, shows that it covers the two \<System Name\> VMs or the relevant users, is current, and comes from someone accountable for the service. A verbal assurance or a general policy statement is recorded but is not enough on its own.

Status values are **Not sent**, **Sent**, **Received**, **Accepted**, **Rejected** and **Not needed**.

Requests are numbered EV-XX-nn, where XX is the family code. A request in section 2 is reused wherever it already answers the need, so that \<Organisation\> is not asked twice.

**Table 1: Family coverage**

| Family | Section | State |
| --- | --- | --- |
| AC Access Control | 4 | Drafted, not sent |
| AT Awareness and Training | 5 | Drafted, not sent |
| AU Audit and Accountability | 6 | Drafted, not sent |
| CA Assessment, Authorization and Monitoring | 7 | Drafted, not sent |
| CM Configuration Management | 8 | Drafted, not sent |
| CP Contingency Planning | 9 | Drafted, not sent |
| IA Identification and Authentication | 10 | Drafted, not sent |
| IR Incident Response | 11 | Drafted, not sent |
| MA Maintenance | 12 | Drafted, not sent |
| MP Media Protection | 13 | Drafted, not sent |
| PE Physical and Environmental Protection | 14 | Drafted, not sent |
| PL Planning | 15 | Drafted, not sent |
| PM Program Management (outside the baseline; inherited) | 16 | Drafted, not sent |
| PS Personnel Security | 17 | Drafted, not sent |
| PT Personally Identifiable Information | 18 | Drafted, not sent |
| RA Risk Assessment | 19 | Drafted, not sent |
| SA System and Services Acquisition | 20 | Drafted, not sent |
| SC System and Communications Protection | 21 | Drafted, not sent |
| SI System and Information Integrity | 22 | Drafted, not sent |
| SR Supply Chain Risk Management | 23 | Drafted, not sent |

### 1.2 Covering request

The requests go to \<Organisation\> as one pack, with this covering note. The pack has not yet been sent.

1. **To:** \[Name\], \<Organisation\>'s security contact, with \[Name\] as deputy.
2. **From:** \[Name\], system owner.
3. **Date sent:** \[Date\].
4. **Reply needed by:** \[Date\]. The records and the list of applicable policies promised on 6 November 2026 are due by 20 November 2026 (section 23).
5. **What is asked:** the 74 requests in sections 2 to 22. Each has an ID, what is needed and the evidence that is acceptable.
6. **How to reply:** for each request ID, give the document or record, its date and its owner, or say that none exists. One reply can answer several requests.
7. **Where to send it:** \[The restricted records location\].
8. **How it is used:** each reply is recorded against its request here. A finding changes only when the evidence is accepted.
9. **Why it matters:** 306 determination statements wait on evidence that is not yet available, and all 61 inherited controls rest on these replies.

## 2 Cross-family requests

**Table 2: Cross-family requests**

| ID | What is needed | Acceptable evidence | Status | Received | Reference |
| --- | --- | --- | --- | --- | --- |
| EV-GEN-01 | \[Name\] is the security contact; \[Name\] is the deputy | Name, role and contact details | Not sent |  |  |
| EV-GEN-02 | Cyber Essentials Plus status and scope | Current certificate, with a statement of whether the scope includes the two VMs and their hosting | Not sent |  |  |
| EV-GEN-03 | The VM hosting service | Service description, who administers the hypervisor and physical hosts, and where they are | Not sent |  |  |
| EV-GEN-04 | The \<Organisation\> policies that apply to \<System Name\> | A list with owners and versions, and copies of the relevant sections | Not sent |  |  |
| EV-GEN-05 | Any NIST-based control statements \<Organisation\> already holds | Existing common control or responsibility documents, or confirmation that none exists | Not sent |  |  |

## 3 Access Control (AC)

### 3.1 Evidence requests

**Table 3: AC evidence requests**

| ID | Controls | What is needed | Acceptable evidence | Status | Received | Reference |
| --- | --- | --- | --- | --- | --- | --- |
| EV-AC-01 | AC-2h, AC-2l, AC-2(13) | How Active Directory accounts are created, changed and disabled for starters, movers and leavers, and how quickly; who owns each \<System Name\> AD group and how a change to its members is recorded; and how \<System Name\>'s system owner is told about leavers, movers and high-risk individuals | Process document; the Starters/Leavers prompt and ServiceNow workflow set up for \<System Name\>; proof that corporate network accounts are disabled immediately, and that \<System Name\> cannot be reached without one | Not sent |  |  |
| EV-AC-02 | AC-2, AC-6(5) | How Windows administrator accounts on the VMs are created, approved and removed | Process, and the group membership for the VMs once built | Not sent |  |  |
| EV-AC-03 | AC-4 | Firewall and network controls for flows F1 to F7, and how changes are approved | Rule set or export for the VMs; change process | Not sent |  |  |
| EV-AC-04 | AC-6(1) | Who holds security functions on the network, hypervisor and firmware | Named roles and access lists | Not sent |  |  |
| EV-AC-05 | AC-7 | Windows logon lockout settings on the VMs | Group policy report or settings export | Not sent |  |  |
| EV-AC-06 | AC-8 | Windows logon banner on the VMs | Group policy report and a screenshot | Not sent |  |  |
| EV-AC-07 | AC-11, AC-11(1) | Screen lock on workstations and servers, and that it hides the display | Group policy or device management settings | Not sent |  |  |
| EV-AC-08 | AC-17 | The remote access service: its name, usage restrictions, connection requirements, guidance and authorisation route | Service description and policy | Not sent |  |  |
| EV-AC-09 | AC-17(1) | Automated monitoring and control of remote access | Tool name, sample log or report | Not sent |  |  |
| EV-AC-10 | AC-17(2) | Encryption of remote access sessions | Configuration showing the protocol and cipher settings | Not sent |  |  |
| EV-AC-11 | AC-17(3) | Remote access routed through managed access points | Network diagram and gateway list | Not sent |  |  |
| EV-AC-12 | AC-17(4) | Whether the VMs' administration ports can be reached from external networks, and the approved administration route | Firewall rules and a written confirmation | Not sent |  |  |
| EV-AC-13 | AC-18, AC-18(1) | Wireless network requirements, authorisation, authentication and encryption | Wireless policy and configuration | Not sent |  |  |
| EV-AC-14 | AC-18(3) | That the VMs and standard builds have wireless disabled when not needed | Build standard; check on the built VMs | Not sent |  |  |
| EV-AC-15 | AC-19, AC-19(5) | Mobile device rules and encryption, and whether a phone or tablet could reach \<System Name\> | Mobile policy; device management settings | Not sent |  |  |
| EV-AC-16 | AC-20 | How unmanaged or personal devices are prevented from reaching internal systems | Network access control or policy, with its enforcement | Not sent |  |  |
| EV-AC-17 | AC-20(2) | USB and portable storage controls | Device control settings or policy | Not sent |  |  |

### 3.2 Responsibility matrix

This matrix is proposed and has not been agreed with \<Organisation\>.

**Table 4: AC responsibility matrix**

| Control | \<System Name\> application | Organisation (system owner and role holders) | \<Organisation\> | Request |
| --- | --- | --- | --- | --- |
| AC-1 | None | Policy, procedures and review | Coordination on inherited controls | EV-GEN-04 |
| AC-2 | Account functions | Approval, review and role holders | Leaver and mover notice; Windows accounts | EV-AC-01, EV-AC-02 |
| AC-2(1) | Automated functions | Manual procedures where none exist | None | None |
| AC-2(2) | None | Prohibition and periodic check | None | None |
| AC-2(3) | Disable function | PRO-AC-3, PRO-AC-4 and PRO-AC-8 | Leaver notice | EV-AC-01 |
| AC-2(4) | Audit records | Reviewing them | None | None |
| AC-2(5) | Idle sign-out | Setting the value | Server sessions | EV-AC-05 |
| AC-2(13) | Disable function | PRO-AC-4 | Reporting a significant risk | EV-AC-01 |
| AC-3 | Access enforcement | Approving access | Windows and network permissions | EV-AC-02, EV-AC-03 |
| AC-4 | Limits on its own connections | Approving the flows | Firewalls and network | EV-AC-03 |
| AC-5 | Role separation | Duties and staffing | Separation of its own administrators | EV-AC-04 |
| AC-6 | Roles and groups | Least-privilege decisions | VM and hosting privileges | EV-AC-02, EV-AC-04 |
| AC-6(1) | Application security functions | Who is authorised | Hardware, firmware, network and hosting functions | EV-AC-04 |
| AC-6(2) | None | Separate everyday accounts | None | None |
| AC-6(5) | Global administrator flag | Who holds privileged roles | Administrators it provides | EV-AC-02 |
| AC-6(7) | Assignment report | Carrying out the review | None | None |
| AC-6(9) | Audit records | Reviewing them | Server logging, if centralised | EV-AC-02 |
| AC-6(10) | Blocking ordinary users | List of privileged functions | Windows and network functions | EV-AC-04 |
| AC-7 | Lockout | Approving the values | Windows logon lockout | EV-AC-05 |
| AC-8 | Sign-in notice | Wording | Windows logon banner | EV-AC-06 |
| AC-11 | Browser lock | Setting the value | Device and server lock | EV-AC-07 |
| AC-11(1) | Lock overlay | None | Device lock screen | EV-AC-07 |
| AC-12 | Session ending | Approving the values | Server sessions | EV-AC-05 |
| AC-14 | Limits actions without sign-in | Approving the list | Anonymous access on the VMs | EV-AC-03 |
| AC-17 | None | Who may work remotely | Remote access service | EV-AC-08 |
| AC-17(1) | None | None | Monitoring and control | EV-AC-09 |
| AC-17(2) | HTTPS for its own traffic | None | Remote access encryption | EV-AC-10 |
| AC-17(3) | None | None | Managed access points | EV-AC-11 |
| AC-17(4) | None | Deciding whether it is allowed | Administration route | EV-AC-12 |
| AC-18 | None | None | Wireless controls | EV-AC-13 |
| AC-18(1) | None | None | Wireless controls | EV-AC-13 |
| AC-18(3) | None | None | VM and device builds | EV-AC-14 |
| AC-19 | None | Whether mobile use is allowed | Mobile controls | EV-AC-15 |
| AC-19(5) | None | None | Device encryption | EV-AC-15 |
| AC-20 | None | Terms and approvals | Device and network rules | EV-AC-16 |
| AC-20(1) | None | Approvals, if any are given | None | None |
| AC-20(2) | None | Rule | USB controls | EV-AC-17 |
| AC-21 | None | Sharing decisions | None | None |
| AC-22 | Requires sign-in | No-public-content decision | None | None |

## 4 Awareness and Training (AT)

**Table 5: AT evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-AT-01 | AT-2, AT-2(2), AT-2(3), AT-3, AT-4 | What \<Organisation\>'s security training covers, including privacy, insider threat and social engineering, how often it is taken, how it is updated, and who has completed it; and the role training \<Organisation\> gives its own administrators of the \<System Name\> servers, with its records | Training content showing the insider threat and social engineering parts, and sample completion records for users and administrators | Not sent |  |  |

## 5 Audit and Accountability (AU)

**Table 6: AU evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-AU-01 | AU-2, AU-6(1), AU-6(3) | Whether \<Organisation\> has central log monitoring, and what it needs from \<System Name\> and the VMs | Service description and scope | Not sent |  |  |
| EV-AU-02 | AU-8 | The time source for the VMs, and evidence that they stay within 1 second of UTC | Time service configuration | Not sent |  |  |
| EV-AU-03 | AU-4, AU-11 | Storage and backup for the VMs, to hold 12 months of records online and 12 months in an offline archive | Service description and backup schedule | Not sent |  |  |
| EV-AU-04 | AU-12 | Which Windows Server events are logged and kept on the VMs | Audit policy and a sample log | Not sent |  |  |
| EV-AU-05 | AU-2, AU-6, AU-6(3), AU-12 | Which AD FS and Active Directory events are logged for \<System Name\>: sign-in attempts, failed sign-ins, lockouts, and changes to \<System Name\>'s groups and their members. How long they are kept, and how \<System Name\>'s auditor receives them each week or on request | Audit settings, a sample record and the agreed route | Not sent |  |  |

## 6 Assessment, Authorization and Monitoring (CA)

**Table 7: CA evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-CA-01 | CA-6 | Who authorises the common controls \<System Name\> inherits | Name, and the authorisation record | Not sent |  |  |
| EV-CA-02 | CA-3, CA-6 | The agreements for the exchanges in \<Assessment, Authorization, and Monitoring Management\>, section 3.7: the hosting and services agreement covering AD FS and Active Directory, central logging, the time service and the backup site, and information exchange agreements for ServiceNow and the Starters/Leavers system | Each agreement, with its date and review date | Not sent | None | None |

## 7 Configuration Management (CM)

**Table 8: CM evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-CM-01 | CM-5 | Physical and logical restrictions on changing the VMs and hosting | Access lists and change process | Not sent |  |  |
| EV-CM-02 | CM-8(3), CM-12(1) | Tools that detect unauthorised components, and any that locate information | Tool names, and a sample report | Not sent |  |  |
| EV-CM-03 | CM-10 | Licences for the software on the VMs and hosting, and peer-to-peer controls. \<System Name\>'s own components are recorded in \<Configuration Management\>, section 3.5 | Licence record and policy | Not sent |  |  |

## 8 Contingency Planning (CP)

**Table 9: CP evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-CP-01 | CP-6, CP-6(1), CP-6(3), CP-7, CP-7(1), CP-7(2), CP-7(3) | Whether a second site is available and separate from the main one, with room for 14 daily, 8 weekly and 12 monthly encrypted backups and one offline or immutable copy (\<Contingency Planning Management\>, section 3.8), whether it can hold encrypted backups and run rebuilt VMs with equivalent controls, how it is reached in a wide-area failure, and what priority of service applies. Also \<Organisation\>'s disaster recovery and business continuity plans: who declares a disaster, and the recovery times of the network, AD FS, Active Directory, name resolution and time, on which \<System Name\>'s 72 hours depends | Site details, and the service agreement | Not sent |  |  |
| EV-CP-02 | CP-8, CP-8(1), CP-8(2) | What alternate telecommunications exist, what priority of service applies, and whether main and alternate services share a single point of failure | Service agreements | Not sent |  |  |

## 9 Identification and Authentication (IA)

**Table 10: IA evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-IA-01 | IA-3, IA-5h | How devices are identified on \<Organisation\>'s network, and how they protect credentials | Network access control description and build standard | Not sent |  |  |
| EV-IA-02 | IA-12, IA-12(2), IA-12(3), IA-12(5) | What identity evidence HR collects and checks in pre-employment checks, for staff and contractors, and how people are told | HR process and a blank record | Not sent |  |  |
| EV-IA-03 | IA-7 | Whether the VMs use validated cryptographic modules | Build standard and settings | Not sent |  |  |
| EV-IA-04 | IA-2(1), IA-2(2), IA-2(8) | How AD FS signs users in to \<System Name\>: the multi-factor methods it requires, its lockout and password standard, how the token is signed, and that it carries the user's Active Directory groups. Also the trust settings for \<System Name\>: the federation protocol, the life of a token, what it carries, how the signing certificate is renewed, and whether the settings meet federation assurance level 2 of NIST SP 800-63C | Service description; the relying party settings for \<System Name\>; the password and lockout policy | Not sent |  |  |

## 10 Incident Response (IR)

**Table 11: IR evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-IR-01 | IR-3(2), IR-4, IR-6, IR-6(3), IR-7, IR-7(1) | \<Organisation\>'s incident process, how the security contact takes reports from \<System Name\>, and what help it gives: monitoring, forensic help, isolating a server, disabling an account, and locking or wiping a device. How it is reached outside working hours. How soon it tells \<System Name\> of a compromise on its side; 24 hours is asked. Who speaks to the press. Whether it will take part in the yearly exercise. Also confirmation, with its date, that the old AD FS secret found in the source repositories has been revoked (INC-2026-001) | The process, and the contact route | Not sent |  |  |

## 11 Maintenance (MA)

**Table 12: MA evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-MA-01 | MA-2, MA-3(3), MA-5, MA-6 | How hardware and the hypervisor are maintained, how equipment is sanitised before it leaves, with sanitising certificates, and whether support and parts for the hardware and hypervisor arrive within 24 hours (D-MA-P02). How its engineers are screened. Whether it tells the system owner before work on the hosts, AD FS, Active Directory, the network, the time service or the backup store that affects \<System Name\> | Maintenance process, and the service agreement | Not sent |  |  |
| EV-MA-02 | MA-4 | The tool and protocol used over the managed route (route R1 in \<Maintenance Management\>), whether it uses multi-factor sign-in, what each session logs, whether sessions and connections end when finished, and the firewall rule that limits the admin portal to the route (PA-83) | Route settings and sample logs | Not sent |  |  |

## 12 Media Protection (MP)

**Table 13: MP evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-MP-01 | MP-2, MP-4, MP-5 | Who can reach disks and backup media, where they are stored, and how they are protected, tracked and carried in transport. Where the offline audit archive and the copy of the secrets are held. What lockable storage and cross-cut shredders its offices provide for printouts | Media handling process, and sample transport records | Not sent |  |  |
| EV-MP-02 | MP-6 | How disks and backup media are sanitised, whether it follows NIST SP 800-88 Revision 2 and IEEE 2883-2022, how virtual disks are erased when a VM is removed, and how each action is verified | Process, and a sample certificate | Not sent |  |  |
| EV-MP-03 | MP-4, MP-6, MP-7 | How USB and portable storage are blocked on users' devices, that no USB device is passed through to the VMs, how exceptions work, and that users' devices are disk-encrypted. How print jobs are held, released and cleared on its managed printers, and how a printer's storage is sanitised | Device control settings | Not sent |  |  |

## 13 Physical and Environmental Protection (PE)

**Table 14: PE evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-PE-01 | PE-2, PE-3, PE-4, PE-6, PE-6(1), PE-8 | Who can enter the data centre, how entry is controlled and logged, how visitors, keys and lines are managed, how access is monitored, and how incidents reach \<System Name\>'s security officer. Also confirm the values in \<Physical and Environmental Protection Management\>. First choice of evidence: \<Organisation\>'s ISO/IEC 27001 certificate, Statement of Applicability and latest audit findings for Annex A.7, or a SOC 2 report covering physical access (CC6.4) and the availability criteria (A1.2), for both the main data centre and the second site (\<Physical and Environmental Protection Management\>, section 3.3). How soon the security contact tells \<System Name\>'s security officer of a physical incident; 24 hours is asked. The name, address and facilities contact of each site | Physical security policy, and audit or certification report | Not sent |  |  |
| EV-PE-02 | PE-9, PE-10, PE-11, PE-12 | How power is protected, whether there is an emergency shutoff, whether backup power allows an orderly shutdown, and what emergency lighting exists, and how the shutoff is guarded against accidental or unauthorised use. How long the backup power lasts, and how \<System Name\>'s administrators are warned that a site is on backup power | Facilities description, and maintenance records | Not sent |  |  |
| EV-PE-03 | PE-13, PE-13(1), PE-14, PE-15 | What fire detection and suppression exist, who they notify, what temperature and humidity levels apply, how they are monitored, and how water damage is prevented | Facilities description, and maintenance records | Not sent |  |  |
| EV-PE-04 | PE-16 | How hardware and media are authorised and recorded when entering or leaving | Process, and sample records | Not sent |  |  |
| EV-PE-05 | PE-5, PE-17 | What office controls protect printers and screens, which managed printers have secure (pull) print release, and what controls apply to managed devices and the route at home | Office security rules, and remote working policy | Not sent |  |  |

## 14 Planning (PL)

**Table 15: PL evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-PL-01 | PL-2, PL-8, PM-7, PM-7(1) | Whether \<Organisation\> has an enterprise architecture that \<System Name\>'s plan must fit; and whether \<Organisation\> runs the VM hypervisor, and whether it is inside the Cyber Essentials Plus scope (D-PL-11) | The relevant architecture standards; the hypervisor's owner and the CE+ scope statement | Not sent |  |  |

## 15 Program Management (PM)

PM is outside \<System Name\>'s baseline (TR-PM-01), but \<System Name\> inherits PM controls as common controls. These requests ask \<Organisation\> to show the programme exists. The full list of PM controls and what relies on each is in \<Program Management\>, section 3.3 (D-PM-02).

**Table 16: PM evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-PM-01 | PM-1, PM-2, PM-3, PM-8, PM-9, PM-11, PM-12, PM-13, PM-15, PM-16, PM-16(1), PM-28, PM-29, PM-32 | Whether \<Organisation\> has an information security programme plan, a risk management strategy with a stated risk appetite, and named programme leaders. Who the senior accountable official for risk management is (PM-29). First choice of evidence: \<Organisation\>'s ISO/IEC 27001 certificate, with its scope statement and Statement of Applicability, showing that the services \<System Name\> uses are within scope | The programme plan, risk management strategy and risk appetite statement, and the roles that lead them | Not sent |  |  |
| EV-PM-02 | PM-5, PM-5(1) | Whether \<System Name\> is in \<Organisation\>'s system inventory, and its HR personal data in a personal data inventory or record of processing | The inventory entries for \<System Name\>, and the record of processing (UK GDPR, Article 30) | Not sent |  |  |
| EV-PM-03 | PM-6, PM-10, PM-14, PM-30, PM-31 | How \<Organisation\> authorises systems, tests and monitors them, measures performance, and manages supply chain risk | The authorisation process, continuous monitoring strategy, supply chain risk management strategy and performance measures | Not sent |  |  |
| EV-PM-04 | PM-18 to PM-23, PM-20(1), PM-25 to PM-27 | Whether \<Organisation\> has a privacy programme, who leads it, and whether a data protection officer is appointed | The privacy programme plan, the data protection officer's name or the reason none is required, and the complaint and reporting processes | Not sent |  |  |

## 16 Personnel Security (PS)

**Table 17: PS evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-PS-01 | PS-2, PS-3 | What pre-employment screening is done, against what standard, whether it covers identity, right to work, employment history and a basic criminal record check (\<Personnel Security Management\>, section 3.3), whether it is repeated, and when | Screening policy or standard, and confirmation, with the date only, for each person with \<System Name\> access | Not sent |  |  |
| EV-PS-02 | PS-4, PS-6, PS-8, PS-9 | How exit interviews, returned equipment and disciplinary action work, and whether job descriptions refer to security duties. A copy of the confidentiality agreement each person signs, and when it is signed | HR processes, and sample job descriptions | Not sent |  |  |
| EV-PS-03 | PS-7 | What contracts require of external people, and how suppliers report leavers and movers, and, if the independent assessment team are not \<Organisation\>'s staff, the terms of their engagement | Standard contract terms | Not sent |  |  |

## 17 Personally Identifiable Information (PT)

**Table 18: PT evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-PT-01 | PT-3, PT-5 | Whether the employee privacy notice names \<System Name\> and its purposes, how people get it, and how often it is reviewed | The notice, and how it is given to employees | Not sent |  |  |
| EV-PT-02 | PE-8(3) | What personal data visitor records hold | A blank visitor record | Not sent |  |  |

## 18 Risk Assessment (RA)

**Table 19: RA evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-RA-01 | RA-3, RA-5(11) | Agreement to use the security contact for vulnerability reports about \<System Name\>, and whether \<Organisation\> offers a shared scanning service or a list of exploited flaws it tracks. How organisational risk feeds into system risk is asked in EV-PM-01. Where the security contact is published, and its terms: that research in good faith is authorised, how long a reporter is asked to wait for a fix before disclosing (\<System Name\> proposes 90 days, D-RA-14), and that indefinite secrecy is not required (NIST RA-5(11)). Whether findings that may affect \<Organisation\>'s other systems should be sent to the security contact (RA-5e) | Risk statement, and written agreement; the published contact and its terms | Not sent |  |  |

## 19 System and Services Acquisition (SA)

**Table 20: SA evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-SA-01 | SA-4 | What the standard contract says about security and privacy requirements, documentation, responsibilities and acceptance | Standard contract terms | Not sent |  |  |
| EV-SA-02 | SA-9, SA-9(2) | What controls \<Organisation\>'s hosting, network, ServiceNow, AD FS, Active Directory and Starters/Leavers services use, and which functions, ports, protocols and services they rely on. \<System Name\> relies on them for running, changes, sign-in and access (D-AC-22, D-AC-23). The service levels for each, how they are measured, and the remedies when they are missed | Service descriptions, and a list of ports and services | Not sent |  |  |
| EV-SA-03 | SA-9, SA-9(2) | What security controls GitHub applies to private repositories, and what plan and settings \<System Name\>'s account has (branch protection, alerts and secret scanning depend on the plan) | GitHub's published security and compliance reports, and the account's plan and settings | Not sent |  |  |

## 20 System and Communications Protection (SC)

**Table 21: SC evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-SC-01 | SC-5, SC-10 | Denial-of-service protection, and network session disconnect | Service description and settings | Not sent |  |  |
| EV-SC-02 | SC-7, SC-7(3), SC-7(4) | Managed interfaces, external connections, flow policy and exceptions | Network diagram, rule set and exception list; the address ranges and ports needed to complete the host firewall allow-lists in \<System and Communications Protection Management\>, section 3.2 | Not sent |  |  |
| EV-SC-03 | SC-7(7), SC-7(8) | Split tunnelling, and the authenticated proxy for the VMs | VPN and proxy configuration | Not sent |  |  |
| EV-SC-04 | SC-17 | The certificate policy and trust anchors | Certificate policy and trust store list; the certificate authority's chain, the key types and lifetimes it issues (ECDSA P-256 or RSA 2048 with SHA-256 needed), and how to request and revoke a certificate | Not sent |  |  |
| EV-SC-05 | SC-20, SC-21, SC-22 | DNS authentication, integrity, fault tolerance and role separation | DNS service description and settings | Not sent |  |  |

## 21 System and Information Integrity (SI)

**Table 22: SI evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-SI-01 | SI-4, SI-4(2), SI-4(4) | Network monitoring, its criteria, and how it is reported; whether central logging can receive \<System Name\>'s audit and Windows logs, and how they are sent (\<System and Information Integrity Management\>, section 3.4). Since sign-in is through AD FS, whether AD FS failed sign-in events and changes to \<System Name\>'s AD administrator groups can be sent to the security officer, for detection use cases U1 and U4 (\<System and Information Integrity Management\>, section 3.4) | Service description and a sample report; the central logging connection details | Not sent |  |  |
| EV-SI-02 | SI-2, SI-7, SI-7(1) | Firmware updates and integrity checks for the VM hosting | Process and a sample record | Not sent |  |  |
| EV-SI-03 | SI-5 | Whether \<Organisation\> is registered for the NCSC Early Warning service and receives CISA or NCSC alerts for its networks, and how alerts that affect \<System Name\> reach the security officer (\<System and Information Integrity Management\>, section 3.3) | Registration confirmation and the forwarding route | Not sent |  |  |

## 22 Supply Chain Risk Management (SR)

**Table 23: SR evidence requests**

| ID | Control | What we need to know | Evidence to provide | Status | Received | Result |
| --- | --- | --- | --- | --- | --- | --- |
| EV-SR-01 | SR-2(1), SR-3, SR-6, SR-8 | Who the approved suppliers are, and how they report a compromise; confirmation that the IT service desk sits on \<System Name\>'s supply chain team and will take part in the yearly supplier review (\<Supply Chain Risk Management\>, section 3.5); the contract term for reporting a compromise to the security officer within 24 hours | The approved supplier list, and notification terms | Not sent |  |  |
| EV-SR-02 | SR-10, SR-11(1), SR-11(2), SR-12 | How hardware is inspected, how buyers are trained, how equipment is controlled during repair, and how it is disposed of | Procedures, a training record and a sample disposal record | Not sent |  |  |

## 23 Answers given on 6 November 2026

\[Name\] and \[Name\] agreed these proposed answers in a meeting, as reported by the system owner. Several began as best guesses. They are statements, not evidence, so findings do not change until the records arrive. \[Name\] is to send the records and the list of applicable policies by 20 November 2026. These replace the "Not sent" status above.

**Table 24: \<Organisation\>'s stated answers**

| Requests | Answer stated |
| --- | --- |
| EV-GEN-02 | Cyber Essentials Plus is held, and the VMs get added to scope when built |
| EV-GEN-03 | \<Organisation\>'s own UK virtual platform, run by its infrastructure team |
| EV-GEN-05 | No NIST-based control statements exist |
| EV-AC-01 | Corporate accounts are disabled immediately for leavers, and \<System Name\> cannot be reached without one |
| EV-AC-02 | Windows administrator accounts are requested through ServiceNow, approved by the system owner and held in a named group |
| EV-AC-03, EV-AC-04 | \<Organisation\>'s network and infrastructure teams hold firewalls and security functions, with changes through its change process |
| EV-AC-05 to 07 | Group policy sets the approved lockout, banner and screen lock values, and screen locks hide the display |
| EV-AC-08 to 11 | \<Organisation\>'s VPN with MFA, encrypted, logged and monitored, through one managed gateway |
| EV-AC-12 | Administration ports are blocked from external networks |
| EV-AC-13, EV-AC-14 | Corporate wireless authenticates users and devices with encryption, and is disabled on the VMs |
| EV-AC-15 to 17 | Mobile devices are managed and cannot reach \<System Name\>, unmanaged devices are blocked, and USB is blocked unless approved |
| EV-AU-01 | \<Organisation\>'s central service takes the Windows and PostgreSQL logs |
| EV-AU-02 | \<Organisation\>'s domain controllers provide time |
| EV-AU-03 | Storage is sized for 12 months of records, with daily backups |
| EV-AU-04 | Group policy sets the Windows audit policy, and logs are kept for 12 months |
| EV-IA-01 | Network access control with device certificates, and disk encryption on managed devices |
| EV-IA-02 | Photo ID and right-to-work checks for staff, and the same through the agency for contractors |
| EV-IA-03 | Standard Windows modules, not in FIPS mode |
| EV-IA-04 | \\\[Expected answer to be confirmed with \<Organisation\>\\\] |
