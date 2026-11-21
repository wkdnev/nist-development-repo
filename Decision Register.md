## 1 Purpose

This register records the approvals and decisions for the set. Each row states what needs deciding, the recommendation and who decides, with space for the decision, name and date. Nothing is decided until a named person completes a row. The recommendations are proposals.

After a decision, the document it affects is updated to match: \<System Description\>, section 4, and the family design document for values, \<Risk List\> for risk treatments and \<Tailoring Register\> for tailoring.

A departure from the reference design (\<System Description\>, section 3.6) is decided by the system owner and recorded here as a D-GEN entry; a departure from a Secure by Design principle (\<System Description\>, section 8) is decided by the authorising official.

Decisions are numbered D-XX-nn, parameter approvals D-XX-Pnn and non-compliance entries NC-XX-nn, where XX is the family code. Cross-family decisions use GEN as the code. Each table has one row for each entry, with a Family column, so that adding an entry never renumbers another.

## 2 Decisions

Documents, policy decisions and cross-family decisions (GEN). The legal adviser confirms the legal positions in PT decisions.

**Table 1: Decisions**

| ID | Family | Decision needed | Recommendation | Who decides | Decision | Name | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D-AC-01 | AC | Approve TR-AC-01: AC-2(2) not applicable | Approve: temporary and emergency accounts are prohibited (P-39), and each access review confirms none exists | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-02 | AC | Approve TR-AC-02: AC-2k not applicable | Approve: shared and group accounts are prohibited (P-36), and \<System Name\> holds no accounts of its own | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-03 | AC | Approve TR-AC-03: AC-8a.01 notice names \<Organisation\>, not the U.S. Government | Approve, with the legal adviser agreeing the wording in \<Access Control Management\>, section 3.16 | Authorising official; legal adviser for the wording | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-04 | AC | Approve TR-AC-04: AC-8c not applicable | Approve: \<System Name\> is not publicly accessible, and only the actions in P-51 work without signing in | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-07 | AC | Approve TR-AC-07: AC-20(1) not applicable | Approve while no external system is approved under P-48 | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-08 | AC | Approve TR-AC-08: AC-22 not applicable | Approve: \<System Name\> holds no public content (P-50) | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-09 | AC | Approve TR-AC-09: AC-07\_ODP\[05\], \[06\] not selected | Approve: the account lock in P-42 is the chosen action | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-10 | AC | Approve TR-AC-10: AC-20\_ODP\[03\] not selected | Approve: the terms in P-48 are used, not asserted controls | Authorising official | \[Decision\] | \[Name\] | \[Date\] | None yet |
| \[D-XX-nn\] | \[XX\] | \[Decision needed\] | \[Recommendation\] | \[Who decides\] | \[Decision\] | \[Name\] | \[Date\] | \[Sheet\] |

## 3 Parameter approvals

The reference values are the parameters in \<System Description\>, section 4, which match \<Organisation\>'s corporate values. Each row records the approval of one control's parameters, with the main values proposed. The AC rows are numbered after the parameter they approve (D-AC-P02 approves P-02).

**Table 2: Parameter approvals**

