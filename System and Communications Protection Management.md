# \<System Name\> System and Communications Protection Management

## 1 Purpose

This document sets out how \<System Name\> is designed and configured to meet the 25 System and Communications Protection (SC) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the principles, the boundary and the allowed flows, with each server's host firewall; transport encryption and sign-in; the cryptographic and key register and certificates; the page policy for mobile code; information at rest; denial of service, shared resources and process isolation; name resolution; what \<Organisation\> provides; and the policy and procedures. Each subsection names the controls it helps to meet.

Other documents hold the rest. Who provides and is responsible for each control, its status and its assessment result are in \<System Security Plan\>, section 7.17 (Table 26). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (SC). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (SC), and the steps people follow are in \<Procedures\> (SC). The flows themselves are in \<System Security Plan\>, section 3.7, and the trust zones and layers of defence in \<Security Architecture\>.

Much of this family is \<Organisation\>'s network: firewalls, the VPN, the proxy, DNS and the certificate authority. \<System Name\>'s own part is its listening addresses, host firewalls, TLS, keys, pages and the protection of what it stores.

Values that CSS asks the organisation to define are set at corporate level by \<Organisation\>. Any settings in section 3 should match those corporate values. Where one does not, it is changed in this document.

## 2 Summary

The implementation status of each control, how it is met, who is responsible, its assessment result and the risk and plan entries for its gaps are recorded in \<System Security Plan\>, section 7.17 (Table 26).

## 3 The design

### 3.1 Principles

Controls met here: SC-2, SC-7, SC-7(5), SC-8, SC-12.

1. **Deny by default.** Only the agreed flows are allowed, at \<Organisation\>'s firewalls and on each server.
2. **Encrypt everything that moves.** Every flow uses TLS, including those that stay inside a server.
3. **Know every key.** Every key and cryptographic use is recorded, owned, protected and changed on time.
4. **Separate.** Administration and the API are kept apart from everyday use.

These carry out the principles and rules of \<Policy\>, sections SC.3 and SC.4.

![Figure 1: The boundary, the flows and their protection](figures/scm-figure-1.png)

**Figure 1: The boundary, the flows and their protection**

### 3.2 Boundary and allowed flows

Controls met here: SC-2, SC-7, SC-7(3), SC-7(4), SC-7(5), SC-7(7), SC-7(8), SC-15.

\<System Name\> has no publicly accessible component and no connection of its own to an outside network. Users reach it from \<Organisation\>'s network, administrators over \<Organisation\>'s managed administration route, and everything outside is reached through \<Organisation\>'s managed interfaces and authenticated proxy (SC-7, SC-7(3), SC-7(8)), as \<Security Architecture\> sets out. Its only external connections are \<Organisation\>'s managed gateways, and all outbound traffic from the servers goes through the proxy or is blocked. \<System Name\> has no collaborative computing devices or applications, so SC-15 is tailored out (\<Tailoring Register\>, TR-SC-01). The flows are in \<System Security Plan\>, section 3.7, Table 7, and \<Security Architecture\>, Table 2.

\<System Name\>'s own part is how each application listens and each server's host firewall:

1. UI application listens on TCP 443 only.
2. The admin portal is reachable only over \<Organisation\>'s managed administration route.
3. API listens only on the application server's loopback address.
4. The database accepts connections only from the application server.

Each server's host firewall denies everything not listed below (SC-7(5)). \<Organisation\>'s firewalls apply the same flows at the network edge (EV-SC-02). A new flow, port or listening address goes through change control and updates these lists first (PRO-SC-4); a temporary exception is recorded on TPL-17 with an end date, and exceptions are reviewed every 12 months (PRO-SC-8). Split tunnelling is not allowed: \<Organisation\>'s VPN prevents it on every remote device (SC-7(7)).

**Table 1: Application server, inbound**

| Rule | Port | From | Flow |
| --- | --- | --- | --- |
| A1 | TCP 443 (UI application) | Users' networks, Z1 \[address ranges from \<Organisation\>\] | F1 |
| A2 | Admin portal port \[to be set\] | \<Organisation\>'s administration route only, Z2 \[address range\] | F2 |
| A3 | Windows administration \[tool and port, EV-MA-02\] | Z2 only | Not numbered |
| None | API | Not reachable from the network: loopback only | F3, F4 |

**Table 2: Database server, inbound**

| Rule | Port | From | Flow |
| --- | --- | --- | --- |
| D1 | TCP 5432 | Application VM address only | F5 to F7 |
| D2 | Windows administration \[tool and port, EV-MA-02\] | Z2 only | Not numbered |

**Table 3: Both servers, outbound**

