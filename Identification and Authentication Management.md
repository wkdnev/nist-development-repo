# \<System Name\> Identification and Authentication Management

## 1 Purpose

This document sets out how \<System Name\> is designed and configured to meet the 24 Identification and Authentication (IA) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: who and what is identified, sign-in through PingFederate, the assurance levels, the authenticators, the authentication settings against CSS, sign-in lifetime and signing in again, identity proofing, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet.

Every user signs in through \<Organisation\>'s PingFederate, with multi-factor authentication, by OpenID Connect. PingFederate's signed response names the person and carries no groups: \<System Name\>'s API reads the person's groups from Active Directory over LDAPS (flow F7). \<System Name\> holds no accounts or passwords of its own, and has no session management.



## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.7 (Table 16). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (IA). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (IA), and the steps people follow are in \<Procedures\> (IA). Who may do what once signed in is in \<Access Control Management\>.

## 3 The design

### 3.1 Principles

Controls met here: IA-2, IA-2(1), IA-2(2), IA-4, IA-5, IA-5(6), IA-12.

1. **Unique.** Each person has one named identifier, which is never reused.
2. **Proven.** A person's identity is established before they have an account.
3. **Strong.** Every sign-in needs more than a password.
4. **Protected.** Authenticators are never stored or sent in the clear, and secrets are kept out of the source repositories.
5. **Current.** Authenticators change whenever they may be compromised.
6. **One place to sign in.** \<System Name\> holds no accounts and no passwords. \<Organisation\>'s PingFederate authenticates every user.

These carry out the principles and rules of \<Policy\>, sections IA.3 and IA.4.

### 3.2 Who and what is identified

Controls met here: IA-2, IA-2(12), IA-3, IA-4, IA-4(4), IA-8, IA-8(1), IA-8(2), IA-8(4).

**Table 1: Identifiers**

| Who or what | Identifier | Issued by | Authenticated by | Reused |
| --- | --- | --- | --- | --- |
| Every user, whatever their role | Their Active Directory account name. It shows whether they are staff or a contractor | \<Organisation\>, after HR's pre-employment checks | PingFederate: password and second factor | Never |
| The API, to the database | Its own managed service account, mapped to a SQL Server login that is not a sysadmin | \<Organisation\>, in Active Directory; the login is created by the database administrator | Windows authentication (Kerberos). No database password exists | Not applicable |
| The API, to Active Directory | The same managed service account, with read-only rights | \<Organisation\>, in Active Directory | A bind over LDAPS (flow F7), with the directory's certificate checked | Not applicable |
| The UI application and the Admin application, to the API | Each application's own Windows service account, to obtain a token; then a signed, short-lived token on every call | The API | Windows authentication (Kerberos) over the loopback HTTPS for the token request, accepted only from those two accounts; then the API checks the token's HMAC-SHA-256 signature on every call and refuses any other caller. Only the API can read the signing key | Not applicable |
| Each application, on the application server | Its own Windows service account | \<Organisation\>, in Active Directory | Windows: a managed service account, whose password no person knows | Not applicable |
| Windows server and database administrators, on the servers | Their own named administrator accounts | \<Organisation\> | \<Organisation\>'s directory, with multi-factor authentication, from their managed devices over \<Organisation\>'s managed administration route only (flow F11) | Never |
| The database server, to the API | Its TLS certificate | \<Organisation\>'s certificate authority | The API checks the certificate and the server's name in full before any data is sent (flow F5) | Not applicable |
| PingFederate, to the applications | Its signing certificate | \<Organisation\> | Each application checks every sign-in response against it. The UI application and the Admin application fetch the certificate in PingFederate's OpenID Connect metadata over HTTPS from the application server (flow F10) | Not applicable |
| Users' devices | The managed device, to the network | \<Organisation\> | Its network access control | Not applicable |

There are no shared, guest, anonymous or local accounts, and nobody outside \<Organisation\>'s staff and contractors may use \<System Name\> (\<Access Control Management\>, section 3.2).

**Issuing identifiers.** \<Organisation\> authorises each Active Directory account through its starters process, and assigns it to the person its HR has checked. \<System Name\>'s part is membership of its groups, which the group's owner authorises through the ServiceNow workflow (\<Access Control Management\>, section 3.13). Service accounts are named for the application they run. Active Directory accounts are never reused, under \<Organisation\>'s rule. \<System Name\> issues no identifiers, so it has none to reuse.

**User status.** Active Directory shows whether a person is staff or a contractor, and the group's owner sees it when authorising a request.

