# \<System Name\> Tailoring Register

## 1 Purpose

CSS (task S-2) allows a baseline to be tailored to the system, and expects each tailoring choice to have a rationale and an approval. This register holds the case for every control, part or parameter proposed as not applicable. Tailoring is not a way to avoid a control that is merely difficult. Every entry states the condition that makes it valid, and it ends if that condition stops being true. All entries are proposals.

Entries are numbered TR-XX-nn, where XX is the family code.

**Table 1: Family coverage**

| Family | Section |
| --- | --- |
| AC Access Control | 2 |
| AT Awareness and Training | None |
| AU Audit and Accountability | None |
| CA Assessment, Authorization, and Monitoring | None |
| CM Configuration Management | None |
| CP Contingency Planning | None |
| IA Identification and Authentication | 3 |
| IR Incident Response | None |
| MA Maintenance | None |
| MP Media Protection | None |
| PE Physical and Environmental Protection | None |
| PL Planning | None |
| PM Program Management | 4 |
| PS Personnel Security | None |
| PT Personally Identifiable Information Processing and Transparency | 5 |
| RA Risk Assessment | None |
| SA System and Services Acquisition | 5 |
| SC System and Communications Protection | 6 |
| SI System and Information Integrity | 7 |
| SR Supply Chain Risk Management | None |

## 2 Access Control (AC)

### 2.1 Tailoring proposals

**Table 2: AC tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-AC-01 | AC-2(2) | Not applicable | Temporary and emergency accounts are prohibited (P-39), and the system cannot expire accounts | Each access review confirms that no such account exists | The system must first be able to disable them automatically |
| TR-AC-02 | AC-2k | Not applicable | Shared and group accounts are prohibited (P-36) | \<System Name\> holds no accounts of its own: every account is a person's own Active Directory account, and there is no built-in or default account | A process for changing shared authenticators is needed |
| TR-AC-03 | AC-8a.01 | Replace the statement with one naming \<Organisation\> | \<System Name\> is not a U.S. Government system, so the statement would be untrue | The notice names \<Organisation\>, and a legal adviser agrees the wording | Applies again if \<System Name\> serves a U.S. Government customer |
| TR-AC-04 | AC-8c | Not applicable | \<System Name\> is not publicly accessible | Items and functions need sign-in, except the list in P-51 | AC-8c applies in full |
| TR-AC-05 | AC-17(4) | Not applicable | CSS defines remote access as access through external networks. Administration is to take place only from inside \<Organisation\>'s network | Administration uses only \<Organisation\>'s managed administration route, for the Admin application (F2) and for server and database administration (F11), and external routes to the VMs' administration ports are blocked (EV-AC-12) | AC-17(4) applies, with defined needs and logging |
| TR-AC-06 | AC-19, AC-19(5) | Not applicable | Phones and tablets are not to be used with \<System Name\> in the first release | \<Organisation\>'s device controls prevent or govern this. \<System Name\> cannot identify a device, so a rule alone is weak evidence (EV-AC-15) | Both apply, with \<Organisation\>'s mobile controls as evidence |
| TR-AC-07 | AC-20(1) | Not applicable | P-48 does not allow external systems to reach or hold \<System Name\> data without the system owner's approval, and none is proposed | No such approval is given | Verification of controls and retained agreements are needed for each approval |
| TR-AC-08 | AC-22 | Not applicable | \<System Name\> holds no public content (P-50) | Items and functions need sign-in, except the list in P-51 | AC-22 applies in full |
| TR-AC-09 | AC-07\_ODP\[05\], \[06\] | Not selected | The account lock is the chosen action, so no delay algorithm or other action is needed | The lock remains in place | Define the value that is then selected |
| TR-AC-10 | AC-20\_ODP\[03\] | Not selected | Terms and conditions are used, not asserted controls | P-48 remains the rule | Define the asserted controls |

### 2.2 Considered and not proposed

These controls may look unnecessary but are not proposed for tailoring, so that their risk stays visible.

**Table 3: AC controls considered and kept**

