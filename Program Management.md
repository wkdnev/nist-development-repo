# \<DocuView\> Program Management

**\<ref\> | Version \<ver\> | Draft for the system owner's approval**

**Contents**

[1 Document control](#1-document-control)

[2 Purpose](#2-purpose)

[3 Summary](#3-summary)

[4 The design](#4-the-design)

[5 Each control and enhancement](#5-each-control-and-enhancement)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<DocuView\> Program Management |
| Version | \<ver\> |
| Status | Draft for the system owner's approval |
| Date | 17 November 2026 |
| Owner | System owner |
| Applies to | Program Management family |
| Classification | Restricted |
| Next review | Every 12 months, and when ABC Technologies' programme changes |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | Neil Ramsbottom | Pending | Pending |

### 1.3 Change history

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | References to the personal data design point to \<PII Processing Management\>, where it is now held (D-PT-22) |
| \<ver\> | 17 November 2026 | The system owner's decision on the cross-check (D-PM-07): ABC Technologies' ISO/IEC 27001 certificate is the first choice of evidence for its programme |
| \<ver\> | 17 November 2026 | Cross-check of each control against the documents it points to: six entries for \<DocuView\>'s part corrected or completed; the official who authorises ABC Technologies' common controls shown as not named; ABC Technologies' ISO/IEC 27001 certificate named as the first choice of evidence; and how the design is kept current set out |
| \<ver\> | 17 November 2026 | The system owner's decisions on the review (D-PM-06): the PM controls in the privacy baseline stay inherited and are not assessed, for the authorising official to confirm; the three added enhancements are confirmed |
| \<ver\> | 17 November 2026 | Issued into the set as a draft for review |
| \<ver\> | 17 November 2026 | First draft, at the system owner's request (D-PM-05). The list of Program Management controls that \<DocuView\> inherits moved here from \<Tailoring Register\>, so that this design is held only in this document. Three enhancements are added to the list, and each control shows whether NIST places it in the privacy baseline. No decision is changed |

| **SECTION 2** |
| --- |

## 2 Purpose

This document shows how \<DocuView\> relies on ABC Technologies' security and privacy programme, for each of the 36 Program Management (PM) controls and enhancements in NIST SP 800-53 Rev 5. Section 4 sets out the design: why PM is treated differently from the other families, who leads the programme, which control is provided by whom and what \<DocuView\> adds, the PM controls NIST places in the privacy baseline, and what is asked of ABC Technologies. Section 5 takes each control in turn.

This is the only place this design is held. Other documents point here. The decision that PM is outside \<DocuView\>'s baseline is TR-PM-01 in \<Tailoring Register\>.

**PM is different from the other families.** Its controls describe an organisation's whole security and privacy programme, not one system. NIST does not place them in the Low, Moderate or High baselines, and expects them to be implemented once, for the organisation. \<DocuView\> therefore has no PM policy or procedures of its own, sets no PM parameter values, and gives no PM control a status. It inherits the controls from ABC Technologies as common controls (NIST SP 800-37, task P-5), and its own documents follow ABC Technologies' programme where that is known.

An assessor of \<DocuView\> will ask who provides each common control, what evidence shows it, and how \<DocuView\> knows the programme it relies on exists. So for each control this document gives:

- **what NIST requires**, in one line;
- **who provides it**;
- **which of \<DocuView\>'s controls rely on it**, and what \<DocuView\> adds;
- **the evidence asked for**, and the position today.

| **SECTION 3** |
| --- |

## 3 Summary

There are 36 PM controls and enhancements. Two do not apply in the United Kingdom. ABC Technologies provides the other 34, in some cases with the Head of Cyber or the legal adviser. None is evidenced: the four evidence requests have not been sent.

**Table 4: PM controls by group**

| Group | Controls | In the privacy baseline | Evidence requests | State |
| --- | --- | --- | --- | --- |
| Security programme | 19 | 10 | EV-PM-01, EV-PM-02, EV-PM-03, EV-PL-01 | Not sent |
| Risk management | 5 | 3 | EV-PM-01, EV-PM-03 | Not sent |
| Privacy programme | 12 | 11 | EV-PM-04 | Not sent |

NIST places 24 of the PM controls in its privacy baseline, which \<DocuView\> applies because it holds personal data. They are still the organisation's to provide, but they matter more to \<DocuView\> than the rest: section 4.4 lists them.

Two decisions are open with other people. The Head of Cyber has not confirmed that he is the senior information security officer, nor that \<DocuView\>'s risk thresholds fit ABC Technologies' risk appetite (D-PM-03). The legal adviser has not named the data protection officer, or recorded why none is required (D-PM-04). The gap as a whole is registered in the Risk List (R-AC-11) and the Plan of Action and Milestones (PA-124).

| **SECTION 4** |
| --- |

## 4 The design

### 4.1 Principles

1. **One programme.** ABC Technologies runs one security and privacy programme, and \<DocuView\> is one system within it.
2. **Inherit with evidence.** A common control counts for \<DocuView\> only once ABC Technologies has evidenced it.
3. **Follow, and feed back.** \<DocuView\>'s policies, plans and registers follow the programme, and its risks, weaknesses and monitoring results feed back into it.
4. **Stand in, and say so.** Where ABC Technologies' document has not been seen, \<DocuView\>'s own document stands in, and the dependency is checked when the evidence arrives.

![Figure 1: How \<DocuView\> relies on the organisation's programme](figures/pmm-figure-1.png)

**Figure 1: How \<DocuView\> relies on the organisation's programme**

### 4.2 Who leads the programme

**Table 5: Programme roles**

| Role | Holder | Controls | State |
| --- | --- | --- | --- |
| Senior information security officer | Alf Fairy, Head of Cyber | PM-2 | Named by the system owner. His confirmation is pending (D-PM-03) |
| Senior official for privacy: the data protection officer | \[Name, or the reason none is required\] | PM-19 | For the legal adviser to complete (D-PM-04) |
| Authorising official | Bob Jones | PM-10 | Named |
| Authorising official for ABC Technologies' common controls | \[ABC common control official\] | PM-10 | Not named: asked of ABC Technologies (EV-CA-01; \<Assessment, Authorization, and Monitoring Management\>) |
| Senior accountable official for risk management | \[ABC Technologies to name\] | PM-29 | Not known. ABC Technologies is asked to name the official (EV-PM-01) |
| System owner | Neil Ramsbottom | All | Keeps \<DocuView\>'s documents in step with the programme, and sends the evidence requests |
| Legal adviser | Adrian Solicitor | PM-18 to PM-27 | Owns the privacy plan, and \<DocuView\>'s part of the privacy programme |

### 4.3 Which control is provided by whom

Agreed on 11 November 2026 (D-PM-02). Each Rev 5 PM control is listed with who provides it, which \<DocuView\> controls rely on it, what \<DocuView\> contributes, the evidence that would show it, whether NIST places it in the privacy baseline, and the position today. A consistency check confirms that every row names a provider and an evidence request that exists. The three enhancements, PM-7(1), PM-16(1) and PM-20(1), were added on 17 November 2026 and confirmed by the system owner (D-PM-06).

**Table 6: PM inheritance**

| PM control | Provider | \<DocuView\> controls that rely on it | \<DocuView\>'s part | Evidence | In the privacy baseline | Today |
| --- | --- | --- | --- | --- | --- | --- |
| PM-1 Information Security Program Plan | ABC Technologies, Head of Cyber | Every family's policy (xx-1) | The 19 family policies follow it | EV-PM-01 | No | Not evidenced (EV-PM-01) |
| PM-2 Information Security Program Leadership Role | Head of Cyber | All | Alf Fairy named as senior information security officer in \<System Security Plan\> (D-PM-03) | EV-PM-01 | No | Alf Fairy is named. His confirmation of the role is pending (D-PM-03) |
| PM-3 Information Security and Privacy Resources | ABC Technologies | CA-5, SA-2 | Fixes costed in \<Plan of Action and Milestones\>, and on TPL-23 | EV-PM-01 | Yes | Not evidenced (EV-PM-01) |
| PM-4 Plan of Action and Milestones Process | ABC Technologies, Head of Cyber | CA-5 | \<Plan of Action and Milestones\> feeds it | EV-PM-01 | Yes | \<DocuView\> keeps its own register. ABC Technologies' process has not been seen (EV-PM-01) |
| PM-5 System Inventory | ABC Technologies | CM-8, PL-2 | A system identifier, shown as a placeholder in \<System Security Plan\>, section 3 | EV-PM-02 | No | \<DocuView\>'s entry in the inventory is not known: a placeholder (EV-PM-02) |
| PM-5(1) Inventory of Personally Identifiable Information | ABC Technologies, legal adviser | PT-2, PT-3, CM-12 | Personal data inventory in \<PII Processing Management\>, section 4.3 | EV-PM-02 | Yes | \<DocuView\> keeps its own inventory of personal data. ABC Technologies' record of processing has not been seen (EV-PM-02) |
| PM-6 Measures of Performance | Head of Cyber | CA-7 | Monitoring results in \<Assessment, Authorization, and Monitoring Management\> | EV-PM-03 | Yes | Not evidenced (EV-PM-03) |
| PM-7 Enterprise Architecture | ABC Technologies | PL-2, PL-8, SA-17 | \<Security Architecture\> fits it | EV-PL-01 | Yes | ABC Technologies' enterprise architecture has not been seen (EV-PL-01) |
| PM-7(1) Offloading | ABC Technologies | PL-8, SA-8 | None | EV-PL-01 | No | Not evidenced (EV-PL-01) |
| PM-8 Critical Infrastructure Plan | ABC Technologies | CP-2 | None; \<DocuView\> is not critical infrastructure | EV-PM-01 | Yes | Not evidenced (EV-PM-01) |
| PM-9 Risk Management Strategy | ABC Technologies, Head of Cyber | RA-3, CA-5, CA-6 | Decision rules in \<Risk List\>, section 5.2, to be confirmed against the risk appetite (D-PM-03) | EV-PM-01 | Yes | \<DocuView\>'s thresholds are agreed, but not confirmed against ABC Technologies' risk appetite (D-PM-03; EV-PM-01) |
| PM-10 Authorization Process | ABC Technologies | CA-6 | TPL-18; authorising official named; acceptance of the inherited controls (\<Assessment, Authorization, and Monitoring Management\>) | EV-PM-03 | Yes | Bob Jones is named as authorising official. ABC Technologies' process has not been seen (EV-PM-03) |
| PM-11 Mission and Business Process Definition | ABC Technologies | CP-2, RA-2 | \<Concept of Operations\>; business impact in \<Contingency Planning Management\> | EV-PM-01 | Yes | Not evidenced (EV-PM-01) |
| PM-12 Insider Threat Program | ABC Technologies | AU-6, PS-3 | Audit records and reviews; the playbook for bulk export misuse (\<Incident Response Management\>, section 4.9) | EV-PM-01 | No | Not evidenced (EV-PM-01) |
| PM-13 Security and Privacy Workforce | ABC Technologies | AT-2, AT-3 | The role curriculum in \<Awareness and Training Management\>, and TPL-9 training records | EV-PM-01 | Yes | Not evidenced (EV-PM-01) |
| PM-14 Testing, Training, and Monitoring | Head of Cyber | CA-2, CA-7, AT-2, CP-4, IR-3 | Family tests and exercises; \<Assessment, Authorization, and Monitoring Management\> | EV-PM-03 | Yes | Not evidenced (EV-PM-03) |
| PM-15 Security and Privacy Groups and Associations | Head of Cyber | SI-5 | None | EV-PM-01 | No | Not evidenced (EV-PM-01) |
| PM-16 Threat Awareness Program | Head of Cyber | SI-5, RA-3 | Advisories handled under \<Procedures\>, PRO-SI-5 | EV-PM-01 | No | Not evidenced (EV-PM-01) |
| PM-16(1) Automated Means for Sharing Threat Intelligence | Head of Cyber | SI-5 | None | EV-PM-01 | No | Not evidenced (EV-PM-01) |
| PM-17 Protecting Controlled Unclassified Information on External Systems | Not applicable | None | United States only | None | Yes | Not applicable in the United Kingdom |
| PM-18 Privacy Program Plan | ABC Technologies, legal adviser | PT family, PL-2 | \<Privacy Plan\> follows it | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-19 Privacy Program Leadership Role | ABC Technologies | PT family | Data protection officer placeholder in \<Roles and Responsibilities\> and \<Privacy Plan\> (D-PM-04) | EV-PM-04 | Yes | The data protection officer is not named, nor the reason recorded why none is required (D-PM-04) |
| PM-20 Dissemination of Privacy Program Information | ABC Technologies | PT-5 | Employee privacy notice (EV-PT-01) | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-20(1) Privacy Policies on Websites, Applications, and Digital Services | ABC Technologies | PT-5 | A link to the employee privacy notice from \<DocuView\>'s pages, which is not built (PA-90) | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-21 Accounting of Disclosures | ABC Technologies, legal adviser | PT-2, AU-2 | Exports and shares are audited | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-22 Personally Identifiable Information Quality Management | ABC Technologies | SI-18 | The yearly check of accuracy (\<Procedures\>, PRO-PT-5) | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-23 Data Governance Body | ABC Technologies | PT-2 | None | EV-PM-04 | No | Not evidenced (EV-PM-04) |
| PM-24 Data Integrity Board | Not applicable | None | United States only | None | Yes | Not applicable in the United Kingdom |
| PM-25 Minimization of PII Used in Testing, Training, and Research | ABC Technologies | SA-8(33), SI-12(2) | Testing uses sample data only | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-26 Complaint Management | ABC Technologies, legal adviser | AC-3(14), PT-5 | TPL-15 privacy requests and TPL-22 complaints (\<Procedures\>, PRO-PT-1 and PRO-PT-2) | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-27 Privacy Reporting | ABC Technologies, legal adviser | IR-8(1) | Breach steps in section 4.8 of \<Incident Response Management\>, and the breach register in its section 4.14 | EV-PM-04 | Yes | Not evidenced (EV-PM-04) |
| PM-28 Risk Framing | ABC Technologies, Head of Cyber | RA-3, RA-7 | \<Risk List\> | EV-PM-01 | Yes | Not evidenced (EV-PM-01) |
| PM-29 Risk Management Program Leadership Roles | ABC Technologies | All | None | EV-PM-01 | No | Not evidenced (EV-PM-01) |
| PM-30 Supply Chain Risk Management Strategy | ABC Technologies | SR-2, SR-3 | \<Supply Chain Risk Management\> follows it | EV-PM-03 | No | Not evidenced (EV-PM-03) |
| PM-31 Continuous Monitoring Strategy | ABC Technologies, Head of Cyber | CA-7 | \<Assessment, Authorization, and Monitoring Management\> follows it | EV-PM-03 | Yes | Not evidenced (EV-PM-03) |
| PM-32 Purposing | ABC Technologies | SA-8 | \<Concept of Operations\> states \<DocuView\>'s purpose | EV-PM-01 | No | Not evidenced (EV-PM-01) |

Where ABC Technologies' document is not yet seen, \<DocuView\>'s own document stands in, and the dependency is checked when the evidence arrives.

### 4.4 PM controls in the privacy baseline

\<DocuView\> applies NIST's privacy baseline, as it holds HR documents with personal data (D-PT-01). That baseline includes 24 PM controls: PM-3, PM-4, PM-5(1), PM-6 to PM-11, PM-13, PM-14, PM-17 to PM-22, PM-20(1), PM-24 to PM-28 and PM-31. NIST still expects them to be met once, by the organisation's programme, so they stay ABC Technologies' to provide. The system owner decided on 17 November 2026 that they stay inherited and are not assessed for \<DocuView\>, and the authorising official is asked to confirm it (D-PM-06). Two of them, PM-17 and PM-24, rest on United States law and do not apply.

For the rest, \<DocuView\>'s privacy controls depend on them directly: the personal data inventory on PM-5(1), complaints on PM-26, breach reporting on PM-27, and the privacy plan on PM-18. Until ABC Technologies evidences its privacy programme (EV-PM-04, EV-PM-02), \<DocuView\>'s own privacy plan, inventory and procedures stand in.

### 4.5 What is asked of ABC Technologies

**Table 7: Asked of ABC Technologies**

| Request | Controls | What is asked | State |
| --- | --- | --- | --- |
| EV-PM-01 | PM-1, PM-2, PM-3, PM-8, PM-9, PM-11, PM-12, PM-13, PM-15, PM-16, PM-16(1), PM-28, PM-29, PM-32 | The information security programme plan, the risk management strategy and risk appetite, and the roles that lead them | Not sent |
| EV-PM-02 | PM-5, PM-5(1) | \<DocuView\>'s entry in the system inventory, and its HR personal data in the record of processing | Not sent |
| EV-PM-03 | PM-6, PM-10, PM-14, PM-30, PM-31 | How systems are authorised, tested and monitored, how performance is measured, and how supply chain risk is managed | Not sent |
| EV-PM-04 | PM-18 to PM-23, PM-20(1), PM-25 to PM-27 | The privacy programme plan, the data protection officer or the reason none is required, and the complaint and reporting processes | Not sent |
| EV-PL-01 | PM-7, PM-7(1) | The enterprise architecture standards that \<DocuView\> must fit | Not sent |

The first choice of evidence is ABC Technologies' ISO/IEC 27001 certificate, with its scope statement and Statement of Applicability. That standard certifies the management system itself: its leadership, risk management, resources, measurement and review. One certificate whose scope includes the services \<DocuView\> uses would evidence most of the security programme controls at once. Where it does not, or if ABC Technologies holds no certificate, the documents in each request are asked for. The system owner agreed this order on 17 November 2026 (D-PM-07).

### 4.6 Keeping this design current

The system owner reviews this document every 12 months with the plans (\<Procedures\>, PRO-PL-1), and whenever ABC Technologies answers an evidence request or changes its programme. What is received is recorded against each control in section 4.3. If the evidence shows that a control \<DocuView\> relies on is not in place, the shortfall is raised as a risk in \<Risk List\>, and the \<DocuView\> controls that rely on it are looked at again.

PM stays outside \<DocuView\>'s assessment for as long as the organisation's programme stays with ABC Technologies and the Head of Cyber, and neither the system owner nor the authorising official asks for it to be assessed (TR-PM-01). If that changes, the PM controls are assessed.

| **SECTION 5** |
| --- |

## 5 Each control and enhancement

The controls are grouped by what they govern, and are in NIST order within each group. No control is given a status: none is \<DocuView\>'s to implement. The Today column says what is known.

### 5.1 Security programme

**Table 8: Security programme controls**

| Control | NIST requires | Provided by | \<DocuView\>'s part | Today |
| --- | --- | --- | --- | --- |
| PM-1 Information Security Program Plan | An organisation-wide information security programme plan, approved by a senior official, reviewed on a schedule and protected | ABC Technologies, Head of Cyber | The 19 family policies follow it | Not evidenced (EV-PM-01) |
| PM-2 Information Security Program Leadership Role | A senior information security officer, with the mission and resources to run the programme | Head of Cyber | Alf Fairy named as senior information security officer in \<System Security Plan\> (D-PM-03) | Alf Fairy is named. His confirmation of the role is pending (D-PM-03) |
| PM-3 Information Security and Privacy Resources | The resources for the security and privacy programmes are planned for and provided | ABC Technologies | Fixes costed in \<Plan of Action and Milestones\>, and on TPL-23 | Not evidenced (EV-PM-01) |
| PM-4 Plan of Action and Milestones Process | A process that keeps plans of action and milestones, and reports on them | ABC Technologies, Head of Cyber | \<Plan of Action and Milestones\> feeds it | \<DocuView\> keeps its own register. ABC Technologies' process has not been seen (EV-PM-01) |
| PM-5 System Inventory | An inventory of the organisation's systems, kept up to date | ABC Technologies | A system identifier, shown as a placeholder in \<System Security Plan\>, section 3 | \<DocuView\>'s entry in the inventory is not known: a placeholder (EV-PM-02) |
| PM-5(1) Inventory of Personally Identifiable Information | An inventory of every system and programme that processes personal data | ABC Technologies, legal adviser | Personal data inventory in \<PII Processing Management\>, section 4.3 | \<DocuView\> keeps its own inventory of personal data. ABC Technologies' record of processing has not been seen (EV-PM-02) |
| PM-6 Measures of Performance | Measures of how well the security and privacy programmes perform, reported | Head of Cyber | Monitoring results in \<Assessment, Authorization, and Monitoring Management\> | Not evidenced (EV-PM-03) |
| PM-7 Enterprise Architecture | An enterprise architecture that considers security, privacy and risk | ABC Technologies | \<Security Architecture\> fits it | ABC Technologies' enterprise architecture has not been seen (EV-PL-01) |
| PM-7(1) Offloading | Functions that are not essential are moved to other systems or providers | ABC Technologies | None | Not evidenced (EV-PL-01) |
| PM-8 Critical Infrastructure Plan | Security and privacy are addressed in a plan for critical infrastructure and key resources | ABC Technologies | None; \<DocuView\> is not critical infrastructure | Not evidenced (EV-PM-01) |
| PM-10 Authorization Process | Systems are authorised through a managed process, with named people for each role | ABC Technologies | TPL-18; authorising official named; acceptance of the inherited controls (\<Assessment, Authorization, and Monitoring Management\>) | Bob Jones is named as authorising official. ABC Technologies' process has not been seen (EV-PM-03) |
| PM-11 Mission and Business Process Definition | Mission and business processes are defined with their information protection needs | ABC Technologies | \<Concept of Operations\>; business impact in \<Contingency Planning Management\> | Not evidenced (EV-PM-01) |
| PM-12 Insider Threat Program | An insider threat programme, with a team drawn from several disciplines | ABC Technologies | Audit records and reviews; the playbook for bulk export misuse (\<Incident Response Management\>, section 4.9) | Not evidenced (EV-PM-01) |
| PM-13 Security and Privacy Workforce | A programme to develop the security and privacy workforce | ABC Technologies | The role curriculum in \<Awareness and Training Management\>, and TPL-9 training records | Not evidenced (EV-PM-01) |
| PM-14 Testing, Training, and Monitoring | A process to plan and oversee security and privacy testing, training and monitoring across the organisation | Head of Cyber | Family tests and exercises; \<Assessment, Authorization, and Monitoring Management\> | Not evidenced (EV-PM-03) |
| PM-15 Security and Privacy Groups and Associations | Contact with security and privacy groups and associations | Head of Cyber | None | Not evidenced (EV-PM-01) |
| PM-16 Threat Awareness Program | A threat awareness programme that shares threat information across the organisation | Head of Cyber | Advisories handled under \<Procedures\>, PRO-SI-5 | Not evidenced (EV-PM-01) |
| PM-16(1) Automated Means for Sharing Threat Intelligence | Threat intelligence is shared by automated means | Head of Cyber | None | Not evidenced (EV-PM-01) |
| PM-32 Purposing | Systems that support essential services are analysed to make sure they are used only for their intended purpose | ABC Technologies | \<Concept of Operations\> states \<DocuView\>'s purpose | Not evidenced (EV-PM-01) |

### 5.2 Risk management

**Table 9: Risk management controls**

| Control | NIST requires | Provided by | \<DocuView\>'s part | Today |
| --- | --- | --- | --- | --- |
| PM-9 Risk Management Strategy | A strategy for managing security and privacy risk across the organisation, reviewed on a schedule | ABC Technologies, Head of Cyber | Decision rules in \<Risk List\>, section 5.2, to be confirmed against the risk appetite (D-PM-03) | \<DocuView\>'s thresholds are agreed, but not confirmed against ABC Technologies' risk appetite (D-PM-03; EV-PM-01) |
| PM-28 Risk Framing | The assumptions, constraints, priorities and tolerances that frame risk decisions are set and shared | ABC Technologies, Head of Cyber | \<Risk List\> | Not evidenced (EV-PM-01) |
| PM-29 Risk Management Program Leadership Roles | A senior accountable official for risk management and a risk executive function | ABC Technologies | None | Not evidenced (EV-PM-01) |
| PM-30 Supply Chain Risk Management Strategy | An organisation-wide strategy for managing supply chain risk | ABC Technologies | \<Supply Chain Risk Management\> follows it | Not evidenced (EV-PM-03) |
| PM-31 Continuous Monitoring Strategy | An organisation-wide continuous monitoring strategy and programme | ABC Technologies, Head of Cyber | \<Assessment, Authorization, and Monitoring Management\> follows it | Not evidenced (EV-PM-03) |

### 5.3 Privacy programme

**Table 10: Privacy programme controls**

| Control | NIST requires | Provided by | \<DocuView\>'s part | Today |
| --- | --- | --- | --- | --- |
| PM-17 Protecting Controlled Unclassified Information on External Systems | A policy for protecting controlled unclassified information held on external systems | Not applicable | United States only | Not applicable in the United Kingdom |
| PM-18 Privacy Program Plan | An organisation-wide privacy programme plan, approved by a senior official and reviewed on a schedule | ABC Technologies, legal adviser | \<Privacy Plan\> follows it | Not evidenced (EV-PM-04) |
| PM-19 Privacy Program Leadership Role | A senior official for privacy, with the authority and resources to run the programme | ABC Technologies | Data protection officer placeholder in \<Roles and Responsibilities\> and \<Privacy Plan\> (D-PM-04) | The data protection officer is not named, nor the reason recorded why none is required (D-PM-04) |
| PM-20 Dissemination of Privacy Program Information | A central public page that tells people about the privacy programme and how to reach the privacy office | ABC Technologies | Employee privacy notice (EV-PT-01) | Not evidenced (EV-PM-04) |
| PM-20(1) Privacy Policies on Websites, Applications, and Digital Services | Privacy policies are published on websites, applications and digital services, in plain language | ABC Technologies | A link to the employee privacy notice from \<DocuView\>'s pages, which is not built (PA-90) | Not evidenced (EV-PM-04) |
| PM-21 Accounting of Disclosures | An accurate account of disclosures of personal data, kept for a set time and given to the person on request | ABC Technologies, legal adviser | Exports and shares are audited | Not evidenced (EV-PM-04) |
| PM-22 Personally Identifiable Information Quality Management | Organisation-wide policies for the accuracy, relevance, timeliness and completeness of personal data | ABC Technologies | The yearly check of accuracy (\<Procedures\>, PRO-PT-5) | Not evidenced (EV-PM-04) |
| PM-23 Data Governance Body | A data governance body, with defined roles and duties | ABC Technologies | None | Not evidenced (EV-PM-04) |
| PM-24 Data Integrity Board | A data integrity board to review computer matching agreements | Not applicable | United States only | Not applicable in the United Kingdom |
| PM-25 Minimization of PII Used in Testing, Training, and Research | Policies that limit the personal data used in testing, training and research | ABC Technologies | Testing uses sample data only | Not evidenced (EV-PM-04) |
| PM-26 Complaint Management | A process for receiving and answering complaints about privacy practices, within set times | ABC Technologies, legal adviser | TPL-15 privacy requests and TPL-22 complaints (\<Procedures\>, PRO-PT-1 and PRO-PT-2) | Not evidenced (EV-PM-04) |
| PM-27 Privacy Reporting | Privacy reports to the oversight bodies and officials who need them | ABC Technologies, legal adviser | Breach steps in section 4.8 of \<Incident Response Management\>, and the breach register in its section 4.14 | Not evidenced (EV-PM-04) |
