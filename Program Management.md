# \<System Name\> Program Management

## 1 Purpose

This document is the design for how \<System Name\> relies on \<Organisation\>'s security and privacy programme. It covers the 37 Program Management (PM) controls and enhancements in CSS (catalog release 5.2.0).

Section 3 is the design: who leads the programme, which control is provided by whom and what \<System Name\> adds, the PM controls in the privacy baseline, what \<Organisation\> provides, and how the design is kept current.

**PM is different from the other families.** Its controls describe an organisation's whole security and privacy programme, not one system, and are implemented once, for the organisation. \<System Name\> therefore has no PM policy or procedures of its own. The controls are common controls provided by \<Organisation\> (TR-PM-01), \<System Name\> inherits them, and its own documents follow \<Organisation\>'s programme where that is known.

The decision that PM is inherited is TR-PM-01 in \<Tailoring Register\>, approved by the authorising official (D-PM-01). The evidence asked of \<Organisation\> is in \<Evidence Requests\>, section 15.

The PM values are set at corporate level by \<Organisation\>, and \<System Name\> sets none of its own. Anything in section 3 that depends on such a value matches it, and is changed in this document where it does not.

## 2 Summary

There are 37 PM controls and enhancements. Two do not apply in the United Kingdom. \<Organisation\> provides the other 35, in some cases with the Head of Cyber or the legal adviser.

**Table 1: PM controls by group**

| Group | Controls | In the privacy baseline |
| --- | --- | --- |
| Security programme | 19 | 10 |
| Risk management | 6 | 3 |
| Privacy programme | 12 | 11 |

24 of the PM controls are in the privacy baseline, which \<System Name\> applies because it holds personal data. They are still the organisation's to provide, but they matter more to \<System Name\> than the rest: section 3.4 lists them.

No PM control is \<System Name\>'s own: none is met by the system, shared or met by \<System Name\>'s people. What \<System Name\> contributes to each is in section 3.3.

**Table 2: How the PM controls are treated**

| Treatment | Controls | Number | Where it is recorded |
| --- | --- | --- | --- |
| Inherited: an organisation-level common control, provided by \<Organisation\>'s programme and not assessed for \<System Name\> | Every PM control and enhancement except PM-17 and PM-24 | 35 | TR-PM-01; section 3.3 |
| Not applicable: rests on United States law | PM-17, PM-24 | 2 | TR-PM-01 |
| System, hybrid or organisational | None | 0 | None |

Two roles rest with other people. The Head of Cyber is the senior information security officer, and confirms that \<System Name\>'s risk thresholds fit \<Organisation\>'s risk appetite. The legal adviser names the data protection officer, or records why none is required. The authorising official approves the treatment in Table 2 (TR-PM-01; \<Decision Register\>, D-PM-01).

## 3 The design

### 3.1 Principles

1. **One programme.** \<Organisation\> runs one security and privacy programme, and \<System Name\> is one system within it.
2. **Inherit what is confirmed.** \<System Name\> relies on a common control once \<Organisation\> has confirmed it. Before \<System Name\> operates, the authorising official accepts reliance on the programme for the 35 inherited PM controls as one line on the authorisation decision record, naming any not yet evidenced.
3. **Follow, and report to the authorising official.** \<System Name\>'s policies, plans and registers follow the programme. Its plan of action and monitoring results are reported each quarter to the authorising official only (\<Assessment, Authorization, and Monitoring Management\>, sections 3.4 and 3.8); the Head of Cyber receives the assessment report and the authorisation decision. Whether anything more must reach \<Organisation\>'s own processes is for \<Organisation\> to say.
4. **Stand in, and say so.** Where \<Organisation\>'s document has not been seen, \<System Name\>'s own document stands in, and the dependency is checked when the evidence arrives.

