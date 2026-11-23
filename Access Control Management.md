# \<System Name\> Access Control Management

## 1 Purpose

This document is the access control design for \<System Name\>. It covers the Access Control (AC) family of the CSS Moderate baseline, 39 controls and enhancements.

Section 3 is the design: the account types, roles, permissions, separation of duties, access routes, settings and rules, the access request workflow, ending access, sign-in lifetime and device lock, the system use notice, actions allowed without signing in, audit, and remote, wireless and mobile access.

As \<System Description\> sets out, \<Organisation\>'s PingFederate authenticates every user, with multi-factor authentication, and \<System Name\>'s API reads each user's groups directly from Active Directory over LDAPS, to give their roles and schema access. \<System Name\> holds no accounts or passwords of its own. The API reads each person's groups, and confirms their account is enabled, on every request, holding the answer for at most 5 minutes. \<System Name\>'s own session is its authentication cookie, which lasts at most 8 hours, is re-checked every 5 minutes and ends on Sign out. An unattended screen is locked by \<Organisation\>'s managed devices.

## 2 Related documents

The policy is in \<Policy\> (AC), and the steps people follow are in \<Procedures\> (AC). Which section of this design meets each control, who is responsible for it and its status are in \<System Security Plan\>, section 7.1 (Table 10). The assessment is in \<Control Assessment Record\> (AC), the risks are in \<Risk List\>, and open work is in \<Plan of Action and Milestones\>.

## 3 The access control model

### 3.1 Principles

1. **Deny by default.** Nothing is allowed unless a role or group grants it. A schema with no group is closed to everyone.
2. **One person, one account.** Each person uses their own Active Directory account. Accounts are never shared, and \<System Name\> holds no accounts or passwords of its own.
3. **Schemas are the boundary.** Each schema has a read group and an edit group, owned by its Data Owner. Edit includes read.
4. **AD groups decide everything.** A person's role groups set what they can do, and their schema groups set which schemas they can do it in. All are Active Directory groups, which the API reads from Active Directory over LDAPS on every request, together with whether the account is enabled. It holds each answer in memory for at most 5 minutes, and stores no group in the cookie, so a removal takes effect within 5 minutes.
5. **Application users have no server access.** Windows and SQL Server administration use separate accounts.
6. **Only the API reaches the database.** The UI app and the Admin app get all their data through the API. The API connects with Windows authentication under its own managed service account, which is not a sysadmin and cannot change the schema.
7. **\<Organisation\>'s single sign-on proves who the user is.** PingFederate authenticates every user, with multi-factor authentication, and gives \<System Name\> a signed OpenID Connect response that names them. \<System Name\> never sees a password.
8. **The cookie is the session.** \<System Name\>'s session is its authentication cookie: 8 hours from sign-in at most, never longer than PingFederate's sign-in, re-checked every 5 minutes on an open page, and ended by Sign out. It has no idle lock, idle timeout or limit on sessions at once; the device screen lock hides an unattended screen.
9. **Administrators see no item content.** The Administrator role manages schemas and settings only. Item content is reached only through a schema's read or edit group, or by the business owner and the legal adviser's delegate for their own tasks.

Figure 1 shows the checks every request passes. Every request passes four checks in order: sign-in through PingFederate, which authenticates the user with multi-factor authentication, shown by the app's valid authentication cookie; the user's AD groups and account state, read from Active Directory by the API over LDAPS for each request and held for at most 5 minutes; the schema decision, read or edit, from those groups; and the role group needed for the page or function. Anything not granted is refused.

The access control library, built into all three apps, makes the schema decisions. Role policies on each page and controller make the function decisions. All three apps, the API included, apply a default rule that requires a signed-in person, and refuse any page or function that states no access rule; only the actions in section 3.17 are open. Every item and file address names the schema, and no address works without it. Item content is sent so that it is not kept in shared caches.

![Figure 1: How an access decision is made](figures/acm-figure-1.png)

**Figure 1: How an access decision is made**

### 3.2 Account types

Every person signs in with their Active Directory account, through PingFederate. The types below are the kinds of access an account may hold.

**Table 1: Account types**

| Type | Held by | Allowed | Rules |
| --- | --- | --- | --- |
| Standard user | Readers | Yes | Their own AD account; member of a schema's read group only |
| Schema editor | Editors | Yes | Their own AD account; member of a schema's edit group |
| Auditor | Auditors | Yes, privileged | Their own AD account; holds no administration role |
| Security officer | Security officers | Yes, privileged | Their own AD account; holds no administration role |
| Business owner | The business owner | Yes, privileged | Their own AD account; approves the disposal of items due under the retention schedule |
| Legal adviser's delegate | The person the legal adviser names | Yes, privileged | Their own AD account; holds no other role |
| Administrator | Administrators | Yes, privileged | Their own AD account; the system owner authorises and adds them to the group; opens no item content; a separate everyday account for any item work |
| Windows administrator | Windows server administrators | Yes, privileged | Named person, only over \<Organisation\>'s managed administration route, with multi-factor authentication (F11) |
| Database administrator | SQL Server database administrators | Yes, privileged | Named person, only over \<Organisation\>'s managed administration route, with multi-factor authentication (F11), for approved maintenance only |
| API service account | The API only | Yes, privileged | The API's group managed service account, which signs in to SQL Server with Windows authentication and reads group membership from Active Directory over LDAPS. Nobody signs in with it. Not a sysadmin, and cannot change the schema (section 3.6) |
| Local \<System Name\> account | Nobody | No | \<System Name\> holds no accounts or passwords of its own. The first administrator is simply the first member of that AD group |
| Temporary and emergency | Nobody | No | Prohibited |
| Supplier or \<Organisation\> engineer doing maintenance | Nobody | No | Holds no account on the servers or in \<System Name\>; watches and guides over the shared screen of an approved administrator, who drives the session (\<Maintenance Management\>, section 3.6) |
| Shared, guest, anonymous and demonstration | Nobody | No | Prohibited on the servers |

