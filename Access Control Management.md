# \<System Name\> Access Control Management

## 1 Purpose

This document shows how \<System Name\> is designed and configured for each of the 39 Access Control (AC) controls and enhancements in the CSS Moderate baseline. Section 3 sets out the access control model: the account types, roles, permissions, separation of duties, access routes, settings, rules and the access request workflow, and the design for ending access, sign-in and sessions, the system use notice, actions allowed without signing in, audit, remote, wireless and mobile access, and the policy and procedures. Section 4 is an index that shows where in section 3 each part of each control is met.

An assessor examines the design, the settings and the records, interviews the people named, and tests the mechanisms (CSS). This document gives the design that meets each part of each control, the mechanisms that enforce it, and their settings. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.1 (Table 10). The tests run, with their results, and the records an assessor will ask for are in \<Control Assessment Record\> (AC). Each control's risk is in \<Risk List\>, and what is still open, with the fix, is in \<Plan of Action and Milestones\>.

As \<System Description\> sets out, \<Organisation\>'s PingFederate authenticates every user, with multi-factor authentication, and \<System Name\>'s API reads each user's Active Directory groups directly from Active Directory over LDAPS, to give their roles and schema access (D-AC-23). \<System Name\> holds no accounts or passwords of its own, and has no session management: how long a sign-in lasts is set by PingFederate, and an unattended screen is locked by \<Organisation\>'s managed devices. Both are corporate services that \<System Name\> uses as they stand. The design in section 3 is written on that basis.

\<System Name\> is not yet built on its servers, so "today" means the tested v1.0 code in the test environment. That build signed in with its own passwords, held its groups and sessions in its own database and used PostgreSQL, so its tests do not show PingFederate sign-in, Active Directory groups or SQL Server working. Where that matters, the "Today" columns and notes in section 3 say so. Its findings are kept where they still apply to the reference design. Test results are in the AC evidence. Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>.

The policy is in \<Policy\> (AC), and the steps people follow are in \<Procedures\> (AC).

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.1 (Table 10).

## 3 The access control model

### 3.1 Principles

1. **Deny by default.** Nothing is allowed unless a role or group grants it. A schema with no group is open only to administrators.
2. **One person, one account.** Each person uses their own Active Directory account. Accounts are never shared, and \<System Name\> holds no accounts or passwords of its own.
3. **Schemas are the boundary.** Each schema has a read group and an edit group, owned by its Data Owner. Edit includes read.
4. **AD groups decide everything.** A person's role groups set what they can do, and their schema groups set which schemas they can do it in. All are Active Directory groups, which the API reads from Active Directory over LDAPS when the person signs in.
5. **Application users have no server access.** Windows and SQL Server administration use separate accounts.
6. **Only the API reaches the database.** The UI app and the Admin app get all their data through the API. The API connects with Windows authentication under its own managed service account, which is not a sysadmin and cannot change the schema (D-AC-18).
7. **\<Organisation\>'s single sign-on proves who the user is.** PingFederate authenticates every user, with multi-factor authentication, and gives \<System Name\> a signed OpenID Connect response that names them. \<System Name\> never sees a password (D-AC-23).
8. **No session management in the application.** \<System Name\> holds no session records and has no idle lock, idle timeout, session limit, sign-out or screen for ending sessions. The sign-in lasts as long as PingFederate allows, and the device screen lock hides an unattended screen.

Figure 1 shows the checks every request passes. Every request passes four checks in order: sign-in through PingFederate, which authenticates the user with multi-factor authentication, shown by the app's valid authentication cookie; the user's AD groups, read from Active Directory by the API over LDAPS; the schema decision, read or edit, from those groups; and the role group needed for the page or function. Anything not granted is refused.

The access control library, built into all three apps, makes the schema decisions. Role policies on each page and controller make the function decisions. The UI app and the Admin app refuse anything not marked as open; the API has no such default, which is why some of its functions are open (section 3.17). Page addresses name the schema, because page numbers restart in each schema. Item content is sent so that it is not kept in shared caches.

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
| Administrator | Administrators | Yes, privileged | Their own AD account; the system owner authorises and adds them to the group; a separate everyday account |
| Windows administrator | Windows server administrators | Yes, privileged | Named person, through \<Organisation\>'s approved route |
| Database administrator | SQL Server database administrators | Yes, privileged | Named person, for approved maintenance only |
| API service account | The API only | Yes, privileged | The API's group managed service account, which signs in to SQL Server with Windows authentication and reads group membership from Active Directory over LDAPS. Nobody signs in with it. Not a sysadmin, and cannot change the schema (section 3.6) |
| Local \<System Name\> account | Nobody | No | \<System Name\> holds no accounts or passwords of its own. The first administrator is simply the first member of that AD group (D-AC-23) |
| Temporary and emergency | Nobody | No | Prohibited (P-AC-09) |
| Shared, guest, anonymous and demonstration | Nobody | No | Prohibited on the servers |

Temporary and emergency accounts are prohibited (P-AC-09), so there is nothing to remove or disable automatically. Each access review confirms that none exists (PRO-AC-7). If such accounts were ever needed, they would be Active Directory accounts with an end date, and the tailoring decision would be made again.

Shared and group accounts are prohibited (TR-AC-02), and \<System Name\> holds no passwords, so there is no shared password to change when someone leaves a group.

### 3.3 Roles

**Table 2: Roles**

| Role | Purpose | Granted through | Group owner, who authorises and manages its members |
| --- | --- | --- | --- |
| Reader | Read items in a schema | The schema's read group, an AD group | The schema's Data Owner |
| Editor | Add, manage and export items in a schema | The schema's edit group, an AD group | The same |
| Administrator | Manage schemas, the AD groups each schema uses, and settings; use the administration dashboard | AD group \<Code\>\_Admins | System owner |
| Auditor | Read audit logs | AD group \<Code\>\_Auditors | System owner |
| Security officer | Read security information | AD group \<Code\>\_Security | System owner |

The people who hold each role are named in \<Roles and Responsibilities\>. The group names use the application's short code, and are confirmed when the groups are created in Active Directory.

Each group's owner adds and removes its members in Active Directory, with \<Organisation\>'s AD tool, as the last step of an approved request (section 3.13). \<System Name\>'s API reads each person's groups from Active Directory over LDAPS, with read-only rights, and cannot change them.

