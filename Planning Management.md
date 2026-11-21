# \<System Name\> Planning Management

## 1 Purpose

This document sets out how \<System Name\>'s plans are written, approved, shared, reviewed and protected, to meet the 7 Planning (PL) controls and enhancements in the CSS Moderate baseline.

Section 3 is the design: the principles, the register of every plan in force, what the security plan and the privacy plan must hold and where each part is, how a plan is approved and kept current, the rules of behaviour and who has signed them, the architecture, the baseline and its tailoring, what \<Organisation\> provides, and the policy and procedures. Each subsection names the controls it helps to meet. The plans themselves are separate documents, listed in section 3.2.

## 2 Related documents

Who provides and is responsible for each control, and its status, are in \<System Security Plan\>, section 7.12 (Table 21). The tests, their results and the records an assessor will ask for are in \<Control Assessment Record\> (PL). Each control's risk is in \<Risk List\>, and what is still open is in \<Plan of Action and Milestones\>. The policy is in \<Policy\> (PL), and the steps people follow are in \<Procedures\> (PL).

## 3 The design

### 3.1 Principles

Controls met here: PL-2, PL-4.

1. **One current set.** The System Security Plan is the single statement of how controls are met, and every plan it relies on is listed in one register.
2. **Rules before access.** Nobody gets access without signing the rules.
3. **Plans change with the system.** Plans change when the system, its risks or an assessment changes, and every review and change is recorded.
4. **Plans are protected.** Plans describe weaknesses, are marked \<Classification\>, and must be protected like the system itself.

These carry out the principles and rules of \<Policy\>, sections PL.3 and PL.4.

![Figure 1: How a plan is kept current](figures/plm-figure-1.png)

**Figure 1: How a plan is kept current**

### 3.2 Register of plans in force

Controls met here: PL-2.

Every plan and planning record in force, with its owner, version, approver and next review. The design documents for each control family are not plans, and are listed in \<Documentation Map\>.

**Table 1: Plans in force**

| Plan or record | Document | Version | Owner | Approver | Next review |
| --- | --- | --- | --- | --- | --- |
| System security plan | \<System Security Plan\> | \<ver\> | System owner | System owner, with the Head of Cyber's concurrence, and accepted by the authorising official as an accurate record | Every 12 months, and after a significant change |
| Privacy plan | \<Privacy Plan\> | \<ver\> | Legal adviser | Legal adviser and authorising official | Every 12 months |
| Data protection impact assessment | \<Data Protection Impact Assessment\> | \<ver\> | Legal adviser | Legal adviser | Before real data is held, and after a significant change in processing |
| Supply chain risk management plan | \<Supply Chain Risk Management\> | \<ver\> | System owner | System owner | Every 12 months |
| Configuration management plan | \<Configuration Management\> | \<ver\> | System owner | System owner | Every 12 months |
| Contingency plan | \<Contingency Planning Management\> | \<ver\> | System owner | System owner and authorising official | Every 12 months, and after a test or activation |
| Incident response plan | \<Incident Response Management\> | \<ver\> | Security officer | Head of Cyber | Every 12 months, and after an incident or exercise |
| Continuous monitoring strategy | \<Assessment, Authorization, and Monitoring Management\> | \<ver\> | System owner | System owner | Every 12 months |
| Security architecture | \<System Description\>, section 6 | \<ver\> | System owner | System owner | Every 12 months, and after a significant change |
| Concept of operations | \<Concept of Operations\> | \<ver\> | System owner | System owner | Every 12 months |
| Rules of behaviour | \<Security Operating Procedures\> | \<ver\> | System owner | System owner | Every 12 months, and after a material change |
| Baseline and tailoring | CSS Moderate and privacy baselines; \<Tailoring Register\> | \<ver\> | System owner | System owner, accepted by the authorising official | Every 12 months, and when a condition changes |
| Risk list | \<Risk List\> | \<ver\> | System owner | System owner | Every 3 months once in operation |
| Plan of action | \<Plan of Action and Milestones\> | \<ver\> | System owner | System owner | Monthly once in operation |

The versions in the register are checked by the plan consistency test, and are brought up to date whenever a plan is given a new version. The register is kept in the restricted document store with the plans.

### 3.3 What the plans hold

Controls met here: PL-2.

