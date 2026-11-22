# \<System Name\> Security Assessment Report

## 1 Purpose and scope

This report brings together the results of the assessment of all 19 control families, so that the authorising official can see in one place how far \<System Name\> meets the CSS Moderate baseline, what the remaining risk is, and what must happen before it can be authorised. It is the assessment report in the authorisation package (CSS, tasks A-4 and R-1), and it meets CA-2e and CA-2f. It covers the privacy controls as well, so it is also the privacy assessment report.

This section states what was assessed: the version of \<System Name\>, its components (UI application, Admin application, API and shared library, and the Microsoft SQL Server 2022 database) and the environment it runs in, two Windows Server 2025 VMs at \<Organisation\>. The detail for each family is in its assessment, which takes precedence over this summary. The figures in this report are taken from the assessments, \<Risk List\> and \<Plan of Action and Milestones\>, and are checked against them.

## 2 Executive summary

This section gives the authorising official the overall position in a few lines: whether \<System Name\> is ready to be authorised, and why.

- **Coverage:** \[The baseline entries assessed and the number of determination statements, with the CSS catalogue release used\]
- **Result:** \[Statements satisfied, and controls fully satisfied\]
- **Why the rest are not satisfied:** \[Statements by cause, as in section 4.3\]
- **Risk:** \[Number of risks recorded in \<Risk List\>, and those rated High\]
- **Remediation:** \[Number of items in \<Plan of Action and Milestones\>, by rating and state\]
- **Inherited controls:** \[Entries that depend wholly on \<Organisation\>, and the state of the requests in \<Evidence Requests\>\]

**Recommendation to the authorising official:** \[Recommendation, with reference to the conditions in section 8\]

## 3 Assessment approach

This section records who assessed \<System Name\>, how independent they are, when and how the assessment was carried out, and its limits.

**Table 1: Assessment approach**

| Item | Detail |
| --- | --- |
| Assessor | Level 2: an independent team led by \[Name\], which meets CA-2(1) once each member's TPL-19 is accepted by the authorising official. This report is for the Level 2 assessment; the Level 1 self-assessment by \[Name\], working for the system owner, is its starting point. An authorisation rests only on a Level 2 report |
| Independence | \[How independent each level of assessment is\] |
| Dates | \[When each family was assessed\] |
| Procedures | \[CSS catalogue release; one finding for every determination statement\] |
| Methods | \[Examine, test and interview: what was examined, which tests were run and who was interviewed\] |
| Environment | \[The environment and data the assessment used\] |
| Limits | \[What was not examined, tested or seen in operation\] |
| Plans | \[Where each family's assessment plan is, in \<Control Assessment Record\>\] |

## 4 Results

### 4.1 Results by family

This section gives, for each family, the number of entries, the controls and statements satisfied, and why the other statements are not satisfied.

**Table 2: Results by family**

| Family | Entries | Controls satisfied | Statements satisfied | Awaiting a decision or operation | Gap in the system | Awaiting evidence | Not applicable | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \[Family\] | \[n\] | \[n\] | \[n of n\] | \[n\] | \[n\] | \[n\] | \[n\] | \<Control Assessment Record\>, \[Family\] chapter |
| **Total** | **\[n\]** | **\[n\]** | **\[n of n\]** | **\[n\]** | **\[n\]** | **\[n\]** | **\[n\]** |  |

A control counts as satisfied only when every one of its statements is satisfied or does not apply.

### 4.2 Controls fully satisfied

This section lists, by family, the controls whose every statement is satisfied or does not apply.

**Table 3: Controls fully satisfied**

| Family | Controls |
| --- | --- |
| \[Family\] | \[Controls\] |

### 4.3 Why statements are other than satisfied

This section groups the statements that are other than satisfied by cause, and says what closes each group.

**Table 4: Other than satisfied, by cause**

| Cause | Statements | What closes it |
| --- | --- | --- |
| \[Cause\] | \[n\] | \[What closes it\] |
| **Total** | **\[n\]** |  |

## 5 Risk position

This section lists the risks from \<Risk List\>, highest rating first, with their treatment and status, and gives the number of open non-compliances behind them by rating. The full register, with causes, consequences and decisions, is \<Risk List\>.

**Table 5: Risks**

| Risk | Rating | Treatment | Status |
| --- | --- | --- | --- |
| \[R-XX-nn\] \[Risk\] | \[Rating\] | \[Treatment\] | \[Status\] |

## 6 Weaknesses fixed or closed during the assessment

This section lists the weaknesses that were fixed or closed while the assessment ran, with how each was closed and whether it awaits a repeat test.

**Table 6: Items fixed or closed**

| Item | Rating | Weakness | Outcome |
| --- | --- | --- | --- |
| \[PA-nn\] | \[Rating\] | \[Weakness\] | \[Outcome\] |

## 7 Evidence

This section lists the test scripts run, the checks each covers, and their results. Each script can be run again, and each evidence folder holds a README and a manifest of SHA-256 hashes for its results. A gap in a result is a real weakness, recorded in \<Plan of Action and Milestones\>. It is not a script failure.

**Table 7: Test scripts and results**

| Script | Families | Checks | Number | Passed | Gaps | Latest results |
| --- | --- | --- | --- | --- | --- | --- |
| \[Script\] | \[Families\] | \[Check IDs\] | \[n\] | \[n\] | \[n\] | \[Results file and evidence folder\] |
| **Total** |  |  | **\[n\]** | **\[n\]** | **\[n\]** |  |

## 8 Conditions before authorisation

This section lists the conditions the assessor recommends are met before \<System Name\> is authorised, each linked to the items, risks or evidence that close it.

1. \[Condition\]

## 9 Authorisation package

This report is one part of the authorisation package. The package is listed once, in \<Assessment, Authorization, and Monitoring Management\>, Table 4, and the authorising official records the decision on TPL-18.