The authorised users of \<System Name\> are the members of its AD groups. Each person's groups are their access, and the approved source for each membership is its ServiceNow request. \<Organisation\> manages the AD accounts themselves. The administrator manages schemas, and which AD groups open each, in \<System Name\>'s Admin app.

The administrator, auditor and security officer groups are privileged. The system owner is their only owner, and authorises each member after role training and a signed Part B of \<Security Operating Procedures\> (PRO-AC-6). An administrator cannot add anyone to a group. On the servers, privileged access is held through Windows administrator group membership and SQL Server roles, and only the named Windows server and database administrators may sign in (section 3.6.2). The API's database service account is privileged and headless, and is managed by the database administrator.

### 3.4 Permissions

**Table 3: Permissions by role**

| Function | Reader | Editor | Administrator | Auditor | Security officer |
| --- | --- | --- | --- | --- | --- |
| Search and read items | Own schemas | Own schemas | All schemas | No | No |
| Report a faulty item | Own schemas | Own schemas | All schemas | No | No |
| Upload, manage and export items | No | Own schemas | All schemas | No | No |
| Manage users, passwords and group membership | No | No | No: done in Active Directory, by each group's owner | No | No |
| Manage schemas, and which AD groups open each | No | No | Yes | No | No |
| Grant administrator | No | No | No: the system owner adds the member to the AD group | No | No |
| Use the administration dashboard and settings | No | No | Yes | No | No |
| Read audit logs | No | No | No | Yes | No |
| Read security information | No | No | No | No | Yes |

### 3.5 Separation of duties

1. Nobody approves their own access or privilege.
2. Nobody reviews their own access or their own privileged actions.
3. Auditors and security officers hold no administration role.
4. Application, Windows and database administration use separate accounts, held by different people where staffing allows.
5. Developers hold no administrator access on the servers.
6. Where staffing cannot meet a rule, it is recorded as an exception, with a compensating check.

Table 4 shows each pair of duties that one person must not hold together, the roles that carry them, and what keeps them apart.

**Table 4: Duties kept apart**

| Duty | Must be separate from | Roles | Kept apart by | Today |
| --- | --- | --- | --- | --- |
| Asking for access | Approving and granting it | The person asks; their line manager approves; the group's owner authorises, and adds them to the AD group | The ServiceNow workflow, in which nobody can decide their own request, and Active Directory, where only a group's owner can change its members (section 3.13) | The ServiceNow workflow is not set up (PA-20). The tested build signed in with its own passwords and held its groups in its own database, so this is not yet tested with PingFederate and Active Directory |
| Administering schemas and settings | Reviewing audit logs | Administrator administers; auditor reviews | Separate access groups: only the auditor group opens the audit log pages, and it opens no administration page | In the tested build an auditor could not manage users (T74), but an administrator could still read the audit logs (T75, PA-15) |
| Administering the system | Reading security information | Administrator administers; security officer reads | Separate access groups | The security officer role has no test account, so this is not yet tested |
| Holding administrator | Granting it | Administrators; the system owner, who alone manages that AD group | Active Directory: an administrator cannot add a member to the group | In the tested build an administrator could grant it with no second person (PA-15) |
| Application administration | Windows administration and database administration | Administrator; Windows server administrator; SQL Server database administrator | Separate accounts on separate layers, held by three different people (\<Roles and Responsibilities\>) | Holders to be named. The servers are not built (PA-30) |
| Development | Production administration | Developers; Windows server and database administrators | Developers hold no administrator account on the servers | The servers are not built |
| Holding access | Reviewing that access | Each account holder; system owner, auditor and Data Owners review | Procedure: nobody reviews their own access (PRO-AC-7) | No review held yet (PA-16) |

**Today:** in the tested build an administrator can do everything, including reading audit logs and security information and reviewing their own actions. This is proposed for acceptance for 12 months as a Medium risk (PA-15).

### 3.6 Access routes

Figure 2 shows \<System Name\>'s boundary and the routes into and inside it. It is the boundary figure of \<Security Architecture\>.

![Figure 2: System boundary and access routes](figures/sd-figure-1.png)

**Figure 2: System boundary and access routes**

**Table 5: Access routes**

| Route | Used by | Design | Today |
| --- | --- | --- | --- |
| Sign-in | Everyone | The browser is sent to \<Organisation\>'s PingFederate, which authenticates the user with multi-factor authentication and returns a signed OpenID Connect response naming them. The API then reads their groups from Active Directory over LDAPS. \<System Name\> has no sign-in of its own | The tested build signed in with its own passwords and held its groups in its own database, so this is not yet tested with PingFederate and Active Directory |
| Browser to the UI app | Readers, editors, administrators | HTTPS on \<Organisation\>'s network, after signing in | Plain HTTP in the test environment (PA-18) |
| Browser to the Admin app | Administration, audit and security roles | HTTPS, over \<Organisation\>'s managed administration route only | Plain HTTP, reachable on every interface (PA-18, PA-83) |
| Apps to the API | The apps only | Inside the application server; people do not connect directly | As designed, over plain HTTP |
| API to the database | The API's service account only | Application server to database server only, using TLS with strict encryption and Windows authentication. The UI app and the Admin app have no database connection | All three apps connect, with one shared database administrator account and no TLS (PA-10, PA-18) |
| Windows administration | Windows server administrators | Named accounts, through \<Organisation\>'s approved route | Servers not yet built |
| Database administration | Database administrators | Named accounts, for approved maintenance only | Servers not yet built |
| Remote access | Approved users and administrators | \<Organisation\>'s remote access service, with multi-factor authentication | Stated by \<Organisation\>, not evidenced |
| Without signing in | Anyone | Only the actions listed in section 3.17 | Some extra functions are open (PA-03, PA-07) |
| API to Active Directory | The API's service account only | LDAPS, TCP 636, read-only, to read the signed-in person's group memberships | Not in the tested build, which held its groups in its own database |
| Outside services | None | Browsers load all code from \<System Name\> itself | Pages load code from an outside service (PA-34) |

**Table 6: Server and database access**

