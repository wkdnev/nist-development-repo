# \<System Name\> Concept of Operations

## 1 Purpose of this document

This document is used by every control family. It describes how \<System Name\> is intended to be used: why it exists, who uses it, the business processes it supports and how it works day to day. How it meets controls is in the SSP. The business details come from the business owner, and the users, information and functions follow \<System Description\>, sections 3.3 to 3.5.

## 2 Mission and purpose

\<System Name\> is an internal digital library. It gives \<Organisation\>'s staff and contractors one place to store, search and view digital items, such as scanned and electronic documents, with their catalogue details and files. Items are kept apart in schemas: each schema is its own database schema, with its own read group and edit group.

Teams need one controlled place to keep their items, so that the right people can find them quickly and others cannot see them. Keeping each schema's items apart lets one system serve several parts of the business.

The business owner is \[Name\] and the information owner is \[Name\] (\<System Description\>, section 3.2; \<Roles and Responsibilities\>). The business purpose and the processes it supports are in \<System Description\>, section 3.1. The benefits the business expects are: \[Benefits expected, from the business owner\].

## 3 User communities

\<System Name\> has no external or public users. Every role comes from an Active Directory group: the five role groups are owned by the system owner, and each schema's read group and edit group are owned by its Data Owner (\<System Description\>, section 3.3).

**Table 1: User communities**