**Devices.** \<Organisation\>'s network access control identifies each managed device before it joins the network, and unmanaged devices are kept off it. \<System Name\> does not identify devices itself: it is reached only from that network or the VPN.

**Users from outside \<Organisation\>.** Only \<Organisation\>'s staff and contractors, with an Active Directory account, may use \<System Name\>, so the controls for non-organisational users do not apply (TR-IA-03 to TR-IA-06 in \<Tailoring Register\>). PIV is a United States federal credential, and no \<System Name\> user holds one, so PIV credentials are not accepted (TR-IA-01).

### 3.3 Sign-in through PingFederate

Controls met here: IA-2, IA-2(1), IA-2(2), IA-2(8), IA-6, IA-11.

![Figure 1: How a person signs in](figures/iam-figure-1.png)

**Figure 1: How a person signs in**

**Table 2: Steps of a sign-in**

| Step | What happens | Who does it |
| --- | --- | --- |
| 1 | The person opens \<System Name\>. Not being signed in, they are sent to PingFederate (flow F6) | \<System Name\> |
| 2 | The person gives their password and their second factor. \<System Name\> never sees either | PingFederate |
| 3 | PingFederate returns a signed OpenID Connect response that names the person. It carries no groups | PingFederate |
| 4 | \<System Name\> completes the sign-in with PingFederate over HTTPS from the application server (flow F10), and checks the response: that PingFederate signed it, that it was issued for \<System Name\>, that it is within its short life, and that it has not been used before | \<System Name\> |
| 5 | The API reads the person's groups from Active Directory over LDAPS (flow F7), which give their roles and schema access. \<System Name\> holds the sign-in only in its authentication cookie, and records the sign-in | \<System Name\> |
| 6 | The application's sign-in lasts 8 hours at most, never longer than PingFederate's sign-in (\<System Description\>, P-02). It ends sooner at Sign out (FR-084), or within 5 minutes of the account being disabled or the membership removed. The person then signs in again | \<System Name\>, PingFederate and \<Organisation\> |

**Table 3: The trust between PingFederate and \<System Name\>**

| Setting | Design |
| --- | --- |
| Protocol | OpenID Connect |
| Who \<System Name\> trusts | \<Organisation\>'s PingFederate only, by its signing certificate, through \<System Name\>'s OpenID Connect client |
| What a sign-in response must show | Signed by PingFederate; issued for \<System Name\>; within its life; not used before |
| Sign-in response life | Short: \[minutes to be agreed with \<Organisation\>\] |
| What the response carries | The person's account name, and nothing more than \<System Name\> needs. It carries no groups: the API reads them from Active Directory over LDAPS (flow F7) |
| Certificate renewal | \<System Name\> picks up PingFederate's new certificate from its OpenID Connect metadata (flow F10) when \<Organisation\> renews it |
| Federation assurance level | Level 2 of CSS: a signed response that only \<System Name\> can use. It is to be set with \<Organisation\> |
| If PingFederate is unavailable | Nobody can sign in. There is no local sign-in to fall back on |

**Second factor.** PingFederate requires a second factor from every user, privileged or not, under the same authentication policy for \<System Name\>. The application roles are AD groups, and nobody reaches an administration page without signing in through PingFederate. The named Windows server and database administrators reach the servers only from their managed devices through \<Organisation\>'s managed administration route, with named accounts, which also requires a second factor (flow F11; \<Maintenance Management\>, section 3.4).

**Replay resistance.** For privileged and non-privileged accounts alike, sign-in responses from PingFederate are signed, short-lived, issued for \<System Name\> only and used once. Everything travels over TLS. \<System Name\> holds the sign-in only in its authentication cookie, marked Secure, HttpOnly and SameSite, whose lifetime is no longer than PingFederate's sign-in lifetime (P-02).

**What the person sees.** Passwords and second factors are entered on PingFederate's page, which masks them and does not say whether an account exists. \<System Name\> shows no sign-in form.

The steps and the trust are the design. The settings shown as placeholders are asked of \<Organisation\> with EV-IA-04, and are filled in when it answers.

### 3.4 Assurance levels

Controls met here: IA-2, IA-2(1), IA-2(2), IA-5, IA-12.

This follows CSS, section 3, and the federal acceptance statement template, applied to sign-in through PingFederate.

Identity assurance is how sure we are that a person is who they claim. Authenticator assurance is how sure we are that the person signing in holds the account. Federation assurance applies when another system, here PingFederate, vouches for the person.

**Table 4: Assurance levels by user group**