| Layer | Who | Rule |
| --- | --- | --- |
| Windows on both VMs | Windows server administrators | Named accounts, through \<Organisation\>'s approved route |
| SQL Server administration | Database administrators | Named accounts, for approved maintenance only |
| API to SQL Server | The API's managed service account | Windows authentication; the rights in the table below. The UI app and the Admin app do not connect |
| App service accounts on Windows | One for each app | Group managed service accounts; cannot sign in interactively; not administrators (Table 8) |

Only the API connects to the database (D-AC-18).

**Table 7: Database accounts and their rights**

| Account | Used by | May | May not |
| --- | --- | --- | --- |
| API's managed service account, \[name to be set at build\] | API only. Headless: no person signs in with it | Read and write application data. Add audit records | Be a sysadmin. Create, alter or drop tables. Change or delete audit records. Connect from anywhere but the application server |
| Schema change account, \[name to be set at build\] | The database administrator, at a release, under an approved change | Create and alter the tables | Be used by any app, or for everyday work |
| Database administrators' own accounts | Each database administrator, by name | Administer SQL Server, for approved maintenance | Be shared |
| Built-in sa login | Nobody, over the network | Be used on the database server itself, in an emergency, by a database administrator | Connect over the network |

These rules follow from it:

1. **No passwords.** \<System Name\> stores no passwords or password hashes, because PingFederate authenticates every user (D-AC-23).
2. **Items and schemas.** The UI app asks the API for item data. The Admin app asks the API for schemas, the groups each uses, settings and audit records, and gets no item content.
3. **Audit log.** The service account can only add records. Nothing can change or delete them. They are read only through the Admin application's audit pages, by the auditor role.
4. **Changes to the database structure.** Only the database administrator makes them, with the schema change account.
5. **Connection.** The API connects only from the application server, over TLS with strict encryption, using Windows authentication under its managed service account. There is no database password to store (D-AC-18).

**Today:** all three apps connect to the database themselves, with one shared account that has full administrative rights, and its password is in the code repositories (T55, PA-10, PA-19).

#### 3.6.1 Windows service accounts

Each app runs under its own Windows account (D-AC-19), so a fault in one app cannot reach another's files.

**Table 8: Windows service accounts**

| Account | Runs | Kind | May | May not |
| --- | --- | --- | --- | --- |
| \[name to be set at build\] | UI application | Group managed service account in \<Organisation\>'s Active Directory. Windows sets and changes its password, and no person knows it | Log on as a service on the application server | Be an administrator. Sign in at the console or by remote desktop. Be used by a person |
| \[name to be set at build\] | Admin application | The same | The same | The same |
| \[name to be set at build\] | API | The same | The same. It signs in to SQL Server with Windows authentication and reads Active Directory over LDAPS, so it holds no database password | The same |

\<Organisation\> uses Active Directory. Its agreement to group managed service accounts for these servers is to be confirmed with its security contact; if it does not agree, ordinary service accounts with the same rights are used, with passwords the Windows server administrator changes every 12 months.

#### 3.6.2 Who may sign in to the servers

**Table 9: Sign-in to the servers**

| Server | May sign in | How | May not |
| --- | --- | --- | --- |
| Application server | The named Windows server administrators | Their own named administrator accounts, through \<Organisation\>'s approved route | Developers, application users, the service accounts, and any shared account |
| Database server | The named Windows server administrators, and the named database administrators | The same | The same |

The holders are named in \<Roles and Responsibilities\>. \<Organisation\> creates and removes these accounts through its ServiceNow process, with the system owner's approval (EV-AC-02).

#### 3.6.3 File permissions on the application server

**Table 10: File permissions**

| Files | Read | Write | Notes |
| --- | --- | --- | --- |
| Each app's program folder | That app's service account; Windows server administrators | Windows server administrators only, at a release | An app cannot change its own code |
| Each app's settings and secrets | That app's service account; Windows server administrators | Windows server administrators only | Secrets are kept out of the code repositories (PA-19). The other two apps cannot read them |
| Each app's key ring, which protects its authentication cookie | That app's service account | That app's service account | Protected with Windows DPAPI (PA-93) |
| Each app's logs | Windows server administrators; the auditor | That app's service account | Kept for 30 days |
| The export working folder | API's service account | API's service account | Holds an export only until it is downloaded |

Item files are held in the SQL Server database, each schema in its own database schema. No item is held as a file on a share.

**Today:** the servers are not built, so none of this exists. In the test environment the apps run as an ordinary user, not as root (PA-18, PA-30).

#### 3.6.4 Firewall rules

\<Organisation\>'s corporate network team writes, holds and changes every firewall rule, through its own change process. The \<System Name\> team has no control over them and cannot see or change a rule (D-AC-20). So \<System Name\> does not design the rules. It states the flows it needs, in Table 11, and asks \<Organisation\> to allow those and nothing else. The rules themselves are \<Organisation\>'s evidence (EV-AC-03).

**Table 11: Flows \<System Name\> asks \<Organisation\> to allow**

| Flow | From | To | Service | Needed for |
| --- | --- | --- | --- | --- |
| F1 | Users' managed devices, in the office or on the VPN | Application server | HTTPS, TCP 443 | The UI app |
| F2 | Administrators, over \<Organisation\>'s managed route | Application server | HTTPS, on a port or host name still to be set | The Admin app |
| F3, F4 | The UI app and the Admin app | The API, on the application server's own loopback address | HTTPS | Needs no firewall rule: it never leaves the server |
| F5 | Application server | Database server | SQL Server with TLS, TCP 1433 | The API's database connection |
| F6 | Users' and administrators' browsers | \<Organisation\>'s PingFederate | HTTPS | Signing in. Both ends are \<Organisation\>'s, so this needs no rule for \<System Name\>'s servers |
| F7 | Application server | \<Organisation\>'s Active Directory domain controllers | LDAPS, TCP 636 | The API reading each signed-in person's group memberships |
| PingFederate metadata | Application server | \<Organisation\>'s PingFederate | HTTPS | Fetching PingFederate's OpenID Connect metadata and signing keys, which check its sign-in responses |
| Administration | Windows server and database administrators, over \<Organisation\>'s managed route | Both servers | Tool and protocol to be confirmed by \<Organisation\> | Running the servers |
| F8 (time) | Both servers | \<Organisation\>'s time service | NTP, UDP 123 | Accurate audit times |