| Control | Reason it stays |
| --- | --- |
| AC-18, AC-18(1) | \<System Name\> provides no wireless access, but users may reach it over \<Organisation\>'s wireless network, so the control is inherited and needs evidence |
| AC-18(3) | It needs confirming on the built VMs and workstation builds |
| AC-17, AC-17(1) to (3) | Approved users may work remotely through \<Organisation\>'s service |
| AC-20, AC-20(2) | Downloads can reach any device the user has, so the rule and its enforcement remain relevant |
| AC-2(5), AC-11, AC-11(1), AC-12 | \<System Name\> has no session management of its own: no idle lock, idle timeout, session limit or sign-out. The controls are not tailored out but are provided by \<Organisation\> and inherited (\<System Description\>, section 7.3). AC-11 and AC-11(1) come from the screen lock on \<Organisation\>'s managed devices (\<System Description\>, P-03); AC-12 and AC-2(5) come from the sign-in lifetime set in PingFederate (P-02), which the application's authentication cookie never outlasts |

## 3 Identification and Authentication (IA)

IA-5i is covered by TR-AC-02.

**Table 4: IA tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-IA-01 | IA-2(12) | Not applicable | PIV credentials are a US federal scheme, and \<Organisation\> is a UK company | \<Organisation\> does not serve a US federal customer through \<System Name\> | IA-2(12) applies |
| TR-IA-02 | IA-5(2) | Not applicable | \<System Name\> does not use public key sign-in | Users do not sign in to \<System Name\> with a public key: PingFederate decides the factors | IA-5(2) applies. A public key second factor would bring it back |
| TR-IA-03 | IA-8 | Not applicable | Only \<Organisation\>'s staff and contractors hold accounts | Each access review confirms no outside user holds an account | IA-8 applies |
| TR-IA-04 | IA-8(1) | Not applicable | As TR-IA-01 and TR-IA-03 | As TR-IA-03 | IA-8(1) applies |
| TR-IA-05 | IA-8(2) | Not applicable | No external authenticators are accepted | As TR-IA-03 | IA-8(2) applies |
| TR-IA-06 | IA-8(4) | Not applicable | No external identity profiles are used | As TR-IA-03 | IA-8(4) applies |

## 4 Program Management (PM)

TR-PM-01 isn't tailoring in the strict sense, as PM has no controls in the Moderate baseline. It is recorded here so that all 20 families are accounted for. PT also has no controls in that baseline, and is assessed against the privacy baseline instead.

**Table 5: PM proposal**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-PM-01 | The whole PM family | Outside the baseline; not assessed for \<System Name\> | PM controls cover an organisation's whole security programme, not one system, and CSS does not allocate them to a baseline. \<System Name\> still inherits them as common controls (CSS, task P-5), as listed in \<Program Management\>, section 3.3 | The organisation's programme stays with \<Organisation\> and the Head of Cyber, and \<System Name\>'s owner or authorising official doesn't ask for it to be assessed | Assess the PM controls |

### 4.1 PM controls \<System Name\> inherits

The list of PM controls that \<System Name\> inherits, with the provider and the evidence for each, is held in \<Program Management\>, section 3.3. It is not repeated here.

## 5 PT and SA

The PT controls are in the CSS privacy baseline, not Moderate, and are assessed against it.

**Table 6: PT and SA proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-PT-01 | PT-5(2), PT-6, PT-6(1), PT-6(2), PT-7(1), PT-7(2), PT-8 | Not applicable | These rest on US law and federal bodies: the Privacy Act, Federal Register notices, Social Security numbers, the First Amendment and computer matching. \<Organisation\> operates in the UK | \<System Name\> processes no data under those US laws. The legal adviser checks this | Assess those controls |
| TR-SA-01 | SA-4(10) | Not applicable | It requires US government PIV identity products, which \<System Name\> doesn't use | \<System Name\> doesn't use PIV cards | Assess SA-4(10) |

## 6 System and Communications Protection (SC)

No CM control is tailored, and CM-2(7) stays in scope.

**Table 7: SC tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-SC-01 | SC-15 | Not applicable | \<System Name\> has no collaborative computing devices or applications | None is added to the system | SC-15 applies |

## 7 System and Information Integrity (SI)

No RA or CA control is tailored.

**Table 8: SI tailoring proposals**

| ID | Control or part | Tailoring | Rationale | Condition that must hold | If the condition changes |
| --- | --- | --- | --- | --- | --- |
| TR-SI-01 | SI-8, SI-8(2) | Not applicable | \<System Name\> sends and receives no email, so it has no entry or exit point for spam | \<System Name\> does not add email | SI-8 and SI-8(2) apply |