| User group | Harm if impersonated | Identity assurance | Authenticator assurance: target | Federation |
| --- | --- | --- | --- | --- |
| Administrators | High: which groups open each schema, and every setting; no item content | \<Organisation\>'s pre-employment checks, with the request authorised by the system owner (PRO-IA-1) | AAL2: multi-factor sign-in through PingFederate | PingFederate, at federation assurance level 2, to be set with \<Organisation\> |
| Editors | Moderate: one schema's items | As above, with the request authorised by the schema's Data Owner | AAL2: multi-factor sign-in through PingFederate | PingFederate, at federation assurance level 2, to be set with \<Organisation\> |
| Readers, auditors and security officers | Moderate: reading one schema's items, the audit log or security information | As above | AAL2: multi-factor sign-in through PingFederate | PingFederate, at federation assurance level 2, to be set with \<Organisation\> |
| Legal adviser's delegate | High: searching every schema for one person's items (\<System Description\>, FR-073) | \<Organisation\>'s pre-employment checks, named by the legal adviser, with the request authorised by the system owner (PRO-IA-1) | AAL2: multi-factor sign-in through PingFederate | PingFederate, at federation assurance level 2, to be set with \<Organisation\> |
| Business owners | Moderate: approving the disposal of items due under the retention schedule (\<System Description\>, FR-074) | \<Organisation\>'s pre-employment checks, with the request authorised by the system owner (PRO-IA-1) | AAL2: multi-factor sign-in through PingFederate | PingFederate, at federation assurance level 2, to be set with \<Organisation\> |
| Services (API to SQL Server) | High: the whole database | Not applicable | Windows authentication with the API's managed service account, whose password Windows sets and no person knows. No database password exists (section 3.5) | Not applicable |

**Reasoning:** \<System Name\> holds information rated Moderate, including personal data, so a failed sign-in check could expose personal data. CSS points to authenticator assurance level 2 for that harm, which needs two factors and replay resistance. Identity proofing is done once, by \<Organisation\>'s HR, and is not repeated by \<System Name\>. Federation is used: PingFederate proves who the person is and vouches for them to \<System Name\>.

### 3.5 Authenticators

Controls met here: IA-5, IA-5(1), IA-5(2), IA-5(6), IA-7.

**Table 5: Authenticator inventory**

| Authenticator | Used by | Held or stored | Changed | If lost or exposed |
| --- | --- | --- | --- | --- |
| Active Directory password | Every user | Active Directory; the person. \<System Name\> never sees it | Under \<Organisation\>'s corporate standard, and on suspected compromise (PRO-IA-3) | \<Organisation\>'s service desk resets it; \<Organisation\> ends the person's PingFederate sign-in |
| Temporary password | Not used by \<System Name\> | Not applicable | Not applicable | Not applicable |
| Second factor | Every user | Held by the person; registered with \<Organisation\> for PingFederate | On loss or replacement (PRO-IA-6) | \<Organisation\>'s service desk resets it after checking who the person is |
| Authentication cookie | UI application, Admin application and API callers | Issued by \<System Name\> after PingFederate has signed the user in, held in the person's browser and protected by the application's key ring. \<System Name\> keeps no record of it | A fixed 8 hours from sign-in (P-02), within PingFederate's sign-in, which is set to at least 8 hours (EV-IA-04) | Change the key ring, so that every cookie stops working and users sign in again through PingFederate |
| Token signing key, for the tokens the UI application and the Admin application send to the API | API, which issues and checks the tokens | The key store, outside the source code and settings files, readable only by the API's service account; protected copy at the second site (\<Contingency Planning Management\>, section 3.8) | As P-10 sets, at once if exposed, and when an administrator who knew it leaves (PRO-IA-4) | Change it; the two applications obtain new tokens. Users are not affected |
| Windows service accounts | UI application, Admin application and API, one each | Managed service accounts in Active Directory. Windows sets and changes the password, and no person knows it. The API's account also signs in to SQL Server by Windows authentication and binds to Active Directory over LDAPS, so no database password exists | By Windows, automatically | \<Organisation\> resets the account |
| First administrator account | Not used | Not applicable: \<System Name\> holds no accounts | Not applicable | Not applicable |
| OpenID Connect client credential | UI application and Admin application, to complete each sign-in with PingFederate (F10) | The key store, readable only by those two applications' service accounts; protected copy at the second site | 12 months (P-10), at once if exposed, and when a holder leaves | Change it in PingFederate and the key store together (PRO-AC-12, step 3) |
| PingFederate signing certificate | UI application, Admin application, API, to check each sign-in response | Published by \<Organisation\>'s PingFederate in its OpenID Connect metadata, fetched from the application server over flow F10; \<System Name\> holds only the public part | When \<Organisation\> renews it | \<Organisation\> replaces it, and \<System Name\> picks up the new one |
| Key rings (ASP.NET Core data protection keys) | UI application, Admin application, API | Each application's own folder on the application server, readable only by its service account and encrypted by the operating system | Every 90 days (P-10) | Users sign in again; no data is lost |
| Server and database administrator accounts | Windows server and database administrators | \<Organisation\>'s directory. SQL Server accepts them by Windows authentication and holds no passwords | \[\<Organisation\>'s rule\] | \<Organisation\>'s process |
| TLS certificates | UI application, Admin application, API, database server | Issued by \<Organisation\>'s certificate authority, held in each server's certificate store | Before expiry | Revoke and reissue |