PL-2 lists 15 things a security plan and a privacy plan must hold. The security plan is \<System Security Plan\>, written to CSS, and the privacy plan is \<Privacy Plan\>. Table 2 shows where each part is held.

**Table 2: Where each required part of the plans is held**

| Part | CSS requires | Security plan | Privacy plan |
| --- | --- | --- | --- |
| a.1 | Consistent with the enterprise architecture | \<System Security Plan\>, section 4; \<System Description\>, sections 6.6 and 10 | \<Privacy Plan\>, section 8 |
| a.2 | Defines the components of the system | \<System Security Plan\>, sections 3.1 and 3.4; \<System Description\>, section 6.1 | \<Privacy Plan\>, section 2 |
| a.3 | Describes the operational context | \<System Security Plan\>, sections 1 and 2; \<Concept of Operations\> | \<Privacy Plan\>, section 2 |
| a.4 | Names the people in each role | \<System Security Plan\>, section 6; \<Roles and Responsibilities\> | \<Privacy Plan\>, section 3 |
| a.5 | Identifies the types of information | \<System Security Plan\>, section 3.3 | \<Privacy Plan\>, section 4 |
| a.6 | Gives the security categorisation, with its reasons | \<System Security Plan\>, section 3.3 | \<Privacy Plan\>, section 4 |
| a.7 | Describes the threats of concern | \<Risk List\>, section 2 | \<Privacy Plan\>, section 5 |
| a.8 | Gives the results of a privacy risk assessment | \<Data Protection Impact Assessment\> | \<Data Protection Impact Assessment\> |
| a.9 | Describes the environment, and the connections to other systems | \<System Security Plan\>, sections 3.1, 3.2 and 4 | \<Privacy Plan\>, section 2 |
| a.10 | Gives an overview of the requirements | \<System Security Plan\>, sections 1 and 5 | \<Privacy Plan\>, section 6 |
| a.11 | Identifies the baselines and overlays | \<System Security Plan\>, section 5; \<Tailoring Register\> | \<Privacy Plan\>, section 6 |
| a.12 | Describes each control, in place or planned, with the reason for any tailoring | \<System Security Plan\>, section 7: one row for each control; \<Tailoring Register\> | \<Privacy Plan\>, section 6 |
| a.13 | Includes the risk decisions on architecture and design | \<Risk List\>; \<Decision Register\> | \<Privacy Plan\>, section 5; \<Decision Register\> |
| a.14 | Includes the activities that need planning and coordination with defined people | The operating calendar in \<Security Operating Procedures\>, Part C; \<Plan of Action and Milestones\>. They are coordinated with the Head of Cyber, the administrators and \<Organisation\>'s security contact | \<Privacy Plan\>, section 7 |
| a.15 | Reviewed and approved by the authorising official before it is put into effect | Approved by the system owner, with the Head of Cyber's concurrence, and accepted by the authorising official as an accurate record | Approved by the legal adviser and the authorising official |

### 3.4 Approval, review, sharing and protection

Controls met here: PL-2.

**Table 3: How a plan is kept current**

| Step | What happens | Who | Record |
| --- | --- | --- | --- |
| 1 Update | After an assessment, a significant change or a problem found in use, the affected plans are updated | System owner | A line in each plan's change record |
| 2 Check | The plan consistency test is run on the whole document set, and every gap is corrected before the plans are issued. It has 24 checks: for example, that the plan and the assessment agree on the status of every control, and that every section one document cites exists in the other | System owner | The test result, kept with its hash |
| 3 Approve | The security plan goes to the Head of Cyber for concurrence and to the authorising official to accept as an accurate record. The privacy plan is approved by the legal adviser and the authorising official | System owner | \<Decision Register\> |
| 4 Share | When a plan is approved or changed, a link to the restricted copy goes to the Head of Cyber, the administrators and \<Organisation\>'s security contact | System owner | Plan review record, naming the recipients |
| 5 Protect | The plans and the assessment evidence are marked \<Classification\>. They are kept only in the restricted document store, where only named people can read or change them, and never in a code repository. The access list is checked against \<Roles and Responsibilities\> at each review | System owner | Plan review record |
| 6 Review | Every plan in the register is reviewed every 12 months, and after an assessment, a significant change or a problem found in use. The record shows who reviewed it, their role, the date, the outcome and the actions | System owner | Plan review record, kept in the change record (\<Documentation Map\>, section 4.1) |

