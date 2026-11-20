# \<System Name\> Control Assessment Record

## 1 How to use this document

This document is the record of the Level 1 self-assessment of \<System Name\> against CSS. It has one chapter for each of the 19 control families assessed, in CSS order, and each chapter gives a finding for every determination statement. The totals across all chapters are in \<Security Assessment Report\>, which is generated from this record.

Level 1 is a self-assessment and is not independent. Each chapter holds its own assessment plan, and all 19 plans were approved by the authorising official (D-GEN-18).

- **Chapters.** Each chapter is named by its family code. Its sections carry the code, so PS.3 is section 3 of the Personnel Security chapter, and its tables are numbered Table PS-1, Table PS-2 and so on.
- **Citing.** Cite a chapter as \<Control Assessment Record\> (PS), a section as \<Control Assessment Record\>, section PS.3, and a table as \<Control Assessment Record\>, Table PS-1.
- **Versions.** The document has one version. A change to any chapter is a new version of the document.

### 1.1 Findings

Findings follow CSS. Each determination statement gets one of these.

**Table 1: Finding codes**

| Code | Meaning |
| --- | --- |
| S | Satisfied |
| N/A | Not applicable. It is counted in the chapter's statements, but not as satisfied |
| O-D | Other than satisfied: a decision or approval is outstanding, or the control has not yet started to operate |
| O-G | Other than satisfied: a gap in the system |
| O-E | Other than satisfied: evidence from the VMs or \<Organisation\> is not available |

The AC chapter was assessed first and uses the result scale in its Table AC-1.

### 1.2 What is the same in every assessment plan

Each chapter ends with its assessment plan. These parts are the same for every family, so they are stated once here, and a chapter repeats one only where it differs.

**Table 2: Assessment plan, common to every chapter**

| Item | Detail |
| --- | --- |
| System | \<System Name\> v1.0, at the commits in \<System Security Plan\>, section 2 |
| Security categorisation | Moderate, confirmed by the authorising official |
| Assessor | Level 1: Claude, an AI assistant, working for the system owner. Level 2: an independent team led by \[Name\], which meets CA-2(1) at Moderate once TPL-19 is completed |
| Level 2 team and schedule | \[Name\]'s team: \[members, dates and the depth and coverage to be agreed with the independent assessor\] |
| Approval | Approved by the authorising official (D-GEN-18), as confirmed by the system owner on 8 November 2026 |

## AC Access Control

### AC.1 Purpose

This records the initial self-assessment of \<System Name\> against each Moderate baseline AC control and enhancement. Section AC.3 is the executive summary, section AC.5 holds the finding for each CSS statement, and section AC.6 is the assessment plan.

### AC.2 How to read this record

**Change since this assessment.** On 12 November 2026 the system owner stated that \<System Name\> signs users in through \<Organisation\>'s AD FS, with multi-factor authentication, takes roles and project access from Active Directory groups, and holds no accounts or passwords of its own (D-AC-23). This chapter assessed the v1.0 build, which signed in with its own passwords and held its accounts and groups in its own database. Its findings are a true record of that build and are not changed. The findings on sign-in, passwords, lockout, accounts and group membership are to be made again with AD FS sign-in, when the tests are repeated and \<Organisation\>'s evidence is in (PA-95).

This is the Level 1 self-assessment, and it makes no fixes. An independent team led by \[Name\] will use it for the Level 2 assessment. A finding does not by itself require a fix: each non-compliance is rated and decided in \<Risk List\>, and only those to be remediated go to \<Plan of Action and Milestones\>. The AC-3 fixes were made before this approach was agreed and are kept, so AC-3 describes the system with them in place.

Each entry follows the CSS approach: the objectives come from CSS, and each gets one of these results.

**Table AC-1: Result scale**

| Result | Meaning |
| --- | --- |
| Satisfied | The evidence shows the objective is met |
| Other than satisfied | The evidence shows a gap, or an approval is outstanding |
| Other than satisfied (E) | CSS has no separate result for missing evidence. This marks objectives where the VMs or \<Organisation\>'s evidence are not available |
| Not applicable | The system owner decided the objective does not apply, with a reason and any condition recorded in \<Tailoring Register\>. This is an organisation's tailoring decision, not a result under CSS, and the independent assessor may test it |

The three methods are **Examine** (documents, code and configuration), **Test** (running the mechanism) and **Interview** (asking the people responsible). The system owner has answered INT-AC-01 to 34 in writing (\<Interview Guide\>, section 22.1). No records were seen, so these answers change no finding, and the role holders and \<Organisation\> have not been interviewed.

**Limit of the current evidence:** \<System Name\> ran in Docker on one PC with sample data. The 75 checks were re-run on the tagged v1.0 build on 8 November 2026 and gave the same results (ac-test-results-2026-11-08-v1.0.csv, with hashes in MANIFEST.md). The Windows Server 2025 VMs, PostgreSQL on Windows and \<Organisation\>'s services have not been examined.

### AC.3 Executive summary

**Table AC-2: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Not applicable, subject to the conditions in \<Tailoring Register\> | 6 | AC-2(2), AC-17(4), AC-19, AC-19(5), AC-20(1), AC-22 |
| Other than satisfied, with at least one system gap | 20 | AC-2, AC-2(1), AC-2(3), AC-2(4), AC-3, AC-4, AC-5, AC-6, AC-6(1), AC-6(2), AC-6(5), AC-6(7), AC-6(9), AC-6(10), AC-7, AC-8, AC-11, AC-14, AC-17(2), AC-21 |
| Other than satisfied, needing only a decision, approval or evidence | 13 | AC-1, AC-2(5), AC-2(13), AC-11(1), AC-12, AC-17, AC-17(1), AC-17(3), AC-18, AC-18(1), AC-18(3), AC-20, AC-20(2) |

**Table AC-2a: Result for each control**

| Control | Result | Statements satisfied | Summary | Finding |
| --- | --- | --- | --- | --- |
| AC-1 | Other than satisfied | 21 of 25 | The policy is approved by the Head of Cyber and the procedures by the system owner (D-AC-01, D-AC-02). They are not yet shared, and coordination with \<Organisation\> is not yet agreed | NC-01, PA-20 |
| AC-2 | Other than satisfied | 14 of 36 | The system can create, change, disable and remove accounts, and disabling works at once. The rules and procedures are approved (D-AC-02, D-AC-03), but they are not yet walked through or in use: no approval is enforced in the system, no review has happened, and accounts are not linked to \<Organisation\>'s staff processes | NC-02, PA-16, PA-20, PA-32 |
| AC-2(1) | Other than satisfied | 1 of 2 | The system automates parts of account management, and the mechanisms are approved (D-AC-03). But accounts sit apart from \<Organisation\>'s directory, and there are no account reports | NC-03, PA-13, PA-16, PA-32 |
| AC-2(2) | Not applicable | None applies | Temporary and emergency accounts are not allowed until the system can expire them (P-AC-09, TR-AC-01). The system cannot expire any account (PA-13), so the Level 2 assessor should check that none exist | TR-AC-01 |
| AC-2(3) | Other than satisfied | 2 of 6 | A disabled account stops working at once, and the time limits are approved (D-AC-03). But nothing disables accounts automatically, and the procedures have not yet been walked through | NC-05, PA-13 |
| AC-2(4) | Other than satisfied | 0 of 5 | Most account changes made in the admin portal have no audit call, and the API's records name "System" instead of the person | NC-06, PA-14 |
| AC-2(5) | Other than satisfied | 1 of 2 | The server ends a session idle for 30 minutes, as tested. The value is approved (D-AC-03), but the rule cannot yet be assessed for server administrators on the VMs | NC-07, PA-20, PA-30 |
| AC-2(13) | Other than satisfied | 2 of 3 | The mechanism works: disabling ends API and web access immediately. The 1-hour limit and its triggers are approved (D-AC-03), but PRO-AC-4 has not yet been walked through or used | NC-08, PA-20 |
| AC-3 | Other than satisfied | 0 of 1 | Project access is enforced and tested, but ordinary users can still reach some session functions, and the database role and secrets give too much access | NC-09, PA-02, PA-19, PA-25, PA-26 |
| AC-4 | Other than satisfied | 1 of 2 | The target flows are drawn, but nothing enforces them yet, and browsers also fetch code from an outside service that was not in the design | NC-10, PA-18, PA-26, PA-34 |
| AC-5 | Other than satisfied | 2 of 3 | Administrator, auditor and security roles exist, an auditor cannot manage users, and the split of duties is approved (D-AC-03). But a global administrator still holds all their rights | NC-11, PA-15 |
| AC-6 | Other than satisfied | 0 of 1 | Readers and editors are limited to their projects, and the apps do not run as root in Docker. But the apps share a database superuser, global administrators reach everything, and some privileged functions are open to everyone | NC-12, PA-10, PA-19, PA-26, PA-31 |
| AC-6(1) | Other than satisfied | 5 of 9 | In the application, the main security functions are limited to the right roles, and that was tested. Who may use them is approved (D-AC-03), but security-relevant information is too widely available, and the VMs are not available to assess | NC-13, PA-07, PA-15, PA-19, PA-30 |
| AC-6(2) | Other than satisfied | 1 of 2 | The rule is approved (D-AC-03), but separate everyday accounts have not been issued, and nothing in the system prevents a global administrator using their privileged account for document work. The risk of no system enforcement is accepted (NC-14) | NC-14, PA-17 |
| AC-6(5) | Other than satisfied | 1 of 2 | Global administrator is limited to named accounts, and only one exists in the sample data. The privileged roles are approved (D-AC-03), but no approval is enforced in the system, the apps' database role is a superuser, and the VM accounts are not yet limited | NC-15, PA-10, PA-30 |
| AC-6(7) | Other than satisfied | 2 of 4 | No review has happened. PRO-AC-7 and the review intervals are approved (D-AC-02, D-AC-03), and the Project Role Summary page shows assignments, but the system has no review record | NC-16, PA-16 |
| AC-6(9) | Other than satisfied | 0 of 1 | Some privileged functions are logged, but many are not, some logs name the wrong actor, and the VM logs are not available | NC-17, PA-14, PA-29, PA-31 |
| AC-6(10) | Other than satisfied | 0 of 1 | The main administration functions are protected, but ordinary users can still run some privileged functions. These include changing another user's session role, clearing the API cache, writing audit records and starting a database migration | NC-18, PA-02, PA-03, PA-06, PA-07, PA-29 |
| AC-7 | Other than satisfied | 4 of 8 | The application mechanism works as tested: five failures lock the account for 15 minutes, and it unlocks afterwards. The values are approved (D-AC-03) | NC-19, PA-20, PA-30, PA-35 |
| AC-8 | Other than satisfied | 1 of 11 | No notice is shown on either sign-in page. The wording in P-AC-16 is approved by the system owner, subject to legal review (D-AC-06), but it is not built (PA-11) | NC-20, PA-11 |
| AC-11 | Other than satisfied | 2 of 4 | A browser overlay appears after 25 minutes, but "Continue Session" removes it without a password, so it is not a true lock. The overlay runs in the browser, so it does not by itself stop a browser user reaching the page behind it | NC-21, PA-12, PA-21 |
| AC-11(1) | Other than satisfied | 0 of 1 | The code draws a dark overlay at 92% opacity, but this has not been seen on screen, so there is no evidence yet that it fully hides what was displayed. Workstation lock screens depend on \<Organisation\> | NC-22, PA-21 |
| AC-12 | Other than satisfied | 1 of 2 | Sessions end after idling, at the 8-hour limit, on sign-out and when revoked. The values are approved (D-AC-03), but one unexplained test result needs resolving (PA-33), and the VMs are not available | NC-23, PA-20, PA-30, PA-33 |
| AC-14 | Other than satisfied | 3 of 4 | The list of what works without signing in is approved (D-AC-12), and the SSP gives its rationale. The result stays open because other endpoints still answer without signing in (PA-03, PA-07), and Windows and PostgreSQL are not yet examined | NC-24, PA-03, PA-07, PA-28 |
| AC-17 | Other than satisfied | 0 of 4 | The remote access route is not named, and no restrictions are written down | NC-25, PA-18 |
| AC-17(1) | Other than satisfied | 0 of 2 | Expected from \<Organisation\>, with no evidence yet | NC-26, PA-18, PA-21 |
| AC-17(2) | Other than satisfied | 0 of 1 | The stack as run in Docker uses plain HTTP, and HTTPS and database TLS are not set up. The apps do include HTTPS redirection and HSTS settings, but these are not in effect in the tested configuration | NC-27, PA-18 |
| AC-17(3) | Other than satisfied | 0 of 1 | Expected from \<Organisation\>, with no evidence yet | NC-28, PA-18, PA-21 |
| AC-17(4) | Not applicable | None applies | Administrators may not work through external networks, and administer the VMs only from inside \<Organisation\>'s network (D-AC-08, TR-AC-05) | TR-AC-05 |
| AC-18 | Other than satisfied | 0 of 4 | \<System Name\> provides no wireless access of its own | NC-30, PA-21 |
| AC-18(1) | Other than satisfied | 1 of 3 | Expected from \<Organisation\>, with no evidence yet | NC-31, PA-21 |
| AC-18(3) | Other than satisfied | 0 of 1 | Server VMs normally have no wireless adapter, but this needs confirming on the built VMs | NC-32, PA-21 |
| AC-19 | Not applicable | None applies | Phones and tablets may not use \<System Name\> in the first release (D-AC-09, TR-AC-06). The system does not identify the device, so the rule depends on \<Organisation\>'s network access control | TR-AC-06 |
| AC-19(5) | Not applicable | None applies | As AC-19 (TR-AC-06) | TR-AC-06 |
| AC-20 | Other than satisfied | 5 of 7 | The rule is approved: no external systems or portable storage without the system owner's approval (D-AC-10). Enforcement depends on \<Organisation\>, because the system cannot tell whether a browser is on an approved device | NC-35, PA-21 |
| AC-20(1) | Not applicable | None applies | External use is forbidden, so there is nothing to verify or agree (TR-AC-07) | TR-AC-07 |
| AC-20(2) | Other than satisfied | 1 of 2 | Downloads and bulk export can reach any device the user has, so this depends on \<Organisation\>'s USB and device controls | NC-37, PA-21 |
| AC-21 | Other than satisfied | 3 of 4 | Nothing helps users judge whether sharing a document outside a project is allowed, and project groups control access only inside \<System Name\> | NC-38, PA-22 |
| AC-22 | Not applicable | None applies | \<System Name\> holds no public content (D-AC-11, TR-AC-08) | TR-AC-08 |

\<System Name\> does not yet fully satisfy any of the 39 entries, because each has at least one statement outstanding or is not applicable. At statement level the position is clearer. Of the CSS 189 statements, 74 are satisfied, 29 are not applicable under \<Tailoring Register\>, 22 await a decision or approval, 39 show a gap in the system, 21 await evidence from the VMs or \<Organisation\>, and 4 are parameters not selected.

The organisation takes a risk-based approach, and does not require every control to be met. Every entry therefore has a non-compliance record in \<Risk List\>, with a risk rating and a proposed treatment: accept, remediate, approve, obtain evidence or tailor. The system owner decided the Low items on 5 November 2026; the Medium and High items await the authorising official. The most serious gaps are the High items in \<Plan of Action and Milestones\>, and \<Plan of Action and Milestones\>, section 5, gives the recommended order of work. This assessment made no fixes, apart from the AC-3 fixes already kept.

### AC.4 Control results

Controls appear in the order they were assessed, which section AC.6 explains. On 8 November 2026 each result and objective here was brought into line with the decisions of 5 and 6 November. Section AC.5 holds the finding for each statement and takes precedence.

Find a control: AC-1 | AC-2 | AC-2(1) | AC-2(2) | AC-2(3) | AC-2(4) | AC-2(5) | AC-2(13) | AC-3 | AC-4 | AC-5 | AC-6 | AC-6(1) | AC-6(2) | AC-6(5) | AC-6(7) | AC-6(9) | AC-6(10) | AC-7 | AC-8 | AC-11 | AC-11(1) | AC-12 | AC-14 | AC-17 | AC-17(1) | AC-17(2) | AC-17(3) | AC-17(4) | AC-18 | AC-18(1) | AC-18(3) | AC-19 | AC-19(5) | AC-20 | AC-20(1) | AC-20(2) | AC-21 | AC-22

#### AC.4.1 AC-3 Access Enforcement

**Result: Other than satisfied.** Project access is enforced and tested, but ordinary users can still reach some session functions, and the database role and secrets give too much access. No AC-3 enhancements are in the Moderate baseline.

**What it requires:** the system must enforce approved authorisations for logical access to information and system resources, in line with access control policies.

**Table AC-3: AC-3 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-03: approved authorisations for logical access are enforced in line with policy | Other than satisfied | See below |

**Table AC-4: AC-3 findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Project read and edit | Enforced through access-control-toolkit, denied by default, including pages, tiles, export and bad file reports | T11 to T23, T48, T56 to T64; browser check |
| Session functions | Any signed-in user can change another user's session role and create session records for them | T33, T34 (PA-02) |
| Export to Folder | An editor can write exports to any server folder the service can reach | Code review (PA-26) |
| API addresses with no project | Access is checked, but the wrong document may be found | Code review (PA-25) |
| Database and secrets | Apps share a superuser role; secrets are committed | T55, Code (PA-10, PA-19) |
| Policy | The policy this control refers to is approved by the Head of Cyber (D-AC-01); it was legally reviewed on 12 November 2026 | \<Policy\> (AC) (PA-20) |
| Windows and PostgreSQL permissions on the VMs | Other than satisfied (E) | VMs not available |

**Examined:** draft policy and procedures, code for all three apps and shared library, configuration, and test results. **Tested:** 23 AC-3 checks, all passing, plus a browser check; these check the mechanisms already fixed, not the items above. **Interviewed:** nobody yet. **Not covered:** every action on every Blazor page was not exercised.

#### AC.4.2 AC-14 Permitted Actions Without Identification or Authentication

**Result: Other than satisfied.** The list of what works without signing in is approved (D-AC-12), and the SSP gives its rationale. The result stays open because other endpoints still answer without signing in (PA-03, PA-07), and Windows and PostgreSQL are not yet examined. No AC-14 enhancements are in the Moderate baseline.

**What it requires:** the organisation must decide which user actions are allowed without signing in, consistent with its mission, and record them with a rationale in the security plan. It does not require that there be none.

**Table AC-5: AC-14 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-14\_ODP: the permitted actions are defined | Other than satisfied | No approved list exists; the proposed list is in \<Access Control Management\> (P-AC-25) |
| AC-14a: actions are identified, consistent with mission and business functions | Other than satisfied | Identified below for the apps and approved (D-AC-12), but other endpoints are open (PA-03, PA-07); Windows and PostgreSQL not yet examined |
| AC-14b\[01\]: actions are documented in the security plan | Other than satisfied | The SSP pointed to a list in \<Access Control Management\> without stating the actions; now stated, but still a draft |
| AC-14b\[02\]: a rationale is given in the security plan | Satisfied | The rationale below is approved (D-AC-12) |

##### AC.4.2.1 What works without signing in

Every route without parameters in UI application (35) and Admin application (51) was requested without signing in, along with 18 API addresses and some static files. All other routes redirected to sign-in or were refused.

**Table AC-6: Actions that work without signing in**

| Action | Where | Result | Proposed rationale | Assessment |
| --- | --- | --- | --- | --- |
| See the sign-in page and sign in | UI application, Admin application, the API sign-in function | 200 | Needed before anyone can identify themselves | Acceptable |
| See the signed-out and session-expired pages | UI application, Admin application | 200 | Shows the result of ending a session; holds no data | Acceptable |
| Change an expired temporary password | the change password page | Redirects to sign-in unless a correct password was just entered | Part of signing in | Acceptable |
| See the access denied page | Admin application | 200 | Explains a refusal; holds no data | Acceptable |
| Load scripts, styles and images | Static files in UI application and Admin application | 200 | Needed to draw the sign-in page; holds no business data | Acceptable; contents not reviewed file by file |
| Check service health | The API's health check | 200, one status word | Monitoring | Acceptable if the organisation agrees |
| Read cache statistics | API the cache statistics function | 200 | None | Finding (PA-03) |
| Clear the API cache | API the cache clearing function, the permission cache clearing function | 200 in test | None | Finding (PA-03) |
| Read diagnostic health, including the environment name | API the security test health function | 200 | None | Finding (PA-07) |
| Call a diagnostic endpoint | The API's test sign-in function | 500 | None | Finding (PA-07) |
| Open a test page | UI application the icon test page | 200 | None | Finding (PA-07) |

The UIs deny anything not marked as open, through a fallback policy. The API does not, which is the root cause of its open endpoints. Swagger is not exposed in the Production configuration.

**Examined:** authorisation attributes in all controllers and pages, the start-up configuration in each app, draft policy, SSP. **Tested:** read-only anonymous requests against the running stack (ac-14-anonymous-probe-2026-11-05.csv), and T01 to T09 on a throwaway stack, including clearing the cache (T08). **Interviewed:** nobody yet.

**Other than satisfied (E):** anonymous access to Windows Server 2025 and to PostgreSQL on the VMs, such as anonymous shares and database client authentication rules.

**Needed to close the documentation part:** the system owner approves the list and rationale.

#### AC.4.3 AC-6(10) Prohibit Non-privileged Users from Executing Privileged Functions

**Result: Other than satisfied.** The main administration functions are protected, but ordinary users can still run some privileged functions. These include changing another user's session role, clearing the API cache, writing audit records and starting a database migration. Moderate has no further enhancements under AC-6(10).

**What it requires:** the system must stop users without the right authorisation from running privileged functions. The CSS examples include changing or bypassing security controls, creating accounts and managing keys. Hiding a button is not enough, so the refusal has to happen where the function runs.

**Table AC-7: AC-6(10) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06(10): non-privileged users are prevented from executing privileged functions | Other than satisfied | See below |

**Table AC-8: AC-6(10) findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Managing users, groups, projects, roles and credentials | All 30 admin portal pages require a role or policy. A reader was refused each one tested | T26, T28, T29; code |
| Listing and ending other users' sessions | Refused for ordinary users in the API and UI application | T24, T25, T27 |
| Session role and session records | Any signed-in user can change another user's session role and create session records for them | T33, T34 (PA-02) |
| Notifications | Any signed-in user can notify anyone and run clean-up. The code comment says "Admin only", but nothing enforces it | T35, T36 (PA-06) |
| API cache | Anyone can clear it, without signing in | T07, T08 (PA-03) |
| Audit log | A reader wrote audit records from diagnostic pages, one of them under the name of a diagnostic tool, not a person | Browser check (PA-29) |
| Database changes | A reader could press Apply Security Migrations and Force Create AuditLog Table. Neither changed anything, because no migrations were pending and the second has a syntax error on PostgreSQL. No access check stopped them | Browser check (PA-29) |
| Becoming an administrator | A reader pressed Fix Global Admin Status and stayed a reader, because that method does nothing in UI application. The page wrongly reported success. This is an accident of the code and not a control | Browser check; code review (PA-29) |
| Assigning roles from diagnostic pages | The method called throws an error in UI application, so nothing is assigned. the test user set-up page would create a ReadOnly role if it were missing | Code review (PA-29) |
| Diagnostic pages and API | Any signed-in user can open them and read all users, their administrator flags and all projects. the role debugging page fails with a server error, not a refusal | T30 to T32, T65 to T70 (PA-07) |
| Build guard | These pages carry a marker meant to leave them out of a release, but the build does not honour it. The pages are in the release build and display the marker as text | Browser check; compiled DLL (PA-07, PA-29) |
| Database | The apps connect as a superuser, so application checks are the only barrier if one is missed | T55 (PA-10) |
| List of privileged functions | The proposed list and role assignments are in \<Access Control Management\> and P-AC-17, and neither is approved | PA-20 |
| Windows and PostgreSQL privileged functions on the VMs | Other than satisfied (E) | VMs not available |

**Examined:** authorisation on every API controller and every page in all three apps, the code behind each diagnostic page, the compiled UI application DLL, draft policy, access control model and SSP.

**Tested:** T24 to T36 and T65 to T70 as demo.reader (ac-test-results-2026-11-05-ac6-10.csv), and actions on the diagnostic pages in a browser (ac-6-10-browser-check-2026-11-05.csv). All of it ran on a throwaway stack.

**Interviewed:** nobody yet.

**Not covered:** every action inside every admin page was not exercised, audit records were not checked for this control, and the export and session clean-up background services were only listed. The AC-6(9) and AC-2 assessments return to audit and account functions.

#### AC.4.4 AC-6(1) Authorize Access to Security Functions

**Result: Other than satisfied.** In the application, the main security functions are limited to the right roles, and that was tested. Who may use them is approved (D-AC-03), but security-relevant information is too widely available, and the VMs are not available to assess.

**What it requires:** the organisation must name who may use its security functions, in hardware, software and firmware, and who may see security-relevant information, then authorise only them. The CSS examples include creating accounts, setting permissions and audit settings, firewall rules, security service settings, key management information and access control lists.

**Table AC-9: AC-6(1) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06(01)\_ODP\[01\]: individuals and roles are defined | Satisfied | Roles approved in \<Access Control Management\> (D-AC-03), with holders named in \<Roles and Responsibilities\> |
| AC-06(01)(a)\[01\]: access to security functions in hardware is authorised | Other than satisfied (E) | VMs not available; the physical hosts depend on \<Organisation\> |
| AC-06(01)(a)\[02\]: access to security functions in software is authorised | Other than satisfied | Enforced for the main functions, with the exceptions below |
| AC-06(01)(a)\[03\]: access to security functions in firmware is authorised | Other than satisfied (E) | VMs not available; firmware depends on \<Organisation\> |
| AC-06(01)(b): access to security-relevant information is authorised | Other than satisfied | See below |

**Table AC-10: AC-6(1) findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Users, groups, projects, roles, credentials and schema changes | Only global administrators can reach these pages | T26, T28, T29; code |
| Audit logs and security pages | A reader is refused, an auditor can read audit logs, and an auditor cannot manage users | T71 to T74 |
| Global administrators and audit logs | A global administrator can read the logs of their own actions, which the proposed model does not allow | T75 (PA-15) |
| Security functions outside those roles | Session roles, notification clean-up, the API cache and audit writes are open, as recorded under AC-6(10) | T07, T08, T33 to T36 (PA-02, PA-03, PA-06, PA-29) |
| User and project information | Any signed-in user can see all users, their administrator flags and all projects | T30, T65, T70 (PA-07) |
| Signing key and database password | Both are committed in the applications' settings files, so anyone who can read the repositories can read them. The files also name a remote database | Code review (PA-19) |
| Password hashes, sessions and access groups in the database | All three apps can reach these through one superuser role | T55 (PA-10) |
| Definition of security-relevant information | The drafts had none. A proposed list is now in P-AC-17 | \<Access Control Management\> (PA-20) |
| Windows, PostgreSQL, firewall rules, certificates, hypervisor and network | Other than satisfied (E). Nobody is named for these, and any part inherited from \<Organisation\> needs a named service and evidence | PA-30 |

**Examined:** authorisation on admin portal pages, role and policy definitions, tracked settings files by name and earlier code review, draft policy, access control model, and roles document.

**Tested:** T26, T28, T29 and T71 to T75, on a throwaway stack (ac-test-results-2026-11-05-ac6-1.csv).

**Interviewed:** nobody yet.

**Not covered:** the Security officer role has no account in the sample data, so a positive test of that role was not run. Static files and error pages were not checked for security-relevant information.

#### AC.4.5 AC-6 Least Privilege

**Result: Other than satisfied.** Readers and editors are limited to their projects, and the apps do not run as root in Docker. But the apps share a database superuser, global administrators reach everything, and some privileged functions are open to everyone.

**What it requires:** users, and processes acting for them, must have only the access they need for their assigned tasks.

**Table AC-11: AC-6 objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06: least privilege is employed for users and processes | Other than satisfied | See below |

**Table AC-12: AC-6 findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Readers and editors | Limited to their own projects, and refused administration | T11 to T29, T48, T56 to T64 |
| Global administrators | Can read and edit every project, including HR, whether or not their task needs it. The proposed model allows this, and the system owner should decide whether it should | T18; \<Access Control Management\> (PA-15) |
| Open functions | Session, notification, cache, audit-writing and diagnostic functions go beyond what ordinary users need | AC-6(10) above (PA-02, PA-03, PA-06, PA-07, PA-29) |
| App processes on the database | All three apps use one superuser role, and the UIs also read the database directly | T55 (PA-10) |
| App processes in Docker | The web and API containers checked run as user 1654, not root | The user identity in the running containers; the image build file |
| Export to Folder | An editor can write to any folder the service can reach | Code review (PA-26) |
| Destructive maintenance pages | Fresh Start can delete every project and reset role data, and Legacy Cleanup, Fix Duplicate Users and Database Update also remain available in production. Only global administrators can reach them | Code review (PA-31) |
| Unused API address | the page upload function has no caller in either UI, and it names no project | Code review (PA-25) |
| Secrets | The signing key and database password are readable in the repositories | Code review (PA-19) |
| Windows service accounts and permissions on the VMs | Other than satisfied (E) | VMs not available (PA-18, PA-30) |

**Examined:** code, the image build file, compose file and the model. **Tested:** the checks above on a throwaway stack, and read-only identity and role queries on the running stack. **Interviewed:** nobody yet. **Not covered:** the maintenance pages were read but not run.

#### AC.4.6 AC-6(5) Privileged Accounts

**Result: Other than satisfied.** Global administrator is limited to named accounts, and only one exists in the sample data. The privileged roles are approved (D-AC-03), but no approval is enforced in the system, the apps' database role is a superuser, and the VM accounts are not yet limited.

**What it requires:** privileged accounts must be restricted to defined people or roles.

**Table AC-13: AC-6(5) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06(05): privileged accounts are restricted to defined personnel or roles | Other than satisfied | Roles approved (D-AC-03) and holders named; the apps' database role is a superuser (T55, PA-10) |

**Table AC-14: AC-6(5) findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Global administrator | A flag on a named account, with one seeded. Only a global administrator can set it. The system does not require the approval that PRO-AC-6 proposes | T26; code (PA-15) |
| First-user logic | Code that makes the first user an administrator remains. With password sign-in it cannot run without an existing account, so no route to it was found | Code review |
| Database role | The account used by all three apps is a superuser, and it is the only role in the database | T55; read-only role query (PA-10) |
| Windows and PostgreSQL administrators | Other than satisfied (E) | VMs not available (PA-30) |

**Examined:** code, seed data, procedures and the roles document. **Tested:** T26, T55 and read-only queries. **Interviewed:** nobody yet.

#### AC.4.7 AC-5 Separation of Duties

**Result: Other than satisfied.** Administrator, auditor and security roles exist, an auditor cannot manage users, and the split of duties is approved (D-AC-03). But a global administrator still holds all their rights. The system owner accepted this for the first release, with a review every 3 months (D-AC-07).

**What it requires:** the organisation must identify and document the duties that need separating, and define access to support that.

**Table AC-15: AC-5 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-05a: duties of individuals are identified and documented | Satisfied | Approved in \<Access Control Management\> (D-AC-03), with holders named in \<Roles and Responsibilities\> |
| AC-05b: access authorisations to support separation of duties are defined | Other than satisfied | Defined for most roles, but not for global administrators (PA-15) |

**Table AC-16: AC-5 findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Auditors | Can read audit logs and cannot manage users | T73, T74 |
| Global administrators | Can read the audit logs of their own actions, and can grant global administrator without a second person | T75; code (PA-15) |
| Staffing | The named role holders are all different people, so separation looks achievable | Interview needed |
| Windows, PostgreSQL and application administration | Other than satisfied (E); the proposed model keeps them separate | VMs not available (PA-30) |

**Examined:** policy definitions in code, the model and the roles document. **Tested:** T73 to T75. **Interviewed:** nobody yet.

#### AC.4.8 AC-6(2) Non-privileged Access for Nonsecurity Functions

**Result: Other than satisfied.** The rule is approved (D-AC-03), but separate everyday accounts have not been issued, and nothing in the system prevents a global administrator using their privileged account for document work. The risk of no system enforcement is accepted (NC-14).

**What it requires:** people with access to security functions must use a non-privileged account or role for other work.

**Table AC-17: AC-6(2) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06(02): users with access to security functions use non-privileged accounts for other work | Other than satisfied | P-AC-18 approved (D-AC-03); not issued or enforced (PA-17), risk accepted (NC-14) |

**Table AC-18: AC-6(2) findings**

| Part of the stack | Finding | Evidence |
| --- | --- | --- |
| Application | The global administrator account can read documents in every project | T18 (PA-17) |
| Windows and PostgreSQL | Other than satisfied (E) | VMs not available (PA-30) |

**Examined:** code, draft policy and SyOPS. **Tested:** T18. **Interviewed:** nobody yet.

#### AC.4.9 AC-6(9) Log Use of Privileged Functions

**Result: Other than satisfied.** Some privileged functions are logged, but many are not, some logs name the wrong actor, and the VM logs are not available.

**What it requires:** running a privileged function must be logged.

**Table AC-19: AC-6(9) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06(09): the execution of privileged functions is logged | Other than satisfied | See below |

**Table AC-20: AC-6(9) findings**

| Function | Finding | Evidence |
| --- | --- | --- |
| Administrator password reset | Logged, with the administrator's name | Code review |
| Global administrator change at the global administrator page | Logged | Code review |
| Global administrator change at the global administrators page | Not logged | Code review (PA-14) |
| Ending all of a user's sessions | Not logged | T37 (PA-14) |
| Creating or deactivating users, unlocking accounts, group, project and role changes in the admin portal | No audit call found | Code review (PA-14) |
| API user service | Logs delete and deactivate events against "System", not the person | Code review (PA-14) |
| Fresh Start and other maintenance pages | No audit call found | Code review (PA-14, PA-31) |
| Audit log integrity | Ordinary users can add records, so the log cannot yet be fully relied on | Browser check (PA-29) |
| Windows and PostgreSQL | Other than satisfied (E) | VMs not available (PA-30) |

**Examined:** every admin portal page and the services behind them. **Tested:** T37 and T39. **Interviewed:** nobody yet. **Not covered:** most of these results come from reading the code and were not confirmed by performing each action. The AU family will assess audit content and protection in full.

#### AC.4.10 AC-2 Account Management

**Result: Other than satisfied.** The system can create, change, disable and remove accounts, and disabling works at once. The rules and procedures are approved (D-AC-02, D-AC-03), but they are not yet walked through or in use: no approval is enforced in the system, no review has happened, and accounts are not linked to \<Organisation\>'s staff processes.

**What it requires:** a managed account lifecycle: defined account types, named account managers, approval, monitoring, timely notification when people leave or move, and periodic review.

**Table AC-21: AC-2 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02a\[01\], a\[02\]: allowed and prohibited account types are defined | Satisfied | Approved in P-AC-04 (D-AC-03) |
| AC-02b: account managers are assigned | Satisfied | \[Name\] is named in \<Roles and Responsibilities\> |
| AC-02c: prerequisites for group and role membership are required | Other than satisfied | PRO-AC-1 and PRO-AC-5 are drafted, and nothing in the system requires them (PA-20) |
| AC-02d.01, d.02, d.03\[01\]: authorised users, membership and privileges are specified | Other than satisfied | Held per account in the database, but with no approved source to compare against |
| AC-02d.03\[02\]: other account attributes are specified | Other than satisfied | None defined; no expiry attribute exists (PA-13) |
| AC-02e: approval is required to create accounts | Other than satisfied | P-AC-05 approved (D-AC-03); the system has no approval step, and the ServiceNow workflow is not yet set up (PA-20) |
| AC-02f\[01\] to f\[05\]: accounts are created, enabled, modified, disabled and removed under procedure | Other than satisfied | The functions exist and T40 to T42 pass, and PRO-AC-1 to PRO-AC-4 are approved (D-AC-02), but not yet walked through (PA-20) |
| AC-02g: account use is monitored | Other than satisfied | Sign-ins are audited and last sign-in is stored (T39), but no monitoring has been done |
| AC-02h.01 to h.03: account managers are told when accounts or need change | Other than satisfied | P-AC-06 proposes 1 working day, and no route exists yet (PA-32) |
| AC-02i.01 to i.03: access is based on valid authorisation and intended use | Other than satisfied | Enforced from groups (T11), but with no approved authorisation behind them |
| AC-02j: accounts are reviewed | Other than satisfied | No review exists (PA-16) |
| AC-02k\[01\], k\[02\]: authenticators change when someone leaves a shared account | Other than satisfied | P-AC-04 proposes no shared accounts, which would remove the need once approved. The generic admin account would need a named owner |
| AC-02l\[01\], l\[02\]: account management aligns with leaver and transfer processes | Other than satisfied (E) | \<Organisation\>'s processes are not available (PA-32) |

**Windows and PostgreSQL accounts:** evidence is not available, because the VMs are not available (PA-30).

**Sample data:** demo accounts are only created if a demo password is supplied to the setup job. Check that this is never supplied on the VMs.

**Examined:** account model, admin portal pages, services, seed code, draft policy and procedures. **Tested:** T10, T11, T39 to T43. **Interviewed:** nobody yet.

#### AC.4.11 AC-2(1) Automated System Account Management

**Result: Other than satisfied.** The system automates parts of account management, and the mechanisms are approved (D-AC-03). But accounts sit apart from \<Organisation\>'s directory, and there are no account reports.

**Table AC-22: AC-2(1) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02(01): account management is supported by defined automated mechanisms | Other than satisfied | See below |

**Table AC-23: AC-2(1) findings**

| Mechanism | Finding | Evidence |
| --- | --- | --- |
| Forced password change, lockout, ending sessions when disabled | Automated | T10, T40, T41, T49 |
| Disabling for inactivity, expiry, access reports | Not automated | T43; code (PA-13, PA-16) |
| Link to \<Organisation\>'s directory or HR | None, because \<System Name\> uses its own accounts after SSO was removed. A leaver at \<Organisation\> keeps their \<System Name\> account until someone acts | Code review (PA-32) |

#### AC.4.12 AC-2(3) Disable Accounts

**Result: Other than satisfied.** A disabled account stops working at once, and the time limits are approved (D-AC-03). But nothing disables accounts automatically, and the procedures have not yet been walked through.

**Table AC-24: AC-2(3) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02(03)(a): disabled when expired | Other than satisfied | Accounts cannot be given an expiry (PA-13) |
| AC-02(03)(b): disabled when no longer associated with a person | Other than satisfied | Manual, using draft PRO-AC-3 |
| AC-02(03)(c): disabled when in violation of policy | Other than satisfied | Manual, using draft PRO-AC-4 |
| AC-02(03)(d): disabled after inactivity | Other than satisfied | An account unused for 400 days still worked (T43, PA-13) |

P-AC-08 proposes 90 days of inactivity, but does not yet say how quickly each case must be disabled. **Tested:** T40 to T43.

#### AC.4.13 AC-2(2) Automated Temporary and Emergency Account Management

**Result: Not applicable.** Temporary and emergency accounts are not allowed until the system can expire them (P-AC-09, TR-AC-01). The system cannot expire any account (PA-13), so the Level 2 assessor should check that none exist.

**Table AC-25: AC-2(2) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02(02): temporary and emergency accounts are automatically removed or disabled after a set time | Not applicable | Not used until the system can expire them (TR-AC-01); no expiry exists (PA-13) |

#### AC.4.14 AC-2(13) Disable Accounts for High-risk Individuals

**Result: Other than satisfied.** The mechanism works: disabling ends API and web access immediately. The 1-hour limit and its triggers are approved (D-AC-03), but PRO-AC-4 has not yet been walked through or used.

**Table AC-26: AC-2(13) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02(13): accounts are disabled within a set time of discovering a significant risk | Other than satisfied | T40 and T41 pass; P-AC-13 sets 1 hour (D-AC-03); PRO-AC-4 is approved but not yet walked through (PA-20) |

T40 changed the database row and did not use the admin page. Windows and database accounts for the same person have no evidence yet (PA-30).

#### AC.4.15 AC-2(4) Automated Audit Actions

**Result: Other than satisfied.** Most account changes made in the admin portal have no audit call, and the API's records name "System" instead of the person.

**Table AC-27: AC-2(4) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02(04)\[01\]: creation is audited | Other than satisfied | No audit call in the portal (PA-14) |
| AC-02(04)\[02\]: modification is audited | Other than satisfied | Password changes and resets are; other changes are not (PA-14) |
| AC-02(04)\[03\]: enabling is audited | Other than satisfied | No audit call in the portal (PA-14) |
| AC-02(04)\[04\]: disabling is audited | Other than satisfied | The API logs against "System", and the portal has no audit call (PA-14) |
| AC-02(04)\[05\]: removal is audited | Other than satisfied | The API logs against "System", and the portal has no audit call (PA-14) |

**Tested:** T39 covers sign-in only. These results come from reading the code and were not confirmed by performing each action.

#### AC.4.16 AC-6(7) Review of User Privileges

**Result: Other than satisfied.** No review has happened. PRO-AC-7 and the review intervals are approved (D-AC-02, D-AC-03), and the Project Role Summary page shows assignments, but the system has no review record.

**Table AC-28: AC-6(7) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-06(07)(a): privileges are reviewed at a set frequency | Other than satisfied | P-AC-07 approved (D-AC-03); no review exists (PA-16) |
| AC-06(07)(b): privileges are reassigned or removed when needed | Other than satisfied | PRO-AC-7 is drafted and has not been used (PA-16) |

#### AC.4.17 AC-7 Unsuccessful Logon Attempts

**Result: Other than satisfied.** The application mechanism works as tested: five failures lock the account for 15 minutes, and it unlocks afterwards. The values are approved (D-AC-03). The result stays open because the password change path has no failure count (PA-35), and Windows and database logons cannot be assessed yet.

**Table AC-29: AC-7 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-07a: a limit of consecutive invalid attempts is enforced | Other than satisfied | Enforced at sign-in (T49) with the approved P-AC-14; the password change path has no count (PA-35) |
| AC-07b: the account is automatically locked when exceeded | Other than satisfied | Locks and unlocks in the application (T49, T50), with the same dependency |
| Windows and PostgreSQL logons on the VMs | Other than satisfied (E) | VMs not available (PA-30) |

#### AC.4.18 AC-8 System Use Notification

**Result: Other than satisfied.** No notice is shown on either sign-in page. The wording in P-AC-16 is approved by the system owner, subject to legal review (D-AC-06), but it is not built (PA-11).

**Table AC-30: AC-8 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-08a.01 to a.04: the notice states the required conditions | Other than satisfied | No notice (T51, T52, PA-11) |
| AC-08b: the notice stays until acknowledged | Other than satisfied | No notice or acknowledgement (PA-11) |
| AC-08c.01 to c.03: conditions for publicly accessible systems | Not applicable if P-AC-24 is approved | \<System Name\> is not intended to be public |
| Windows logon banner on the VMs | Other than satisfied (E) | Depends on \<Organisation\> (PA-30) |

AC-08a.01 is written for U.S. Government systems. The system owner needs to decide how it applies to \<Organisation\>, and record the decision alongside the wording.

#### AC.4.19 AC-2(5) Inactivity Logout

**Result: Other than satisfied.** The server ends a session idle for 30 minutes, as tested. The value is approved (D-AC-03), but the rule cannot yet be assessed for server administrators on the VMs.

**Table AC-31: AC-2(5) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-02(05): users are required to log out at the set time | Other than satisfied | Enforced in the application (T44) with the approved P-AC-10; VM administration not yet available |
| Windows and PostgreSQL administration sessions | Other than satisfied (E) | VMs not available (PA-30) |

#### AC.4.20 AC-12 Session Termination

**Result: Other than satisfied.** Sessions end after idling, at the 8-hour limit, on sign-out and when revoked. The values are approved (D-AC-03), but one unexplained test result needs resolving (PA-33), and the VMs are not available.

**Table AC-32: AC-12 objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-12: a session is automatically ended under set conditions | Other than satisfied | T38, T44 to T47 pass, including in the v1.0 run of 8 November 2026; P-AC-10 to P-AC-12 approved; T45's one failure on 5 November was not reproduced in five runs (PA-33); the VMs are not available |
| 8-hour limit reliability | Other than satisfied | T45 returned 200 in one full run. It then returned 401 in 15 repeats on its own and in later full runs. The cause was not found (PA-33) |
| Windows and PostgreSQL sessions | Other than satisfied (E) | VMs not available (PA-30) |

#### AC.4.21 AC-11 Device Lock

**Result: Other than satisfied.** A browser overlay appears after 25 minutes, but "Continue Session" removes it without a password, so it is not a true lock. The overlay runs in the browser, so it does not by itself stop a browser user reaching the page behind it.

**Table AC-33: AC-11 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-11a: further access is prevented by a lock | Other than satisfied | Browser overlay only (T53, code, PA-12) |
| AC-11b: the lock stays until the user signs in again | Other than satisfied | No password is asked for (code, PA-12) |
| Workstation and server locks | Other than satisfied (E) | Depends on \<Organisation\>'s builds (PA-21, PA-30) |

The lock was found by code review and has not been exercised in a browser.

#### AC.4.22 AC-11(1) Pattern-hiding Displays

**Result: Other than satisfied.** The code draws a dark overlay at 92% opacity, but this has not been seen on screen, so there is no evidence yet that it fully hides what was displayed. Workstation lock screens depend on \<Organisation\>.

**Table AC-34: AC-11(1) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-11(01): the lock conceals what was on screen | Other than satisfied | Code only, not seen in a browser (T53); workstations have no evidence yet (PA-21) |

#### AC.4.23 AC-4 Information Flow Enforcement

**Result: Other than satisfied.** The target flows are drawn, but nothing enforces them yet, and browsers also fetch code from an outside service that was not in the design.

**Table AC-35: AC-4 objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-04: approved authorisations control information flow within the system and to connected systems | Other than satisfied | See below |

**Table AC-36: AC-4 findings**

| Flow | Finding | Evidence |
| --- | --- | --- |
| Browser to cdn.jsdelivr.net | Every page, including the sign-in pages, loads scripts and styles from this outside service, with no integrity check. A change there would run in signed-in users' browsers | Code review (PA-34) |
| API port in Docker | The compose file publishes the web, admin and API ports on all network interfaces. The database port is limited to the local machine | Compose file (PA-18) |
| Cross-origin requests | The API allows only named origins, and they name localhost | Code review |
| Between the VMs, and to the network | Firewall rules do not exist yet | VMs not available (PA-18) |
| \<Organisation\>'s firewalls | Other than satisfied (E) | PA-18, PA-21 |
| Data leaving through export | Editors can export documents, and Folder output can write anywhere the service can reach | Code review (PA-26) |

#### AC.4.24 AC-17 Remote Access

**Result: Other than satisfied.** The remote access route is not named, and no restrictions are written down.

**Table AC-37: AC-17 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-17a\[01\] to a\[03\]: restrictions, requirements and guidance are documented | Other than satisfied | P-AC-20 only says \<Organisation\>'s service, name to be confirmed (PA-18) |
| AC-17b: remote access is authorised before connecting | Other than satisfied (E) | Depends on \<Organisation\> (PA-18) |

#### AC.4.25 AC-17(1) Monitoring and Control

**Result: Other than satisfied (E).**

**Table AC-38: AC-17(1) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-17(01)\[01\], \[02\]: remote access is monitored and controlled automatically | Other than satisfied (E) | Expected from \<Organisation\>, with no evidence yet (PA-18, PA-21) |

#### AC.4.26 AC-17(2) Protection of Confidentiality and Integrity Using Encryption

**Result: Other than satisfied.** The stack as run in Docker uses plain HTTP, and HTTPS and database TLS are not set up. The apps do include HTTPS redirection and HSTS settings, but these are not in effect in the tested configuration.

**Table AC-39: AC-17(2) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-17(02): encryption protects remote access sessions | Other than satisfied | T54 (PA-18); the remote route itself has no evidence yet |

#### AC.4.27 AC-17(3) Managed Access Control Points

**Result: Other than satisfied (E).**

**Table AC-40: AC-17(3) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-17(03): remote access goes through managed access points | Other than satisfied (E) | Expected from \<Organisation\>, with no evidence yet (PA-18, PA-21) |

#### AC.4.28 AC-17(4) Privileged Commands and Access

**Result: Not applicable.** Administrators may not work through external networks, and administer the VMs only from inside \<Organisation\>'s network (D-AC-08, TR-AC-05).

**Table AC-41: AC-17(4) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-17(04)(a)\[01\], \[02\]: remote privileged access leaves assessable evidence | Not applicable | Remote privileged access is not allowed (D-AC-08, TR-AC-05) |
| AC-17(04)(a)\[03\], \[04\]: it is allowed only for defined needs | Not applicable | Not allowed (D-AC-08, TR-AC-05) |
| AC-17(04)(b): the rationale is in the security plan | Not applicable | The rationale is in \<Tailoring Register\> (TR-AC-05) |

#### AC.4.29 AC-18 Wireless Access

**Result: Other than satisfied (E).** \<System Name\> provides no wireless access of its own.

**Table AC-42: AC-18 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-18a\[01\] to a\[03\], b: wireless requirements, guidance and authorisation | Other than satisfied (E) | Expected from \<Organisation\> (P-AC-21, PA-21) |

#### AC.4.30 AC-18(1) Authentication and Encryption

**Result: Other than satisfied (E).**

**Table AC-43: AC-18(1) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-18(01)\[01\], \[02\]: wireless access is authenticated and encrypted | Other than satisfied (E) | Expected from \<Organisation\> (PA-21) |

#### AC.4.31 AC-18(3) Disable Wireless Networking

**Result: Other than satisfied (E).** Server VMs normally have no wireless adapter, but this needs confirming on the built VMs.

**Table AC-44: AC-18(3) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-18(03): unused wireless is disabled before deployment | Other than satisfied (E) | VMs not available; \<Organisation\>'s builds (PA-21) |

#### AC.4.32 AC-19 Access Control for Mobile Devices

**Result: Not applicable.** Phones and tablets may not use \<System Name\> in the first release (D-AC-09, TR-AC-06). The system does not identify the device, so the rule depends on \<Organisation\>'s network access control.

**Table AC-45: AC-19 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-19a\[01\] to a\[03\], b: mobile device requirements and authorisation | Not applicable | Phones and tablets are not allowed (D-AC-09, TR-AC-06) |

#### AC.4.33 AC-19(5) Full Device or Container-based Encryption

**Result: Not applicable.** As AC-19 (TR-AC-06).

**Table AC-46: AC-19(5) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-19(05): mobile devices use full device or container encryption | Not applicable | As AC-19 (TR-AC-06) |

#### AC.4.34 AC-20 Use of External Systems

**Result: Other than satisfied (E).** The rule is approved: no external systems or portable storage without the system owner's approval (D-AC-10). Enforcement depends on \<Organisation\>, because the system cannot tell whether a browser is on an approved device.

**Table AC-47: AC-20 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-20a.01, a.02: external access and processing follow agreed terms | Satisfied | P-AC-22 approved: no use without the system owner's approval (D-AC-10) |
| AC-20b: prohibited external system types are prohibited | Other than satisfied (E) | Approved rule; enforcement depends on \<Organisation\> (PA-21) |

#### AC.4.35 AC-20(1) Limits on Authorized Use

**Result: Not applicable.** External use is forbidden, so there is nothing to verify or agree (TR-AC-07).

**Table AC-48: AC-20(1) objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-20(01)(a), (b): external use needs verified controls and a retained agreement | Not applicable | External use is forbidden (TR-AC-07) |

#### AC.4.36 AC-20(2) Portable Storage Devices

**Result: Other than satisfied (E).** Downloads and bulk export can reach any device the user has, so this depends on \<Organisation\>'s USB and device controls.

**Table AC-49: AC-20(2) objective**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-20(02): portable storage is restricted on external systems | Other than satisfied (E) | Expected from \<Organisation\> (PA-21) |

#### AC.4.37 AC-21 Information Sharing

**Result: Other than satisfied.** Nothing helps users judge whether sharing a document outside a project is allowed, and project groups control access only inside \<System Name\>.

**Table AC-50: AC-21 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-21a: users can decide whether a sharing partner's access matches restrictions | Other than satisfied | P-AC-23 approved (D-AC-03); documents have no sharing restrictions recorded (PA-22), risk accepted (NC-38) |
| AC-21b: mechanisms assist sharing decisions | Other than satisfied | None exist (PA-22) |

#### AC.4.38 AC-22 Publicly Accessible Content

**Result: Not applicable.** \<System Name\> holds no public content (D-AC-11, TR-AC-08).

**Table AC-51: AC-22 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-22a to d: public content is authorised, reviewed and corrected | Not applicable | No public content (D-AC-11, TR-AC-08). Documents need signing in (T02, T03); the anonymous cache and diagnostic endpoints are recorded under AC-14 (PA-22) |

#### AC.4.39 AC-1 Policy and Procedures

**Result: Other than satisfied.** The policy is approved by the Head of Cyber and the procedures by the system owner (D-AC-01, D-AC-02). They are not yet shared, and coordination with \<Organisation\> is not yet agreed. The policy was legally reviewed on 12 November 2026.

**Table AC-52: AC-1 objectives**

| Objective | Result | Basis |
| --- | --- | --- |
| AC-01a\[01\], a\[03\]: policy and procedures are developed and documented | Satisfied | \<Policy\> (AC) \<ver\> approved by the Head of Cyber (D-AC-16) and \<Procedures\> (AC) \<ver\> approved (D-AC-17); the later versions, \<ver\> and \<ver\>, make editorial changes only |
| AC-01a\[02\], a\[04\]: they are shared with defined people | Other than satisfied | Recipients defined in \<Access Control Management\>; not yet shared (PA-20) |
| AC-01a.01(a)\[01\] to \[05\], \[07\]: the policy addresses purpose, scope, roles, responsibilities, commitment and compliance | Satisfied | \<Policy\>, sections AC.1, AC.5 and AC.6, approved |
| AC-01a.01(a)\[06\]: the policy addresses coordination between organisations | Satisfied | Noted in \<Policy\>, section AC.6; not yet agreed with \<Organisation\> (PA-20) |
| AC-01a.01(b): the policy is consistent with laws, standards and guidance | Satisfied | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| AC-01b: an official manages policy and procedures | Satisfied | Neil is named as system owner, who manages both documents |
| AC-01c.01, c.02: both are reviewed at set times and after set events | Other than satisfied | Reviewed after set events: the AC pack review on 8 November 2026, approved. Reviews at set times are not yet due |

**Examined for this group:** code, compose file, draft policy, procedures, SSP and architecture. **Tested:** T02, T03, T54. **Interviewed:** nobody yet. \<Organisation\>'s evidence has not been requested.

### AC.5 Findings by determination statement

This section records one finding for each CSS determination statement, including those about organisation-defined parameters, in control order. It is current, and it takes precedence over the grouped objectives in section AC.4, which record what was examined and tested before the system owner's decisions of 5 November 2026. Statement wording is condensed, and the identifiers are CSS's. Findings are dated 5 November 2026 unless the basis or the change record says otherwise.

Findings: **S** satisfied. **O-D** other than satisfied, because a decision or approval is outstanding. **O-G** other than satisfied, because of a gap in the system. **O-E** other than satisfied, because evidence from the VMs or \<Organisation\> is not available. **N/S** the parameter applies only if selected, and is not selected. N/A not applicable, as decided in \<Tailoring Register\>.

**Table AC-53: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| AC-01\_ODP\[01\] | Who receives the policy is defined | S | D-AC-P01 |
| AC-01\_ODP\[02\] | Who receives the procedures is defined | S | D-AC-P01 |
| AC-01\_ODP\[03\] | Policy level is selected | S | D-AC-P01 |
| AC-01\_ODP\[04\] | Managing official is defined | S | P-AC-01; \[Name\] is the system owner |
| AC-01\_ODP\[05\] | Policy review frequency is defined | S | D-AC-P01 |
| AC-01\_ODP\[06\] | Policy review events are defined | S | D-AC-P01 |
| AC-01\_ODP\[07\] | Procedures review frequency is defined | S | D-AC-P01 |
| AC-01\_ODP\[08\] | Procedures review events are defined | S | D-AC-P01 |
| AC-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-AC-16) |
| AC-01a.\[02\] | Policy is disseminated | O-D | Not yet shared (D-AC-05) |
| AC-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved (D-AC-17) |
| AC-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared (D-AC-05) |
| AC-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section AC.1 |
| AC-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section AC.1 |
| AC-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section AC.5 |
| AC-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section AC.5 |
| AC-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section AC.6 |
| AC-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section AC.6. Not yet agreed with \<Organisation\> |
| AC-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section AC.6 |
| AC-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| AC-01b. | Official is designated | S | \[Name\] is the system owner |
| AC-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | Frequency approved; first review not yet due |
| AC-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 8 November 2026 after the AC pack review; version \<ver\> approved (D-AC-16) |
| AC-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | Frequency approved; first review not yet due |
| AC-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed on 8 November 2026 after the AC pack review; version \<ver\> approved (D-AC-17) |
| AC-02\_ODP\[01\] | Membership prerequisites are defined | S | D-AC-P02 |
| AC-02\_ODP\[02\] | Account attributes are defined | S | D-AC-P02. An expiry attribute is not built (PA-13) |
| AC-02\_ODP\[03\] | Account approvers are defined | S | D-AC-P02 |
| AC-02\_ODP\[04\] | Basis for account actions is defined | S | D-AC-P02 |
| AC-02\_ODP\[05\] | Others to be notified are defined | S | D-AC-P02 |
| AC-02\_ODP\[06\] | Notice period, account not required, is defined | S | D-AC-P02 |
| AC-02\_ODP\[07\] | Notice period, leaver or transfer, is defined | S | D-AC-P02 |
| AC-02\_ODP\[08\] | Notice period, change of need, is defined | S | D-AC-P02 |
| AC-02\_ODP\[09\] | Attributes authorising access are defined | S | D-AC-P02 |
| AC-02\_ODP\[10\] | Account review frequency is defined | S | D-AC-P02 |
| AC-02a.\[01\] | Allowed account types are documented | S | Approved (D-AC-03) |
| AC-02a.\[02\] | Prohibited account types are documented | S | Approved (D-AC-03) |
| AC-02b. | Account managers are assigned | S | \[Name\], global administrator |
| AC-02c. | Membership prerequisites are required | O-G | Not required by the system; manual process approved, not yet operated |
| AC-02d.01 | Authorised users are specified | O-D | Approved access list not yet built (D-AC-14) |
| AC-02d.02 | Group and role membership are specified | O-D | Approved access list not yet built (D-AC-14) |
| AC-02d.03\[01\] | Privileges are specified per account | O-D | Approved access list not yet built (D-AC-14) |
| AC-02d.03\[02\] | Attributes are specified per account | O-G | No expiry attribute (PA-13) |
| AC-02e. | Approval is required to create accounts | O-G | No step in \<System Name\>; ServiceNow approval workflow planned, not yet set up (PA-20) |
| AC-02f.\[01\] | Accounts are created under procedure | O-D | Function exists; PRO-AC-1 approved, not walked through |
| AC-02f.\[02\] | Accounts are enabled under procedure | O-D | Function exists; procedure approved, not walked through |
| AC-02f.\[03\] | Accounts are modified under procedure | O-D | Function exists; PRO-AC-2 approved, not walked through |
| AC-02f.\[04\] | Accounts are disabled under procedure | O-D | T40, T41 pass; PRO-AC-3, PRO-AC-4 approved, not walked through |
| AC-02f.\[05\] | Accounts are removed under procedure | O-D | T42 passes; PRO-AC-3 approved, not walked through |
| AC-02g. | Account use is monitored | O-G | Recorded (T39), but not monitored |
| AC-02h.01 | Notice when an account is not required | O-G | Starters/Leavers prompt planned, not yet set up (PA-32) |
| AC-02h.02 | Notice when a user leaves or transfers | O-G | Starters/Leavers prompt planned, not yet set up (PA-32) |
| AC-02h.03 | Notice when need changes | O-G | ServiceNow change request planned, not yet set up (PA-32) |
| AC-02i.01 | Access rests on a valid authorisation | O-D | Enforced (T11); approved access list not yet built |
| AC-02i.02 | Access rests on intended usage | O-D | Not recorded until TPL-2 is used |
| AC-02i.03 | Access rests on the set attributes | O-D | Attributes approved; approved access list not yet built |
| AC-02j. | Accounts are reviewed | O-G | No review exists (PA-16) |
| AC-02k.\[01\] | Shared authenticator process is established | S | Shared accounts are prohibited, so no process is needed (D-AC-03, TR-AC-02) |
| AC-02k.\[02\] | Shared authenticator process is implemented | O-D | Docker seeds a generic admin; a named first administrator on the VMs avoids it (PRO-AC-12, TR-AC-02) |
| AC-02l.\[01\] | Aligned with termination processes | O-E | \<Organisation\>'s processes not available (PA-32) |
| AC-02l.\[02\] | Aligned with transfer processes | O-E | \<Organisation\>'s processes not available (PA-32) |
| AC-02(01)\_ODP | Automated mechanisms are defined | S | D-AC-P03 |
| AC-02(01) | Accounts are managed with those mechanisms | O-G | Part automated; no directory link or reports |
| AC-02(02)\_ODP\[01\] | Remove or disable is selected | N/A | TR-AC-01 |
| AC-02(02)\_ODP\[02\] | Time period is defined | N/A | TR-AC-01 |
| AC-02(02) | Temporary accounts are automatically disabled | N/A | TR-AC-01 |
| AC-02(03)\_ODP\[01\] | Time to disable is defined | S | D-AC-P05 |
| AC-02(03)\_ODP\[02\] | Inactivity period is defined | S | D-AC-P05 |
| AC-02(03)(a) | Expired accounts are disabled | O-G | No expiry exists (PA-13) |
| AC-02(03)(b) | Accounts with no person are disabled | O-D | Manual; PRO-AC-3 approved, not walked through |
| AC-02(03)(c) | Accounts in violation are disabled | O-D | Manual; PRO-AC-4 approved, not walked through |
| AC-02(03)(d) | Inactive accounts are disabled | O-G | 400 days still worked (T43) |
| AC-02(04)\[01\] | Creation is audited | O-G | No audit call (PA-14) |
| AC-02(04)\[02\] | Modification is audited | O-G | Password changes only (PA-14) |
| AC-02(04)\[03\] | Enabling is audited | O-G | No audit call (PA-14) |
| AC-02(04)\[04\] | Disabling is audited | O-G | Against "System" (PA-14) |
| AC-02(04)\[05\] | Removal is audited | O-G | Against "System" (PA-14) |
| AC-02(05)\_ODP | Logout condition is defined | S | D-AC-P06 |
| AC-02(05) | Users are logged out at that condition | O-E | Application yes (T44); VM administration not available |
| AC-02(13)\_ODP\[01\] | Time to disable is defined | S | D-AC-P07 |
| AC-02(13)\_ODP\[02\] | Triggering risks are defined | S | D-AC-P07 |
| AC-02(13) | Accounts are disabled within the time | O-D | T40, T41 pass; PRO-AC-4 approved, not walked through |
| AC-03 | Approved authorisations are enforced | O-G | Project access yes; session functions and database no (PA-02, PA-10, PA-19) |
| AC-04\_ODP | Flow control policies are defined | S | D-AC-P08 |
| AC-04 | Flow authorisations are enforced | O-G | Not enforced; outside service loaded (PA-18, PA-34) |
| AC-05\_ODP | Duties to separate are defined | S | D-AC-P09 |
| AC-05a. | Duties are identified and documented | S | Approved (D-AC-03); holders named |
| AC-05b. | Authorisations support separation | O-G | Global administrator holds all rights (T75, PA-15) |
| AC-06 | Least privilege is employed | O-G | Readers and editors yes; database and open functions no (PA-10) |
| AC-06(01)\_ODP\[01\] | Authorised individuals and roles are defined | S | D-AC-P10; holders named |
| AC-06(01)\_ODP\[02\] | Hardware security functions are defined | S | Stated by \[Name\] (D-AC-P10) |
| AC-06(01)\_ODP\[03\] | Software security functions are defined | S | D-AC-P10 |
| AC-06(01)\_ODP\[04\] | Firmware security functions are defined | S | Stated by \[Name\] (D-AC-P10) |
| AC-06(01)\_ODP\[05\] | Security-relevant information is defined | S | D-AC-P10 |
| AC-06(01)(a)\[01\] | Access to hardware functions is authorised | O-E | VMs not available |
| AC-06(01)(a)\[02\] | Access to software functions is authorised | O-G | Main functions yes; others open (PA-02, PA-03, PA-06) |
| AC-06(01)(a)\[03\] | Access to firmware functions is authorised | O-E | VMs not available |
| AC-06(01)(b) | Access to security-relevant information is authorised | O-G | Secrets and user lists exposed (PA-07, PA-19) |
| AC-06(02)\_ODP | Functions needing separate accounts are defined | S | D-AC-P11 |
| AC-06(02) | Non-privileged accounts are used for other work | O-G | Not issued (PA-17); risk of no system enforcement accepted (NC-14) |
| AC-06(05)\_ODP | Privileged roles are defined | S | D-AC-P12; holders named |
| AC-06(05) | Privileged accounts are restricted | O-G | Database superuser (T55, PA-10) |
| AC-06(07)\_ODP\[01\] | Review frequency is defined | S | D-AC-P13 |
| AC-06(07)\_ODP\[02\] | Roles to review are defined | S | D-AC-P13 |
| AC-06(07)(a) | Privileges are reviewed | O-G | No review exists (PA-16) |
| AC-06(07)(b) | Privileges are reassigned or removed | O-G | PRO-AC-7 not used (PA-16) |
| AC-06(09) | Privileged functions are logged | O-G | Many not logged (PA-14, PA-29) |
| AC-06(10) | Non-privileged users are prevented | O-G | Several functions open (PA-02, PA-03, PA-06, PA-29) |
| AC-07\_ODP\[01\] | Number of attempts is defined | S | D-AC-P14 |
| AC-07\_ODP\[02\] | Time period is defined | S | D-AC-P14: no limit |
| AC-07\_ODP\[03\] | Action is selected | S | D-AC-P14 |
| AC-07\_ODP\[04\] | Lock period is defined | S | D-AC-P14 |
| AC-07\_ODP\[05\] | Delay algorithm is defined, if selected | N/S | Not selected |
| AC-07\_ODP\[06\] | Other action is defined, if selected | N/S | Not selected |
| AC-07a. | The limit is enforced | O-G | Sign-in yes (T49); password change path has no count (PA-35); VMs not available |
| AC-07b. | The action is automatic | O-E | Application yes (T49, T50); VMs not available |
| AC-08\_ODP\[01\] | Notice wording is defined | S | D-AC-P15; legal review to follow |
| AC-08\_ODP\[02\] | Conditions for public systems are defined | N/S | Not public (TR-AC-04) |
| AC-08a. | Notice is displayed before access | O-G | No notice (T51, T52, PA-11) |
| AC-08a.01 | States a U.S. Government system | N/A | TR-AC-03 |
| AC-08a.02 | States monitoring and audit | O-G | Wording approved; no notice built (PA-11) |
| AC-08a.03 | States prohibition and penalties | O-G | Wording approved; no notice built (PA-11) |
| AC-08a.04 | States consent to monitoring | O-G | Wording approved; no notice built (PA-11) |
| AC-08b. | Notice stays until acknowledged | O-G | No notice (PA-11) |
| AC-08c.01 | Public systems: conditions are displayed | N/A | TR-AC-04 |
| AC-08c.02 | Public systems: monitoring references | N/A | TR-AC-04 |
| AC-08c.03 | Public systems: authorised uses | N/A | TR-AC-04 |
| AC-11\_ODP\[01\] | How the lock starts is selected | S | D-AC-P16 |
| AC-11\_ODP\[02\] | Inactivity period is defined | S | D-AC-P16 |
| AC-11a. | Lock prevents further access | O-G | Browser overlay only (PA-12) |
| AC-11b. | Lock stays until re-authentication | O-G | No password is asked for (PA-12) |
| AC-11(01) | Lock conceals the display | O-E | Not observed on screen; workstations not available |
| AC-12\_ODP | Termination conditions are defined | S | D-AC-P17 |
| AC-12 | Sessions end automatically | O-E | Application yes (T38, T44 to T47), and T45's one failure on 5 November not reproduced in five runs on 8 November (PA-33); VMs not available |
| AC-14\_ODP | Actions without sign-in are defined | S | D-AC-P18 |
| AC-14a. | Actions are identified | O-G | Identified, but other endpoints are open (PA-03, PA-07) |
| AC-14b.\[01\] | Actions are in the security plan | S | Approved (D-AC-12) |
| AC-14b.\[02\] | A rationale is in the security plan | S | Approved (D-AC-12) |
| AC-17a.\[01\] | Usage restrictions are documented | O-D | None written (PA-18) |
| AC-17a.\[02\] | Connection requirements are documented | O-D | None written (PA-18) |
| AC-17a.\[03\] | Implementation guidance is documented | O-D | None written (PA-18) |
| AC-17b. | Remote access is authorised first | O-E | Depends on \<Organisation\> (PA-18) |
| AC-17(01)\[01\] | Remote access is monitored automatically | O-E | \<Organisation\>; no evidence (PA-21) |
| AC-17(01)\[02\] | Remote access is controlled automatically | O-E | \<Organisation\>; no evidence (PA-21) |
| AC-17(02) | Remote sessions are encrypted | O-G | Plain HTTP (T54, PA-18) |
| AC-17(03) | Routed through managed points | O-E | \<Organisation\>; no evidence (PA-21) |
| AC-17(04)\_ODP\[01\] | Needs for remote commands are defined | N/A | TR-AC-05 |
| AC-17(04)\_ODP\[02\] | Needs for remote security information are defined | N/A | TR-AC-05 |
| AC-17(04)(a)\[01\] | Remote commands leave assessable evidence | N/A | TR-AC-05 |
| AC-17(04)(a)\[02\] | Remote information access leaves evidence | N/A | TR-AC-05 |
| AC-17(04)(a)\[03\] | Remote commands only for defined needs | N/A | TR-AC-05 |
| AC-17(04)(a)\[04\] | Remote information only for defined needs | N/A | TR-AC-05 |
| AC-17(04)(b) | Rationale is in the security plan | N/A | TR-AC-05 |
| AC-18a.\[01\] | Wireless configuration requirements exist | O-E | \<Organisation\> (PA-21) |
| AC-18a.\[02\] | Wireless connection requirements exist | O-E | \<Organisation\> (PA-21) |
| AC-18a.\[03\] | Wireless guidance exists | O-E | \<Organisation\> (PA-21) |
| AC-18b. | Wireless is authorised first | O-E | \<Organisation\> (PA-21) |
| AC-18(01)\_ODP | Users, devices or both are selected | S | Users and devices (D-AC-P20) |
| AC-18(01)\[01\] | Wireless is authenticated | O-E | \<Organisation\> (PA-21) |
| AC-18(01)\[02\] | Wireless is encrypted | O-E | \<Organisation\> (PA-21) |
| AC-18(03) | Unused wireless is disabled | O-E | VMs not available (PA-21) |
| AC-19a.\[01\] | Mobile configuration requirements exist | N/A | TR-AC-06 |
| AC-19a.\[02\] | Mobile connection requirements exist | N/A | TR-AC-06 |
| AC-19a.\[03\] | Mobile guidance exists | N/A | TR-AC-06 |
| AC-19b. | Mobile connection is authorised | N/A | TR-AC-06 |
| AC-19(05)\_ODP\[01\] | Encryption type is selected | N/A | TR-AC-06 |
| AC-19(05)\_ODP\[02\] | Mobile devices are defined | N/A | TR-AC-06 |
| AC-19(05) | Mobile devices are encrypted | N/A | TR-AC-06 |
| AC-20\_ODP\[01\] | Terms or asserted controls are selected | S | D-AC-P22 |
| AC-20\_ODP\[02\] | Terms and conditions are defined | S | D-AC-P22 |
| AC-20\_ODP\[03\] | Asserted controls are defined, if selected | N/S | Not selected |
| AC-20\_ODP\[04\] | Prohibited external systems are defined | S | D-AC-P22 |
| AC-20a.01 | Terms cover access from external systems | S | Approved (D-AC-10) |
| AC-20a.02 | Terms cover processing on external systems | S | Approved (D-AC-10) |
| AC-20b. | Prohibited systems are prohibited | O-E | Enforcement depends on \<Organisation\> (PA-21) |
| AC-20(01)(a) | Controls are verified before external use | N/A | TR-AC-07 |
| AC-20(01)(b) | Agreements are retained | N/A | TR-AC-07 |
| AC-20(02)\_ODP | Portable storage restrictions are defined | S | D-AC-P23 |
| AC-20(02) | Portable storage is restricted | O-E | \<Organisation\> (PA-21) |
| AC-21\_ODP\[01\] | Sharing circumstances are defined | S | D-AC-P24 |
| AC-21\_ODP\[02\] | Assisting process is defined | S | D-AC-P24 |
| AC-21a. | Users can determine a match | O-G | No restrictions recorded on documents (PA-22); risk accepted (NC-38) |
| AC-21b. | Mechanisms assist decisions | S | Manual process PRO-AC-16 approved (D-AC-02) |
| AC-22\_ODP | Review frequency is defined | N/A | TR-AC-08 |
| AC-22a. | People are designated to publish | N/A | TR-AC-08 |
| AC-22b. | They are trained | N/A | TR-AC-08 |
| AC-22c. | Content is reviewed before posting | N/A | TR-AC-08 |
| AC-22d.\[01\] | Content is reviewed periodically | N/A | TR-AC-08 |
| AC-22d.\[02\] | Non-public information is removed | N/A | TR-AC-08 |

### AC.6 Assessment plan

This records how the assessment was planned and carried out, following CSS. It describes this initial self-assessment and what remains for an independent one.

**Table AC-54: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 39 AC entries in the CSS Moderate baseline, with 189 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Assessor | Level 1: Claude, an AI assistant, working for the system owner. Level 2: an independent team led by \[Name\], which meets CA-2(1) at Moderate once TPL-19 is completed |
| Dates | 5 November 2026; the 75 checks re-run on the tagged v1.0 build on 8 November 2026 with the same results |
| Site | One PC, using a separate throwaway Docker stack with sample data, and the running local stack for read-only checks. The Windows Server 2025 VMs are not built |
| Examine | Policies, procedures, the SSP, code in all repositories, configuration and test results. Depth: focused. Coverage: focused, on the functions each control concerns |
| Test | 75 repeatable checks, a browser check and an anonymous probe. Depth: focused. Coverage: focused. Every action on every page was not exercised |
| Interview | System owner's written answers to INT-AC-01 to 34 only. Account managers, administrators and \<Organisation\>'s security contact are to be interviewed. The people are named in \<Roles and Responsibilities\> |
| Previous results reused | None |
| Boundary | The whole stack: the application and database VMs, with Windows accounts, PostgreSQL roles and service accounts as well as application users. \<Organisation\>'s network, remote access, devices and directory are inherited, and Cyber Essentials Plus supports but does not prove them |
| Order of assessment | A, access enforcement (AC-3, AC-14, AC-6(10), AC-6(1)); B, privilege (AC-6, AC-6(5), AC-5, AC-6(2), AC-6(9)); C, account lifecycle (AC-2 and its enhancements, AC-6(7)); D, sign-in and sessions (AC-7, AC-8, AC-2(5), AC-12, AC-11, AC-11(1)); E, network and devices (AC-4, AC-17, AC-18 and AC-19 families); F, organisation (AC-20 family, AC-21, AC-22, AC-1). Access enforcement comes first because the other results depend on it |
| Needed from \<Organisation\> | Evidence for the inherited parts of AC-4, AC-17, AC-18, AC-19, AC-20 and AC-6(9), as requested in \<Evidence Requests\> |
| Approval | Approved by the authorising official (D-GEN-18), as confirmed by the system owner on 8 November 2026 |
| Evidence retained | \<Access Control Management\>, section A.9, and the AC evidence, with its manifest |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. For the Level 2 assessment, the assessor should repeat the tests on the VMs, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section AC.5.

## AT Awareness and Training

### AT.1 Purpose

This records the Level 1 self-assessment of the 6 AT entries in the CSS Moderate baseline, using catalog release 5.2.0. AT-3(5) is a privacy baseline control, assessed with the PT family (\<Control Assessment Record\> (PT)). An independent team led by \[Name\] will use this record for the Level 2 assessment. It makes no fixes.

### AT.2 How to read this record

The method was **Examine** (documents). This family has no code to test. No training has been given, no training records exist, and no interviews have been held. Check L14 of Test-PlanConsistency.ps1 confirms that every security role has its training defined (the PL evidence).

### AT.3 Executive summary

**Table AT-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, needing only a decision, approval or evidence | 6 | AT-1, AT-2, AT-2(2), AT-2(3), AT-3, AT-4 |

**Table AT-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| AT-1 | Other than satisfied | 21 of 25 | Not yet shared; Head of Cyber's re-approval (D-AT-07) outstanding; legally reviewed | NC-AT-01 |
| AT-2 | Other than satisfied | 7 of 17 | \<System Name\> briefing not yet given; \<Organisation\>'s course not seen | NC-AT-02 |
| AT-2(2) | Other than satisfied | 0 of 2 | As AT-2 | NC-AT-03 |
| AT-2(3) | Other than satisfied | 0 of 4 | As AT-2 | NC-AT-04 |
| AT-3 | Other than satisfied | 5 of 14 | Curriculum set; content not yet written or given | NC-AT-05 |
| AT-4 | Other than satisfied | 1 of 4 | No training yet | NC-AT-06 |

Of the CSS 66 statements, 34 are satisfied, 17 await a decision or approval, none shows a gap in the system and 15 await evidence from \<Organisation\>.

The programme is now fully defined: who needs what, the role curriculum, the briefing outline, one training matrix, the register and the measures. What remains is training actually being given, and \<Organisation\>'s evidence.

### AT.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 12 November 2026 unless the basis says otherwise.

**Table AT-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| AT-01\_ODP\[01\] | Who receives the policy is defined | S | \<Organisation\>'s corporate parameter values |
| AT-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Organisation\>'s corporate parameter values |
| AT-01\_ODP\[03\] | Policy level is selected | S | \<Organisation\>'s corporate parameter values |
| AT-01\_ODP\[04\] | Managing official is defined | S | System owner |
| AT-01\_ODP\[05\] | Policy review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-01\_ODP\[06\] | Policy review events are defined | S | \<Organisation\>'s corporate parameter values |
| AT-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-01\_ODP\[08\] | Procedures review events are defined | S | \<Organisation\>'s corporate parameter values |
| AT-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber, subject to legal review (D-AT-01); version \<ver\> awaits re-approval (D-AT-07) |
| AT-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| AT-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-AT-08) |
| AT-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| AT-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (AT) \<ver\>, section AT.1 |
| AT-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (AT) \<ver\>, section AT.1 |
| AT-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (AT) \<ver\>, section AT.5 |
| AT-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (AT) \<ver\>, section AT.5 |
| AT-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (AT) \<ver\>, section AT.6 |
| AT-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (AT) \<ver\>, section AT.6 |
| AT-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (AT) \<ver\>, section AT.6 |
| AT-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| AT-01b. | Official is designated | S | \[Name\] is the system owner |
| AT-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| AT-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 12 November 2026 after the AT pack review (D-AT-06) |
| AT-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| AT-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 12 November 2026 (D-AT-08) |
| AT-02\_ODP\[01\] | Security training frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-02\_ODP\[02\] | Privacy training frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-02\_ODP\[03\] | Security training events are defined | S | \<Organisation\>'s corporate parameter values |
| AT-02\_ODP\[04\] | Privacy training events are defined | S | \<Organisation\>'s corporate parameter values |
| AT-02\_ODP\[05\] | Awareness techniques are defined | S | \<Organisation\>'s corporate parameter values |
| AT-02\_ODP\[06\] | Content update frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-02\_ODP\[07\] | Content update events are defined | S | \<Organisation\>'s corporate parameter values |
| AT-02a.01\[01\] | New users get security training | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02a.01\[02\] | New users get privacy training | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02a.01\[03\] | Users get security training at the set frequency | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02a.01\[04\] | Users get privacy training at the set frequency | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02a.02\[01\] | Security training follows changes and events | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02a.02\[02\] | Privacy training follows changes and events | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02b. | Awareness techniques are used | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02c.\[01\] | Content is updated at the set frequency | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02c.\[02\] | Content is updated after set events | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02d. | Lessons from incidents are built in | O-D | PRO-AT-3 \<ver\> approved; not yet in use |
| AT-02(02)\[01\] | Training covers recognising insider threat | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3, B4), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02(02)\[02\] | Training covers reporting insider threat | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3, B4 and B5), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02(03)\[01\] | Training covers recognising social engineering | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3, B3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02(03)\[02\] | Training covers reporting social engineering | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3, B5), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02(03)\[03\] | Training covers recognising social mining | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3, B3), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-02(03)\[04\] | Training covers reporting social mining | O-E | \<System Name\> briefing outlined (\<Awareness and Training Management\>, section 3.3, B5), not yet given; \<Organisation\>'s course not seen (EV-AT-01) |
| AT-03\_ODP\[01\] | Roles for security training are defined | S | \<Organisation\>'s corporate parameter values |
| AT-03\_ODP\[02\] | Roles for privacy training are defined | S | \<Organisation\>'s corporate parameter values |
| AT-03\_ODP\[03\] | Training frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-03\_ODP\[04\] | Content update frequency is defined | S | \<Organisation\>'s corporate parameter values |
| AT-03\_ODP\[05\] | Content update events are defined | S | \<Organisation\>'s corporate parameter values |
| AT-03a.01\[01\] | Role security training comes before access | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03a.01\[02\] | Role privacy training comes before access | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03a.01\[03\] | Role security training repeats | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03a.01\[04\] | Role privacy training repeats | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03a.02\[01\] | Role security training follows system changes | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03a.02\[02\] | Role privacy training follows system changes | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03b.\[01\] | Content is updated at the set frequency | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03b.\[02\] | Content is updated after set events | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-03c. | Lessons from incidents are built in | O-D | Curriculum and matrix set (\<Awareness and Training Management\>, sections 3.4 and 3.5); module content not yet written or given |
| AT-04\_ODP | Retention is defined | S | \<Organisation\>'s corporate parameter values |
| AT-04a.\[01\] | Security training is documented and monitored | O-D | PRO-AT-4 and the training register approved; no training yet |
| AT-04a.\[02\] | Privacy training is documented and monitored | O-D | PRO-AT-4 and the training register approved; no training yet |
| AT-04b. | Records are kept | O-D | PRO-AT-4 and the training register approved; no training yet |

### AT.5 Assessment plan

**Table AT-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 6 AT entries in the Moderate baseline, with 66 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 12 November 2026 after the AT pack review |
| Examine | \<Policy\> (AT), \<Procedures\> (AT) and the awareness and training chapter of \<Control Implementation Register\> at \<ver\>, now in \<Awareness and Training Management\>; \<Security Operating Procedures\>; \<Procedures\> (AC); PRO-IR-3; PRO-CP-4; \<PII Processing Management\>. Depth: focused. Coverage: focused |
| Test | Not applicable to this family. Check L14 of Test-PlanConsistency.ps1 (the PL evidence) |
| Interview | None held. The system owner, the security officer, one person from each role in the matrix and a sample of users remain |
| Boundary | \<System Name\>'s own briefing, role training and records. \<Organisation\>'s general course and its administrators' training are provider evidence (EV-AT-01) |
| Order of assessment | A, the programme (AT-1, \<Awareness and Training Management\>, section 3.2); B, awareness (AT-2, AT-2(2), AT-2(3)); C, role training (AT-3); D, records (AT-4) |
| Needed from providers | EV-AT-01 in \<Evidence Requests\> |
| Evidence retained | TPL-9 and TPL-21 records; the training register in \<Awareness and Training Management\>, section 3.8; the monthly measures on TPL-8; the PL evidence |

For the Level 2 assessment, the assessor should:

- sample TPL-9 records against the register and the accounts that hold privileged roles;
- sit in on the briefing or a module, and review the end-of-module checks;
- examine EV-AT-01;
- hold the interviews, and re-determine every statement in section AT.4.

## AU Audit and Accountability

### AU.1 Purpose

This records the Level 1 self-assessment of the 16 AU entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes: each non-compliance is rated and decided in \<Risk List\>, and only those to be remediated go to \<Plan of Action and Milestones\>.

### AU.2 How to read this record

**Change since this assessment.** On 12 November 2026 the system owner stated that \<System Name\> signs in through \<Organisation\>'s AD FS and takes its groups from Active Directory (D-AC-23), that only the API reaches the database (D-AC-18), and that an audit record's session field holds a hash of the session ID (D-AU-11). This chapter assessed the v1.0 build. Its findings are a true record of that build and are not changed. Since then five items have been added for gaps the review of the design found: PA-101 to PA-105. The findings are to be made again when the tests are repeated on the AD FS build (PA-95).

The methods were **Examine** (code and configuration), **Test** (Test-AuditAndAuth.ps1, checks A01 to A38, results of 6 and 8 November 2026 in the AU and IA evidence) and read-only database checks. The system owner answered INT-AU-01 to 06 in writing, as proposed answers (\<Interview Guide\>). No records were seen, so these change no finding, and the role holders have not been interviewed.

**Limit of the current evidence:** \<System Name\> ran in Docker on one PC with sample data, in the build labelled v1.0. The Windows Server 2025 VMs, PostgreSQL on Windows and \<Organisation\>'s services have not been examined.

### AU.3 Executive summary

**Table AU-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 1 | AU-3(1) |
| Other than satisfied, with at least one system gap | 11 | AU-2, AU-3, AU-5, AU-6, AU-6(1), AU-6(3), AU-7, AU-7(1), AU-9, AU-9(4), AU-12 |
| Other than satisfied, needing only a decision, approval or evidence | 4 | AU-1, AU-4, AU-8, AU-11 |

**Table AU-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| AU-1 | Other than satisfied | 21 of 25 | Policy and procedures not yet shared; first reviews outstanding; legally reviewed | NC-AU-01; PA-20 |
| AU-2 | Other than satisfied | 7 of 10 | Most account, group and role changes and the PA-76 events not logged; coordination with \<Organisation\> not agreed | NC-AU-02, NC-AU-17; PA-14, PA-76 |
| AU-3 | Other than satisfied | 0 of 6 | Application records are complete except some named "System"; VMs not available | NC-AU-03; PA-14 |
| AU-3(1) | Satisfied | 2 of 2 | Session, browser, project and document recorded (A20, A21) | None |
| AU-4 | Other than satisfied | 1 of 2 | No storage planned, as the VMs are not built | NC-AU-04; PA-42 |
| AU-5 | Other than satisfied | 3 of 5 | Failures reach only the application log; nobody is alerted | NC-AU-05; PA-38 |
| AU-6 | Other than satisfied | 3 of 6 | Review defined but not started | NC-AU-06; PA-40 |
| AU-6(1) | Other than satisfied | 1 of 2 | No automated integration; central monitoring unconfirmed | NC-AU-07; PA-40 |
| AU-6(3) | Other than satisfied | 0 of 1 | Only the application table can be reviewed | NC-AU-08, accepted |
| AU-7 | Other than satisfied | 3 of 4 | No export or report | NC-AU-09; PA-41 |
| AU-7(1) | Other than satisfied | 1 of 3 | Four of six search fields, no sort choice | NC-AU-10; PA-41 |
| AU-8 | Other than satisfied | 1 of 3 | Applications use UTC; the VMs' time source is not evidenced | NC-AU-11; EV-AU-02 |
| AU-9 | Other than satisfied | 1 of 3 | The application account can change records; the chain has no key and is not checked; the application log repeats personal data | NC-AU-12, NC-AU-16; PA-36, PA-37, PA-73 to PA-75 |
| AU-9(4) | Other than satisfied | 1 of 2 | Global administrators can read records | NC-AU-13; PA-39 |
| AU-11 | Other than satisfied | 1 of 2 | No retention or archive in place; VMs not built | NC-AU-14; PA-42 |
| AU-12 | Other than satisfied | 2 of 5 | PostgreSQL logging off; Windows not assessed; events built into each release | NC-AU-15; PA-14, PA-43 |

Of the CSS 81 statements, 48 are satisfied, 8 await a decision or approval, 15 show a gap in the system and 10 await evidence from the VMs or \<Organisation\>.

The application records the right detail for most events, in UTC, with a chain hash on each record. The most serious gap is protection: the application's database account can change, delete or empty the audit table, and nothing checks the chain. The chain itself has no key, cannot show that the newest records were removed, and as stored cannot be recomputed (A36, A37). Every audit event is also repeated in the unprotected application log with the username, IP address and session ID (A38). Global administrators can also read the records, against the agreed value. Nobody is alerted when logging fails, and no review has started.

### AU.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Statement wording is condensed, and the identifiers are CSS's. Findings are dated 6 November 2026 unless the basis or the change record says otherwise. The notes for AU-06\_ODP\[02\], AU-09a and AU-09b were updated on 8 November 2026 from checks A36 to A38, and no finding code changed.

**Table AU-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| AU-01\_ODP\[01\] | Who receives the policy is defined | S | \<Audit and Accountability Management\> |
| AU-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Audit and Accountability Management\> |
| AU-01\_ODP\[03\] | Policy level is selected | S | \<Audit and Accountability Management\> |
| AU-01\_ODP\[04\] | Managing official is defined | S | System owner |
| AU-01\_ODP\[05\] | Policy review frequency is defined | S | \<Audit and Accountability Management\> |
| AU-01\_ODP\[06\] | Policy review events are defined | S | \<Audit and Accountability Management\> |
| AU-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Audit and Accountability Management\> |
| AU-01\_ODP\[08\] | Procedures review events are defined | S | \<Audit and Accountability Management\> |
| AU-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-AU-01); version \<ver\> approved (D-AU-08) |
| AU-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| AU-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved (D-AU-02); version \<ver\> approved (D-AU-09) |
| AU-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| AU-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section AU.1 |
| AU-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section AU.1 |
| AU-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section AU.5 |
| AU-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section AU.5 |
| AU-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section AU.6 |
| AU-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section AU.6. Not yet agreed with \<Organisation\> |
| AU-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section AU.6 |
| AU-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| AU-01b. | Official is designated | S | \[Name\] is the system owner |
| AU-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| AU-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 8 November 2026 after the AU pack review; version \<ver\> approved (D-AU-08) |
| AU-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| AU-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed on 8 November 2026 after the AU pack review; version \<ver\> approved (D-AU-09) |
| AU-02\_ODP\[01\] | Event types the system can log are defined | S | \<Audit and Accountability Management\> |
| AU-02\_ODP\[02\] | Event types to log are defined | S | \<Audit and Accountability Management\>, sections 3.2 and 3.3 |
| AU-02\_ODP\[03\] | How often they are logged is defined | S | Every occurrence |
| AU-02\_ODP\[04\] | Review of selected events is defined | S | Every 12 months |
| AU-02a. | Event types are identified | S | \<Audit and Accountability Management\>, Table 3 |
| AU-02b. | Logging is coordinated with other entities | O-D | Not yet agreed with \<Organisation\> (EV-AU-01) |
| AU-02c.\[01\] | Event types are specified for logging | S | \<Audit and Accountability Management\>, sections 3.2 and 3.3 |
| AU-02c.\[02\] | They are logged at the set frequency | O-G | Most account, group and role changes are not logged (PA-14), nor are reading the audit log, start-up and shut-down, or logging changes (PA-76) |
| AU-02d. | Rationale is provided | S | the audit chapter of \<Control Implementation Register\>, version \<ver\> approved (D-AU-03); version \<ver\> approved (D-AU-09) |
| AU-02e. | Selected events are reviewed | O-D | First review not yet due |
| AU-03a. | Records show the type of event | O-E | Application yes (A19); VMs not available |
| AU-03b. | Records show when | O-E | Application yes (A19); VMs not available |
| AU-03c. | Records show where | O-E | Application yes (A19); VMs not available |
| AU-03d. | Records show the source | O-E | Application yes (A19); VMs not available |
| AU-03e. | Records show the outcome | O-E | Application yes (A19); VMs not available |
| AU-03f. | Records show who was involved | O-G | Some API records name "System" (PA-14) |
| AU-03(01)\_ODP | Additional content is defined | S | \<Audit and Accountability Management\> |
| AU-03(01) | Records hold the additional content | S | A20, A21 |
| AU-04\_ODP | Retention requirement is defined | S | 24 months: 12 online and 12 archived |
| AU-04 | Storage capacity is allocated | O-E | VMs not built (PA-42) |
| AU-05\_ODP\[01\] | Who is alerted is defined | S | \<Audit and Accountability Management\> |
| AU-05\_ODP\[02\] | Time to alert is defined | S | Within 1 hour |
| AU-05\_ODP\[03\] | Additional actions are defined | S | \<Audit and Accountability Management\> |
| AU-05a. | They are alerted to a logging failure | O-G | Application log only (A31, A35, PA-38) |
| AU-05b. | The actions are taken | O-D | PRO-AU-3 approved, not walked through. System keeps running (A32) |
| AU-06\_ODP\[01\] | Review frequency is defined | S | Weekly |
| AU-06\_ODP\[02\] | Activity to look for is defined | S | \<Security Operating Procedures\>, section 4.2 |
| AU-06\_ODP\[03\] | Who receives findings is defined | S | \<Audit and Accountability Management\> |
| AU-06a. | Records are reviewed and analysed | O-G | No review has started (PA-40) |
| AU-06b. | Findings are reported | O-G | No review has started (PA-40) |
| AU-06c. | Review is adjusted when risk changes | O-D | PRO-AU-1 approved, not walked through |
| AU-06(01)\_ODP | Automated mechanisms are defined | S | \<Audit and Accountability Management\> |
| AU-06(01) | Processes are integrated using them | O-G | No integration exists; \<Organisation\>'s monitoring unconfirmed (PA-40) |
| AU-06(03) | Records are correlated across repositories | O-G | Only the application table is reviewable (PA-40) |
| AU-07a.\[01\] | Reduction and reporting capability is provided | S | Audit page filters and statistics |
| AU-07a.\[02\] | It meets on-demand and investigation needs | O-G | No export or report (PA-41) |
| AU-07b.\[01\] | It does not alter original content | S | Page reads only; code |
| AU-07b.\[02\] | It does not alter time ordering | S | Page reads only; code |
| AU-07(01)\_ODP | Fields to search and sort are defined | S | \<Audit and Accountability Management\> |
| AU-07(01)\[01\] | Search and sort are provided | O-G | Four of six fields, with no sort choice (PA-41) |
| AU-07(01)\[02\] | Search and sort are implemented | O-G | Four of six fields, with no sort choice (PA-41) |
| AU-08\_ODP | Granularity is defined | S | Nearest second, UTC; clocks within 1 second of UTC |
| AU-08a. | Internal clocks generate time stamps | O-E | Application yes (code); VMs and time source not available |
| AU-08b. | Time stamps meet the granularity in UTC | O-E | Application yes (A22); VMs not available |
| AU-09\_ODP | Who is alerted to tampering is defined | S | \<Audit and Accountability Management\> |
| AU-09a. | Audit information is protected | O-G | Database account can change, delete and empty it (A26 to A28, PA-36); the application log repeats usernames, IP addresses and session IDs without protection (A38, PA-75) |
| AU-09b. | They are alerted to tampering | O-G | Nothing runs the chain check or alerts (PA-37), and the unkeyed chain could not detect tampering or removal of the newest records even if it ran (A36, A37; PA-73, PA-74) |
| AU-09(04)\_ODP | Who manages audit logging is defined | S | \<Audit and Accountability Management\> |
| AU-09(04) | Access is limited to them | O-G | Global administrators can read records (A25, PA-39) |
| AU-11\_ODP | Retention period is defined | S | 12 months online, then 12 months archived; application logs 30 days |
| AU-11 | Records are retained for that period | O-E | Nothing removes records; storage and backup on the VMs not available (PA-42) |
| AU-12\_ODP\[01\] | Components are defined | S | \<Audit and Accountability Management\> |
| AU-12\_ODP\[02\] | Who selects events is defined | S | System owner |
| AU-12a. | Components generate records | O-E | Application yes (A15 to A18); Windows not available |
| AU-12b. | They can select events | O-G | Events are built into each release, so a change needs a release (PRO-AU-5) |
| AU-12c. | Records for the selected events are generated | O-G | Gaps in PA-14; PostgreSQL logging off (A30, PA-43) |

### AU.5 Assessment plan

**Table AU-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 16 AU entries in the CSS Moderate baseline, with 81 determination statements. AU-3(3), which limits personal data in records, is assessed with the PT family |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Assessor | Level 1: Claude, an AI assistant, working for the system owner. Level 2: an independent team led by \[Name\], which meets CA-2(1) at Moderate once TPL-19 is completed |
| Dates | 6 November 2026; evidence re-run on the tagged v1.0 build on 8 November 2026 |
| Site | One PC, using a separate throwaway Docker stack with sample data. The Windows Server 2025 VMs are not built |
| Examine | The audit service, the audit record format, the audit page, the database's grants and settings, and \<Policy\> (AU), \<Procedures\> (AU) and \<Audit and Accountability Management\>. Depth: focused. Coverage: focused, on the functions each control concerns |
| Test | Test-AuditAndAuth.ps1: checks A15 to A32 and A35 to A38 cover AU, and A01 to A14, A33 and A34 cover IA. Results of 6 November and of 8 November 2026 (au-ia-test-results-2026-11-08-v1.0.csv, with hashes in MANIFEST.md). Depth: focused. Coverage: focused. Windows and PostgreSQL logging on the VMs not tested |
| Interview | System owner's written answers to INT-AU-01 to 06 only. The auditor, security officer, Windows server and database administrators and \<Organisation\>'s security contact remain. The people are named in \<Roles and Responsibilities\> |
| Previous results reused | None |
| Boundary | Audit records in dbo.AuditLog, the application logs, and the PostgreSQL and Windows logs on both VMs. \<Organisation\>'s central monitoring and time service are inherited |
| Order of assessment | A, record generation and content (AU-12, AU-2, AU-3, AU-3(1)); B, protection (AU-9, AU-9(4)); C, failure, capacity and retention (AU-5, AU-4, AU-11); D, review and reporting (AU-6, AU-6(1), AU-6(3), AU-7, AU-7(1)); E, time (AU-8); F, policy (AU-1). Generation comes first because every other result depends on records existing |
| Needed from \<Organisation\> | EV-AU-01 to EV-AU-05 in \<Evidence Requests\>: central monitoring, the time source, storage and backup, the Windows audit policy, and AD FS and Active Directory audit records |
| Evidence retained | The AU and IA evidence, with its manifest; \<Audit and Accountability Management\>, section 4 |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. The independent assessor's team, schedule, and depth and coverage are added once agreed. For the Level 2 assessment, the assessor should repeat the tests on the VMs, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section AU.4.

## CA Assessment, Authorization, and Monitoring

### CA.1 Purpose

This records the Level 1 self-assessment of the 10 CA entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### CA.2 How to read this record

**Change since this assessment.** On 12 November 2026 the design moved to \<Assessment, Authorization, and Monitoring Management\>. The interface record gained the exchange with AD FS and the connection from the two user-facing apps to the API (D-AC-23, D-AC-18). The inherited controls now number 65. Four items were added for the gaps this chapter found: PA-106 to PA-109. The findings below are a true record of 6 and 8 November 2026 and are not changed.

The method was **Examine** (the assessment, plan and decision documents). No interviews have been held. This family assesses the assessment process itself, so a self-assessment has clear limits here.

### CA.3 Executive summary

**Table CA-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, needing only a decision, approval or evidence | 10 | CA-1, CA-2, CA-2(1), CA-3, CA-5, CA-6, CA-7, CA-7(1), CA-7(4), CA-9 |

**Table CA-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| CA-1 | Other than satisfied | 21 of 25 | Policy and procedures not yet shared; first scheduled reviews outstanding; legally reviewed | NC-CA-01; PA-20 |
| CA-2 | Other than satisfied | 11 of 13 | Level 2 not yet held | NC-CA-02 |
| CA-2(1) | Other than satisfied | 0 of 1 | Independence not yet confirmed on TPL-19 | NC-CA-03 |
| CA-3 | Other than satisfied | 9 of 11 | Connections planned; no agreement signed or reviewed | NC-CA-04; PA-63 |
| CA-5 | Other than satisfied | 2 of 3 | Monthly updates start at go-live | NC-CA-05 |
| CA-6 | Other than satisfied | 2 of 7 | Not authorised; inherited controls not yet accepted | NC-CA-06; EV-CA-01 |
| CA-7 | Other than satisfied | 11 of 18 | Monitoring starts at go-live | NC-CA-07 |
| CA-7(1) | Other than satisfied | 0 of 1 | Independent monitoring starts at go-live | NC-CA-08 |
| CA-7(4) | Other than satisfied | 1 of 4 | Risk monitoring starts at go-live | NC-CA-09 |
| CA-9 | Other than satisfied | 7 of 10 | Internal connection planned; not yet reviewed | NC-CA-10; PA-63 |

Of the CSS 93 statements, 64 are satisfied, 27 await a decision or approval, none shows a gap in the system and 2 await evidence from \<Organisation\>.

The assessments, plans, assessment report and plan of action exist, and all 19 assessment plans are approved. Level 2, authorisation and monitoring have not started, as \<System Name\> is not live.

### CA.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026 unless the basis or the change record says otherwise.

**Table CA-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| CA-01\_ODP\[01\] | Who receives the policy is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01\_ODP\[03\] | Policy level is selected | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01\_ODP\[04\] | Managing official is defined | S | System owner |
| CA-01\_ODP\[05\] | Policy review frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01\_ODP\[06\] | Policy review events are defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01\_ODP\[08\] | Procedures review events are defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber, as confirmed by the system owner (D-CA-06); legally reviewed on 12 November 2026 |
| CA-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| CA-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved (D-CA-06) |
| CA-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| CA-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section CA.1 |
| CA-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section CA.1 |
| CA-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section CA.5 |
| CA-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section CA.5 |
| CA-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section CA.6 |
| CA-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section CA.6 |
| CA-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section CA.6 |
| CA-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| CA-01b. | Official is designated | S | \[Name\] is the system owner |
| CA-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| CA-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 8 November 2026 after the CA pack review; version \<ver\> approved (D-CA-06) |
| CA-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| CA-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed on 8 November 2026 after the CA pack review; version \<ver\> approved (D-CA-06) |
| CA-02\_ODP\[01\] | Assessment frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-02\_ODP\[02\] | Who receives results is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-02a. | An assessor is selected | S | \[Name\]'s team |
| CA-02b.01 | The plan describes scope | S | Each family assessment's plan, section 5 (section 6 for AC) |
| CA-02b.02 | The plan describes procedures | S | Each family assessment's plan, section 5 (section 6 for AC) |
| CA-02b.03\[01\] | The plan describes the environment | S | Each family assessment, sections 2 and 5 (3 and 7 for AC) |
| CA-02b.03\[02\] | The plan describes the team | S | Each family assessment, sections 1 and 5 (2 and 7 for AC) |
| CA-02b.03\[03\] | The plan describes roles and responsibilities | S | Each family assessment, sections 1 and 5 (2 and 7 for AC) |
| CA-02c. | The authorising official approves the plan | S | All 19 assessment plans approved (D-GEN-18), as confirmed by the system owner on 8 November 2026 |
| CA-02d.\[01\] | Controls are assessed for effect, at the set frequency | O-D | Level 1 only; Level 2 not held |
| CA-02d.\[02\] | Controls are assessed for outcome, at the set frequency | O-D | Level 1 only; Level 2 not held |
| CA-02e. | A report is produced | S | \<Security Assessment Report\>, with the 19 family assessments |
| CA-02f. | Results are provided | S | \<Security Assessment Report\> issued to the system owner, authorising official and Head of Cyber on 8 November 2026 |
| CA-02(01) | Independent assessors are used | O-D | Level 2 not held; independence not yet confirmed |
| CA-03\_ODP\[01\] | How exchanges are managed is selected | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-03\_ODP\[02\] | Type of agreement is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-03\_ODP\[03\] | Review frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-03a. | Exchanges are approved and managed | O-D | Recorded; connections not yet built or approved |
| CA-03b.\[01\] | Interfaces are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-03b.\[02\] | Security needs are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-03b.\[03\] | Privacy needs are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-03b.\[04\] | Controls are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-03b.\[05\] | Responsibilities are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-03b.\[06\] | Impact level is documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-03c. | Agreements are reviewed | O-D | First review not yet due |
| CA-05\_ODP | Update frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-05a. | A plan of action and milestones exists | S | \<Plan of Action and Milestones\> |
| CA-05b. | The plan is updated at the set frequency | O-D | Monthly updates not started |
| CA-06\_ODP | Update frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-06a. | An authorising official is assigned | S | \[Name\] (D-GEN-02) |
| CA-06b. | An official for common controls is assigned | O-E | \<Organisation\> (EV-CA-01) |
| CA-06c.01 | Common controls are accepted before operation | O-D | Not yet decided |
| CA-06c.02 | The system is authorised before operation | O-D | \<System Name\> is not authorised |
| CA-06d. | Common controls are authorised for use | O-E | \<Organisation\> (EV-CA-01) |
| CA-06e. | Authorisations are updated | O-D | Not yet authorised |
| CA-07\_ODP\[01\] | Metrics are defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\_ODP\[02\] | Monitoring frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\_ODP\[03\] | Assessment frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\_ODP\[04\] | Who receives security status is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\_ODP\[05\] | Security reporting frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\_ODP\[06\] | Who receives privacy status is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\_ODP\[07\] | Privacy reporting frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-07\[01\] | A monitoring strategy is developed | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.8 (D-CA-03) |
| CA-07\[02\] | Monitoring is carried out | O-D | Not started |
| CA-07a. | Metrics are established | S | \<Assessment, Authorization, and Monitoring Management\> (D-CA-03) |
| CA-07b.\[01\] | Monitoring frequencies are established | S | \<Assessment, Authorization, and Monitoring Management\> (D-CA-03) |
| CA-07b.\[02\] | Assessment frequencies are established | S | \<Assessment, Authorization, and Monitoring Management\> (D-CA-03) |
| CA-07c. | Control assessments continue | O-D | Not started |
| CA-07d. | Metrics are monitored | O-D | Not started |
| CA-07e. | Information is correlated and analysed | O-D | Not started |
| CA-07f. | Response actions are taken | O-D | Not started |
| CA-07g.\[01\] | Security status is reported | O-D | Not started |
| CA-07g.\[02\] | Privacy status is reported | O-D | Not started |
| CA-07(01) | Independent assessors monitor controls | O-D | Not started |
| CA-07(04) | Risk monitoring is part of the monitoring strategy | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.8: the measures cover effectiveness, compliance and change |
| CA-07(04)(a) | Risk monitoring covers effectiveness | O-D | Not started |
| CA-07(04)(b) | Risk monitoring covers compliance | O-D | Not started |
| CA-07(04)(c) | Risk monitoring covers change | O-D | Not started |
| CA-09\_ODP\[01\] | Components are defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-09\_ODP\[02\] | When a connection ends is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-09\_ODP\[03\] | Review frequency is defined | S | \<Assessment, Authorization, and Monitoring Management\> |
| CA-09a. | Internal connections are authorised | O-D | Recorded; connection not yet built or approved |
| CA-09b.\[01\] | Interfaces are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-09b.\[02\] | Security needs are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-09b.\[03\] | Privacy needs are documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-09b.\[04\] | The information is documented | S | \<Assessment, Authorization, and Monitoring Management\>, section 3.7 (D-CA-03) |
| CA-09c. | Connections are ended when set | O-D | VMs not built |
| CA-09d. | Continued need is reviewed | O-D | First review not yet due |

### CA.5 Assessment plan

**Table CA-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 10 CA entries in the CSS Moderate baseline, with 93 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 8 November 2026 after the CA pack review and the approvals confirmed by the system owner |
| Site | Documents only: CA assesses the organisation's processes, not the running system |
| Examine | \<Policy\> (CA), \<Procedures\> (CA), \<Assessment, Authorization, and Monitoring Management\>, \<Security Assessment Report\>, \<Plan of Action and Milestones\>, \<Risk List\>, \<Decision Register\> and the 19 family assessments. Depth: focused. Coverage: every CA statement |
| Test | Not applicable to this family at Level 1 |
| Interview | None held. The system owner, authorising official, security officer and security assessor remain |
| Previous results reused | None |
| Boundary | The assessment, authorisation and monitoring processes for \<System Name\>, and the connections in \<Assessment, Authorization, and Monitoring Management\>, section 3.7 |
| Order of assessment | A, plan and assessment (CA-2, CA-2(1)); B, remediation (CA-5); C, authorisation and inherited controls (CA-6); D, connections (CA-3, CA-9); E, monitoring (CA-7, CA-7(1), CA-7(4)); F, policy (CA-1). Assessment comes first because every other CA result depends on it |
| Needed from \<Organisation\> | EV-CA-01 in \<Evidence Requests\>, for the inherited controls in \<Assessment, Authorization, and Monitoring Management\>, section 3.6; and the agreements in \<Assessment, Authorization, and Monitoring Management\>, section 3.7 |
| Evidence retained | The documents above, at the versions in their change records |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. The independent assessor's team, schedule, and depth and coverage are added once agreed. For the Level 2 assessment, the assessor should confirm their independence, examine the monitoring reports once started, hold the interviews and re-determine every statement in section CA.4.

## CM Configuration Management

### CM.1 Purpose

This records the Level 1 self-assessment of the 24 CM entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### CM.2 How to read this record

**Change since this assessment.** On 13 November 2026 the Configuration Management Plan was rebuilt as \<Configuration Management\> in the form of the other family documents, with each control set out part by part (D-CM-13). The system owner decided that the applications run as Windows services (D-PL-10), and removed accounts from the value for CM-12 (D-CM-14). Four items were added for gaps this chapter found: PA-110 to PA-113. The findings below are a true record of 6 and 8 November 2026 and are not changed.

The methods were **Examine** (code and configuration) and **Test** (checks B06 to B08 on 6 November 2026, and C01 to C11 by \Test-ConfigurationManagement.ps1 on the tagged v1.0 build on 8 November 2026, with hashes in MANIFEST.md, in the SC and CM evidence, on a throwaway stack). The system owner answered the interview questions at Level 1 (\<Interview Guide\>, Table 31). Those answers changed no finding, and the role holders have not been interviewed.

**Limit of the current evidence:** \<System Name\> ran in Docker on one PC with sample data, in the build tagged v1.0. The Windows Server 2025 VMs and \<Organisation\>'s services have not been examined.

### CM.3 Executive summary

**Table CM-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 2 | CM-2(7), CM-3(4) |
| Other than satisfied, with at least one system gap | 6 | CM-2, CM-3, CM-3(2), CM-7, CM-7(2), CM-7(5) |
| Other than satisfied, needing only a decision, approval or evidence | 16 | CM-1, CM-2(2), CM-2(3), CM-4, CM-4(2), CM-5, CM-6, CM-7(1), CM-8, CM-8(1), CM-8(3), CM-9, CM-10, CM-11, CM-12, CM-12(1) |

**Table CM-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| CM-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews outstanding; legally reviewed | NC-CM-01; PA-20 |
| CM-2 | Other than satisfied | 2 of 7 | Baseline documented but images not pinned; VMs not built | NC-CM-02, NC-CM-25; PA-54, PA-77 |
| CM-2(2) | Other than satisfied | 1 of 5 | Not yet in use on the VMs | NC-CM-03; PA-53, PA-77 |
| CM-2(3) | Other than satisfied | 1 of 2 | Only v1.0 exists | NC-CM-04 |
| CM-2(7) | Satisfied | 5 of 5 | No device is issued for travel | None |
| CM-3 | Other than satisfied | 6 of 15 | ServiceNow change workflow not set up | NC-CM-06; PA-53 |
| CM-3(2) | Other than satisfied | 0 of 3 | No release test gate | NC-CM-07; PA-53 |
| CM-3(4) | Satisfied | 5 of 5 | Security and privacy representatives named | None |
| CM-4 | Other than satisfied | 0 of 2 | Impact analysis defined; not yet in use | NC-CM-09; PA-53 |
| CM-4(2) | Other than satisfied | 0 of 6 | Verification defined; not yet in use | NC-CM-10; PA-53 |
| CM-5 | Other than satisfied | 2 of 6 | Physical restrictions with \<Organisation\>; VMs not built | NC-CM-11; EV-CM-01 |
| CM-6 | Other than satisfied | 3 of 9 | VMs not built; hosting not decided | NC-CM-12; PA-54, PA-80 |
| CM-7 | Other than satisfied | 6 of 12 | Diagnostic pages remain; unused packages | NC-CM-13, NC-CM-27; PA-07, PA-31, PA-79 |
| CM-7(1) | Other than satisfied | 6 of 12 | First review not yet held | NC-CM-14 |
| CM-7(2) | Other than satisfied | 2 of 3 | Not technically enforced; risk accepted | NC-CM-15; PA-55 |
| CM-7(5) | Other than satisfied | 2 of 5 | List not yet written; not enforced, risk accepted | NC-CM-16; PA-55 |
| CM-8 | Other than satisfied | 2 of 8 | Software listed; servers when built | NC-CM-17, NC-CM-26; PA-54, PA-78 |
| CM-8(1) | Other than satisfied | 0 of 3 | Updating at each change not yet in use | NC-CM-18; PA-78 |
| CM-8(3) | Other than satisfied | 6 of 12 | \<Organisation\>'s detection not evidenced | NC-CM-19; EV-CM-02 |
| CM-9 | Other than satisfied | 10 of 13 | Not yet in use; moves to the protected store later | NC-CM-20; D-GEN-15 |
| CM-10 | Other than satisfied | 0 of 3 | \<Organisation\>'s licences not evidenced | NC-CM-21; EV-CM-03 |
| CM-11 | Other than satisfied | 4 of 6 | VMs not built; first check not yet due | NC-CM-22 |
| CM-12 | Other than satisfied | 4 of 8 | Approved access list not yet built | NC-CM-23 |
| CM-12(1) | Other than satisfied | 2 of 3 | Tools not yet confirmed | NC-CM-24; EV-CM-02 |

Of the CSS 178 statements, 90 are satisfied, 41 await a decision or approval, 16 show a gap in the system and 31 await evidence from the VMs or \<Organisation\>.

Most of this family is a process that has not started, because \<System Name\> is not live. The gaps are that the ServiceNow change workflow is not set up, diagnostic and maintenance pages remain in production builds, and software is not technically restricted, by decision.

### CM.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026 unless the basis or the change record says otherwise.

**Table CM-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| CM-01\_ODP\[01\] | Who receives the policy is defined | S | \<Configuration Management\> |
| CM-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Configuration Management\> |
| CM-01\_ODP\[03\] | Policy level is selected | S | \<Configuration Management\> |
| CM-01\_ODP\[04\] | Managing official is defined | S | System owner |
| CM-01\_ODP\[05\] | Policy review frequency is defined | S | \<Configuration Management\> |
| CM-01\_ODP\[06\] | Policy review events are defined | S | \<Configuration Management\> |
| CM-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Configuration Management\> |
| CM-01\_ODP\[08\] | Procedures review events are defined | S | \<Configuration Management\> |
| CM-01a.\[01\] | Policy is developed and documented | S | Approved by the Head of Cyber, subject to legal review (D-CM-01); legally reviewed on 12 November 2026 |
| CM-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| CM-01a.\[03\] | Procedures are developed and documented | S | Approved (D-CM-02) |
| CM-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| CM-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section CM.1 |
| CM-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section CM.1 |
| CM-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section CM.5 |
| CM-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section CM.5 |
| CM-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section CM.6 |
| CM-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section CM.6 |
| CM-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section CM.6 |
| CM-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| CM-01b. | Official is designated | S | \[Name\] is the system owner |
| CM-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| CM-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 8 November 2026 after the CM pack review; version \<ver\> approved by the Head of Cyber on 8 November 2026 (D-CM-11) |
| CM-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| CM-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed on 8 November 2026 after the CM pack review; version \<ver\> approved (D-CM-12) |
| CM-02\_ODP\[01\] | Review frequency is defined | S | Every 12 months |
| CM-02\_ODP\[02\] | Circumstances are defined | S | Each release |
| CM-02a.\[01\] | A current baseline is documented | O-G | Documented in \<Configuration Management\>, section 3.4, but the images are not pinned, so it cannot be rebuilt exactly (C01, C02; PA-77); VMs not built |
| CM-02a.\[02\] | It is under configuration control | O-E | Git tags yes; VMs not built |
| CM-02b.01 | Reviewed at the set frequency | O-D | First review not yet due |
| CM-02b.02 | Reviewed in the set circumstances | O-D | PRO-CM-2 approved; not yet in use |
| CM-02b.03 | Reviewed when components change | O-D | PRO-CM-2 approved; not yet in use |
| CM-02(02)\_ODP | Mechanisms are defined | S | \<Configuration Management\> |
| CM-02(02)\[01\] | Currency is kept with them | O-D | Value agreed; not yet in use on the VMs |
| CM-02(02)\[02\] | Completeness is kept with them | O-D | Value agreed; not yet in use on the VMs |
| CM-02(02)\[03\] | Accuracy is kept with them | O-D | Value agreed; not yet in use on the VMs |
| CM-02(02)\[04\] | Availability is kept with them | O-D | Value agreed; not yet in use on the VMs |
| CM-02(03)\_ODP | Versions kept are defined | S | 3 |
| CM-02(03) | Previous versions are retained | O-D | PRO-CM-2 approved; only v1.0 exists |
| CM-02(07)\_ODP\[01\] | Systems are defined | S | \<Configuration Management\> |
| CM-02(07)\_ODP\[02\] | Configurations are defined | S | \<Configuration Management\> |
| CM-02(07)\_ODP\[03\] | Controls are defined | S | \<Configuration Management\> |
| CM-02(07)(a) | Travel devices are issued with those settings | S | Kept in scope; none is issued (D-CM-05) |
| CM-02(07)(b) | Controls are applied on return | S | Kept in scope; none is issued (D-CM-05) |
| CM-03\_ODP\[01\] | Retention is defined | S | 3 years |
| CM-03\_ODP\[02\] | Change control element is defined | S | \<Configuration Management\> |
| CM-03\_ODP\[03\] | How it convenes is selected | S | \<Configuration Management\> |
| CM-03\_ODP\[04\] | Frequency is defined | S | \<Configuration Management\> |
| CM-03\_ODP\[05\] | Conditions are defined | S | \<Configuration Management\> |
| CM-03a. | Change types are determined | S | \<Configuration Management\> (D-CM-03) |
| CM-03b.\[01\] | Changes are reviewed | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03b.\[02\] | Changes are approved or refused | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03c. | Decisions are documented | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03d. | Approved changes are implemented | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03e. | Records are retained | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03f.\[01\] | Change activities are monitored | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03f.\[02\] | Change activities are reviewed | O-G | ServiceNow workflow not set up (PA-53) |
| CM-03g.\[01\] | Activities are coordinated by the element | O-G | Not yet operating (PA-53) |
| CM-03g.\[02\] | The element convenes | O-G | Not yet operating (PA-53) |
| CM-03(02)\[01\] | Changes are tested first | O-G | Test scripts exist; no release gate (PA-53) |
| CM-03(02)\[02\] | Changes are validated first | O-G | No release gate (PA-53) |
| CM-03(02)\[03\] | Changes are documented first | O-G | No release gate (PA-53) |
| CM-03(04)\_ODP\[01\] | Security representative is defined | S | Security officer |
| CM-03(04)\_ODP\[02\] | Privacy representative is defined | S | \<Configuration Management\> |
| CM-03(04)\_ODP\[03\] | Element is defined | S | \<Configuration Management\> |
| CM-03(04)\[01\] | Security representative is a member | S | \<Configuration Management\> (D-CM-03) |
| CM-03(04)\[02\] | Privacy representative is a member | S | \<Configuration Management\> (D-CM-03) |
| CM-04\[01\] | Security impact is analysed | O-D | PRO-CM-1 approved; not yet in use |
| CM-04\[02\] | Privacy impact is analysed | O-D | PRO-CM-1 approved; not yet in use |
| CM-04(02)\[01\] | Controls are correct for security | O-D | PRO-CM-1 approved; not yet in use |
| CM-04(02)\[02\] | Controls are correct for privacy | O-D | PRO-CM-1 approved; not yet in use |
| CM-04(02)\[03\] | Controls operate for security | O-D | PRO-CM-1 approved; not yet in use |
| CM-04(02)\[04\] | Controls operate for privacy | O-D | PRO-CM-1 approved; not yet in use |
| CM-04(02)\[05\] | Controls meet the outcome for security | O-D | PRO-CM-1 approved; not yet in use |
| CM-04(02)\[06\] | Controls meet the outcome for privacy | O-D | PRO-CM-1 approved; not yet in use |
| CM-05\[01\] | Physical restrictions are defined | O-E | \<Organisation\> (EV-CM-01) |
| CM-05\[02\] | Physical restrictions are documented | O-E | \<Organisation\> (EV-CM-01) |
| CM-05\[03\] | Physical restrictions are enforced | O-E | \<Organisation\> (EV-CM-01) |
| CM-05\[04\] | Logical restrictions are defined | S | \<Configuration Management\> (D-CM-03) |
| CM-05\[05\] | Logical restrictions are documented | S | \<Configuration Management\> (D-CM-03) |
| CM-05\[06\] | Logical restrictions are enforced | O-E | VMs not built |
| CM-06\_ODP\[01\] | Secure configurations are defined | S | CIS Benchmarks |
| CM-06\_ODP\[02\] | Components are defined | S | \<Configuration Management\> |
| CM-06\_ODP\[03\] | Operational requirements are defined | S | \<Configuration Management\> |
| CM-06a. | Settings are documented | O-E | VMs not built (PA-54) |
| CM-06b. | Settings are implemented | O-E | VMs not built (PA-54) |
| CM-06c.\[01\] | Deviations are identified | O-E | VMs not built (PA-54) |
| CM-06c.\[02\] | Deviations are approved | O-E | VMs not built (PA-54) |
| CM-06d.\[01\] | Changes to settings are monitored | O-E | VMs not built (PA-54) |
| CM-06d.\[02\] | Changes to settings are controlled | O-E | VMs not built (PA-54) |
| CM-07\_ODP\[01\] | Capabilities are defined | S | \<Configuration Management\> |
| CM-07\_ODP\[02\] | Functions are defined | S | \<Configuration Management\> |
| CM-07\_ODP\[03\] | Ports are defined | S | \<Configuration Management\> |
| CM-07\_ODP\[04\] | Protocols are defined | S | \<Configuration Management\> |
| CM-07\_ODP\[05\] | Software is defined | S | \<Configuration Management\> |
| CM-07\_ODP\[06\] | Services are defined | S | \<Configuration Management\> |
| CM-07a. | Only essential capabilities are provided | O-G | Diagnostic and maintenance pages remain (PA-07, PA-31) |
| CM-07b.\[01\] | Functions are restricted | O-E | Application part in CM-07a; VMs not built |
| CM-07b.\[02\] | Ports are restricted | O-E | Database local in Docker (B07); VMs not built |
| CM-07b.\[03\] | Protocols are restricted | O-E | VMs not built |
| CM-07b.\[04\] | Software is restricted | O-E | VMs not built |
| CM-07b.\[05\] | Services are restricted | O-E | VMs not built |
| CM-07(01)\_ODP\[01\] | Review frequency is defined | S | Every 12 months |
| CM-07(01)\_ODP\[02\] | Functions are defined | S | \<Configuration Management\> |
| CM-07(01)\_ODP\[03\] | Ports are defined | S | \<Configuration Management\> |
| CM-07(01)\_ODP\[04\] | Protocols are defined | S | \<Configuration Management\> |
| CM-07(01)\_ODP\[05\] | Software is defined | S | \<Configuration Management\> |
| CM-07(01)\_ODP\[06\] | Services are defined | S | \<Configuration Management\> |
| CM-07(01)(a) | The system is reviewed | O-D | PRO-CM-5 approved; first review not yet held |
| CM-07(01)(b)\[01\] | Unneeded functions are removed | O-D | PRO-CM-5 approved; first review not yet held |
| CM-07(01)(b)\[02\] | Unneeded ports are removed | O-D | PRO-CM-5 approved; first review not yet held |
| CM-07(01)(b)\[03\] | Unneeded protocols are removed | O-D | PRO-CM-5 approved; first review not yet held |
| CM-07(01)(b)\[04\] | Unneeded software is removed | O-D | PRO-CM-5 approved; first review not yet held |
| CM-07(01)(b)\[05\] | Unneeded services are removed | O-D | PRO-CM-5 approved; first review not yet held |
| CM-07(02)\_ODP\[01\] | Prevention rule is selected | S | \<Configuration Management\> |
| CM-07(02)\_ODP\[02\] | Rules are defined | S | The approved list |
| CM-07(02) | Program execution is prevented | O-G | Not enforced, by decision of 6 November 2026; risk with the authorising official (PA-55) |
| CM-07(05)\_ODP\[01\] | Authorised software is defined | S | The approved list |
| CM-07(05)\_ODP\[02\] | Review frequency is defined | S | Every 12 months |
| CM-07(05)(a) | Authorised software is identified | O-D | List not yet written (PA-55) |
| CM-07(05)(b) | Deny-all, permit-by-exception applies | O-G | Not enforced, by decision (PA-55) |
| CM-07(05)(c) | The list is reviewed | O-D | List not yet written (PA-55) |
| CM-08\_ODP\[01\] | Inventory information is defined | S | \<Configuration Management\> |
| CM-08\_ODP\[02\] | Review frequency is defined | S | At each change |
| CM-08a.01 | Inventory reflects the system | O-E | Software components listed in \<Configuration Management\>, section 3.5 (C04); servers when the VMs are built (PA-54) |
| CM-08a.02 | It includes all components | O-E | VMs not built (PA-54) |
| CM-08a.03 | It has no duplicates | O-E | VMs not built (PA-54) |
| CM-08a.04 | It has the right granularity | O-E | VMs not built (PA-54) |
| CM-08a.05 | It holds the defined information | O-E | VMs not built (PA-54) |
| CM-08b. | It is reviewed | O-D | PRO-CM-1 approved; not yet in use |
| CM-08(01)\[01\] | Updated at installation | O-D | PRO-CM-1 approved; not yet in use |
| CM-08(01)\[02\] | Updated at removal | O-D | PRO-CM-1 approved; not yet in use |
| CM-08(01)\[03\] | Updated at system updates | O-D | PRO-CM-1 approved; not yet in use |
| CM-08(03)\_ODP\[01\] | Hardware mechanism is defined | S | \<Organisation\>'s tools |
| CM-08(03)\_ODP\[02\] | Software mechanism is defined | S | \<Organisation\>'s tools |
| CM-08(03)\_ODP\[03\] | Firmware mechanism is defined | S | \<Organisation\>'s tools |
| CM-08(03)\_ODP\[04\] | Frequency is defined | S | Monthly |
| CM-08(03)\_ODP\[05\] | Action is selected | S | \<Configuration Management\> |
| CM-08(03)\_ODP\[06\] | Who is told is defined | S | Windows server administrator |
| CM-08(03)(a)\[01\] | Unauthorised hardware is detected | O-E | \<Organisation\> (EV-CM-02) |
| CM-08(03)(a)\[02\] | Unauthorised software is detected | O-E | \<Organisation\> (EV-CM-02) |
| CM-08(03)(a)\[03\] | Unauthorised firmware is detected | O-E | \<Organisation\> (EV-CM-02) |
| CM-08(03)(b)\[01\] | Action is taken on hardware | O-E | \<Organisation\> (EV-CM-02) |
| CM-08(03)(b)\[02\] | Action is taken on software | O-E | \<Organisation\> (EV-CM-02) |
| CM-08(03)(b)\[03\] | Action is taken on firmware | O-E | \<Organisation\> (EV-CM-02) |
| CM-09\_ODP | Who approves the plan is defined | S | System owner |
| CM-09\[01\] | A plan is developed and documented | S | \<Configuration Management\> (D-CM-03) |
| CM-09\[02\] | The plan is implemented | O-D | Not yet in use |
| CM-09a.\[01\] | It addresses roles | S | \<Configuration Management\>, section 3.2 |
| CM-09a.\[02\] | It addresses responsibilities | S | \<Configuration Management\>, section 3.2 |
| CM-09a.\[03\] | It addresses processes | S | \<Configuration Management\>, section 3.2 |
| CM-09b.\[01\] | It identifies configuration items | S | \<Configuration Management\>, section 3.2 |
| CM-09b.\[02\] | It manages them through the life cycle | S | \<Configuration Management\>, section 3.2 |
| CM-09c.\[01\] | It defines the items | S | \<Configuration Management\>, section 3.3 |
| CM-09c.\[02\] | It places them under control | S | \<Configuration Management\>, section 3.3 |
| CM-09d. | It is reviewed and approved | S | Approved (D-CM-03) |
| CM-09e.\[01\] | It is protected from disclosure | O-D | Moves to SharePoint when all families are done (D-GEN-15) |
| CM-09e.\[02\] | It is protected from modification | O-D | Moves to SharePoint when all families are done (D-GEN-15) |
| CM-10a. | Software follows contracts and copyright | O-E | \<System Name\>'s components reviewed (\<Configuration Management\>, section 3.5), with ImageSharp under its community licence (D-CM-09); \<Organisation\>'s licences not evidenced (EV-CM-03) |
| CM-10b. | Quantity licences are tracked | O-E | \<Organisation\> (EV-CM-03) |
| CM-10c. | Peer-to-peer use is controlled | O-E | \<Organisation\> (EV-CM-03) |
| CM-11\_ODP\[01\] | Installation policy is defined | S | \<Configuration Management\> |
| CM-11\_ODP\[02\] | Enforcement is defined | S | \<Configuration Management\> |
| CM-11\_ODP\[03\] | Monitoring frequency is defined | S | \<Configuration Management\> |
| CM-11a. | Policies are established | S | PRO-CM-4, approved (D-CM-02) |
| CM-11b. | They are enforced | O-E | VMs not built |
| CM-11c. | Compliance is monitored | O-D | Value agreed; first check not yet due |
| CM-12\_ODP | Information is defined | S | \<Configuration Management\> |
| CM-12a.\[01\] | Location is documented | S | \<System Security Plan\>, sections 3.3 and 3.4 |
| CM-12a.\[02\] | Processing components are documented | S | \<System Security Plan\>, section 3.4 |
| CM-12a.\[03\] | Storage components are documented | S | \<System Security Plan\>, section 3.4 |
| CM-12b.\[01\] | Users with access are identified | O-D | Approved access list not yet built (D-AC-14) |
| CM-12b.\[02\] | Users with access are documented | O-D | Approved access list not yet built (D-AC-14) |
| CM-12c.\[01\] | Location changes are documented | O-D | PRO-CM-1 approved; not yet in use |
| CM-12c.\[02\] | Component changes are documented | O-D | PRO-CM-1 approved; not yet in use |
| CM-12(01)\_ODP\[01\] | Information is defined | S | \<Configuration Management\> |
| CM-12(01)\_ODP\[02\] | Components are defined | S | \<Configuration Management\> |
| CM-12(01) | Automated tools identify the information | O-D | Value agreed; tools to be confirmed (EV-CM-02) |

### CM.5 Assessment plan

**Table CM-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 24 CM entries in the CSS Moderate baseline, with 178 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 8 November 2026 after the CM pack review |
| Site | One PC, using a separate throwaway Docker stack with sample data. The VMs are not built |
| Examine | The image build file, compose file, project files, settings files, the start-up configuration and the repositories at tag v1.0; \<Policy\> (CM), \<Procedures\> (CM) and \<Configuration Management\>. Depth: focused. Coverage: focused |
| Test | B06 to B08 by hand on 6 November 2026; C01 to C11 by Test-ConfigurationManagement.ps1 on 8 November 2026 (cm-test-results-2026-11-08-v1.0.csv, with the component inventory and MANIFEST.md). Depth: focused. Coverage: focused. The VMs, CIS settings and drift were not tested |
| Interview | System owner's written answers only. Developers, the Windows server and database administrators, and \<Organisation\>'s security contact remain |
| Previous results reused | None |
| Boundary | The code, images, components and settings of \<System Name\> v1.0, and the Windows Server and PostgreSQL configuration of both VMs. \<Organisation\>'s discovery tools and licences are inherited |
| Order of assessment | A, baseline and inventory (CM-2, CM-8, CM-10); B, change control (CM-3, CM-4, CM-5); C, secure settings and least functionality (CM-6, CM-7 and enhancements, CM-11); D, the plan and information location (CM-9, CM-12); E, policy (CM-1). The baseline comes first because every other result is judged against it |
| Needed from \<Organisation\> | EV-CM-01 to EV-CM-03 in \<Evidence Requests\>: physical change restrictions, discovery tools, and licences |
| Evidence retained | The SC and CM evidence, with its manifest; \<Configuration Management\>, sections 3.4 to 3.6 |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. The independent assessor's team, schedule, and depth and coverage are added once agreed. For the Level 2 assessment, the assessor should repeat the checks on the VMs, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section CM.4.

## CP Contingency Planning

### CP.1 Purpose

This records the Level 1 self-assessment of the 23 CP entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### CP.2 How to read this record

**Change since this assessment.** On 15 November 2026 the Contingency Plan was rebuilt as \<Contingency Planning Management\> in the form of the other family documents, with the plan as its section 3 and each control set out part by part (D-CP-14). AD FS was added to what recovery depends on (D-AC-23). Two items were added for gaps this chapter found: PA-114 and PA-115. The findings below are a true record of 6 and 9 November 2026 and are not changed.

The methods were **Examine** (documents and the Docker configuration) and **Test** (R01 to R09 by Test-BackupRestore.ps1 on the tagged v1.0 build on 9 November 2026, with hashes in MANIFEST.md, in the CP evidence, on a throwaway stack). The system owner answered the interview questions at Level 1 (\<Interview Guide\>).

**Limit of the current evidence:** the restore test proves the procedure in Docker with sample data. There are no backups of the VMs, and the second site and \<Organisation\>'s services have not been examined.

### CP.3 Executive summary

**Table CP-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 2 | CP-2(3), CP-2(8) |
| Other than satisfied, with at least one system gap | 5 | CP-9, CP-9(1), CP-9(8), CP-10, CP-10(2) |
| Other than satisfied, needing only a decision, approval or evidence | 16 | CP-1, CP-2, CP-2(1), CP-3, CP-4, CP-4(1), CP-6, CP-6(1), CP-6(3), CP-7, CP-7(1), CP-7(2), CP-7(3), CP-8, CP-8(1), CP-8(2) |

**Table CP-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| CP-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews not yet due | NC-CP-01; PA-20 |
| CP-2 | Other than satisfied | 19 of 31 | Version \<ver\> approved; not yet shared, tested or protected in the library | NC-CP-02; D-GEN-15 |
| CP-2(1) | Other than satisfied | 0 of 1 | Related plans named; coordination not yet shown in use | NC-CP-03 |
| CP-2(3) | Satisfied | 3 of 3 | Resumption within 72 hours planned, within a 120-hour maximum | None |
| CP-2(8) | Satisfied | 2 of 2 | Essential assets listed and corrected | None |
| CP-3 | Other than satisfied | 4 of 9 | Training content outlined; no training yet | NC-CP-06, NC-CP-24; PA-81 |
| CP-4 | Other than satisfied | 3 of 8 | No test of the plan on the VMs yet | NC-CP-07, NC-CP-24; PA-81 |
| CP-4(1) | Other than satisfied | 0 of 1 | No tabletop with the incident response plan yet | NC-CP-08, NC-CP-24; PA-81 |
| CP-6 | Other than satisfied | 0 of 3 | Second site unconfirmed | NC-CP-09; PA-66, EV-CP-01 |
| CP-6(1) | Other than satisfied | 0 of 1 | Separation unconfirmed | NC-CP-10; PA-66, EV-CP-01 |
| CP-6(3) | Other than satisfied | 0 of 2 | Accessibility unconfirmed | NC-CP-11; PA-66, EV-CP-01 |
| CP-7 | Other than satisfied | 2 of 6 | Second site unconfirmed | NC-CP-12; PA-66, EV-CP-01 |
| CP-7(1) | Other than satisfied | 0 of 1 | Separation unconfirmed | NC-CP-13; PA-66, EV-CP-01 |
| CP-7(2) | Other than satisfied | 0 of 2 | Accessibility unconfirmed | NC-CP-14; PA-66, EV-CP-01 |
| CP-7(3) | Other than satisfied | 0 of 1 | Priority of service unconfirmed | NC-CP-15; PA-66, EV-CP-01 |
| CP-8 | Other than satisfied | 2 of 3 | Alternate telecommunications unconfirmed | NC-CP-16; EV-CP-02 |
| CP-8(1) | Other than satisfied | 0 of 3 | Priority of service unconfirmed | NC-CP-17; EV-CP-02 |
| CP-8(2) | Other than satisfied | 0 of 1 | Single points of failure unconfirmed | NC-CP-18; EV-CP-02 |
| CP-9 | Other than satisfied | 4 of 10 | No backups; the restore procedure works in Docker | NC-CP-19; PA-64 |
| CP-9(1) | Other than satisfied | 2 of 4 | Tested in Docker (R03 to R07); no backups on the VMs | NC-CP-20; PA-64 |
| CP-9(8) | Other than satisfied | 1 of 2 | The default backup is unencrypted (R02) | NC-CP-21; PA-64 |
| CP-10 | Other than satisfied | 2 of 4 | No backups, so no recovery today; restore shown in Docker in 4.5 seconds | NC-CP-22; PA-64 |
| CP-10(2) | Other than satisfied | 0 of 1 | Transaction logs are not archived (R09) | NC-CP-23; PA-64 |

Of the CSS 124 statements, 65 are satisfied, 28 await a decision or approval, 12 show a gap in the system and 19 await evidence from the VMs or \<Organisation\>.

The plan now follows CSS, with a business impact analysis and its three phases, but it has not been tested on the VMs. The restore test shows the procedure works: a backup restored to a fresh server in 4.5 seconds with every row, document checksum and audit hash intact. The gaps are that \<System Name\> has no backups, the default backup is unencrypted and transaction logs are not archived, so nothing could be recovered today. The second site is unconfirmed.

### CP.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, and were updated on 9 November 2026 after the CP pack review.

**Table CP-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| CP-01\_ODP\[01\] | Who receives the policy is defined | S | \<Contingency Planning Management\> |
| CP-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Contingency Planning Management\> |
| CP-01\_ODP\[03\] | Policy level is selected | S | \<Contingency Planning Management\> |
| CP-01\_ODP\[04\] | Managing official is defined | S | System owner |
| CP-01\_ODP\[05\] | Policy review frequency is defined | S | \<Contingency Planning Management\> |
| CP-01\_ODP\[06\] | Policy review events are defined | S | \<Contingency Planning Management\> |
| CP-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Contingency Planning Management\> |
| CP-01\_ODP\[08\] | Procedures review events are defined | S | \<Contingency Planning Management\> |
| CP-01a.\[01\] | Policy is developed and documented | S | Approved by the Head of Cyber (D-CP-01) |
| CP-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| CP-01a.\[03\] | Procedures are developed and documented | S | Approved by the system owner (D-CP-02) |
| CP-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| CP-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section CP.1 |
| CP-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section CP.1 |
| CP-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section CP.5 |
| CP-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section CP.5 |
| CP-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section CP.6 |
| CP-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section CP.6 |
| CP-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section CP.6 |
| CP-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 9 November 2026, as confirmed by the system owner |
| CP-01b. | Official is designated | S | \[Name\] is the system owner |
| CP-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| CP-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 9 November 2026 after the CP pack review; version \<ver\> approved by the Head of Cyber on 9 November 2026 (D-CP-12) |
| CP-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| CP-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 9 November 2026 after the CP pack review (D-CP-13) |
| CP-02\_ODP\[01\] | Who reviews the plan is defined | S | \<Contingency Planning Management\> |
| CP-02\_ODP\[02\] | Who approves the plan is defined | S | \<Contingency Planning Management\> |
| CP-02\_ODP\[03\] | Personnel receiving copies are defined | S | \<Contingency Planning Management\> |
| CP-02\_ODP\[04\] | Elements receiving copies are defined | S | \<Contingency Planning Management\> |
| CP-02\_ODP\[05\] | Review frequency is defined | S | \<Contingency Planning Management\> |
| CP-02\_ODP\[06\] | Personnel told of changes are defined | S | \<Contingency Planning Management\> |
| CP-02\_ODP\[07\] | Elements told of changes are defined | S | \<Contingency Planning Management\> |
| CP-02a.01 | The plan identifies essential functions | S | \<Contingency Planning Management\>, section 3.3 |
| CP-02a.02\[01\] | The plan gives recovery objectives | S | \<Contingency Planning Management\>, section 3.3.2 |
| CP-02a.02\[02\] | The plan gives restoration priorities | S | \<Contingency Planning Management\>, section 3.3 |
| CP-02a.02\[03\] | The plan gives measures | S | \<Contingency Planning Management\>, sections 3.3.2 and 3.10: time to recover and data lost against the objectives, and the restore test result |
| CP-02a.03\[01\] | The plan addresses roles | S | \<Contingency Planning Management\>, section 3.4 |
| CP-02a.03\[02\] | The plan addresses responsibilities | S | \<Contingency Planning Management\>, section 3.4 |
| CP-02a.03\[03\] | The plan addresses people and contacts | S | \<Contingency Planning Management\>, section 3.4 |
| CP-02a.04 | The plan addresses continuing functions in failure | S | \<Contingency Planning Management\>, section 3.6.3: no manual alternative exists, so a reduced service is restored first with the authorising official's agreement |
| CP-02a.05 | The plan addresses full restoration | S | \<Contingency Planning Management\>, section 3.7 |
| CP-02a.06 | The plan addresses sharing information | S | \<Contingency Planning Management\>, section 3.5.3 and appendix A: the call tree, daily user updates and contacts. Phone numbers are still to be added |
| CP-02a.07\[01\] | The plan is reviewed | S | Version \<ver\> reviewed by the system owner and authorising official (D-CP-03); version \<ver\> reviewed by both on 9 November 2026 (D-CP-11) |
| CP-02a.07\[02\] | The plan is approved | S | Version \<ver\> approved by the system owner and authorising official (D-CP-03); version \<ver\> approved by both on 9 November 2026 (D-CP-11) |
| CP-02b.\[01\] | Copies go to personnel | O-D | Not yet shared |
| CP-02b.\[02\] | Copies go to elements | O-D | Not yet shared |
| CP-02c. | Planning is coordinated with incident handling | O-D | Plans approved; not yet in use |
| CP-02d. | The plan is reviewed at the set frequency | O-D | First review not yet due |
| CP-02e.\[01\] | The plan is updated for changes | O-D | First review not yet due |
| CP-02e.\[02\] | The plan is updated for problems | O-D | No test yet held |
| CP-02f.\[01\] | Changes go to personnel | O-D | No changes yet |
| CP-02f.\[02\] | Changes go to elements | O-D | No changes yet |
| CP-02g.\[01\] | Lessons from testing are built in | O-D | No test yet held |
| CP-02g.\[02\] | Lessons from training are built in | O-D | No training yet held |
| CP-02h.\[01\] | The plan is protected from disclosure | O-D | Moves to SharePoint when all families are done (D-GEN-15) |
| CP-02h.\[02\] | The plan is protected from change | O-D | Moves to SharePoint when all families are done (D-GEN-15) |
| CP-02(01) | Planning is coordinated with related plans | O-D | Plans approved; coordination not yet shown |
| CP-02(03)\_ODP\[01\] | Functions are selected | S | \<Contingency Planning Management\> |
| CP-02(03)\_ODP\[02\] | Time is defined | S | \<Contingency Planning Management\> |
| CP-02(03) | Resumption is planned within the time | S | Planned in \<Contingency Planning Management\>, approved (D-CP-03) |
| CP-02(08)\_ODP | Functions are selected | S | \<Contingency Planning Management\> |
| CP-02(08) | Critical assets are identified | S | Listed in \<Contingency Planning Management\>, approved (D-CP-03) |
| CP-03\_ODP\[01\] | Time to train is defined | S | \<Contingency Planning Management\> |
| CP-03\_ODP\[02\] | Training frequency is defined | S | \<Contingency Planning Management\> |
| CP-03\_ODP\[03\] | Content review frequency is defined | S | \<Contingency Planning Management\> |
| CP-03\_ODP\[04\] | Content review events are defined | S | \<Contingency Planning Management\> |
| CP-03a.01 | Training is given within the set time | O-D | PRO-CP-4 approved; not yet in use |
| CP-03a.02 | Training is given when required by changes | O-D | PRO-CP-4 approved; not yet in use |
| CP-03a.03 | Training is given at the set frequency | O-D | PRO-CP-4 approved; not yet in use |
| CP-03b.\[01\] | Content is reviewed at the set frequency | O-D | Content outlined in \<Contingency Planning Management\>, section 3.10; first review not yet due |
| CP-03b.\[02\] | Content is reviewed after set events | O-D | Content outlined in \<Contingency Planning Management\>, section 3.10; no training given yet (PA-81) |
| CP-04\_ODP\[01\] | Test frequency is defined | S | \<Contingency Planning Management\> |
| CP-04\_ODP\[02\] | Tests of effectiveness are defined | S | \<Contingency Planning Management\> |
| CP-04\_ODP\[03\] | Tests of readiness are defined | S | \<Contingency Planning Management\> |
| CP-04a.\[01\] | The plan is tested | O-D | No test yet held |
| CP-04a.\[02\] | Tests show effectiveness | O-D | No test yet held |
| CP-04a.\[03\] | Tests show readiness | O-D | No test yet held |
| CP-04b. | Results are reviewed | O-D | No test yet held |
| CP-04c. | Corrective actions are started | O-D | No test yet held |
| CP-04(01) | Testing is coordinated with related plans | O-D | No test yet held |
| CP-06a.\[01\] | An alternate storage site exists | O-E | \<Organisation\> (EV-CP-01) |
| CP-06a.\[02\] | Agreements allow storage and retrieval | O-E | \<Organisation\> (EV-CP-01) |
| CP-06b. | Controls match the main site | O-E | \<Organisation\> (EV-CP-01) |
| CP-06(01) | It is separate from the main site | O-E | \<Organisation\> (EV-CP-01) |
| CP-06(03)\[01\] | Access problems are identified | O-E | \<Organisation\> (EV-CP-01) |
| CP-06(03)\[02\] | Actions to address them are set | O-E | \<Organisation\> (EV-CP-01) |
| CP-07\_ODP\[01\] | Operations are defined | S | \<Contingency Planning Management\> |
| CP-07\_ODP\[02\] | Time is defined | S | \<Contingency Planning Management\> |
| CP-07a. | An alternate processing site exists | O-E | \<Organisation\> (EV-CP-01) |
| CP-07b.\[01\] | Equipment is available to transfer | O-E | \<Organisation\> (EV-CP-01) |
| CP-07b.\[02\] | Equipment is available to resume | O-E | \<Organisation\> (EV-CP-01) |
| CP-07c. | Controls match the main site | O-E | \<Organisation\> (EV-CP-01) |
| CP-07(01) | It is separate from the main site | O-E | \<Organisation\> (EV-CP-01) |
| CP-07(02)\[01\] | Access problems are identified | O-E | \<Organisation\> (EV-CP-01) |
| CP-07(02)\[02\] | Actions to address them are set | O-E | \<Organisation\> (EV-CP-01) |
| CP-07(03) | Agreements give priority of service | O-E | \<Organisation\> (EV-CP-01) |
| CP-08\_ODP\[01\] | Operations are defined | S | \<Contingency Planning Management\> |
| CP-08\_ODP\[02\] | Time is defined | S | \<Contingency Planning Management\> |
| CP-08 | Alternate telecommunications exist | O-E | \<Organisation\> (EV-CP-02) |
| CP-08(01)(a)\[01\] | Main agreements give priority | O-E | \<Organisation\> (EV-CP-02) |
| CP-08(01)(a)\[02\] | Alternate agreements give priority | O-E | \<Organisation\> (EV-CP-02) |
| CP-08(01)(b) | Priority service is requested where needed | O-E | \<Organisation\> (EV-CP-02) |
| CP-08(02) | No single point of failure is shared | O-E | \<Organisation\> (EV-CP-02) |
| CP-09\_ODP\[01\] | Components are defined | S | \<Contingency Planning Management\> |
| CP-09\_ODP\[02\] | User-level frequency is defined | S | \<Contingency Planning Management\> |
| CP-09\_ODP\[03\] | System-level frequency is defined | S | \<Contingency Planning Management\> |
| CP-09\_ODP\[04\] | Documentation frequency is defined | S | \<Contingency Planning Management\> |
| CP-09a. | User-level information is backed up | O-G | No backups (PA-64) |
| CP-09b. | System-level information is backed up | O-G | No backups (PA-64) |
| CP-09c. | Documentation is backed up | O-G | No second copy (PA-64) |
| CP-09d.\[01\] | Backup confidentiality is protected | O-G | No backups (PA-64) |
| CP-09d.\[02\] | Backup integrity is protected | O-G | No backups (PA-64) |
| CP-09d.\[03\] | Backup availability is protected | O-G | No backups (PA-64) |
| CP-09(01)\_ODP\[01\] | Reliability test frequency is defined | S | \<Contingency Planning Management\> |
| CP-09(01)\_ODP\[02\] | Integrity test frequency is defined | S | \<Contingency Planning Management\> |
| CP-09(01)\[01\] | Backups are tested for reliability | O-G | Procedure shown in Docker on 9 November 2026 (R03, R04); no backups on the VMs (PA-64) |
| CP-09(01)\[02\] | Backups are tested for integrity | O-G | Procedure shown in Docker on 9 November 2026 (R05 to R07); no backups on the VMs (PA-64) |
| CP-09(08)\_ODP | Information is defined | S | \<Contingency Planning Management\> |
| CP-09(08) | Backups are encrypted | O-G | The default backup is a plain archive (R02); no backups (PA-64) |
| CP-10\_ODP\[01\] | Recovery time is defined | S | \<Contingency Planning Management\> |
| CP-10\_ODP\[02\] | Reconstitution time is defined | S | \<Contingency Planning Management\> |
| CP-10\[01\] | Recovery is possible within the time | O-G | Restore shown in Docker in 4.5 seconds (R04, R08); no backups on the VMs (PA-64) |
| CP-10\[02\] | Reconstitution is possible within the time | O-G | Checks defined in \<Contingency Planning Management\>, section 3.7, and shown in Docker (R05 to R07); no backups on the VMs (PA-64) |
| CP-10(02) | Transaction recovery is in place | O-G | Transaction logs are not archived: archive\_mode is off (R09, PA-64) |

### CP.5 Assessment plan

**Table CP-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 23 CP entries in the CSS Moderate baseline, with 124 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 9 November 2026 after the CP pack review |
| Site | One PC, using a separate throwaway Docker stack with sample data. The VMs, backups and second site do not exist yet |
| Examine | \<Policy\> (CP), \<Procedures\> (CP) and \<Contingency Planning Management\> \<ver\>; the test stack's compose file for backup support and volumes; where documents and audit records are stored. Depth: focused. Coverage: focused |
| Test | R01 to R09 by Test-BackupRestore.ps1 on 9 November 2026 (cp-test-results-2026-11-09-v1.0.csv and MANIFEST.md): backup, restore to a fresh server, and checks of rows, document checksums and audit hashes. Depth: focused. Coverage: focused. Backups on the VMs, the second site and a tabletop exercise were not tested |
| Interview | System owner's written answers only. The database and Windows server administrators and \<Organisation\>'s IT service desk remain |
| Previous results reused | None |
| Boundary | \<System Name\>'s database, applications, secrets and the two VMs. \<Organisation\>'s second site, network and telecommunications are inherited |
| Order of assessment | A, recovery objectives and the plan (CP-2 and enhancements); B, backups and recovery (CP-9, CP-10 and enhancements); C, training and testing (CP-3, CP-4); D, inherited sites and telecommunications (CP-6 to CP-8); E, policy (CP-1). The objectives come first because every other result is judged against them |
| Needed from \<Organisation\> | EV-CP-01 and EV-CP-02 in \<Evidence Requests\>: the second site, and telecommunications |
| Evidence retained | The CP evidence, with its manifest; \<Contingency Planning Management\>, sections 3.3 and 3.8 |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. The independent assessor's team, schedule, and depth and coverage are added once agreed. For the Level 2 assessment, the assessor should repeat the restore test on the VMs with encrypted backups at the second site, observe a tabletop exercise, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section CP.4.

## IA Identification and Authentication

### IA.1 Purpose

This records the Level 1 self-assessment of the 24 IA entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes: each non-compliance is rated and decided in \<Risk List\>, and only those to be remediated go to \<Plan of Action and Milestones\>.

### IA.2 How to read this record

**Change since this assessment.** On 12 November 2026 the system owner stated that \<System Name\> signs users in through \<Organisation\>'s AD FS, with multi-factor authentication, takes roles and project access from Active Directory groups, and holds no accounts or passwords of its own (D-AC-23). This chapter assessed the v1.0 build, which signed in with its own passwords and held its accounts and groups in its own database. Its findings are a true record of that build and are not changed. The findings on sign-in, passwords, lockout, accounts and group membership are to be made again with AD FS sign-in, when the tests are repeated and \<Organisation\>'s evidence is in (PA-95). On 15 November 2026 the design moved to \<Identification and Authentication Management\> (D-IA-11), and two items were added for gaps found in its review: PA-116 and PA-117.

**N/A** means not applicable, as decided in \<Tailoring Register\>. This is the organisation's tailoring decision, not a result under CSS, and the independent assessor may test it.

The methods were **Examine** (code and configuration) and **Test**: Test-AuditAndAuth.ps1 checks A01 to A35 on 6 November 2026, repeated with A36 to A38 on the tagged v1.0 build on 8 November with the same IA results; Test-Identification.ps1 checks I01 to I11 against CSS on 9 November; and the AC session checks T38 and T44 to T47. Results and hash manifests are in the AU and IA evidence. The system owner answered INT-IA-01 to 06 in writing.

**Limit of the current evidence:** \<System Name\> ran in Docker on one PC with sample data, in the build labelled v1.0. The Windows Server 2025 VMs, PostgreSQL on Windows and \<Organisation\>'s services have not been examined.

### IA.3 Executive summary

**Table IA-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Not applicable, subject to the conditions in \<Tailoring Register\> | 6 | IA-2(12), IA-5(2), IA-8, IA-8(1), IA-8(2), IA-8(4) |
| Other than satisfied, with at least one system gap | 8 | IA-2(1), IA-2(2), IA-2(8), IA-4, IA-4(4), IA-5, IA-5(1), IA-5(6) |
| Other than satisfied, needing only a decision, approval or evidence | 10 | IA-1, IA-2, IA-3, IA-6, IA-7, IA-11, IA-12, IA-12(2), IA-12(3), IA-12(5) |

**Table IA-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| IA-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews not yet due | NC-IA-01; PA-20 |
| IA-2 | Other than satisfied | 0 of 2 | Met in the application (A09, A10); VMs not assessable | NC-IA-02; PA-25 |
| IA-2(1) | Other than satisfied | 0 of 1 | Administrators sign in with a password alone; accepted to 6 May 2027 | NC-IA-03; PA-23; D-GEN-13, D-IA-07 |
| IA-2(2) | Other than satisfied | 0 of 1 | Users sign in with a password alone; accepted to 6 May 2027 | NC-IA-04; PA-23; D-GEN-13, D-IA-07 |
| IA-2(8) | Other than satisfied | 1 of 2 | Tokens replay from another client; plain HTTP | NC-IA-05; PA-18, PA-46 |
| IA-2(12) | Not applicable | Not applicable | No PIV credentials (TR-IA-01) | None |
| IA-3 | Other than satisfied | 2 of 3 | Device identification not evidenced | NC-IA-06; EV-IA-01 |
| IA-4 | Other than satisfied | 4 of 6 | ServiceNow not set up; deletion frees a username | NC-IA-07; PA-20, PA-47 |
| IA-4(4) | Other than satisfied | 1 of 2 | No staff or contractor status | NC-IA-08; PA-47 |
| IA-5 | Other than satisfied | 4 of 11 | Users cannot change their own password; secrets committed and never changed | NC-IA-09; PA-19, PA-44 |
| IA-5(1) | Other than satisfied | 5 of 10 | 12 to 14 characters accepted; short blocklist; plain HTTP; no strength tool | NC-IA-10; PA-18, PA-45, PA-49, PA-82 |
| IA-5(2) | Not applicable | Not applicable | No PKI authentication (TR-IA-02) | None |
| IA-5(6) | Other than satisfied | 0 of 1 | Secrets committed in source | NC-IA-11; PA-19 |
| IA-6 | Other than satisfied | 0 of 1 | Met in the application (A07, A08); Windows logon not assessable | NC-IA-12 |
| IA-7 | Other than satisfied | 0 of 1 | Cryptographic modules on the VMs not confirmed | NC-IA-13; PA-48, EV-IA-03 |
| IA-8 | Not applicable | Not applicable | No non-organisational users (TR-IA-03) | None |
| IA-8(1) | Not applicable | Not applicable | TR-IA-04 | None |
| IA-8(2) | Not applicable | Not applicable | TR-IA-05 | None |
| IA-8(4) | Not applicable | Not applicable | TR-IA-06 | None |
| IA-11 | Other than satisfied | 1 of 2 | Met in the application (T44, I08, I11); VMs not assessable | NC-IA-14 |
| IA-12 | Other than satisfied | 0 of 5 | Identity proofing by \<Organisation\>'s HR, not evidenced | NC-IA-15; EV-IA-02 |
| IA-12(2) | Other than satisfied | 0 of 1 | As IA-12 | NC-IA-16; EV-IA-02 |
| IA-12(3) | Other than satisfied | 1 of 2 | As IA-12 | NC-IA-17; EV-IA-02 |
| IA-12(5) | Other than satisfied | 1 of 2 | As IA-12 | NC-IA-18; EV-IA-02 |

Of the CSS 92 statements, 41 are satisfied, 14 are not applicable, 7 await a decision or approval, 15 show a gap in the system and 15 await evidence from the VMs or \<Organisation\>.

Password storage, sign-in feedback, lockout, session limits and forced change of temporary passwords work as agreed, and the session limits are stricter than CSS requires. The most serious gaps are password-only sign-in, including for global administrators, accepted to 6 May 2027 with an agreed end state (D-IA-07), and secrets committed in source code. Passwords of 12 to 14 characters are still accepted where CSS requires 15 while sign-in is password-only (PA-82), users cannot change their own password, and the blocked list is short. The assurance levels in \<Identification and Authentication Management\>, section 3.4, were accepted by the authorising official (D-IA-08).

### IA.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Statement wording is condensed, and the identifiers are CSS's. Findings are dated 6 November 2026, updated on 9 November 2026 where the basis says so.

**Table IA-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| IA-01\_ODP\[01\] | Who receives the policy is defined | S | \<Identification and Authentication Management\> |
| IA-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Identification and Authentication Management\> |
| IA-01\_ODP\[03\] | Policy level is selected | S | \<Identification and Authentication Management\> |
| IA-01\_ODP\[04\] | Managing official is defined | S | System owner |
| IA-01\_ODP\[05\] | Policy review frequency is defined | S | \<Identification and Authentication Management\> |
| IA-01\_ODP\[06\] | Policy review events are defined | S | \<Identification and Authentication Management\> |
| IA-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Identification and Authentication Management\> |
| IA-01\_ODP\[08\] | Procedures review events are defined | S | \<Identification and Authentication Management\> |
| IA-01a.\[01\] | Policy is developed and documented | S | Approved by the Head of Cyber (D-IA-01) |
| IA-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| IA-01a.\[03\] | Procedures are developed and documented | S | Approved (D-IA-02) |
| IA-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| IA-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section IA.1 |
| IA-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section IA.1 |
| IA-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section IA.5 |
| IA-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section IA.5 |
| IA-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section IA.6 |
| IA-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section IA.6. Not yet agreed with \<Organisation\> |
| IA-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section IA.6 |
| IA-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 9 November 2026, as confirmed by the system owner |
| IA-01b. | Official is designated | S | \[Name\] is the system owner |
| IA-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| IA-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 9 November 2026 after the IA pack review; version \<ver\> approved by the Head of Cyber on 9 November 2026 (D-IA-09) |
| IA-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| IA-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 9 November 2026 (D-IA-10) |
| IA-02\[01\] | Users are uniquely identified and authenticated | O-E | Application yes (A09, A10); VMs not available |
| IA-02\[02\] | Identity is tied to processes acting for users | O-E | Application yes (session-bound tokens); VMs not available |
| IA-02(01) | MFA for privileged accounts | O-G | Password alone works (A11, PA-23) |
| IA-02(02) | MFA for non-privileged accounts | O-G | Password alone works (A12, PA-23) |
| IA-02(08)\_ODP | Accounts needing replay resistance are selected | S | \<Identification and Authentication Management\> |
| IA-02(08) | Authentication is replay resistant | O-G | Token works from another client (A13), and traffic is plain HTTP (A14) (PA-46, PA-18) |
| IA-02(12) | PIV credentials are accepted | N/A | TR-IA-01 |
| IA-03\_ODP\[01\] | Devices are defined | S | \<Identification and Authentication Management\> |
| IA-03\_ODP\[02\] | Connection type is selected | S | Network |
| IA-03 | Devices are identified before connecting | O-E | Inherited from \<Organisation\> (EV-IA-01) |
| IA-04\_ODP\[01\] | Who authorises identifiers is defined | S | \<Identification and Authentication Management\> |
| IA-04\_ODP\[02\] | Reuse period is defined | S | Never reused |
| IA-04a. | Authorisation is received before assigning | O-G | ServiceNow workflow planned, not yet set up (PA-20) |
| IA-04b. | An identifier is selected for the person or role | S | Named accounts; PRO-AC-1 |
| IA-04c. | It is assigned to the intended person | S | PRO-AC-1, PRO-IA-1 |
| IA-04d. | Reuse is prevented | O-G | Deleting an account frees its username (PA-47) |
| IA-04(04)\_ODP | Status to show is defined | S | Staff or contractor |
| IA-04(04) | Identifiers show the status | O-G | No such field (PA-47) |
| IA-05\_ODP\[01\] | Change periods are defined | S | \<Identification and Authentication Management\> |
| IA-05\_ODP\[02\] | Change events are defined | S | \<Identification and Authentication Management\> |
| IA-05a. | Identity is verified before issuing | O-D | PRO-IA-2 approved, not walked through |
| IA-05b. | Initial content is established | S | Temporary passwords; generated seed values |
| IA-05c. | Strength is sufficient | O-G | Password only, with a short blocked list (PA-23, PA-45) |
| IA-05d. | Administrative procedures are in place | O-D | PRO-IA-2 and PRO-IA-3 approved, not walked through |
| IA-05e. | Defaults are changed before first use | S | A01 |
| IA-05f. | Authenticators are changed as set | O-G | Users cannot change their own (A34, PA-44); secrets never rotated (PA-19). A change by reset ends other sessions (I07) |
| IA-05g. | Content is protected | O-G | Secrets committed in source (PA-19) |
| IA-05h.\[01\] | Individuals must protect authenticators | O-D | \<Security Operating Procedures\> approved; not yet signed |
| IA-05h.\[02\] | Devices must protect authenticators | O-E | \<Organisation\> (EV-IA-01) |
| IA-05i. | Shared authenticators change with membership | N/A | Shared accounts prohibited (TR-AC-02) |
| IA-05(01)\_ODP\[01\] | List refresh frequency is defined | S | Every 12 months |
| IA-05(01)\_ODP\[02\] | Composition rules are defined | S | \<Identification and Authentication Management\> |
| IA-05(01)(a) | A list is kept and updated | O-G | 15 entries built into the application (PA-45) |
| IA-05(01)(b) | New passwords are checked against it | O-G | Checked (A06), but a common password passes (A33, PA-45) |
| IA-05(01)(c) | Passwords travel over protected channels | O-G | Plain HTTP (A14, PA-18) |
| IA-05(01)(d) | Passwords are stored with a salted function | S | A02 |
| IA-05(01)(e) | New password is required on recovery | S | Reset forces a change; code |
| IA-05(01)(f) | Long passwords are allowed | S | Up to 128 characters, with spaces and accented letters (I05, I06) |
| IA-05(01)(g) | Tools help users pick strong passwords | O-G | None (PA-49) |
| IA-05(01)(h) | Composition rules are enforced | O-G | The rule is now 15 characters while password-only (D-IA-P02); 12 and 14 are accepted (I02, I03, PA-82) |
| IA-05(02)(a)(01) | Private key access is enforced | N/A | TR-IA-02 |
| IA-05(02)(a)(02) | Identity maps to the account | N/A | TR-IA-02 |
| IA-05(02)(b)(01) | Certificates are validated | N/A | TR-IA-02 |
| IA-05(02)(b)(02) | Revocation data is cached | N/A | TR-IA-02 |
| IA-05(06) | Authenticators are protected to match the data | O-G | Secrets committed in source (PA-19) |
| IA-06 | Feedback is obscured | O-E | Application yes (A07, A08); VMs not available |
| IA-07 | Cryptographic module authentication meets requirements | O-E | Modules on the VMs not confirmed (PA-48) |
| IA-08 | Non-organisational users are identified | N/A | TR-IA-03 |
| IA-08(01)\[01\] | Other agencies' PIV is accepted | N/A | TR-IA-04 |
| IA-08(01)\[02\] | Other agencies' PIV is verified | N/A | TR-IA-04 |
| IA-08(02)(a) | Only compliant external authenticators are accepted | N/A | TR-IA-05 |
| IA-08(02)(b)\[01\] | A list is documented | N/A | TR-IA-05 |
| IA-08(02)(b)\[02\] | A list is maintained | N/A | TR-IA-05 |
| IA-08(04)\_ODP | Identity profiles are defined | N/A | TR-IA-06 |
| IA-08(04) | Profiles are followed | N/A | TR-IA-06 |
| IA-11\_ODP | When to sign in again is defined | S | \<Identification and Authentication Management\> |
| IA-11 | Users must sign in again then | O-E | Application yes: idle limit (T44), tokens under 8 hours (I08), and the 8-hour limit passed five times in a row (I11, closing PA-33); VMs not available |
| IA-12a. | Users are identity proofed | O-E | \<Organisation\>'s pre-employment checks (EV-IA-02) |
| IA-12b. | Identities resolve to one person | O-E | \<Organisation\> (EV-IA-02) |
| IA-12c.\[01\] | Evidence is collected | O-E | \<Organisation\> (EV-IA-02) |
| IA-12c.\[02\] | Evidence is validated | O-E | \<Organisation\> (EV-IA-02) |
| IA-12c.\[03\] | Evidence is verified | O-E | \<Organisation\> (EV-IA-02) |
| IA-12(02) | Evidence is presented | O-E | \<Organisation\> (EV-IA-02) |
| IA-12(03)\_ODP | Methods are defined | S | \<Identification and Authentication Management\> |
| IA-12(03) | Evidence is validated by those methods | O-E | \<Organisation\> (EV-IA-02) |
| IA-12(05)\_ODP | Confirmation method is selected | S | Notice of proofing |
| IA-12(05) | Address is confirmed by that method | O-E | \<Organisation\> (EV-IA-02) |

### IA.5 Assessment plan

**Table IA-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 24 IA entries in the CSS Moderate baseline, with 92 determination statements, 14 of them not applicable under \<Tailoring Register\> |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0), with CSS as the test standard for authenticators |
| Dates | 6 November 2026; updated on 8 and 9 November 2026 |
| Site | One PC, using a separate throwaway Docker stack with sample data. The VMs are not built |
| Examine | The API's password service, the API's sign-in service, the sign-in service of each UI, the security data model, the settings files and the database, at tag v1.0; \<Policy\> (IA), \<Procedures\> (IA) and \<Identification and Authentication Management\>. Depth: focused. Coverage: focused |
| Test | A01 to A38 by Test-AuditAndAuth.ps1 (6 and 8 November); I01 to I11 by Test-Identification.ps1 (9 November); T38 and T44 to T47 from the AC tests. Each run has a hash manifest. Depth: focused. Coverage: focused. Windows logon, device identification and cryptographic modules were not tested |
| Interview | System owner's written answers only. Global administrators, \<Organisation\>'s security contact and HR remain |
| Previous results reused | The AC session checks from 5 November 2026 |
| Boundary | \<System Name\>'s sign-in, accounts, authenticators and secrets. \<Organisation\>'s identity proofing and device identification are inherited |
| Order of assessment | A, authenticators (IA-5 and enhancements, IA-6, IA-7); B, sign-in and multi-factor (IA-2 and enhancements, IA-11); C, identifiers (IA-4); D, inherited proofing and devices (IA-3, IA-12); E, policy (IA-1). Authenticators come first because sign-in depends on them |
| Needed from \<Organisation\> | EV-IA-01 to EV-IA-04 in \<Evidence Requests\>: device identification, identity proofing, cryptographic modules, and sign-in through AD FS |
| Evidence retained | The AU and IA evidence, with its manifest; \<Identification and Authentication Management\>, sections 3.4 to 3.6 |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. The independent assessor's team, schedule, and depth and coverage are added once agreed. For the Level 2 assessment, the assessor should repeat the checks on the VMs, test multi-factor sign-in once built, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section IA.4.

## IR Incident Response

### IR.1 Purpose

This records the Level 1 self-assessment of the 13 IR entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### IR.2 How to read this record

**Change since this assessment.** On 17 November 2026 the Incident Response Plan was rebuilt as \<Incident Response Management\> in the form of the other family documents, with the plan as its section 3 and each control set out part by part (D-IR-10). A playbook for a compromise at \<Organisation\> was added, as sign-in now goes through AD FS (D-AC-23). Two items were added for gaps this chapter found: PA-118 and PA-119. The section numbers cited for IR-8 follow the rebuilt document. The findings below are a true record of 6 and 10 November 2026 and are not changed.

The methods were **Examine** (documents and code) and **Test**: the containment and evidence drill D01 to D08 by Test-IncidentReadiness.ps1 on the tagged v1.0 build on 10 November 2026, with hashes in MANIFEST.md, in the IR evidence, on a throwaway stack. The system owner answered INT-IR-01 to 04 in writing. \<System Name\> has had no operational incidents, as it is not live; INC-2026-001 records the secrets found in git history.

**Limit of the current evidence:** the drill shows the containment steps work in Docker. No tabletop exercise has been held, and the VMs and \<Organisation\>'s services have not been examined.

### IR.3 Executive summary

**Table IR-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, with at least one system gap | 3 | IR-4(1), IR-6(1), IR-7(1) |
| Other than satisfied, needing only a decision, approval or evidence | 10 | IR-1, IR-2, IR-3, IR-3(2), IR-4, IR-5, IR-6, IR-6(3), IR-7, IR-8 |

**Table IR-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| IR-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews outstanding | NC-IR-01; PA-20 |
| IR-2 | Other than satisfied | 4 of 9 | Training content written; no training yet | NC-IR-02; PA-81 |
| IR-3 | Other than satisfied | 2 of 3 | No tabletop yet; containment shown in Docker (D01, D03) | NC-IR-03; PA-81 |
| IR-3(2) | Other than satisfied | 0 of 1 | No tabletop with the contingency plan yet | NC-IR-04; PA-81 |
| IR-4 | Other than satisfied | 0 of 13 | Plan and playbooks written; handling not yet in use | NC-IR-05 |
| IR-4(1) | Other than satisfied | 1 of 2 | ServiceNow not set up for incidents | NC-IR-06; PA-65 |
| IR-5 | Other than satisfied | 0 of 2 | Register in \<Incident Response Management\> with INC-2026-001; ServiceNow not in use | NC-IR-07; PA-65 |
| IR-6 | Other than satisfied | 2 of 4 | Reporting not yet in use; \<Organisation\>'s route unconfirmed | NC-IR-08; EV-IR-01 |
| IR-6(1) | Other than satisfied | 1 of 2 | ServiceNow not set up for incidents | NC-IR-09; PA-65 |
| IR-6(3) | Other than satisfied | 0 of 1 | Supplier reporting not yet in use | NC-IR-10 |
| IR-7 | Other than satisfied | 0 of 2 | Assistance not yet in use | NC-IR-11; EV-IR-01 |
| IR-7(1) | Other than satisfied | 1 of 2 | ServiceNow not set up for incidents | NC-IR-12; PA-65 |
| IR-8 | Other than satisfied | 17 of 24 | Version \<ver\> awaits the Head of Cyber; not yet shared or protected | NC-IR-13; D-IR-07, D-GEN-15 |

Of the CSS 90 statements, 49 are satisfied, 38 await a decision or approval, 3 show a gap in the system and none awaits evidence.

The plan now follows CSS, with severity targets, breach steps, playbooks and evidence handling, but has not been exercised. The drill shows containment works: a suspect user's sessions ended and a disabled account was locked out at once, and audit records exported with a repeatable hash. The gaps are that ServiceNow is not set up for incidents, ending sessions is not audited (D02, PA-14), and the application log repeats personal data (D08, PA-75).

### IR.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 10 November 2026 where the basis says so.

**Table IR-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| IR-01\_ODP\[01\] | Who receives the policy is defined | S | \<Incident Response Management\> |
| IR-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Incident Response Management\> |
| IR-01\_ODP\[03\] | Policy level is selected | S | \<Incident Response Management\> |
| IR-01\_ODP\[04\] | Managing official is defined | S | System owner |
| IR-01\_ODP\[05\] | Policy review frequency is defined | S | \<Incident Response Management\> |
| IR-01\_ODP\[06\] | Policy review events are defined | S | \<Incident Response Management\> |
| IR-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Incident Response Management\> |
| IR-01\_ODP\[08\] | Procedures review events are defined | S | \<Incident Response Management\> |
| IR-01a.\[01\] | Policy is developed and documented | S | Approved by the Head of Cyber (D-IR-01) |
| IR-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| IR-01a.\[03\] | Procedures are developed and documented | S | Approved by the system owner (D-IR-02) |
| IR-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| IR-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section IR.1 |
| IR-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section IR.1 |
| IR-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section IR.5 |
| IR-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section IR.5 |
| IR-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section IR.6 |
| IR-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section IR.6 |
| IR-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section IR.6 |
| IR-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 10 November 2026, as confirmed by the system owner |
| IR-01b. | Official is designated | S | \[Name\] is the system owner |
| IR-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| IR-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 10 November 2026 after the IR pack review; version \<ver\> awaits the Head of Cyber (D-IR-07) |
| IR-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| IR-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 10 November 2026 (D-IR-08) |
| IR-02\_ODP\[01\] | Time to train is defined | S | \<Incident Response Management\> |
| IR-02\_ODP\[02\] | Training frequency is defined | S | \<Incident Response Management\> |
| IR-02\_ODP\[03\] | Content review frequency is defined | S | \<Incident Response Management\> |
| IR-02\_ODP\[04\] | Content review events are defined | S | \<Incident Response Management\> |
| IR-02a.01 | Training is given within the set time | O-D | PRO-IR-3 approved; not yet in use |
| IR-02a.02 | Training is given when required by changes | O-D | PRO-IR-3 approved; not yet in use |
| IR-02a.03 | Training is given at the set frequency | O-D | PRO-IR-3 approved; not yet in use |
| IR-02b.\[01\] | Content is reviewed at the set frequency | O-D | Content written in \<Incident Response Management\>, section 3.4, and PRO-IR-3; first review not yet due |
| IR-02b.\[02\] | Content is reviewed after set events | O-D | Content written in \<Incident Response Management\>, section 3.4, and PRO-IR-3; no event yet |
| IR-03\_ODP\[01\] | Test frequency is defined | S | \<Incident Response Management\> |
| IR-03\_ODP\[02\] | Tests are defined | S | \<Incident Response Management\> |
| IR-03 | Capability is tested | O-D | No exercise yet held |
| IR-03(02) | Testing is coordinated with related plans | O-D | No exercise yet held |
| IR-04a.\[01\] | A handling capability is in place, consistent with the plan | O-D | Plan approved; not yet in use |
| IR-04a.\[02\] | It includes preparation | O-D | Plan approved; not yet in use |
| IR-04a.\[03\] | It includes detection and analysis | O-D | Plan approved; not yet in use |
| IR-04a.\[04\] | It includes containment | O-D | Playbooks in \<Incident Response Management\>, section 3.9; containment shown in Docker (D01, D03); not yet in use |
| IR-04a.\[05\] | It includes eradication | O-D | Plan approved; not yet in use |
| IR-04a.\[06\] | It includes recovery | O-D | Plan approved; not yet in use |
| IR-04b. | Handling is coordinated with contingency planning | O-D | Plans approved; not yet in use |
| IR-04c.\[01\] | Lessons are built into procedures, training and testing | O-D | No incident or exercise yet |
| IR-04c.\[02\] | Changes from lessons are made | O-D | No incident or exercise yet |
| IR-04d.\[01\] | Rigour is consistent | O-D | Plan approved; not yet in use |
| IR-04d.\[02\] | Intensity is consistent | O-D | Plan approved; not yet in use |
| IR-04d.\[03\] | Scope is consistent | O-D | Plan approved; not yet in use |
| IR-04d.\[04\] | Results are consistent | O-D | Plan approved; not yet in use |
| IR-04(01)\_ODP | Mechanisms are defined | S | \<Incident Response Management\> |
| IR-04(01) | Handling is supported automatically | O-G | ServiceNow not set up for incidents (PA-65) |
| IR-05\[01\] | Incidents are tracked | O-D | PRO-IR-2 approved; not yet in use |
| IR-05\[02\] | Incidents are documented | O-D | PRO-IR-2 approved; not yet in use |
| IR-06\_ODP\[01\] | Time to report is defined | S | \<Incident Response Management\> |
| IR-06\_ODP\[02\] | Authorities are defined | S | \<Incident Response Management\> |
| IR-06a. | People must report within the set time | O-D | Policy approved; not yet in use |
| IR-06b. | Incidents are reported to the authorities | O-D | PRO-IR-1 approved; not yet in use |
| IR-06(01)\_ODP | Mechanisms are defined | S | \<Incident Response Management\> |
| IR-06(01) | Reporting uses those mechanisms | O-G | ServiceNow not set up for incidents (PA-65) |
| IR-06(03) | Suppliers are told | O-D | PRO-IR-1 approved; not yet in use |
| IR-07\[01\] | A support resource exists | O-D | PRO-IR-4 approved; not yet in use |
| IR-07\[02\] | It gives advice and help to users | O-D | PRO-IR-4 approved; not yet in use |
| IR-07(01)\_ODP | Mechanisms are defined | S | \<Incident Response Management\> |
| IR-07(01) | Support is made more available automatically | O-G | ServiceNow not set up for incidents (PA-65) |
| IR-08\_ODP\[01\] | Who approves the plan is defined | S | \<Incident Response Management\> |
| IR-08\_ODP\[02\] | Review frequency is defined | S | \<Incident Response Management\> |
| IR-08\_ODP\[03\] | Who designates responsibility is defined | S | \<Incident Response Management\> |
| IR-08\_ODP\[04\] | Personnel receiving copies are defined | S | \<Incident Response Management\> |
| IR-08\_ODP\[05\] | Elements receiving copies are defined | S | \<Incident Response Management\> |
| IR-08\_ODP\[06\] | Personnel told of changes are defined | S | \<Incident Response Management\> |
| IR-08\_ODP\[07\] | Elements told of changes are defined | S | \<Incident Response Management\> |
| IR-08a.01 | The plan gives a roadmap | S | \<Incident Response Management\>, section 3 |
| IR-08a.02 | The plan describes the structure | S | \<Incident Response Management\>, section 3.3 |
| IR-08a.03 | The plan gives the approach | S | \<Incident Response Management\>, section 3.2 |
| IR-08a.04 | The plan meets \<System Name\>'s needs | S | \<Incident Response Management\>, sections 3.2, 3.6, 3.8 and 3.9: severity set for Restricted and HR documents, the personal data breach steps, and playbooks for \<System Name\>'s likely incidents |
| IR-08a.05 | The plan defines reportable incidents | S | \<Incident Response Management\>, section 3.11 |
| IR-08a.06 | The plan gives measures | S | \<Incident Response Management\>, section 3.12: measures with targets, reported monthly |
| IR-08a.07 | The plan defines resources and support | S | \<Incident Response Management\>, section 3.12 |
| IR-08a.08 | The plan addresses sharing | S | \<Incident Response Management\>, section 3.13 |
| IR-08a.09 | The plan is reviewed and approved | S | Approved by the Head of Cyber (D-IR-03) |
| IR-08a.10 | The plan designates responsibility | S | \<Incident Response Management\>, section 3.3 |
| IR-08b.\[01\] | Copies go to personnel | O-D | Not yet shared |
| IR-08b.\[02\] | Copies go to elements | O-D | Not yet shared |
| IR-08c. | The plan is updated | O-D | First review not yet due |
| IR-08d.\[01\] | Changes go to personnel | O-D | No changes yet |
| IR-08d.\[02\] | Changes go to elements | O-D | No changes yet |
| IR-08e.\[01\] | The plan is protected from disclosure | O-D | Moves to SharePoint when all families are done (D-GEN-15) |
| IR-08e.\[02\] | The plan is protected from change | O-D | Moves to SharePoint when all families are done (D-GEN-15) |

### IR.5 Assessment plan

**Table IR-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 13 IR entries in the CSS Moderate baseline, with 90 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0), with CSS as the reference for the plan |
| Dates | 6 November 2026; updated on 10 November 2026 after the IR pack review |
| Site | One PC, using a separate throwaway Docker stack with sample data. The VMs are not built |
| Examine | \<Policy\> (IR), \<Procedures\> (IR) and \<Incident Response Management\> \<ver\>; TPL-10 and TPL-11; SyOps section 4.9; the session and audit code. Depth: focused. Coverage: focused |
| Test | D01 to D08 by Test-IncidentReadiness.ps1 on 10 November 2026 (ir-test-results-2026-11-10-v1.0.csv, the evidence export and MANIFEST.md). Depth: focused. Coverage: focused. No tabletop exercise has been held |
| Interview | System owner's written answers only. The security officer, legal adviser and \<Organisation\>'s security contact remain |
| Previous results reused | The AC session checks T37, T38 and T40 to T42 from 5 November 2026 |
| Boundary | \<System Name\>'s incident handling, records and evidence. \<Organisation\>'s monitoring, incident process and forensic help are inherited |
| Order of assessment | A, the plan and its approval (IR-8); B, handling and records (IR-4, IR-4(1), IR-5); C, reporting (IR-6 and enhancements); D, training and testing (IR-2, IR-3, IR-3(2)); E, assistance (IR-7, IR-7(1)); F, policy (IR-1). The plan comes first because every other result is judged against it |
| Needed from \<Organisation\> | EV-IR-01 in \<Evidence Requests\>: its incident process and contact route |
| Evidence retained | The IR evidence, with its manifest; \<Incident Response Management\>, sections 3.9, 3.10 and 3.14 |

The authorising official approved this plan (D-GEN-18), as confirmed by the system owner on 8 November 2026. The independent assessor's team, schedule, and depth and coverage are added once agreed. For the Level 2 assessment, the assessor should observe the first tabletop exercise, repeat the drill on the VMs, examine the incident register and TPL-10 records, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section IR.4.

## MA Maintenance

### MA.1 Purpose

This records the Level 1 self-assessment of the 9 MA entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### MA.2 How to read this record

**Change since this assessment.** On 17 November 2026 the maintenance design was cut from \<Control Implementation Register\> into \<Maintenance Management\>, with each control set out part by part (D-MA-09). The system owner had decided on 13 November that the applications run as Windows services on the servers (D-PL-10), so the container tools and images tested here belong to the test environment only. Sign-in now goes through AD FS (D-AC-23). One item was added for gaps this chapter found: PA-120. The findings below are a true record of 6 and 10 November 2026 and are not changed.

The methods were **Examine** (documents and code) and **Test**: checks M01 to M12 by Test-Maintenance.ps1 on the tagged v1.0 build on 10 November 2026, with hashes in MANIFEST.md, in the MA evidence, on a throwaway stack. The system owner answered INT-MA-01 to 04 in writing. No maintenance has taken place on the target VMs, as they are not built.

**Limit of the current evidence:** the tests show how the code and images behave in Docker. They are not evidence of maintenance on the VMs, or of \<Organisation\>'s maintenance, routes and support.

### MA.3 Executive summary

**Table MA-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, with at least one system gap | 2 | MA-3, MA-4 |
| Other than satisfied, needing only a decision, approval or evidence | 7 | MA-1, MA-2, MA-3(1), MA-3(2), MA-3(3), MA-5, MA-6 |

**Table MA-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| MA-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews outstanding | NC-MA-01; PA-20 |
| MA-2 | Other than satisfied | 3 of 12 | Procedures written; not yet in use; no record of built-in page use or schema changes | NC-MA-02; PA-31, PA-84 |
| MA-3 | Other than satisfied | 2 of 5 | Built-in maintenance pages and a package manager in the images (M01, M03, M10) | NC-MA-03; PA-31, PA-85, PA-67 |
| MA-3(1) | Other than satisfied | 0 of 1 | Inspection not yet in use | NC-MA-04 |
| MA-3(2) | Other than satisfied | 0 of 1 | Defender not on the VMs | NC-MA-05; PA-58 |
| MA-3(3) | Other than satisfied | 1 of 5 | Removal control not yet in use | NC-MA-06 |
| MA-4 | Other than satisfied | 1 of 8 | Admin portal open to every network and password-only (M04); \<Organisation\>'s route not evidenced | NC-MA-07; PA-83, PA-23, EV-MA-02 |
| MA-5 | Other than satisfied | 2 of 4 | Provisional list; screening dates to come | NC-MA-08; PA-67 |
| MA-6 | Other than satisfied | 2 of 3 | Support within 24 hours not evidenced; software versions supported (M11) | NC-MA-09; EV-MA-01 |

Of the CSS 64 statements, 32 are satisfied, 23 await a decision or approval, 4 show a gap in the system and 5 await evidence from the VMs or \<Organisation\>.

The approach is approved but not yet in use. The tests show that the check after maintenance works and that an admin session ends at sign-out. The gaps are in \<System Name\> itself: five maintenance pages that write no audit record, an admin portal open to every network, and a package manager in the images.

### MA.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 10 November 2026 where the basis says so.

**Table MA-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| MA-01\_ODP\[01\] | Who receives the policy is defined | S | \<Maintenance Management\> |
| MA-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Maintenance Management\> |
| MA-01\_ODP\[03\] | Policy level is selected | S | \<Maintenance Management\> |
| MA-01\_ODP\[04\] | Managing official is defined | S | System owner |
| MA-01\_ODP\[05\] | Policy review frequency is defined | S | \<Maintenance Management\> |
| MA-01\_ODP\[06\] | Policy review events are defined | S | \<Maintenance Management\> |
| MA-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Maintenance Management\> |
| MA-01\_ODP\[08\] | Procedures review events are defined | S | \<Maintenance Management\> |
| MA-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-MA-01); version \<ver\> awaits re-approval (D-MA-07) |
| MA-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| MA-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-MA-08) |
| MA-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| MA-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section MA.1 |
| MA-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section MA.1 |
| MA-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section MA.5 |
| MA-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section MA.5 |
| MA-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section MA.6 |
| MA-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section MA.6 |
| MA-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section MA.6 |
| MA-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 10 November 2026, as confirmed by the system owner |
| MA-01b. | Official is designated | S | \[Name\] is the system owner |
| MA-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| MA-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 10 November 2026 after the MA pack review (D-MA-06) |
| MA-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| MA-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 10 November 2026 (D-MA-08) |
| MA-02\_ODP\[01\] | Who approves removal is defined | S | \<Maintenance Management\> |
| MA-02\_ODP\[02\] | Information to remove is defined | S | \<Maintenance Management\> |
| MA-02\_ODP\[03\] | Information in records is defined | S | \<Organisation\>'s corporate parameter values; TPL-12 extended |
| MA-02a.\[01\] | Maintenance is scheduled | O-D | Schedule in PRO-MA-6 and change records in PRO-MA-1; not yet in use |
| MA-02a.\[02\] | Maintenance is documented | O-D | PRO-MA-1 approved; not yet in use |
| MA-02a.\[03\] | Records are reviewed | O-D | Monthly review by the security officer (C48); not yet in use |
| MA-02b.\[01\] | All maintenance is approved | O-D | PRO-MA-1 approved; not yet in use |
| MA-02b.\[02\] | All maintenance is monitored | O-D | PRO-MA-1 and PRO-MA-4; not yet in use. The built-in maintenance pages leave no audit record (M03, PA-31) |
| MA-02c. | Removal is explicitly approved | O-D | PRO-MA-2 approved; not yet in use |
| MA-02d. | Equipment is sanitised before removal | O-E | \<Organisation\> (EV-MA-01) |
| MA-02e. | Controls are checked afterwards | O-D | Checklist in PRO-MA-1 (\<Procedures\>, Table MA-2); the first three checks passed in Docker after a simulated restart (M06 to M08); not yet in use on the VMs |
| MA-02f. | Information is in maintenance records | O-D | TPL-12 holds the fields; not yet in use. Schema changes leave no record in the database (M09, PA-84) |
| MA-03\_ODP | Tool review frequency is defined | S | \<Maintenance Management\> |
| MA-03a.\[01\] | Tool use is approved | S | Provisional tool list in \<Maintenance Management\>, section 3.5, approved by the system owner (D-MA-08); to be confirmed at VM build (PA-67) |
| MA-03a.\[02\] | Tool use is controlled | O-G | Five built-in maintenance pages are open to global administrators (M01), and the images hold a package manager (M10); controlled only by PRO-MA-7 (PA-31, PA-85) |
| MA-03a.\[03\] | Tool use is monitored | O-G | The built-in maintenance pages write no audit record, so their use cannot be monitored (M03, PA-31) |
| MA-03b. | Tools are reviewed | O-D | First review at VM build, then every 12 months (C28) |
| MA-03(01) | Tools are inspected | O-D | PRO-MA-3 approved; not yet in use |
| MA-03(02) | Media are checked for malicious code | O-E | Defender not yet on the VMs (PA-58) |
| MA-03(03)\_ODP | Who allows removal is defined | S | \<Maintenance Management\> |
| MA-03(03)(a) | Removal prevented by checking for no data | O-D | PRO-MA-3 approved; not yet in use |
| MA-03(03)(b) | Removal prevented by sanitising | O-D | PRO-MA-3 approved; not yet in use |
| MA-03(03)(c) | Removal prevented by keeping it on site | O-D | PRO-MA-3 approved; not yet in use |
| MA-03(03)(d) | Removal needs an exemption | O-D | PRO-MA-2 and PRO-MA-7, including data sent for support; not yet in use |
| MA-04a.\[01\] | Remote maintenance is approved | O-D | PRO-MA-4 approved; not yet in use |
| MA-04a.\[02\] | Remote maintenance is monitored | O-D | PRO-MA-4 approved; not yet in use |
| MA-04b.\[01\] | Tools are allowed only as policy says | O-G | The admin portal, route R3, is published on every network interface, not only the managed route (M04, PA-83) |
| MA-04b.\[02\] | Tools are documented in the security plan | S | Routes and tools in \<Maintenance Management\>, sections 3.4 and 3.5, referenced from \<System Security Plan\>, section 3.7. SSP Appendix L is superseded |
| MA-04c. | Strong authentication is used | O-G | The admin portal is password-only (PA-23); \<Organisation\>'s route is not evidenced (EV-MA-02) |
| MA-04d. | Records are kept | O-D | TPL-12 with the session reference (PRO-MA-4); not yet in use |
| MA-04e.\[01\] | Sessions end when finished | O-E | Signing out of the admin portal ends the session (M12); \<Organisation\>'s route not evidenced (EV-MA-02) |
| MA-04e.\[02\] | Network connections end when finished | O-E | \<Organisation\>'s route (EV-MA-02) |
| MA-05a.\[01\] | An authorisation process exists | S | PRO-MA-5, approved (D-MA-02) |
| MA-05a.\[02\] | A list is kept | S | Provisional list in \<Maintenance Management\>, section 3.6, approved by the system owner (D-MA-08); to be confirmed at VM build (PA-67) |
| MA-05b. | Unescorted people have the access needed | O-D | Screening and Part B dates are placeholders in \<Maintenance Management\>, section 3.6 |
| MA-05c. | Others are supervised | O-D | PRO-MA-5 approved; not yet in use |
| MA-06\_ODP\[01\] | Components are defined | S | \<Maintenance Management\>, section 3.8 (D-MA-P02) |
| MA-06\_ODP\[02\] | Time is defined | S | 24 hours for hardware and the hypervisor (D-MA-P02) |
| MA-06 | Support and parts arrive within the time | O-E | \<Organisation\> (EV-MA-01). .NET 10 and PostgreSQL 18 are supported versions (M11) |

### MA.5 Assessment plan

**Table MA-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 9 MA entries in the CSS Moderate baseline, with 64 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 10 November 2026 after the MA pack review |
| Site | One PC, using a separate throwaway Docker stack with sample data. The VMs are not built |
| Examine | \<Policy\> (MA), \<Procedures\> (MA) and the MA chapter of \<Control Implementation Register\> at \<ver\>, now in \<Maintenance Management\>; TPL-12; SyOps sections 4.6 and 4.7; the admin portal maintenance pages, the test stack's compose file and the image build file. Depth: focused. Coverage: focused |
| Test | M01 to M12 by Test-Maintenance.ps1 on 10 November 2026 (ma-test-results-2026-11-10-v1.0.csv and MANIFEST.md). Depth: focused. Coverage: focused |
| Interview | System owner's written answers only. The Windows server administrator, database administrator, global administrator and \<Organisation\>'s IT service desk remain |
| Previous results reused | AC checks T03, T26 and T38 (5 November 2026); IA check A11 (global administrator password-only); CM checks C09 and C10 |
| Boundary | Maintenance of the VMs, database and applications, and \<System Name\>'s built-in maintenance functions. Hardware and hypervisor maintenance, the managed route and support are inherited from \<Organisation\> |
| Order of assessment | A, tools and built-in functions (MA-3 and enhancements); B, remote routes (MA-4); C, controlled maintenance and records (MA-2); D, people (MA-5); E, timely maintenance (MA-6); F, policy (MA-1). Tools come first because the largest gaps are there |
| Needed from \<Organisation\> | EV-MA-01 and EV-MA-02 in \<Evidence Requests\>: its maintenance process, sanitising, service agreement, and the managed route's settings and logs |
| Evidence retained | The MA evidence, with its manifest; \<Maintenance Management\>, sections 3.4 to 3.8 |

For the Level 2 assessment, the assessor should repeat the tests on the VMs, examine TPL-12 records and change records for real maintenance, observe a remote session over the managed route, hold the interviews, examine \<Organisation\>'s evidence and re-determine every statement in section MA.4.

## MP Media Protection

### MP.1 Purpose

This records the Level 1 self-assessment of the 7 MP entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### MP.2 How to read this record

**Change since this assessment.** On 17 November 2026 the media protection design was cut from \<Control Implementation Register\> into \<Media Protection Management\>, with each control set out part by part (D-MP-09). Six places were added to the media inventory, and the export folder is checked each working day in place of weekly (D-MP-10). One item was added for gaps this chapter found: PA-121. The findings below are a true record of 6 and 10 November 2026 and are not changed.

The Not applicable statement is counted in the 71 but not as satisfied.

The methods were **Examine** (documents and code) and **Test**: checks P01 to P09 by Test-MediaProtection.ps1 on the tagged v1.0 build on 10 November 2026, with hashes in MANIFEST.md, in the MP evidence, on a throwaway stack. The system owner answered INT-MP-01 to 03 in writing.

**Limit of the current evidence:** the tests show how \<System Name\>'s exports, marking and storage behave in Docker. They are not evidence of how \<Organisation\> stores, moves or sanitises disks and backup media, or of USB blocking.

### MP.3 Executive summary

**Table MP-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, with at least one system gap | 2 | MP-3, MP-4 |
| Other than satisfied, needing only a decision, approval or evidence | 5 | MP-1, MP-2, MP-5, MP-6, MP-7 |

**Table MP-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding and POA&M |
| --- | --- | --- | --- | --- |
| MP-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews outstanding | NC-MP-01; PA-20 |
| MP-2 | Other than satisfied | 4 of 6 | Exports limited to editors (P01); \<Organisation\>'s media access not evidenced | NC-MP-02; EV-MP-01 |
| MP-3 | Other than satisfied | 2 of 4, 1 not applicable | Nothing \<System Name\> produces is marked (P04, P07) | NC-MP-03; PA-87 |
| MP-4 | Other than satisfied | 6 of 11 | Export copies left unencrypted on the server (P02 to P06, P09) | NC-MP-04; PA-86, PA-52 |
| MP-5 | Other than satisfied | 3 of 9 | Physical transport by exception, not evidenced; backups not yet encrypted | NC-MP-05; PA-64, EV-MP-01 |
| MP-6 | Other than satisfied | 6 of 10 | Methods set; sanitising not evidenced | NC-MP-06; EV-MP-02 |
| MP-7 | Other than satisfied | 4 of 6 | USB blocking not evidenced | NC-MP-07; EV-MP-03 |

Of the CSS 71 statements, 46 are satisfied, 1 is not applicable, 7 await a decision or approval, 3 show a gap in the system and 14 await evidence from the VMs or \<Organisation\>.

The approach is approved and the media are now all listed. The gaps are in \<System Name\> itself: export copies left unencrypted on the server, and no marking on anything it shows or produces.

### MP.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 10 November 2026 where the basis says so.

**Table MP-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| MP-01\_ODP\[01\] | Who receives the policy is defined | S | \<Media Protection Management\> |
| MP-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Media Protection Management\> |
| MP-01\_ODP\[03\] | Policy level is selected | S | \<Media Protection Management\> |
| MP-01\_ODP\[04\] | Managing official is defined | S | System owner |
| MP-01\_ODP\[05\] | Policy review frequency is defined | S | \<Media Protection Management\> |
| MP-01\_ODP\[06\] | Policy review events are defined | S | \<Media Protection Management\> |
| MP-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Media Protection Management\> |
| MP-01\_ODP\[08\] | Procedures review events are defined | S | \<Media Protection Management\> |
| MP-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-MP-01); version \<ver\> awaits re-approval (D-MP-07) |
| MP-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| MP-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-MP-08) |
| MP-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| MP-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section MP.1 |
| MP-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section MP.1 |
| MP-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section MP.5 |
| MP-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section MP.5 |
| MP-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section MP.6 |
| MP-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section MP.6 |
| MP-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section MP.6 |
| MP-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 10 November 2026, as confirmed by the system owner |
| MP-01b. | Official is designated | S | \[Name\] is the system owner |
| MP-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| MP-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 10 November 2026 after the MP pack review (D-MP-06) |
| MP-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| MP-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 10 November 2026 (D-MP-08) |
| MP-02\_ODP\[01\] | Digital media are defined | S | \<Media Protection Management\>, section 3.2 (D-MP-P02) |
| MP-02\_ODP\[02\] | Who may access them is defined | S | \<Organisation\>'s corporate parameter values (D-MP-P02) |
| MP-02\_ODP\[03\] | Non-digital media are defined | S | \<Media Protection Management\> |
| MP-02\_ODP\[04\] | Who may access them is defined | S | \<Media Protection Management\> |
| MP-02\[01\] | Digital media access is restricted | O-E | Exports limited to editors (P01); disks, volumes and backups with \<Organisation\> (EV-MP-01) |
| MP-02\[02\] | Non-digital media access is restricted | O-D | PRO-MP-1 approved; not yet in use |
| MP-03\_ODP\[01\] | Exempt media are defined | S | \<Media Protection Management\>: none |
| MP-03\_ODP\[02\] | Controlled areas are defined | S | \<Media Protection Management\> |
| MP-03a. | Media are marked | O-G | Nothing \<System Name\> shows or produces is marked: exports (P04) and viewer and printouts (P07); manual marking only (PA-87) |
| MP-03b. | Exempt media stay in controlled areas | N/A | No media is exempt |
| MP-04\_ODP\[01\] | Digital media controlled are defined | S | \<Media Protection Management\> |
| MP-04\_ODP\[02\] | Non-digital media controlled are defined | S | \<Media Protection Management\> |
| MP-04\_ODP\[03\] | Digital media stored are defined | S | \<Media Protection Management\> |
| MP-04\_ODP\[04\] | Non-digital media stored are defined | S | \<Media Protection Management\> |
| MP-04\_ODP\[05\] | Controlled areas are defined | S | \<Media Protection Management\> |
| MP-04\_ODP\[06\] | Controlled areas are defined | S | \<Media Protection Management\> |
| MP-04a.\[01\] | Digital media are physically controlled | O-E | \<Organisation\> (EV-MP-01) |
| MP-04a.\[02\] | Non-digital media are physically controlled | O-D | PRO-MP-1 approved; not yet in use |
| MP-04a.\[03\] | Digital media are securely stored | O-G | Export copies are left unencrypted on the application server after download and after a restart (P02, P05, P06, P09; PA-86) |
| MP-04a.\[04\] | Non-digital media are securely stored | O-D | PRO-MP-1 approved; not yet in use |
| MP-04b. | Media are protected until destroyed | O-G | Export copies stay on the server indefinitely if the API restarts before the in-memory clean-up runs (P06; PA-86) |
| MP-05\_ODP\[01\] | Media transported are defined | S | \<Media Protection Management\>: physical transport only by exception (D-MP-P02) |
| MP-05\_ODP\[02\] | Protection is defined | S | \<Media Protection Management\> |
| MP-05\_ODP\[03\] | Control is defined | S | \<Media Protection Management\> (D-MP-P02) |
| MP-05a.\[01\] | Media are protected in transport | O-E | \<Organisation\> (EV-MP-01) |
| MP-05a.\[02\] | Media are controlled in transport | O-E | \<Organisation\> (EV-MP-01) |
| MP-05b. | Accountability is kept | O-E | \<Organisation\> (EV-MP-01) |
| MP-05c. | Transport is documented | O-E | \<Organisation\> (EV-MP-01) |
| MP-05d.\[01\] | Authorised people are identified | O-E | \<Organisation\> (EV-MP-01) |
| MP-05d.\[02\] | Transport is limited to them | O-E | \<Organisation\> (EV-MP-01) |
| MP-06\_ODP\[01\] | Media for disposal are defined | S | \<Media Protection Management\> |
| MP-06\_ODP\[02\] | Media for release are defined | S | \<Media Protection Management\> |
| MP-06\_ODP\[03\] | Media for reuse are defined | S | \<Media Protection Management\> |
| MP-06\_ODP\[04\] | Technique for disposal is defined | S | \<Media Protection Management\>, section 3.6: CSS and IEEE 2883-2022 (D-MP-P02) |
| MP-06\_ODP\[05\] | Technique for release is defined | S | \<Media Protection Management\>, section 3.6 (D-MP-P02) |
| MP-06\_ODP\[06\] | Technique for reuse is defined | S | \<Media Protection Management\>, section 3.6 (D-MP-P02) |
| MP-06a.\[01\] | Media are sanitised before disposal | O-E | \<Organisation\> (EV-MP-02) |
| MP-06a.\[02\] | Media are sanitised before release | O-E | \<Organisation\> (EV-MP-02) |
| MP-06a.\[03\] | Media are sanitised before reuse | O-E | \<Organisation\> (EV-MP-02) |
| MP-06b. | Mechanisms match the classification | O-E | Methods by media type set in \<Media Protection Management\>, section 3.6, including cryptographic erase; not evidenced (EV-MP-02, PA-52) |
| MP-07\_ODP\[01\] | Media types are defined | S | \<Media Protection Management\> |
| MP-07\_ODP\[02\] | Restrict or prohibit is selected | S | \<Media Protection Management\> |
| MP-07\_ODP\[03\] | Systems are defined | S | \<Media Protection Management\> |
| MP-07\_ODP\[04\] | Controls are defined | S | \<Media Protection Management\> |
| MP-07a. | Use of the media is restricted | O-E | \<Organisation\> (EV-AC-17, EV-MP-03) |
| MP-07b. | Portable devices with no owner are prohibited | O-E | Rule R11 and PRO-MP-4 written; \<Organisation\>'s device control not evidenced (EV-MP-03) |

### MP.5 Assessment plan

**Table MP-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 7 MP entries in the CSS Moderate baseline, with 71 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0), with CSS as the reference for sanitising |
| Dates | 6 November 2026; updated on 10 November 2026 after the MP pack review |
| Site | One PC, using a separate throwaway Docker stack with sample data. The VMs are not built |
| Examine | \<Policy\> (MP), \<Procedures\> (MP) and the MP chapter of \<Control Implementation Register\> at \<ver\>, now in \<Media Protection Management\>; TPL-13; SyOps A28, A30 to A35 and section 4.8; the export code and UI application pages. Depth: focused. Coverage: focused |
| Test | P01 to P09 by Test-MediaProtection.ps1 on 10 November 2026 (mp-test-results-2026-11-10-v1.0.csv and MANIFEST.md). Depth: focused. Coverage: focused |
| Interview | System owner's written answers only. The database administrator, a sample of users and \<Organisation\>'s IT service desk remain |
| Previous results reused | AC check T62 (export ownership); CP check R02 (unencrypted backup); AU check A38 (personal data in the log) |
| Boundary | \<System Name\>'s exports, marking, users' copies and printouts. Storage, transport and sanitising of physical disks and backup media, and device control, are inherited from \<Organisation\> |
| Order of assessment | A, the media inventory (MP-2, MP-4); B, export copies (MP-4, MP-6); C, marking (MP-3); D, sanitising (MP-6); E, transport (MP-5); F, portable storage (MP-7); G, policy (MP-1). The inventory comes first because every other result depends on it |
| Needed from \<Organisation\> | EV-MP-01 to EV-MP-03 in \<Evidence Requests\>: media handling, sanitising certificates and device control |
| Evidence retained | The MP evidence, with its manifest; \<Media Protection Management\>, sections 3.2 to 3.6 |

For the Level 2 assessment, the assessor should repeat the tests on the VMs, examine the export folder and a sample of users' devices, examine TPL-13 records and \<Organisation\>'s certificates, test USB blocking, hold the interviews and re-determine every statement in section MP.4.

## PE Physical and Environmental Protection

### PE.1 Purpose

This records the Level 1 self-assessment of the 18 PE entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### PE.2 How to read this record

**Change since this assessment.** On 17 November 2026 the physical and environmental protection design was cut from \<Control Implementation Register\> into \<Physical and Environmental Protection Management\>, with each control set out part by part (D-PE-11). A SOC 2 report is now accepted only if it covers the availability criteria as well as physical access, the emergency shutoff must be guarded, and a physical incident is to be reported within 24 hours (D-PE-12). Both data centres are inspected at Level 2. One item was added for the gaps this chapter found: PA-122. The findings below are a true record of 6 and 10 November 2026 and are not changed.

The method was **Examine** (documents). Fifteen of the 18 controls are inherited from \<Organisation\>'s data centres, and the inheritance matrix in \<Physical and Environmental Protection Management\>, section 3.3, shows the evidence that closes each one. Nothing more in PE can be tested in Docker: \<System Name\>'s own part, the screen lock, was tested under AC-11, and output marking under MP-3. No site has been visited.

**Limit of the current evidence:** none of \<Organisation\>'s evidence (EV-PE-01 to EV-PE-05) has been received, so every inherited statement stays O-E.

### PE.3 Executive summary

**Table PE-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, with at least one system gap | 0 | None |
| Other than satisfied, needing only a decision, approval or evidence | 18 | All PE controls |

**Table PE-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| PE-1 | Other than satisfied | 21 of 25 | Not yet shared; re-approval (D-PE-09) and first scheduled reviews outstanding | NC-PE-01 |
| PE-2 | Other than satisfied | 1 of 7 | Inherited; not evidenced | NC-PE-02 |
| PE-3 | Other than satisfied | 10 of 22 | Inherited; not evidenced | NC-PE-03 |
| PE-4 | Other than satisfied | 2 of 3 | Inherited; not evidenced | NC-PE-04 |
| PE-5 | Other than satisfied | 1 of 2 | Managed printers not listed or evidenced | NC-PE-05 |
| PE-6 | Other than satisfied | 2 of 7 | Inherited; not evidenced | NC-PE-06 |
| PE-6(1) | Other than satisfied | 0 of 2 | Inherited; not evidenced | NC-PE-07 |
| PE-8 | Other than satisfied | 3 of 6 | Inherited; not evidenced | NC-PE-08 |
| PE-9 | Other than satisfied | 0 of 2 | Inherited; not evidenced | NC-PE-09 |
| PE-10 | Other than satisfied | 2 of 5 | Inherited; not evidenced | NC-PE-10 |
| PE-11 | Other than satisfied | 1 of 2 | Inherited; not evidenced | NC-PE-11 |
| PE-12 | Other than satisfied | 0 of 4 | Inherited; not evidenced | NC-PE-12 |
| PE-13 | Other than satisfied | 0 of 6 | Inherited; not evidenced | NC-PE-13 |
| PE-13(1) | Other than satisfied | 2 of 5 | Inherited; not evidenced | NC-PE-14 |
| PE-14 | Other than satisfied | 4 of 6 | Inherited; not evidenced | NC-PE-15 |
| PE-15 | Other than satisfied | 0 of 4 | Inherited; not evidenced | NC-PE-16 |
| PE-16 | Other than satisfied | 2 of 7 | Inherited; not evidenced | NC-PE-17 |
| PE-17 | Other than satisfied | 3 of 6 | Yearly check not yet held; contacts are placeholders | NC-PE-18 |

Of the CSS 121 statements, 54 are satisfied, 6 await a decision or approval, none shows a gap in the system and 61 await evidence from \<Organisation\>.

The approach is approved and every inherited control is mapped to the evidence that would close it. Nothing can move further until \<Organisation\>'s certification or facility evidence arrives, and the site is inspected at Level 2.

### PE.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 10 November 2026 where the basis says so. Every inherited statement applies to the data centre and the second site alike.

**Table PE-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| PE-01\_ODP\[01\] | Who receives the policy is defined | S | \<Physical and Environmental Protection Management\> |
| PE-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Physical and Environmental Protection Management\> |
| PE-01\_ODP\[03\] | Policy level is selected | S | \<Physical and Environmental Protection Management\> |
| PE-01\_ODP\[04\] | Managing official is defined | S | System owner |
| PE-01\_ODP\[05\] | Policy review frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-01\_ODP\[06\] | Policy review events are defined | S | \<Physical and Environmental Protection Management\> |
| PE-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-01\_ODP\[08\] | Procedures review events are defined | S | \<Physical and Environmental Protection Management\> |
| PE-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-PE-01); version \<ver\> awaits re-approval (D-PE-09) |
| PE-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| PE-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-PE-10) |
| PE-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| PE-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section PE.1 |
| PE-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section PE.1 |
| PE-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section PE.5 |
| PE-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section PE.5 |
| PE-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section PE.6 |
| PE-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section PE.6 |
| PE-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section PE.6 |
| PE-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 10 November 2026, as confirmed by the system owner |
| PE-01b. | Official is designated | S | \[Name\] is the system owner |
| PE-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| PE-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 10 November 2026 after the PE pack review (D-PE-08) |
| PE-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| PE-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 10 November 2026 (D-PE-10) |
| PE-02\_ODP | Review frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-02a.\[01\] | An access list is developed | O-E | \<Organisation\> (EV-PE-01) |
| PE-02a.\[02\] | The list is approved | O-E | \<Organisation\> (EV-PE-01) |
| PE-02a.\[03\] | The list is maintained | O-E | \<Organisation\> (EV-PE-01) |
| PE-02b. | Credentials are issued | O-E | \<Organisation\> (EV-PE-01) |
| PE-02c. | The list is reviewed | O-E | \<Organisation\> (EV-PE-01) |
| PE-02d. | People are removed when no longer needed | O-E | \<Organisation\> (EV-PE-01) |
| PE-03\_ODP\[01\] | Entry and exit points are defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[02\] | How entry is controlled is selected | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[03\] | Systems or devices are defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[04\] | Logged points are defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[05\] | Controls on public areas are defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[06\] | Visitor circumstances are defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[07\] | Access devices are defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[08\] | Inventory frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[09\] | Combination frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-03\_ODP\[10\] | Key frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-03a.01 | Authorisation is verified at entry | O-E | \<Organisation\> (EV-PE-01) |
| PE-03a.02 | Entry and exit are controlled | O-E | \<Organisation\> (EV-PE-01) |
| PE-03b. | Access logs are kept | O-E | \<Organisation\> (EV-PE-01) |
| PE-03c. | Public areas are controlled | O-E | \<Organisation\> (EV-PE-01) |
| PE-03d.\[01\] | Visitors are escorted | O-E | \<Organisation\> (EV-PE-01) |
| PE-03d.\[02\] | Visitor activity is controlled | O-E | \<Organisation\> (EV-PE-01) |
| PE-03e.\[01\] | Keys are secured | O-E | \<Organisation\> (EV-PE-01) |
| PE-03e.\[02\] | Combinations are secured | O-E | \<Organisation\> (EV-PE-01) |
| PE-03e.\[03\] | Other access devices are secured | O-E | \<Organisation\> (EV-PE-01) |
| PE-03f. | Access devices are inventoried | O-E | \<Organisation\> (EV-PE-01) |
| PE-03g.\[01\] | Combinations are changed | O-E | \<Organisation\> (EV-PE-01) |
| PE-03g.\[02\] | Keys are changed | O-E | \<Organisation\> (EV-PE-01) |
| PE-04\_ODP\[01\] | Lines are defined | S | \<Physical and Environmental Protection Management\> |
| PE-04\_ODP\[02\] | Controls are defined | S | \<Physical and Environmental Protection Management\> |
| PE-04 | Access to lines is controlled | O-E | \<Organisation\> (EV-PE-01) |
| PE-05\_ODP | Output devices are defined | S | \<Physical and Environmental Protection Management\>: managed printers with secure release, and screens (D-PE-P02) |
| PE-05 | Access to output is controlled | O-E | Managed printers with secure release not yet listed or evidenced (EV-PE-05); \<System Name\> locks the page after 25 minutes (AC-11) |
| PE-06\_ODP\[01\] | Review frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-06\_ODP\[02\] | Review events are defined | S | \<Physical and Environmental Protection Management\> |
| PE-06a. | Access is monitored | O-E | \<Organisation\> (EV-PE-01) |
| PE-06b.\[01\] | Logs are reviewed at the set frequency | O-E | \<Organisation\> (EV-PE-01) |
| PE-06b.\[02\] | Logs are reviewed after set events | O-E | \<Organisation\> (EV-PE-01) |
| PE-06c.\[01\] | Review results go to incident response | O-E | Physical incident playbook in \<Incident Response Management\> \<ver\>; \<Organisation\>'s reporting not evidenced (EV-PE-01) |
| PE-06c.\[02\] | Investigation results go to incident response | O-E | Physical incident playbook in \<Incident Response Management\> \<ver\>; \<Organisation\>'s reporting not evidenced (EV-PE-01) |
| PE-06(01)\[01\] | Intrusion alarms are used | O-E | \<Organisation\> (EV-PE-01) |
| PE-06(01)\[02\] | Surveillance equipment is used | O-E | \<Organisation\> (EV-PE-01) |
| PE-08\_ODP\[01\] | Retention is defined | S | \<Physical and Environmental Protection Management\> |
| PE-08\_ODP\[02\] | Review frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-08\_ODP\[03\] | Who gets anomalies is defined | S | \<Physical and Environmental Protection Management\> |
| PE-08a. | Visitor records are kept | O-E | \<Organisation\> (EV-PE-01) |
| PE-08b. | Visitor records are reviewed | O-E | \<Organisation\> (EV-PE-01) |
| PE-08c. | Anomalies are reported | O-E | \<Organisation\> (EV-PE-01) |
| PE-09\[01\] | Power equipment is protected | O-E | \<Organisation\> (EV-PE-02) |
| PE-09\[02\] | Power cabling is protected | O-E | \<Organisation\> (EV-PE-02) |
| PE-10\_ODP\[01\] | What can be shut off is defined | S | \<Physical and Environmental Protection Management\> |
| PE-10\_ODP\[02\] | Switch location is defined | S | \<Physical and Environmental Protection Management\> |
| PE-10a. | Power can be shut off in an emergency | O-E | \<Organisation\> (EV-PE-02) |
| PE-10b. | Switches are safely reachable | O-E | \<Organisation\> (EV-PE-02) |
| PE-10c. | Shutoff is protected from misuse | O-E | \<Organisation\> (EV-PE-02) |
| PE-11\_ODP | What backup power allows is selected | S | \<Physical and Environmental Protection Management\> |
| PE-11 | An uninterruptible supply is provided | O-E | \<Organisation\> (EV-PE-02) |
| PE-12\[01\] | Emergency lighting activates in an outage | O-E | \<Organisation\> (EV-PE-02) |
| PE-12\[02\] | Emergency lighting activates in a disruption | O-E | \<Organisation\> (EV-PE-02) |
| PE-12\[03\] | Lighting covers emergency exits | O-E | \<Organisation\> (EV-PE-02) |
| PE-12\[04\] | Lighting covers evacuation routes | O-E | \<Organisation\> (EV-PE-02) |
| PE-13\[01\] | Fire detection is used | O-E | \<Organisation\> (EV-PE-03) |
| PE-13\[02\] | Detection has its own power | O-E | \<Organisation\> (EV-PE-03) |
| PE-13\[03\] | Detection is maintained | O-E | \<Organisation\> (EV-PE-03) |
| PE-13\[04\] | Fire suppression is used | O-E | \<Organisation\> (EV-PE-03) |
| PE-13\[05\] | Suppression has its own power | O-E | \<Organisation\> (EV-PE-03) |
| PE-13\[06\] | Suppression is maintained | O-E | \<Organisation\> (EV-PE-03) |
| PE-13(01)\_ODP\[01\] | Who is notified is defined | S | \<Physical and Environmental Protection Management\> |
| PE-13(01)\_ODP\[02\] | Responders are defined | S | \<Physical and Environmental Protection Management\> |
| PE-13(01)\[01\] | Detection activates automatically | O-E | \<Organisation\> (EV-PE-03) |
| PE-13(01)\[02\] | Detection notifies the named people | O-E | \<Organisation\> (EV-PE-03) |
| PE-13(01)\[03\] | Detection notifies responders | O-E | \<Organisation\> (EV-PE-03) |
| PE-14\_ODP\[01\] | Levels are selected | S | \<Physical and Environmental Protection Management\> |
| PE-14\_ODP\[02\] | Controls are defined | S | \<Physical and Environmental Protection Management\> |
| PE-14\_ODP\[03\] | Acceptable levels are defined | S | \<Physical and Environmental Protection Management\>: the ASHRAE TC 9.9 recommended envelope (D-PE-P02) |
| PE-14\_ODP\[04\] | Monitoring frequency is defined | S | \<Physical and Environmental Protection Management\> |
| PE-14a. | Levels are maintained | O-E | \<Organisation\> (EV-PE-03) |
| PE-14b. | Levels are monitored | O-E | \<Organisation\> (EV-PE-03) |
| PE-15\[01\] | Shutoff valves protect against leaks | O-E | \<Organisation\> (EV-PE-03) |
| PE-15\[02\] | Valves are accessible | O-E | \<Organisation\> (EV-PE-03) |
| PE-15\[03\] | Valves work | O-E | \<Organisation\> (EV-PE-03) |
| PE-15\[04\] | Key people know about them | O-E | \<Organisation\> (EV-PE-03) |
| PE-16\_ODP\[01\] | Items entering are defined | S | \<Physical and Environmental Protection Management\> |
| PE-16\_ODP\[02\] | Items leaving are defined | S | \<Physical and Environmental Protection Management\> |
| PE-16a.\[01\] | Items entering are authorised | O-E | \<Organisation\> (EV-PE-04) |
| PE-16a.\[02\] | Items entering are controlled | O-E | \<Organisation\> (EV-PE-04) |
| PE-16a.\[03\] | Items leaving are authorised | O-E | \<Organisation\> (EV-PE-04) |
| PE-16a.\[04\] | Items leaving are controlled | O-E | \<Organisation\> (EV-PE-04) |
| PE-16b. | Records are kept | O-E | \<Organisation\> (EV-PE-04) |
| PE-17\_ODP\[01\] | Work sites are defined | S | \<Physical and Environmental Protection Management\> |
| PE-17\_ODP\[02\] | Controls are defined | S | \<Physical and Environmental Protection Management\> |
| PE-17a. | Controls at work sites are determined | S | \<Physical and Environmental Protection Management\>, approved (D-PE-03) |
| PE-17b. | Those controls are used | O-E | \<Organisation\> (EV-PE-05) |
| PE-17c. | Their effectiveness is assessed | O-D | Yearly checklist (PRO-PE-4, C30, TPL-4); not yet assessed |
| PE-17d. | People can reach security staff | O-D | Security officer named in \<Security Operating Procedures\>, section 6; the contact details in \<Roles and Responsibilities\>, section 6, are still placeholders |

### PE.5 Assessment plan

**Table PE-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 18 PE entries in the CSS Moderate baseline, with 121 determination statements, at the data centre, the second site, the offices and homes |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 10 November 2026 after the PE pack review |
| Site | No site visited. The data centre and second site are \[to be named\] in \<Physical and Environmental Protection Management\>, section 3.2 |
| Examine | \<Policy\> (PE), \<Procedures\> (PE) and the PE chapter of \<Control Implementation Register\> at \<ver\>, now in \<Physical and Environmental Protection Management\>, with the inheritance matrix; SyOps A33, A36 to A38; \<Incident Response Management\>, section 3.9. Depth: focused. Coverage: focused |
| Test | None for PE. The screen lock was tested under AC-11, and output marking under MP-3 (P07) |
| Interview | System owner's written answers only. The security officer, a sample of home workers and \<Organisation\>'s facilities contact remain |
| Site inspection | Once at Level 2, using TPL-20, by the independent assessor or \<Organisation\>'s auditor (PRO-PE-5) |
| Previous results reused | AC checks of the screen lock and sign-out (AC-11, AC-12); MP check P07 (no marking) |
| Boundary | Physical and environmental protection of the data centre and second site is inherited from \<Organisation\>. \<System Name\> provides the policy, the printer and screen rules, home working rules, and incident handling |
| Order of assessment | A, inherited evidence against the matrix (PE-2 to PE-16); B, the site inspection; C, output devices (PE-5); D, home working (PE-17); E, policy (PE-1). The inherited evidence comes first because it closes most statements |
| Needed from \<Organisation\> | EV-PE-01 to EV-PE-05 in \<Evidence Requests\>: first its ISO/IEC 27001 certificate and Statement of Applicability for Annex A.7, or a SOC 2 report, for both sites |
| Evidence retained | \<Physical and Environmental Protection Management\>, sections 3.2 and 3.3; \<Evidence Requests\>; completed TPL-20 |

For the Level 2 assessment, the assessor should examine \<Organisation\>'s certificate, Statement of Applicability or SOC 2 report against the inheritance matrix, inspect the data centre with TPL-20, interview the security officer and a sample of home workers, and re-determine every statement in section PE.4.

## PL Planning

### PL.1 Purpose

This records the Level 1 self-assessment of the 7 PL entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### PL.2 How to read this record

**Change since this assessment.** On 17 November 2026 the planning design was cut from \<Control Implementation Register\> into \<Planning Management\>, with each control set out part by part and the two registers (D-PL-12). The plan consistency test has grown from the 12 checks run for this assessment to 24, and the set passes all of them. A draft impact assessment now exists (\<Data Protection Impact Assessment\>), though the privacy risk results are not complete (PA-72). One item was added for gaps this chapter found: PA-123. The findings below are a true record of 6 and 11 November 2026 and are not changed.

The methods were **Examine** (documents) and **Test**. The test is Test-PlanConsistency.ps1, which reads the whole document set and checks that the plans agree with each other and with the assessments (checks L01 to L12). It runs on the documents only, with no Docker stack. The results and their hashes are in the PL evidence. No interviews have been held.

The plans are compared with CSS (June 2026), which sets out what a system plan contains, and how its approval, reviews and changes are recorded.

### PL.3 Executive summary

**Table PL-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 3 | PL-4(1), PL-10, PL-11 |
| Other than satisfied, with at least one system gap | 0 | None |
| Other than satisfied, needing only a decision, approval or evidence | 4 | PL-1, PL-2, PL-4, PL-8 |

**Table PL-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| PL-1 | Other than satisfied | 21 of 25 | Not yet shared; re-approval (D-PL-07) and first scheduled reviews outstanding | NC-PL-01 |
| PL-2 | Other than satisfied | 31 of 41 | Not yet shared or in the restricted store; privacy risk results and \<Organisation\>'s architecture outstanding | NC-PL-02, NC-PL-06 |
| PL-4 | Other than satisfied | 5 of 8 | Rules approved; none signed yet | NC-PL-03 |
| PL-4(1) | Satisfied | 3 of 3 | Rules A43 and A44 | NC-PL-04 |
| PL-8 | Other than satisfied | 12 of 14 | First yearly review not due; no procurement yet | NC-PL-05 |
| PL-10 | Satisfied | 1 of 1 | Moderate, approved | Met |
| PL-11 | Satisfied | 1 of 1 | Tailoring register 1.0 | Met |

Of the CSS 93 statements, 74 are satisfied, 17 await a decision or approval, none shows a gap in the system and 2 await evidence from \<Organisation\>.

The plans are complete and agree with each other: the plan-consistency test passed all 12 checks after this review's corrections. What remains is to sign the rules, share the plans, move them to the restricted store, and let the first yearly reviews fall due.

### PL.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 11 November 2026 where the basis says so.

**Table PL-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| PL-01\_ODP\[01\] | Who receives the policy is defined | S | \<Planning Management\> |
| PL-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Planning Management\> |
| PL-01\_ODP\[03\] | Policy level is selected | S | \<Planning Management\> |
| PL-01\_ODP\[04\] | Managing official is defined | S | System owner |
| PL-01\_ODP\[05\] | Policy review frequency is defined | S | \<Planning Management\> |
| PL-01\_ODP\[06\] | Policy review events are defined | S | \<Planning Management\> |
| PL-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Planning Management\> |
| PL-01\_ODP\[08\] | Procedures review events are defined | S | \<Planning Management\> |
| PL-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-PL-01); version \<ver\> awaits re-approval (D-PL-07) |
| PL-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| PL-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-PL-08) |
| PL-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| PL-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section PL.1 |
| PL-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section PL.1 |
| PL-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section PL.5 |
| PL-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section PL.5 |
| PL-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section PL.6 |
| PL-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section PL.6 |
| PL-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section PL.6 |
| PL-01a.01(b) | Policy is consistent with laws and standards | S | Reviewed by the legal adviser on 11 November 2026, as confirmed by the system owner |
| PL-01b. | Official is designated | S | \[Name\] is the system owner |
| PL-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| PL-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 11 November 2026 after the PL pack review (D-PL-06) |
| PL-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| PL-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 11 November 2026 (D-PL-08) |
| PL-02\_ODP\[01\] | Who planning is coordinated with is defined | S | \<Planning Management\> |
| PL-02\_ODP\[02\] | Who receives copies is defined | S | \<Planning Management\> |
| PL-02\_ODP\[03\] | Review frequency is defined | S | \<Planning Management\> |
| PL-02a.01\[01\] | Security plan fits the enterprise architecture | O-E | \<Organisation\>'s architecture not seen (EV-PL-01) |
| PL-02a.01\[02\] | Privacy plan fits the enterprise architecture | O-E | \<Organisation\>'s architecture not seen (EV-PL-01) |
| PL-02a.02\[01\] | Security plan defines the boundary | S | \<System Security Plan\>, section 3.1; \<Security Architecture\>, section 2 |
| PL-02a.02\[02\] | Privacy plan defines the boundary | S | \<Privacy Plan\>, section 2 |
| PL-02a.03\[01\] | Security plan describes the operational context | S | \<System Security Plan\>, \<Concept of Operations\> |
| PL-02a.03\[02\] | Privacy plan describes the operational context | S | \<Privacy Plan\>, section 2 |
| PL-02a.04\[01\] | Security plan identifies people in roles | S | \<System Security Plan\>, \<Roles and Responsibilities\> |
| PL-02a.04\[02\] | Privacy plan identifies people in roles | S | \<Privacy Plan\>, section 3 |
| PL-02a.05\[01\] | Security plan identifies information types | S | \<System Security Plan\>, Table 4 |
| PL-02a.05\[02\] | Privacy plan identifies information types | S | \<Privacy Plan\>, section 4 |
| PL-02a.06\[01\] | Security plan gives the categorisation | S | \<System Security Plan\>, approved by \[Name\] |
| PL-02a.06\[02\] | Privacy plan gives the categorisation | S | \<Privacy Plan\>, section 4 |
| PL-02a.07\[01\] | Security plan describes threats | S | \<System Security Plan\>, \<Risk List\> |
| PL-02a.07\[02\] | Privacy plan describes threats | S | \<Privacy Plan\>, section 5 |
| PL-02a.08\[01\] | Security plan gives privacy risk results | O-D | No impact assessment yet (PA-72) |
| PL-02a.08\[02\] | Privacy plan gives privacy risk results | O-D | No impact assessment yet (PA-72) |
| PL-02a.09\[01\] | Security plan describes the environment | S | \<System Security Plan\>, \<Security Architecture\> |
| PL-02a.09\[02\] | Privacy plan describes the environment | S | \<Privacy Plan\>, section 2 |
| PL-02a.10\[01\] | Security plan gives requirements | S | \<System Security Plan\> |
| PL-02a.10\[02\] | Privacy plan gives requirements | S | \<Privacy Plan\>, section 6 |
| PL-02a.11\[01\] | Security plan identifies baselines and overlays | S | \<System Security Plan\>, Moderate |
| PL-02a.11\[02\] | Privacy plan identifies baselines and overlays | S | \<Privacy Plan\>, section 6 |
| PL-02a.12\[01\] | Security plan describes controls | S | \<System Security Plan\>, section 7, one row for each control |
| PL-02a.12\[02\] | Privacy plan describes controls | S | \<Privacy Plan\>, section 6; \<System Security Plan\>, section 7.14 |
| PL-02a.13\[01\] | Security plan includes risk determinations | S | \<Risk List\>, \<Decision Register\> |
| PL-02a.13\[02\] | Privacy plan includes risk determinations | S | \<Privacy Plan\>, section 5; \<Decision Register\> |
| PL-02a.14\[01\] | Security plan includes activities to coordinate | S | \<Security Operating Procedures\>, Table 5, \<Plan of Action and Milestones\> |
| PL-02a.14\[02\] | Privacy plan includes activities to coordinate | S | \<Privacy Plan\>, section 7 |
| PL-02a.15\[01\] | Security plan is reviewed and approved | S | Approved by the system owner and accepted by \[Name\] as an accurate record at version \<ver\> of the plan; later versions await his acceptance (D-GEN-20); the Head of Cyber's concurrence requested (D-PL-06) |
| PL-02a.15\[02\] | Privacy plan is reviewed and approved | S | Approved by \[Name\] and \[Name\] (D-PT-05) |
| PL-02b.\[01\] | Copies are distributed | O-D | Not yet shared; each issue to be recorded in the plan review record (PRO-PL-2) |
| PL-02b.\[02\] | Changes are communicated | O-D | Not yet shared; each issue to be recorded in the plan review record (PRO-PL-2) |
| PL-02c. | Plans are reviewed | O-D | First yearly review not yet due; plan review record started on 11 November 2026 |
| PL-02d.\[01\] | Plans are updated for changes | S | \<System Security Plan\> change record and plan review record |
| PL-02d.\[02\] | Plans are updated for problems in use | O-D | Not yet in use |
| PL-02d.\[03\] | Plans are updated for assessment problems | S | \<System Security Plan\> change record; Test-PlanConsistency.ps1 (L01 to L12) run on 11 November 2026 |
| PL-02e.\[01\] | Plans are protected from disclosure | O-D | Not yet in the restricted store. Held on the system owner's computer, where the code repository has ignored them since 12 November 2026 (NC-PL-06, PA-88) |
| PL-02e.\[02\] | Plans are protected from change | O-D | Not yet in the restricted store. Every change has been recorded in a private local repository since 12 November 2026, with a manifest of hashes for each issue (NC-PL-06, PA-88) |
| PL-04\_ODP\[01\] | Review frequency is defined | S | \<Planning Management\> |
| PL-04\_ODP\[02\] | When people re-sign is selected | S | \<Planning Management\> (D-PL-P02) |
| PL-04\_ODP\[03\] | Re-sign frequency is defined | S | \<Planning Management\> |
| PL-04a.\[01\] | Security rules are established | S | \<Security Operating Procedures\> \<ver\>, Parts A and B |
| PL-04a.\[02\] | Privacy rules are established | S | \<Security Operating Procedures\> \<ver\>, section 2.5, rules A23 to A29 |
| PL-04b. | People acknowledge before access | O-D | TPL-21 and the register of signatures ready (\<Planning Management\>, section 3.5); none signed |
| PL-04c. | Rules are reviewed | O-D | First review not yet due |
| PL-04d. | People re-sign | O-D | None signed yet; signing again after a material change (D-PL-P02) |
| PL-04(01)(a) | Rules restrict social media and external sites | S | \<Security Operating Procedures\> \<ver\>, rule A43 |
| PL-04(01)(b) | Rules restrict posting information | S | \<Security Operating Procedures\> \<ver\>, rules A25 and A43 |
| PL-04(01)(c) | Rules restrict using work credentials | S | \<Security Operating Procedures\> \<ver\>, rule A44 |
| PL-08\_ODP | Review frequency is defined | S | \<Planning Management\> |
| PL-08a.01 | Security architecture states requirements and approach | S | \<Security Architecture\> \<ver\>, section 6 |
| PL-08a.02 | Privacy architecture states requirements and approach | S | \<Privacy Plan\>, section 8 |
| PL-08a.03\[01\] | Security architecture fits the enterprise | S | \<Security Architecture\>, sections 4 and 6.3 |
| PL-08a.03\[02\] | Privacy architecture fits the enterprise | S | \<Privacy Plan\>, section 8 |
| PL-08a.04\[01\] | Security architecture states assumptions | S | \<Security Architecture\>, section 6.6 |
| PL-08a.04\[02\] | Privacy architecture states assumptions | S | \<Privacy Plan\>, section 8 |
| PL-08b. | Architecture is reviewed | O-D | First review not yet due |
| PL-08c.\[01\] | Changes are in the security plan | S | \<System Security Plan\>, sections 3 and 4 |
| PL-08c.\[02\] | Changes are in the privacy plan | S | \<Privacy Plan\>, section 8 |
| PL-08c.\[03\] | Changes are in the Concept of Operations | S | \<Concept of Operations\> |
| PL-08c.\[04\] | Changes are in the criticality analysis | S | Critical components in \<Risk Assessment Management\>, section 3.9; changes carried there by PRO-PL-5 |
| PL-08c.\[05\] | Changes are in procedures | S | Each family's procedures; PRO-PL-5 |
| PL-08c.\[06\] | Changes are in procurements | O-D | PRO-SA-3 approved; no procurement yet |
| PL-10 | A baseline is selected | S | Moderate, approved by \[Name\] (D-GEN-06) |
| PL-11 | The baseline is tailored | S | \<Tailoring Register\> \<ver\>, approved by the system owner (D-PL-09, D-PM-02) |

### PL.5 Assessment plan

**Table PL-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 7 PL entries in the CSS Moderate baseline, with 93 determination statements, covering every plan in the register in \<Planning Management\>, section 3.2 |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0); plan contents compared with CSS |
| Dates | 6 November 2026; updated on 11 November 2026 after the PL pack review |
| Examine | \<Policy\> (PL) and \<Procedures\> (PL) \<ver\>, the PL chapter of \<Control Implementation Register\> at \<ver\>, now in \<Planning Management\>, \<System Security Plan\>, \<Privacy Plan\>, \<Security Architecture\> \<ver\>, \<Concept of Operations\>, \<Security Operating Procedures\> \<ver\>, \<Tailoring Register\> \<ver\> and \<Risk Assessment Management\>. Depth: focused. Coverage: focused |
| Test | Test-PlanConsistency.ps1, checks L01 to L12, run on the document set before and after this review's corrections (evidence in the PL evidence) |
| Interview | System owner's written answers only. The Head of Cyber, an administrator and a sample of users, on the rules they signed, remain |
| Previous results reused | The privacy plan's approval (D-PT-05); the critical components list from the RA assessment |
| Boundary | Planning is organisational. The only technical element is where the plans are kept (PA-88) |
| Order of assessment | A, the register of plans and the SSP (PL-2); B, the rules and signatures (PL-4, PL-4(1)); C, the architecture (PL-8); D, the baseline and tailoring (PL-10, PL-11); E, policy (PL-1). The SSP comes first because every other family relies on it |
| Needed from \<Organisation\> | EV-PL-01 in \<Evidence Requests\>: the enterprise architecture standards that \<System Name\> must fit, and the hypervisor question (D-PL-11) |
| Evidence retained | the PL evidence (results, README and MANIFEST); the plan review record in \<System Security Plan\>; TPL-21 forms and the register of signatures, once signed |

For the Level 2 assessment, the assessor should run Test-PlanConsistency.ps1 on the issued set, sample signed TPL-21 forms against the register and the access requests, check the restricted store's access list, interview the Head of Cyber and a sample of users, and re-determine every statement in section PL.4.

## PS Personnel Security

### PS.1 Purpose

This records the Level 1 self-assessment of the 9 PS entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### PS.2 How to read this record

**Change since this assessment.** On 17 November 2026 the personnel security design was cut from \<Control Implementation Register\> into \<Personnel Security Management\>, with each control set out part by part (D-PS-10). Since sign-in moved to AD FS (D-AC-23), \<System Name\> holds no accounts: a person's access is their membership of \<System Name\>'s groups, and a leaver's access ends when \<Organisation\> disables their Active Directory account. Members who have not signed in for 90 days are removed each month (D-PS-11). One item was added for the gaps this chapter found: PA-125. The findings below are a true record of 6 and 12 November 2026 and are not changed.

The method was **Examine** (documents). This family has no code to test: the leaver and mover route depends on \<Organisation\>'s Starters/Leavers system, which is not yet connected (PA-32). Nobody has yet been given an account, so no agreement is signed and no record exists. No interviews have been held. Check L17 of Test-PlanConsistency.ps1 confirms that every role has a risk designation (the PL evidence).

### PS.3 Executive summary

**Table PS-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, needing only a decision, approval or evidence | 9 | PS-1, PS-2, PS-3, PS-4, PS-5, PS-6, PS-7, PS-8, PS-9 |

**Table PS-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| PS-1 | Other than satisfied | 21 of 25 | Not yet shared; version \<ver\> of the policy awaits the Head of Cyber and the legal adviser (D-PS-08) | NC-PS-01 |
| PS-2 | Other than satisfied | 2 of 4 | Every role is designated; \<Organisation\>'s screening criteria not seen | NC-PS-02 |
| PS-3 | Other than satisfied | 2 of 5 | \<Organisation\>'s screening not evidenced | NC-PS-03 |
| PS-4 | Other than satisfied | 2 of 7 | Leaver route not built; exit process not evidenced | NC-PS-04 |
| PS-5 | Other than satisfied | 4 of 8 | Mover route not built | NC-PS-05 |
| PS-6 | Other than satisfied | 3 of 6 | Agreements exist; none signed | NC-PS-06 |
| PS-7 | Other than satisfied | 2 of 7 | Contract terms not evidenced | NC-PS-07 |
| PS-8 | Other than satisfied | 2 of 4 | Sanctions process not evidenced | NC-PS-08 |
| PS-9 | Other than satisfied | 0 of 2 | \<System Name\>'s role duties are in \<Roles and Responsibilities\>; \<Organisation\>'s job descriptions not seen | NC-PS-09 |

Of the CSS 68 statements, 38 are satisfied, 17 await a decision or approval, none shows a gap in the system and 13 await evidence from \<Organisation\>.

What \<System Name\> itself decides is now defined: a designation for every role, the minimum screening it expects, the time limits, and the register. What remains is \<Organisation\>'s evidence of its screening, HR and disciplinary processes, the leaver and mover route (PA-32), and the first people signing their agreements.

### PS.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 12 November 2026 unless the basis says otherwise.

**Table PS-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| PS-01\_ODP\[01\] | Who receives the policy is defined | S | \<Organisation\>'s corporate parameter values |
| PS-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Organisation\>'s corporate parameter values |
| PS-01\_ODP\[03\] | Policy level is selected | S | \<Organisation\>'s corporate parameter values |
| PS-01\_ODP\[04\] | Managing official is defined | S | System owner |
| PS-01\_ODP\[05\] | Policy review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| PS-01\_ODP\[06\] | Policy review events are defined | S | \<Organisation\>'s corporate parameter values |
| PS-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| PS-01\_ODP\[08\] | Procedures review events are defined | S | \<Organisation\>'s corporate parameter values |
| PS-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-PS-01); version \<ver\> awaits re-approval (D-PS-08) |
| PS-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| PS-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-PS-09) |
| PS-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| PS-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (PS) \<ver\>, section PS.1 |
| PS-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (PS) \<ver\>, section PS.1 |
| PS-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (PS) \<ver\>, section PS.5 |
| PS-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (PS) \<ver\>, section PS.5 |
| PS-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (PS) \<ver\>, section PS.6 |
| PS-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (PS) \<ver\>, section PS.6 |
| PS-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (PS) \<ver\>, section PS.6 |
| PS-01a.01(b) | Policy is consistent with laws and standards | S | Version \<ver\> legally reviewed on 12 November 2026, as confirmed by the system owner; version \<ver\> goes to the legal adviser with its approval (D-PS-08) |
| PS-01b. | Official is designated | S | \[Name\] is the system owner |
| PS-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| PS-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 12 November 2026 after the whole-set review (D-PS-07) |
| PS-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| PS-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 12 November 2026 (D-PS-09) |
| PS-02\_ODP | Review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| PS-02a. | Positions have a risk designation | S | All 19 roles in \<Roles and Responsibilities\> are designated in \<Personnel Security Management\>, section 3.2 (D-PS-07; check L17) |
| PS-02b. | Screening criteria are set | O-E | Minimum set in \<Personnel Security Management\>, section 3.3; \<Organisation\>'s criteria not seen (EV-PS-01) |
| PS-02c. | Designations are reviewed | O-D | Reviewed and updated on 12 November 2026; first scheduled review not yet due |
| PS-03\_ODP\[01\] | Rescreening conditions are defined | S | \<Organisation\>'s corporate parameter values |
| PS-03\_ODP\[02\] | Rescreening frequency is defined | S | \<Organisation\>'s corporate parameter values |
| PS-03a. | People are screened before access | O-E | \<Organisation\> (EV-PS-01) |
| PS-03b.\[01\] | People are rescreened under the conditions | O-E | \<Organisation\> (EV-PS-01) |
| PS-03b.\[02\] | People are rescreened at the frequency | O-E | \<Organisation\> (EV-PS-01) |
| PS-04\_ODP\[01\] | Time to disable is defined | S | \<Organisation\>'s corporate parameter values |
| PS-04\_ODP\[02\] | Exit interview topics are defined | S | \<Organisation\>'s corporate parameter values |
| PS-04a. | Access is disabled within the time | O-D | PRO-PS-2 \<ver\> approved, with 1 hour for a higher-risk leaver; route not built (PA-32) |
| PS-04b. | Credentials are revoked | O-D | PRO-PS-2 \<ver\> approved; not yet in use |
| PS-04c. | Exit interviews are held | O-E | \<Organisation\> (EV-PS-02) |
| PS-04d. | Equipment is recovered | O-E | \<Organisation\> (EV-PS-02) |
| PS-04e. | Access to information is retained | O-D | PRO-PS-2 \<ver\> approved; not yet in use |
| PS-05\_ODP\[01\] | Transfer actions are defined | S | \<Organisation\>'s corporate parameter values |
| PS-05\_ODP\[02\] | Time to start is defined | S | \<Organisation\>'s corporate parameter values |
| PS-05\_ODP\[03\] | Who is notified is defined | S | \<Organisation\>'s corporate parameter values |
| PS-05\_ODP\[04\] | Time to notify is defined | S | \<Organisation\>'s corporate parameter values |
| PS-05a. | Need for access is reviewed on transfer | O-D | PRO-PS-3 \<ver\> approved; route not built (PA-32) |
| PS-05b. | Actions start within the time | O-D | PRO-PS-3 \<ver\> approved; route not built (PA-32) |
| PS-05c. | Access is changed as needed | O-D | PRO-PS-3 \<ver\> approved; not yet in use |
| PS-05d. | People are notified within the time | O-D | PRO-PS-3 \<ver\> approved; route not built (PA-32) |
| PS-06\_ODP\[01\] | Review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| PS-06\_ODP\[02\] | Re-sign frequency is defined | S | \<Organisation\>'s corporate parameter values |
| PS-06a. | Access agreements exist | S | \<Security Operating Procedures\> \<ver\>, section 9, approved |
| PS-06b. | Agreements are reviewed | O-D | First review not yet due |
| PS-06c.01 | People sign before access | O-D | PRO-PS-1 \<ver\> approved; none signed |
| PS-06c.02 | People re-sign | O-D | None signed yet |
| PS-07\_ODP\[01\] | Who suppliers notify is defined | S | \<Organisation\>'s corporate parameter values |
| PS-07\_ODP\[02\] | Time to notify is defined | S | \<Organisation\>'s corporate parameter values |
| PS-07a. | Requirements are set for external people | O-E | \<Organisation\> (EV-PS-03) |
| PS-07b. | Providers must comply | O-E | \<Organisation\> (EV-PS-03) |
| PS-07c. | Requirements are documented | O-E | \<Organisation\> (EV-PS-03) |
| PS-07d. | Providers must report leavers and movers | O-E | \<Organisation\> (EV-PS-03) |
| PS-07e. | Compliance is monitored | O-D | PRO-PS-5 \<ver\> approved; not yet in use |
| PS-08\_ODP\[01\] | Who is told is defined | S | \<Organisation\>'s corporate parameter values |
| PS-08\_ODP\[02\] | Time to tell them is defined | S | \<Organisation\>'s corporate parameter values |
| PS-08a. | A sanctions process is used | O-E | \<Organisation\> (EV-PS-02) |
| PS-08b. | People are told within the time | O-D | PRO-PS-6 \<ver\> approved; not yet in use |
| PS-09\[01\] | Job descriptions include security duties | O-E | \<Roles and Responsibilities\> \<ver\> states the security duties of each \<System Name\> role; \<Organisation\>'s job descriptions not seen (EV-PS-02) |
| PS-09\[02\] | Job descriptions include privacy duties | O-E | \<Roles and Responsibilities\> \<ver\> states the privacy duties of each \<System Name\> role; \<Organisation\>'s job descriptions not seen (EV-PS-02) |

### PS.5 Assessment plan

**Table PS-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 9 PS entries in the Moderate baseline, with 68 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 12 November 2026 after the whole-set review |
| Examine | \<Policy\> (PS), \<Procedures\> (PS) and the PS chapter of \<Control Implementation Register\> at \<ver\>, now in \<Personnel Security Management\>; \<Roles and Responsibilities\>; \<Security Operating Procedures\>, sections 4.4 and 9; \<Procedures\>, PRO-AC-3 and PRO-AC-4. Depth: focused. Coverage: focused |
| Test | Not applicable to this family today. Check L17 of Test-PlanConsistency.ps1 (the PL evidence). The leaver and mover route is tested once it is built (PA-32) |
| Interview | None held. The system owner, the global administrator, a line manager and \<Organisation\>'s HR remain (INT-PS-01 to INT-PS-05) |
| Boundary | \<System Name\>'s own designations, agreements, time limits and register. \<Organisation\>'s screening, HR and disciplinary processes are provider evidence (EV-PS-01 to EV-PS-03) |
| Order of assessment | A, designations (PS-2); B, screening (PS-3); C, agreements (PS-6); D, leavers and movers (PS-4, PS-5); E, external people (PS-7); F, sanctions and role descriptions (PS-8, PS-9); G, policy (PS-1) |
| Needed from providers | EV-PS-01, EV-PS-02 and EV-PS-03 in \<Evidence Requests\> |
| Evidence retained | TPL-2, TPL-14 and TPL-21 records; the personnel security register in \<Personnel Security Management\>, section 3.9; the PL evidence |

For the Level 2 assessment, the assessor should:

- sample accounts against the personnel security register, TPL-2 and the signed agreements;
- follow one leaver and one mover from notice to TPL-14, and compare the times with the audit records;
- examine EV-PS-01 to EV-PS-03;
- hold the interviews, and re-determine every statement in section PS.4.

## PT Personally Identifiable Information Processing and Transparency

### PT.1 Purpose

This records the Level 1 self-assessment of personal data handling in \<System Name\>, against CSS catalog release 5.2.0. It covers 6 PT controls and the 16 privacy baseline controls that are outside the Moderate baseline (D-PT-01, D-PT-07). An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### PT.2 How to read this record

**Change since this assessment.** On 18 November 2026 the personal data design was cut from \<Control Implementation Register\> into \<PII Processing Management\>, with each control set out part by part, the inventory and the retention schedule (D-PT-22). Since sign-in moved to AD FS (D-AC-23), \<System Name\> holds no accounts and has no sign-in page of its own, so the inventory and the notice were reworded. The request route now covers every right a person has, and recipients are told of a correction. One item was added for the gaps this chapter found: PA-126. The findings below are a true record of 6 and 11 November 2026 and are not changed.

**N/A** means the statement does not apply.

The methods were **Examine** (documents and code) and **Test**. The test is Test-PersonalData.ps1, run on 11 November 2026 on the tagged v1.0 build and a fresh throwaway stack (checks Q01 to Q10). The results and their hashes are in the PT evidence. No interviews have been held. Legal positions are placeholders until the legal adviser completes \<Data Protection Impact Assessment\> and \<PII Processing Management\>, section 3.3.

### PT.3 Executive summary

**Table PT-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 1 | IR-8(1) |
| Not applicable | 1 | SI-19 |
| Other than satisfied, with at least one system gap | 6 | PT-5, AC-3(14), AU-3(3), SC-7(24), SI-12(3), SI-18(4) |
| Other than satisfied, needing only a decision, approval or evidence | 14 | PT-1, PT-2, PT-3, PT-4, PT-7, AT-3(5), IR-2(3), PE-8(3), PL-9, RA-8, SA-8(33), SI-12(1), SI-12(2), SI-18 |

**Table PT-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| PT-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews outstanding | NC-PT-01 |
| PT-2 | Other than satisfied | 3 of 5 | Lawful basis and conditions not confirmed | NC-PT-02 |
| PT-3 | Other than satisfied | 6 of 10 | Notice not seen; processing not yet limited | NC-PT-03 |
| PT-4 | Other than satisfied | 1 of 2 | Position on consent not confirmed | NC-PT-04 |
| PT-5 | Other than satisfied | 2 of 8 | Notice not seen; no link at sign-in (Q06) | NC-PT-05 |
| PT-7 | Other than satisfied | 1 of 2 | Conditions not confirmed; HR documents not marked (Q01) | NC-PT-06 |
| AC-3(14) | Other than satisfied | 2 of 3 | No search across projects for one person (Q02) | NC-PT-07 |
| AT-3(5) | Other than satisfied | 2 of 3 | Training not yet given | NC-PT-08 |
| AU-3(3) | Other than satisfied | 1 of 2 | Application log repeats personal data (Q05) | NC-PT-09 |
| IR-2(3) | Other than satisfied | 0 of 2 | Training not yet given | NC-PT-10 |
| IR-8(1) | Satisfied | 3 of 3 | \<Incident Response Management\>, section 3.8 | NC-PT-11 |
| PE-8(3) | Other than satisfied | 1 of 2 | Visitor records not seen | NC-PT-12 |
| PL-9 | Other than satisfied | 1 of 2 | Not yet in the restricted store | NC-PT-13 |
| RA-8 | Other than satisfied | 0 of 3 | Impact assessment drafted, not completed | NC-PT-14 |
| SA-8(33) | Other than satisfied | 1 of 2 | Minimisation not yet reviewed | NC-PT-15 |
| SC-7(24) | Other than satisfied | 1 of 7 | Processing not monitored | NC-PT-16 |
| SI-12(1) | Other than satisfied | 1 of 2 | Projects not yet reviewed | NC-PT-17 |
| SI-12(2) | Other than satisfied | 4 of 6 | Research and training rule not in use | NC-PT-18 |
| SI-12(3) | Other than satisfied | 3 of 6 | No retention or disposal (Q03, Q08) | NC-PT-19 |
| SI-18 | Other than satisfied | 4 of 9 | Quality checks not yet made | NC-PT-20 |
| SI-18(4) | Other than satisfied | 0 of 1 | Corrections not audited (Q10) | NC-PT-21, NC-PT-22 |
| SI-19 | Not applicable | None of 4 applies | No dataset is de-identified | Met |

Of the CSS 109 statements, 58 are satisfied, 4 do not apply, 31 await a decision or approval, 9 show a gap in the system and 7 await evidence from \<Organisation\>.

The largest concerns are the impact assessment and lawful bases, which are drafted for the legal adviser but not decided, and the system's limits in serving people's rights: no search across projects, unaudited corrections and deletions, and no retention.

### PT.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 11 November 2026 where the basis says so.

**Table PT-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| PT-01\_ODP\[01\] | Who receives the policy is defined | S | \<PII Processing Management\> |
| PT-01\_ODP\[02\] | Who receives the procedures is defined | S | \<PII Processing Management\> |
| PT-01\_ODP\[03\] | Policy level is selected | S | \<PII Processing Management\> |
| PT-01\_ODP\[04\] | Managing official is defined | S | System owner |
| PT-01\_ODP\[05\] | Policy review frequency is defined | S | \<PII Processing Management\> |
| PT-01\_ODP\[06\] | Policy review events are defined | S | \<PII Processing Management\> |
| PT-01\_ODP\[07\] | Procedures review frequency is defined | S | \<PII Processing Management\> |
| PT-01\_ODP\[08\] | Procedures review events are defined | S | \<PII Processing Management\> |
| PT-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-PT-02); version \<ver\> awaits re-approval (D-PT-18) |
| PT-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| PT-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-PT-19) |
| PT-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| PT-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\>, section PT.1 |
| PT-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\>, section PT.1 |
| PT-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\>, section PT.5 |
| PT-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\>, section PT.5 |
| PT-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\>, section PT.6 |
| PT-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\>, section PT.6 |
| PT-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\>, section PT.6 |
| PT-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 11 November 2026, as confirmed by the system owner |
| PT-01b. | Official is designated | S | \[Name\] is the system owner |
| PT-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| PT-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 11 November 2026 after the PT pack review (D-PT-17) |
| PT-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| PT-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 11 November 2026 (D-PT-19) |
| PT-02\_ODP\[01\] | Authority is defined | S | \<PII Processing Management\>, including the Data (Use and Access) Act 2025 |
| PT-02\_ODP\[02\] | Permitted processing is defined | S | \<PII Processing Management\> |
| PT-02\_ODP\[03\] | Restricted processing is defined | S | \<PII Processing Management\> |
| PT-02a. | The authority permitting processing is determined and documented | O-D | Basis and conditions for each kind of data are placeholders in \<PII Processing Management\>, section 3.3, for the legal adviser (D-PT-20) |
| PT-02b. | Processing is restricted to what is authorised | O-D | Rule approved; not yet in use; lawful basis not confirmed |
| PT-03\_ODP\[01\] | Purposes are defined | S | \<PII Processing Management\> |
| PT-03\_ODP\[02\] | Processing restricted to the purposes is defined | S | \<PII Processing Management\> |
| PT-03\_ODP\[03\] | How changes are controlled is defined | S | \<PII Processing Management\> |
| PT-03\_ODP\[04\] | Requirements for changes are defined | S | \<PII Processing Management\> |
| PT-03a. | Purposes are identified and documented | S | Stated in \<Policy\> (PT), approved (D-PT-02) |
| PT-03b.\[01\] | Purposes are in the privacy notice | O-E | EV-PT-01: \<Organisation\>'s notice not seen |
| PT-03b.\[02\] | Purposes are in policies | S | \<Policy\> (PT), approved (D-PT-02) |
| PT-03c. | Processing is limited to what fits the purposes | O-D | Rule approved; not yet in use; nothing limits what is uploaded, and HR documents are not marked (Q01) |
| PT-03d.\[01\] | Changes in processing are monitored | O-D | PRO-PT-3 approved; not yet in use |
| PT-03d.\[02\] | Changes follow the set requirements | O-D | PRO-PT-3 approved; not yet in use |
| PT-04\_ODP | Consent tools are defined | S | None, as consent is not the lawful basis |
| PT-04 | Consent tools are implemented | O-D | The legal adviser has yet to confirm that consent is not the basis |
| PT-05\_ODP\[01\] | Notice review frequency is defined | S | \<PII Processing Management\> |
| PT-05\_ODP\[02\] | Notice content is defined | S | \<PII Processing Management\> |
| PT-05a.\[01\] | Notice is available on first contact | O-G | Neither sign-in page links to a privacy notice (Q06, PA-90); notice not seen (EV-PT-01) |
| PT-05a.\[02\] | Notice stays available | O-E | EV-PT-01 |
| PT-05b. | Notice is clear and in plain language | O-E | EV-PT-01 |
| PT-05c. | Notice names the authority | O-E | EV-PT-01 |
| PT-05d. | Notice names the purpose | O-E | EV-PT-01 |
| PT-05e. | Notice includes the set information | O-E | EV-PT-01 |
| PT-07\_ODP | Conditions for special categories are defined | S | \<PII Processing Management\> |
| PT-07 | Conditions are applied to special categories | O-D | Conditions are placeholders (D-PT-20), and HR documents are classified Internal like every other project (Q01, PA-89) |
| AC-03(14)\_ODP\[01\] | How individuals get access is defined | S | \<PII Processing Management\> |
| AC-03(14)\_ODP\[02\] | What they can access is defined | S | \<PII Processing Management\> |
| AC-03(14) | Individuals can access their data | O-G | No page searches every project for one person (Q02, PA-89); PRO-PT-1 \<ver\> sets the manual route |
| AT-03(05)\_ODP\[01\] | Who gets privacy training is defined | S | \<PII Processing Management\> |
| AT-03(05)\_ODP\[02\] | Frequency is defined | S | \<PII Processing Management\> |
| AT-03(05) | Initial and refresher training is given | O-D | No privacy training yet given |
| AU-03(03)\_ODP | Personal data allowed in audit records is defined | S | \<PII Processing Management\> |
| AU-03(03) | Audit records hold only that personal data | O-G | Audit free text holds no extra personal data (Q04), but the application log repeats usernames and IP addresses (Q05, PA-75) |
| IR-02(03)\[01\] | Training on identifying and responding to a breach | O-D | Training not yet given (\<Control Assessment Record\> (IR)) |
| IR-02(03)\[02\] | Training on reporting a breach | O-D | Training not yet given |
| IR-08(01)(a) | Plan decides whether notice of a breach is needed | S | \<Incident Response Management\>: the legal adviser decides on notifying the ICO |
| IR-08(01)(b) | Plan assesses harm to individuals, and how to reduce it | S | \<Incident Response Management\> \<ver\>, section 3.8: harm to people and telling them |
| IR-08(01)(c) | Plan identifies privacy requirements | S | \<Incident Response Management\> \<ver\>, section 3.8: the 72-hour ICO report and the breach register |
| PE-08(03)\_ODP | Personal data allowed in visitor records is defined | S | \<PII Processing Management\> |
| PE-08(03) | Visitor records hold only that personal data | O-E | EV-PT-02: \<Organisation\>'s records not seen |
| PL-09\_ODP | What is centrally managed is defined | S | \<PII Processing Management\> |
| PL-09 | Those items are centrally managed | O-D | This document set awaits moving to the restricted store (PA-88) |
| RA-08a. | Impact assessment before developing or buying | O-D | Draft \<Data Protection Impact Assessment\> \<ver\> prepared; the legal adviser completes it (D-PT-20, PA-72); \<System Name\> is already built |
| RA-08b.\[01\] | Impact assessment before collecting personal data | O-D | Draft \<Data Protection Impact Assessment\> \<ver\> prepared; the legal adviser completes it (D-PT-20, PA-72) |
| RA-08b.\[02\] | Impact assessment before collecting contact details | O-D | Draft \<Data Protection Impact Assessment\> \<ver\> prepared; the legal adviser completes it (D-PT-20, PA-72) |
| SA-08(33)\_ODP | How minimisation is done is defined | S | \<PII Processing Management\> |
| SA-08(33) | Minimisation is implemented | O-D | Rule approved; not yet in use; reviewed in \<Data Protection Impact Assessment\> when completed |
| SC-07(24)\_ODP | Processing rules are defined | S | \<PII Processing Management\> |
| SC-07(24)(a) | Rules are applied to personal data elements | O-D | Project permissions apply to whole documents; impact assessment not done |
| SC-07(24)(b)\[01\] | Processing is monitored at external interfaces | O-G | No such monitoring (PA-71) |
| SC-07(24)(b)\[02\] | Processing is monitored at internal boundaries | O-G | No such monitoring (PA-71) |
| SC-07(24)(c) | Exceptions are documented | O-D | No process yet |
| SC-07(24)(d)\[01\] | Exceptions are reviewed | O-D | No process yet |
| SC-07(24)(d)\[02\] | Unsupported exceptions are removed | O-D | No process yet |
| SI-12(01)\_ODP | Elements processed are defined | S | \<PII Processing Management\> |
| SI-12(01) | Personal data is limited to those elements | O-D | Rule approved; not yet in use; projects not yet reviewed |
| SI-12(02)\_ODP\[01\] | Technique for research is defined | S | \<PII Processing Management\> |
| SI-12(02)\_ODP\[02\] | Technique for testing is defined | S | \<PII Processing Management\> |
| SI-12(02)\_ODP\[03\] | Technique for training is defined | S | \<PII Processing Management\> |
| SI-12(02)\[01\] | Personal data in research is minimised | O-D | Rule approved; not yet in use |
| SI-12(02)\[02\] | Personal data in testing is minimised | S | Test stacks hold sample data only (Q09) |
| SI-12(02)\[03\] | Personal data in training is minimised | O-D | Rule approved; not yet in use |
| SI-12(03)\_ODP\[01\] | Disposal technique is defined | S | \<PII Processing Management\> |
| SI-12(03)\_ODP\[02\] | Destruction technique is defined | S | \<PII Processing Management\> |
| SI-12(03)\_ODP\[03\] | Erasure technique is defined | S | \<PII Processing Management\> |
| SI-12(03)\[01\] | Information is disposed of after retention | O-G | No retention field or disposal (Q08, PA-70); deleted pages remain until vacuum (Q03) |
| SI-12(03)\[02\] | Information is destroyed after retention | O-G | No retention field or disposal (Q08, PA-70) |
| SI-12(03)\[03\] | Information is erased after retention | O-G | No retention field or disposal (Q08, PA-70) |
| SI-18\_ODP\[01\] | Accuracy check frequency is defined | S | \<PII Processing Management\> |
| SI-18\_ODP\[02\] | Relevance check frequency is defined | S | \<PII Processing Management\> |
| SI-18\_ODP\[03\] | Timeliness check frequency is defined | S | \<PII Processing Management\> |
| SI-18\_ODP\[04\] | Completeness check frequency is defined | S | \<PII Processing Management\> |
| SI-18a.\[01\] | Accuracy is checked | O-D | PRO-PT-5 approved; no check yet |
| SI-18a.\[02\] | Relevance is checked | O-D | PRO-PT-5 approved; no check yet |
| SI-18a.\[03\] | Timeliness is checked | O-D | PRO-PT-5 approved; no check yet |
| SI-18a.\[04\] | Completeness is checked | O-D | PRO-PT-5 approved; no check yet |
| SI-18b. | Inaccurate or outdated data is corrected or deleted | O-D | PRO-PT-5 approved; not yet in use |
| SI-18(04) | Data is corrected or deleted on request | O-G | Corrections in the admin portal are not audited (Q10, PA-89); PRO-PT-1 \<ver\> records them by hand meanwhile |
| SI-19\_ODP\[01\] | Elements removed are defined | N/A | No dataset is de-identified or released, so no value is needed (\<PII Processing Management\>) |
| SI-19\_ODP\[02\] | Evaluation frequency is defined | N/A | No dataset is de-identified or released, so no value is needed (\<PII Processing Management\>) |
| SI-19a. | Elements are removed from datasets | N/A | No dataset is de-identified or released |
| SI-19b. | De-identification is evaluated | N/A | No dataset is de-identified or released |

### PT.5 Assessment plan

**Table PT-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Security categorisation | Moderate, confirmed by the authorising official; privacy baseline applied (D-PT-01) |
| Scope | 6 PT controls and 16 privacy baseline controls outside Moderate, with 109 determination statements, covering every kind of personal data in \<PII Processing Management\>, section 3.3 |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0); UK GDPR, the DPA 2018 and the Data (Use and Access) Act 2025 for what the organisation must comply with |
| Dates | 6 November 2026; updated on 11 November 2026 after the PT pack review |
| Examine | \<Policy\> (PT), \<Procedures\> (PT) and the PT chapter of \<Control Implementation Register\> at \<ver\>, now in \<PII Processing Management\>, \<Data Protection Impact Assessment\> \<ver\>, \<Privacy Plan\>, \<Incident Response Management\>, section 3.8, SyOps A23 to A29; the audit record format, the admin portal's document management and the repositories' search. Depth: focused. Coverage: focused |
| Test | Test-PersonalData.ps1, checks Q01 to Q10, on a fresh throwaway stack (evidence in the PT evidence) |
| Interview | System owner's written answers only. The legal adviser, the business owner, the data protection officer and an administrator who would handle a request remain |
| Previous results reused | AU checks on audit records; IR readiness drill (D02, D08) for the application log; MP export checks (P02 to P06) for export copies |
| Boundary | \<System Name\>'s handling of personal data. \<Organisation\>'s notice, record of processing and privacy programme are inherited (EV-PT-01, EV-PM-02, EV-PM-04) |
| Order of assessment | A, the impact assessment and lawful bases (RA-8, PT-2, PT-7); B, people's rights (AC-3(14), SI-18(4)); C, retention (SI-12(3)); D, transparency (PT-5); E, logs (AU-3(3)); F, policy (PT-1). The impact assessment comes first because most other findings depend on it |
| Needed from \<Organisation\> | EV-PT-01, EV-PT-02, EV-PM-02 and EV-PM-04 in \<Evidence Requests\> |
| Evidence retained | the PT evidence (results, README and MANIFEST); completed TPL-15 and TPL-22 records; the approved \<Data Protection Impact Assessment\> |

For the Level 2 assessment, the assessor should examine the completed impact assessment and the lawful bases, run Test-PersonalData.ps1 on the built VMs, walk through a sample subject access request and complaint with the legal adviser, interview the business owner on retention, and re-determine every statement in section PT.4.

## RA Risk Assessment

### RA.1 Purpose

This records the Level 1 self-assessment of the 10 RA entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### RA.2 How to read this record

**Change since this assessment.** On 18 November 2026 the risk assessment design was cut from \<Control Implementation Register\> into \<Risk Assessment Management\>, with each control set out part by part (D-RA-11). Since sign-in moved to AD FS (D-AC-23), \<System Name\> holds no accounts, so the critical components were reworded and AD FS with Active Directory, the application server and the bulk export folder added. The cross-check found that the risk assessment and the supply chain review have not been reviewed after the changes to sign-in and hosting, that nothing scans \<System Name\>'s own applications, and that the public reporting route has no published terms; PA-62 and PA-127 cover them. The findings below are a true record of 6 and 11 November 2026 and are not changed.

The methods were **Examine** (the risk documents) and **Test**. The test is Test-Vulnerability.ps1, run on 11 November 2026 on the tagged v1.0 build and the throwaway stack's images (checks V01 to V09). It checks the packages, the images and their operating system packages, and whether the risk list, decisions, acceptances, critical components and POA&M agree. The results and their hashes are in the RA evidence. No interviews have been held.

**Limit of the current evidence:** the Windows Server 2025 VMs and \<Organisation\>'s services have not been examined.

### RA.3 Executive summary

**Table RA-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 2 | RA-2, RA-9 |
| Other than satisfied, with at least one system gap | 2 | RA-5, RA-5(2) |
| Other than satisfied, needing only a decision, approval or evidence | 6 | RA-1, RA-3, RA-3(1), RA-5(5), RA-5(11), RA-7 |

**Table RA-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| RA-1 | Other than satisfied | 21 of 25 | Not yet shared; first scheduled reviews outstanding | NC-RA-01 |
| RA-2 | Satisfied | 3 of 3 | Categorised and approved; availability rationale for confirmation (D-RA-07) | Met |
| RA-3 | Other than satisfied | 9 of 13 | First scheduled review not due; not shared with the Head of Cyber; \<Organisation\>'s risk appetite not seen | NC-RA-02 |
| RA-3(1) | Other than satisfied | 3 of 4 | First review held; yearly update not yet due | NC-RA-03 |
| RA-5 | Other than satisfied | 4 of 14 | No scanner for the images or VMs; 5 High advisories open (V01, V02) | NC-RA-04 |
| RA-5(2) | Other than satisfied | 2 of 3 | No scanner | NC-RA-05 |
| RA-5(5) | Other than satisfied | 2 of 3 | VMs not yet built | NC-RA-06 |
| RA-5(11) | Other than satisfied | 0 of 1 | Route not yet confirmed with \<Organisation\> | NC-RA-07 |
| RA-7 | Other than satisfied | 2 of 4 | No monitoring or audit findings yet | NC-RA-08 |
| RA-9 | Satisfied | 3 of 3 | \<Risk Assessment Management\>, section 3.9, reviewed | Met |

Of the CSS 73 statements, 49 are satisfied, 13 await a decision or approval, 9 show a gap in the system and 2 await evidence from the VMs or \<Organisation\>.

The risk method, categorisation and risk response are in place. The gaps are that nothing scans the images or VMs, and that five High package advisories are open. The test also found the base images unpinned (V03, PA-77).

### RA.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 11 November 2026 where the basis says so.

**Table RA-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| RA-01\_ODP\[01\] | Who receives the policy is defined | S | \<Risk Assessment Management\> |
| RA-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Risk Assessment Management\> |
| RA-01\_ODP\[03\] | Policy level is selected | S | \<Risk Assessment Management\> |
| RA-01\_ODP\[04\] | Managing official is defined | S | System owner |
| RA-01\_ODP\[05\] | Policy review frequency is defined | S | \<Risk Assessment Management\> |
| RA-01\_ODP\[06\] | Policy review events are defined | S | \<Risk Assessment Management\> |
| RA-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Risk Assessment Management\> |
| RA-01\_ODP\[08\] | Procedures review events are defined | S | \<Risk Assessment Management\> |
| RA-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-RA-01); version \<ver\> awaits re-approval (D-RA-06) |
| RA-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| RA-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-RA-09) |
| RA-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| RA-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (RA) \<ver\>, section RA.1 |
| RA-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (RA) \<ver\>, section RA.1 |
| RA-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (RA) \<ver\>, section RA.5 |
| RA-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (RA) \<ver\>, section RA.5 |
| RA-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (RA) \<ver\>, section RA.6 |
| RA-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (RA) \<ver\>, section RA.6 |
| RA-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (RA) \<ver\>, section RA.6 |
| RA-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 11 November 2026, as confirmed by the system owner |
| RA-01b. | Official is designated | S | \[Name\] is the system owner |
| RA-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| RA-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 11 November 2026 after the RA pack review (D-RA-08) |
| RA-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| RA-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 11 November 2026 (D-RA-09) |
| RA-02a. | The system and its information are categorised | S | \<System Security Plan\>, section 3.3; availability rationale awaits the information owner and authorising official (D-RA-07) |
| RA-02b. | Results and rationale are documented | S | \<System Security Plan\>, section 3.3 |
| RA-02c. | The authorising official approves the categorisation | S | \[Name\] (D-GEN-06) |
| RA-03\_ODP\[01\] | Where results go is selected | S | \<Risk Assessment Management\> |
| RA-03\_ODP\[02\] | Document is defined | S | \<Risk List\> |
| RA-03\_ODP\[03\] | Review frequency is defined | S | \<Risk Assessment Management\> |
| RA-03\_ODP\[04\] | Who receives results is defined | S | \<Risk Assessment Management\> |
| RA-03\_ODP\[05\] | Update frequency is defined | S | \<Risk Assessment Management\> |
| RA-03a.01 | Threats and vulnerabilities are identified | S | \<Risk List\> \<ver\>: threat sources in section 4, Table 3c; causes in section 2 |
| RA-03a.02 | Likelihood and magnitude of harm are determined | S | \<Risk List\> \<ver\>, section 4: scales in Tables 3a and 3b, matrix in Table 3 |
| RA-03a.03 | Likelihood and impact on privacy are determined | S | \<Risk List\>, R-PT-01 and R-AU-02, rated by the same method; \<Data Protection Impact Assessment\> drafted |
| RA-03b. | Results are integrated with higher-level decisions | O-E | \<Organisation\>'s risk appetite and organisational risk not seen (EV-RA-01, EV-PM-01, D-PM-03) |
| RA-03c. | Results are documented | S | \<Risk List\> |
| RA-03d. | Results are reviewed | O-D | First review not yet due |
| RA-03e. | Results are shared | O-D | Not yet shared with the Head of Cyber |
| RA-03f. | The assessment is updated | O-D | First update not yet due |
| RA-03(01)\_ODP\[01\] | Items assessed are defined | S | \<Risk Assessment Management\> |
| RA-03(01)\_ODP\[02\] | Update frequency is defined | S | \<Risk Assessment Management\> |
| RA-03(01)(a) | Supply chain risks are assessed | S | First review held on 11 November 2026: \<Risk Assessment Management\>, section 3.4 (D-RA-09) |
| RA-03(01)(b) | The supply chain assessment is updated | O-D | First yearly update not yet due |
| RA-05\_ODP\[01\] | Monitoring frequency is defined | S | \<Risk Assessment Management\> |
| RA-05\_ODP\[02\] | Scan frequency is defined | S | \<Risk Assessment Management\> |
| RA-05\_ODP\[03\] | Response times are defined | S | \<Risk Assessment Management\>, section 3.6 (D-RA-P02) |
| RA-05\_ODP\[04\] | Who receives results is defined | S | \<Risk Assessment Management\> |
| RA-05a.\[01\] | Systems are monitored for vulnerabilities | O-G | Packages checked by Test-Vulnerability.ps1 (V01); images and VMs not monitored (V02, PA-62) |
| RA-05a.\[02\] | Systems are scanned for vulnerabilities | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05b. | Tools are used that work with each other | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05b.01 | Tools work together and automate parts of the process | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05b.02 | Tools report flaws in a common format | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05b.03 | Tools measure the effect of vulnerabilities | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05c. | Results are analysed | O-D | PRO-RA-3 \<ver\> approved, with analysis and false positives on TPL-7; not yet in use |
| RA-05d. | Real vulnerabilities are fixed in time | O-G | 7 advisories open, 5 of them High, in API and UI application (V01, PA-56) |
| RA-05e. | Information is shared to remove similar flaws | O-D | PRO-RA-5 \<ver\> approved; not yet in use |
| RA-05f. | Tools can update what they scan for | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05(02)\_ODP\[01\] | When the list is updated is selected | S | \<Risk Assessment Management\> |
| RA-05(02)\_ODP\[02\] | Frequency is defined | S | \<Risk Assessment Management\> |
| RA-05(02) | Vulnerabilities to scan for are updated | O-G | No scanner for the images or VMs (V02, PA-62) |
| RA-05(05)\_ODP\[01\] | Components are defined | S | \<Risk Assessment Management\> |
| RA-05(05)\_ODP\[02\] | Scanning activities are defined | S | \<Risk Assessment Management\> |
| RA-05(05) | Privileged access is used for scans | O-E | On the VMs |
| RA-05(11) | A channel for reports exists | O-D | Route agreed (D-RA-05) and set in PRO-RA-5; not yet confirmed with \<Organisation\> (EV-RA-01) |
| RA-07\[01\] | Assessment findings are responded to | S | \<Risk List\>, \<Decision Register\> and \<Plan of Action and Milestones\> |
| RA-07\[02\] | Privacy assessment findings are responded to | S | PT assessment findings answered in \<Risk List\>, section 5.14, and \<Plan of Action and Milestones\> (PA-70 to PA-72, PA-89, PA-90) |
| RA-07\[03\] | Monitoring findings are responded to | O-D | Monitoring not started; PRO-RA-1 reviews new test results |
| RA-07\[04\] | Audit findings are responded to | O-D | No audit held |
| RA-09\_ODP\[01\] | Items analysed are defined | S | \<Risk Assessment Management\> |
| RA-09\_ODP\[02\] | Decision points are defined | S | \<Risk Assessment Management\> |
| RA-09 | Critical components are identified | S | \<Risk Assessment Management\>, section 3.9, with its method, reviewed on 11 November 2026 (D-RA-09) |

### RA.5 Assessment plan

**Table RA-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 10 RA entries in the Moderate baseline, with 73 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0); CSS for the risk method |
| Dates | 6 November 2026; updated on 11 November 2026 after the RA pack review |
| Examine | \<Policy\> (RA), \<Procedures\> (RA) and the RA chapter of \<Control Implementation Register\> at \<ver\>, now in \<Risk Assessment Management\>; \<Risk List\> \<ver\>; \<System Security Plan\>, section 3; \<Supply Chain Risk Management\>; \<Decision Register\>; \<Plan of Action and Milestones\>. Depth: focused. Coverage: focused |
| Test | Test-Vulnerability.ps1, checks V01 to V09, on the v1.0 tag and the images the throwaway stack runs (evidence in the RA evidence) |
| Interview | None held. The system owner, the security officer, the Windows server administrator and \<Organisation\>'s security contact remain |
| Previous results reused | CM checks on image tags and the bill of materials (C01 to C11); MA check M10 for package managers in the images |
| Boundary | \<System Name\>'s risk assessment and vulnerability management. \<Organisation\>'s risk strategy, scanning services and the VMs are inherited or not yet built (EV-RA-01, EV-PM-01) |
| Order of assessment | A, vulnerabilities (RA-5, RA-5(2), RA-5(5)); B, risk method and register (RA-3, RA-7); C, supply chain and critical components (RA-3(1), RA-9); D, categorisation (RA-2); E, policy (RA-1) |
| Needed from \<Organisation\> | EV-RA-01 and EV-PM-01 in \<Evidence Requests\> |
| Evidence retained | the RA evidence (results, README and MANIFEST); the 6 November package check in the SI, RA and CA evidence; completed TPL-7 and TPL-23 records |

For the Level 2 assessment, the assessor should run Test-Vulnerability.ps1 and a credentialed scan on the built VMs, sample TPL-7 records against the timetable, interview the security officer on an exploited flaw, and re-determine every statement in section RA.4.

## SA System and Services Acquisition

### SA.1 Purpose

This records the Level 1 self-assessment of the 17 SA entries in the CSS Moderate baseline, using catalog release 5.2.0. SA-4(10) is tailored out (\<Tailoring Register\>, TR-SA-01), so 16 are assessed. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### SA.2 How to read this record

**Change since this assessment.** On 18 November 2026 the acquisition design was cut from \<Control Implementation Register\> into \<System and Services Acquisition Management\>, with each control set out part by part (D-SA-19). The developer test plan now lists 15 scripts, AD FS, Active Directory, the Starters/Leavers system and Docker Hub are listed as external services, and the applications run as Windows services (D-PL-10). The cross-check added the kinds of analysis, the basis of trust for each service, and checks that open-source components are still maintained; PA-68 and PA-128 cover what is not done, and PA-68, PA-91 and PA-92 are now due before go-live, as the authorising official decided (D-SA-14). The findings below are a true record of 6 and 11 November 2026 and are not changed.

The methods were **Examine** (documents, repositories and test evidence) and **Test**. The test is Test-Development.ps1, run on 11 November 2026 (checks S01 to S10). It reads the GitHub settings of the six repositories through the GitHub API (read-only), the Git history at tag v1.0, the build files and the component support dates. The results and their hashes are in the SA evidence. No interviews have been held.

### SA.3 Executive summary

**Table SA-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 5 | SA-4(1), SA-4(2), SA-4(9), SA-15(3), SA-22 |
| Other than satisfied, with at least one system gap | 2 | SA-10, SA-11 |
| Other than satisfied, needing only a decision, approval or evidence | 9 | SA-1, SA-2, SA-3, SA-4, SA-5, SA-8, SA-9, SA-9(2), SA-15 |

**Table SA-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| SA-1 | Other than satisfied | 21 of 25 | Not yet shared; Head of Cyber's re-approval (D-SA-16) and first scheduled reviews outstanding | NC-SA-01 |
| SA-2 | Other than satisfied | 2 of 6 | Costs not yet raised in budgeting | NC-SA-02 |
| SA-3 | Other than satisfied | 5 of 9 | CSS mapped; not yet in routine use | NC-SA-03 |
| SA-4 | Other than satisfied | 2 of 18 | Contract not seen | NC-SA-04 |
| SA-4(1) | Satisfied | 1 of 1 | SSP section 7 and the register chapters | Met |
| SA-4(2) | Satisfied | 4 of 4 | \<Security Architecture\> and the SSP | Met |
| SA-4(9) | Satisfied | 4 of 4 | \<System Security Plan\>, section 3.7 | Met |
| SA-5 | Other than satisfied | 2 of 22 | Guides drafted; awaiting the developers | NC-SA-08 |
| SA-8 | Other than satisfied | 6 of 12 | Principles mapped for specification and design only | NC-SA-09 |
| SA-9 | Other than satisfied | 4 of 8 | Providers' compliance not seen; no review held | NC-SA-10 |
| SA-9(2) | Other than satisfied | 1 of 2 | Providers' lists not seen | NC-SA-11 |
| SA-10 | Other than satisfied | 7 of 14 | No branch protection, required review or signed tags (S01, S05) | NC-SA-12 |
| SA-11 | Other than satisfied | 10 of 12 | No unit tests or pipeline (S08) | NC-SA-13 |
| SA-15 | Other than satisfied | 9 of 12 | Process not yet reviewed | NC-SA-14 |
| SA-15(3) | Satisfied | 6 of 6 | \<Risk Assessment Management\>, section 3.9 | Met |
| SA-22 | Satisfied | 4 of 4 | No component near the end of support (S09) | Met |

Of the CSS 159 statements, 88 are satisfied, 46 await a decision or approval, 5 show a gap in the system and 20 await evidence from providers.

The largest concern is change control: no repository protects its default branch or requires a review, and the release had no reviewed merge or signed tag (PA-91). The build also turns the package audit off (PA-92).

### SA.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 6 November 2026, updated on 11 November 2026 where the basis says so.

**Table SA-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| SA-01\_ODP\[01\] | Who receives the policy is defined | S | \<System and Services Acquisition Management\> |
| SA-01\_ODP\[02\] | Who receives the procedures is defined | S | \<System and Services Acquisition Management\> |
| SA-01\_ODP\[03\] | Policy level is selected | S | \<System and Services Acquisition Management\> |
| SA-01\_ODP\[04\] | Managing official is defined | S | System owner |
| SA-01\_ODP\[05\] | Policy review frequency is defined | S | \<System and Services Acquisition Management\> |
| SA-01\_ODP\[06\] | Policy review events are defined | S | \<System and Services Acquisition Management\> |
| SA-01\_ODP\[07\] | Procedures review frequency is defined | S | \<System and Services Acquisition Management\> |
| SA-01\_ODP\[08\] | Procedures review events are defined | S | \<System and Services Acquisition Management\> |
| SA-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber (D-SA-01); version \<ver\> awaits re-approval (D-SA-16) |
| SA-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| SA-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-SA-18) |
| SA-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| SA-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (SA) \<ver\>, section SA.1 |
| SA-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (SA) \<ver\>, section SA.1 |
| SA-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (SA) \<ver\>, section SA.5 |
| SA-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (SA) \<ver\>, section SA.5 |
| SA-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (SA) \<ver\>, section SA.6 |
| SA-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (SA) \<ver\>, section SA.6 |
| SA-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (SA) \<ver\>, section SA.6 |
| SA-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 11 November 2026, as confirmed by the system owner |
| SA-01b. | Official is designated | S | \[Name\] is the system owner |
| SA-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| SA-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 11 November 2026 after the SA pack review (D-SA-17) |
| SA-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| SA-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 11 November 2026 (D-SA-18) |
| SA-02a.\[01\] | Security requirements are set in planning | S | \<System Security Plan\> and the Moderate baseline |
| SA-02a.\[02\] | Privacy requirements are set in planning | S | \<Privacy Plan\>, approved (D-PT-05) |
| SA-02b.\[01\] | Resources are determined and documented | O-D | Not yet raised in budgeting; TPL-23 now records the costs |
| SA-02b.\[02\] | Resources are allocated | O-D | Not yet raised in budgeting; TPL-23 now records the costs |
| SA-02c.\[01\] | Budget line for security | O-D | Not yet raised in budgeting; TPL-23 now records the costs |
| SA-02c.\[02\] | Budget line for privacy | O-D | Not yet raised in budgeting; TPL-23 now records the costs |
| SA-03\_ODP | Lifecycle is defined | S | \<System and Services Acquisition Management\>: CSS \<ver\>, section SA.3 |
| SA-03a.\[01\] | Lifecycle includes security | O-D | CSS mapped in \<System and Services Acquisition Management\>, section 3.2; not yet in routine use |
| SA-03a.\[02\] | Lifecycle includes privacy | O-D | CSS mapped in \<System and Services Acquisition Management\>, section 3.2; not yet in routine use |
| SA-03b.\[01\] | Security roles are documented | S | \<Roles and Responsibilities\> |
| SA-03b.\[02\] | Privacy roles are documented | S | \<Privacy Plan\>, approved (D-PT-05) |
| SA-03c.\[01\] | People with security roles are identified | S | \<Roles and Responsibilities\> |
| SA-03c.\[02\] | People with privacy roles are identified | S | \<Privacy Plan\>, section 3 |
| SA-03d.\[01\] | Security risk management is part of the lifecycle | O-D | PRO-SA-1 approved; not yet in use |
| SA-03d.\[02\] | Privacy risk management is part of the lifecycle | O-D | PRO-PT-2 and PRO-PT-3 approved; not yet in use |
| SA-04\_ODP\[01\] | Contract method is selected | S | \<System and Services Acquisition Management\> |
| SA-04\_ODP\[02\] | Contract language is defined | S | \<System and Services Acquisition Management\> |
| SA-04a.\[01\] | Contracts include security functional requirements | O-E | EV-SA-01 |
| SA-04a.\[02\] | Contracts include privacy functional requirements | O-E | EV-SA-01 |
| SA-04b. | Contracts include strength of mechanism | O-E | EV-SA-01 |
| SA-04c.\[01\] | Contracts include security assurance | O-E | EV-SA-01 |
| SA-04c.\[02\] | Contracts include privacy assurance | O-E | EV-SA-01 |
| SA-04d.\[01\] | Contracts include controls for security | O-E | EV-SA-01 |
| SA-04d.\[02\] | Contracts include controls for privacy | O-E | EV-SA-01 |
| SA-04e.\[01\] | Contracts include security documentation | O-E | EV-SA-01 |
| SA-04e.\[02\] | Contracts include privacy documentation | O-E | EV-SA-01 |
| SA-04f.\[01\] | Contracts protect security documentation | O-E | EV-SA-01 |
| SA-04f.\[02\] | Contracts protect privacy documentation | O-E | EV-SA-01 |
| SA-04g. | Contracts describe the development environment | O-E | EV-SA-01 |
| SA-04h.\[01\] | Contracts allocate responsibility for security | O-E | EV-SA-01 |
| SA-04h.\[02\] | Contracts allocate responsibility for privacy | O-E | EV-SA-01 |
| SA-04h.\[03\] | Contracts allocate responsibility for supply chain risk | O-E | EV-SA-01 |
| SA-04i. | Contracts include acceptance criteria | O-E | EV-SA-01 |
| SA-04(01) | Developer describes the controls' functional properties | S | \<System Security Plan\>, section 7, and each family's register chapter describe the controls' functional properties |
| SA-04(02)\_ODP\[01\] | Design information is selected | S | \<System and Services Acquisition Management\> |
| SA-04(02)\_ODP\[02\] | Other information is defined | S | \<System and Services Acquisition Management\> |
| SA-04(02)\_ODP\[03\] | Level of detail is defined | S | \<System and Services Acquisition Management\> |
| SA-04(02) | Developer provides design information | S | \<Security Architecture\> \<ver\> and \<System Security Plan\>, sections 3 and 4 |
| SA-04(09)\[01\] | Developer identifies functions | S | \<System Security Plan\>, section 3.7, Table 7 |
| SA-04(09)\[02\] | Developer identifies ports | S | \<System Security Plan\>, section 3.7, Table 7 |
| SA-04(09)\[03\] | Developer identifies protocols | S | \<System Security Plan\>, section 3.7, Table 7 |
| SA-04(09)\[04\] | Developer identifies services | S | \<System Security Plan\>, section 3.7, Table 7 |
| SA-05\_ODP\[01\] | Actions for missing documents are defined | S | \<System and Services Acquisition Management\> |
| SA-05\_ODP\[02\] | Who receives documentation is defined | S | \<System and Services Acquisition Management\> |
| SA-05a.01\[01\] | Administrator guide covers secure configuration | O-D | \<Administrator Guide\> \<ver\>, section 3; awaiting the developers (S10, PA-69) |
| SA-05a.01\[02\] | Administrator guide covers secure installation | O-D | \<Administrator Guide\> \<ver\>, section 2; awaiting the developers (S10, PA-69) |
| SA-05a.01\[03\] | Administrator guide covers secure operation | O-D | \<Administrator Guide\> \<ver\>, section 4; awaiting the developers (S10, PA-69) |
| SA-05a.02\[01\] | Covers using security functions | O-D | \<Administrator Guide\> \<ver\>, section 5; awaiting the developers (S10, PA-69) |
| SA-05a.02\[02\] | Covers maintaining security functions | O-D | \<Administrator Guide\> \<ver\>, section 5; awaiting the developers (S10, PA-69) |
| SA-05a.02\[03\] | Covers using privacy functions | O-D | \<Administrator Guide\> \<ver\>, section 6; awaiting the developers (S10, PA-69) |
| SA-05a.02\[04\] | Covers maintaining privacy functions | O-D | \<Administrator Guide\> \<ver\>, section 6; awaiting the developers (S10, PA-69) |
| SA-05a.03\[01\] | Covers known problems configuring privileged functions | O-D | \<Administrator Guide\> \<ver\>, section 7; awaiting the developers (S10, PA-69) |
| SA-05a.03\[02\] | Covers known problems using privileged functions | O-D | \<Administrator Guide\> \<ver\>, section 7; awaiting the developers (S10, PA-69) |
| SA-05b.01\[01\] | User guide covers security functions | O-D | \<User Guide\> \<ver\>, section 3; awaiting the developers (S10, PA-69) |
| SA-05b.01\[02\] | User guide covers using them | O-D | \<User Guide\> \<ver\>, section 3; awaiting the developers (S10, PA-69) |
| SA-05b.01\[03\] | User guide covers privacy functions | O-D | \<User Guide\> \<ver\>, section 4; awaiting the developers (S10, PA-69) |
| SA-05b.01\[04\] | User guide covers using them | O-D | \<User Guide\> \<ver\>, section 4; awaiting the developers (S10, PA-69) |
| SA-05b.02\[01\] | User guide covers working securely | O-D | \<User Guide\> \<ver\>, section 3; awaiting the developers (S10, PA-69) |
| SA-05b.02\[02\] | User guide covers protecting privacy | O-D | \<User Guide\> \<ver\>, section 4; awaiting the developers (S10, PA-69) |
| SA-05b.03\[01\] | User guide covers security responsibilities | O-D | \<User Guide\> \<ver\>, section 5; awaiting the developers (S10, PA-69) |
| SA-05b.03\[02\] | User guide covers privacy responsibilities | O-D | \<User Guide\> \<ver\>, section 4; awaiting the developers (S10, PA-69) |
| SA-05c.\[01\] | Attempts to get missing documents are recorded | O-D | PRO-SA-4 approved; not yet in use |
| SA-05c.\[02\] | Actions are taken for missing documents | O-D | PRO-SA-4 approved; not yet in use |
| SA-05d. | Documentation is distributed | O-D | Drafts not yet distributed |
| SA-08\_ODP\[01\] | Security principles are defined | S | \<System and Services Acquisition Management\> |
| SA-08\_ODP\[02\] | Privacy principles are defined | S | \<System and Services Acquisition Management\> |
| SA-08\[01\] | Security principles in specification | S | \<Security Architecture\> \<ver\>, section 6.5, maps the NCSC principles to the specification |
| SA-08\[02\] | Security principles in design | S | \<Security Architecture\> \<ver\>, section 6.5, maps the NCSC principles to the design |
| SA-08\[03\] | Security principles in development | O-D | Checked from now on through PRO-SA-1; earlier development not checked |
| SA-08\[04\] | Security principles in implementation | O-D | Checked from now on through PRO-SA-1; earlier development not checked |
| SA-08\[05\] | Security principles in modification | O-D | Checked from now on through PRO-SA-1 |
| SA-08\[06\] | Privacy principles in specification | S | \<Security Architecture\> \<ver\>, section 6.5, maps the privacy objectives to the specification |
| SA-08\[07\] | Privacy principles in design | S | \<Security Architecture\> \<ver\>, section 6.5, maps the privacy objectives to the design |
| SA-08\[08\] | Privacy principles in development | O-D | Checked from now on through PRO-SA-1; earlier development not checked |
| SA-08\[09\] | Privacy principles in implementation | O-D | Checked from now on through PRO-SA-1; earlier development not checked |
| SA-08\[10\] | Privacy principles in modification | O-D | Checked from now on through PRO-SA-1 |
| SA-09\_ODP\[01\] | Controls for providers are defined | S | \<System and Services Acquisition Management\> |
| SA-09\_ODP\[02\] | How compliance is monitored is defined | S | \<System and Services Acquisition Management\> |
| SA-09a.\[01\] | Providers comply with security requirements | O-E | EV-SA-02, EV-SA-03 |
| SA-09a.\[02\] | Providers comply with privacy requirements | O-E | EV-SA-02, EV-SA-03 |
| SA-09a.\[03\] | Providers use the set controls | O-E | EV-SA-02, EV-SA-03 |
| SA-09b.\[01\] | Oversight is defined and documented | S | \<System and Services Acquisition Management\>, section 3.7, and PRO-SA-3 |
| SA-09b.\[02\] | User roles are defined and documented | S | \<Roles and Responsibilities\> |
| SA-09c. | Compliance is monitored on an ongoing basis | O-D | No review yet held; TPL-16 every 12 months |
| SA-09(02)\_ODP | Services are defined | S | \<System and Services Acquisition Management\> |
| SA-09(02) | Providers identify functions, ports, protocols and services | O-E | EV-SA-02, EV-SA-03 |
| SA-10\_ODP\[01\] | Stages are selected | S | \<System and Services Acquisition Management\> |
| SA-10\_ODP\[02\] | Items are defined | S | \<System and Services Acquisition Management\> |
| SA-10\_ODP\[03\] | Who is told is defined | S | \<System and Services Acquisition Management\> |
| SA-10a. | Developer performs configuration management | S | Code is in Git on private GitHub repositories (S04) |
| SA-10b.\[01\] | Developer documents the integrity of changes | O-G | No branch protection, required review or signed tags (S01, S05; PA-91) |
| SA-10b.\[02\] | Developer manages the integrity of changes | O-G | No branch protection, required review or signed tags (S01, S05; PA-91) |
| SA-10b.\[03\] | Developer controls the integrity of changes | O-G | No branch protection, required review or signed tags (S01, S05; PA-91) |
| SA-10c. | Only approved changes are made | O-G | No branch protection, required review or signed tags (S01, S05; PA-91) |
| SA-10d.\[01\] | Approved changes are documented | O-D | PRO-SA-1 \<ver\> and TPL-6; not yet in routine use |
| SA-10d.\[02\] | Security effect is documented | O-D | PRO-SA-1 \<ver\> and TPL-6; not yet in routine use |
| SA-10d.\[03\] | Privacy effect is documented | O-D | PRO-SA-1 \<ver\> and TPL-6; not yet in routine use |
| SA-10e.\[01\] | Flaws are tracked | S | Flaws found by the tests are tracked in \<Risk List\> and \<Plan of Action and Milestones\> |
| SA-10e.\[02\] | Flaw fixes are tracked | S | Fixes are tracked by POA&M status and repeat tests |
| SA-10e.\[03\] | Findings are reported | S | Reported to the system owner and security officer through \<Risk List\> |
| SA-11\_ODP\[01\] | Test types are selected | S | \<System and Services Acquisition Management\> |
| SA-11\_ODP\[02\] | Frequency is defined | S | \<System and Services Acquisition Management\> |
| SA-11\_ODP\[03\] | Depth and coverage are defined | S | \<System and Services Acquisition Management\> |
| SA-11a.\[01\] | Security assessment plan is developed | S | Developer test plan in \<System and Services Acquisition Management\>, section 3.9 |
| SA-11a.\[02\] | Security assessment plan is implemented | S | Implemented: the scripts ran on the v1.0 build (the evidence store) |
| SA-11a.\[03\] | Privacy assessment plan is developed | S | Privacy tests in the plan: Test-PersonalData.ps1 (\<System and Services Acquisition Management\>, section 3.9) |
| SA-11a.\[04\] | Privacy assessment plan is implemented | S | Implemented: Q01 to Q10 ran on 11 November 2026 (the PT evidence) |
| SA-11b. | Testing is performed at the set depth and frequency | O-G | Run by hand, with no unit tests or pipeline (S08; PA-68) |
| SA-11c.\[01\] | Evidence of the plan is produced | S | Each run has a README and MANIFEST in the evidence store |
| SA-11c.\[02\] | Test results are produced | S | Results kept with SHA-256 hashes in the evidence store |
| SA-11d. | Flaw fixing can be verified | S | Fixes are verified by running the test again (PRO-SA-2), as for the AC fixes and T45 |
| SA-11e. | Flaws found are corrected | O-D | Corrections wait for the development phase (\<Plan of Action and Milestones\>) |
| SA-15\_ODP\[01\] | Review frequency is defined | S | \<System and Services Acquisition Management\> |
| SA-15\_ODP\[02\] | Security requirements are defined | S | \<System and Services Acquisition Management\> |
| SA-15\_ODP\[03\] | Privacy requirements are defined | S | \<System and Services Acquisition Management\> |
| SA-15a.01\[01\] | Process addresses security | S | \<System and Services Acquisition Management\>, section 3.2 (CSS), and \<Policy\> (SA) \<ver\> |
| SA-15a.01\[02\] | Process addresses privacy | S | \<System and Services Acquisition Management\>, section 3.2, and \<Policy\> (PT) |
| SA-15a.02\[01\] | Process identifies standards | S | CSS, ASVS 5.0 and the NCSC principles (\<System and Services Acquisition Management\>, sections 3.2 and 3.9) |
| SA-15a.02\[02\] | Process identifies tools | S | \<System and Services Acquisition Management\>, section 3.10 |
| SA-15a.03\[01\] | Process documents the tools | S | \<System and Services Acquisition Management\>, section 3.10 |
| SA-15a.03\[02\] | Process documents tool configurations | S | \<System and Services Acquisition Management\>, section 3.10, including the audit setting turned off (PA-92) |
| SA-15a.04 | Process manages changes to itself and its tools | O-D | PRO-SA-6 \<ver\> approved; not yet in use |
| SA-15b.\[01\] | Process is reviewed against security requirements | O-D | No review yet held |
| SA-15b.\[02\] | Process is reviewed against privacy requirements | O-D | No review yet held |
| SA-15(03)\_ODP\[01\] | Decision points are defined | S | \<System and Services Acquisition Management\> |
| SA-15(03)\_ODP\[02\] | Breadth is defined | S | \<System and Services Acquisition Management\> |
| SA-15(03)\_ODP\[03\] | Depth is defined | S | \<System and Services Acquisition Management\> |
| SA-15(03)(a) | Criticality analysis at the set points | S | \<Risk Assessment Management\>, section 3.9, analysed on 11 November 2026 |
| SA-15(03)(b)\[01\] | Analysis at the set breadth | S | \<Risk Assessment Management\>, section 3.9: all components considered |
| SA-15(03)(b)\[02\] | Analysis at the set depth | S | \<Risk Assessment Management\>, section 3.9: critical components identified |
| SA-22\_ODP\[01\] | Support options are selected | S | \<System and Services Acquisition Management\> |
| SA-22\_ODP\[02\] | External support is defined | S | \<System and Services Acquisition Management\> |
| SA-22a. | Components are replaced when support ends | S | No component within 6 months of support ending (S09; \<Maintenance Management\>, section 3.8) |
| SA-22b. | Options for other support are provided | S | In-house support, or a supplier's extended support by exception (\<System and Services Acquisition Management\>) |

### SA.5 Assessment plan

**Table SA-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 17 SA entries in the Moderate baseline, 16 assessed (SA-4(10) tailored), with 159 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0); CSS \<ver\> for the development process |
| Dates | 6 November 2026; updated on 11 November 2026 after the SA pack review |
| Examine | \<Policy\> (SA), \<Procedures\> (SA) and the SA chapter of \<Control Implementation Register\> at \<ver\>, now in \<System and Services Acquisition Management\>; \<Security Architecture\> \<ver\>; \<System Security Plan\>, sections 3, 4 and 7; \<Risk Assessment Management\>; \<Maintenance Management\>; the draft guides; the test evidence folders. Depth: focused. Coverage: focused |
| Test | Test-Development.ps1, checks S01 to S10, read-only, against the six GitHub repositories, the v1.0 history and the build files (evidence in the SA evidence) |
| Interview | None held. The developers, the system owner and \<Organisation\>'s contract owner remain |
| Previous results reused | All family test evidence as the developer test results (\<System and Services Acquisition Management\>, section 3.9); RA checks V01 to V04 on packages and images; MA check M11 on component versions |
| Boundary | \<System Name\>'s development and acquisition. \<Organisation\>'s contracts and services, and GitHub's own controls, are provider evidence (EV-SA-01 to EV-SA-03) |
| Order of assessment | A, change control (SA-10); B, developer testing (SA-11); C, process and tools (SA-3, SA-15); D, documentation (SA-5); E, external services and contracts (SA-4, SA-9); F, policy and resources (SA-1, SA-2) |
| Needed from providers | EV-SA-01, EV-SA-02 and EV-SA-03 in \<Evidence Requests\> |
| Evidence retained | the SA evidence (results, README and MANIFEST); the other evidence folders; completed TPL-6, TPL-16 and TPL-23 records |

For the Level 2 assessment, the assessor should run Test-Development.ps1 again after PA-91, sample merged changes for a recorded review, check the confirmed guides against the screens, and re-determine every statement in section SA.4.

## SC System and Communications Protection

### SC.1 Purpose

This records the Level 1 self-assessment of the 25 SC entries in the CSS Moderate baseline, using catalog release 5.2.0. SC-15 is tailored out (\<Tailoring Register\>, TR-SC-01), so 24 are assessed. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### SC.2 How to read this record

**Change since this assessment.** On 18 November 2026 the communications protection design was cut from \<Control Implementation Register\> into \<System and Communications Protection Management\>, with each control set out part by part (D-SC-09). Since sign-in moved to AD FS (D-AC-23), \<System Name\> has no sign-in pages, so the checks that used them are to be run again. The cross-check added the audit chain key and the AD FS token-signing certificate to the key register, and set out session handling; PA-74 and PA-95 cover them. The findings below are a true record of their dates and are not changed.

**N/A** means not applicable, as decided in \<Tailoring Register\>, which the independent assessor may test.

The methods were **Examine** (code, settings and documents) and **Test**. The test is Test-Protection.ps1, run on 12 November 2026 (checks N01 to N12) against the throwaway docuview-test stack built from the build tagged v1.0, then removed. It sends GET requests to the sign-in pages, runs read-only queries in the database container, and reads the code and settings, printing counts and lengths only. The results and their hashes are in the SC evidence. Check B09 from 6 November is still used for SC-2.

**Correction:** the 6 November hand check B04 recorded that a page policy was set. Test-Protection.ps1 found that UI application and Admin application send none, because their security headers are switched off in the code; only API sends one. SC-18 findings now reflect this.

**Limit of the current evidence:** \<System Name\> ran in Docker on one PC with sample data. The Windows Server 2025 VMs, PostgreSQL on Windows and \<Organisation\>'s services have not been examined.

### SC.3 Executive summary

**Table SC-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 1 | SC-2 |
| Not applicable, subject to the conditions in \<Tailoring Register\> | 1 | SC-15 |
| Other than satisfied, with at least one system gap | 7 | SC-7(5), SC-8, SC-8(1), SC-12, SC-13, SC-18, SC-23 |
| Other than satisfied, needing only a decision, approval or evidence | 16 | SC-1, SC-4, SC-5, SC-7, SC-7(3), SC-7(4), SC-7(7), SC-7(8), SC-10, SC-17, SC-20, SC-21, SC-22, SC-28, SC-28(1), SC-39 |

**Table SC-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| SC-1 | Other than satisfied | 21 of 25 | Not yet shared; Head of Cyber's re-approval (D-SC-06) outstanding | NC-SC-01 |
| SC-2 | Satisfied | 1 of 1 | Separate admin application | Met |
| SC-4 | Other than satisfied | 0 of 2 | VMs not available; export copies in a shared folder | NC-SC-02 |
| SC-5 | Other than satisfied | 3 of 5 | \<Organisation\> not evidenced; rate limiter switched off | NC-SC-03 |
| SC-7 | Other than satisfied | 1 of 7 | \<Organisation\> not evidenced | NC-SC-04 |
| SC-7(3) | Other than satisfied | 0 of 1 | \<Organisation\> not evidenced | NC-SC-05 |
| SC-7(4) | Other than satisfied | 1 of 11 | \<Organisation\> not evidenced | NC-SC-06 |
| SC-7(5) | Other than satisfied | 2 of 4 | Host firewalls not built; apps listen on every interface (N07) | NC-SC-07 |
| SC-7(7) | Other than satisfied | 1 of 2 | \<Organisation\> not evidenced | NC-SC-08 |
| SC-7(8) | Other than satisfied | 2 of 3 | \<Organisation\> not evidenced | NC-SC-09 |
| SC-8 | Other than satisfied | 1 of 2 | Plain HTTP and database TLS off (N01, N06) | NC-SC-10 |
| SC-8(1) | Other than satisfied | 1 of 2 | As SC-8 | NC-SC-11 |
| SC-10 | Other than satisfied | 1 of 2 | Network side not evidenced | NC-SC-12 |
| SC-12 | Other than satisfied | 1 of 3 | Keys in source; key rings unencrypted (N08, N09) | NC-SC-13 |
| SC-13 | Other than satisfied | 3 of 4 | TLS, disk and key ring encryption not in place | NC-SC-14 |
| SC-15 | Not applicable | 0 of 3 | TR-SC-01 | None |
| SC-17 | Other than satisfied | 1 of 3 | \<Organisation\> not evidenced | NC-SC-15 |
| SC-18 | Other than satisfied | 5 of 7 | No page policy on UI application and Admin application (N04) | NC-SC-16 |
| SC-20 | Other than satisfied | 0 of 4 | \<Organisation\> not evidenced | NC-SC-17 |
| SC-21 | Other than satisfied | 0 of 4 | \<Organisation\> not evidenced | NC-SC-18 |
| SC-22 | Other than satisfied | 0 of 3 | \<Organisation\> not evidenced | NC-SC-19 |
| SC-23 | Other than satisfied | 0 of 1 | Cookies not Secure; no HSTS (N02, N03) | NC-SC-20 |
| SC-28 | Other than satisfied | 2 of 3 | VMs not built; nothing encrypted at rest in Docker | NC-SC-21 |
| SC-28(1) | Other than satisfied | 2 of 4 | As SC-28 | NC-SC-22 |
| SC-39 | Other than satisfied | 0 of 1 | Windows Server not available | NC-SC-23 |

Of the CSS 107 statements, 49 are satisfied, 3 are not applicable, 4 await a decision or approval, 10 show a gap in the system and 41 await evidence from the VMs or \<Organisation\>.

The gaps within \<System Name\> are plain traffic on every flow, keys in source and unencrypted key rings, no page policy on the two web apps, and apps listening on every interface. Most of the rest depends on \<Organisation\>'s network and the VMs.

### SC.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 12 November 2026 unless the basis says otherwise.

**Table SC-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| SC-01\_ODP\[01\] | Who receives the policy is defined | S | \<Organisation\>'s corporate parameter values |
| SC-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Organisation\>'s corporate parameter values |
| SC-01\_ODP\[03\] | Policy level is selected | S | \<Organisation\>'s corporate parameter values |
| SC-01\_ODP\[04\] | Managing official is defined | S | System owner |
| SC-01\_ODP\[05\] | Policy review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SC-01\_ODP\[06\] | Policy review events are defined | S | \<Organisation\>'s corporate parameter values |
| SC-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SC-01\_ODP\[08\] | Procedures review events are defined | S | \<Organisation\>'s corporate parameter values |
| SC-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber, subject to legal review (D-SC-01); version \<ver\> awaits re-approval (D-SC-06) |
| SC-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| SC-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-SC-08) |
| SC-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| SC-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (SC) \<ver\>, section SC.1 |
| SC-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (SC) \<ver\>, section SC.1 |
| SC-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (SC) \<ver\>, section SC.5 |
| SC-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (SC) \<ver\>, section SC.5 |
| SC-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (SC) \<ver\>, section SC.6 |
| SC-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (SC) \<ver\>, section SC.6 |
| SC-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (SC) \<ver\>, section SC.6 |
| SC-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| SC-01b. | Official is designated | S | \[Name\] is the system owner |
| SC-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| SC-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 12 November 2026 after the SC pack review (D-SC-07) |
| SC-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| SC-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 12 November 2026 (D-SC-08) |
| SC-02 | User and management functions are separated | S | Separate admin application and process (B09; \<System and Communications Protection Management\>, section 3.9) |
| SC-04\[01\] | Unauthorised transfer through shared resources is prevented | O-E | VMs not available (PA-54); export copies stay in a shared temporary folder (PA-86) |
| SC-04\[02\] | Unintended transfer through shared resources is prevented | O-E | VMs not available (PA-54); export copies stay in a shared temporary folder (PA-86) |
| SC-05\_ODP\[01\] | Denial-of-service events are defined | S | \<Organisation\>'s corporate parameter values |
| SC-05\_ODP\[02\] | Protect or limit is selected | S | Limit |
| SC-05\_ODP\[03\] | Controls are defined | S | \<Organisation\>'s corporate parameter values |
| SC-05a. | The effects are limited | O-E | \<Organisation\> (EV-SC-01). No rate limiter; the rate limit is switched off in the code (N12, PA-50) |
| SC-05b. | The controls are employed | O-E | Lockout tested; network not available |
| SC-07\_ODP | Separation is selected | S | Logical |
| SC-07a.\[01\] | External interfaces are monitored | O-E | \<Organisation\> (EV-SC-02) |
| SC-07a.\[02\] | External interfaces are controlled | O-E | \<Organisation\> (EV-SC-02) |
| SC-07a.\[03\] | Key internal interfaces are monitored | O-E | \<Organisation\> (EV-SC-02) |
| SC-07a.\[04\] | Key internal interfaces are controlled | O-E | \<Organisation\> (EV-SC-02) |
| SC-07b. | Public subnetworks are separated | O-E | No public component planned; network not available |
| SC-07c. | External connections use managed interfaces | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(03) | External connections are limited | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)\_ODP | Exception review is defined | S | Every 12 months |
| SC-07(04)(a) | Each telecoms service has a managed interface | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(b) | A flow policy exists for each interface | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(c)\[01\] | Confidentiality across interfaces is protected | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(c)\[02\] | Integrity across interfaces is protected | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(d) | Exceptions are documented | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(e)\[01\] | Exceptions are reviewed | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(e)\[02\] | Unneeded exceptions are removed | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(f) | Unauthorised control plane traffic is prevented | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(g) | Information is published for remote networks | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(04)(h) | Unauthorised control plane traffic is filtered | O-E | \<Organisation\> (EV-SC-02) |
| SC-07(05)\_ODP\[01\] | Where deny by default applies is selected | S | At managed interfaces and each host firewall (\<Organisation\>'s corporate parameter values) |
| SC-07(05)\_ODP\[02\] | Systems are defined | S | The two VMs |
| SC-07(05)\[01\] | Traffic is denied by default | O-G | Allow-lists set (\<System and Communications Protection Management\>, section 3.2) but not built; the apps listen on every interface (N07, PA-83); \<Organisation\> (EV-AC-03) |
| SC-07(05)\[02\] | Traffic is allowed by exception | O-G | As SC-07(05)\[01\] |
| SC-07(07)\_ODP | Safeguards are defined | S | \<Organisation\>'s VPN prevents split tunnelling (\<Organisation\>'s corporate parameter values; D-SC-P02) |
| SC-07(07) | Split tunnelling is prevented | O-E | \<Organisation\> (EV-SC-03) |
| SC-07(08)\_ODP\[01\] | Traffic is defined | S | Outbound from the VMs |
| SC-07(08)\_ODP\[02\] | External networks are defined | S | All |
| SC-07(08) | Traffic is routed through authenticated proxies | O-E | \<Organisation\> (EV-SC-03) |
| SC-08\_ODP | Protection is selected | S | Confidentiality and integrity |
| SC-08 | Transmitted information is protected | O-G | Plain HTTP on every app and the internal API calls; database TLS off (N01, N06; PA-18) |
| SC-08(01)\_ODP | Purpose is selected | S | \<System and Communications Protection Management\>, section 3.3 |
| SC-08(01) | Cryptography protects transmission | O-G | No TLS on any flow (N01, N02, N06; PA-18) |
| SC-10\_ODP | Time period is defined | S | 30 minutes idle |
| SC-10 | Network connections end at that time | O-E | Application sessions end at 30 minutes idle and 8 hours; network side not available (EV-SC-01) |
| SC-12\_ODP | Key requirements are defined | S | \<System and Communications Protection Management\>, section 3.4 |
| SC-12\[01\] | Keys are established | O-G | Register set (\<System and Communications Protection Management\>, section 3.4); signing key and passwords committed in source (N09, PA-19) |
| SC-12\[02\] | Keys are managed | O-G | No protected store or rotation (PA-19); key rings unencrypted (N08, PA-93) |
| SC-13\_ODP\[01\] | Cryptographic uses are defined | S | \<Organisation\>'s corporate parameter values |
| SC-13\_ODP\[02\] | Types are defined | S | \<System and Communications Protection Management\>, section 3.3 and section 3.4 (D-SC-P02) |
| SC-13a. | Uses are identified | S | \<System and Communications Protection Management\>, section 3.4 |
| SC-13b. | Types are implemented | O-G | Password hashing and token signing in place (N11); TLS, disk and key ring encryption not; document checksums use MD5 (PA-18, PA-52, PA-93, PA-61) |
| SC-15\_ODP | Exceptions are defined | N/A | TR-SC-01 |
| SC-15a. | Remote activation is prohibited | N/A | TR-SC-01 |
| SC-15b. | Use is indicated to those present | N/A | TR-SC-01 |
| SC-17\_ODP | Certificate policy is defined | S | \<Organisation\>'s corporate parameter values |
| SC-17a. | Certificates are issued under the policy | O-E | \<Organisation\> (EV-SC-04) |
| SC-17b. | Only approved trust anchors are used | O-E | \<Organisation\> (EV-SC-04) |
| SC-18a.\[01\] | Acceptable mobile code is defined | S | \<System and Communications Protection Management\>, section 3.5 (D-SC-03) |
| SC-18a.\[02\] | Unacceptable mobile code is defined | S | \<System and Communications Protection Management\>, section 3.5 (D-SC-03) |
| SC-18a.\[03\] | Acceptable technologies are defined | S | \<System and Communications Protection Management\>, section 3.5 (D-SC-03) |
| SC-18a.\[04\] | Unacceptable technologies are defined | S | \<System and Communications Protection Management\>, section 3.5 (D-SC-03) |
| SC-18b.\[01\] | Use is authorised | S | Approved in \<System and Communications Protection Management\>, section 3.5 (D-SC-03) |
| SC-18b.\[02\] | Use is monitored | O-G | Nothing monitors it; checked only by Test-Protection.ps1 at release (N04, N10; PA-51) |
| SC-18b.\[03\] | Use is controlled | O-G | UI application and Admin application send no page policy; the configured policy allows inline scripts, eval and outside hosts (N04, N10, N12; PA-34, PA-51) |
| SC-20a.\[01\] | Origin authentication comes with DNS answers | O-E | \<Organisation\> (EV-SC-05) |
| SC-20a.\[02\] | Integrity artefacts come with DNS answers | O-E | \<Organisation\> (EV-SC-05) |
| SC-20b.\[01\] | Child zone security status is shown | O-E | \<Organisation\> (EV-SC-05) |
| SC-20b.\[02\] | Chain of trust can be verified | O-E | \<Organisation\> (EV-SC-05) |
| SC-21\[01\] | Origin authentication is requested | O-E | \<Organisation\> (EV-SC-05) |
| SC-21\[02\] | Origin authentication is performed | O-E | \<Organisation\> (EV-SC-05) |
| SC-21\[03\] | Integrity verification is requested | O-E | \<Organisation\> (EV-SC-05) |
| SC-21\[04\] | Integrity verification is performed | O-E | \<Organisation\> (EV-SC-05) |
| SC-22\[01\] | DNS systems are fault tolerant | O-E | \<Organisation\> (EV-SC-05) |
| SC-22\[02\] | Internal and external roles are separated | O-E | \<Organisation\> (EV-SC-05) |
| SC-22\[03\] | Roles are separated by exposure | O-E | \<Organisation\> (EV-SC-05) |
| SC-23 | Session authenticity is protected | O-G | Sessions are checked on the server, but cookies are not Secure, there is no HSTS and traffic is plain HTTP (N02, N03; PA-18); key rings unencrypted (PA-93) |
| SC-28\_ODP\[01\] | Protection is selected | S | Confidentiality and integrity |
| SC-28\_ODP\[02\] | Information is defined | S | \<Organisation\>'s corporate parameter values |
| SC-28 | Information at rest is protected | O-E | Documents in PostgreSQL, backups, export copies and key rings not encrypted in Docker; BitLocker planned on the VMs (PA-52, PA-86, PA-93) |
| SC-28(01)\_ODP\[01\] | Information is defined | S | \<Organisation\>'s corporate parameter values |
| SC-28(01)\_ODP\[02\] | Components are defined | S | \<Organisation\>'s corporate parameter values |
| SC-28(01)\[01\] | Cryptography prevents disclosure | O-E | VMs not built (PA-52); key rings and export copies unencrypted (PA-86, PA-93) |
| SC-28(01)\[02\] | Cryptography prevents modification | O-E | VMs not built (PA-52) |
| SC-39 | Each process has its own execution domain | O-E | Windows Server not available |

### SC.5 Assessment plan

**Table SC-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 25 SC entries in the Moderate baseline, 24 assessed (SC-15 tailored), with 107 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0); NCSC's TLS guidance and CSS for the values |
| Dates | 6 November 2026; updated on 12 November 2026 after the SC pack review |
| Examine | \<Policy\> (SC), \<Procedures\> (SC) and the SC chapter of \<Control Implementation Register\> at \<ver\>, now in \<System and Communications Protection Management\>; \<Security Architecture\> \<ver\>; \<System Security Plan\>, sections 3.7, 4 and 7; the start-up configuration, the security headers component, the API's sign-in service, the API's password service, the settings files and the test stack's compose file at tag v1.0. Depth: focused. Coverage: focused |
| Test | Test-Protection.ps1, checks N01 to N12, on the throwaway docuview-test stack (evidence in the SC evidence); B09 by hand on 6 November 2026 |
| Interview | None held. The Windows server administrator, database administrator, developers and \<Organisation\>'s security contact remain |
| Previous results reused | CM checks C07 to C10 (secrets, listening addresses, non-root); MP checks on export copies (PA-86); MA check M04 on the admin portal (PA-83) |
| Boundary | \<System Name\>'s apps, database, keys and the two VMs. \<Organisation\>'s network, VPN, proxy, DNS and certificate authority are provider evidence (EV-SC-01 to EV-SC-05) |
| Order of assessment | A, transport and sessions (SC-8, SC-8(1), SC-23); B, keys and cryptography (SC-12, SC-13); C, page code (SC-18); D, boundary (SC-7 and enhancements); E, data at rest (SC-28); F, inherited services (SC-17, SC-20 to SC-22, SC-39); G, policy (SC-1) |
| Needed from providers | EV-SC-01 to EV-SC-05 and EV-AC-03 in \<Evidence Requests\> |
| Evidence retained | the SC evidence (results, README and MANIFEST); the SC and CM evidence; completed TPL-6, TPL-8, TPL-11 and TPL-23 records |

For the Level 2 assessment, the assessor should run Test-Protection.ps1 against the VMs, run an outside TLS scan of the web address, check the host firewall rules against \<System and Communications Protection Management\>, section 3.2, confirm BitLocker and the key ring protection, hold the interviews, and re-determine every statement in section SC.4.

## SI System and Information Integrity

### SI.1 Purpose

This records the Level 1 self-assessment of the 18 SI entries in the CSS Moderate baseline, using catalog release 5.2.0. SI-8 and SI-8(2) are tailored out (\<Tailoring Register\>, TR-SI-01), so 16 are assessed. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### SI.2 How to read this record

**Change since this assessment.** On 18 November 2026 the integrity design was cut from \<Control Implementation Register\> into \<System and Information Integrity Management\>, with each control set out part by part (D-SI-10). Detection use cases U1 and U4 now take their events from \<Organisation\>'s AD FS and Active Directory (D-SR-15). The cross-check added a one-off scan of documents already stored (PA-58). The findings below are a true record of their dates and are not changed.

**N/A** means not applicable, as decided in \<Tailoring Register\>, which the independent assessor may test.

The methods were **Examine** (code, settings and documents) and **Test**. The test is Test-Integrity.ps1, run on 12 November 2026 (checks H01 to H12) against the throwaway docuview-test stack built from the build tagged v1.0, then removed. Upload checks used the API's dry-run endpoint, which stores nothing. The results, the integrity baseline and their hashes are in the SI evidence. Package findings come from Test-Vulnerability.ps1 (RA, 11 November 2026).

**Limit of the current evidence:** \<System Name\> ran in Docker on one PC with sample data. The Windows Server 2025 VMs, Defender, PostgreSQL on Windows and \<Organisation\>'s services have not been examined.

### SI.3 Executive summary

**Table SI-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 2 | SI-7(7), SI-10 |
| Not applicable, subject to the conditions in \<Tailoring Register\> | 2 | SI-8, SI-8(2) |
| Other than satisfied, with at least one system gap | 8 | SI-2, SI-2(2), SI-3, SI-4(2), SI-4(5), SI-7, SI-7(1), SI-11 |
| Other than satisfied, needing only a decision, approval or evidence | 6 | SI-1, SI-4, SI-4(4), SI-5, SI-12, SI-16 |

**Table SI-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| SI-1 | Other than satisfied | 21 of 25 | Not yet shared; Head of Cyber's re-approval (D-SI-06) outstanding; legally reviewed | NC-SI-01 |
| SI-2 | Other than satisfied | 4 of 11 | 7 package advisories open (PA-56) | NC-SI-02 |
| SI-2(2) | Other than satisfied | 2 of 3 | Checks run by hand (PA-57) | NC-SI-03 |
| SI-3 | Other than satisfied | 6 of 14 | Uploads not scanned (H08) | NC-SI-04 |
| SI-4 | Other than satisfied | 6 of 18 | Reviews not started; \<Organisation\> not evidenced | NC-SI-05 |
| SI-4(2) | Other than satisfied | 0 of 1 | No automated analysis (H12) | NC-SI-06 |
| SI-4(4) | Other than satisfied | 4 of 8 | \<Organisation\> not evidenced | NC-SI-07 |
| SI-4(5) | Other than satisfied | 2 of 3 | No alerts (H12) | NC-SI-08 |
| SI-5 | Other than satisfied | 5 of 9 | Not yet in use | NC-SI-09 |
| SI-7 | Other than satisfied | 6 of 12 | MD5 checksums; chain does not verify (H09, H10) | NC-SI-10 |
| SI-7(1) | Other than satisfied | 12 of 15 | Checks not built | NC-SI-11 |
| SI-7(7) | Satisfied | 2 of 2 | PRO-SI-6 | Met |
| SI-8 | Not applicable | 0 of 5 | TR-SI-01 | None |
| SI-8(2) | Not applicable | 0 of 2 | TR-SI-01 | None |
| SI-10 | Satisfied | 2 of 2 | Tested (H03 to H07) | Met |
| SI-11 | Other than satisfied | 1 of 3 | API leaks exception detail (H01) | NC-SI-14 |
| SI-12 | Other than satisfied | 0 of 4 | Retention schedule not applied | NC-SI-15 |
| SI-16 | Other than satisfied | 1 of 2 | Windows protections on the VMs | NC-SI-16 |

Of the CSS 139 statements, 74 are satisfied, 7 are not applicable, 22 await a decision or approval, 13 show a gap in the system and 23 await evidence from the VMs or \<Organisation\>.

The gaps within \<System Name\> are open package advisories, no malware scan of uploads, no alerting, MD5 document checksums and an audit chain that cannot be recomputed, and exception detail returned by the API. Input validation and the upload type checks work.

### SI.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 12 November 2026 unless the basis says otherwise.

**Table SI-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| SI-01\_ODP\[01\] | Who receives the policy is defined | S | \<Organisation\>'s corporate parameter values |
| SI-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Organisation\>'s corporate parameter values |
| SI-01\_ODP\[03\] | Policy level is selected | S | \<Organisation\>'s corporate parameter values |
| SI-01\_ODP\[04\] | Managing official is defined | S | System owner |
| SI-01\_ODP\[05\] | Policy review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-01\_ODP\[06\] | Policy review events are defined | S | \<Organisation\>'s corporate parameter values |
| SI-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-01\_ODP\[08\] | Procedures review events are defined | S | \<Organisation\>'s corporate parameter values |
| SI-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber, subject to legal review (D-SI-01); version \<ver\> awaits re-approval (D-SI-06) |
| SI-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| SI-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-SI-09) |
| SI-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| SI-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (SI) \<ver\>, section SI.1 |
| SI-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (SI) \<ver\>, section SI.1 |
| SI-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (SI) \<ver\>, section SI.5 |
| SI-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (SI) \<ver\>, section SI.5 |
| SI-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (SI) \<ver\>, section SI.6 |
| SI-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (SI) \<ver\>, section SI.6 |
| SI-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (SI) \<ver\>, section SI.6 |
| SI-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| SI-01b. | Official is designated | S | \[Name\] is the system owner |
| SI-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| SI-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 12 November 2026 after the SI pack review (D-SI-08) |
| SI-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| SI-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 12 November 2026 (D-SI-09) |
| SI-02\_ODP | Time to install updates is defined | S | \<Organisation\>'s corporate parameter values (\<Risk Assessment Management\>, section 3.6) |
| SI-02a.\[01\] | Flaws are identified | S | Test-Vulnerability.ps1, 11 November 2026 (V01) |
| SI-02a.\[02\] | Flaws are reported | S | \<Plan of Action and Milestones\>, PA-56 |
| SI-02a.\[03\] | Flaws are corrected | O-G | 7 advisories open, 5 High (PA-56) |
| SI-02b.\[01\] | Software updates are tested for effect | O-D | PRO-SI-1 \<ver\> approved; not yet in use |
| SI-02b.\[02\] | Software updates are tested for side effects | O-D | PRO-SI-1 \<ver\> approved; not yet in use |
| SI-02b.\[03\] | Firmware updates are tested for effect | O-E | \<Organisation\> (EV-SI-02) |
| SI-02b.\[04\] | Firmware updates are tested for side effects | O-E | \<Organisation\> (EV-SI-02) |
| SI-02c.\[01\] | Software updates are installed in time | O-G | Advisories not fixed within the timetable (PA-56) |
| SI-02c.\[02\] | Firmware updates are installed in time | O-E | \<Organisation\> (EV-SI-02) |
| SI-02d. | Flaw fixing is part of configuration management | S | PRO-SI-1 \<ver\>, through \<Procedures\> (CM) (D-SI-09) |
| SI-02(02)\_ODP\[01\] | Mechanisms are defined | S | \<Organisation\>'s corporate parameter values |
| SI-02(02)\_ODP\[02\] | Frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-02(02) | Update status is checked automatically | O-G | Test-Vulnerability.ps1 exists but is run by hand; dependency alerts off (PA-57, PA-91) |
| SI-03\_ODP\[01\] | Type of protection is selected | S | \<Organisation\>'s corporate parameter values |
| SI-03\_ODP\[02\] | Scan frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-03\_ODP\[03\] | Real-time scan locations are selected | S | \<Organisation\>'s corporate parameter values |
| SI-03\_ODP\[04\] | Response is selected | S | \<Organisation\>'s corporate parameter values |
| SI-03\_ODP\[05\] | Other action is defined | S | \<Organisation\>'s corporate parameter values |
| SI-03\_ODP\[06\] | Who is alerted is defined | S | \<Organisation\>'s corporate parameter values |
| SI-03a.\[01\] | Protection detects malicious code at entry | O-G | No scanner call in the upload path (H08; PA-58) |
| SI-03a.\[02\] | Protection eradicates malicious code at entry | O-G | No scanner call in the upload path (H08; PA-58) |
| SI-03b. | Protection updates automatically | O-E | On the VMs |
| SI-03c.01\[01\] | Periodic scans are set | O-E | On the VMs |
| SI-03c.01\[02\] | Real-time scans are set | O-E | On the VMs |
| SI-03c.02\[01\] | Response to detection is set | O-E | On the VMs |
| SI-03c.02\[02\] | Alerts on detection are set | O-E | On the VMs |
| SI-03d. | False positives are addressed | O-D | PRO-SI-2 \<ver\> approved; not yet in use |
| SI-04\_ODP\[01\] | Monitoring objectives are defined | S | \<Organisation\>'s corporate parameter values |
| SI-04\_ODP\[02\] | Techniques are defined | S | \<Organisation\>'s corporate parameter values |
| SI-04\_ODP\[03\] | Monitoring information is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04\_ODP\[04\] | Who receives it is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04\_ODP\[05\] | When it is provided is selected | S | \<Organisation\>'s corporate parameter values |
| SI-04\_ODP\[06\] | Frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04a.01 | Attacks are monitored for | O-E | \<Organisation\> (EV-SI-01) |
| SI-04a.02\[01\] | Unauthorised local connections are monitored for | O-E | On the VMs |
| SI-04a.02\[02\] | Unauthorised network connections are monitored for | O-E | \<Organisation\> (EV-SI-01) |
| SI-04a.02\[03\] | Unauthorised remote connections are monitored for | O-E | \<Organisation\> (EV-SI-01) |
| SI-04b. | Unauthorised use is identified | O-D | PRO-SI-3 \<ver\> approved; reviews not started |
| SI-04c.01 | Monitoring is placed to collect key information | O-E | On the VMs |
| SI-04c.02 | Monitoring is placed to track specific transactions | O-E | On the VMs |
| SI-04d.\[01\] | Events are analysed | O-D | Reviews not started |
| SI-04d.\[02\] | Anomalies are analysed | O-D | Reviews not started |
| SI-04e. | Monitoring level changes when risk changes | O-D | PRO-SI-3 \<ver\> approved; not yet in use |
| SI-04f. | A legal opinion on monitoring is obtained | O-D | Legal adviser's opinion on monitoring users requested (D-SI-07) |
| SI-04g. | Monitoring information is provided | O-E | Reviews not started; \<Organisation\> (EV-SI-01) |
| SI-04(02) | Automated tools support near real-time analysis | O-G | No log forwarding or alerting (H12; PA-59) |
| SI-04(04)\_ODP\[01\] | Inbound monitoring frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04(04)\_ODP\[02\] | Unusual inbound activity is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04(04)\_ODP\[03\] | Outbound monitoring frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04(04)\_ODP\[04\] | Unusual outbound activity is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04(04)(a)\[01\] | Inbound criteria are determined | O-E | \<Organisation\> (EV-SI-01) |
| SI-04(04)(a)\[02\] | Outbound criteria are determined | O-E | \<Organisation\> (EV-SI-01) |
| SI-04(04)(b)\[01\] | Inbound traffic is monitored | O-E | \<Organisation\> (EV-SI-01) |
| SI-04(04)(b)\[02\] | Outbound traffic is monitored | O-E | \<Organisation\> (EV-SI-01) |
| SI-04(05)\_ODP\[01\] | Who is alerted is defined | S | \<Organisation\>'s corporate parameter values |
| SI-04(05)\_ODP\[02\] | Compromise indicators are defined | S | \<Organisation\>'s corporate parameter values |
| SI-04(05) | Alerts are raised on those indicators | O-G | Nothing raises an alert on the use cases in \<System and Information Integrity Management\>, section 3.4 (H12; PA-59) |
| SI-05\_ODP\[01\] | Sources are defined | S | \<Organisation\>'s corporate parameter values |
| SI-05\_ODP\[02\] | Who advisories go to is selected | S | \<Organisation\>'s corporate parameter values |
| SI-05\_ODP\[03\] | Personnel are defined | S | \<Organisation\>'s corporate parameter values |
| SI-05\_ODP\[04\] | Elements are defined | S | \<Organisation\>'s corporate parameter values |
| SI-05\_ODP\[05\] | External organisations are defined | S | \<Organisation\>'s corporate parameter values |
| SI-05a. | Advisories are received | O-D | PRO-SI-5 \<ver\> approved; not yet in use |
| SI-05b. | Internal advisories are generated | O-D | Internal advisory defined (TPL-7); not yet in use |
| SI-05c. | Advisories are passed on | O-D | PRO-SI-5 \<ver\> approved; not yet in use |
| SI-05d. | Directives are implemented in time | O-D | PRO-SI-5 \<ver\> approved; not yet in use |
| SI-07\_ODP\[01\] | Software is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07\_ODP\[02\] | Firmware is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07\_ODP\[03\] | Information is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07\_ODP\[04\] | Actions for software are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07\_ODP\[05\] | Actions for firmware are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07\_ODP\[06\] | Actions for information are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07a.\[01\] | Tools detect changes to software | O-G | Baseline recorded (\<System and Information Integrity Management\>, section 3.5); no check runs (PA-61) |
| SI-07a.\[02\] | Tools detect changes to firmware | O-E | \<Organisation\> (EV-SI-02) |
| SI-07a.\[03\] | Tools detect changes to information | O-G | Documents use MD5 (H09); only 1 of 15 audit hashes recompute (H10; PA-61, PA-74) |
| SI-07b.\[01\] | Actions are taken on software changes | O-D | PRO-SI-6 \<ver\> approved; not yet in use |
| SI-07b.\[02\] | Actions are taken on firmware changes | O-E | \<Organisation\> (EV-SI-02) |
| SI-07b.\[03\] | Actions are taken on information changes | O-D | PRO-SI-6 \<ver\> approved; not yet in use |
| SI-07(01)\_ODP\[01\] | Software checked is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[02\] | When it is checked is selected | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[03\] | Events are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[04\] | Frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[05\] | Firmware checked is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[06\] | When it is checked is selected | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[07\] | Events are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[08\] | Frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[09\] | Information checked is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[10\] | When it is checked is selected | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[11\] | Events are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\_ODP\[12\] | Frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(01)\[01\] | Software is checked | O-G | Not built (PA-61) |
| SI-07(01)\[02\] | Firmware is checked | O-E | \<Organisation\> (EV-SI-02) |
| SI-07(01)\[03\] | Information is checked | O-G | Not built (PA-37, PA-61, PA-74) |
| SI-07(07)\_ODP | Changes for incident response are defined | S | \<Organisation\>'s corporate parameter values |
| SI-07(07) | Detected changes go to incident response | S | PRO-SI-6 \<ver\>, approved (D-SI-09) |
| SI-08a.\[01\] | Spam is detected at entry | N/A | TR-SI-01 |
| SI-08a.\[02\] | Spam is detected at exit | N/A | TR-SI-01 |
| SI-08a.\[03\] | Spam is acted on at entry | N/A | TR-SI-01 |
| SI-08a.\[04\] | Spam is acted on at exit | N/A | TR-SI-01 |
| SI-08b. | Spam protection is updated | N/A | TR-SI-01 |
| SI-08(02)\_ODP | Update frequency is defined | N/A | TR-SI-01 |
| SI-08(02) | Spam protection updates automatically | N/A | TR-SI-01 |
| SI-10\_ODP | Inputs are defined | S | \<Organisation\>'s corporate parameter values |
| SI-10 | Validity of inputs is checked | S | Tested on 12 November 2026: injection-style input refused, and wrong signatures, disguised executables, unknown types and paths rejected (H03 to H07) |
| SI-11\_ODP | Who sees detail is defined | S | \<Organisation\>'s corporate parameter values |
| SI-11a. | Errors give what is needed without revealing detail | O-G | A malformed upload returns the exception message; about 29 API responses do so (H01; PA-60) |
| SI-11b. | Error detail goes only to those named | O-G | Exception detail reaches callers, not only administrators (H01; PA-60) |
| SI-12\[01\] | Information is managed under the rules | O-D | \<PII Processing Management\>, section 3.7, set with placeholders; not applied (PA-70) |
| SI-12\[02\] | Information is retained under the rules | O-D | \<PII Processing Management\>, section 3.7, set with placeholders; not applied (PA-70) |
| SI-12\[03\] | Output is managed under the rules | O-D | Export copies not yet deleted reliably (PA-86); schedule not applied (PA-70) |
| SI-12\[04\] | Output is retained under the rules | O-D | \<PII Processing Management\>, section 3.7, set with placeholders; not applied (PA-70) |
| SI-16\_ODP | Memory controls are defined | S | \<Organisation\>'s corporate parameter values |
| SI-16 | Controls protect memory | O-E | .NET managed memory and non-root containers in place; Windows DEP and address randomisation to confirm on the VMs |

### SI.5 Assessment plan

**Table SI-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 18 SI entries in the Moderate baseline, 16 assessed (SI-8 and SI-8(2) tailored), with 139 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 12 November 2026 after the SI pack review |
| Examine | \<Policy\> (SI), \<Procedures\> (SI) and the SI chapter of \<Control Implementation Register\> at \<ver\>, now in \<System and Information Integrity Management\>; \<Risk Assessment Management\>, section 3.6; \<PII Processing Management\>, section 3.7; the upload, validation, audit and error-handling code at tag v1.0. Depth: focused. Coverage: focused |
| Test | Test-Integrity.ps1, checks H01 to H12, on the throwaway docuview-test stack (evidence in the SI evidence); Test-Vulnerability.ps1 (the RA evidence) |
| Interview | None held. The security officer, Windows server administrator and \<Organisation\>'s security contact remain |
| Previous results reused | RA check V01 (packages); AU checks A36 and A37 (audit chain); CM check C08 (non-root containers) |
| Boundary | \<System Name\>'s apps, database and records. \<Organisation\>'s network monitoring, firmware and logging are provider evidence (EV-SI-01 to EV-SI-03) |
| Order of assessment | A, flaws (SI-2); B, malicious code and uploads (SI-3, SI-10); C, monitoring and alerts (SI-4); D, integrity (SI-7); E, errors (SI-11); F, advisories, retention and memory (SI-5, SI-12, SI-16); G, policy (SI-1) |
| Needed from providers | EV-SI-01, EV-SI-02 and EV-SI-03 in \<Evidence Requests\> |
| Evidence retained | the SI evidence (results, baseline, README and MANIFEST); the RA evidence; completed TPL-7, TPL-8 and TPL-10 records |

For the Level 2 assessment, the assessor should run Test-Integrity.ps1 and Test-Vulnerability.ps1 against the VMs, upload the EICAR test file once scanning is built, check Defender and the alert rules, compare release packages with the baseline, hold the interviews, and re-determine every statement in section SI.4.

## SR Supply Chain Risk Management

### SR.1 Purpose

This records the Level 1 self-assessment of the 12 SR entries in the CSS Moderate baseline, using catalog release 5.2.0. An independent team led by \[Name\] will use it for the Level 2 assessment. It makes no fixes.

### SR.2 How to read this record

**Change since this assessment.** On 18 November 2026 the supply chain plan was rebuilt in the family form and renamed Supply Chain Risk Management (D-SR-14). Its parameter register is now appendix A, and section 3 is the plan. The findings below are a true record of their dates and are not changed.

The methods were **Examine** (code, settings and documents) and **Test**. The test is Test-SupplyChain.ps1, run on 12 November 2026 (checks U01 to U10) on the build tagged v1.0 and the images built from it, with no running stack. The results and their hashes are in the SR evidence.

**Limit of the current evidence:** the VMs are not built, and \<Organisation\>'s supplier, hardware and disposal processes have not been examined.

### SR.3 Executive summary

**Table SR-1: Results by control**

| Result | Count | Controls |
| --- | --- | --- |
| Satisfied | 0 | None |
| Other than satisfied, with at least one system gap | 3 | SR-3, SR-5, SR-10 |
| Other than satisfied, needing only a decision, approval or evidence | 9 | SR-1, SR-2, SR-2(1), SR-6, SR-8, SR-11, SR-11(1), SR-11(2), SR-12 |

**Table SR-2: Result for each control**

| Control | Result | Statements satisfied | Main reason | Finding |
| --- | --- | --- | --- | --- |
| SR-1 | Other than satisfied | 21 of 25 | Not yet shared; Head of Cyber's re-approval (D-SR-12) outstanding; legally reviewed | NC-SR-01 |
| SR-2 | Other than satisfied | 11 of 14 | Not yet reviewed or in the restricted store | NC-SR-02 |
| SR-2(1) | Other than satisfied | 2 of 3 | Team not confirmed by \<Organisation\> | NC-SR-03 |
| SR-3 | Other than satisfied | 6 of 9 | Only OfflineModules packages use the offline feed (U01) | NC-SR-04 |
| SR-5 | Other than satisfied | 2 of 4 | Packages acquired from nuget.org unchecked (U01) | NC-SR-05 |
| SR-6 | Other than satisfied | 1 of 2 | No supplier review held | NC-SR-06 |
| SR-8 | Other than satisfied | 2 of 3 | \<Organisation\>'s terms not seen | NC-SR-07 |
| SR-10 | Other than satisfied | 4 of 5 | No release checksums or bill of materials | NC-SR-08 |
| SR-11 | Other than satisfied | 3 of 8 | Not yet in use | NC-SR-09 |
| SR-11(1) | Other than satisfied | 1 of 2 | Training not seen | NC-SR-10 |
| SR-11(2) | Other than satisfied | 1 of 3 | Repair process not seen | NC-SR-11 |
| SR-12 | Other than satisfied | 2 of 3 | Disposal not seen | NC-SR-12 |

Of the CSS 81 statements, 56 are satisfied, 16 await a decision or approval, 4 show a gap in the system and 5 await evidence from \<Organisation\>.

The gaps within \<System Name\> are that packages other than the in-house OfflineModules come straight from nuget.org with no lock file or signature policy, images are not pinned, and releases have no checksums or bill of materials. The offline feed itself is intact (U05), and the release images match the integrity baseline (U08).

### SR.4 Findings by determination statement

There is one finding for each CSS determination statement, including those about organisation-defined parameters. Findings are dated 12 November 2026 unless the basis says otherwise.

**Table SR-3: Finding for each determination statement**

| Statement | Determination, condensed | Finding | Basis |
| --- | --- | --- | --- |
| SR-01\_ODP\[01\] | Who receives the policy is defined | S | \<Organisation\>'s corporate parameter values |
| SR-01\_ODP\[02\] | Who receives the procedures is defined | S | \<Organisation\>'s corporate parameter values |
| SR-01\_ODP\[03\] | Policy level is selected | S | \<Organisation\>'s corporate parameter values |
| SR-01\_ODP\[04\] | Managing official is defined | S | System owner |
| SR-01\_ODP\[05\] | Policy review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SR-01\_ODP\[06\] | Policy review events are defined | S | \<Organisation\>'s corporate parameter values |
| SR-01\_ODP\[07\] | Procedures review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SR-01\_ODP\[08\] | Procedures review events are defined | S | \<Organisation\>'s corporate parameter values |
| SR-01a.\[01\] | Policy is developed and documented | S | Version \<ver\> approved by the Head of Cyber, subject to legal review (D-SR-01); version \<ver\> awaits re-approval (D-SR-12) |
| SR-01a.\[02\] | Policy is disseminated | O-D | Not yet shared |
| SR-01a.\[03\] | Procedures are developed and documented | S | Version \<ver\> approved by the system owner (D-SR-13) |
| SR-01a.\[04\] | Procedures are disseminated | O-D | Not yet shared |
| SR-01a.01(a)\[01\] | Policy addresses purpose | S | \<Policy\> (SR) \<ver\>, section SR.1 |
| SR-01a.01(a)\[02\] | Policy addresses scope | S | \<Policy\> (SR) \<ver\>, section SR.1 |
| SR-01a.01(a)\[03\] | Policy addresses roles | S | \<Policy\> (SR) \<ver\>, section SR.5 |
| SR-01a.01(a)\[04\] | Policy addresses responsibilities | S | \<Policy\> (SR) \<ver\>, section SR.5 |
| SR-01a.01(a)\[05\] | Policy addresses management commitment | S | \<Policy\> (SR) \<ver\>, section SR.6 |
| SR-01a.01(a)\[06\] | Policy addresses coordination | S | \<Policy\> (SR) \<ver\>, section SR.6 |
| SR-01a.01(a)\[07\] | Policy addresses compliance | S | \<Policy\> (SR) \<ver\>, section SR.6 |
| SR-01a.01(b) | Policy is consistent with laws and standards | S | Legally reviewed on 12 November 2026, as confirmed by the system owner |
| SR-01b. | Official is designated | S | \[Name\] is the system owner |
| SR-01c.01\[01\] | Policy is reviewed at the set frequency | O-D | First review not yet due |
| SR-01c.01\[02\] | Policy is reviewed after set events | S | Reviewed on 12 November 2026 after the SR pack review (D-SR-11) |
| SR-01c.02\[01\] | Procedures are reviewed at the set frequency | O-D | First review not yet due |
| SR-01c.02\[02\] | Procedures are reviewed after set events | S | Reviewed and approved as version \<ver\> on 12 November 2026 (D-SR-13) |
| SR-02\_ODP\[01\] | What the plan covers is defined | S | \<Organisation\>'s corporate parameter values |
| SR-02\_ODP\[02\] | Review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SR-02a.\[01\] | Plan is developed | S | \<Supply Chain Risk Management\> \<ver\>, approved (D-SR-13) |
| SR-02a.\[02\] | Plan addresses research and development | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[03\] | Plan addresses design | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[04\] | Plan addresses manufacturing | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[05\] | Plan addresses acquisition | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[06\] | Plan addresses delivery | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[07\] | Plan addresses integration | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[08\] | Plan addresses operation and maintenance | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02a.\[09\] | Plan addresses disposal | S | \<Supply Chain Risk Management\>, section 3.4 |
| SR-02b. | Plan is reviewed and updated | O-D | First review not yet due |
| SR-02c.\[01\] | Plan is protected from disclosure | O-D | Restricted store not yet in use (PA-88) |
| SR-02c.\[02\] | Plan is protected from modification | O-D | Restricted store not yet in use (PA-88) |
| SR-02(01)\_ODP\[01\] | Team is defined | S | \<Organisation\>'s corporate parameter values |
| SR-02(01)\_ODP\[02\] | Team's activities are defined | S | \<Organisation\>'s corporate parameter values |
| SR-02(01) | Team is established | O-D | Named in \<Supply Chain Risk Management\> \<ver\>; \<Organisation\>'s part not confirmed; the team has not met |
| SR-03\_ODP\[01\] | What is covered is defined | S | \<Organisation\>'s corporate parameter values |
| SR-03\_ODP\[02\] | Who is coordinated with is defined | S | \<Organisation\>'s corporate parameter values |
| SR-03\_ODP\[03\] | Controls are defined | S | \<Organisation\>'s corporate parameter values |
| SR-03\_ODP\[04\] | Where controls are documented is selected | S | \<Organisation\>'s corporate parameter values |
| SR-03\_ODP\[05\] | Other document is defined | S | \<Organisation\>'s corporate parameter values |
| SR-03a.\[01\] | Process to address weaknesses is established | O-D | PRO-SR-1 and PRO-SR-2 \<ver\> approved; not yet in use |
| SR-03a.\[02\] | Process is coordinated | O-D | Not yet agreed with \<Organisation\> |
| SR-03b. | Controls are employed | O-G | Only OfflineModules packages use the offline feed; no lock files, trust policy or pinned images (U01 to U03, U06; PA-94, PA-77) |
| SR-03c. | Controls are documented | S | \<Supply Chain Risk Management\>, sections 3.5 to 3.7, approved (D-SR-13) |
| SR-05\_ODP | Strategies are defined | S | \<Organisation\>'s corporate parameter values |
| SR-05\[01\] | They protect against supply chain risks | O-G | Packages come straight from nuget.org, unchecked (U01; PA-94) |
| SR-05\[02\] | They identify supply chain risks | S | Test-SupplyChain.ps1 (U01 to U10) and Test-Vulnerability.ps1 (V01) identify supply chain risks, 12 November 2026 |
| SR-05\[03\] | They reduce supply chain risks | O-G | Not reduced until PA-94 and PA-92 are fixed |
| SR-06\_ODP | Review frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SR-06 | Suppliers are assessed and reviewed | O-D | No supplier review yet held on TPL-16 (PRO-SR-2) |
| SR-08\_ODP\[01\] | What is notified is selected | S | \<Organisation\>'s corporate parameter values |
| SR-08\_ODP\[02\] | Results shared are defined | S | \<Organisation\>'s corporate parameter values |
| SR-08 | Notification agreements are in place | O-E | \<Organisation\>'s terms not seen (EV-SR-01); open-source advisories watched (\<System and Information Integrity Management\>, section 3.3) |
| SR-10\_ODP\[01\] | What is inspected is defined | S | \<Organisation\>'s corporate parameter values |
| SR-10\_ODP\[02\] | When is selected | S | \<Organisation\>'s corporate parameter values |
| SR-10\_ODP\[03\] | Frequency is defined | S | \<Organisation\>'s corporate parameter values |
| SR-10\_ODP\[04\] | Signs of tampering are defined | S | \<Organisation\>'s corporate parameter values |
| SR-10 | Components are inspected for tampering | O-G | Images and assemblies match the baseline (U08); release checksums and bill of materials not built (PA-61, PA-78) |
| SR-11\_ODP\[01\] | Who is told is selected | S | \<Organisation\>'s corporate parameter values |
| SR-11\_ODP\[02\] | External bodies are defined | S | \<Organisation\>'s corporate parameter values |
| SR-11\_ODP\[03\] | Roles told are defined | S | \<Organisation\>'s corporate parameter values |
| SR-11a.\[01\] | Anti-counterfeit policy is in place | O-D | \<Policy\> (SR) \<ver\>, R11; awaits re-approval (D-SR-12) |
| SR-11a.\[02\] | Anti-counterfeit procedures are in place | O-D | PRO-SR-4 \<ver\> approved; not yet in use |
| SR-11a.\[03\] | Procedures detect counterfeits | O-D | PRO-SR-4 \<ver\> approved; not yet in use; no trust policy (U03) |
| SR-11a.\[04\] | Procedures prevent counterfeits | O-D | PRO-SR-4 \<ver\> approved; not yet in use |
| SR-11b. | Counterfeits are reported | O-D | PRO-SR-4 \<ver\> approved; not yet in use |
| SR-11(01)\_ODP | Who is trained is defined | S | \<Organisation\>'s corporate parameter values |
| SR-11(01) | They are trained to detect counterfeits | O-E | EV-SR-02 |
| SR-11(02)\_ODP | Components are defined | S | \<Organisation\>'s corporate parameter values |
| SR-11(02)\[01\] | Control is kept while awaiting repair | O-E | EV-SR-02 |
| SR-11(02)\[02\] | Control is kept while awaiting return | O-E | EV-SR-02 |
| SR-12\_ODP\[01\] | What is disposed of is defined | S | \<Organisation\>'s corporate parameter values |
| SR-12\_ODP\[02\] | How is defined | S | \<Organisation\>'s corporate parameter values |
| SR-12 | Components are disposed of that way | O-E | EV-SR-02 |

### SR.5 Assessment plan

**Table SR-4: Assessment plan**

| Item | Detail |
| --- | --- |
| Scope | The 12 SR entries in the Moderate baseline, with 81 determination statements |
| Procedures | CSS, using the CSS published statements and identifiers (catalog release 5.2.0) |
| Dates | 6 November 2026; updated on 12 November 2026 after the SR pack review |
| Examine | \<Policy\> (SR), \<Procedures\> (SR) and \<Supply Chain Risk Management\> \<ver\>; \<Risk Assessment Management\>, sections 3.9 and 3.4; the four package source settings files, the image build file, the compose file, each app's restored package list and the offline feed index at tag v1.0. Depth: focused. Coverage: focused |
| Test | Test-SupplyChain.ps1, checks U01 to U10, with no running stack (evidence in the SR evidence); Test-Vulnerability.ps1 (the RA evidence) |
| Interview | None held. The developers, security officer and \<Organisation\>'s IT service desk remain |
| Previous results reused | RA checks V01 and V03 (packages and image pinning); SI integrity baseline (the SI evidence); CM checks C04 and C05 (inventory and unused components) |
| Boundary | \<System Name\>'s code, build and release. \<Organisation\>'s suppliers, hardware, repair and disposal are provider evidence (EV-SR-01, EV-SR-02) |
| Order of assessment | A, sources and acquisition (SR-3, SR-5); B, inspection (SR-10); C, suppliers and notices (SR-6, SR-8); D, authenticity (SR-11); E, plan and team (SR-2); F, disposal (SR-12); G, policy (SR-1) |
| Needed from providers | EV-SR-01 and EV-SR-02 in \<Evidence Requests\> |
| Evidence retained | the SR evidence (results, README and MANIFEST); the RA evidence; completed TPL-6, TPL-7, TPL-10 and TPL-16 records |

For the Level 2 assessment, the assessor should run Test-SupplyChain.ps1 on the release to be deployed, check the bill of materials and release SHA-256 values once built, examine \<Organisation\>'s supplier, hardware and disposal evidence, hold the interviews, and re-determine every statement in section SR.4.