Everything else should be refused, in and out. \<System Name\> needs no route to the internet once pages stop loading code from an outside service (PA-34). ServiceNow and the Starters/Leavers system (F9) have no connection to \<System Name\>. The flows are also listed in \<Security Architecture\>, Table 2.

What \<System Name\> itself controls is limited to its own apps: the API listens only on the loopback address, each app accepts only HTTPS, and the API accepts requests only from the two apps' addresses.

**Today:** no rule exists, as the servers are not built, and the request has not been sent (PA-18).

#### 3.6.5 What \<Organisation\>'s corporate configuration provides

![Figure 3: Who provides each part of access control](figures/acm-figure-3.png)

**Figure 3: Who provides each part of access control**

These are set by \<Organisation\> as part of its corporate network, directory and device configuration. The \<System Name\> team has no control over them (D-AC-21, D-AC-23). \<System Name\> accepts \<Organisation\>'s corporate standard for each, and records the values once \<Organisation\> supplies them. Table 12 says what \<System Name\> relies on. What \<Organisation\> has said so far is a statement by its security contacts, not evidence.

**Table 12: Provided by \<Organisation\>'s corporate configuration**

| Provided | Controls | What \<System Name\> relies on | Said by \<Organisation\> | Evidence asked |
| --- | --- | --- | --- | --- |
| Single sign-on: PingFederate | AC-3, AC-7, AC-12, AC-14, and the IA controls | Every user is authenticated by PingFederate, with multi-factor authentication. Repeated failed sign-ins lock the account under the corporate standard. The OpenID Connect response \<System Name\> receives is signed. PingFederate's sign-in lifetime is the only limit on how long a sign-in lasts (AC-12) | Stated by the system owner (D-AC-23); not yet by \<Organisation\> | EV-IA-04 |
| Accounts and groups: Active Directory | AC-2 and its enhancements, AC-6(5), AC-6(7) | Each person has one AD account, created, changed and disabled by \<Organisation\>'s starters and leavers process. A disabled account can no longer sign in. Only a group's owner can change its members. The API reads group membership over LDAPS | The same | EV-AC-01 |
| Account lockout on the servers and on users' devices | AC-7 | Repeated failed Windows sign-ins lock the account | Group Policy sets the lockout | EV-AC-05 |
| Logon banner on the servers | AC-8 | A system use notice before an administrator signs in to Windows | Group Policy sets the banner | EV-AC-06 |
| Screen lock on the servers and on users' devices | AC-11, AC-11(1), AC-2(5) | An unattended screen locks after the time in P-AC-15, hides what was on it, and needs the password to unlock. As \<System Name\> has no page lock of its own, this is the only session lock | Group Policy sets the lock, and it hides the display | EV-AC-07 |
| Remote access | AC-17, AC-17(1), AC-17(2), AC-17(3) | One route in from outside: the VPN, from a managed device, with multi-factor authentication, encrypted, logged and monitored, through one managed gateway | As described | EV-AC-08 to EV-AC-11 |
| No remote administration from outside | AC-17(4) | The servers' administration ports cannot be reached from external networks | Administration ports are blocked from external networks | EV-AC-12 |
| Wireless | AC-18, AC-18(1), AC-18(3) | Corporate wireless authenticates users and devices and is encrypted; the servers have no wireless | As described | EV-AC-13, EV-AC-14 |
| Device controls | AC-19, AC-20, AC-20(2) | Phones and tablets cannot reach \<System Name\>; unmanaged devices are kept off the network; USB storage is blocked unless approved | As described | EV-AC-15 to EV-AC-17 |

The only \<System Name\> setting for the same controls is its system use notice (section 3.7). \<System Name\> has no page lock or session limits of its own.

**Today:** none of the evidence has been requested (PA-18, PA-21, PA-30, PA-95).

### 3.7 Settings

The P-AC numbers are the access control settings used across the document set. P-AC-01 to P-AC-03 are in \<Policy\> (AC). Sign-in settings, such as lockout, multi-factor authentication and the sign-in lifetime, are PingFederate's and are not set in \<System Name\>.

**Table 13: Access control settings**

