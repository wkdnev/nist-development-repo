# \<System Name\> System Description

## 1 Purpose, and how to use this document

This document describes the reference system that a series of \<Organisation\>'s internal digital library applications are designed and built to. It says what such an application is for, how it is built, what it runs on, how it is designed and what it must do, from a security standpoint. Every other document in the set is written against it. An application that follows this design starts with its security and privacy controls already designed, rather than added after it is built: that is what Secure by Design means here.

The document is written so that a person, or an AI assistant, can answer questions about the security of an application built on the reference system against CSS without the source code. Everything a reader needs is stated in plain words. No part of it points to code.

It is a summary. The detail of each control family is held once, in the design document named in section 9, and that document is the authority if the two ever differ. Each control has one line in \<System Security Plan\>, and \<Guide to the Document Set\> shows how the whole set fits together.

### 1.1 Placeholders

**Table 1: Placeholders used in this document**

| Placeholder | Meaning | Where it is set |
| --- | --- | --- |
| \<System Name\> | The name of the application the set is issued for | Section 3.1 |
| \<Organisation\> | The organisation that owns and operates the application and provides the services in section 10 | Section 3.1 |
| \<Document Name\> | Another document in the set, such as \<Access Control Management\> | \<Documentation Map\> |
| \<ver\> | A document's version, where a record cites one | The change record (\<Documentation Map\>, section 4.1) |
| \<Classification\> | The protective marking of the set | Section 3.1 |
| \<Code\> | The application's short code, used in component, service and group names | Section 3.1 |
| P-nn | A value the application confirms or changes, such as a retention period | Section 4 |
| AF-nnn | A function particular to one application | Section 3.5 |
| \[Text in square brackets\] | A fact that must be supplied for the application. Do not guess it | Where it appears |

### 1.2 How an application adopts the set

1. **Complete the application profile** in section 3: its name, purpose, owners, users, information types and its own functions.
2. **Confirm the parameters** in section 4. Keep the reference value, or record a different value with the reason.
3. **Check the family settings against the corporate values.** Each setting in the family design documents should match \<Organisation\>'s corporate value. Where one does not, change it in the family document.
4. **Record each departure** from the reference design in section 3.6, with the risk it brings and the control that answers it. A departure is decided by the system owner and recorded in \<Decision Register\>.
5. **Categorise the application** from its information types, under CSS. If it comes out above Moderate in any objective, the Moderate baseline in this set is not enough and the system owner must decide how to proceed before going further.
6. **Carry the profile into the set.** Replace the placeholders throughout, fill in the square brackets, and confirm each control in the family design documents.
7. **Build to the design, then assess.** The application is tested against the requirements in section 5, and any shortfall becomes an item in \<Plan of Action and Milestones\>.

### 1.3 Rules for anyone answering questions from this document, human or AI

1. **This is the design.** It states what an application built on the reference system must do. Whether a given application does it is shown by that application's assessment, in \<Security Assessment Report\> and \<Plan of Action and Milestones\>. Do not claim that any application meets a requirement because it is written here.
2. **Check the profile first.** An application may set a different parameter or record a departure in section 3. Where it has, that is the answer for that application.
3. **Say when something is not known.** Text in square brackets is a fact nobody has yet supplied. Do not guess it.
4. **Name the owner.** Where a requirement is met by \<Organisation\> and not by the application, say so; section 10 lists those services.

## 2 The reference system at a glance

**Table 2: Key facts**

| Fact | Reference value |
| --- | --- |
| What it is | An internal digital library: a browser-based application in which staff store, search and view digital items, such as scanned and electronic documents, kept apart in separate schemas. It holds Moderate-impact information, including personal data |
| Owner and operator | \<Organisation\>. Its system owner, authorising official and information owner are named in section 3.2 |
| Users | \<Organisation\>'s staff and contractors only. No external or public users |
| Exposure | Internal only. Reached by browser from \<Organisation\>'s network or its VPN, on managed devices. Not reachable from the internet |
| Applications | Three: the UI application for readers and editors, a separate Admin application, and an API that is the only route to the data, with a shared library built into all three |
| Database | Microsoft SQL Server 2022, holding every item, file, schema definition and audit record. Each schema is its own database schema |
| Hosting | Two Windows Server 2025 virtual servers in \<Organisation\>'s data centre: an application server and a database server. Each application runs as a Windows service under its own managed service account |
| Sign-in | \<Organisation\>'s PingFederate single sign-on service, with multi-factor authentication, against Active Directory. The application holds no accounts and no passwords, and has no session management of its own |
| Authorisation | Active Directory groups, read directly from Active Directory by the API: five role groups, and a read group and an edit group for each schema |
| Information held | The information types in section 3.4, and in every case sign-in identities and audit records |
| Security categorisation | Moderate: confidentiality Moderate, integrity Moderate, availability Low (CSS), unless the application profile sets otherwise (P-01) |
| Control baseline | CSS Moderate baseline, with the CSS privacy baseline, as tailored in \<Tailoring Register\>. Program Management is inherited from \<Organisation\> |
| Law | UK GDPR, the Data Protection Act 2018, the Data (Use and Access) Act 2025 and the Computer Misuse Act 1990 (P-31) |
| Development | Built in-house under \<Organisation\>'s corporate software development life cycle (SDLC) |

## 3 Application profile

This section is completed for each application built on the reference system. Until it is, every other section describes the reference system only.

### 3.1 Identity of the application

**Table 3: Application identity**

| Item | Value |
| --- | --- |
| Application name (\<System Name\>) | \[Name\] |
| Short code, used in component, service and group names (\<Code\>) | \[Code\] |
| Organisation (\<Organisation\>) | \[Organisation\] |
| Business purpose, in one sentence | \[Purpose\] |
| Business processes it supports | \[Processes\] |
| Classification of the document set (\<Classification\>) | \[Marking\] |
| Release this set describes | \[Release\] |

### 3.2 Owners and named roles

Who holds each role, and how to reach them, is in \<Roles and Responsibilities\>, so that names are filled in once.

**Table 4: Owners and named roles**

| Role | Responsible for |
| --- | --- |
| System owner | The application, its design and this document set |
| Authorising official | Accepting the risk of operating the application |
| Information owner | The information held, its categorisation and who may see it |
| Business owner | The business need, the requirements that are theirs to set, and retention |
| Security officer | Security monitoring, alerts and incident response |
| Legal adviser or data protection officer | Lawful basis, the impact assessment, people's requests and breach reporting |
| Data Owners | Authorising who may read or edit a schema, through the ServiceNow access approval workflow |

### 3.3 Who uses it

The reference system has the roles below. An application may rename a role, or leave one out where it has no use for it, and records that in section 3.6.

**Table 5: Users and roles**

| Role | What they do | Where | How the role is given |
| --- | --- | --- | --- |
| Reader | Searches and reads items in their schemas, and reports a fault | UI application | Member of the schema's read group |
| Editor | A reader's work, and creates, uploads, manages and exports the schema's items | UI application | Member of the schema's edit group. Edit includes read |
| Administrator | Manages schemas, which groups open each schema, and system settings. Can reach every schema | Admin application and UI application | Member of the administrators' group |
| Auditor | Reads and searches the audit log, and reviews it as P-08 sets. Holds no administration role | Admin application | Member of the auditors' group |
| Security officer | Reads security information, reviews alerts and the central logs, leads incident response. Does not read the audit log. Holds no administration role | Admin application | Member of the security group |
| Business owner | Approves the disposal of items due under the retention schedule (FR-074) | Admin application | Member of the business owners' group |
| Legal adviser's delegate | Searches every schema for one person's items to answer a request under data protection law (FR-073). Holds no other role | Admin application | Member of the legal search group, named by the legal adviser |
| Data Owner | Owns a schema's data and its two groups. Authorises who may read or edit it, in ServiceNow | ServiceNow and the directory | Named in section 3.2 and \<Roles and Responsibilities\> |
| Server and database administrators | Run the servers and the database. Need no application role | The servers, over \<Organisation\>'s managed administration route | Named accounts from \<Organisation\> |
| Developers | Build and fix the applications. Hold no administrator access on the servers | Development environment | Named in \<Roles and Responsibilities\> |

All role and schema groups are Active Directory groups. The system owner owns the five role groups, and each Data Owner owns their schema's two groups. Only a group's owner changes its members.

### 3.4 What information it holds

Each application lists the information it holds and rates each type under CSS. The application's categorisation is the highest rating in each column. The last row is held by every application built on the reference system.

**Table 6: Information types and impact**

| Information type | Personal data? | Confidentiality | Integrity | Availability |
| --- | --- | --- | --- | --- |
| \[Information type 1\] | \[Yes, including special category data / Yes / No\] | \[Rating\] | \[Rating\] | \[Rating\] |
| \[Information type 2\] | \[\] | \[Rating\] | \[Rating\] | \[Rating\] |
| Sign-in identities and audit records | Yes | Moderate | Moderate | Low |
| **The application, taking the highest of each** | | **\[Rating\]** | **\[Rating\]** | **\[Rating\]** |

The reference system is designed for Moderate confidentiality, Moderate integrity and Low availability. An application rated Low in any objective may keep the Moderate controls. An application rated High in any objective is outside this reference system (section 1.2, step 5).

### 3.5 Functions particular to the application

The functional requirements in section 5.1 are common to every application built on the reference system. The functions only this application has are listed here, numbered AF-001 onwards, in the same form. Each must name who may use it and the access check that guards it, and must be built from the common components: the same sign-in, schema access checks, input validation, audit and file handling.

**Table 7: Application functions**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| AF-001 | \[Function\] | \[Role\] | \[Which part does the work, where the data is held and where the access check is made\] |

A function that would break a statement in section 5.1.12, "What the application does not do", is a departure and goes in section 3.6.

### 3.6 Departures from the reference design

**Table 8: Departures**

| No. | Reference design | What this application does instead | Why | Risk, and the control that answers it | Decision |
| --- | --- | --- | --- | --- | --- |
| DEP-01 | \[Section and requirement\] | \[\] | \[\] | \[\] | \[Decision Register number\] |

An application with no departures says "None".

## 4 Parameters

These are the values the controls depend on. CSS calls many of them organisation-defined parameters. Each has a reference value that the design in this set is written to. An application keeps it or sets its own, and states the reason in the last column. A change to P-01 or to any time in P-12 to P-14 changes the categorisation or the contingency plan, and needs the authorising official's agreement.

**Table 9: Parameters**

