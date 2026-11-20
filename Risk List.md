# \<System Name\> Risk List

## 1 Purpose

This list records the risks to \<System Name\> and every non-compliance with the controls, across all control families, and how each is treated. It is used by every control family. Section 2 is the risk register. Section 3 records each risk acceptance. Section 4 sets the method: how risks are rated, who may decide, and the treatments. Section 5 is the non-compliance register, with one section per family.

Risks are numbered R-XX-nn and non-compliances NC-XX-nn, where XX is the family code. Each non-compliance names the risk it contributes to, and each risk names the items in \<Plan of Action and Milestones\> that treat it.

## 2 Risk register

The register has one entry for each risk. Likelihood, impact and rating follow section 4.1. Residual is the rating once the treatment is complete.

**Table 1: Risk register**

| ID | Risk | Cause | Consequence | Likelihood | Impact | Rating | Treatment | Residual | Owner | POA&M | Status | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[R-XX-nn\] | \[Risk\] | \[Cause\] | \[Consequence\] | \[Likelihood\] | \[Impact\] | \[Rating\] | \[Treatment\] | \[Residual\] | \[Owner\] | \[PA-nn\] | \[Status\] | \[Date\] |

## 3 Risk acceptance

Each acceptance is recorded here by the person allowed to make it under section 4.2, with the non-compliance, the risk it belongs to, any compensating measure, and the date by which it is reviewed.

**Table 2: Risk acceptance**

| Risk | Decision | Name | Date | Review date |
| --- | --- | --- | --- | --- |
| \[NC-XX-nn\] (\[R-XX-nn\]): \[Non-compliance and compensating measure\] | \[Decision, rating and period\] | \[Name\] | \[Date\] | \[Review date\] |

## 4 Risk method

\<System Name\> is not required to meet every control. The organisation takes a risk-based approach: every non-compliance is identified and documented, its risk is understood, and a named person decides what happens to it. A risk that is acceptable may be accepted with a recorded decision. A risk that is too high requires a remediation plan in \<Plan of Action and Milestones\>. Finding a non-compliance does not by itself start a fix.

This method follows the risk response in CSS (tasks R-2 and R-3). The risk model follows CSS: a threat source exploits a weakness, with a likelihood, to cause an impact.

### 4.1 Rating

Likelihood and impact are each rated Low, Medium or High. Impact considers the confidentiality, integrity and availability of the documents \<System Name\> holds, and the effect on \<Organisation\>.

**Table 3: Risk rating**

| Likelihood | Impact Low | Impact Medium | Impact High |
| --- | --- | --- | --- |
| Low | Low | Low | Medium |
| Medium | Low | Medium | High |
| High | Low | Medium | High |

The matrix weights impact more than likelihood on purpose. A High impact can never rate below Medium, and a Low impact never above Low, because \<System Name\>'s harm is driven by what it holds: one disclosure of HR documents matters more than how often an attempt is made. CSS allows the organisation to set this (Appendix I).

**Table 3a: Likelihood scale**

| Level | Meaning |
| --- | --- |
| High | The threat source is motivated and able, the weakness is known or easy to find, and nothing in place stops it; expected within a year |
| Medium | The threat source is able, but something in place makes success less likely, or the weakness needs inside knowledge; possible within a year |
| Low | Needs rare skill, access or a chain of failures, or a compensating control is in place and tested; unlikely within a year |

**Table 3b: Impact scale**

| Level | Meaning |
| --- | --- |
| High | Severe or serious adverse effect (CSS): disclosure or loss of many documents or of special category data, or \<Organisation\> breaching the law |
| Medium | Serious adverse effect on part of the service: some documents disclosed or changed, or a loss of service beyond the 72-hour recovery time |
| Low | Limited adverse effect: no documents disclosed, and a short loss of service within the recovery time |

**Table 3c: Threat sources considered**

| Source (CSS, Table D-2) | Examples for \<System Name\> |
| --- | --- |
| Adversarial | An outsider exploiting a known flaw; an insider reading another schema's items; a supplier's compromised package |
| Accidental | An administrator deleting or misconfiguring; a user sending an export to the wrong person |
| Structural | A disk, VM or database failure; a software flaw; loss of the key or backup |
| Environmental | Loss of power, cooling or the site, provided by \<Organisation\> |

**Assumptions and uncertainty.**

- Ratings assume \<Organisation\>'s inherited controls work as their Cyber Essentials Plus certificate describes, until the evidence in \<Evidence Requests\> is seen.
- Risks are rated for the target design on its servers.
- Where the evidence is a single test or a document review, not operation over time, the rating is the higher of the two plausible levels.
- Ratings are reviewed every 12 months, and after a significant change, incident or new test result (\<Procedures\>, PRO-RA-1).

**Table 3d: Provisional ratings**

A rating marked provisional was set before the evidence was seen. Each is settled, and the word removed, when the evidence below arrives.