| No. | Control | Setting and approved value | Today |
| --- | --- | --- | --- |
| P-AC-04 | AC-2 | Allowed account types: as listed in Table 1 | Not yet approved; a rule for people, nothing to build |
| P-AC-05 | AC-2 | Who decides access: the person's line manager approves in ServiceNow, then the group's owner authorises and adds them to the AD group. The owner is the system owner for a role group, and the Data Owner for a schema group (section 3.13) | Not yet approved; a rule for people, carried out in ServiceNow and Active Directory |
| P-AC-06 | AC-2 | A leaver's AD account is disabled by \<Organisation\> at once, which ends their access to \<System Name\>. Each group's owner removes the membership within 5 working days. Owners are told of a role change within 1 working day | Not yet approved; no notice from \<Organisation\> yet (PA-32) |
| P-AC-07 | AC-2, AC-6(7) | Access review: administrators and the other privileged groups every 3 months, all other accounts every 12 months | Not yet approved; no review held yet (PA-16) |
| P-AC-08 | AC-2(3) | Unused AD accounts are disabled under \<Organisation\>'s corporate standard, which \<System Name\> accepts. An account no longer required or in breach of policy is disabled by \<Organisation\> on notice. In addition, each month, the owner of each group removes any member who has not signed in to \<System Name\> for 90 days, from the sign-in dates in the audit records that an administrator provides (D-PS-11) | \<Organisation\>'s standard is to be supplied |
| P-AC-09 | AC-2(2) | Temporary and emergency accounts: not allowed until the system can expire them | Not yet approved; a rule for people, nothing to build |
| P-AC-10 | AC-2(5), AC-12 | Sign-in lifetime: as set in PingFederate for \<System Name\> (\<System Description\>, P-02). \<System Name\> has no idle sign-out of its own | Value to be supplied by \<Organisation\>. The tested build signed users out after 30 minutes idle, which the reference design does not have |
| P-AC-11 | AC-12 | No session limit in \<System Name\>. The PingFederate sign-in lifetime in P-AC-10 is the only limit | Not yet approved. The tested build ended sessions after 8 hours, which the reference design does not have |
| P-AC-12 | AC-12 | No limit on sign-ins at once in \<System Name\> | Not yet approved. The tested build allowed 3 sessions per user, which the reference design does not have |
| P-AC-13 | AC-2(13) | Within 1 hour of notice: \<Organisation\> disables the AD account of a high-risk individual and ends their PingFederate sign-in. \<System Name\> reads groups from Active Directory, so a disabled account or a removed membership is refused at the next group lookup | Not yet approved; a rule for people, not yet used |
| P-AC-14 | AC-7 | Failed sign-ins are counted and the account locked by PingFederate and Active Directory, under \<Organisation\>'s corporate standard. \<System Name\> has no sign-in of its own to lock | \<Organisation\>'s standard is to be supplied. The tested build locked after 5 failures, for 15 minutes |
| P-AC-15 | AC-11 | Device screen lock after inactivity, set by \<Organisation\> on its managed devices and the servers (\<System Description\>, P-03). \<System Name\> has no page lock of its own | Value to be supplied by \<Organisation\>. The tested build had a page lock after 25 minutes, which the reference design does not have |
| P-AC-16 | AC-8 | System use notice wording: the wording in section 3.16 | Not yet approved; not shown yet (PA-11) |
| P-AC-17 | AC-6(1), AC-6(10) | Privileged functions: managing schemas and the AD groups each uses; settings; audit log access; database maintenance; cache management. Security-relevant information: secrets and security settings, PingFederate's signing keys, access groups and schema access rules, audit logs, firewall rules and certificates | Not yet approved; a rule for people, nothing to build |
| P-AC-18 | AC-6(2) | Administrators use a separate non-privileged account for everyday item work | Not yet approved; everyday accounts not issued (PA-17) |
| P-AC-19 | AC-6(9) | Privileged functions are logged: as P-AC-17 | Not yet approved; partly built (PA-14) |
| P-AC-20 | AC-17 | Remote access route: \<Organisation\>'s remote access service, name to be confirmed | To be confirmed by \<Organisation\> |
| P-AC-21 | AC-18, AC-19 | Wireless and mobile access: follows \<Organisation\>'s policies, to be confirmed | To be confirmed by \<Organisation\> |
| P-AC-22 | AC-20 | External systems and portable storage with \<System Name\> data: not allowed without system owner approval | Not yet approved; a rule for people, nothing to build |
| P-AC-23 | AC-21 | Who decides on sharing information outside a schema: the Data Owner | Not yet approved; a rule for people, nothing to build |
| P-AC-24 | AC-22 | Public content: none. \<System Name\> must not hold or serve public content without system owner approval | Not yet approved; a rule for people, nothing to build |
| P-AC-25 | AC-14 | Actions allowed without signing in: be sent to PingFederate to sign in; see the access-denied page; load static files; check API health. Nothing else | Not yet approved; other functions are also open (PA-03, PA-07) |

### 3.8 Privileged functions and security information

**Privileged functions:** managing schemas and the AD groups each uses; changing settings; reading audit logs; database maintenance; and cache management. Managing the members of \<System Name\>'s AD groups is also privileged, and is done in Active Directory by each group's owner.

**Security-relevant information:** secrets and security settings, PingFederate's signing keys, access groups and schema access rules, audit logs, firewall rules and certificates.

Only the privileged roles in Table 1 may use these. Their use must be logged (section 3.18).

Security functions in hardware and firmware, namely the physical hosts, the network equipment and the host firmware, are held by \<Organisation\>'s network and infrastructure teams, under \<Organisation\>'s own access lists.

These rules apply:

1. **Checked where it runs.** Each privileged function checks the caller's role where the function runs, not only in the menu, through the role policies on every Admin application page and API controller. Table 3 says which role may run each. Everything else is refused.
2. **Information kept to the roles.** Role policies on the Admin application's pages, database rights and file permissions on the servers keep the security information to the roles that need it. Secrets are kept out of the code repositories, and each app's secrets are readable only by that app's service account and the Windows server administrators (section 3.6.3).
3. **A separate everyday account.** Each administrator has two AD accounts: a privileged one for administration, and an everyday one for item work (P-AC-18; \<Security Operating Procedures\>, rules B2 and B3). This is a rule for people. The system does not enforce it.
4. **Nothing extra in production.** No maintenance, diagnostic or test page is present in production.

### 3.9 Export and download rules

1. Only editors of a schema and administrators may bulk export its items.
2. An export job can be seen, downloaded or cancelled only by the person who started it.
3. Exports are delivered as downloads. Writing exports to a server folder is not allowed (PA-26).
4. Exported items stay under the schema's access rules, and leaving \<Organisation\>'s systems needs approval under P-AC-22 and P-AC-23.
5. Every export is recorded in the audit log.

### 3.10 Information sharing rules

1. Sharing outside a schema needs a decision by that schema's access approver, its Data Owner (P-AC-23), through the manual process in PRO-AC-16.
2. The approver checks that the recipient is authorised for the information, and the decision is recorded on TPL-2. Exported documents stay under the schema's rules.
3. Inside \<System Name\>, the schema groups control sharing. Sharing outside is a manual decision.
4. External systems and portable storage may hold \<System Name\> data only with system owner approval (P-AC-22). External systems may reach or hold it only with the system owner's written approval. None is approved, and none is proposed (TR-AC-07). Terms and conditions are used, not asserted controls (TR-AC-10).
5. Personal devices, personal cloud storage and any unmanaged system are prohibited (\<Security Operating Procedures\>, rules A31, A35 and A45). \<Organisation\>'s network access control keeps unmanaged devices off the network.
6. USB and other portable storage may not hold \<System Name\> data without the system owner's approval, recorded as a sharing decision (P-AC-22, PRO-AC-16; \<Security Operating Procedures\>, rule A32). \<Organisation\>'s device control on managed devices enforces this.
7. \<System Name\> holds and serves no public content (P-AC-24, D-AC-11). Every document needs sign-in, and the sign-in requirement on every page that returns content enforces this.

### 3.11 Review schedules

**Table 14: Review schedules**