| Rule | Port | To | Purpose |
| --- | --- | --- | --- |
| O1 | UDP 123 | \<Organisation\>'s time service | Time |
| O2 | \[To be confirmed\] | \<Organisation\>'s central logging | Logs |
| O3 | \[Proxy port\] | \<Organisation\>'s authenticated proxy | Updates and anything else outbound (SC-7(8)) |
| O4 | TCP 5432 (application VM only) | Database VM | F5 to F7 |
| O5 | Backup \[method to be chosen\] (database VM only) | \<Organisation\>'s backup site | Backups |

### 3.3 Transport encryption and sign-in

Controls met here: SC-7(4), SC-8, SC-8(1), SC-10, SC-13, SC-23.

Every flow uses this profile, from NCSC's guidance. It covers F1 to F7, including the API calls that stay on the application server, and F11, sign-in through PingFederate, which \<Organisation\> protects.

**Table 4: TLS profile**

| Setting | Required value |
| --- | --- |
| Versions | TLS 1.3 preferred; TLS 1.2 allowed; SSL, TLS 1.0 and TLS 1.1 off |
| TLS 1.3 key exchange | Hybrid X25519MLKEM768 or SecP256r1MLKEM768 where Windows supports it; otherwise secp256r1 |
| TLS 1.3 cipher suite | TLS\_AES\_128\_GCM\_SHA256 (TLS\_AES\_256\_GCM\_SHA384 also allowed) |
| TLS 1.2 cipher suites | TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 or TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 only |
| Also off | Compression, insecure renegotiation, export ciphers, 0-RTT |
| Certificates | ECDSA P-256 or RSA 2048-bit, SHA-256, from \<Organisation\>'s certificate authority |
| Web | HTTPS only, HTTP redirected, HSTS with a maximum age of one year, cookies always Secure, and a page policy that upgrades insecure requests |
| Database | TLS on in PostgreSQL, every client rule requiring TLS, a minimum of TLS 1.2, and API checking the server's certificate and host name in full |
| API (F3, F4) | API on the loopback address only, over HTTPS with K2 |

\<System Name\> has no sessions, session identifiers or sign-out of its own (\<Access Control Management\>, section 3.1). The authenticity of each sign-in is protected in two ways instead (SC-23). First, the application accepts only PingFederate's signed OpenID Connect response, and checks that PingFederate signed it (K12), that it was issued for \<System Name\> and that it is still valid. Second, the sign-in is then held only in the application's authentication cookie, which is protected by the application's data protection key ring (K5 to K7) so that it cannot be forged or changed, is marked Secure, HttpOnly and SameSite, is sent only over TLS, and lasts no longer than PingFederate's sign-in lifetime (P-AC-10). The UI application and the Admin application call the API with a signed, short-lived token (K4).

Network connections end when they are no longer needed (SC-10). Each TLS connection on F1 to F7 is closed when the exchange ends or when it has been idle for the web server's or database's connection time-out, and \<Organisation\> ends network and remote access (VPN) sessions after 30 minutes idle. There is no application session to end: a sign-in ends when PingFederate's sign-in lifetime does (P-AC-10).

### 3.4 Cryptographic and key register

Controls met here: SC-12, SC-13, SC-17.

Every key and cryptographic use in \<System Name\> is listed here (SC-12, SC-13). Each key is generated randomly, held in a protected store outside the source code, and owned. It is changed at its cryptoperiod, when a holder leaves, and at once if compromise is suspected. Cryptoperiods follow CSS. Values are never recorded, only where they are kept. United States CSS validation is not required: NCSC's profiles and these algorithms are used instead.

**Table 5: Cryptographic and key register**

