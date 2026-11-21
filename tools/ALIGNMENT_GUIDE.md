# Aligning a document with the System Description

Working rules for bringing each document in the set into line with `System Description.md`, the generic Secure by Design reference. Worked example: `Access Control Management.md`, which was done by hand as the pilot.

## 1 What the set is

A clean template for any application, describing the reference design. It holds no records of anything that happened: no results, findings, decisions, risks, plan items, incidents, dates, approvals or notes about a tested build. `tools/CLEAN_GUIDE.md` and `tools/BLANK_GUIDE.md` set those rules, and they still apply. Do not add any of these back.

## 2 The reference system (from the System Description)

| Topic | Reference design |
| --- | --- |
| What it is | An internal digital library: staff store, search and view digital items, kept apart in **schemas** |
| Apps | UI app, Admin app, API (the only route to the database), shared library |
| Hosting | Two Windows Server 2025 VMs in the organisation's data centre; each app a Windows service under its own group managed service account |
| Platform | .NET 10, ASP.NET Core, Blazor Server, EF Core with the SQL Server provider |
| Database | **Microsoft SQL Server 2022**. Each schema is its own database schema. The API connects with **Windows authentication** (no database password) over TLS with strict encryption, TCP 1433 |
| Sign-in | **PingFederate** by **OpenID Connect**, with MFA, against Active Directory. The signed response names the person and carries no groups |
| Groups | The **API reads group membership directly from Active Directory over LDAPS** (TCP 636), read-only |
| Roles | Reader, Editor, **Administrator** (one role: no separate global administrator), Auditor, Security officer, Business owner, Legal adviser's delegate. Five role groups: \<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners, \<Code\>\_LegalSearch |
| Audit log review | **Auditors** read and review the audit log weekly (P-08, NFR-027) and report anything suspicious to the security officer. The security officer reviews alerts and the central logs, and does not read the audit log |
| Schema ownership | Each schema's read and edit groups are owned by its **Data Owner**, who authorises access |
| Access approval | **ServiceNow** workflow (never Jira) |
| Sessions | **No session management in the application**: no session records, idle lock, idle timeout, session limit, sign-out or session-ending screen. AC-11 and AC-11(1) come from the device screen lock; AC-12 and AC-2(5) from PingFederate's sign-in lifetime. The app holds the sign-in only in its ASP.NET Core authentication cookie, with a lifetime no longer than PingFederate's |
| Build | Under the organisation's **corporate SDLC**, inherited |
| Flows | F1 browser to UI; F2 admin route to Admin; F3, F4 apps to API on loopback; F5 API to SQL Server; F6 browser to PingFederate; F7 API to AD over LDAPS; F8 servers to time, logging, proxy and backup; F9 ServiceNow and starters and leavers, people only; F10 application server to PingFederate (OpenID Connect metadata, signing certificate, completing sign-in); F11 administrators' managed devices to both servers over the managed administration route |
| Parameters | The System Description's P-01 to P-35 (section 4). Refer to them where a family document sets the same value |
| Figure | `figures/sd-figure-1.png` is the architecture figure |

## 3 Review and approval information

None. See section 1.

## 4 Method

1. Read `System Description.md` in full first: it is the reference, and every fact in your documents must agree with it.
2. Read the whole document. Fix everything that contradicts it: sentences about tokens carrying groups, session controls, global administrator rows in tables, PostgreSQL-specific features such as SCRAM-SHA-256, and anything that contradicts section 2.
3. Grep afterwards for: `session`, `token`, `global admin`, `project`, `AD FS`, `PostgreSQL`, `superuser`, `SCRAM`, `pg_`, `psql`, `Docker`, `container`, `Linux`, `password` (the API has no database password; users have none in the app), `signing key`, `jsDelivr`, `CDN`, `Jira`, `document` where the design says item, and `a administrator`.
4. Keep the document's own structure, numbering and plain-English style. No em dashes. If a section or table is added or removed, renumber those that follow and every reference to them, across the set.