| Review | How often | By | Steps |
| --- | --- | --- | --- |
| The three role groups | Every 3 months | System owner, auditor; Head of Cyber as an extra check, for administrators | PRO-AC-7 |
| Schema groups | Every 12 months | Data Owners | PRO-AC-7 |
| Members who have not signed in for 90 days | Monthly | Each group's owner, with the sign-in dates an administrator provides | PRO-AC-8 |
| Audit logs | Weekly | Auditor | \<Security Operating Procedures\> |
| Actions allowed without signing in | Every 12 months, and after a change | System owner | PRO-AC-14 |
| This document | Every 12 months, and after a significant change | System owner | PRO-AC-14 |

In each access review, the group's owner checks its members against the ServiceNow requests, and removes in Active Directory any member who no longer needs the access. Each review is recorded on TPL-3 (P-AC-07, PRO-AC-7). The review is manual.

### 3.12 Exception rules

1. Every exception needs written system owner approval, a reason, an owner and an end date of no more than 12 months.
2. Each one needs a compensating check where possible, and an entry in \<Risk List\>.
3. Exceptions above the system owner's authority go to the authorising official.
4. Exceptions are checked at each access review and end on their end date unless renewed.
5. Steps are in PRO-AC-15.

### 3.13 Access request workflow

![Figure 4: Access request workflow](figures/acm-figure-4.png)

**Figure 4: Access request workflow**

Every change to a person's access goes through a request in ServiceNow (D-AC-22). ServiceNow is \<Organisation\>'s corporate service. The Application Support Team builds and maintains the \<System Name\> workflow in it.

**Table 15: Access request workflow**

| Request | Raised by | Approved by | Authorised by | Carried out by |
| --- | --- | --- | --- | --- |
| Access to a schema, to read or to edit | The person who needs it, in ServiceNow | Their line manager | The schema's Data Owner | The Data Owner, who adds the person to the schema's AD group with \<Organisation\>'s AD tool |
| A privileged role | The person | Their line manager | The system owner, who cannot authorise their own | The system owner, who adds the person to the role's AD group |
| A change of role (mover) | The person's line manager, within 1 working day | Not needed for a removal; as above for any new access | As above for any new access | Each group's owner, who removes the old membership and adds any new one |
| Removal (leaver) | \<Organisation\>'s Starters/Leavers system, automatically | Not needed | Not needed | \<Organisation\> disables the AD account at once, which ends access. Each group's owner removes the membership within 5 working days |

No \<System Name\> account is ever created: a person's AD account is their account, and joining a group is what gives them access.

These rules apply:

1. **Two decisions before any access.** The line manager confirms the person needs it for their work. The owner of the data, or the system owner, decides whether to allow it, and only then adds the person to the AD group.
2. **Nobody decides their own request.** The person who raises a request cannot approve or authorise it. ServiceNow is set to refuse it. An owner who needs access to their own group asks the system owner.
3. **What each request records:** the person; what is asked for; the business reason; who approved and who authorised it, and when; that the training is done and the rules are signed; and who carried it out, and when.
4. **The record.** The closed ServiceNow request is the record of the access decision, in place of form TPL-2. It is kept for 3 years.
5. **Before the person is added to a group,** they complete security training and sign \<Security Operating Procedures\> (PRO-AC-1).
6. **A high-risk individual.** \<Organisation\> disables the AD account and ends the person's PingFederate sign-in, within 1 hour. \<System Name\> reads group membership from Active Directory at sign-in, so a disabled account cannot sign in again. \<System Name\> has no sessions of its own to end (section 3.14).
7. **Conditions for membership.** A need confirmed by the line manager, authorisation by the group's owner, security training, and a signed acknowledgement of \<Security Operating Procedures\> are the conditions for membership of any group (PRO-AC-1, PRO-AC-5, PRO-AC-6).
8. **Notice of a change.** When an account is no longer needed, a user leaves or moves, or their need changes, the owners of the groups the person belongs to and the system owner are told within 1 working day in each case. The notice comes as a prompt from \<Organisation\>'s Starters/Leavers system (P-AC-06).
9. **Aligned with leavers and movers.** \<System Name\> uses the same AD account that \<Organisation\>'s leaver and transfer processes act on, so disabling it ends access to \<System Name\>. The Starters/Leavers system prompts the group owners to remove memberships (PRO-AC-2, PRO-AC-3).

**Today:** the workflow is not built, and no request has been raised (PA-20). The Starters/Leavers prompt is not set up (PA-32). The AD groups are not yet created.

### 3.14 Disabling accounts and ending access

\<Organisation\> disables Active Directory accounts. A disabled account cannot sign in through PingFederate, so it cannot reach \<System Name\>. A sign-in already open lasts until PingFederate's sign-in lifetime ends, but any removed group membership is refused at the next Active Directory lookup. \<System Name\>'s API refuses a person whose account is disabled or whose groups cannot be read. Table 16 shows when access is ended.

**Table 16: When access is ended**

| Condition | What happens | Setting |
| --- | --- | --- |
| The account has expired | AD accounts with an end date are disabled by Active Directory on that date | None |
| The person leaves | \<Organisation\> disables the leaver's AD account at once. Each group's owner removes the membership within 5 working days | P-AC-06 |
| The account breaches policy | \<Organisation\> disables the AD account on notice (PRO-AC-4) | P-AC-08 |
| A high-risk individual | Within 1 hour of notice from management or \<Organisation\>'s security contact of misconduct, compromised credentials or a hostile departure, \<Organisation\> disables the AD account and ends the person's PingFederate sign-in, so the person cannot sign in again, and any group lookup for them fails (PRO-AC-4, record TPL-14; TPL-10 if it is an incident). \<System Name\> has no sessions of its own to end | P-AC-13 |
| The account is unused | Unused AD accounts are disabled under \<Organisation\>'s corporate standard, which \<System Name\> accepts. In addition, each month, the owner of each group removes any member who has not signed in to \<System Name\> for 90 days, from the sign-in dates in the audit records that an administrator provides, so that an unused membership ends even while the Active Directory account stays in use for other work (D-PS-11, PRO-AC-8) | P-AC-08 |

### 3.15 Sign-in lifetime, failed sign-ins and device lock

\<System Name\> has no session management (section 3.1), so it does not sign users out, lock a page or limit sessions itself. These are \<Organisation\>'s corporate configuration, which \<System Name\> accepts as it stands (section 3.6.5).