| No. | Parameter | Reference value | Main controls | This application, and why |
| --- | --- | --- | --- | --- |
| P-01 | Security categorisation | Confidentiality Moderate, integrity Moderate, availability Low | RA-2 | \[\] |
| P-02 | Sign-in lifetime | \[As set in PingFederate for the application\]. The application has no session controls or idle sign-out of its own, so this is the only limit on how long a sign-in lasts | AC-2(5), AC-12 | \[\] |
| P-03 | Device screen lock after inactivity | \[As set on \<Organisation\>'s managed devices, for example 15 minutes\] | AC-11 | \[\] |
| P-04 | Review of role group members | Every 3 months | AC-2, AC-6(7) | \[\] |
| P-05 | Review of schema group members | Every 12 months | AC-2 | \[\] |
| P-06 | Leavers and movers | Leaver: Active Directory account disabled at once; group memberships removed within 5 working days. Mover: group owners told within 1 working day | AC-2, PS-4 | \[\] |
| P-07 | Audit record retention | 12 months online, then 12 months in an offline archive | AU-11 | \[\] |
| P-08 | Audit log review | Weekly | AU-6 | \[\] |
| P-09 | Clock accuracy | Within 1 second of UTC | AU-8 | \[\] |
| P-10 | Key and secret change | Application keys every 90 days; secrets every 12 months; at once if exposed | SC-12 | \[\] |
| P-11 | Flaw fixing | 3 days if exploited; 14 days Critical or High; 30 days Medium; 90 days Low | SI-2, RA-5 | \[\] |
| P-12 | Recovery time objective | 72 hours | CP-2, CP-10 | \[\] |
| P-13 | Recovery point objective | 24 hours | CP-9 | \[\] |
| P-14 | Maximum tolerable downtime | 120 hours | CP-2 | \[\] |
| P-15 | Backups kept | 14 daily, 8 weekly and 12 monthly; one copy at a second site and one offline or immutable | CP-9, CP-6 | \[\] |
| P-16 | Contingency tests | A restore every 6 months; a tabletop exercise every 12 months | CP-4 | \[\] |
| P-17 | Largest single upload, by role | 25, 50, 75 or 100 MB | SI-10 | \[\] |
| P-18 | Largest batch | 100 files and 500 MB | SI-10 | \[\] |
| P-19 | File types accepted | \[The types the application needs, from a fixed list\]. Reference: PDF, TIFF, JPEG and PNG | SI-10, CM-7 | \[\] |
| P-20 | Export working copies | Deleted once downloaded, and always within 24 hours | MP-6 | \[\] |
| P-21 | Incident reporting | A suspected incident reported within 1 hour; a personal data breach assessed for the regulator within 72 hours | IR-6 | \[\] |
| P-22 | Answer to a person's request about their data | Within one month | PT-2, PM-21 | \[\] |
| P-23 | Where data may be held | The United Kingdom only | SA-9(5) | \[\] |
| P-24 | Training | Before access, and every 12 months; role modules before privileged access | AT-2, AT-3 | \[\] |
| P-25 | Authorisation | Before real data is held, and reviewed at least every 12 months | CA-6 | \[\] |
| P-26 | Transport encryption | TLS 1.3 preferred; TLS 1.2 with AES-GCM allowed; HSTS for one year | SC-8, SC-13 | \[\] |
| P-27 | Events that raise an alert | The eight in section 7.10 | SI-4 | \[\] |
| P-28 | Application security verification standard | OWASP ASVS 5.0, Level 2 | SA-11 | \[\] |
| P-29 | Check of the running system against its baseline | Monthly, and at each release | CM-3, SI-7 | \[\] |
| P-30 | Vulnerability scanning | Servers monthly; packages and code at each release | RA-5 | \[\] |
| P-31 | Laws that apply | UK GDPR, the Data Protection Act 2018, the Data (Use and Access) Act 2025 and the Computer Misuse Act 1990 | PT-1, PL-1 | \[\] |
| P-32 | Hours of service and planned maintenance windows | \[From the business owner\] | CP-2, MA-2 | \[\] |
| P-33 | Numbers of users, schemas and items, and their growth | \[From the business owner\] | AU-4, CP-2 | \[\] |
| P-34 | Response times for the main functions | \[From the business owner\] | SC-5 | \[\] |
| P-35 | Accessibility standard and languages | \[From the business owner\]. Reference: WCAG 2.2 Level AA, English | PL-2 | \[\] |
| P-36 | Account types allowed | As listed in \<Access Control Management\>, Table 1 | AC-2 | \[\] |
| P-37 | Who decides access | The line manager approves in ServiceNow, then the group's owner authorises and adds the person to the AD group: the system owner for a role group, the Data Owner for a schema group | AC-2 | \[\] |
| P-38 | Unused accounts | AD accounts disabled under \<Organisation\>'s corporate standard; each month, members who have not signed in for 90 days are removed from \<System Name\>'s groups | AC-2(3) | \[\] |
| P-39 | Temporary and emergency accounts | Not allowed until the system can expire them | AC-2(2) | \[\] |
| P-40 | Sign-ins at once | No limit in the application | AC-10 | \[\] |
| P-41 | Disabling a high-risk individual | Within 1 hour of notice: AD account disabled and PingFederate sign-in ended | AC-2(13) | \[\] |
| P-42 | Failed sign-ins | Counted and the account locked by PingFederate and Active Directory, under \<Organisation\>'s corporate standard. The application has no sign-in of its own to lock | AC-7 | \[\] |
| P-43 | System use notice wording | The wording in \<Access Control Management\>, section 3.16 | AC-8 | \[\] |
| P-44 | Privileged functions and security-relevant information | Functions: managing schemas and the AD groups each uses; settings; diagnostics; audit log access; approving disposal; searching every schema for one person's items; database maintenance. Information: secrets and security settings, PingFederate's signing certificate, access groups and schema access rules, audit logs, firewall rules and certificates. All privileged functions are logged | AC-6(1), AC-6(9), AC-6(10) | \[\] |
| P-45 | Separate account for everyday work | Administrators use a separate non-privileged account for everyday item work | AC-6(2) | \[\] |
| P-46 | Remote access route | \<Organisation\>'s remote access service, \[name to be supplied\] | AC-17 | \[\] |
| P-47 | Wireless and mobile access | Follows \<Organisation\>'s policies, \[to be supplied\] | AC-18, AC-19 | \[\] |
| P-48 | External systems and portable storage | Not allowed with the application's data without system owner approval | AC-20 | \[\] |
| P-49 | Who decides on sharing outside a schema | The Data Owner | AC-21 | \[\] |
| P-50 | Public content | None, unless the system owner approves | AC-22 | \[\] |
| P-51 | Actions allowed without signing in | Being sent to PingFederate to sign in; the access-denied page; static files; the API health check. Nothing else | AC-14 | \[\] |

## 5 Requirements

This section lists what every application built on the reference system must do. Section 5.1 gives the common functional requirements, FR-001 onwards. Section 5.2 gives the non-functional requirements, NFR-001 onwards: the qualities the system must have, with the document that holds the detail. The functions particular to one application are in section 3.5.

The **How it is implemented** column says, in a sentence or two, how the reference design does it: which part does the work, where the data is held, and where the check is made. It stands in for the source code. The API is the only part that reads or writes the database: the UI application and the Admin application ask the API for everything. Where a person and not the system meets the requirement, it says so.

Each requirement is to be verified before the application is authorised. \<Security Assessment Report\> records the result for the application, and a requirement not met becomes an item in \<Plan of Action and Milestones\>.

### 5.1 Functional requirements

#### 5.1.1 Sign-in and the person's own account

**Table 10: Functional requirements: sign-in and the person's own account**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-001 | Sign in through \<Organisation\>'s PingFederate single sign-on service, with multi-factor authentication. The application shows no sign-in form of its own | Everyone | The application sends a person who is not signed in to PingFederate, which authenticates them against Active Directory, and accepts only PingFederate's signed response |
| FR-002 | Find the person's Active Directory groups, and give the roles and schema access those groups allow | System | The API queries Active Directory directly over LDAPS, under its own service account, for the signed-in person's group memberships, and maps them to roles and schemas. Nothing is looked up in an application account table |
| FR-003 | Refuse a sign-in response that is not signed by PingFederate, not issued for this application or outside its validity, and record the refusal | System | The response's signature, audience and validity are checked against PingFederate's public certificate |
| FR-004 | Show a system use notice at sign-in, which the person accepts before going further | Everyone | A notice page shown after sign-in, whose acceptance is written to the audit log |
| FR-005 | Open a home page showing the schemas and functions the person's groups allow, and nothing else | Everyone | The home page asks the API for the schemas whose read or edit group is among the person's groups, and shows those |
| FR-006 | Show only the menu items the person may use. The menu is a convenience: each function checks access itself | Everyone | The menu is drawn from the person's roles. Each page and each API function carries its own access rule as well |
| FR-007 | Show an access-denied page when a request is refused, without saying what exists behind it | Everyone | A refused request is sent to one fixed page with one fixed message, and the refusal is audited |
| FR-008 | Let nobody choose or change a role for themselves or for another person: roles come only from groups | System | Roles are set by the API from the person's Active Directory groups. No function changes a role |
| FR-009 | Show an About page that describes the application and its version | Everyone | A fixed page in the UI application |
| FR-010 | Link to the employee privacy notice, and say what the application records about its users | Everyone | A link and a short statement on the home page and the About page |
| FR-011 | Hold no user accounts, passwords, password resets or session management | System | Accounts, passwords and lockout live in Active Directory and PingFederate. The database has no account or password table |

#### 5.1.2 Schemas and search

**Table 11: Functional requirements: schemas and search**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-012 | Choose a schema from a list of those the person may read. A schema the person may not read is not shown and cannot be opened | Reader | A list filled by the API with the schemas the person's groups allow. The API checks the schema again on each request |
| FR-013 | Search the chosen schema's items | Reader | One parameterised query in that schema. The search is audited |
| FR-014 | Sort and page the results, with the sort column and page size chosen from fixed lists | Reader | Sorting and paging are done by the database, on a column chosen from a fixed list, so no text from the user becomes part of the query |
| FR-015 | Search one schema at a time. There is no search across schemas except the one in FR-073 | Reader | Every query names one schema. No other function queries more than one |
| FR-016 | Keep a person's recent searches, if kept at all, in their own browser only | Reader | Held in the browser's own storage on the person's device. Not sent to the server |
| FR-017 | Save a list of results, not the items' content, as a file | Reader | The UI application writes the rows on screen to a file and hands it to the browser. The save is audited |

#### 5.1.3 Viewing items and files

**Table 12: Functional requirements: viewing items and files**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-018 | View an item and its details | Reader | The API returns the item after the schema access check |
| FR-019 | View a stored file in the browser, without installing anything | Reader | The API sends the file, or an image of it rendered on the server, to a viewer served by the application |
| FR-020 | Download the original file | Reader | The API sends the stored file as a download, after the same access check as viewing. The download is audited |
| FR-021 | Copy a link to an item. A link opens only for a person who may read the schema | Reader | The link holds the schema and a random token for the item, not its number. Opening it runs the normal sign-in and access checks |
| FR-022 | Check the person's access to the schema on every request for an item, file, page, preview or download | System | Every API function that returns content takes the schema, confirms it against the person's groups, and only then reads from that schema's area |
| FR-023 | Name the schema in every item address | System | The address of each item and file carries the schema. No address works without it |
| FR-024 | Send content so that it is not kept in shared caches or in the browser after use | System | The API sets response headers that forbid shared caching and storing |
| FR-025 | Mark what the application shows, prints and exports with its classification | System | A banner and watermark on the viewer, on printed pages and in export files |

#### 5.1.4 Reporting a fault in an item

**Table 13: Functional requirements: reporting a fault in an item**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-026 | Report an item or file as faulty, with the kind of fault, a priority and a description | Reader | A dialog and a page, each sending the report to the API, which stores it with the reporter's name and the time |
| FR-027 | List a schema's reports, and filter them by status and priority | Reader, editor | The API reads the reports of one schema after checking the person's access to it |
| FR-028 | Move a report through its states, and record the corrective action | Editor | An editor changes the state on the report. The API checks edit access to the schema first |
| FR-029 | Record each report and each change of state in the audit log | System | The API writes an audit record when a report is created or changes state |

#### 5.1.5 Creating, uploading and managing items

**Table 14: Functional requirements: creating, uploading and managing items**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-030 | Manage the schema's items on pages open only to its editors | Editor | Each page first checks the person is an editor of the schema, then works through the API |
| FR-031 | Create an item, or upload a file as a new item, with its details | Editor | The details and any file go to the API, which checks them, creates the item and stores the file |
| FR-032 | Accept only the file types in P-19 | System | The extension and the declared type are checked against a fixed list on the server |
| FR-033 | Check on the server that a file's first bytes match its type, that its name holds no path, and that its size is within the limit for the person's role in P-17 | System | The API compares the file's leading bytes with the known signature of its type, strips any folder from the name, and compares its size with the limit |
| FR-034 | Scan each upload for malicious code before it is stored; refuse, record and report a flagged file | System | The API passes the file to the server's anti-malware service before storing it, and stores it only if it is clean |
| FR-035 | Give each item a status and a classification from fixed lists, and mark items that hold personal or special category data | Editor | Fields on the item, chosen from fixed lists |
| FR-036 | Correct an item's details | Editor, administrator | The API updates the item after checking access, and writes an audit record holding the old and new values |
| FR-037 | Replace a stored file | Administrator | The API stores the new file in place of the old one, keeps the checksum of both in the audit record, and audits the change |
| FR-038 | Delete an item, after confirming | Administrator | The API removes the item and its files, and writes an audit record of what was deleted and by whom |
| FR-039 | Store each file with a SHA-256 checksum, so that a change can be detected | System | The API calculates the checksum when the file is stored and holds it on the item |
| FR-040 | Record who created or uploaded each item, and when | System | The signed-in name and the time are written to the item by the API |

#### 5.1.6 Bulk upload

**Table 15: Functional requirements: bulk upload**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-041 | Upload a batch within the limits in P-18, as separate files or a ZIP file, with the details of each in a list from a template the application provides | Editor | The API counts the files and their total size and refuses a batch over either limit. A ZIP file is unpacked and each entry treated as a separate file |
| FR-042 | Check the batch and its list before anything is stored, and show what is wrong | Editor | A separate API function checks every file and row and returns the faults, storing nothing |
| FR-043 | Apply every check of a single upload, including the malware scan, to every file in the batch | System | The same checking routine runs for each file. One failure does not stop the others |
| FR-044 | Show the result for each file and for the batch, and notify the person when it ends | Editor | The API returns a result for each file, and creates a notification for the person |
| FR-045 | Check the person's edit access against the schema the files are stored in, not only the schema named in the request | System | The API takes the database schema from the schema definition it has just checked, not from a name in the request |

#### 5.1.7 Bulk export

**Table 16: Functional requirements: bulk export**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-046 | Choose a schema's items to export by filters, and see how many match before the export starts | Editor | The filters become one parameterised query in that schema. Field names come from a fixed list |
| FR-047 | Run the export as a job in the background, and let the person follow, download or cancel their own jobs | Editor | The API places the job on a queue, and a background task works through it |
| FR-048 | Let only the person who started a job see, download or cancel it | System | Each job holds the name of its starter, and the API compares it with the caller on every status, download and cancel request |
| FR-049 | Deliver exports only as downloads. There is no export to a folder or another system | System | The download is the only output |
| FR-050 | Encrypt an export's working copies, and delete them as P-20 sets | System | The API writes working copies to an encrypted working area, deletes them after the download, and a background task removes any left past the limit |
| FR-051 | Record every export in the audit log, with who, which schema and how many items | System | An audit record is written for each export |
| FR-052 | Raise an alert on an export above a set size | System | A rule in central monitoring on the export audit records |

#### 5.1.8 Notifications

**Table 17: Functional requirements: notifications**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-053 | Show a count of unread notifications, and list, filter, mark read and delete the person's own | Everyone | The API returns and changes only the caller's own notifications |
| FR-054 | Let only the application itself create a notification, and show a person only their own | System | Notifications are created inside the API by the function concerned. No function lets a caller create one for another person |
| FR-055 | Remove old notifications on a schedule | System | A background task in the API. No user can start it |
| FR-056 | Send no email or message outside the application | System | The application has no mail or messaging component, and no outbound route for one |

#### 5.1.9 Administration

**Table 18: Functional requirements: administration**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-057 | Show a dashboard in the Admin application with only the functions the person's role allows | Administrator, auditor, security officer | Each tile on the dashboard is shown only for the role it needs, and each page behind it has its own access rule |
| FR-058 | Create a schema with a code, a name and a description, as its own schema in the database | Administrator | The API adds the schema's definition and creates the database schema with its tables |
| FR-059 | Name the Active Directory group that may read a schema and the group that may edit it | Administrator | Two fields on the schema definition. The API compares them with the person's Active Directory groups |
| FR-060 | Change, deactivate, reactivate and delete schemas. A deactivated schema opens for nobody | Administrator | The API updates the schema definition and audits the change. Inactive schemas are left out of every list and refused on request |
| FR-061 | Close a schema with no groups to everyone but administrators | System | The access check finds no group to match, so only the administrator rule lets a person in |
| FR-062 | Manage the system settings that are safe to change while running | Administrator | A fixed list of settings, each change audited. Security settings are changed only by a release |
| FR-063 | Run fixed diagnostics that read no item content | Administrator | A page that runs fixed checks and shows the results. No diagnostic or test page is included in a release |
| FR-064 | Change the database's structure only by a release under an approved change, never from a page | Database administrator | Structure changes are scripts in a release, applied by the database administrator |
| FR-065 | Hold no pages for user accounts, passwords, roles or group membership: these are managed in Active Directory | System | No such page or table exists |
| FR-066 | Answer a health check without sign-in, giving no detail | System | One API function that returns a fixed answer and reads no data |

#### 5.1.10 Audit and security information

**Table 19: Functional requirements: audit and security information**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-067 | Record every event type in section 7.6 in one audit log, with who, what, when, where and the result | System | The function that carries out an action calls the audit service in the API, which adds one record |
| FR-068 | Accept audit records only from the application's own components, and let no user write or change one | System | The API accepts audit events only on calls bearing the token of the UI application or Admin application, and its database account may only add rows |
| FR-069 | Chain the audit records with a keyed hash, and check the chain on a schedule and on request | System | Each audit record stores a keyed hash of its own content and the previous record's hash. A scheduled task recomputes the chain and reports a break |
| FR-070 | Read, filter, search, sort and export the audit log | Auditor | The Admin application asks the API, which runs parameterised queries on the audit table. Only the auditor role may do this |
| FR-071 | Record each reading and export of the audit log | System | The API writes an audit record when the audit log is read or exported |
| FR-072 | Show the security officer a report of every page and function and the access it requires | Security officer | A page that lists each page and API function with the access rule it declares |

#### 5.1.11 Privacy and the life of an item

**Table 20: Functional requirements: privacy and the life of an item**

| No. | Requirement | Who | How it is implemented |
| --- | --- | --- | --- |
| FR-073 | Find every item about one person across all schemas, to answer a request under data protection law | Legal adviser's delegate | A search function limited to a named role, which queries every schema and is audited |
| FR-074 | Keep each kind of item for the period in the retention schedule, then dispose of it and record the disposal | Business owner | A retention period on each schema or item type, and a scheduled task that lists items due and deletes them once approved |
| FR-075 | Correct or erase a person's data on the legal adviser's instruction, and record it | Editor, administrator | The correct and delete functions, each audited |
| FR-076 | Keep personal data out of the free text of audit records and out of the application logs | System | Audit free text is built from fixed wording and identifiers, and the application logs carry no usernames, addresses or cookie values |
| FR-077 | Use only invented data in test and development. Real personal data is never used there | Developers | Test environments are built from a script that loads invented schemas and items |

#### 5.1.12 What the application does not do

Each statement below narrows what can go wrong. An application that needs one of these is outside the reference design for that part, and records it in section 3.6.

**Table 21: What the application does not do**

| No. | The application does not provide | How this is ensured |
| --- | --- | --- |
| FR-078 | Access for the public, customers or other organisations | The applications are reachable only on \<Organisation\>'s network, and only its directory accounts can sign in |
| FR-079 | An interface for other systems to call, or data sent to another system | The API accepts calls only from the other two applications on the same server |
| FR-080 | Email, text message or other outbound message | No mail or messaging component is included |
| FR-081 | A mobile application, or use from phones, tablets or unmanaged devices | The pages are built for a desktop browser, and \<Organisation\>'s network admits managed devices only |
| FR-082 | Automated decisions about people | No function scores, ranks or decides about a person |
| FR-083 | Storage outside the location in P-23, or a cloud service at run time | Both servers and the backups are in \<Organisation\>'s data centres |

### 5.2 Non-functional requirements

#### 5.2.1 Access control

**Table 22: Non-functional requirements: access control**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-001 | Refuse anything not granted: every page and function states the access it needs, and one with none is refused | The applications apply a default rule that requires a signed-in person, and each page or function adds the role or schema it needs | \<Access Control Management\> |
| NFR-002 | Check access on the server on every request, where the function runs. Nothing is decided in the browser | The access rule sits on the server-side page and on the API function. Pages are drawn on the server, so the browser receives only what was allowed | \<Access Control Management\> |
| NFR-003 | Take roles and schema access only from Active Directory groups. The application holds no table of who may do what | The API reads the person's groups from Active Directory and compares them with the group names on role settings and schema definitions | \<Access Control Management\> |
| NFR-004 | Keep each schema's items in its own database schema, so that one schema's items are never returned for another | The API picks the database schema from the checked schema definition, never from the request | Section 6 |
| NFR-005 | Give each person, service and administrator the least access their work needs | Separate groups for each role, a separate service account for each application, and a database account limited to what the API needs | \<Access Control Management\> |
| NFR-006 | Keep duties apart: nobody approves or reviews their own access; auditors and security officers hold no administration role; application, server and database administration are held by different people | Separate Active Directory groups with different owners, and role rules that give auditors and security officers no administration page | \<Access Control Management\> |
| NFR-007 | Allow without sign-in only the redirect to PingFederate, the access-denied page, static files and the health check | A short fixed list of open pages and functions in each application. Everything else falls under the default rule | \<Access Control Management\> |
| NFR-008 | Review group members as P-04 and P-05 set | A person does this: each group's owner checks its members against a list and signs a form | \<Access Control Management\> |
| NFR-009 | End a leaver's access as P-06 sets | \<Organisation\>'s leavers process disables the Active Directory account, so the next sign-in and group lookup fail | \<Access Control Management\> |
| NFR-010 | Require every user to sign the rules of behaviour before being added to a group | A person does this: the group's owner sees the signed form before adding the member | \<Planning Management\> |

#### 5.2.2 Identification and authentication

**Table 23: Non-functional requirements: identification and authentication**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-011 | Identify every user uniquely by their Active Directory account. No shared or generic accounts | The username in every audit record is the Active Directory account name | \<Identification and Authentication Management\> |
| NFR-012 | Multi-factor authentication for every user, at authenticator assurance level 2 and federation assurance level 2 of CSS | PingFederate requires the second factor before it signs a person in. The application accepts no other sign-in | \<Identification and Authentication Management\> |
| NFR-013 | Hold no passwords, password hashes or user accounts in the application | No account or password table exists in the database | \<Identification and Authentication Management\> |
| NFR-014 | Read group membership from Active Directory over LDAPS only, with the directory's certificate checked | The API binds to Active Directory with its managed service account, over LDAPS on TCP 636 | \<Identification and Authentication Management\> |
| NFR-015 | Give each application its own service account, managed by the operating system, with no interactive sign-in | Managed service accounts, whose passwords the operating system sets and changes | \<Identification and Authentication Management\> |
| NFR-016 | Authenticate the UI application and the Admin application to the API with a signed, short-lived token on every call | The two applications obtain a token from the API, signed with HMAC-SHA-256, and send it with every call | \<Identification and Authentication Management\> |
| NFR-017 | Authenticate the API to the database with its own Windows account, which is not a system administrator, over TLS | Windows authentication with the API's managed service account, so no database password exists. Its SQL Server login has rights on the application's database only | \<Identification and Authentication Management\> |
| NFR-018 | Show nothing that helps an attacker when sign-in or access fails | One general message for every failure. The reason is written to the logs only | \<Identification and Authentication Management\> |

#### 5.2.3 Sign-in lifetime and forms

The application has no session management of its own: no idle lock, no idle timeout, no limit on sign-ins at once and no screen for ending sign-ins. Session lock and session termination (AC-11 and AC-12) are therefore provided outside the application, by PingFederate and by \<Organisation\>'s managed devices.

**Table 24: Non-functional requirements: sign-in lifetime and forms**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-019 | Keep the signed-in person's identity only in the standard authentication cookie, marked Secure, HttpOnly and SameSite, with a lifetime no longer than P-02 | ASP.NET Core cookie authentication, protected by the application's key ring | \<Access Control Management\> |
| NFR-020 | Rely on the device screen lock in P-03 to hide the application when a person leaves their device | \<Organisation\>'s device policy | \<Access Control Management\> |
| NFR-021 | Protect every form with an anti-forgery token | Built into the web framework: each form carries a token, checked on submission | \<System and Communications Protection Management\> |

#### 5.2.4 Audit and accountability

**Table 25: Non-functional requirements: audit and accountability**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-022 | Record in each audit record the event type and action, the time in UTC, the application, the address and browser, the result, the user, and the schema and item | One record layout, filled in by the audit service in the API from the request | \<Audit and Accountability Management\> |
| NFR-023 | Never record a password, key, token or cookie | The audit service takes named fields only | \<Audit and Accountability Management\> |
| NFR-024 | Let only the API write audit records, and let its database account add records and nothing more | Only the API has a route to the audit table, and its database role is granted insert and select on it and nothing more | \<Audit and Accountability Management\> |
| NFR-025 | Chain audit records with HMAC-SHA-256 under a key held outside the database, so that a change or removal is detected | The hash covers the record's content and the previous hash, keyed with a secret from the key store | \<Audit and Accountability Management\> |
| NFR-026 | Keep audit records as P-07 sets | A scheduled archive and deletion, with the archive kept offline | \<Audit and Accountability Management\> |
| NFR-027 | Review the audit log as P-08 sets, and compare it with the server, database and PingFederate and Active Directory records | A person does this: an auditor, recording the review on a form, and reporting anything suspicious to the security officer | \<Audit and Accountability Management\> |
| NFR-028 | Alert the security officer when an audit record cannot be written | The audit service reports a failed write to central monitoring, which alerts the security officer | \<Audit and Accountability Management\> |
| NFR-029 | Keep both servers within the clock accuracy in P-09, from \<Organisation\>'s time service | The operating system's time service on each server, pointed at \<Organisation\>'s source | \<Audit and Accountability Management\> |
| NFR-030 | Plan storage for the full audit retention period, and warn before it fills | Sized when the servers are built, with a disk-space alert | \<Audit and Accountability Management\> |

#### 5.2.5 Cryptography and data protection

**Table 26: Non-functional requirements: cryptography and data protection**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-031 | Encrypt every flow as P-26 sets, under NCSC's profiles. No plain HTTP anywhere, including test | Set in the server configuration and each application's web server settings | \<System and Communications Protection Management\> |
| NFR-032 | Use certificates from \<Organisation\>'s certificate authority, renewed before they expire | Server certificates issued by \<Organisation\> and installed on both servers | \<System and Communications Protection Management\> |
| NFR-033 | Check the database server's certificate and name in full on every connection | The API's database connection verifies the certificate chain and the server name | \<System and Communications Protection Management\> |
| NFR-034 | Encrypt both servers' disks with AES-256 | Full-disk encryption switched on when the servers are built, with recovery keys held by \<Organisation\> | \<System and Communications Protection Management\> |
| NFR-035 | Encrypt backups with AES-256, with the key held apart from the backup | The backup tool encrypts each backup, and the key is kept in a different store | \<Contingency Planning Management\> |
| NFR-036 | Hold every secret in a key store outside the source code and settings files, readable only by the account that needs it | Secrets are read at start-up from a store protected by the operating system for the service account | \<System and Communications Protection Management\> |
| NFR-037 | Give every key an owner, a store and a life in the key register, and change keys and secrets as P-10 sets | The key register lists each key. Rotation is a duty in the operating calendar | \<System and Communications Protection Management\> |
| NFR-038 | Use only approved algorithms: AES-256, SHA-256 and HMAC-SHA-256. No MD5 or SHA-1 for protection. No cryptography written in-house | The algorithms built into Windows, .NET and SQL Server | \<System and Communications Protection Management\> |
| NFR-039 | Hold a SHA-256 checksum for each stored file and each release, and check them as P-29 sets | Calculated by the API when a file is stored and by the build when a release is made, and compared by a scheduled check | \<System and Information Integrity Management\> |

#### 5.2.6 Network and boundary

**Table 27: Non-functional requirements: network and boundary**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-040 | Internal only: no route to the application from the internet, and none from it to the internet | No firewall rule or address translation exposes either server, and outbound traffic is blocked or sent through the proxy | \<System and Communications Protection Management\> |
| NFR-041 | Allow only the flows in section 6.5, at \<Organisation\>'s firewalls and at each server's own firewall | Rules written by \<Organisation\> on its firewalls, and host firewall rules on each server | \<System and Communications Protection Management\> |
| NFR-042 | Listen for users on TCP 443 only; the API on the application server's loopback address only; the database to the application server only | Set by the address and port each application is bound to, and by the database's list of permitted clients | \<System and Communications Protection Management\> |
| NFR-043 | Reach the Admin application only over \<Organisation\>'s managed administration route, with multi-factor authentication | The Admin application is bound to the administration network, with a firewall rule to match | \<Maintenance Management\> |
| NFR-044 | Remote users only through \<Organisation\>'s VPN, from a managed device, with no split tunnelling | \<Organisation\>'s VPN and its device checks | \<Access Control Management\> |
| NFR-045 | Keep the UI application, the Admin application, the API and the database apart, so that user functions are separate from management functions | Four separate programs on two servers | \<System and Communications Protection Management\> |
| NFR-046 | Limit how fast any one client may send requests | A request limit for each client, built into each application and switched on in every environment | \<System and Communications Protection Management\> |

#### 5.2.7 Application and information integrity

**Table 28: Non-functional requirements: application and information integrity**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-047 | Validate all input on the server: every API request, upload and search term | Every API function checks its inputs for type, length and range before use, and uploads go through the checks in section 7.5 | \<System and Information Integrity Management\> |
| NFR-048 | Use parameters in every database query | Queries are built with placeholders for values, and names of columns and schemas come only from fixed lists or checked schema definitions | \<System and Information Integrity Management\> |
| NFR-049 | Run only code the application itself serves: a page policy with no inline scripts and no outside hosts, and headers that stop content-type guessing and limit referrer information | A content security policy header and related headers, added to every response by each application | \<System and Communications Protection Management\> |
| NFR-050 | Serve every script and style from the application. No content delivery service | Browser libraries are packaged with the UI application | \<System and Communications Protection Management\> |
| NFR-051 | Show users and callers a general error message, with the detail only in the logs | A common error handler returns a fixed message and logs the detail | \<System and Information Integrity Management\> |
| NFR-052 | Fail secure: an error, a time-out or a missing dependency, including Active Directory, refuses access | Access checks are written so that any failure returns a refusal. If the groups cannot be read, the person gets no role and no schema | Section 6 |
| NFR-053 | Scan every upload, and run anti-malware with current definitions on both servers | The operating system's malware scanning interface for uploads, and real-time protection on each server | \<System and Information Integrity Management\> |
| NFR-054 | Fix or mitigate a flaw within the times in P-11 | A person does this: the developers and administrators, tracked in the plan of action | \<Risk Assessment Management\> |
| NFR-055 | Scan for vulnerabilities as P-30 sets | \<Organisation\>'s scanner for the servers, and a package and code scan for each release | \<Risk Assessment Management\> |
| NFR-056 | Raise an alert on the events in P-27, to a named person, within the time set for its severity | Rules in central monitoring, each with a named recipient | \<System and Information Integrity Management\> |

#### 5.2.8 Availability and recovery

**Table 29: Non-functional requirements: availability and recovery**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-057 | Tolerate an outage up to the maximum tolerable downtime in P-14 | A business decision, recorded in the business impact analysis | \<Contingency Planning Management\> |
| NFR-058 | Recover within the recovery time objective in P-12 | By rebuilding the servers and restoring the latest backup, in the order in section 7.11 | \<Contingency Planning Management\> |
| NFR-059 | Lose no more data than the recovery point objective in P-13 | A daily backup, with the database's transaction log archived between backups | \<Contingency Planning Management\> |
| NFR-060 | Back up the database daily, and keep copies as P-15 sets | A scheduled database backup, copied by \<Organisation\>'s backup service | \<Contingency Planning Management\> |
| NFR-061 | Test recovery as P-16 sets | People do this, to a written plan, and record the result | \<Contingency Planning Management\> |
| NFR-062 | After a restore, check row counts, file checksums and the audit chain before users return | Scripts that compare counts and checksums and run the chain check | \<Contingency Planning Management\> |
| NFR-063 | No high availability, clustering or second live site is required at availability Low | One application server and one database server | \<Contingency Planning Management\> |
| NFR-064 | When PingFederate or Active Directory is down nobody can sign in or be authorised, and no local sign-in is provided | The applications redirect to PingFederate and read groups only from Active Directory | \<Concept of Operations\> |
| NFR-065 | Provide the hours of service in P-32 | \[From the business owner\] | \<Concept of Operations\> |

#### 5.2.9 Capacity and performance

**Table 30: Non-functional requirements: capacity and performance**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-066 | Support the numbers in P-33 and the response times in P-34 | \[Sized when the profile is complete\] | \<Concept of Operations\> |
| NFR-067 | Server sizes: processors, memory and storage | \[When the servers are built\] | Section 6 |
| NFR-068 | Enforce the upload limits in P-17 and P-18 | Limits checked by the API before a file is stored | \<System and Information Integrity Management\> |
| NFR-069 | Run bulk uploads and exports in the background, so that other users are not held up | Jobs run on a queue in the API, apart from the request that started them | Section 6 |
| NFR-070 | Send results and large files a part at a time, so that the time taken does not grow with the size of an item or a schema | Paging is done in the database, and large files are sent in parts | Section 6 |

#### 5.2.10 Privacy

**Table 31: Non-functional requirements: privacy**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-071 | Process personal data only for the purposes stated in the application profile and \<PII Processing Management\> | A rule of use, in the policy and the rules of behaviour | \<PII Processing Management\> |
| NFR-072 | Hold only the personal data a schema needs, and keep special category data only in schemas the business owner authorises | A person does this: the Data Owner and the business owner | \<PII Processing Management\> |
| NFR-073 | Answer a person's request about their data within the time in P-22 | A person does this: the legal adviser's delegate, using the search in FR-073 | \<PII Processing Management\> |
| NFR-074 | Send a personal data breach to the legal adviser, who decides on the report to the regulator as P-21 sets | The incident response playbook routes it there | \<Incident Response Management\> |
| NFR-075 | Keep all data in the location in P-23 | Servers, backups and the second site are all in that location, and nothing is sent elsewhere | \<PII Processing Management\> |
| NFR-076 | Complete the data protection impact assessment before real data is held, and review it at each significant change | A person does this: the legal adviser | \<Data Protection Impact Assessment\> |

#### 5.2.11 Platform and compatibility

**Table 32: Non-functional requirements: platform and compatibility**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-077 | Run on the reference stack in section 6.4, or on the stack the profile records, each part within its vendor's support | Fixed by the release's build settings and the server build | \<System and Services Acquisition Management\> |
| NFR-078 | Run each application as a service under its own low-privilege account | Each application is installed as a service by the release procedure | \<Configuration Management\> |
| NFR-079 | Work in a current browser on a device \<Organisation\> manages, with nothing installed on it | The pages use only standard browser features, and no plug-in or installed program | \<System Security Plan\> |
| NFR-080 | Use only the components on the approved list; remove what is not used | The component list in the configuration management design, checked at each release | \<Configuration Management\> |
| NFR-081 | Meet the accessibility standard in P-35 | Tested at each release | \<Concept of Operations\> |

#### 5.2.12 Build, change and supply chain

**Table 33: Non-functional requirements: build, change and supply chain**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-082 | Develop under \<Organisation\>'s corporate SDLC, whose security practices meet CSS | The corporate SDLC, inherited from \<Organisation\> | \<System and Services Acquisition Management\> |
| NFR-083 | Model the threats to the application before it is built, and again at each significant change | A threat model of the profile and its functions, kept with the risk list | \<Risk Assessment Management\> |
| NFR-084 | Have every change reviewed by a second developer and merged through a protected branch | Branch rules in the source repositories | \<System and Services Acquisition Management\> |
| NFR-085 | Approve every change to production by the change control board, after a security impact analysis | A change record, with the board's decision, before any release | \<Configuration Management\> |
| NFR-086 | Build and test every release in a pipeline, with automated tests, a package and code scan, and the verification standard in P-28 | The pipeline builds from the protected branch and runs the tests and scans before a release can be made | \<System and Services Acquisition Management\> |
| NFR-087 | Release from a signed tag with recorded checksums, so that a release can be rebuilt exactly | The release procedure tags the source and records a checksum for each package | \<Configuration Management\> |
| NFR-088 | Take every package through one checked source, with lock files and a software bill of materials for each release | An in-house package feed, with package sources mapped so that nothing else is used | \<Supply Chain Risk Management\> |
| NFR-089 | Keep development, test and production apart, with no production data outside production | Separate environments, with invented data loaded by script | \<System and Services Acquisition Management\> |
| NFR-090 | Compare the running system with its approved baseline as P-29 sets | A scheduled comparison of files and settings with the release record | \<Configuration Management\> |
| NFR-091 | Configure both servers to the CIS Benchmark, with only the functions, ports and services the application needs | Policy applied by \<Organisation\>, checked with a benchmark tool | \<Configuration Management\> |
| NFR-092 | Keep secrets out of source code, and scan every change for them | A secret scan in the pipeline that blocks a merge | \<System and Services Acquisition Management\> |

#### 5.2.13 Operation and assurance

**Table 34: Non-functional requirements: operation and assurance**

| No. | Requirement | How it is implemented | Held in |
| --- | --- | --- | --- |
| NFR-093 | Operate under the duties in \<Security Operating Procedures\>, each with a named owner, a frequency and a record | The operating calendar | \<Security Operating Procedures\> |
| NFR-094 | Train users as P-24 sets | \<Organisation\>'s course, and the application's briefing and role modules | \<Awareness and Training Management\> |
| NFR-095 | Report and handle incidents as P-21 sets | The incident response plan, with \<Organisation\>'s service desk | \<Incident Response Management\> |
| NFR-096 | Approve maintenance beforehand, and record it | A change record for each piece of maintenance | \<Maintenance Management\> |
| NFR-097 | Meet the CSS Moderate baseline and privacy baseline, as tailored | The control register and the family design documents | \<Tailoring Register\> |
| NFR-098 | Be authorised as P-25 sets | A signed authorisation decision | \<Assessment, Authorization, and Monitoring Management\> |
| NFR-099 | Be assessed independently before authorisation, and monitored continuously after it | An assessor independent of the developers, and the monitoring measures | \<Assessment, Authorization, and Monitoring Management\> |
| NFR-100 | Comply with the laws in P-31 | Through the privacy design and the legal adviser's review | \<Planning Management\> |
| NFR-101 | Provide an administrator guide and a user guide | Two guides, written by the developers | \<Administrator Guide\> |

## 6 Architecture

### 6.1 Boundary

![Figure 1: The reference system's boundary on the organisation's network](figures/sd-figure-1.png)

**Figure 1: The reference system's boundary on the organisation's network**

The authorisation boundary is the whole stack on two servers: the application server, which runs the three applications, and the database server, which runs the database. Everything else is outside it and is provided by \<Organisation\>: the network and firewalls, the VPN, users' devices, the sign-on service and directory, the virtual platform and hardware, central logging, time, certificates, name resolution, ServiceNow and the starters and leavers process (section 10).

### 6.2 Hardware and hosting

**Table 35: Hardware and hosting**

| Item | Reference design |
| --- | --- |
| Application server | A virtual server hosted by \<Organisation\>. Runs the UI application, the Admin application and the API, each as a service under its own low-privilege service account |
| Database server | A separate virtual server. Runs the database |
| Virtual platform and hardware | \<Organisation\>'s hypervisor and physical hosts, in its data centre in the location in P-23 |
| Second site | A separate \<Organisation\> site, for encrypted backups and for rebuilding the servers |
| Disks | Full-disk encryption with AES-256, keyed to the server's TPM |
| Users' devices | Laptops and desktops managed by \<Organisation\>, with disk encryption, a screen lock and removable storage blocked unless approved |
| Sizes, host names and addresses | \[For each application, when its servers are built\] |

An application built on the reference system has no hardware of its own, no wireless, no mobile application and no removable media in normal use.

### 6.3 Software components

**Table 36: Software components**

| Component | What it is | What it does | Runs on |
| --- | --- | --- | --- |
| UI application | A web application whose pages run on the server | Every function in section 5.1 used by readers and editors, and the functions in section 3.5 | Application server |
| Admin application | A second web application of the same kind, separate from the UI application | Schemas and their groups, settings, the audit log for auditors, security information and the dashboard | Application server, reachable only over the administration route |
| API | A web service | The only route to the database: every read and write, the Active Directory group lookup, access decisions for the other two applications, background jobs, and writing the audit log | Application server, on its loopback address only |
| Shared library | A library built into all three applications | The data model, the access checks and the audit record format, so that every application makes the same decision the same way | Built in |
| Database | Microsoft SQL Server | Holds every item, file, schema definition and audit record, with each schema in its own database schema | Database server |
| Browser libraries | Any third-party script or style the pages need | For example a document viewer or an icon set | The user's browser, served by the application itself |

The components are named \<Code\>\_Web, \<Code\>\_Admin, \<Code\>\_API and \<Code\>\_Shared, using the short code in section 3.1.

### 6.4 Technologies

The reference stack is below. An application may replace any part of it with a supported equivalent that meets the same requirements, and records the change in section 3.6. The family design documents name the reference stack where a control depends on it.

**Table 37: Reference technology stack**

| Layer | Reference technology | Why it is chosen |
| --- | --- | --- |
| Operating system | Windows Server 2025 | Under Microsoft support; CIS Benchmark available; Defender, BitLocker and managed service accounts built in |
| Application platform | Microsoft .NET 10 and ASP.NET Core 10, a long-term support release | Under Microsoft support; built-in data protection, anti-forgery and authentication for federated sign-in |
| User interface | Blazor Server: pages are rendered on the server and updated over a live connection from the browser | No application logic or data access runs in the browser |
| API | ASP.NET Core web API, called over HTTPS by the other two applications with a signed token | Interactive API documentation is for development only and is left out of releases |
| Data access | Entity Framework Core 10 with the Microsoft SQL Server provider (Microsoft.Data.SqlClient) | Queries use parameters by default |
| Database | Microsoft SQL Server 2022 | TLS with strict encryption, Windows authentication, fine-grained permissions and backup encryption |
| Sign-in | \<Organisation\>'s PingFederate, by federation using OpenID Connect, with multi-factor authentication against Active Directory | No accounts or passwords in the application |
| Group lookup | Active Directory, queried by the API over LDAPS | Groups are read from the directory itself, not carried in the sign-in response |
| Tokens between the applications | HMAC-SHA-256, with the key in a key store | Short-lived, and refused from any other caller |
| Malicious code | Microsoft Defender, called for each upload through the Windows Antimalware Scan Interface | Scanning before anything is stored |
| Disk encryption | BitLocker, XTS-AES 256, with the TPM | Encryption at rest without application changes |
| Source control and pipeline | Git, in private repositories with protected branches, and a build pipeline, under the corporate SDLC | Reviewed, repeatable releases |
| Packages | NuGet, through an in-house checked package feed | One controlled source for every component |
| Test environment | A throwaway copy of the whole system, built from a tagged release, with invented data | Testing never touches production or real data |

### 6.5 Data flows

**Table 38: Data flows**

| Flow | From | To | Purpose | Reference design |
| --- | --- | --- | --- | --- |
| F1 | User's browser | UI application | User work | HTTPS, TCP 443 |
| F2 | Administrator's browser | Admin application | Administration | HTTPS, only over \<Organisation\>'s managed administration route |
| F3, F4 | UI application and Admin application | API | Every request for data and background work | HTTPS, on the application server's loopback address only |
| F5 | API | Database | All data | SQL Server over TLS 1.2 or later with strict encryption, TCP 1433, from the application server only |
| F6 | Browser | \<Organisation\>'s PingFederate | Sign-in with multi-factor authentication | HTTPS |
| F7 | API | \<Organisation\>'s Active Directory | Reading the signed-in person's group memberships | LDAPS, TCP 636 |
| F8 | Both servers | \<Organisation\>'s time service, central logging, proxy and backup site | Time, logs, updates and backups | As \<Organisation\> sets, encrypted |
| F9 | ServiceNow and the starters and leavers process | People, not the application | Access approvals and leaver notices | By people, in \<Organisation\>'s services. ServiceNow has no connection to the application |
| F10 | UI application and Admin application | \<Organisation\>'s PingFederate | Fetching PingFederate's OpenID Connect metadata and signing certificate, and completing each sign-in | HTTPS, TCP 443, from the application server only |
| F11 | Server and database administrators' managed devices | Both servers | Server and database administration | Only over \<Organisation\>'s managed administration route, with multi-factor authentication, using named accounts |

No other flow is allowed. The UI application and the Admin application have no connection to the database. The application needs no route to the internet, and loads nothing from an outside host.

### 6.6 Trust zones and layers of defence

**Table 39: Trust zones**

| Zone | What is in it | Trust | Entry into the zone |
| --- | --- | --- | --- |
| Z1 Users | Users' managed devices and \<Organisation\>'s corporate network | Not trusted by \<System Name\> | Not applicable |
| Z2 Administration route | \<Organisation\>'s managed route for administrators | Trusted for administration only | Managed route and administrator sign-in |
| Z3 Application | Application VM: UI application, Admin application and API | Trusted to enforce access | HTTPS on 443 from Z1 (F1); the Admin application only from Z2 (F2); server administration only from Z2 (F11) |
| Z4 Data | Database VM: SQL Server and the \<System Name\> database | Most protected | Encrypted database connections from the API in Z3 only (F5); database administration only from Z2 (F11) |
| Z5 Provider services | \<Organisation\>'s directory, sign-on, monitoring, ServiceNow and starters and leavers services | Trusted by agreement and evidence | From browsers to PingFederate (F6), outbound from Z3 (F7, F8, F10) or by people (F9), as in section 10 |

The layers are the boundary, transport, identity, authorisation, data at rest, audit, the host, recovery and people. Each is described in section 7, with its main controls in section 6.8, and the principles behind them are in section 8.

### 6.7 Environments

**Table 40: Environments**

| Environment | What it is | Data |
| --- | --- | --- |
| Production | The two servers at \<Organisation\> | Real data |
| Test | A separate, throwaway copy of the whole system, built from a tagged release and removed after each test run. Configured as production is, including TLS | Invented data only. Real personal data is never used |
| Development | Developers' computers | Invented data only |

### 6.8 Security architecture

This section is the security architecture that PL-8 calls for: the protection goals, the layers of defence, the engineering principles, the configuration on the servers, and the assumptions the design rests on. The boundary, flows and trust zones are in sections 6.1, 6.5 and 6.6, and the design principles in section 8. The privacy architecture is in \<Privacy Plan\>, section 8.

**Table 40a: Protection goals**

| Objective | Impact | What it means for \<System Name\> | Main protections |
| --- | --- | --- | --- |
| Confidentiality | Moderate | Items, including personal data, are seen only by members of the schema's read or edit group, and by administrators | Schema groups read from Active Directory, encrypted transport and storage, audit |
| Integrity | Moderate | Items, their details and files, and the audit trail cannot be changed without trace | Edit rights by role, change control, hash-chained audit records |
| Availability | Low (\<System Security Plan\>, section 3.3; P-01) | \<System Name\> can be restored after a failure within the times in \<Contingency Planning Management\> | Encrypted backups at the second site, rebuild procedure |

**Table 40b: Layers of defence**

| Layer | Protection | Main controls |
| --- | --- | --- |
| Boundary | \<Organisation\>'s firewalls allow only HTTPS into Z3, and the Admin application and server and database administration (F11) only from Z2 | SC-7, AC-17, MA-4 |
| Transport | TLS on every flow, F1 to F8 and F10, as \<System Description\>, P-26, sets, under NCSC's profiles (\<System and Communications Protection Management\>, section 3.3); data protection key rings protected with DPAPI | SC-8, SC-13 |
| Identity | Each person's own Active Directory account, signed in through PingFederate with multi-factor authentication; roles and schema access from AD groups, read by the API over LDAPS (F7) | IA-2, IA-5, AC-7 |
| Authorisation | Roles and schema access checked on every page and API call | AC-3, AC-6 |
| Sign-in lifetime and screen lock | No session management in \<System Name\>. The sign-in is held only in the authentication cookie, which lasts no longer than PingFederate's sign-in lifetime (\<System Description\>, P-02); an unattended screen is locked by the operating system on \<Organisation\>'s managed devices and the servers (\<System Description\>, P-03) | AC-11, AC-12, SC-23 |
| Data at rest | Full-disk encryption on both VMs; no plain copies left by exports | SC-28, MP-4 |
| Audit | Hash-chained audit records, reviewed and kept | AU-2, AU-6, AU-9 |
| Host | CIS hardening, Microsoft Defender, patching | CM-6, SI-2, SI-3 |
| Recovery | Encrypted backups and logs at the second site | CP-9, CP-10 |
| People | Rules signed before access, training, screening | PL-4, AT-2, PS-3 |

\<System Name\>'s security engineering principles are the NCSC secure design principles, and its privacy engineering principles are the CSS privacy engineering objectives (\<System and Services Acquisition Management\>; SA-8). Table 40c shows where the design meets each. Development, implementation and changes are checked against it (\<Procedures\>, PRO-SA-1).

**Table 40c: Engineering principles**

| Principle | Where \<System Name\>'s design meets it |
| --- | --- |
| NCSC 1: Establish the context | Boundary, data flows and trust zones (sections 6.1, 6.5 and 6.6); information types and impact in \<System Security Plan\>, section 3.3; risks in \<Risk List\> |
| NCSC 2: Make compromise difficult | Deny by default and least privilege (section 8); schema access checked on every request; layered defences (Table 40b); trust zones with the Admin application only from Z2 |
| NCSC 3: Make disruption difficult | Separate application and database VMs; recovery times in \<Contingency Planning Management\> |
| NCSC 4: Make compromise detection easier | Hash-chained audit records, weekly review and alerts (\<Audit and Accountability Management\>), detection use cases U1 to U8 (\<System and Information Integrity Management\>, section 3.4); log forwarding to \<Organisation\> |
| NCSC 5: Reduce the impact of compromise | Each schema's items in its own database schema; database reachable only from Z3; separate administration route; critical components in \<Risk Assessment Management\>, section 3.9 |
| CSS privacy: Predictability | Purposes and processing rules in \<PII Processing Management\>; privacy notice through \<Organisation\> |
| CSS privacy: Manageability | Requests, corrections and deletions through PRO-PT-1; retention schedule |
| CSS privacy: Disassociability | Access limited by schema group; audit free text holds no extra personal data |

**Table 40d: Configuration on the servers**

| Item | Target |
| --- | --- |
| Host | Two Windows Server 2025 VMs |
| Traffic | HTTPS and encrypted database connections |
| Secrets | The token signing key and the audit chain key, in a key store outside source code, changed as \<System Description\>, P-10, sets. There is no database password: the API uses Windows authentication |
| Database login | One least-privilege SQL Server login for the API's managed service account, by Windows authentication, used only by API |
| Storage | Full-disk encryption on both VMs |
| Malicious code | Microsoft Defender on both VMs, and each upload scanned through AMSI before it is stored (\<System and Information Integrity Management\>, section 3.2) |
| Hardening | CIS Benchmarks for Windows Server 2025 and SQL Server 2022 |
| Backups | Encrypted daily backups and transaction logs, kept at the second site |
| Retention | Schedule in \<PII Processing Management\>, section 3.7, with periods set by the business owner, and disposal when they end |
| Build and test | Built under \<Organisation\>'s corporate SDLC, with a build pipeline and release test gate |

The design rests on these assumptions:

1. \<Organisation\> provides and evidences the services in section 10. \<System Name\> relies on them but does not describe how they are built.
2. The servers are built to this design, with the configuration in Table 40d, before production.
3. Users work only on \<Organisation\>'s managed devices, over its network or managed route.
4. The critical components and their failure effects are in \<Risk Assessment Management\>, section 3.9.

## 7 Design

### 7.1 Identity and sign-in

1. A person opens the application. Not being signed in, they are sent to \<Organisation\>'s PingFederate.
2. PingFederate checks their password and second factor against Active Directory. The application never sees either.
3. PingFederate returns a signed OpenID Connect response that names the person. It carries no groups.
4. The application checks the response: that PingFederate signed it, that it was issued for this application and that it is still valid.
5. The API queries Active Directory directly, over LDAPS, for the person's group memberships, and gives the roles and schema access those groups allow. The sign-in is recorded.

The application holds no accounts, no passwords and no password hashes. There is no local sign-in to fall back on, so nobody can sign in while PingFederate or Active Directory is down. Failed sign-ins and lockouts happen in PingFederate and Active Directory, under \<Organisation\>'s standard. A leaver's Active Directory account is disabled by \<Organisation\> at once, which ends their access. The target is federation assurance level 2 and authenticator assurance level 2 of CSS.

### 7.2 Authorisation

Every request passes four checks, in order. Anything not granted is refused.

1. The person signed in through PingFederate, and the request carries the application's valid authentication cookie.
2. The person's Active Directory groups were read successfully.
3. The person's groups allow the schema, to read or to edit.
4. The person's groups allow the page or function.

A schema with no group is closed to everyone but administrators. Checks are made where the function runs, not only in the menu, and the database schema is taken from the checked schema definition, never from the request. Content is sent so that it is not kept in shared caches. The permissions of each role are in section 3.3 and \<Access Control Management\>.

**Duties kept apart.** Nobody approves their own access: the Data Owner authorises each request in ServiceNow. Auditors and security officers hold no administration role. Application, server and database administration use separate accounts held by different people. Developers hold no administrator access on the servers.

**Without signing in,** a person may only be sent to PingFederate, see the access-denied page, load static files, and check that the API is healthy. No diagnostic, cache or test function is reachable without sign-in, and none is included in a release.

### 7.3 Sign-in lifetime

The application has no session management. Once signed in, the person's identity is held in the standard ASP.NET Core authentication cookie, marked Secure, HttpOnly and SameSite, whose lifetime follows PingFederate's (P-02). The application has no idle lock, no idle timeout, no limit on sign-ins at once, no sign-out of its own and no screen for ending sign-ins. Session lock (AC-11) is provided by the screen lock on \<Organisation\>'s managed devices (P-03), and session termination (AC-12) by the sign-in lifetime set in PingFederate. Both are recorded as provided by \<Organisation\> in \<Tailoring Register\>.

### 7.4 Data and storage

**Table 41: Where data is held**

| Data | Held in | Protected by |
| --- | --- | --- |
| Schema definitions, and the read group and edit group of each | The database, in a common schema shared by all schemas | The API's service account; changed only by administrators |
| Items, their details and their files | The database, each schema in its own database schema | Schema access checks; disk encryption; a SHA-256 checksum for each file |
| The audit log | The database | The API's service account may add records and nothing more; a keyed hash chains the records |
| Export working copies | An encrypted working area on the application server, written by the API | Deleted as P-20 sets |
| Each application's key ring | Its own folder on the application server | Readable only by that application's service account; encrypted by the operating system |
| Each application's log | Log files on the application server, forwarded to central logging | Readable by the server administrators and the auditor; no personal data |
| Secrets: the token signing key and the audit chain key | A key store outside the source code | Access limited to the service account that needs each; changed as P-10 sets. There is no database password: the API uses Windows authentication |
| Backups | \<Organisation\>'s backup store and second site | Encrypted, with the key held apart |

The application holds no user accounts. The names and groups that arrive at sign-in are held only in the authentication cookie, in the audit records, and in items, such as who created or uploaded an item.

### 7.5 Files: upload, viewing and export

**Upload.** Every upload is checked on the server before it is stored: the type must be one of those in P-19; the file's first bytes must match its type; its size must be within the limit for the person's role; and its name must not contain a path. Each upload is then passed to the anti-malware service, and a flagged file is refused, audited and reported.

**Viewing.** A file is sent to the browser, or rendered on the server and sent as an image, only after the schema access check. The viewer is served by the application.

**Export.** Only an editor of the schema, or an Administrator, may bulk export. A job can be seen, downloaded or cancelled only by the person who started it. Exports are delivered as downloads, marked with their classification, and every export is audited. Taking exported items outside \<Organisation\>'s systems needs the Data Owner's decision.

### 7.6 Audit

One application audit log, written only by the API. The other two applications send their events to the API, which accepts them only from those two applications.

**Table 42: What is audited**

| Event type | Examples |
| --- | --- |
| Sign-in | Sign-in accepted; sign-in response refused; Active Directory lookup failed; system use notice accepted |
| Schema and group administration | Schema created, changed or deactivated; a schema's groups changed |
| Access decision | Access to a page, function or schema refused |
| Item access and export | Viewed; downloaded; searched; exported |
| Data change | Created; uploaded; corrected; replaced; deleted, with the old and new values |
| Privileged function | Settings changed; diagnostics run |
| Configuration change | A security setting changed |
| Audit | Audit log read or exported; chain check result |
| System | Application started or stopped |
| Logging failure | A record could not be written |

Each record holds the event type and action, the time in UTC, the application that raised it, the IP address and browser, the result, the username and user ID, the schema and item, fixed-form free text, and a chain hash. It never holds a password, key, token or cookie. Records are read only by auditors, reviewed as P-08 sets, and kept as P-07 sets. Failed passwords, lockouts and group membership changes are recorded by PingFederate and Active Directory, not by the application. The operating system and the database keep their own logs.

### 7.7 Cryptography and keys

**Table 43: Cryptography**

| Use | Reference design |
| --- | --- |
| Traffic | As P-26 sets, with certificates from \<Organisation\>'s certificate authority |
| Database connection | TLS with strict encryption, with the server's certificate and name checked in full |
| Tokens between the applications | HMAC-SHA-256 with a random key of at least 256 bits, held in a key store |
| Cookies and anti-forgery tokens | AES-256 with HMAC-SHA-256, from each application's key ring, changed every 90 days |
| Disks | AES-256 full-disk encryption with the TPM |
| Backups | AES-256, with the key held apart |
| File checksums | SHA-256 |
| Audit chain | HMAC-SHA-256 with a key held outside the database |
| Database connection account | Windows authentication (Kerberos) with the API's managed service account. No password is held |
| Sign-in responses | Signed by PingFederate; the application holds only its public certificate |

Every key has an owner, a store and a cryptoperiod in the key register, in \<System and Communications Protection Management\>. Keys are never held in source code or settings files. Validation of cryptographic modules to a United States standard is not required: NCSC's profiles are used instead.

### 7.8 Network and boundary

\<Organisation\>'s firewalls and each server's own firewall deny everything but the flows in section 6.5. The UI application listens on TCP 443 only. The Admin application is reachable only over the administration route. The API listens only on the application server's loopback address, so nothing off the server can call it. The database accepts connections only from the application server. Outbound traffic goes through \<Organisation\>'s authenticated proxy, or is blocked. Remote users come in through \<Organisation\>'s VPN, which does not allow split tunnelling. \<Organisation\> writes and holds every firewall rule; the application states the flows it needs.

### 7.9 Pages and input

Pages may run only code the application itself serves. Each application sends a page security policy that allows no inline scripts and no outside hosts, with headers that stop content-type guessing and limit referrer information. All input to the API, every upload and every search term is validated on the server, and database queries use parameters. Users and callers see a general error message; the detail goes only to the logs. Each application limits how fast requests may arrive.

### 7.10 Monitoring, flaws and integrity

Application, operating system and database logs are forwarded to \<Organisation\>'s central logging, and the security officer reviews them as P-08 sets. Eight events raise an alert: repeated failed sign-ins; a break in the audit chain; malware detected; a person added to an administrator group; a bulk export above a set size; an administrator sign-in out of hours; an audit logging failure; and an unexpected change to the software. Advisories come from NCSC, CISA and the vendors of every component, and CISA's list of known exploited vulnerabilities is checked weekly. Releases, stored files and audit records are checked against a recorded baseline at start-up, at each release and as P-29 sets.

### 7.11 Backup and recovery

The database is backed up daily, encrypted, with transaction logs archived, and copies are kept as P-15 sets. Recovery is in order: \<Organisation\>'s network, PingFederate and Active Directory; the database server and its backup; the secrets; the API; the UI application; the Admin application. After a restore, row counts, file checksums and the audit chain are checked, and the members of the application's groups are checked against current staff before users return. Recovery is tested as P-16 sets.

### 7.12 Build, release and supply chain

Every application is built in-house under \<Organisation\>'s corporate software development life cycle (SDLC), which is inherited from \<Organisation\>. The reference system relies on the SDLC to provide these security practices, which together meet CSS: threats modelled before a significant change is built, and the change checked against the principles in section 8; each change reviewed by a second developer and merged through a protected branch; a build pipeline with automated tests, a package scan, a code scan and a secret scan; releases through change control from a signed tag with recorded checksums; every package through one checked feed, with lock files; and a software bill of materials for each release. Where the SDLC does not provide one of these, the application provides it itself or records a departure in section 3.6. The suppliers are in a register with their criticality.

### 7.13 Operation and maintenance

Day-to-day duties are in \<Security Operating Procedures\>, each with the record that proves it. Every user signs rules of behaviour before access. Maintenance is approved first as a change, and remote maintenance uses only \<Organisation\>'s managed route with multi-factor authentication. Changes are approved by a change control board of the system owner, the security officer and a server administrator.

### 7.14 Privacy

The personal data an application holds, and the purposes it is processed for, are set in its profile (section 3.4) and in \<PII Processing Management\>. Consent is not the lawful basis for staff data. The application makes no automated decisions about people and transfers no data outside the location in P-23. A person's request about their data goes to the legal adviser and is answered within the time in P-22; a personal data breach goes to the legal adviser, who decides on the report to the regulator as P-21 sets. Retention and disposal are built in (FR-074), and the impact assessment is completed before real data is held.

## 8 Secure by Design principles

These principles are fixed for every application built on the reference system. A departure from one is decided by the authorising official, not the system owner.

**Table 44: Principles and where the design meets them**

| Principle | What it means here | Where it is met |
| --- | --- | --- |
| Deny by default | Anything not expressly granted is refused, for people, services and network flows | NFR-001, NFR-007, NFR-041; section 7.2 |
| Least privilege | Each person, service and administrator has only the access their work needs | NFR-005, NFR-017, NFR-024 |
| No trust from network position | Being on the internal network grants nothing; every request is authenticated and authorised | Section 6.6, zone Z1; section 7.2 |
| Defence in depth | No single control stands alone: boundary, transport, identity, authorisation, data at rest, audit, host, recovery and people | Section 6.6 |
| Fail secure | An error, a time-out or a missing dependency refuses access | NFR-052 |
| Secure defaults | The application is secure as delivered: TLS on, rate limits on, no diagnostic pages, no default accounts | NFR-031, NFR-046, FR-063, FR-011 |
| No local credentials | Identity is \<Organisation\>'s; the application holds no passwords, and its secrets are in a key store | NFR-013, NFR-036, NFR-092 |
| Keep the attack surface small | Internal only, one route to the data, no outbound messages, no interface for other systems, only the components needed | Section 5.1.12; NFR-040, NFR-080 |
| Separation | User functions apart from management functions; each schema's data apart; duties apart | NFR-004, NFR-006, NFR-045 |
| Accountability | Every significant action is attributed to a person and recorded in a log that cannot be changed unnoticed | Section 7.6; NFR-025 |
| Privacy by design | Only the personal data needed, kept only as long as needed, with people's rights supported by the system | Section 5.1.11; section 7.14 |
| Secure development | Threats modelled, changes reviewed, releases built, tested and signed, components from one checked source | Section 7.12 |

The principles draw on CSS, NCSC's secure design principles and CISA's Secure by Design guidance.

## 9 Security, family by family

Table 45 gives each CSS control family, the reference design in brief, and the document that holds the full design, where every control is set out part by part. The number of controls in each family, and which are met by the system, shared, met by people, inherited or not applicable, are in \<Tailoring Register\>.

**Table 45: The control families**

| Family | Reference design in brief | Full design |
| --- | --- | --- |
| AC Access Control | Deny by default. Roles and schema access come only from Active Directory groups. Each schema has a read group and an edit group. The application has no session controls: session lock and termination come from the managed device and PingFederate (P-02, P-03). Duties are kept apart by separate groups. A system use notice is shown at sign-in, and access is reviewed on a schedule | \<Access Control Management\> |
| AT Awareness and Training | Nobody is added to a group until they have had \<Organisation\>'s awareness course and the application's briefing, and privileged roles complete role modules first. Repeated as P-24 sets | \<Awareness and Training Management\> |
| AU Audit and Accountability | One application audit log, written only by the API, with who, what, when, where and the result. Records are chained by a keyed hash, read only by auditors, reviewed and kept as P-07 and P-08 set | \<Audit and Accountability Management\> |
| CA Assessment, Authorization, and Monitoring | A self-assessment against every CSS determination statement, then an independent assessment; a plan of action; authorisation by a named official; continuous monitoring measures | \<Assessment, Authorization, and Monitoring Management\> |
| CM Configuration Management | A baseline for each release, changes approved by a change control board after a security impact analysis, CIS Benchmark settings, least functionality, and a check for drift | \<Configuration Management\> |
| CP Contingency Planning | Recover within P-12, losing at most P-13. Encrypted daily backups with transaction logs, a copy at a second site, and recovery tested as P-16 sets | \<Contingency Planning Management\> |
| IA Identification and Authentication | Every user signs in through \<Organisation\>'s PingFederate with multi-factor authentication. The application holds no accounts or passwords. Services use their own accounts and secrets held in a key store | \<Identification and Authentication Management\> |
| IR Incident Response | Report within the time in P-21, four severities with targets, playbooks, evidence preserved before clean-up, and personal data breaches to the legal adviser | \<Incident Response Management\> |
| MA Maintenance | Maintenance is approved first, done by known people with approved tools over \<Organisation\>'s managed route, checked afterwards and recorded | \<Maintenance Management\> |
| MP Media Protection | Items stay in the database. Exports are limited, encrypted, marked and removed; portable storage needs approval; media are sanitised to CSS | \<Media Protection Management\> |
| PE Physical and Environmental Protection | Provided by \<Organisation\> at its data centre and second site. The system owner checks its evidence each year and sets rules for offices and home working | \<Physical and Environmental Protection Management\> |
| PL Planning | A security plan, a privacy plan and rules of behaviour that every user signs, all checked for consistency before each issue | \<Planning Management\> |
| PM Program Management | Outside the baseline. Inherited from \<Organisation\>'s security and privacy programme | \<Program Management\> |
| PS Personnel Security | \<Organisation\> screens staff. Every role has a risk designation; access agreements are signed; a leaver's account is disabled at once | \<Personnel Security Management\> |
| PT PII Processing and Transparency | Personal data is processed only for the purposes in the profile. An inventory, a retention schedule built into the system, a search across schemas for people's requests, and an impact assessment | \<PII Processing Management\> |
| RA Risk Assessment | Categorised from the profile. A threat model, a risk list on the CSS method, a vulnerability timetable (P-11), and a list of critical components | \<Risk Assessment Management\> |
| SA System and Services Acquisition | Built in-house under the corporate SDLC, meeting CSS, with reviewed changes, a pipeline with automated tests and scans, verification to P-28, and external services reviewed yearly | \<System and Services Acquisition Management\> |
| SC System and Communications Protection | Deny by default at the firewalls and on each server, TLS on every flow, a register of every key, a strict page policy, and encryption at rest | \<System and Communications Protection Management\> |
| SI System and Information Integrity | Uploads are checked and scanned for malware, flaws are fixed to the timetable, logs are forwarded and eight events raise alerts, and releases are checked against a baseline | \<System and Information Integrity Management\> |
| SR Supply Chain Risk Management | A supplier register with criticality, every package through one checked source with lock files and a bill of materials, and each release inspected against its record | \<Supply Chain Risk Management\> |

## 10 What \<Organisation\> provides

An application built on the reference system relies on \<Organisation\> for much of its protection. These controls are inherited, and \<Organisation\> supplies the evidence for them; the requests are in \<Evidence Requests\>. A certification such as Cyber Essentials Plus or ISO/IEC 27001 supports these services but does not by itself prove a CSS control.

**Table 46: Services provided by \<Organisation\>**

| Service | What the application relies on |
| --- | --- |
| PingFederate and Active Directory | Authenticating every user with multi-factor authentication; lockout after failed sign-ins; accounts created, changed and disabled by its starters and leavers process; groups whose members only the owner can change |
| Network and firewalls | Only the application's flows allowed, at the network edge; network monitoring; denial-of-service protection |
| Remote access | One route in from outside: the VPN, from a managed device, with multi-factor authentication and no split tunnelling |
| Users' devices | Managed builds, disk encryption, screen lock, and removable storage blocked unless approved |
| Virtual platform and hardware | The servers, their hardware maintenance, firmware and physical security |
| Data centre and second site | Physical access control, power, fire and environmental protection; a second site for backups |
| Certificates, name resolution, time and proxy | A certificate authority, signed and validated name resolution, a time service and an authenticated proxy |
| Central logging | Receiving the application's logs, and giving the auditor the PingFederate and Active Directory events |
| ServiceNow | The access approval workflow, in which the Data Owner authorises each request and nobody approves their own; and prompt notice of leavers from the starters and leavers process |
| People | Pre-employment screening, the employee privacy notice, awareness training and the disciplinary process |
| Media | Storing, transporting and sanitising disks and backup media |

## 11 Questions and answers

These are questions an assessor is likely to ask, each with the reference answer and where the full answer is held. For a given application, check its profile in section 3 first.

**Table 47: Common questions**

| Question | Reference answer | Held in |
| --- | --- | --- |
| How do users authenticate? | Through \<Organisation\>'s sign-on service, with multi-factor authentication. The application holds no passwords | \<Identification and Authentication Management\> |
| How is access to an item decided? | By membership of the schema's read or edit group in the directory, checked on every request | \<Access Control Management\> |
| Who can see every item? | Administrators, by right of the role. Database administrators could by reaching the database, under an approved change only | \<Access Control Management\> |
| How is a leaver's access removed? | As P-06 sets | \<Access Control Management\> |
| What are the session limits? | The application has none of its own. The sign-in lasts as long as PingFederate allows (P-02), and the device screen lock hides it when idle (P-03) | \<Access Control Management\> |
| Is data encrypted in transit? | Yes, on every flow, as P-26 sets | \<System and Communications Protection Management\> |
| Is data encrypted at rest? | Yes: full-disk encryption on both servers, encrypted backups and encrypted export working copies | \<System and Communications Protection Management\> |
| Where are items stored? | In the database, each schema in its own database schema | Section 7.4 |
| Where are secrets kept? | In a key store, never in source code or settings files | \<System and Communications Protection Management\> |
| What is logged, and for how long? | The events in section 7.6, kept as P-07 sets | \<Audit and Accountability Management\> |
| Can an administrator change the audit log? | No. Only the API writes it, its database account can only add records, and the keyed chain shows any change | \<Audit and Accountability Management\> |
| Is the system reachable from the internet? | No. It is internal only | Section 6.5 |
| Are uploads scanned for malware? | Yes, each one, before it is stored | \<System and Information Integrity Management\> |
| How quickly are vulnerabilities fixed? | As P-11 sets | \<Risk Assessment Management\> |
| What are the recovery objectives? | As P-12 to P-14 set | \<Contingency Planning Management\> |
| What third-party software is used? | The reference stack in section 6.4, or the stack in the application's profile | \<Configuration Management\> |
| What external services does it depend on? | \<Organisation\>'s services in section 10; for building, the source repositories and the package feed | \<System and Services Acquisition Management\> |
| Does it hold personal data? | Yes, at least the identities in its audit records, and whatever the profile's information types hold | \<PII Processing Management\> |
| Which controls are inherited? | Those \<Organisation\> provides, listed in \<Tailoring Register\> | \<Assessment, Authorization, and Monitoring Management\> |
| Is the application authorised to operate? | Only once its authorising official signs the decision; see \<Security Assessment Report\> | \<Security Assessment Report\> |
| What happens if PingFederate or Active Directory is down? | Nobody can sign in. If Active Directory cannot be read, requests are refused | \<Concept of Operations\> |
| Is multi-factor authentication used for administrators? | Yes, for every user, through the sign-on service; and again on the VPN and the administration route | \<Identification and Authentication Management\> |

## 12 Terms and acronyms

Table 48 defines the terms used across the set, including those in \<Policy\>. Table 49 spells out the acronyms. Control family codes, such as AC and SR, are spelled out in \<System Security Plan\>, Table 8, and the rules and duties A, B and C in \<Security Operating Procedures\>.

**Table 48: Terms**

| Term | Meaning |
| --- | --- |
| Access | The ability to use \<System Name\> or its information, including reading, editing, exporting and administering |
| Access agreement | A signed undertaking: \<Organisation\>'s confidentiality agreement and the acknowledgement in \<Security Operating Procedures\>, section 9 |
| Account | A named Active Directory identity that a person or service uses to sign in to \<System Name\>, Windows or SQL Server. \<System Name\> holds no accounts of its own |
| Advisory | A security alert, warning or directive from an outside source, or an internal note made from one |
| After-action report | The record of a test or activation: what happened, against the objectives, and what will change |
| AMSI | The Windows Antimalware Scan Interface, through which an application asks the installed antivirus to scan data |
| API | The service the other two applications call, and the only route to the database |
| Application profile | Section 3: the facts and choices particular to one application |
| Appropriate policy document | The document the Data Protection Act 2018, Schedule 1, Part 4 requires when relying on certain Schedule 1 conditions |
| Approver | The people who must agree an access change before it is made: the person's line manager approves it in ServiceNow, and the group's owner authorises it, the system owner for a role group or the Data Owner for a schema group (P-37) |
| Assessment | Testing and examining controls to decide whether they work as intended. Level 1 is the system owner's self-assessment; Level 2 is the independent assessment |
| Audit information | Audit records, any log that repeats them, and the tools and settings used to read or manage them |
| Audit log | The store of audit records, the table dbo.AuditLog in the \<System Name\> database |
| Audit record | One entry that records an event: what happened, when, where, from where, the outcome and who was involved |
| Auditor | The person who reviews audit records and does not administer the system |
| Authenticator | Something used to prove an identity: a password, a second factor, a key or a secret |
| Authenticator assurance level | How sure the organisation is that the person signing in holds the account |
| Authorisation | The authorising official's decision, recorded on TPL-18, that \<System Name\> may operate and that its remaining risk is accepted |
| Authorisation package | What the authorising official receives before deciding, listed in \<Assessment, Authorization, and Monitoring Management\>, section 3.5 |
| Awareness | Messages and briefings that keep security in people's minds |
| Baseline | The approved, recorded configuration of a configuration item at a point in time, from which it can be rebuilt |
| Bill of materials | A list of every component in a release, with its version, supplier, hash and licence, in a machine-readable form |
| Built-in maintenance function | The fixed diagnostics page in the Admin application, which reads no item content. \<System Name\> has no page that changes its data or set-up |
| Business impact analysis | The analysis of how an outage harms the organisation over time, which sets the recovery objectives |
| Chain hash | A value calculated from each record and the one before it, so that a change can be detected |
| Change control board | The group that approves changes: the system owner, security officer and Windows server administrator |
| Change record | A record of a change. For a system change or maintenance job, TPL-6 or a ServiceNow record with the same fields; for a document, the change record described in \<Documentation Map\>, section 4.1 |
| Complaint | A complaint to the controller about how personal data is handled, under the Data (Use and Access) Act 2025 |
| Component | A software package, runtime, operating system or database that \<System Name\> is built from or runs on |
| Configuration item | Anything placed under configuration control: code, packages, components, settings or documents |
| Containment | Action that stops an incident spreading or causing more harm |
| Continuous monitoring | Checking controls, risks and changes on a set schedule after authorisation, under the strategy in \<Assessment, Authorization, and Monitoring Management\>, section 3.8 |
| Controlled area | A place where access is limited to authorised people: \<Organisation\>'s data centres and locked storage |
| Corporate SDLC | \<Organisation\>'s software development life cycle, inherited by \<System Name\>, whose security practices meet CSS: preparing the organisation, protecting the software, producing well-secured software and responding to vulnerabilities |
| Counterfeit | A component that is not what it claims to be, including a look-alike package |
| Critical component | A component whose failure or compromise would expose or lose the items, or defeat a security control (\<Risk Assessment Management\>, section 3.9) |
| Cryptographic erase | Sanitising encrypted media by destroying the keys, so the data can no longer be decrypted |
| Cryptoperiod | How long a key may be used before it must be changed |
| CSS | Cyber Security Standards: the control catalogue, baselines, assessment procedures and supporting standards the set is built on |
| Data centre | The \<Organisation\> facility that hosts \<System Name\>'s VMs |
| Data Owner | The person who owns a schema's data and its read and edit groups, and authorises who may read or edit it |
| Data protection key ring | The keys ASP.NET Core uses to protect each app's cookies and antiforgery tokens |
| Default branch | The branch in each repository that releases are built from |
| Departure | A part of an application that differs from the reference design, recorded in section 3.6 |
| Detection use case | A defined event or pattern, its source, threshold and the response to it |
| Digital media | Media that need power to be read, including virtual disks, export files and managed devices |
| Directory | \<Organisation\>'s Active Directory, which holds accounts and groups and which the API reads for group membership |
| Drift | Any difference between the running configuration and the baseline |
| Escort | A person on the approved list who supervises someone who is not |
| Event | An action or occurrence that \<Audit and Accountability Management\> says must be logged |
| Evidence | Records and copies kept to show what happened, with a hash and a record of custody |
| Exception | Written permission to depart from a requirement for a set period, recorded in \<Risk List\> |
| Exploited flaw | A vulnerability in CISA's Known Exploited Vulnerabilities catalogue, or confirmed as exploited by its vendor or \<Organisation\> |
| Export copy | A copy of items made by \<System Name\>'s export or download functions |
| External person | Someone who works on \<System Name\>, or assesses it, but is not employed by \<Organisation\>, such as a contractor, a supplier's engineer or an independent assessor |
| External service | A service run by someone else that \<System Name\> depends on, such as hosting, source code hosting or a package source |
| Flaw | A weakness in software or firmware that could be exploited, including a known vulnerability in a package |
| Flow | A permitted connection between two parts of the system, or between \<System Name\> and something outside it |
| Higher risk role | A role with privileged technical access, or one that can see or change security records |
| Identifier | The name that identifies one person or service. For a person it is their Active Directory account name |
| Identity assurance level | How sure the organisation is that a person is who they claim, from identity proofing |
| Immutable copy | A backup that cannot be changed or deleted for a set time, even by an administrator |
| Impact assessment | \<Data Protection Impact Assessment\>, the data protection impact assessment |
| Independent assessor | An assessor who has had no part in designing, building, running or administering \<System Name\>, and who confirms it on TPL-19 |
| Inheritance matrix | The table in \<Physical and Environmental Protection Management\> showing who provides each PE control and what evidence closes it |
| Inherited control | A control provided by \<Organisation\>, which supplies the evidence |
| Insider threat | Harm, deliberate or accidental, by someone with authorised access |
| Integrity baseline | The recorded hashes of a known-good release, used to detect later change |
| Item | A digital object the library holds in a schema, such as a scanned or electronic document, with its catalogue details and files |
| Key ring | The keys an application uses to protect its authentication cookie and anti-forgery tokens |
| Least privilege | Giving each person or process only the access its tasks need |
| Leaver, mover | Someone who leaves \<Organisation\> or stops needing \<System Name\>; someone who changes role |
| Lock file | A file that records the exact version and content hash of every package a .NET project restores |
| Logging failure | Any period in which agreed events are not recorded, for whatever reason |
| Loopback address | An address that can be reached only from the same server |
| Maintenance | Preventive or corrective work on a \<System Name\> component, including repair and replacement |
| Maintenance tool | Any program, device or function used to diagnose or maintain \<System Name\> |
| Marking | The \<Classification\> label, with the item's own classification, on what \<System Name\> shows or produces |
| Material change | A change to the rules that adds or tightens a rule, changes a consequence, adds monitoring or adds a privileged duty |
| Maximum tolerable downtime | The longest an outage can last before the harm is unacceptable |
| Media | Anything that holds \<System Name\> information outside the running application: disks, volumes, files, devices, backups and paper |
| Mitigate | Reduce a vulnerability's risk without the fix, for example by disabling the affected feature or blocking access to it |
| Mobile code | Code a page sends to run in the browser, such as JavaScript or WebAssembly |
| Multi-factor sign-in | Signing in with two different kinds of authenticator, such as a password and an app or key |
| Offline feed | The in-house checked package feed, held offline, whose packages are recorded with SHA-256 values |
| Parameter | A value the controls depend on, numbered P-nn in section 4, with a reference value an application keeps or changes |
| Personal data | Any information about an identified or identifiable living person |
| Personal data breach | A security incident leading to the accidental or unlawful loss, change, disclosure of, or access to personal data |
| Physical incident | Loss, theft, unauthorised entry, or a fire, flood or power event affecting \<System Name\> |
| Plan review record | A record of each review of a plan: who, their role, the date, the outcome and actions |
| Playbook | Pre-agreed first actions for a common kind of incident |
| Privileged access | Access that can change accounts, settings, security functions, servers or the database, or read audit records |
| Reconstitution | Checking the recovered system's data, functions and controls, and returning it to normal use |
| Record of processing | \<Organisation\>'s record of processing activities under UK GDPR, Article 30 |
| Recovery point objective | The most recent point to which data must be recoverable, which sets how much data may be lost |
| Recovery time objective | The longest a function can take to come back, which must be within the maximum tolerable downtime |
| Reference system | The design in this document, which every application in the series is built to |
| Remote (nonlocal) maintenance | Maintenance done over a network rather than in person at the component |
| Replay resistance | Protection against reusing a captured sign-in or token |
| Retention period | How long records are kept before they may be deleted |
| Risk | The chance that a threat source exploits a weakness, combined with the harm that would cause (CSS) |
| Risk designation | How much harm the holder of a role could do, which sets the screening and attention the role receives |
| Role training | Training in the security duties a person performs in their \<System Name\> role |
| Rules of behaviour | \<Security Operating Procedures\>: Part A for everyone, and Part B for privileged users |
| Sanitising | Making information on media impossible to recover, by clearing, purging, cryptographic erase or destruction |
| Schema | A set of items with its own read group and edit group, kept apart from every other schema |
| Screening | The checks an employer makes on a person before and during employment |
| Second site | An \<Organisation\> site, apart from the main one, that holds backups and can run rebuilt VMs |
| Secure by Design | Designing security and privacy into the system before it is built, so that it is secure by default, rather than adding controls afterwards |
| Secure release | Printing that holds a job until the user releases it at the printer |
| Security function | A part of \<System Name\> that enforces a control, such as sign-in, schema access or audit |
| Security impact analysis | The check, before a change, of its effect on security and privacy controls |
| Security incident | An event that harms, or may harm, the confidentiality, integrity or availability of \<System Name\> or its data, or breaks a security policy |
| Security-critical component | A component that \<System Name\>'s security depends on, listed in \<Maintenance Management\> |
| Separation of duties | Splitting duties so that no one person can misuse them together unnoticed |
| Service account | An account used by a program rather than a person |
| Severity | For an incident, the level from Low to Critical that sets how fast it is handled and who is told. For a vulnerability, the vendor's rating or, without one, its CVSS base score: 9.0 or more Critical, 7.0 to 8.9 High, 4.0 to 6.9 Medium, below 4.0 Low |
| Sign-on service | \<Organisation\>'s PingFederate single sign-on service, which authenticates users against Active Directory with multi-factor authentication |
| Significant change | A change likely to alter \<System Name\>'s security or privacy risk, as listed in \<Assessment, Authorization, and Monitoring Management\>, section 3.9 |
| Single sign-on | Signing in once, to \<Organisation\>'s PingFederate, which then vouches for the person to \<System Name\>. \<System Name\> never sees the password |
| Social engineering | Manipulating people into giving access or information, including by email, phone or in person |
| Special category data | Data about health, ethnicity, religion, trade union membership, sex life, sexual orientation, genetics or biometrics (UK GDPR, Article 9) |
| Supplier | Anyone who provides a component or service \<System Name\> depends on, including open-source projects and package registries |
| System plans | The System Security Plan, privacy plan and supply chain risk management plan, as in CSS |
| Tailoring | Deciding, with a rationale, that a baseline control or part does not apply, or applies in a changed form |
| Tampering | Any unauthorised change, deletion or addition of audit information |
| Third-party component | Any package, library or script \<System Name\> uses but did not write |
| Training matrix | The table of roles, modules, deadlines and frequencies in \<Awareness and Training Management\> |
| Trust anchor | A root certificate that the system trusts to issue other certificates |
| Vulnerability | A weakness in \<System Name\>, its components or its operation that a threat source could exploit |

**Table 49: Acronyms**

| Acronym | Meaning |
| --- | --- |
| --- | --- |
| AMSI | Antimalware Scan Interface, in Windows |
| API | Application programming interface |
| CE+ | Cyber Essentials Plus |
| CIS | Center for Internet Security |
| CISA | US Cybersecurity and Infrastructure Security Agency |
| CSS | Cyber Security Standards |
| DNS | Domain Name System |
| DPA | Data Protection Act 2018 |
| ECDSA | Elliptic Curve Digital Signature Algorithm |
| EV | Evidence request in \<Evidence Requests\> |
| HMAC | Hash-based message authentication code |
| HR | Human resources |
| HSTS | HTTP Strict Transport Security |
| HTTP, HTTPS | Hypertext Transfer Protocol, and its secure form |
| ICO | Information Commissioner's Office |
| IP | Internet Protocol |
| AD | Active Directory, \<Organisation\>'s directory service |
| LDAPS | Lightweight Directory Access Protocol over TLS |
| MFA | Multi-factor authentication |
| NC | Non-compliance entry in \<Risk List\> |
| NCSC | UK National Cyber Security Centre |
| NTP | Network Time Protocol |
| PII | Personally identifiable information |
| PIV | Personal Identity Verification, a US government card |
| PKI | Public key infrastructure |
| POA&M | Plan of action and milestones |
| PRO | Procedure in \<Procedures\> |
| RSA | Rivest-Shamir-Adleman, a public key algorithm |
| SCRM | Supply chain risk management |
| SDLC | Software development life cycle |
| SHA | Secure Hash Algorithm |
| SSP | System security plan |
| SyOps | Security operating procedures, \<Security Operating Procedures\> |
| TCP, UDP | Transmission Control Protocol, User Datagram Protocol |
| TLS | Transport Layer Security |
| TPL | Record form in \<Record Templates\> |
| TPM | Trusted Platform Module |
| TR | Tailoring entry in \<Tailoring Register\> |
| UK GDPR | UK General Data Protection Regulation |
| USB | Universal Serial Bus |
| UTC | Coordinated Universal Time |
| VM | Virtual machine |
| VPN | Virtual private network |