![Figure 1: How \<System Name\> relies on the organisation's programme](figures/pmm-figure-1.png)

**Figure 1: How \<System Name\> relies on the organisation's programme**

### 3.2 Who leads the programme

**Table 3: Programme roles**

| Role | Holder | Controls | Notes |
| --- | --- | --- | --- |
| Senior information security officer | \[Name\], Head of Cyber | PM-2 | |
| Senior official for privacy: the data protection officer | \[Name, or the reason none is required\] | PM-19 | Completed by the legal adviser |
| Authorising official | \[Name\] | PM-10 | |
| Authorising official for \<Organisation\>'s common controls | \[Organisation common control official\] | PM-10 | Asked of \<Organisation\> (\<Assessment, Authorization, and Monitoring Management\>) |
| Senior accountable official for risk management | \[\<Organisation\> to name\] | PM-29 | \<Organisation\> is asked to name the official |
| System owner | \[Name\] | All | Keeps \<System Name\>'s documents in step with the programme, and sends the evidence requests |
| Legal adviser | \[Name\] | PM-18 to PM-27 | Owns the privacy plan, and \<System Name\>'s part of the privacy programme |

### 3.3 Which control is provided by whom

Each PM control is listed with who provides it, which \<System Name\> controls rely on it, what \<System Name\> contributes, and whether it is in the privacy baseline. All five enhancements, PM-5(1), PM-7(1), PM-16(1), PM-20(1) and PM-30(1), are included.

**Table 4: PM inheritance**

| PM control | Provider | \<System Name\> controls that rely on it | \<System Name\>'s part | In the privacy baseline |
| --- | --- | --- | --- | --- |
| PM-1 Information Security Program Plan | \<Organisation\>, Head of Cyber | Every family's policy (xx-1) | The 19 family policies follow it | No |
| PM-2 Information Security Program Leadership Role | \<Organisation\>, which appoints the Head of Cyber | All | \[Name\] named as senior information security officer in \<System Security Plan\> | No |
| PM-3 Information Security and Privacy Resources | \<Organisation\> | CA-5, SA-2 | Fixes costed in \<Plan of Action and Milestones\>, and on the risk and supply chain review | Yes |
| PM-4 Plan of Action and Milestones Process | \<Organisation\>, Head of Cyber | CA-5 | \<Plan of Action and Milestones\> is kept for \<System Name\>, and its overdue items are reported each quarter to the authorising official. It is not sent to \<Organisation\>'s own process, which has not been seen | Yes |
| PM-5 System Inventory | \<Organisation\> | CM-8, PL-2 | A system identifier, shown as a placeholder in \<System Security Plan\>, section 2 | No |
| PM-5(1) Inventory of Personally Identifiable Information | \<Organisation\>, legal adviser | PT-2, PT-3, CM-12 | Personal data inventory in \<PII Processing Management\>, section 3.3 | Yes |
| PM-6 Measures of Performance | Head of Cyber | CA-7 | \<System Name\>'s own measures in \<Assessment, Authorization, and Monitoring Management\>, section 3.8, reported to the authorising official. They are not part of \<Organisation\>'s measures | Yes |
| PM-7 Enterprise Architecture | \<Organisation\> | PL-2, PL-8, SA-17 | \<System Description\>, section 6, fits it | Yes |
| PM-7(1) Offloading | \<Organisation\> | PL-8, SA-8 | None | No |
| PM-8 Critical Infrastructure Plan | \<Organisation\> | CP-2 | None; \<System Name\> is not critical infrastructure | Yes |
| PM-9 Risk Management Strategy | \<Organisation\>, Head of Cyber | RA-3, CA-5, CA-6 | Decision rules in \<Risk List\>, section 4.2, set to fit the risk appetite | Yes |
| PM-10 Authorization Process | \<Organisation\> | CA-6 | Authorisation decision record, on which the authorising official accepts the 62 inherited controls and, as one line, reliance on this programme for the 35 inherited PM controls (\<Assessment, Authorization, and Monitoring Management\>, section 3.5) | Yes |
| PM-11 Mission and Business Process Definition | \<Organisation\> | CP-2, RA-2 | \<Concept of Operations\>; business impact in \<Contingency Planning Management\> | Yes |
| PM-12 Insider Threat Program | \<Organisation\> | AU-6, PS-3 | Audit records and reviews; the playbook for bulk export misuse (\<Incident Response Management\>, section 3.9) | No |
| PM-13 Security and Privacy Workforce | \<Organisation\> | AT-2, AT-3 | The role curriculum in \<Awareness and Training Management\>, and the training records | Yes |
| PM-14 Testing, Training, and Monitoring | Head of Cyber | CA-2, CA-7, AT-2, CP-4, IR-3 | Family tests and exercises; \<Assessment, Authorization, and Monitoring Management\> | Yes |
| PM-15 Security and Privacy Groups and Associations | Head of Cyber | SI-5 | None | No |
| PM-16 Threat Awareness Program | Head of Cyber | SI-5, RA-3 | Advisories handled as \<System and Information Integrity Management\>, section 3.3, sets out | No |
| PM-16(1) Automated Means for Sharing Threat Intelligence | Head of Cyber | SI-5 | None | No |
| PM-17 Protecting Controlled Unclassified Information on External Systems | Not applicable | None | United States only | Yes |
| PM-18 Privacy Program Plan | \<Organisation\>, legal adviser | PT family, PL-2 | \<Privacy Plan\> follows it | Yes |
| PM-19 Privacy Program Leadership Role | \<Organisation\> | PT family | Data protection officer placeholder in \<Roles and Responsibilities\> and \<Privacy Plan\> | Yes |
| PM-20 Dissemination of Privacy Program Information | \<Organisation\> | PT-5 | The privacy notices for employees, contractors and agency staff | Yes |
| PM-20(1) Privacy Policies on Websites, Applications, and Digital Services | \<Organisation\> | PT-5 | A link to the privacy notices from \<System Name\>'s pages (FR-010) | Yes |
| PM-21 Accounting of Disclosures | \<Organisation\>, legal adviser | PT-2, AU-2 | Downloads and exports are audited, which shows what personal data left \<System Name\>, when and by whom. They are not the accounting itself: the recipient, purpose and address of a disclosure outside \<Organisation\>, and keeping the accounting for 5 years or for as long as the data is held, are \<Organisation\>'s (\<Audit and Accountability Management\>, Appendix B) | Yes |
| PM-22 Personally Identifiable Information Quality Management | \<Organisation\> | SI-18 | The yearly check of accuracy | Yes |
| PM-23 Data Governance Body | \<Organisation\> | PT-2 | None | No |
| PM-24 Data Integrity Board | Not applicable | None | United States only | Yes |
| PM-25 Minimization of PII Used in Testing, Training, and Research | \<Organisation\> | SA-8(33), SI-12(2) | Testing and development use invented data only | Yes |
| PM-26 Complaint Management | \<Organisation\>, legal adviser | AC-3(14), PT-5 | Records of privacy requests and data protection complaints | Yes |
| PM-27 Privacy Reporting | \<Organisation\>, legal adviser | IR-8(1) | Breach steps in section 3.8 of \<Incident Response Management\>, and the breach register in its section 3.14 | Yes |
| PM-28 Risk Framing | \<Organisation\>, Head of Cyber | RA-3, RA-7 | \<Risk List\> | Yes |
| PM-29 Risk Management Program Leadership Roles | \<Organisation\> | All | None | No |
| PM-30 Supply Chain Risk Management Strategy | \<Organisation\> | SR-2, SR-3 | \<Supply Chain Risk Management\> follows it | No |
| PM-30(1) Suppliers of Critical or Mission-essential Items | \<Organisation\> | RA-9, SR-3, SR-6 | The supplier register with criticality in \<Supply Chain Risk Management\>, section 3.5, and the critical components in \<Risk Assessment Management\>, section 3.9 | No |
| PM-31 Continuous Monitoring Strategy | \<Organisation\>, Head of Cyber | CA-7 | \<Assessment, Authorization, and Monitoring Management\>, section 3.8, follows it; \<System Name\>'s status is reported to the authorising official, not to \<Organisation\>'s programme | Yes |
| PM-32 Purposing | \<Organisation\> | SA-8 | \<Concept of Operations\> states \<System Name\>'s purpose | No |

Where \<Organisation\>'s document is not yet seen, \<System Name\>'s own document stands in, and the dependency is checked when the evidence arrives.

### 3.4 PM controls in the privacy baseline

\<System Name\> applies the CSS privacy baseline, as it holds personal data. That baseline includes 24 PM controls: PM-3, PM-4, PM-5(1), PM-6 to PM-11, PM-13, PM-14, PM-17 to PM-22, PM-20(1), PM-24 to PM-28 and PM-31. They are met once, by the organisation's programme, so they stay \<Organisation\>'s to provide, and inherited. Two of them, PM-17 and PM-24, rest on United States law and do not apply.

For the rest, \<System Name\>'s privacy controls depend on them directly: the personal data inventory on PM-5(1), complaints on PM-26, breach reporting on PM-27, and the privacy plan on PM-18. Until \<Organisation\> evidences its privacy programme, \<System Name\>'s own privacy plan, inventory and procedures stand in.

### 3.5 What \<Organisation\> provides

**Table 5: Provided by \<Organisation\>**

| Provided | What \<System Name\> relies on |
| --- | --- |
| The information security programme | A programme plan, a risk management strategy with a stated risk appetite, and named leaders, including the senior accountable official for risk management |
| The system inventory and the record of processing | An entry for \<System Name\> in the system inventory, and its personal data in the record of processing |
| Authorisation, testing, monitoring and supply chain risk management | Processes for authorising, testing and monitoring systems, measures of performance, and a supply chain risk management strategy with its suppliers of critical items |
| The privacy programme | A privacy programme plan, a data protection officer or the reason none is required, and the complaint and reporting processes |
| The enterprise architecture | The standards \<System Name\>'s architecture must fit |

### 3.6 Keeping this design current

The system owner reviews this document every 12 months, when the condition of TR-PM-01 is checked with the other tailoring entries, and whenever \<Organisation\> answers an evidence request or changes its programme. What is received is recorded in \<Evidence Requests\>. Until the evidence is seen, the dependency is held in \<Risk List\> as R-PM-02. If the evidence shows that a control \<System Name\> relies on is not in place, the shortfall is raised as a risk in \<Risk List\>, and the \<System Name\> controls that rely on it are looked at again.

PM stays outside \<System Name\>'s assessment for as long as the organisation's programme stays with \<Organisation\> and the Head of Cyber, and neither the system owner nor the authorising official asks for it to be assessed (TR-PM-01, approved by the authorising official in D-PM-01). If that changes, the PM controls are assessed.