1. **Sign-in lifetime.** A user's sign-in ends when PingFederate's sign-in lifetime for \<System Name\> ends (P-AC-10), or when \<Organisation\> ends their PingFederate sign-in or disables their account. \<System Name\> holds the sign-in only in its authentication cookie, whose lifetime is no longer than PingFederate's. It reads the person's groups from Active Directory at sign-in, so a change to their groups takes effect at their next sign-in.
2. **Failed sign-ins.** PingFederate and Active Directory count failed sign-ins and lock the account, under \<Organisation\>'s corporate standard, which \<System Name\> accepts (P-AC-14). \<System Name\> has no sign-in of its own. The lock applies to every system the person uses, not only \<System Name\>. \<Organisation\>'s Group Policy locks sign-in to the servers. SQL Server accepts connections only from the application server.
3. **Device lock.** \<Organisation\>'s managed devices and the servers lock the screen after the inactivity period in P-AC-15, by Group Policy or device management. The lock screen hides the display, and the lock stays until the user unlocks the device with their own credentials.
4. **What users do.** \<Security Operating Procedures\> tells users to close the browser and lock their device when they finish.

### 3.16 System use notice

Each app shows the notice on its first page, before it sends the user to PingFederate to sign in. The wording is: "This system is for authorised use only. Activity is monitored and recorded. Unauthorised use may lead to disciplinary or legal action. By signing in you accept these terms." (P-AC-16). The notice names \<Organisation\>, not the U.S. Government (TR-AC-03).

The notice stays until the user chooses to continue to sign-in, which is the acceptance. It is text on the first page of the UI app and of the Admin application, changed only through an approved change (PRO-AC-13). \<System Name\> is not public, so no conditions for public systems apply (TR-AC-04). On the servers, the Windows logon banner, which is \<Organisation\>'s corporate configuration, gives a system use notice before an administrator signs in (section 3.6.5).

### 3.17 Actions allowed without signing in

Only these actions are allowed without signing in (P-AC-25):

1. be sent to PingFederate to sign in;
2. see the access-denied page;
3. load static files, such as scripts, styles and images;
4. check that the API is running, which returns one status word.

Each is needed before a person can identify themselves, and none returns business data. The API health check supports monitoring. The list and the reasons are also stated in \<System Security Plan\>. The list is reviewed every 12 months and after a change (PRO-AC-14).

The UI app and the Admin application refuse anything not marked as open. The API has no such default, so an unmarked API function is open.

### 3.18 Audit of accounts and privileged actions

1. **Account events.** Active Directory audits the creation of every account, every change to an account and to the members of a group, and enabling, including unlocking, disabling and removal. \<Organisation\> holds these records.
2. **Sign-ins.** \<System Name\> audits every sign-in it accepts, with the person and the time. PingFederate records every sign-in attempt.
3. **Schema settings.** \<System Name\>'s audit log records changes to schemas and to which AD groups open each schema.
4. **Privileged functions.** Every use of a function in section 3.8 writes an audit record naming the person, the action, the target and the time (P-AC-19). The application audit log and its audit service hold these records. Only the system can write audit records. On the servers, Windows and SQL Server logging record their use.
5. **Review.** The auditor reviews privileged actions weekly (\<Security Operating Procedures\>, duty C3; Table 14).

### 3.19 Remote, wireless and mobile access

These are provided by \<Organisation\>'s corporate network and device configuration, over which the \<System Name\> team has no control (section 3.6.5). \<System Name\> has no remote access or wireless function of its own.

**Remote access.** One type only: \<Organisation\>'s VPN, from a managed device, with multi-factor authentication (P-AC-20). It is used by users working from home and by approved administrators. \<Organisation\> authorises VPN access for each person through its own process, and logs and monitors VPN sessions. All remote access enters through \<Organisation\>'s one managed gateway. \<System Name\> is not reachable from the internet. Rules for users are in \<Security Operating Procedures\> (rules A39 and A40).

**Encryption.** The VPN is encrypted. Inside it, every \<System Name\> flow uses TLS under NCSC's profiles: HTTPS to both apps, and TLS to SQL Server. The TLS settings of each app and of SQL Server are in \<System and Communications Protection Management\>.

**Remote administration.** CSS defines remote access as access through external networks. Administration takes place only from inside \<Organisation\>'s network, so no privileged remote access is allowed (D-AC-08). \<Organisation\>'s firewall rules block the servers' administration ports from external networks. The reason privileged remote access does not apply is in \<Tailoring Register\> (TR-AC-05), for the authorising official's approval.

**Wireless.** \<System Name\> has no wireless part. Users' devices may use \<Organisation\>'s corporate wireless network, under its wireless policy (P-AC-21). \<Organisation\> authorises wireless access, and its wireless network authenticates both users and devices, and is encrypted. Users must not use public wireless without the VPN (\<Security Operating Procedures\>, rule A40). The two servers have no wireless adapter, and \<Organisation\>'s build standard disables wireless where it is not needed.

**Mobile devices.** Phones and tablets are not to be used with \<System Name\> in the first release (D-AC-09), and none is authorised. \<Organisation\>'s device management and network access control enforce this. As no mobile devices are used, full device or container-based encryption does not apply (TR-AC-06).

### 3.20 Policy and procedures

1. **Policy.** \<Policy\> (AC) is a system-level policy within \<Organisation\>'s organisational policies. Its purpose and scope are in section AC.1, responsibilities in AC.5, and commitment, coordination and compliance in AC.6. It is shared with everyone who uses or administers \<System Name\>. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (AC) holds 17 procedures, PRO-AC-1 to PRO-AC-17, each naming who acts, the time limit and the record. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures (P-AC-01).
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change (P-AC-02). The procedures are reviewed every 12 months, and after a change to the steps (P-AC-03). The steps are in PRO-AC-14.
5. **Records.** The documents are under version control, and each review is recorded in the change record and on TPL-4.

## 4 Control index

Each part of each control is met by the design in section 3. Table 17 shows, for each control and enhancement in CSS order, the section 3 subsections that meet each part, and the settings that apply. Each control's status, responsibility and assessment result are in \<System Security Plan\>, section 7.1 (Table 10), its risk in \<Risk List\>, and its open items in \<Plan of Action and Milestones\>.