| ID | Family | Control | Parameters | Main values | Who decides | Decision | Name | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D-AC-P02 | AC | AC-12 | 1: P-02 Sign-in lifetime | 8 hours from sign-in, no sliding extension, never longer than PingFederate's sign-in; open pages re-checked every 5 minutes | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P03 | AC | AC-11, AC-11(1) | 1: P-03 Device screen lock | 15 minutes, on managed devices and both servers. To be confirmed against \<Organisation\>'s evidence (EV-AC-07) | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P04 | AC | AC-2, AC-6(7) | 1: P-04 Review of role group members | Every 3 months | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P05 | AC | AC-2 | 1: P-05 Review of schema group members | Every 12 months | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P06 | AC | AC-2 | 1: P-06 Leavers and movers | AD account disabled at once; memberships removed within 5 working days; owners told of a mover within 1 working day | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P36 | AC | AC-2 | 1: P-36 Account types allowed | As in \<Access Control Management\>, Table 1 | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P37 | AC | AC-2 | 1: P-37 Who decides access | Line manager approves; the group's owner authorises and adds the person | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P38 | AC | AC-2(3) | 1: P-38 Unused accounts | AD accounts unused for 90 days disabled within 1 working day; monthly last sign-in check by the security officer. To be confirmed against \<Organisation\>'s evidence (EV-AC-01) | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P39 | AC | AC-2(2) | 1: P-39 Temporary and emergency accounts | Not allowed | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P40 | AC | AC-10 (beyond the baseline) | 1: P-40 Sign-ins at once | No limit; recorded for information only | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P41 | AC | AC-2(13) | 1: P-41 Disabling a high-risk individual | Within 1 hour of notice; \<System Name\> refuses the person within 5 minutes | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P42 | AC | AC-7 | 1: P-42 Failed sign-ins | 10 failed attempts in 15 minutes lock the account for 15 minutes, then it unlocks automatically. To be confirmed against \<Organisation\>'s evidence (EV-IA-04, EV-AC-05) | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P43 | AC | AC-8 | 1: P-43 System use notice wording | "Monitored, recorded and audited" wording in \<Access Control Management\>, section 3.16 | System owner and legal adviser | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P44 | AC | AC-6(1), AC-6(9), AC-6(10) | 1: P-44 Privileged functions and security-relevant information | As listed in P-44, including the OpenID Connect client credential | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P45 | AC | AC-6(2) | 1: P-45 Separate account for everyday work | Administrators use a separate non-privileged account for item work | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P46 | AC | AC-17 | 1: P-46 Remote access route | \<Organisation\>'s VPN, from a managed device, with multi-factor authentication. To be confirmed against \<Organisation\>'s evidence (EV-AC-08) | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P47 | AC | AC-18, AC-18(1), AC-19, AC-19(5) | 1: P-47 Wireless and mobile access | 802.1X user and device authentication with WPA2 or WPA3 Enterprise; managed, encrypted laptops only. To be confirmed against \<Organisation\>'s evidence (EV-AC-13, EV-AC-15) | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P48 | AC | AC-20, AC-20(2) | 1: P-48 External systems and portable storage | Only with the system owner's written approval as a TPL-17 exception, on the terms in P-48 | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P49 | AC | AC-21 | 1: P-49 Who decides on sharing outside a schema | The Data Owner, recorded on TPL-25 | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P50 | AC | AC-22 | 1: P-50 Public content | None, unless the system owner approves | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P51 | AC | AC-14 | 1: P-51 Actions allowed without signing in | The list in P-51, including the sign-in and signed-out return addresses and the loopback token request | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P52 | AC | AC-2, AC-6(7) | 1: P-52 Review of server and database accounts | Every 6 months, by the system owner and the security officer | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P53 | AC | AC-2(5) | 1: P-53 When users must sign out | End of each working day, and when leaving the device for longer than a short break | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P54 | AC | AC-17(4) | 1: P-54 Privileged access over remote access | Approved changes, maintenance and incident response only; VPN then the administration route, with multi-factor authentication at both; logged | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| D-AC-P55 | AC | AC-2 | 1: P-55 Account and access attributes | AD account name and ID, line manager, enabled state, expiry date; role groups and schema groups | System owner | \[Decision\] | \[Name\] | \[Date\] | None yet |
| \[D-XX-Pnn\] | \[XX\] | \[Control\] | \[Number of parameters\] | \[Main values\] | \[Who decides\] | \[Decision\] | \[Name\] | \[Date\] | \[Sheet\] |

## 4 Non-compliance treatment decisions

The control, rating, reason and treatment of each entry are in \<Risk List\>, section 5. This table records who decided, when, and the sheet that proves it, with one row for each batch of decisions. The system owner decides Low risks and the authorising official decides Medium and High risks. A provisional rating is confirmed when the evidence is seen.

**Table 3: Non-compliance treatment decisions**

| Entries | Family | Who decides | Decision | Name | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| \[NC-XX-nn\] | \[XX\] | \[Who decides\] | \[Decision\] | \[Name\] | \[Date\] | \[Sheet\] |

## 5 Proof of approval

Every decision in this register names the person who made it. Where the system owner records another person's decision, that person signs for it on their own sheet.

The Evidence column of each table names the sign-off sheet that proves the decision. A sheet is form TPL-24 in \<Record Templates\>. It lists the decisions by number, and the approver signs it, or confirms it by email or in a minuted meeting. One sheet covers every decision a person has made up to its date, and a new sheet is started for later decisions. "None yet" marks a decision that is still pending. A row that covers several entries counts once for each entry.

Until a sheet is filed, the decisions it covers rest on the system owner's record alone. The system owner files each sheet in the Restricted store and enters its reference and date below. Nobody signs for anyone else.

**Table 4: Sign-off sheets**

| Sheet | Approver | Role | Covers | Decisions | Filed |
| --- | --- | --- | --- | --- | --- |
| \[Sheet\] | \[Name\] | \[Role\] | \[Decisions covered\] | \[Number of decisions\] | \[Reference and date\] |
