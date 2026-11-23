# \<System Name\> Program Management

## 1 Purpose

This document is the design for how \<System Name\> relies on \<Organisation\>'s security and privacy programme. It covers the 37 Program Management (PM) controls and enhancements in CSS (catalog release 5.2.0).

Section 3 is the design: who leads the programme, which control is provided by whom and what \<System Name\> adds, the PM controls in the privacy baseline, what \<Organisation\> provides, and how the design is kept current.

**PM is different from the other families.** Its controls describe an organisation's whole security and privacy programme, not one system, and are implemented once, for the organisation. \<System Name\> therefore has no PM policy or procedures of its own. The controls are common controls provided by \<Organisation\>, \<System Name\> inherits them, and its own documents follow \<Organisation\>'s programme where that is known.

The decision that PM is inherited is recorded in \<Tailoring Register\>, approved by the authorising official. The evidence asked of \<Organisation\> is in \<Evidence Requests\>, section 15.

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
| Inherited: an organisation-level common control, provided by \<Organisation\>'s programme and not assessed for \<System Name\> | Every programme control and enhancement except the two below | 35 | \<Tailoring Register\>; section 3.3 |
| Not applicable: rests on United States law | Protecting controlled unclassified information on external systems; the data integrity board | 2 | \<Tailoring Register\> |
| System, hybrid or organisational | None | 0 | None |

Two roles rest with other people. The Head of Cyber is the senior information security officer, and confirms that \<System Name\>'s risk thresholds fit \<Organisation\>'s risk appetite. The legal adviser names the data protection officer, or records why none is required. The authorising official approves the treatment in Table 2 (\<Decision Register\>).

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

| Role | Holder | Notes |
| --- | --- | --- |
| Senior information security officer | \[Name\], Head of Cyber |  |
| Senior official for privacy: the data protection officer | \[Name, or the reason none is required\] | Completed by the legal adviser |
| Authorising official | \[Name\] |  |
| Authorising official for \<Organisation\>'s common controls | \[Organisation common control official\] | Asked of \<Organisation\> (\<Assessment, Authorization, and Monitoring Management\>) |
| Senior accountable official for risk management | \[\<Organisation\> to name\] | \<Organisation\> is asked to name the official |
| System owner | \[Name\] | Keeps \<System Name\>'s documents in step with the programme, and sends the evidence requests |
| Legal adviser | \[Name\] | Owns the privacy plan, and \<System Name\>'s part of the privacy programme |

### 3.3 Which control is provided by whom

Each programme control is listed with who provides it, what \<System Name\> contributes, and whether it is in the privacy baseline. All five enhancements are included.

**Table 4: PM inheritance**

