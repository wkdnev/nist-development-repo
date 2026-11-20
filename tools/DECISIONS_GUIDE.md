# Four design decisions to carry through the set

`System Description.md` now records these. Make every document and figure agree.

1. **Auditors review the audit log.** Auditors read the audit log and review it weekly (P-08, NFR-027), compare it with the server, database, PingFederate and Active Directory records, record the review, and report anything suspicious to the security officer. The security officer reviews alerts and the central logs, leads incident response, and does not read the audit log. Change any text that has the security officer, or anyone else, reviewing or reading the application audit log.
2. **New flow F10.** UI application and Admin application, from the application server, to \<Organisation\>'s PingFederate: fetching the OpenID Connect metadata and signing certificate, and completing each sign-in. HTTPS, TCP 443, from the application server only. Firewall allow-lists, flow tables, interface records and evidence requests that list flows gain it.
3. **New flow F11.** Server and database administrators' managed devices to both servers: server and database administration, only over \<Organisation\>'s managed administration route, with multi-factor authentication, using named accounts. Where a document has an unnumbered row for this route, number it F11.
4. **Two new roles.**
   - **Business owner** (role in the application): approves the disposal of items due under the retention schedule (FR-074). Admin application. Group \<Code\>\_BusinessOwners.
   - **Legal adviser's delegate**: searches every schema for one person's items to answer a request under data protection law (FR-073). Holds no other role. Admin application. Group \<Code\>\_LegalSearch, named by the legal adviser.
   - There are now five role groups: \<Code\>\_Admins, \<Code\>\_Auditors, \<Code\>\_Security, \<Code\>\_BusinessOwners, \<Code\>\_LegalSearch. The system owner owns all five. Change "three role groups" to five, and add the two roles to role tables, permission tables, training matrices, personnel risk designations, account types and interview roles where those list every role.

"F1 to F9" becomes "F1 to F11" where it means every flow. Keep each document's structure, numbering and style; plain British English; no em dashes, NIST, dates, approvals or records. Edit only your files. No git commands. Report what you changed.