| Community | What they do | Where |
| --- | --- | --- |
| Readers | Search and read items in their schemas, view and download files, and report a fault in an item | UI application |
| Editors | A reader's work, and create, upload, bulk upload, manage and bulk export the schema's items. Edit includes read | UI application |
| Administrators | Manage schemas, which groups open each schema (a change only with the Data Owner's approval), and system settings. Open no item content. There is one Administrator role and no separate global administrator | Admin application |
| Auditors | Read, search and export the audit log, and review it weekly (\<System Description\>, P-08). Hold no administration role | Admin application |
| Security officers | Read security information, review alerts and the central logs, and lead incident response. Do not read the audit log. Hold no administration role | Admin application |
| Business owners | Approve the disposal of items due under the retention schedule (\<System Description\>, FR-074) | UI application |
| Legal adviser's delegates | Search every schema for one person's items to answer a request under data protection law (\<System Description\>, FR-073). Hold no other role, and are named by the legal adviser | UI application |
| Data Owners | Own a schema's data and its two groups, and authorise who may read or edit it | ServiceNow and the directory |
| Server and database administrators | Run the servers and the database. Need no application role | The servers, only over \<Organisation\>'s managed administration route, with multi-factor authentication and named accounts (flow F11) |
| Developers | Build and fix the applications. Hold no administrator access on the servers | Development environment |

## 4 Business workflows

An item normally moves through four stages: it is added to a schema, found and read, corrected if something is wrong, and exported if it is needed elsewhere, until it is disposed of under the retention schedule. The business processes \<System Name\> will support are: \[Business processes, from the business owner\]. The functions particular to \<System Name\>, AF-001 onwards, are in \<System Description\>, section 3.5. Test and development use invented schemas and items only.

**Table 2: Business workflows**

| Activity | Who | What happens |
| --- | --- | --- |
| Find and read an item | Reader | Chooses one of their schemas, searches it, sorts and pages the results, opens the item and views its file in the browser, or downloads the original |
| Add items | Editor | Creates an item or uploads a file with its details, or bulk uploads a batch with a list of details. Each file is checked and scanned for malicious code before it is stored |
| Report a fault | Reader, editor | A reader reports a faulty item or file. An editor moves the report through its states and records the corrective action |
| Correct, replace or delete an item | Editor, administrator | An editor or administrator corrects an item's details. An administrator replaces a stored file or deletes an item. Each change is audited |
| Export a schema's items | Editor | Chooses items by filters and runs an export in the background, then downloads it. Taking exported items outside \<Organisation\>'s systems needs the Data Owner's decision |
| Manage schemas | Administrator | Creates, changes, deactivates and deletes schemas, and names each schema's read group and edit group |
| Start a new person | The person, their line manager, the group's owner | The person requests access in ServiceNow, their line manager approves it, and the group's owner authorises it: the Data Owner for a schema, the system owner for a role. The owner then adds the person to the Active Directory group. \<System Name\> creates no account |
| Remove a leaver | \<Organisation\>, the group owners | \<Organisation\> disables the person's Active Directory account at once, which ends their access, and the group owners remove their group memberships within 5 working days (\<System Description\>, P-06) |
| Check activity | Auditor, security officer | The auditor reads and searches the audit log, reviews it weekly (\<System Description\>, P-08), compares it with the server, database, PingFederate and Active Directory records, records the review, and reports anything suspicious to the security officer. The security officer reviews alerts and the central logs |
| Answer a request about personal data | Legal adviser and their delegate | The delegate finds every item about the person across all schemas, and the legal adviser answers within the time in P-22 |
| Dispose of items | Business owner | Items due under the retention schedule are listed, and deleted once approved. The disposal is recorded |

## 5 Operational scenarios

**Table 3: Operational scenarios**

| Scenario | Situation | What happens |
| --- | --- | --- |
| Answering a query | A reader needs a past item | They sign in, choose their schema, search and read it on screen |
| Adding a batch | An editor has a set of newly scanned items | They bulk upload them to the schema with their details, and readers can then find them |
| A poor scan | A reader finds a page is unreadable | They report a fault, and an editor or administrator corrects it and updates the report |
| A request for items | Someone needs a schema's items elsewhere | The schema's Data Owner decides, and an editor exports them as a download |
| Wrong schema | A user tries to open a schema they may not read | \<System Name\> shows the access-denied page, and they request access in ServiceNow, which their line manager approves and the schema's Data Owner authorises |
| Forgotten password or lockout | A user cannot sign in | \<Organisation\>'s IT service desk resets the Active Directory password or releases the lock, after checking who they are |
| Leaving a desk | A user walks away while signed in | The device's screen lock hides the screen after the inactivity time \<Organisation\> sets (\<System Description\>, P-03). The sign-in lasts no longer than PingFederate's sign-in lifetime (P-02) |
| A new starter or a leaver | Staff change | Access is requested and authorised for a starter, and removed for a leaver |

## 6 Operational concepts

### 6.1 Where it runs

It runs on \<Organisation\>'s internal network, on two Windows Server 2025 virtual servers in \<Organisation\>'s data centre: an application server, which runs the UI application, the Admin application and the API, each as a Windows service under its own managed service account, and a database server, which runs Microsoft SQL Server 2022. It is not reachable from the internet. Testing uses a separate, throwaway copy of the whole system, built from a tagged release, and development uses developers' computers; both hold invented data only.

### 6.2 How access works day to day

1. A person signs in through \<Organisation\>'s single sign-on, PingFederate, with multi-factor authentication against Active Directory. \<System Name\> holds no accounts and no passwords.
2. PingFederate's signed response names the person and carries no groups. The API reads the person's group memberships directly from Active Directory over LDAPS, and gives the roles and schema access those groups allow.
3. Their group memberships decide which schemas they see. Each schema names a read group and an edit group. A schema with no group is closed to everyone, and administrators open no item content.
4. The application's session is its authentication cookie. It ends 8 hours after sign-in at most, never later than PingFederate's sign-in (P-02), and when the person uses Sign out; an open page re-checks the person every 5 minutes, and the API refuses a disabled account or removed membership within 5 minutes. An unattended screen is locked by the operating system on \<Organisation\>'s managed devices (P-03).

### 6.3 Modes of operation

**Table 4: Modes of operation**

| Mode | What happens |
| --- | --- |
| Normal | Everyone can work as usual |
| PingFederate down | Nobody can sign in, because \<Organisation\>'s PingFederate authenticates every user and there is no local sign-in. People already signed in carry on until their sign-in ends at PingFederate's sign-in lifetime |
| Active Directory down | Nobody can sign in or be authorised. If the API cannot read a person's groups, it gives them no role and no schema, and refuses the request |
| API down | Nobody can work, because both applications reach the items only through the API |
| Database down | The API cannot read any data, so it refuses every request and nobody can open an item. People stay signed in |
| Maintenance | Users cannot reach \<System Name\>. Planned maintenance falls in the windows in P-32, and users get 2 working days' notice |

These modes come from reading the design.

### 6.4 How it is kept secure in operation

Each part of operation, from changes, patching and monitoring to backups, incidents, training, maintenance, media, buildings, people, personal data, suppliers and authorisation, is designed in its family's design document, listed in \<Documentation Map\>, Table 2. The day-to-day duties and the rules everyone signs are in \<Security Operating Procedures\>. No real data is held until \<System Name\> is authorised.

## 7 Open questions

1. Which \<Organisation\> staff will use \<System Name\>, and from where? \[Teams and locations, from the business owner\].
2. Who is the Data Owner of each schema? \[Name and role for each schema, from the business owner\].
3. Which business processes will \<System Name\> support, and what are the expected benefits? See sections 2 and 4.
4. What hours must it be available, and how many users, schemas and items are expected? \[Hours, and numbers of users, schemas and items, from the business owner (\<System Description\>, P-32 and P-33)\].