**Table 17: Control index**

| Control | Part | Where it is met | Settings |
| --- | --- | --- | --- |
| AC-1 Policy and Procedures | a.1 | 3.20 | None |
| AC-1 | a.2 | 3.20 | None |
| AC-1 | b | 3.20 | P-AC-01 |
| AC-1 | c.1 | 3.20 | P-AC-02 |
| AC-1 | c.2 | 3.20 | P-AC-03 |
| AC-2 Account Management | a | 3.2 | P-AC-04 |
| AC-2 | b | 3.3, 3.6.5 | None |
| AC-2 | c | 3.13 | P-AC-05 |
| AC-2 | d | 3.3, 3.13 | None |
| AC-2 | e | 3.13 | P-AC-05 |
| AC-2 | f | 3.3, 3.6.2, 3.6.5 | None |
| AC-2 | g | 3.11, 3.18 | None |
| AC-2 | h | 3.13 | P-AC-06 |
| AC-2 | i | 3.1, 3.3, 3.4 | None |
| AC-2 | j | 3.11 | P-AC-07 |
| AC-2 | k | 3.2 | None |
| AC-2 | l | 3.13, 3.14 | P-AC-06 |
| AC-2(1) Automated System Account Management | All | 3.1, 3.6.5, 3.13 | None |
| AC-2(2) Automated Temporary and Emergency Account Management | All | 3.2 | P-AC-09 |
| AC-2(3) Disable Accounts | a | 3.14 | None |
| AC-2(3) | b | 3.14 | P-AC-06 |
| AC-2(3) | c | 3.14 | P-AC-08, P-AC-13 |
| AC-2(3) | d | 3.11, 3.14 | P-AC-08 |
| AC-2(4) Automated Audit Actions | Creation | 3.18 | None |
| AC-2(4) | Modification | 3.18 | None |
| AC-2(4) | Enabling | 3.18 | None |
| AC-2(4) | Disabling | 3.18 | None |
| AC-2(4) | Removal | 3.18 | None |
| AC-2(5) Inactivity Logout | All | 3.6.5, 3.15 | P-AC-10, P-AC-15 |
| AC-2(13) Disable Accounts for High-risk Individuals | All | 3.13, 3.14 | P-AC-13 |
| AC-3 Access Enforcement | All | 3.1, 3.3, 3.4, 3.9 | None |
| AC-4 Information Flow Enforcement | All | 3.6, 3.6.4, 3.9 | None |
| AC-5 Separation of Duties | a | 3.5 | None |
| AC-5 | b | 3.4, 3.5 | None |
| AC-6 Least Privilege | All | 3.3, 3.4, 3.6, 3.6.1, 3.6.3, 3.8 | None |
| AC-6(1) Authorize Access to Security Functions | a | 3.8 | P-AC-17 |
| AC-6(1) | b | 3.6.3, 3.8 | P-AC-17 |
| AC-6(2) Non-privileged Access for Nonsecurity Functions | All | 3.8 | P-AC-18 |
| AC-6(5) Privileged Accounts | All | 3.2, 3.3, 3.6.2 | None |
| AC-6(7) Review of User Privileges | a | 3.11 | P-AC-07 |
| AC-6(7) | b | 3.11 | None |
| AC-6(9) Log Use of Privileged Functions | All | 3.8, 3.18 | P-AC-19 |
| AC-6(10) Prohibit Non-privileged Users from Executing Privileged Functions | All | 3.4, 3.8 | P-AC-17 |
| AC-7 Unsuccessful Logon Attempts | a | 3.6.5, 3.15 | P-AC-14 |
| AC-7 | b | 3.6.5, 3.15 | P-AC-14 |
| AC-8 System Use Notification | a | 3.16 | P-AC-16 |
| AC-8 | b | 3.16 | P-AC-16 |
| AC-8 | c | 3.16 | None |
| AC-11 Device Lock | a | 3.6.5, 3.15 | P-AC-15 |
| AC-11 | b | 3.6.5, 3.15 | P-AC-15 |
| AC-11(1) Pattern-hiding Displays | All | 3.6.5, 3.15 | None |
| AC-12 Session Termination | All | 3.15 | P-AC-10, P-AC-11, P-AC-12 |
| AC-14 Permitted Actions Without Identification or Authentication | a | 3.11, 3.17 | P-AC-25 |
| AC-14 | b | 3.17 | P-AC-25 |
| AC-17 Remote Access | a | 3.6.5, 3.19 | P-AC-20 |
| AC-17 | b | 3.19 | P-AC-20 |
| AC-17(1) Monitoring and Control | All | 3.6.5, 3.19 | None |
| AC-17(2) Protection of Confidentiality and Integrity Using Encryption | All | 3.6.5, 3.19 | None |
| AC-17(3) Managed Access Control Points | All | 3.6.5, 3.19 | None |
| AC-17(4) Privileged Commands and Access | a | 3.6.5, 3.19 | None |
| AC-17(4) | b | 3.19 | None |
| AC-18 Wireless Access | a | 3.19 | P-AC-21 |
| AC-18 | b | 3.19 | P-AC-21 |
| AC-18(1) Authentication and Encryption | All | 3.6.5, 3.19 | P-AC-21 |
| AC-18(3) Disable Wireless Networking | All | 3.6.5, 3.19 | None |
| AC-19 Access Control for Mobile Devices | a | 3.6.5, 3.19 | P-AC-21 |
| AC-19 | b | 3.19 | P-AC-21 |
| AC-19(5) Full Device or Container-based Encryption | All | 3.19 | P-AC-21 |
| AC-20 Use of External Systems | a | 3.10 | P-AC-22 |
| AC-20 | b | 3.6.5, 3.10 | None |
| AC-20(1) Limits on Authorized Use | All | 3.10 | P-AC-22 |
| AC-20(2) Portable Storage Devices: Restricted Use | All | 3.6.5, 3.10 | P-AC-22 |
| AC-21 Information Sharing | a | 3.9, 3.10 | P-AC-23 |
| AC-21 | b | 3.10 | P-AC-23 |
| AC-22 Publicly Accessible Content | All | 3.10 | P-AC-24 |