### 3.5 Rules of behaviour and the register of signatures

Controls met here: PL-4, PL-4(1).

The Security Operating Procedures are the rules of behaviour. Part A applies to everyone, and Part B, the privileged rules, to privileged users as well (\<Security Operating Procedures\>, section 3). The privacy rules are A23 to A29. The rules on social media, public websites and outside sites are these:

- **A43:** \<System Name\> information, items and how the system works are not posted or discussed on social media, forums or any public website.
- **A25:** \<Organisation\>'s information is not posted on public websites.
- **A44:** work credentials are not used to create accounts on outside sites.
- **A45:** the use of outside services and AI tools is limited.

The system owner reviews and updates the rules every 12 months.

1. Before access, the person is given the rules, and signs a declaration that they have read and understood them and agree to follow them, on paper or electronically. The system owner completes TPL-21.
2. The signature is added to the register below. The access request in ServiceNow checks the register before access is given, and the group's owner adds nobody to a group without a signature in it.
3. Everyone signs again every 12 months, and after a material change to the rules: a new or stricter rule, a changed consequence, new monitoring or a new privileged duty. The system owner decides whether a change is material, and records it in the change record of the rules. After a material change everyone signs within 30 days, or loses access.

Signed forms are kept for as long as the person has access, and for 3 years after it ends. The declaration each person signs is: "I have read and understood these rules, and I agree to follow them."

The register starts empty. First signatures are taken on the current version of the rules, before access is given.

**Table 4: Register of signatures**

| TPL-21 record | Name | Role | Parts | SyOps version | Reason | Date signed | Next due |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \[TPL-21 reference\] | \[Name\] | \[Role\] | \[Part A, or Parts A and B\] | \[Version\] | \[First access, yearly or material change\] | \[Date\] | \[Date\] |

### 3.6 Architecture

Controls met here: PL-8.

The security architecture is \<System Description\>, section 6. The protection goals, the design principles, the trust zones and the layers of defence are in \<System Description\>, section 6.8. What is inherited from \<Organisation\>, and where the trust zones meet its network, is in \<System Description\>, sections 6.6 and 10: this is how the architecture fits \<Organisation\>'s enterprise architecture. The assumptions about, and dependencies on, external systems and services are in \<System Description\>, section 6.8. The privacy architecture is in \<Privacy Plan\>, section 8, which covers the same for the processing of personal data. The system owner reviews the architecture against the system itself every 12 months and after a significant change. Each change is carried into the security plan, the privacy plan, the concept of operations, the list of critical components (\<Risk Assessment Management\>, section 3.9), the procedures and any procurement, and each is noted in the review record (PRO-PL-5). New open questions go to \<Decision Register\> or \<Plan of Action and Milestones\>, and not into the architecture.

### 3.7 Baseline and tailoring

Controls met here: PL-10, PL-11.

The baseline is CSS Moderate, with the privacy baseline. It was chosen from the categorisation of \<System Name\>'s information in \<System Security Plan\>, section 3.3, which is Moderate for confidentiality and integrity and Low for availability. A control, or a part of one, is set aside only through \<Tailoring Register\>, with a rationale, a condition that must hold, what happens if the condition changes, and a recorded decision. Each condition is checked at the yearly review (PRO-PL-4). The plan consistency test checks that the applicability table in \<System Security Plan\> agrees with the tailoring register.

### 3.8 What \<Organisation\> provides

Controls met here: PL-2, PL-8.

**Table 5: Asked of \<Organisation\>**

| Provided | Controls | What \<System Name\> relies on | Evidence asked |
| --- | --- | --- | --- |
| Its enterprise architecture standards | PL-2, PL-8 | The standards that \<System Name\>'s plans and architecture must fit | EV-PL-01 |
| Who runs the hypervisor beneath the servers, and whether it is within the Cyber Essentials Plus scope | PL-8 | The answer settles a dependency recorded in the architecture | EV-PL-01 |
| The restricted document store | PL-2 | A SharePoint area where only named people can read or change the plans | Not an evidence request |

### 3.9 Policy and procedures

Controls met here: PL-1.

\<Policy\> (PL) and \<Procedures\> (PL) meet PL-1. Who they are shared with is in \<Policy\>, section PL.6. Their ownership, approval, review and records follow the rules common to every policy in \<Policy\>, section 1.1.