Temporary and emergency accounts are prohibited, so there is nothing to remove or disable automatically. Each access review confirms that none exists. If such accounts were ever needed, they would be Active Directory accounts with an end date, and the tailoring decision would be made again.

Shared and group accounts are prohibited, and \<System Name\> holds no passwords, so there is no shared password to change when someone leaves a group.

### 3.3 Roles

**Table 2: Roles**

| Role | Purpose | Granted through | Group owner, who authorises and manages its members |
| --- | --- | --- | --- |
| Reader | Read items in a schema | The schema's read group, an AD group | The schema's Data Owner |
| Editor | Add, manage and export items in a schema | The schema's edit group, an AD group | The same |
| Administrator | Manage schemas, the AD groups each schema uses (a change of groups only with the Data Owner's approval), and settings; use the administration dashboard. No item content | AD group \<Code\>\_Admins | System owner |
| Auditor | Read the audit log and review it weekly | AD group \<Code\>\_Auditors | System owner |
| Security officer | Read security information; run the last sign-in report and the monthly check of members who have not signed in for 90 days. Does not read the audit log | AD group \<Code\>\_Security | System owner |
| Business owner | Approve the disposal of items due under the retention schedule | AD group \<Code\>\_BusinessOwners | System owner |
| Legal adviser's delegate | Search every schema for one person's items to answer a request under data protection law. Holds no other role | AD group \<Code\>\_LegalSearch, whose member the legal adviser names | System owner |

The people who hold each role are named in \<Roles and Responsibilities\>. The group names use the application's short code, and are confirmed when the groups are created in Active Directory.

Each group's owner adds and removes its members in Active Directory, with \<Organisation\>'s AD tool, as the last step of an approved request (section 3.13). \<System Name\>'s API reads each person's groups from Active Directory over LDAPS, with read-only rights, and cannot change them.

The authorised users of \<System Name\> are the members of its AD groups. Each person's groups are their access, and the approved source for each membership is its ServiceNow request. \<Organisation\> manages the AD accounts themselves. The administrator manages schemas, and which AD groups open each, in \<System Name\>'s Admin app; a change to a schema's groups needs that schema's Data Owner's approval in a change record.

The five role groups, for administrators, auditors, the security officer, the business owner and the legal adviser's delegate, are privileged. The system owner is their only owner, and authorises each member after role training and a signed Part B of \<Security Operating Procedures\>. An administrator cannot add anyone to a group. On the servers, privileged access is held through Windows administrator group membership and SQL Server roles, and only the named Windows server and database administrators may sign in (section 3.6.2). The API's database service account is privileged and headless, and is managed by the database administrator.

### 3.4 Permissions

**Table 3: Permissions by role**

| Function | Who may do it |
| --- | --- |
| Search and read items | Readers and editors, in their own schemas. The legal adviser's delegate sees search results for one person. The business owner sees only the details of items due for disposal, not their content |
| Report a faulty item | Readers and editors, in their own schemas |
| Upload, correct, replace, delete and export items | Editors, in their own schemas |
| Manage users, passwords and group membership | Nobody in \<System Name\>: it is done in Active Directory, by each group's owner |
| Manage schemas, and which AD groups open each | Administrators. A change of groups, or deactivating, reactivating or deleting a schema, needs the Data Owner's approval. Only an empty schema can be deleted |
| Grant administrator | Nobody in \<System Name\>: the system owner adds the member to the AD group |
| Use the administration dashboard and settings | Administrators |
| Read audit logs | Auditors |
| Read security information | The security officer |
| Run the last sign-in report | The security officer |
| Approve the disposal of items due under the retention schedule | The business owner |
| Search every schema for one person's items, for a request under data protection law | The legal adviser's delegate |

Administrators see no item content. Any item work an administrator does is as a reader or editor, through a schema group given to their everyday account. The business owner approves disposals, and the legal adviser's delegate runs their search, in the UI application. The disposal page shows each item's schema, reference, title, type, date and retention period, but not its content or files; to look inside an item, the business owner asks that schema's Data Owner. An administrator cannot delete a schema that still holds items: a schema in use is retired by deactivating it, and its items leave only by disposal.

### 3.5 Separation of duties

1. Nobody approves their own access or privilege.
2. Nobody reviews their own access or their own privileged actions.
3. Auditors and security officers hold no administration role, and the legal adviser's delegate holds no other role.
4. Application, Windows and database administration use separate accounts, held by different people where staffing allows.
5. Developers hold no administrator access on the servers.
6. Where staffing cannot meet a rule, it is recorded as an exception, with a compensating check.

Table 4 shows each pair of duties that one person must not hold together, the roles that carry them, and what keeps them apart.

**Table 4: Duties kept apart**

| Duty | Must be separate from | Roles | Kept apart by |
| --- | --- | --- | --- |
| Asking for access | Approving and granting it | The person asks; their line manager approves; the group's owner authorises, and adds them to the AD group | The ServiceNow workflow, in which nobody can decide their own request, and Active Directory, where only a group's owner can change its members (section 3.13) |
| Changing which groups open a schema, or deactivating or deleting it | Deciding who may see the schema's items, and when they are disposed of | The administrator makes the change; the schema's Data Owner approves it; only the business owner approves disposal of items | A change record approved by the Data Owner, an audit record with its reference, and an alert to the security officer (U9) |
| Administering schemas and settings | Reviewing audit logs | Administrator administers; auditor reviews | Separate access groups: only the auditor group opens the audit log pages, and it opens no administration page |
| Administering the system | Reading security information | Administrator administers; security officer reads | Separate access groups |
| Searching every schema for one person's items | Any other role | Legal adviser's delegate | A separate access group, whose member the legal adviser names; the delegate holds no other role |
| Holding administrator | Granting it | Administrators; the system owner, who alone manages that AD group | Active Directory: an administrator cannot add a member to the group |
| Application administration | Windows administration and database administration | Administrator; Windows server administrator; SQL Server database administrator | Separate accounts on separate layers, held by three different people (\<Roles and Responsibilities\>) |
| Development | Production administration | Developers; Windows server and database administrators | Developers hold no administrator account on the servers |
| Granting role-group access | Reviewing it | The system owner grants and prepares each role-group review; the auditor checks and signs it; the Head of Cyber reviews the system owner's own memberships | Procedure |
| Holding access | Reviewing that access | Each account holder; the auditor, Data Owners, system owner and security officer review | Procedure: nobody reviews their own access |

### 3.6 Access routes

Figure 2 shows \<System Name\>'s boundary and the routes into and inside it. It is the boundary figure of \<System Description\>.

![Figure 2: System boundary and access routes](figures/sd-figure-1.png)

**Figure 2: System boundary and access routes**

**Table 5: Access routes**

| Route | Used by | Design |
| --- | --- | --- |
| Sign-in | Everyone | The browser is sent to \<Organisation\>'s PingFederate (F6), which authenticates the user with multi-factor authentication and returns a signed OpenID Connect response naming them. The app completes the sign-in with PingFederate from the application server (F10). The API then reads their groups from Active Directory over LDAPS. \<System Name\> has no sign-in of its own |
| Browser to the UI app | Readers, editors, the business owner and the legal adviser's delegate | HTTPS on \<Organisation\>'s network, after signing in |
| Browser to the Admin app | Administrators, auditors and the security officer | HTTPS, over \<Organisation\>'s managed administration route only |
| Apps to the API | The apps only | Inside the application server; people do not connect directly |
| API to the database | The API's service account only | Application server to database server only, using TLS with strict encryption and Windows authentication. The UI app and the Admin app have no database connection |
| Windows administration (F11) | Windows server administrators | Named accounts, from managed devices, only over \<Organisation\>'s managed administration route, with multi-factor authentication |
| Database administration (F11) | Database administrators | Named accounts, from managed devices, only over \<Organisation\>'s managed administration route, with multi-factor authentication, for approved maintenance only |
| Remote access | Approved users; administrators only for approved changes, maintenance and incident response | \<Organisation\>'s VPN, with multi-factor authentication. Privileged work then goes only through the managed administration route, with multi-factor authentication again |
| Without signing in | Anyone | Only the actions listed in section 3.17 |
| API to Active Directory | The API's service account only | LDAPS, TCP 636, read-only, to read the signed-in person's group memberships |
| Outside services | None | Browsers load all code from \<System Name\> itself |

**Table 6: Server and database access**

| Layer | Who | Rule |
| --- | --- | --- |
| Windows on both VMs | Windows server administrators | Named accounts, only over \<Organisation\>'s managed administration route, with multi-factor authentication (F11) |
| SQL Server administration | Database administrators | Named accounts, only over \<Organisation\>'s managed administration route, with multi-factor authentication (F11), for approved maintenance only |
| API to SQL Server | The API's managed service account | Windows authentication; the rights in the table below. The UI app and the Admin app do not connect |
| App service accounts on Windows | One for each app | Group managed service accounts; cannot sign in interactively; not administrators (Table 8) |

Only the API connects to the database.

**Table 7: Database accounts and their rights**

| Account | Used by | May | May not |
| --- | --- | --- | --- |
| API's managed service account, \[name to be set at build\] | API only. Headless: no person signs in with it | Read and write application data. Add audit records | Be a sysadmin. Create, alter or drop tables. Change or delete audit records. Connect from anywhere but the application server |
| Schema change account, \[name to be set at build\] | The database administrator, at a release, under an approved change | Create and alter the tables | Be used by any app, or for everyday work |
| Database administrators' own accounts | Each database administrator, by name | Administer SQL Server, for approved maintenance | Be shared |
| Built-in sa login | Nobody | Nothing: it is disabled, and SQL Server accepts Windows authentication only | Be enabled, or used by any person or app |

These rules follow from it:

1. **No passwords.** \<System Name\> stores no passwords or password hashes, because PingFederate authenticates every user.
2. **Items and schemas.** The UI app asks the API for item data. The Admin app asks the API for schemas, the groups each uses, settings and audit records, and gets no item content.
3. **Audit log.** The service account can add and read records, and cannot change or delete them. Nothing changes them, and the database administrator removes them only once archived. They are read only through the Admin application's audit pages, by the auditor role. The one exception is the last sign-in report, which shows the security officer each member's username and last sign-in date, and nothing else.
4. **Changes to the database structure.** Only the database administrator makes them, with the schema change account.
5. **Connection.** The API connects only from the application server, over TLS with strict encryption, using Windows authentication under its managed service account. There is no database password to store.

#### 3.6.1 Windows service accounts

Each app runs under its own Windows account, so a fault in one app cannot reach another's files.

**Table 8: Windows service accounts**

| Runs | Account | May | May not |
| --- | --- | --- | --- |
| UI application | \[name to be set at build\] | Log on as a service on the application server | Be an administrator. Sign in at the console or by remote desktop. Be used by a person |
| Admin application | \[name to be set at build\] | The same | The same |
| API | \[name to be set at build\] | The same. It signs in to SQL Server with Windows authentication and reads Active Directory over LDAPS, so it holds no database password | The same |

Each is a group managed service account in \<Organisation\>'s Active Directory. Windows sets and changes its password, and no person knows it.

Each is a managed service account in \<Organisation\>'s Active Directory, with no interactive sign-in, whose password Windows sets and changes.

#### 3.6.2 Who may sign in to the servers

**Table 9: Sign-in to the servers**

| Server | May sign in | How | May not |
| --- | --- | --- | --- |
| Application server | The named Windows server administrators | Their own named administrator accounts, only over \<Organisation\>'s managed administration route, with multi-factor authentication (F11) | Developers, application users, the service accounts, and any shared account |
| Database server | The named Windows server administrators, and the named database administrators | The same | The same |

The holders are named in \<Roles and Responsibilities\>. \<Organisation\> creates and removes these accounts through its ServiceNow process, with the system owner's approval.

#### 3.6.3 File permissions on the application server

**Table 10: File permissions**

| Files | Read | Write | Notes |
| --- | --- | --- | --- |
| Each app's program folder | That app's service account; Windows server administrators | Windows server administrators only, at a release | An app cannot change its own code |
| Each app's settings and secrets | That app's service account; Windows server administrators | Windows server administrators only | Secrets are kept out of the code repositories. The token signing key and the audit chain key are readable only by the API's account; the OpenID Connect client credential only by the UI and Admin applications' accounts |
| Each app's key ring, which protects its authentication cookie | That app's service account | That app's service account | Protected with Windows DPAPI |
| Each app's logs | Windows server administrators | That app's service account | Kept for 30 days, and forwarded to central logging, where the auditor reads them |
| The export working folder | API's service account | API's service account | Holds an export only until it is downloaded |

Item files are held in the SQL Server database, each schema in its own database schema. No item is held as a file on a share.

#### 3.6.4 Firewall rules

\<Organisation\>'s corporate network team writes, holds and changes every firewall rule, through its own change process. The \<System Name\> team cannot see or change a rule. \<System Name\> states the flows it needs, in Table 11, and \<Organisation\> allows those and nothing else.

**Table 11: Flows \<System Name\> asks \<Organisation\> to allow**

| Flow | From and to | Service | Needed for |
| --- | --- | --- | --- |
| F1 | Users' managed devices, in the office or on the VPN, to the application server | HTTPS, TCP 443 | The UI app |
| F2 | Administrators, auditors and the security officer, over \<Organisation\>'s managed route, to the application server | HTTPS, on a port or host name still to be set | The Admin app |
| F3, F4 | The UI app and the Admin app to the API, on the application server's own loopback address | HTTPS | Needs no firewall rule: it never leaves the server |
| F5 | Application server to database server | SQL Server over TLS 1.2 or later with strict encryption, TCP 1433 | The API's database connection |
| F6 | Users' and administrators' browsers to \<Organisation\>'s PingFederate | HTTPS | Signing in. Both ends are \<Organisation\>'s, so this needs no rule for \<System Name\>'s servers |
| F7 | Application server to \<Organisation\>'s Active Directory domain controllers | LDAPS, TCP 636 | The API reading each signed-in person's group memberships |
| F8 | Both servers to \<Organisation\>'s time service, central logging, proxy and backup site | As \<Organisation\> sets: logs, updates and backups encrypted; time by NTP, authenticated where the service allows | Accurate audit times, log forwarding, updates and backups |
| F10 | Application server to \<Organisation\>'s PingFederate | HTTPS, TCP 443 | The UI app and the Admin app fetching PingFederate's OpenID Connect metadata and signing certificate, and completing each sign-in |
| F11 | Server and database administrators' managed devices, over \<Organisation\>'s managed administration route with multi-factor authentication, to both servers | Tool and protocol to be supplied by \<Organisation\> | Server and database administration, using named accounts |
| None: infrastructure | Both servers to \<Organisation\>'s DNS, domain controllers and certificate authority; the vulnerability scanner and \<Organisation\>'s discovery tools to both servers | DNS, domain and revocation list traffic, and scanning, allowed only on the ports \<System and Communications Protection Management\>, section 3.2, lists for them | Name resolution, domain membership and Kerberos, certificate revocation checks, and scans. These carry no \<System Name\> data |

Everything else should be refused, in and out. \<System Name\> needs no route to the internet, as browsers load all code from \<System Name\> itself. The applications fetch PingFederate's OpenID Connect metadata and signing certificate, which checks its sign-in responses, from \<Organisation\>'s PingFederate (F10), and fetch nothing from an outside host. ServiceNow and the starters and leavers process (F9) have no connection to \<System Name\>.

What \<System Name\> itself controls is limited to its own servers: the API listens only on the loopback address, each app accepts only HTTPS, the API accepts requests only from the two apps' addresses, and each server's host firewall allows only the rules in \<System and Communications Protection Management\>, section 3.2.

#### 3.6.5 What \<Organisation\>'s corporate configuration provides

![Figure 3: Who provides each part of access control](figures/acm-figure-3.png)

**Figure 3: Who provides each part of access control**

These are set by \<Organisation\> as part of its corporate network, directory and device configuration, and the \<System Name\> team has no control over them. The reference value of each is in \<System Description\>, section 4. Table 12 says what \<System Name\> relies on.

**Table 12: Provided by \<Organisation\>'s corporate configuration**

| Provided | What \<System Name\> relies on |
| --- | --- |
| Single sign-on: PingFederate | Every user is authenticated by PingFederate, with multi-factor authentication. Repeated failed sign-ins lock the account: 10 failed attempts within 15 minutes lock it for 15 minutes. The OpenID Connect response \<System Name\> receives is signed. PingFederate's sign-in lifetime for \<System Name\> is at least 8 hours, so \<System Name\>'s own 8-hour session always ends within it. PingFederate ends its sign-in when the person uses Sign out |
| Accounts and groups: Active Directory | Each person has one AD account, created, changed and disabled by \<Organisation\>'s starters and leavers process. A disabled account can no longer sign in, and \<System Name\>'s API refuses it within 5 minutes. Only a group's owner can change its members. The API reads group membership over LDAPS |
| Account lockout on the servers and on users' devices | Repeated failed Windows sign-ins lock the account |
| Logon banner on the servers | A system use notice before an administrator signs in to Windows |
| Screen lock on the servers and on users' devices | An unattended screen locks after 15 minutes of inactivity, hides what was on it, and needs the password to unlock. As \<System Name\> has no page lock of its own, this is the only session lock |
| Remote access | One route in from outside: the VPN, from a managed device, with multi-factor authentication, encrypted, logged and monitored, through one managed gateway |
| Privileged remote access | An administrator working remotely comes in through the VPN and then the managed administration route, with multi-factor authentication at both, only for approved changes, maintenance and incident response. The servers' administration ports cannot be reached from external networks any other way |
| Wireless | Corporate wireless authenticates users and devices and is encrypted; the servers have no wireless |
| Device controls | Managed laptops are the only mobile devices allowed, configured by \<Organisation\> with full-device encryption; phones and tablets cannot reach \<System Name\>; unmanaged devices are kept off the network; USB storage is blocked unless approved |

\<System Name\>'s own settings for these controls are its sign-in session (section 3.15) and its system use notice (section 3.16). \<System Name\> has no page lock of its own.

### 3.7 Settings

The values the access controls depend on are listed in Table 13. Lockout and multi-factor authentication are PingFederate's and are not set in \<System Name\>. The session lifetime is a fixed 8 hours set in \<System Name\>; PingFederate's own sign-in lifetime is set to at least that. The policy review and ownership values are in \<Policy\>, section 1.1.

**Table 13: Access control values**

| Setting | Value |
| --- | --- |
| Accounts and their attributes | Account types: as listed in Table 1. Account attributes: the AD account name and ID, line manager, enabled state and expiry date; access attributes: the person's role groups and schema read or edit groups. Who decides access: the line manager approves in ServiceNow, then the group's owner (the system owner for a role group, the Data Owner for a schema group) authorises and adds the person. Leavers: AD account disabled at once and group memberships removed within 5 working days; movers: group owners told within 1 working day. Access reviews: role groups every 3 months, schema groups every 12 months, server and database accounts every 6 months |
| Temporary and emergency accounts | Temporary and emergency accounts are not allowed |
| Inactive accounts | AD accounts unused for 90 days are disabled within 1 working day; each month, members of \<System Name\>'s groups who have not signed in for 90 days are removed |
| Signing out | Users sign out at the end of each working day, and whenever they leave their device for longer than a short break |
| Screen lock | Device screen lock after 15 minutes of inactivity, on users' managed devices and on both servers |
| Sign-in lifetime | Sign-in lifetime of 8 hours from sign-in, with no sliding extension |
| High-risk individuals | A high-risk individual's AD account is disabled within 1 hour of notice |
| Privileged functions and their logging | The privileged functions and security-relevant information in section 3.8; all privileged functions are logged |
| Non-privileged accounts for everyday work | Administrators use a separate non-privileged account for everyday item work |
| Review of privileges | Role group members reviewed every 3 months; server and database accounts every 6 months |
| Failed sign-ins | 10 failed sign-ins within 15 minutes lock the account for 15 minutes |
| System use notice | The system use notice wording in section 3.16 |
| Sign-ins at once (beyond the baseline) | No limit on sign-ins at once |
| Actions without signing in | The actions in section 3.17, and nothing else, are allowed without signing in |
| Remote access | Remote access only through \<Organisation\>'s VPN, from a managed device, with multi-factor authentication |
| Privileged remote access | Privileged access over remote access only for approved changes, maintenance and incident response, through the VPN and then the managed administration route, with multi-factor authentication at both |
| Wireless and mobile devices | Corporate wireless authenticates user and device (802.1X) and is encrypted (WPA2 or WPA3 Enterprise); managed laptops with full-device encryption are the only mobile devices allowed |
| External systems and portable storage | External systems and portable storage not allowed without the system owner's written approval on the exception request; an approved external system needs a contract with confidentiality terms, encryption at rest, storage in the United Kingdom only, and deletion when the need ends |
| Sharing outside a schema | The Data Owner decides on sharing outside a schema |
| Public content | No public content, unless the system owner approves |

### 3.8 Privileged functions and security information

**Privileged functions:** managing schemas and the AD groups each uses, including deactivating and deleting empty schemas; approving a change to a schema's groups or its deactivation or deletion; changing settings; running diagnostics; reading audit logs; running the last sign-in report; approving the disposal of items due under the retention schedule; searching every schema for one person's items; and database maintenance. Managing the members of the five role groups is also privileged, and is done in Active Directory by the system owner as their owner.

**Security-relevant information:** secrets and security settings, the OpenID Connect client credential, PingFederate's signing certificate, access groups and schema access rules, audit logs, firewall rules and certificates.

Only the privileged roles in Table 1 may use these: administrators, auditors, the security officer, the business owner, the legal adviser's delegate, the system owner as owner of the role groups, and the Windows server and database administrators. Their use must be logged (section 3.18).

**Data Owners are not privileged users.** A Data Owner approves a change to their own schema's groups, authorises access to them, and adds and removes their members. These are business decisions about their own schema, not privileged access: each is logged, approved in ServiceNow or a change record, and reviewed at the access review. Data Owners therefore sign Part A of \<Security Operating Procedures\> only, not Part B, and module M2 trains them for these duties.

Security functions in hardware and firmware, namely the physical hosts, the network equipment and the host firmware, are held by \<Organisation\>'s network and infrastructure teams, under \<Organisation\>'s own access lists.

These rules apply:

1. **Checked where it runs.** Each privileged function checks the caller's role where the function runs, not only in the menu, through the role policies on every Admin application page and API controller. Table 3 says which role may run each. Everything else is refused.
2. **Information kept to the roles.** Role policies on the Admin application's pages, database rights and file permissions on the servers keep the security information to the roles that need it. Secrets are kept out of the code repositories, and each app's secrets are readable only by that app's service account and the Windows server administrators (section 3.6.3).
3. **A separate everyday account.** Each administrator has two AD accounts: a privileged one for administration, and an everyday one for item work. They use the privileged account only for the privileged task in hand, and never to browse the web, read email, join meetings or chat (\<Security Operating Procedures\>). The system supports the rule: the Administrator role opens no item content, so item work is possible only through schema groups, which the Data Owner gives to the everyday account. That privileged accounts are not put in schema groups is checked at each access review.
4. **Nothing extra in production.** No test page, and no diagnostic beyond the fixed checks that read no item content, is present in production.

### 3.9 Export and download rules

1. Only editors of a schema may bulk export its items.
2. An export job can be seen, downloaded or cancelled only by the person who started it.
3. Exports are delivered as downloads. Writing exports to a server folder is not allowed.
4. Exported items stay under the schema's access rules, and leaving \<Organisation\>'s systems needs the system owner's written approval for the external system and the Data Owner's decision to share outside the schema (section 3.10, items 1 and 4).
5. Every export is recorded in the audit log.

### 3.10 Information sharing rules

1. Sharing outside a schema needs a decision by that schema's access approver, its Data Owner. It is a manual decision, outside \<System Name\>.
2. The approver checks that the recipient is authorised for the information, and the decision is recorded on a sharing decision record. Exported items stay under the schema's rules.
3. Inside \<System Name\>, the schema groups control sharing. Sharing outside is a manual decision.
4. External systems and portable storage may hold \<System Name\> data only with the system owner's written approval, recorded as an exception on the exception request. None is approved. An approved external system must meet these terms: a contract with confidentiality terms, encryption at rest, storage in the United Kingdom only, and deletion when the need ends.
5. Personal devices, personal cloud storage and any unmanaged system are prohibited: exported files are saved only in approved \<Organisation\> locations, \<System Name\> is used only on a managed device, and no outside service or AI tool is used without the system owner's written approval (\<Security Operating Procedures\>). \<Organisation\>'s network access control keeps unmanaged devices off the network.
6. USB and other portable storage may not hold \<System Name\> data without the system owner's approval, recorded as an exception on the exception request (\<Security Operating Procedures\>). \<Organisation\>'s device control on managed devices enforces this. Portable storage issued under an exception may be used only on \<Organisation\>'s managed devices and the external system named in the approval, must never be connected to a personal or other unmanaged device, and is returned for sanitising when the exception ends.
7. \<System Name\> holds and serves no public content. Every item needs sign-in, and the sign-in requirement on every page that returns content enforces this.

### 3.11 Review schedules

**Table 14: Review schedules**

| Review | How often | By |
| --- | --- | --- |
| The five role groups | Every 3 months | The system owner prepares it and the auditor checks and signs it; the Head of Cyber reviews any membership the system owner holds and checks the administrators |
| Server and database accounts: Windows administrators, SQL Server logins and their roles, and the service accounts | Every 6 months | System owner and security officer |
| Schema groups | Every 12 months | Data Owners |
| Members who have not signed in for 90 days | Monthly | The security officer lists them from the last sign-in report; each group's owner removes them |
| Audit logs | Weekly | Auditor, for the application audit log; security officer, for the logs in central logging |
| Actions allowed without signing in | Every 12 months, and after a change | System owner |
| This document | Every 12 months, and after a significant change | System owner |

In each access review, the group's owner checks its members against the ServiceNow requests, and removes in Active Directory any member who no longer needs the access. Each review is recorded on the access review record. The review is manual.

### 3.12 Exception rules

1. Every exception needs written system owner approval, a reason, an owner and an end date of no more than 12 months.
2. Each one needs a compensating check where possible, and an entry in \<Risk List\>.
3. Exceptions above the system owner's authority go to the authorising official.
4. Exceptions are checked at each access review and end on their end date unless renewed.

### 3.13 Access request workflow

![Figure 4: Access request workflow](figures/acm-figure-4.png)

**Figure 4: Access request workflow**

Every change to a person's access goes through a request in ServiceNow. ServiceNow is \<Organisation\>'s corporate service. The Application Support Team builds and maintains the \<System Name\> workflow in it.

**Table 15: Access request workflow**

| Request | Raised by | Approved and authorised by | Carried out by |
| --- | --- | --- | --- |
| Access to a schema, to read or to edit | The person who needs it, in ServiceNow | Approved: their line manager. Authorised: the schema's Data Owner | The Data Owner, who adds the person to the schema's AD group with \<Organisation\>'s AD tool |
| A privileged role | The person | Approved: their line manager. Authorised: the system owner, who cannot authorise their own | The system owner, who adds the person to the role's AD group |
| A change of role (mover) | The person's line manager, within 1 working day | Approved: not needed for a removal; as above for any new access. Authorised: as above for any new access | Each group's owner, who removes the old membership and adds any new one |
| Removal (leaver) | \<Organisation\>'s starters and leavers process, automatically | Not needed | \<Organisation\> disables the AD account at once, and the API refuses it within 5 minutes, which ends access. Each group's owner removes the membership within 5 working days |

No \<System Name\> account is ever created: a person's AD account is their account, and joining a group is what gives them access.

These rules apply:

1. **Two decisions before any access.** The line manager confirms the person needs it for their work. The owner of the data, or the system owner, decides whether to allow it, and only then adds the person to the AD group.
2. **Nobody decides their own request.** The person who raises a request cannot approve or authorise it. ServiceNow is set to refuse it. An owner who needs access to their own group asks the system owner.
3. **What each request records:** the person; what is asked for; the business reason; who approved and who authorised it, and when; that the training is done and the rules are signed; and who carried it out, and when.
4. **The record.** The closed ServiceNow request is the access request record, the record of the access decision: it holds the access request record's fields. It is kept for 3 years.
5. **Before the person is added to a group,** they complete security training and sign \<Security Operating Procedures\>.
6. **A high-risk individual.** \<Organisation\> disables the AD account within 1 hour. \<System Name\>'s API then refuses the disabled account within 5 minutes, which also ends any session the person has open (section 3.14). Ending the person's PingFederate sign-in as well stops a new sign-in, but it is not what ends access to \<System Name\>.
7. **Conditions for membership.** A need confirmed by the line manager, authorisation by the group's owner, security training, and a signed acknowledgement of \<Security Operating Procedures\> are the conditions for membership of any group.
8. **Notice of a change.** When an account is no longer needed, a user leaves or moves, or their need changes, the owners of the groups the person belongs to and the system owner are told within 1 working day in each case. The notice comes as a prompt from \<Organisation\>'s starters and leavers process.
9. **Aligned with leavers and movers.** \<System Name\> uses the same AD account that \<Organisation\>'s leaver and transfer processes act on, so disabling it ends access to \<System Name\>. The starters and leavers process prompts the group owners to remove memberships.

### 3.14 Disabling accounts and ending access

\<Organisation\> disables Active Directory accounts. A disabled account cannot sign in through PingFederate. Disabling an account does not remove its group memberships, so \<System Name\>'s API checks on every request that the account is enabled, as well as reading its groups, and holds each answer for at most 5 minutes. A person whose account is disabled, whose groups no longer allow them, or whose groups cannot be read is refused within 5 minutes, even while a session is open: by the next request, or by the 5-minute re-check of an open page, which skips the cache. Table 16 shows when access is ended.

**Table 16: When access is ended**

| Condition | What happens | Setting |
| --- | --- | --- |
| The account has expired | AD accounts with an end date are disabled by Active Directory on that date | None |
| The person leaves | \<Organisation\> disables the leaver's AD account at once, and \<System Name\> refuses it within 5 minutes. Each group's owner removes the membership within 5 working days | Leavers and movers |
| The account breaches policy | \<Organisation\> disables the AD account on notice, as for a high-risk individual | Disabling a high-risk individual |
| A high-risk individual | Within 1 hour of notice from management or \<Organisation\>'s security contact of misconduct, compromised credentials, a hostile departure or the departure of the holder of a higher risk role (\<Personnel Security Management\>, section 3.2), \<Organisation\> disables the AD account, so the person cannot sign in again, and \<System Name\>'s API refuses the disabled account within 5 minutes, ending any open session. The account stays disabled for at least 8 hours, unless every key in the key rings is revoked first, so that a cookie issued before it was disabled cannot be used again | Disabling a high-risk individual |
| The account is unused | \<Organisation\> disables AD accounts unused for 90 days within 1 working day. In addition, each month, the security officer lists, from the last sign-in report, every member who has not signed in to \<System Name\> for 90 days, and the owner of each group removes them, so that an unused membership ends even while the Active Directory account stays in use for other work | Unused accounts |

### 3.15 Sign-in session, sign-out, failed sign-ins and device lock

\<System Name\>'s session is its authentication cookie, which it sets and ends itself. Failed sign-ins and the screen lock are \<Organisation\>'s corporate configuration (section 3.6.5).

1. **Session lifetime.** The cookie has a fixed absolute lifetime of 8 hours from sign-in, with no sliding extension. PingFederate's sign-in lifetime for \<System Name\> is set to at least 8 hours, so the cookie always ends within PingFederate's sign-in; if PingFederate is ever set shorter, the 8 hours are lowered to match through a change. The UI is Blazor Server, so an open page keeps a live connection: the application re-checks the person on it every 5 minutes and ends it when the cookie has expired or the person is refused. That re-check makes the API read Active Directory afresh, skipping its 5-minute cache, so an open page is also ended within 5 minutes. The session therefore ends 8 hours after sign-in, on Sign out, or within 5 minutes of the person's account being disabled or their groups no longer allowing them. Ending a person's PingFederate sign-in on its own does not end the cookie.
2. **Sign-out.** Users must sign out at the end of each working day, and whenever they leave their device for longer than a short break. The Sign out button clears the cookie, ends the Blazor connection and ends the PingFederate sign-in. \<Security Operating Procedures\> tells users to use it.
3. **Failed sign-ins.** PingFederate and Active Directory count failed sign-ins and lock the account: 10 failed attempts within 15 minutes lock it for 15 minutes. \<System Name\> has no sign-in of its own. The lock applies to every system the person uses, not only \<System Name\>. \<Organisation\>'s Group Policy locks sign-in to the servers. SQL Server accepts connections only from the application server.
4. **Device lock.** \<Organisation\>'s managed devices and the servers lock the screen after 15 minutes of inactivity, by Group Policy or device management. The lock screen hides the display, and the lock stays until the user unlocks the device with their own credentials.
5. **What users do.** \<Security Operating Procedures\> tells users to lock their screen whenever they leave their device, even briefly, and to sign out at the end of each working day and whenever they leave it for longer than a short break.

### 3.16 System use notice

Each app shows the notice on a page straight after the user signs in through PingFederate, before they can go further. No other page, menu or data is served until the notice is accepted. The wording is: "This system is for authorised use only. Activity is monitored, recorded and audited. Unauthorised use may lead to disciplinary or legal action. By continuing you accept these terms.". The legal adviser approves the wording. The notice names \<Organisation\>, not the U.S. Government.

The notice stays until the user accepts it, and the acceptance is written to the audit log. It is text on a page of the UI app and of the Admin application, changed only through an approved change. On the servers, the Windows logon banner, which is \<Organisation\>'s corporate configuration, gives a system use notice before an administrator signs in (section 3.6.5).

### 3.17 Actions allowed without signing in

Only these actions are allowed without signing in:

1. be sent to PingFederate to sign in;
2. be returned from PingFederate to the sign-in return address, which accepts only PingFederate's signed response;
3. be returned to the signed-out page after Sign out;
4. see the access-denied page;
5. load static files, such as scripts, styles and images;
6. check that the API is running, which returns one status word;
7. on the application server's loopback address only, the UI and Admin applications' token request to the API, which carries no user's cookie: the application asks for a token naming a person it has already signed in. Each application authenticates it with Windows authentication under its own service account, and the API issues tokens only to those two accounts. Only the API's service account can read the token signing key, so no application can make its own token.

Each is needed before a person can identify themselves, or involves no person, and none returns business data. The API health check supports monitoring. The list is reviewed every 12 months and after a change.

The UI app, the Admin application and the API each refuse anything not marked as open, so a page or function that states no access rule is refused.

### 3.18 Audit of accounts and privileged actions

1. **Account events.** Active Directory audits the creation of every account, every change to an account and to the members of a group, and enabling, including unlocking, disabling and removal. \<Organisation\> holds these records.
2. **Sign-ins.** \<System Name\> audits every sign-in it accepts, every sign-in response it refuses, every failed group lookup, every account found disabled, every acceptance of the system use notice and every sign-out, with the person and the time. PingFederate records every sign-in attempt.
3. **Schema settings.** \<System Name\>'s audit log records changes to schemas and to which AD groups open each schema, with the reference of the Data Owner's approval. A change of groups raises an alert to the security officer (U9).
4. **Privileged functions.** Every use of a function in section 3.8 writes an audit record naming the person, the action, the target and the time. The application audit log and the audit service in the API hold these records. Only the API writes audit records. On the servers, Windows and SQL Server logging record their use, and SQL Server Audit records any read of the item tables by a login other than the API's. Disposal approvals and the search across every schema are recorded under the privacy and retention event type (\<System Description\>, section 7.6).
5. **Review.** The auditor reviews privileged actions weekly (\<Security Operating Procedures\>; Table 14).

### 3.19 Remote, wireless and mobile access

These are provided by \<Organisation\>'s corporate network and device configuration, over which the \<System Name\> team has no control (section 3.6.5). \<System Name\> has no remote access or wireless function of its own.

**Remote access.** One type only: \<Organisation\>'s VPN, from a managed device, with multi-factor authentication. It is used by users working from home, and by administrators only for approved changes, maintenance and incident response. \<Organisation\> authorises VPN access for each person through its own process, and logs and monitors VPN sessions. All remote access enters through \<Organisation\>'s one managed gateway. \<System Name\> is not reachable from the internet. Users must connect to the VPN before opening \<System Name\>, never send traffic around it, and never use public or shared computers (\<Security Operating Procedures\>).

**Encryption.** The VPN is encrypted. Inside it, every \<System Name\> flow uses TLS under NCSC's profiles: HTTPS to both apps, and TLS to SQL Server. The TLS settings of each app and of SQL Server are in \<System and Communications Protection Management\>.

**Privileged remote access.** Administrators, auditors and the security officer may do privileged work from outside the office only for approved changes, maintenance and incident response. They connect to the VPN with multi-factor authentication, and then reach the Admin application or the servers only through the managed administration route, with multi-factor authentication again. \<Organisation\>'s firewall rules block the servers' administration ports from external networks any other way. Each session is logged by Windows, SQL Server and the application audit log, and the change or incident record gives the reason.

**Wireless.** \<System Name\> has no wireless part. Users' devices may use \<Organisation\>'s corporate wireless network, under its wireless policy. \<Organisation\> authorises wireless access, and its wireless network authenticates both users and devices, and is encrypted. Users must not use public wireless without the VPN (\<Security Operating Procedures\>). The two servers have no wireless adapter, and \<Organisation\>'s build standard disables wireless where it is not needed.

**Mobile devices.** The only mobile devices allowed are \<Organisation\>'s managed laptops. \<Organisation\> sets their configuration and connection requirements, authorises each before it can join the network, and encrypts each with full-device encryption, BitLocker. Phones and tablets are not used with \<System Name\>, and none is authorised; \<Organisation\>'s device management and network access control enforce this.

### 3.20 Policy and procedures

\<Policy\> (AC) and \<Procedures\> (AC) are the access control policy and procedures. Who they are shared with is in \<Policy\>, section AC.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.

