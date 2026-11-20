# Aligning a document with the System Description

Working rules for bringing each document in the set into line with `System Description.md`, the generic Secure by Design reference. Worked example: `Access Control Management.md`, which was done by hand as the pilot.

## 1 What stays

- Every control's **status** (Implemented, Partially implemented, Not implemented, Not applicable) and the findings, test results (T-numbers), weaknesses (PA-), risks (NC-), evidence requests (EV-), tailoring (TR-) and decision (D-) references, where they still hold for the reference design.
- Test results describe the **tested v1.0 build**, which signed in with its own passwords, held its groups and sessions in its own database and ran PostgreSQL in containers. Keep them, but say so where the reference design differs, for example "the tested build had a page lock after 25 minutes (T53), which the reference design does not have".
- Appendix A "How it is built today" and similar records of the tested build stay as records of that build, with a note that the reference design differs.

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
| Roles | Reader, Editor, **Administrator** (one role: no separate global administrator), Auditor, Security officer. Three role groups: \<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security |
| Schema ownership | Each schema's read and edit groups are owned by its **Data Owner**, who authorises access |
| Access approval | **ServiceNow** workflow (never Jira) |
| Sessions | **No session management in the application**: no session records, idle lock, idle timeout, session limit, sign-out or session-ending screen. AC-11 and AC-11(1) come from the device screen lock; AC-12 and AC-2(5) from PingFederate's sign-in lifetime. The app holds the sign-in only in its ASP.NET Core authentication cookie, with a lifetime no longer than PingFederate's |
| Build | Under the organisation's **corporate SDLC**, inherited |
| Flows | F1 browser to UI; F2 admin route to Admin; F3, F4 apps to API on loopback; F5 API to SQL Server; F6 browser to PingFederate; F7 API to AD over LDAPS; F8 servers to time, logging, proxy and backup; F9 ServiceNow and starters and leavers, people only |
| Parameters | The System Description's P-01 to P-35 (section 5). Refer to them where a family document sets the same value |
| Figure | `figures/sd-figure-1.png` replaces `figures/arch-figure-1.png` |

## 3 Review and approval information is removed

The set is treated as **not yet reviewed or approved**.

- Document control: Status "Draft, not yet reviewed or approved"; Date 20 November 2026; Classification `\<Classification\>`; approval rows Pending.
- Change history: replace with one row describing the alignment, plus "Earlier: the earlier versions. Their history is kept in the change record".
- "Approved (D-x)" becomes "Proposed (D-x), not yet approved"; "Approved;" becomes "Not yet approved;".
- "Reviewed on (date)", "legally reviewed", "approved by the Head of Cyber", "the system owner approved these values on (date)" and similar: remove, or say not yet reviewed or approved.
- Risk decisions "approved" or "accepted" become "acceptance proposed, not yet decided".
- Design decisions keep their D- reference but lose "the system owner decided on (date)".

## 4 Method

1. Run `python3 tools/align_terms.py "<Document>.md"` for the mechanical term pass.
2. Read the whole document. Fix what the term pass cannot: sentences about tokens carrying groups, session controls, global administrator rows in tables, PostgreSQL-specific features such as SCRAM-SHA-256, and anything that contradicts section 2.
3. Grep afterwards for: `session`, `token`, `global admin`, `project`, `AD FS`, `PostgreSQL`, `superuser`, `SCRAM`, `Jira`, `Approved`, `reviewed on`, `approved by`, `accepted`, `a administrator`.
4. Keep the document's own structure, numbering and plain-English style. No em dashes.