Only the API connects to SQL Server, by Windows authentication with its managed service account, which is not a sysadmin. The system owner and security officer review the inventory every 12 months (PRO-IA-7).

1. **First issue.** For people, \<Organisation\>'s service desk issues authenticators after HR's pre-employment checks (PRO-IA-2), with first content under \<Organisation\>'s corporate standard. The token signing key and the audit chain key are generated randomly, at least 256 bits long, by the named administrators and placed in the key store. The audit chain key is generated by the Windows server administrator, never by anyone with rights in SQL Server. Service account passwords are set by Windows.
2. **Lost, compromised or revoked.** \<Organisation\>'s service desk issues, resets and revokes, and \<Organisation\> ends the person's PingFederate sign-in at once, or disables their AD account (PRO-IA-2, PRO-IA-3, PRO-IA-6). After account recovery, \<Organisation\>'s service desk process requires a new password at once.
3. **No defaults.** \<System Name\> ships with no default account or password. SQL Server accepts Windows authentication only, and its built-in sa login is disabled, so no database password exists. No vendor default is left on either server.
4. **Protection.** User passwords stay in Active Directory and never reach \<System Name\>: they are typed into PingFederate over TLS, and never into \<System Name\>. The API has no database password: it connects by Windows authentication. The information is rated Moderate, and the token signing key and the audit chain key protect the calls to the API and the audit log, so they are held in the key store, outside the source repositories and settings files, readable only by the service account that needs each, with a protected copy at the second site (\<System Description\>, section 7.7). Windows permissions protect each application's settings (\<Access Control Management\>, section 3.6.3). Everything travels over TLS.
5. **What people do.** The rules of behaviour require people never to share a password or second factor, and to report a loss at once (\<Security Operating Procedures\>, Part A). Managed devices encrypt their disks.
6. **Group accounts.** There are no shared, group or role accounts (TR-AC-02 in \<Tailoring Register\>). Service secrets are changed when an administrator who knew them leaves.
7. **Certificates.** No person or service signs in to \<System Name\> with a certificate, so public key authentication does not apply (TR-IA-02 in \<Tailoring Register\>). If \<Organisation\>'s PingFederate uses a public key second factor, such as a security key, it applies again, and falls to \<Organisation\>.
8. **Cryptographic modules.** \<System Name\> uses the cryptographic modules of Windows Server 2025 and .NET. No person signs in to a module directly: the applications reach them through their service accounts. \<Organisation\> is asked which modules and mode the servers use (EV-IA-03).

### 3.6 Settings against CSS

Controls met here: IA-2(1), IA-2(2), IA-2(8), IA-5, IA-5(1), IA-6, IA-11.

\<System Name\> sets no password rule of its own. \<Organisation\>'s corporate standard applies, and is to be compared with CSS and NCSC password guidance when \<Organisation\> supplies it (EV-IA-04).

**Table 6: Authentication settings at authenticator assurance level 2**

