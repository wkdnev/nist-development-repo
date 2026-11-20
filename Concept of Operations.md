# \<System Name\> Concept of Operations

## 1 Purpose of this document

This document is used by every control family. It describes how \<System Name\> is intended to be used: why it exists, who uses it, the business processes it supports and how it works day to day. How it meets controls is in the SSP. The business details are proposals until the business owner confirms them.

## 2 Mission and purpose

\<System Name\> gives authorised people one place to find and read scanned and electronic documents, such as PDFs and TIFFs. Each project's documents are kept separate from the others.

Teams need one controlled place to keep scanned and electronic documents, so that the right people can find them quickly and others cannot see them. Keeping each project's documents separate lets one system serve several parts of the business.

The business and information owner is \[Name\] (\<Roles and Responsibilities\>). The benefits the business expects are still to be stated: \[Benefits expected, from the business owner\].

## 3 User communities

**Table 1: User communities**

| Community | What they do | Where |
| --- | --- | --- |
| Document readers | Search and read documents in their projects, and report bad files | UI application |
| Project editors | Readers' work, plus upload, bulk upload, bulk export and manage project documents | UI application |
| Administrators | Manage system settings | Admin portal |
| Global administrators | Manage projects and the AD groups each project uses, in every project | Admin portal and UI application |
| Auditors | Read audit logs | Admin portal |
| Security officers | Monitor security information | Admin portal |

## 4 Business workflows

A document normally moves through four stages: it is added to a project, found and read, corrected if something is wrong, and exported if it is needed elsewhere. The business processes \<System Name\> will support are still to be confirmed: \[Business processes, from the business owner\]. The sample data uses invoices, correspondence and HR projects.

**Table 2: Business workflows**

| Activity | Who | What happens |
| --- | --- | --- |
| Find and read a document | Reader | Chooses a project, searches by title, author, number or date, and opens the document on screen |
| Add documents | Editor | Uploads files one at a time or in bulk, with details such as title and author |
| Report a bad file | Reader, editor | Flags a corrupt or wrong document so it can be corrected |
| Export a project's documents | Editor | Downloads a set of documents for approved use elsewhere |
| Start a new person | The person, their line manager, the group's owner | The person requests access, their line manager approves it and the owner authorises it, then the owner adds the person to the project's or role's Active Directory group. \<System Name\> creates no account (D-AC-23) |
| Remove a leaver | \<Organisation\>, the group owners | \<Organisation\> disables the person's Active Directory account at once, which ends their access, and the group owners remove their group memberships within 5 working days |
| Check activity | Auditor | Reviews who did what |

## 5 Operational scenarios

**Table 3: Operational scenarios**

| Scenario | Situation | What happens |
| --- | --- | --- |
| Answering a query | A reader needs a past document | They sign in, choose their project, search and read it on screen |
| Adding a batch | An editor has a set of newly scanned documents | They bulk upload them to the project with their details, and readers can then find them |
| A poor scan | A reader finds a page is unreadable | They report a bad file, and an editor corrects it and updates the report |
| A request for documents | Someone needs a project's documents elsewhere | The project access approver decides, and an editor exports them as a download |
| Wrong project | A user opens a project they are not approved for | \<System Name\> refuses, and they request access, which their line manager approves and the project's owner authorises |
| Forgotten password or lockout | A user cannot sign in | \<Organisation\>'s IT service desk resets the Active Directory password or releases the lock, after checking who they are |
| Leaving a desk | A user walks away while signed in | The device's screen lock hides the screen after the inactivity time \<Organisation\> sets (P-AC-15). The sign-in lasts no longer than PingFederate's sign-in lifetime (P-AC-10) |
| A new starter or a leaver | Staff change | Access is requested and approved for a starter, and removed for a leaver |

## 6 Operational concepts

### 6.1 Where it runs

It is not in production. It will run on the corporate network of \<Organisation\>, on an application server VM and a separate database server VM, both Windows Server 2025, with each application running as a Windows service (D-PL-10). The current development stack runs in Docker on one PC with sample data.

### 6.2 How access works day to day

1. A person signs in through \<Organisation\>'s single sign-on, PingFederate, with multi-factor authentication (D-AC-23). \<System Name\> has no password of its own.
2. \<System Name\> takes their roles and project access from their Active Directory groups.
3. Their group memberships decide which projects they see. Each project names a read group and an edit group.
4. \<System Name\> has no sessions of its own. The sign-in is held only in the application's authentication cookie and lasts no longer than PingFederate's sign-in lifetime (P-AC-10). An unattended screen is locked by the operating system on \<Organisation\>'s managed devices (P-AC-15).