| Programme control | Provider | \<System Name\>'s part |
| --- | --- | --- |
| Information security programme plan | \<Organisation\>, Head of Cyber | The 19 family policies follow it |
| Information security programme leadership role | \<Organisation\>, which appoints the Head of Cyber | \[Name\] named as senior information security officer in \<System Security Plan\> |
| Information security and privacy resources (also in the privacy baseline) | \<Organisation\> | Fixes costed in \<Plan of Action and Milestones\>, and on the risk and supply chain review |
| Plan of action and milestones process (also in the privacy baseline) | \<Organisation\>, Head of Cyber | \<Plan of Action and Milestones\> is kept for \<System Name\>, and its overdue items are reported each quarter to the authorising official. It is not sent to \<Organisation\>'s own process, which has not been seen |
| System inventory | \<Organisation\> | A system identifier, shown as a placeholder in \<System Security Plan\>, section 2 |
| Inventory of personally identifiable information (also in the privacy baseline) | \<Organisation\>, legal adviser | Personal data inventory in \<PII Processing Management\>, section 3.3 |
| Measures of performance (also in the privacy baseline) | Head of Cyber | \<System Name\>'s own measures in \<Assessment, Authorization, and Monitoring Management\>, section 3.8, reported to the authorising official. They are not part of \<Organisation\>'s measures |
| Enterprise architecture (also in the privacy baseline) | \<Organisation\> | \<System Description\>, section 6, fits it |
| Offloading | \<Organisation\> | None |
| Critical infrastructure plan (also in the privacy baseline) | \<Organisation\> | None; \<System Name\> is not critical infrastructure |
| Risk management strategy (also in the privacy baseline) | \<Organisation\>, Head of Cyber | Decision rules in \<Risk List\>, section 4.2, set to fit the risk appetite |
| Authorization process (also in the privacy baseline) | \<Organisation\> | Authorisation decision record, on which the authorising official accepts the 62 inherited controls and, as one line, reliance on this programme for the 35 inherited PM controls (\<Assessment, Authorization, and Monitoring Management\>, section 3.5) |
| Mission and business process definition (also in the privacy baseline) | \<Organisation\> | \<Concept of Operations\>; business impact in \<Contingency Planning Management\> |
| Insider threat programme | \<Organisation\> | Audit records and reviews; the playbook for bulk export misuse (\<Incident Response Management\>, section 3.9) |
| Security and privacy workforce (also in the privacy baseline) | \<Organisation\> | The role curriculum in \<Awareness and Training Management\>, and the training records |
| Testing, training, and monitoring (also in the privacy baseline) | Head of Cyber | Family tests and exercises; \<Assessment, Authorization, and Monitoring Management\> |
| Security and privacy groups and associations | Head of Cyber | None |
| Threat awareness programme | Head of Cyber | Advisories handled as \<System and Information Integrity Management\>, section 3.3, sets out |
| Automated means for sharing threat intelligence | Head of Cyber | None |
| Protecting controlled unclassified information on external systems (also in the privacy baseline) | Not applicable | United States only |
| Privacy programme plan (also in the privacy baseline) | \<Organisation\>, legal adviser | \<Privacy Plan\> follows it |
| Privacy programme leadership role (also in the privacy baseline) | \<Organisation\> | Data protection officer placeholder in \<Roles and Responsibilities\> and \<Privacy Plan\> |
| Dissemination of privacy programme information (also in the privacy baseline) | \<Organisation\> | The privacy notices for employees, contractors and agency staff |
| Privacy policies on websites, applications, and digital services (also in the privacy baseline) | \<Organisation\> | A link to the privacy notices from \<System Name\>'s pages |
| Accounting of disclosures (also in the privacy baseline) | \<Organisation\>, legal adviser | Downloads and exports are audited, which shows what personal data left \<System Name\>, when and by whom. They are not the accounting itself: the recipient, purpose and address of a disclosure outside \<Organisation\>, and keeping the accounting for 5 years or for as long as the data is held, are \<Organisation\>'s (\<Audit and Accountability Management\>, Appendix B) |
| Personally identifiable information quality management (also in the privacy baseline) | \<Organisation\> | The yearly check of accuracy |
| Data governance body | \<Organisation\> | None |
| Data integrity board (also in the privacy baseline) | Not applicable | United States only |
| Minimization of personal data used in testing, training, and research (also in the privacy baseline) | \<Organisation\> | Testing and development use invented data only |
| Complaint management (also in the privacy baseline) | \<Organisation\>, legal adviser | Records of privacy requests and data protection complaints |
| Privacy reporting (also in the privacy baseline) | \<Organisation\>, legal adviser | Breach steps in section 3.8 of \<Incident Response Management\>, and the breach register in its section 3.14 |
| Risk framing (also in the privacy baseline) | \<Organisation\>, Head of Cyber | \<Risk List\> |
| Risk management programme leadership roles | \<Organisation\> | None |
| Supply chain risk management strategy | \<Organisation\> | \<Supply Chain Risk Management\> follows it |
| Suppliers of critical or mission-essential items | \<Organisation\> | The supplier register with criticality in \<Supply Chain Risk Management\>, section 3.5, and the critical components in \<Risk Assessment Management\>, section 3.9 |
| Continuous monitoring strategy (also in the privacy baseline) | \<Organisation\>, Head of Cyber | \<Assessment, Authorization, and Monitoring Management\>, section 3.8, follows it; \<System Name\>'s status is reported to the authorising official, not to \<Organisation\>'s programme |
| Purposing | \<Organisation\> | \<Concept of Operations\> states \<System Name\>'s purpose |

Controls marked "also in the privacy baseline" are in both the CSS Moderate and the privacy baselines.

Where \<Organisation\>'s document is not yet seen, \<System Name\>'s own document stands in, and the dependency is checked when the evidence arrives.

### 3.4 PM controls in the privacy baseline

\<System Name\> applies the CSS privacy baseline, as it holds personal data. That baseline includes 24 programme controls, marked in Table 4. They are met once, by the organisation's programme, so they stay \<Organisation\>'s to provide, and inherited. Two of them, on controlled unclassified information and the data integrity board, rest on United States law and do not apply.

For the rest, \<System Name\>'s privacy controls depend on them directly: the personal data inventory, complaint management, privacy reporting and the privacy programme plan. Until \<Organisation\> evidences its privacy programme, \<System Name\>'s own privacy plan, inventory and procedures stand in.

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

The system owner reviews this document every 12 months, when the condition of its tailoring entry is checked with the others, and whenever \<Organisation\> answers an evidence request or changes its programme. What is received is recorded in \<Evidence Requests\>. Until the evidence is seen, the dependency is held as a risk in \<Risk List\>. If the evidence shows that a control \<System Name\> relies on is not in place, the shortfall is raised as a risk in \<Risk List\>, and the \<System Name\> controls that rely on it are looked at again.

PM stays outside \<System Name\>'s assessment for as long as the organisation's programme stays with \<Organisation\> and the Head of Cyber, and neither the system owner nor the authorising official asks for it to be assessed (approved by the authorising official). If that changes, the PM controls are assessed.