| Requirement | CSS | \<System Name\> |
| --- | --- | --- |
| Password length, password only | At least 15 characters | \<Organisation\>'s corporate standard, to be supplied |
| Password length, with multi-factor | At least 8 characters | \<Organisation\>'s corporate standard, to be supplied |
| Longest password allowed | At least 64 should be allowed | \<Organisation\>'s corporate standard |
| Spaces and all characters | Should be allowed | \<Organisation\>'s corporate standard |
| Composition rules | Must not be imposed | \<Organisation\>'s corporate standard |
| Scheduled changes | Must not be required | \<Organisation\>'s corporate standard |
| Blocklist | Must be checked | \<Organisation\>'s corporate standard |
| Storage | Salted, with a costly function | Active Directory. \<System Name\> stores no passwords |
| Rate limiting | At most 100 failures | Lockout by PingFederate and Active Directory, as P-42 sets: 10 failed attempts in 15 minutes lock the account for 15 minutes |
| Inactivity timeout | No more than 1 hour | None in \<System Name\>. Users must sign out with Sign out (FR-084) when they leave their device for longer than a short break (\<System Description\>, P-53), and the device screen lock hides an unattended screen (\<System Description\>, P-03) |
| Overall sign-in limit | No more than 24 hours | 8 hours from sign-in: the application's authentication cookie has a fixed lifetime with no sliding extension, never longer than PingFederate's sign-in (P-02) |
| Second factor | Required | Provided by PingFederate |
| Replay resistance | Required | Sign-in responses from PingFederate are signed, short-lived, issued for \<System Name\> only and used once, over TLS (section 3.3) |
| Sign-in ends on password change | Expected | \<System Name\> holds no passwords. Its session, the authentication cookie, is not ended by a password change on its own: \<Organisation\> ends the person's PingFederate sign-in on notice, and disables the account or removes the membership where the password may be compromised, which the API refuses within 5 minutes (PRO-IA-3) |
| Feedback | No hint whether the user exists | Given by PingFederate, not \<System Name\> |

### 3.7 Sign-in lifetime and signing in again

Controls met here: IA-2, IA-11.

\<System Name\>'s session is its authentication cookie (\<Access Control Management\>, section 3.15). It has no idle timeout, session limit or page lock.

1. A sign-in lasts 8 hours from sign-in, with no sliding extension, and never longer than PingFederate's sign-in (P-02). It ends sooner when the person uses Sign out (FR-084), or when their account is disabled or their membership removed, which the API refuses within 5 minutes. The person then signs in again through PingFederate.
2. An unattended screen is locked by \<Organisation\>'s managed devices and the servers after the inactivity period in P-03 (\<Access Control Management\>, section 3.15).
3. A change to a person's AD groups or account takes effect within 5 minutes, because the API reads them on every request and holds each answer for at most 5 minutes; an open page re-checks the person every 5 minutes (NFR-102).
4. Access is ended outside \<System Name\>: \<Organisation\> disables the AD account or the group's owner removes the membership, and \<Organisation\> ends the person's PingFederate sign-in. This is the first step when a password or second factor may be compromised, when someone leaves, and when a role is removed (PRO-IA-3).
5. Each sign-in is tied to the person PingFederate authenticated, and every audit record names them.

### 3.8 Identity proofing

Controls met here: IA-12, IA-12(2), IA-12(3), IA-12(5).

\<Organisation\>'s HR proves who each person is, once, in its pre-employment checks, before the person has an Active Directory account. That is photo identification and a right-to-work check for staff, and the same through the agency for contractors, with a notice of proofing sent to the person. HR sees the evidence, and validates and verifies it, in those checks, and each identity resolves to one person, with one Active Directory account. \<System Name\> does not repeat it. Before adding anyone to a group, the group's owner confirms the request came from that person and their line manager (PRO-IA-1).

### 3.9 What \<Organisation\> provides

Controls met here: IA-2, IA-2(1), IA-2(2), IA-2(8), IA-3, IA-4, IA-4(4), IA-5, IA-5(1), IA-6, IA-7, IA-12, IA-12(2), IA-12(3), IA-12(5).

**Table 7: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| PingFederate and its multi-factor authentication | IA-2, IA-2(1), IA-2(2), IA-2(8), IA-6 | Every user is authenticated with two factors; the sign-in response is signed and names the person, and carries no groups; the sign-in page hides what is typed | EV-IA-04 |
| Active Directory accounts and passwords | IA-4, IA-4(4), IA-5, IA-5(1) | One named account for each person, never reused, showing staff or contractor; passwords under the corporate standard | EV-IA-04, EV-AC-01 |
| Device identification | IA-3 | Only managed devices join the network | EV-IA-01 |
| Identity proofing | IA-12, IA-12(2), IA-12(3), IA-12(5) | Each person's identity is checked before they have an account | EV-IA-02 |
| Cryptographic modules on the servers | IA-7 | The modules meet the applicable standards | EV-IA-03 |

### 3.10 Policy and procedures

Controls met here: IA-1.

\<Policy\> (IA) and \<Procedures\> (IA) meet IA-1. Who they are shared with is in \<Policy\>, section IA.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