### 6.3 Modes of operation

**Table 4: Modes of operation**

| Mode | What happens |
| --- | --- |
| Normal | Everyone can work as usual |
| PingFederate down | Nobody can sign in, because \<Organisation\>'s PingFederate authenticates every user. People already signed in carry on until their sign-in ends at PingFederate's sign-in lifetime |
| API down | Nobody can work, because both apps reach the documents only through API |
| Database down | API cannot read any data, so it refuses every request and nobody can open a document. People stay signed in |
| Maintenance | Users cannot reach \<System Name\>; there is no notice page explaining why. Users get 2 working days' notice of planned maintenance, and a maintenance page is recommended (REC-53) |

These modes come from reading the design. They have not been exercised.

### 6.4 How it is kept secure in operation

None of this has started, as \<System Name\> is not live. Table 5 says in brief how each part of operation is kept secure. The time limits, frequencies and other values are in the document named, so that the set does not repeat them.

**Table 5: Keeping \<System Name\> secure in operation**

| Activity | In brief | Held in |
| --- | --- | --- |
| Changes | Approved by the change control board, after a security impact analysis and a review by a second developer. The running system is checked against the approved baseline | \<Configuration Management\> |
| Patches and vulnerabilities | The system is scanned regularly, and flaws are fixed within time limits set by their severity | \<Risk Assessment Management\>, section 3.6 |
| Malicious code and monitoring | Microsoft Defender runs on both VMs and uploads are scanned. Audit records and logs are reviewed, and detection use cases alert the security officer | \<System and Information Integrity Management\>, section 3.4; \<Security Operating Procedures\>, section 4 |
| Encryption | TLS on every flow, encrypted disks and backups, and a register of keys. Not yet built (PA-18, PA-52, PA-93) | \<System and Communications Protection Management\> |
| Backups and recovery | Encrypted backups, tested restores, and recovery within the objectives the business has set | \<Contingency Planning Management\> |
| Incidents and breaches | Reported to the security officer and handled by severity. The legal adviser decides whether to tell the ICO and the people affected | \<Incident Response Management\> |
| Training | Security training and a \<System Name\> briefing before access, repeated on a schedule, with role modules for those with special duties | \<Awareness and Training Management\> |
| Maintenance | Approved first, done by known people with approved tools, checked afterwards and recorded | \<Maintenance Management\> |
| Media and paper | Exports, downloads and printouts are limited, marked and removed. \<Organisation\> looks after disks and backup media | \<Media Protection Management\>; \<Security Operating Procedures\>, Part A |
| Buildings | \<Organisation\> protects the data centre and the second site, and its evidence is checked | \<Physical and Environmental Protection Management\> |
| People | Screened before access, bound by signed rules, and their access changed promptly when they move or leave | \<Personnel Security Management\>, section 3.6 |
| Personal data | Used only for HR administration and managing project documents. Requests and complaints go to the legal adviser, and the impact assessment is completed before production | \<Privacy Plan\>; \<Data Protection Impact Assessment\> |
| Building and buying | Changes follow the development lifecycle. Suppliers are approved, and packages are to arrive through the offline feed (PA-94) | \<System and Services Acquisition Management\>; \<Supply Chain Risk Management\> |
| Risk and authorisation | The risk list and plan of action are kept current, and the authorising official is kept informed. Authorisation is decided from the authorisation package | \<Assessment, Authorization, and Monitoring Management\>, section 3.5; \<Security Assessment Report\> |

\<System Name\> is not authorised. No production documents are held until multi-factor authentication through PingFederate is shown working (PA-95), or the acceptance of password-only sign-in ends on 6 May 2027.

## 7 Open questions

1. Which \<Organisation\> staff will use \<System Name\>, and from where? Still open: \[Teams and locations, from the business owner\].
2. Answered: \[Name\], as project access approver, decides who may read each project.
3. Which business processes will \<System Name\> support, and what are the expected benefits? Still open: see sections 2 and 4.
4. What hours must it be available, and how many users and documents are expected? Still open: \[Hours, and numbers of users and documents, from the business owner\].