| Non-compliance | Control | Rating | Settled by |
| --- | --- | --- | --- |
| \[NC-XX-nn\] | \[Control\] | \[Rating\], provisional | \[EV-XX-nn\]: \[The evidence that settles it\] |

### 4.2 Who may decide

**Table 4: Decision rules by rating**

| Rating | Default position | Who decides | Conditions of acceptance |
| --- | --- | --- | --- |
| Low | May be accepted | System owner | Recorded in this document; reviewed every 12 months |
| Medium | May be accepted or remediated | Authorising official, on the system owner's advice | A compensating measure where one exists; reviewed every 6 months |
| High | Not acceptable by default; a remediation plan is required | Authorising official | Acceptance only for a stated, limited period while the remediation plan runs |

These thresholds are \<System Name\>'s own, and sit within \<Organisation\>'s risk management strategy and risk appetite (PM-9).

### 4.3 Treatments

**Table 5: Treatments**

| Treatment | Meaning | Where it is recorded |
| --- | --- | --- |
| Accept | The risk is understood and tolerated, and the non-compliance remains | Section 3 of this document, and the control's line in \<System Security Plan\>, section 7 |
| Remediate | The non-compliance is to be fixed, on a plan and not immediately | \<Plan of Action and Milestones\>, with milestones |
| Approve | The mechanism exists or no mechanism is needed, and only a decision or value is outstanding | \<Organisation\>'s corporate parameter values |
| Evidence | The control is expected to be inherited, and \<Organisation\> must supply the evidence | \<Evidence Requests\> and the control's line in \<System Security Plan\>, section 7, then rated when the evidence is seen |
| Tailor | The control or part is proposed as not applicable, with a rationale | \<System Security Plan\>, section 5 |

## 5 Non-compliance register

This register has one entry for each control that is not fully satisfied, by family in CSS order. Each entry names the risk it contributes to in section 2, its proposed treatment from Table 5, and its item in \<Plan of Action and Milestones\> where it is remediated. Cause codes are D (a decision or approval is outstanding), G (a gap in the system) and E (evidence is not yet available from the servers or \<Organisation\>). Ratings marked "provisional" are set when the evidence is seen (Table 3d).

### 5.1 Access Control (AC)

There is one entry for each AC control that is not fully satisfied.

**Table 6: AC non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-AC-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.2 Awareness and Training (AT)

There is one entry for each AT control that is not fully satisfied.

**Table 7: AT non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-AT-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.3 Audit and Accountability (AU)

There is one entry for each AU control that is not fully satisfied.

**Table 8: AU non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-AU-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.4 Assessment, Authorization and Monitoring (CA)

There is one entry for each CA control that is not fully satisfied.

**Table 9: CA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-CA-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.5 Configuration Management (CM)

There is one entry for each CM control that is not fully satisfied.

**Table 10: CM non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-CM-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.6 Contingency Planning (CP)

There is one entry for each CP control that is not fully satisfied.

**Table 11: CP non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-CP-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.7 Identification and Authentication (IA)

There is one entry for each IA control that is not fully satisfied.

**Table 12: IA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-IA-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.8 Incident Response (IR)

There is one entry for each IR control that is not fully satisfied.

**Table 13: IR non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-IR-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.9 Maintenance (MA)

There is one entry for each MA control that is not fully satisfied.

**Table 14: MA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-MA-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.10 Media Protection (MP)

There is one entry for each MP control that is not fully satisfied.

**Table 15: MP non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-MP-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.11 Physical and Environmental Protection (PE)

There is one entry for each PE control that is not fully satisfied.

**Table 16: PE non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-PE-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.12 Planning (PL)

There is one entry for each PL control that is not fully satisfied.

**Table 17: PL non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-PL-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.13 Personnel Security (PS)

There is one entry for each PS control that is not fully satisfied.

**Table 18: PS non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-PS-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.14 Personally Identifiable Information (PT)

There is one entry for each PT control, and each other privacy baseline control, that is not fully satisfied.

**Table 19: PT non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-PT-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.15 Risk Assessment (RA)

There is one entry for each RA control that is not fully satisfied.

**Table 20: RA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-RA-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.16 System and Services Acquisition (SA)

There is one entry for each SA control that is not fully satisfied.

**Table 21: SA non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-SA-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.17 System and Communications Protection (SC)

There is one entry for each SC control that is not fully satisfied.

**Table 22: SC non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-SC-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.18 System and Information Integrity (SI)

There is one entry for each SI control that is not fully satisfied.

**Table 23: SI non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-SI-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |

### 5.19 Supply Chain Risk Management (SR)

There is one entry for each SR control that is not fully satisfied.

**Table 24: SR non-compliance register**

| ID | Control | Non-compliance | Cause | Risk | Rating | Proposed treatment | Reason | POA&M | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[NC-SR-nn\] | \[Control\] | \[Non-compliance\] | \[D, G or E\] | \[R-XX-nn\] | \[Rating\] | \[Treatment\] | \[Reason\] | \[PA-nn\] | \[Decision\] |