| Item | Purpose | Algorithm and size | Stored in | Owner | Cryptoperiod |
| --- | --- | --- | --- | --- | --- |
| K1 Web and admin TLS certificate | HTTPS for F1 and F2 | ECDSA P-256 or RSA 2048, SHA-256; NCSC profiles (section 3.3) | Application VM certificate store, private key not exportable | Windows server administrator | 1 year, or \<Organisation\>'s maximum if shorter |
| K2 API loopback certificate | HTTPS for F3 and F4 | As K1 | Application VM certificate store | Windows server administrator | 1 year |
| K3 Database server certificate | TLS for F5 to F7 | As K1 | Database VM, key file readable only by the PostgreSQL service | Database administrator | 1 year |
| K4 Token signing key | Signs the short-lived tokens that the UI application and the Admin application send to API | HMAC-SHA256, at least 256 random bits | Protected store \[\<Organisation\>'s store, to be named\] | Developers | 1 year, and when a holder leaves |
| K5 to K7 Data protection key rings (API, UI application, Admin application) | Protect the authentication cookie and antiforgery tokens | AES-256-CBC with HMAC-SHA256 (ASP.NET Core default) | Each app's own folder, protected with Windows DPAPI at machine level, backed up | Developers, Windows server administrator | 90 days (the default automatic change) |
| K8 Database service account password | API's connection to PostgreSQL, the only one | SCRAM-SHA-256 | Protected store | Database administrator | 1 year, and when a holder leaves |
| K9 BitLocker keys (both VMs) | Encryption of the VMs' disks | XTS-AES 256 with the TPM | TPM; recovery keys in \<Organisation\>'s protected store | Windows server administrator | Life of the disk; recovery key tested every 12 months |
| K11 Audit chain key | Keys the hash that chains the audit records (\<Audit and Accountability Management\>, section 3.5) | HMAC-SHA-256, at least 256 random bits | Outside the database, where the applications' accounts cannot read it | Database administrator | 1 year, and when a holder leaves |
| K12 PingFederate signing certificate | Signs the OpenID Connect sign-in responses \<System Name\> accepts. \<System Name\> holds only the public part, and trusts nothing else | As \<Organisation\> sets it \[algorithm and size, EV-IA-04\] | \<Organisation\>'s PingFederate; the public part in \<System Name\>'s sign-in settings | \<Organisation\>; Windows server administrator for \<System Name\>'s PingFederate connection | As \<Organisation\> sets it. \<System Name\> follows each change of certificate without a gap |
| K10 Backup encryption key | Encrypted database backups | AES-256 \[method to be chosen\] | Protected store, apart from the backups | Database administrator | 1 year |
| A1 Password hashing | Not used: \<System Name\> stores no passwords | PBKDF2-SHA512, 600,000 iterations, 128-bit salt | Database | Developers | Not applicable; iterations reviewed every 12 months |
| A2 Audit chain | Shows audit records weren't changed | HMAC-SHA-256 with K11, as the audit design requires | Database | Developers | Not applicable |
| A3 Document checksums | Shows documents weren't changed | SHA-256 | Database | Developers | Not applicable |

Certificates come from \<Organisation\>'s certificate authority, under its certificate policy, using ECDSA P-256 or RSA 2048-bit with SHA-256. They are renewed at least 30 days before they expire, and only \<Organisation\>'s approved trust anchors are trusted (SC-17; PRO-SC-2).

### 3.5 Mobile code and the page policy

Controls met here: SC-18.

Acceptable mobile code is JavaScript and WebAssembly served by \<System Name\> itself. Anything else is unacceptable, including scripts from outside services, unless the system owner approves it (SC-18). Each application sends this page policy, and developers check page code at each release (PRO-SC-5).

**Table 6: Page policy**

| Directive | Required |
| --- | --- |
| default-src | 'self' |
| script-src | 'self' |
| style-src | 'self' |
| font-src | 'self' |
| img-src | 'self' data: |
| connect-src | 'self' wss: (same host) |
| frame-ancestors, base-uri | 'none', 'self' |
| form-action | 'self' |
| upgrade-insecure-requests | Present |

### 3.6 Information at rest

Controls met here: SC-4, SC-28, SC-28(1).

The information protected at rest is the documents and pages in PostgreSQL, the database files, the backups, the bulk export copies and the data protection key rings (SC-28).

1. **The servers' disks.** BitLocker with XTS-AES 256 and the TPM on both servers. Recovery keys are held in \<Organisation\>'s protected store, and one is tested every 12 months (PRO-SC-7).
2. **Backups.** Encrypted, with the key held apart from the backups (K10).
3. **Key rings.** Each application keeps its key ring in its own folder, readable only by its service account and protected with Windows DPAPI at machine level, and backed up with the server.
4. **Export copies.** Deleted once downloaded, and swept at start-up.
5. **Integrity.** Document checksums use SHA-256, and the audit records are chained (\<Audit and Accountability Management\>).

### 3.7 Denial of service, shared resources and process isolation

Controls met here: SC-2, SC-4, SC-5, SC-39.

1. **Denial of service** (SC-5). \<System Name\> limits the effects of network flooding, request flooding and resource exhaustion. \<Organisation\>'s network protections come first; each application limits its request rates; and PingFederate and Active Directory lock an account after repeated failed sign-ins. When the service slows or fails under traffic, the security officer and \<Organisation\>'s service desk respond (PRO-SC-6).
2. **Shared resources** (SC-4). Windows Server clears memory and storage between processes and users. Each application runs as its own Windows service under its own account. Export copies are removed, as above.
3. **Process isolation** (SC-39). Windows Server gives each process its own address space.
4. **Separation of functions** (SC-2). The admin portal, Admin application, is a separate application and process from the user application, UI application, and is reached only over \<Organisation\>'s managed administration route (section 3.2).

### 3.8 Name resolution

Controls met here: SC-20, SC-21, SC-22.

\<System Name\> uses \<Organisation\>'s DNS, which provides signed authoritative answers, validating resolvers, and fault-tolerant servers with internal and external roles kept apart (SC-20, SC-21, SC-22). \<System Name\> runs no DNS service of its own. \<Organisation\>'s evidence is asked for in EV-SC-05.

### 3.9 What \<Organisation\> provides

Controls met here: SC-5, SC-7, SC-7(3), SC-7(4), SC-7(5), SC-7(7), SC-7(8), SC-10, SC-17, SC-20, SC-21, SC-22.

**Table 7: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Denial-of-service protection and network disconnect | SC-5, SC-10 | Network flooding is limited, and network and remote access (VPN) sessions end after 30 minutes idle | EV-SC-01 |
| Managed interfaces, flow policy and exceptions | SC-7, SC-7(3), SC-7(4) | Only \<System Name\>'s flows are allowed at the network edge, and the address ranges and ports for the allow-lists. Each interface protects what crosses it, and prevents, filters and publishes information about unauthorised control plane traffic from outside networks | EV-SC-02 |
| The firewall rules | SC-7(5) | They deny by default and allow \<System Name\>'s flows only | EV-AC-03 |
| The VPN and the authenticated proxy | SC-7(7), SC-7(8) | No split tunnelling, and outbound traffic from the servers goes through the proxy | EV-SC-03 |
| The certificate authority and trust anchors | SC-17 | Certificates with the required keys and lifetimes, and a list of approved trust anchors | EV-SC-04 |
| DNS | SC-20, SC-21, SC-22 | Signed, validated and fault-tolerant name resolution | EV-SC-05 |

### 3.10 Policy and procedures

Controls met here: SC-1.

1. **Policy.** \<Policy\> (SC) is a system-level policy, shared with everyone who administers or develops \<System Name\>. The legal adviser reviews it.
2. **Procedures.** \<Procedures\> (SC) holds eight procedures, PRO-SC-1 to PRO-SC-8. They are shared with the same people.
3. **Owner.** The system owner manages the policy and procedures.
4. **Review.** The policy is reviewed every 12 months, and after a significant incident, audit finding or system change. The procedures are reviewed every 12 months, and after a change to the steps.
5. **Records.** The documents are under version control.

## Appendix A Communications protection controls outside the Moderate baseline

CSS does not select these at Moderate, so they are not assessed. SC-15 is tailored out (TR-SC-01), and SC-7(24) is a privacy baseline control set out in \<PII Processing Management\>. Table 8 says where the design goes some way towards them.

**Table 8: Related controls and enhancements not selected**

| Control | What it adds | \<System Name\>'s position |
| --- | --- | --- |
| SC-7(10) Prevent Exfiltration | Stops data leaving by unauthorised routes | Not required. Done in part: outbound traffic only through \<Organisation\>'s proxy (section 3.2) |
| SC-7(12) Host-based Protection | A firewall on each host | Not required. Done in design: each server's host firewall (section 3.2) |
| SC-7(18) Fail Secure | The boundary fails closed | Not required. Done in design: deny by default |
| SC-7(21) Isolation of System Components | Separates components by boundary | Not required. Done in design: separate application and database servers |
| SC-8(2) Pre- and Post-transmission Handling | Protects information while it is prepared for or received from transmission | Not required |
| SC-12(1) to SC-12(3) | Key availability and symmetric and asymmetric key production | Not required. Keys are recorded with their store and owner (section 3.4) |
| SC-23(1), SC-23(3), SC-23(5) | Invalidate session identifiers at sign-out, unique identifiers, allowed certificate authorities | Not required. \<System Name\> has no session identifiers of its own. Done in design: only PingFederate's signed response is accepted, and the sign-in is held only in the protected authentication cookie, whose lifetime is no longer than PingFederate's (section 3.3) |
| SC-28(2), SC-28(3) | Offline storage of information at rest; protected key storage | Not required. Done in part: encrypted backups with the key held apart (K10) |
| SC-39(1), SC-39(2) | Hardware separation and separate execution threads | Not required |
| SC-45 System Time Synchronization | Synchronises clocks with an authoritative source | Not selected at Moderate in the SC family. Done in design: \<Organisation\>'s time service (rule O1; \<Audit and Accountability Management\>) |
