# \<System Name\> Control Implementation Register

**\<ref\> | Version \<ver\> | The layout introduced in version \<ver\> awaits the system owner's approval; the content of every chapter is unchanged**

**Contents**

[1 Document control](#1-document-control)

[2 How to use this document](#2-how-to-use-this-document)

[AC Access Control](#ac-access-control)

[AT Awareness and Training](#at-awareness-and-training)

[AU Audit and Accountability](#au-audit-and-accountability)

[CA Assessment, Authorization, and Monitoring](#ca-assessment-authorization-and-monitoring)

[IA Identification and Authentication](#ia-identification-and-authentication)

[MA Maintenance](#ma-maintenance)

[MP Media Protection](#mp-media-protection)

[PE Physical and Environmental Protection](#pe-physical-and-environmental-protection)

[PL Planning](#pl-planning)

[PS Personnel Security](#ps-personnel-security)

[PT Personally Identifiable Information Processing and Transparency](#pt-personally-identifiable-information-processing-and-transparency)

[RA Risk Assessment](#ra-risk-assessment)

[SA System and Services Acquisition](#sa-system-and-services-acquisition)

[SC System and Communications Protection](#sc-system-and-communications-protection)

[SI System and Information Integrity](#si-system-and-information-integrity)

| **SECTION 1** |
| --- |

## 1 Document control

### 1.1 Document details

**Table 1: Document details**

| Item | Detail |
| --- | --- |
| Reference | \<ref\> |
| Title | \<System Name\> Control Implementation Register |
| Version | \<ver\> |
| Status | Version \<ver\> has one status, approval and change history for the whole document, as the system owner asked on 12 November 2026 (D-GEN-24), and that layout awaits the system owner's approval. No rule, value, finding or decision changed, so each chapter stands as it was approved (Table 4) |
| Date | 13 November 2026 |
| Owner | System owner |
| Applies to | The 15 control families listed in Table 4 |
| Classification | Restricted |
| Next review | Every 12 months, and after a significant change |
| Format | \<Documentation Map\>, section 5 |

### 1.2 Approval

**Table 2: Approval**

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| System owner | \[Name\] | The layout introduced in version \<ver\> awaits approval. The approval of each chapter's content is in Table 4 | Pending |

### 1.3 Change history

From version \<ver\> the document has one version, one approval and one change history. A change to any chapter raises the document's version, and the row below names the chapter that changed.

**Table 3: Change history**

| Version | Date | Change |
| --- | --- | --- |
| \<ver\> | 18 November 2026 | Kept as an index until the next whole-set review (D-SR-15) |
| \<ver\> | 18 November 2026 | The communications protection chapter now points to \<System and Communications Protection Management\>, which holds that design, the key register, the TLS profile and the allow-lists, as the system owner asked (D-SC-09). No value is changed. The integrity chapter now points to \<System and Information Integrity Management\>, which holds that design, the detection use cases and the integrity baseline, as the system owner asked (D-SI-10). No value is changed. Section 2 says the register now holds no design: every family has its own design document, and each chapter points to it (D-SC-09, D-SI-10). The examples of how to cite a chapter are removed, as no chapter holds content |
| \<ver\> | 18 November 2026 | The acquisition chapter now points to \<System and Services Acquisition Management\>, which holds that design, the development framework, the external services and the developer test plan, as the system owner asked (D-SA-19). The examples of how to cite the register use the SC chapter. No value is changed |
| \<ver\> | 18 November 2026 | The risk assessment chapter now points to \<Risk Assessment Management\>, which holds that design, the vulnerability timetable and the critical components, as the system owner asked (D-RA-11). The examples of how to cite the register use the SA chapter. No value is changed |
| \<ver\> | 18 November 2026 | The personal data chapter now points to \<PII Processing Management\>, which holds that design, the inventory and the retention schedule, as the system owner asked (D-PT-22). No value is changed |
| \<ver\> | 17 November 2026 | The retention schedule gains rows for the personnel security register and leaver and mover records (D-PS-12) |
| \<ver\> | 17 November 2026 | The personnel security chapter now points to \<Personnel Security Management\>, which holds that design, as the system owner asked (D-PS-10). The examples of how to cite the register use the RA chapter. No value is changed |
| \<ver\> | 17 November 2026 | The retention schedule gains a row for the signed rules of behaviour (D-PL-14) |
| \<ver\> | 17 November 2026 | The planning chapter now points to \<Planning Management\>, which holds that design and the two registers, as the system owner asked (D-PL-12). No value is changed |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | The physical and environmental protection chapter now points to \<Physical and Environmental Protection Management\>, which holds that design, as the system owner asked (D-PE-11). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | The retention schedule gains two rows, for maintenance records and media records, each kept for 3 years (D-MP-11); chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | The media protection chapter now points to \<Media Protection Management\>, which holds that design, as the system owner asked (D-MP-09). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | The maintenance chapter now points to \<Maintenance Management\>, which holds that design, as the system owner asked (D-MA-09). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 17 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 16 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 15 November 2026 | The identification and authentication chapter now points to \<Identification and Authentication Management\>, which holds that design, as the system owner asked (D-IA-11). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 15 November 2026 | The retention table gives the backup retention set in \<Contingency Planning Management\>, in place of a placeholder. The register of plans shows that the rebuilt configuration and contingency documents await approval; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 15 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 15 November 2026 | References to the contingency design follow the new section numbers of \<Contingency Planning Management\> (D-CP-14); chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 13 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The assessment, authorisation and monitoring chapter now points to \<Assessment, Authorization, and Monitoring Management\>, which holds that design, as the system owner asked (D-CA-11). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | No document sends the reader to the application's code: source file, class and setting names are replaced by what they stand for, stated in plain words. No value, finding or decision is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The audit chapter now points to \<Audit and Accountability Management\>, which holds the audit design, as the system owner asked (D-AU-10). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The awareness and training chapter now points to \<Awareness and Training Management\>, which holds the training design, as the system owner asked (D-AT-09). No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | Chapter IA follows D-AC-23: sign-in through AD FS with multi-factor authentication, and no passwords held by the system. The parameter values, the assurance levels, the authenticator inventory and the settings table change; the revised acceptance statement awaits the authorising official. Section IA.6 is kept as the record of the tested build. Four controls join the inherited list in section CA.7, as AD FS and Active Directory provide them (D-AC-23); chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | Version numbers are shown as a placeholder, as the system owner asked (D-GEN-28). No other change; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The document number is replaced by a placeholder on the line under the title and in the details table, as the system owner asked (D-GEN-27). No other change; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The name of the system is shown as a placeholder, as the system owner asked (D-GEN-26). No other change; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The access control chapter now points to \<Access Control Management\>, which holds the access control design, as the system owner asked. No value is changed; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | References to documents that no longer exist now name where their content is, as the system owner asked. No other change; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | The earlier rows of the change history are folded into one row, as the system owner decided (D-GEN-25). No other change; chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> | 12 November 2026 | chapter PL: The register of plans in force shows the current version of each plan |
| \<ver\> to \<ver\> | 12 November 2026 | The earlier versions. Their history is kept in the change record (\<Documentation Map\>, section 5.1) |

### 1.4 What each chapter was approved as

Until version \<ver\> each chapter carried its own version, approval and change history. Table 4 records where each stood. The earlier change histories are kept in the change record (\<Documentation Map\>, section 5.1).

**Table 4: Chapters**

| Chapter | Family | Last chapter version | Status at that version |
| --- | --- | --- | --- |
| AC | Access Control | \<ver\> | Version \<ver\> approved by the system owner; version \<ver\> approved on 8 November 2026 (D-AC-17); version \<ver\> makes editorial changes only, issued by the system owner under D-GEN-19 |
| AT | Awareness and Training | \<ver\> | Approved by the system owner |
| AU | Audit and Accountability | \<ver\> | Version \<ver\> approved by the system owner; version \<ver\> approved on 8 November 2026 (D-AU-09) |
| CA | Assessment, Authorization, and Monitoring | \<ver\> | Approved by the system owner; version \<ver\> makes editorial changes only, issued by the system owner under D-GEN-19 |
| IA | Identification and Authentication | \<ver\> | Approved by the system owner (D-IA-10). The acceptance statement in section IA.4 was accepted by the authorising official on 9 November 2026, as confirmed by the system owner (D-IA-08) |
| MA | Maintenance | \<ver\> | Approved by the system owner (D-MA-08) |
| MP | Media Protection | \<ver\> | Approved by the system owner (D-MP-08) |
| PE | Physical and Environmental Protection | \<ver\> | Approved by the system owner (D-PE-10) |
| PL | Planning | \<ver\> | Approved by the system owner |
| PS | Personnel Security | \<ver\> | Version \<ver\> approved by the system owner (D-PS-09) |
| PT | Personally Identifiable Information Processing and Transparency | \<ver\> | Approved by the system owner (D-PT-19); legal placeholders for the legal adviser (D-PT-20) and retention periods for the business owner (D-PT-21) |
| RA | Risk Assessment | \<ver\> | Approved by the system owner (D-RA-09) |
| SA | System and Services Acquisition | \<ver\> | Approved by the system owner (D-SA-18) |
| SC | System and Communications Protection | \<ver\> | Approved by the system owner (D-SC-08) |
| SI | System and Information Integrity | \<ver\> | Approved by the system owner (D-SI-09) |

| **SECTION 2** |
| --- |

## 2 How to use this document

This document was the register of how each control family is implemented in \<System Name\>: the approved decisions, the values of NIST's parameters, the registers and lists the controls call for, and an index from each control to where it is met. Since 18 November 2026 every family's design is held in a document of its own, in the same form, as the system owner asked, and this register holds none of it. Each chapter is kept as a pointer to the document that now holds its family's design, so that the decisions and records that cite a chapter still lead to it. The system owner decided on 18 November 2026 to keep it as an index until the next whole-set review, when it may be retired (D-SR-15). Table 4 records what each chapter was approved as. The rules are in \<Policy\>, the steps people follow are in \<Procedures\>, and \<Documentation Map\>, section 3.2, lists where each family is documented.

- **Chapters.** Each chapter is named by its family code, and says which document now holds its family's design.
- **Versions.** The document has one version. A change to any chapter is a new version of the document.

| **CHAPTER AC** |
| --- |

## AC Access Control

The access control design, settings, parameter values, how the system is built today and the AC control index are held in \<Access Control Management\>. They are not repeated here.

| **CHAPTER AT** |
| --- |

## AT Awareness and Training


The training design is held in \<Awareness and Training Management\>: who needs what, the briefing, the role curriculum, the training matrix, the training register, the measures and the parameter values. It is not repeated here.

| **CHAPTER AU** |
| --- |

## AU Audit and Accountability


The audit design is held in \<Audit and Accountability Management\>: the sources of audit records, the events logged, what a record holds, how records are stored and protected, time, retention, review, alerts and the parameter values. It is not repeated here.

| **CHAPTER CA** |
| --- |

## CA Assessment, Authorization, and Monitoring


The design for assessing, authorising and monitoring \<System Name\> is held in \<Assessment, Authorization, and Monitoring Management\>: assessment, the plan of action, authorisation, the inherited controls, the interface record, the monitoring strategy, significant change and the parameter values. It is not repeated here.

| **CHAPTER IA** |
| --- |

## IA Identification and Authentication


The identification and authentication design is held in \<Identification and Authentication Management\>: who is identified and how, sign-in through AD FS, the assurance levels, the authenticator inventory, the settings against NIST SP 800-63B, and the parameter values. It is not repeated here.

| **CHAPTER MA** |
| --- |

## MA Maintenance


The maintenance design is held in \<Maintenance Management\>: who maintains what, how a job is controlled, the remote maintenance routes, the approved tools and people, the security-critical components, and the parameter values. It is not repeated here.

| **CHAPTER MP** |
| --- |

## MP Media Protection


The media protection design is held in \<Media Protection Management\>: the media inventory, the marking scheme, storage and transport, the sanitising methods, portable storage, and the parameter values. It is not repeated here.

| **CHAPTER PE** |
| --- |

## PE Physical and Environmental Protection


The physical and environmental protection design is held in \<Physical and Environmental Protection Management\>: the sites, the inheritance matrix, how \<Organisation\>'s evidence is checked, the rules for offices and home working, and the parameter values. It is not repeated here.

| **CHAPTER PL** |
| --- |

## PL Planning


The planning design is held in \<Planning Management\>: the register of plans in force, what the plans hold, how they are approved, shared, reviewed and protected, the register of signatures, and the parameter values. It is not repeated here.

| **CHAPTER PS** |
| --- |

## PS Personnel Security


The personnel security design is held in \<Personnel Security Management\>: the risk designation of every role, the screening standard, the access agreements, joiners, movers and leavers, the time limits, the personnel security register, and the parameter values. It is not repeated here.

| **CHAPTER PT** |
| --- |

## PT Personally Identifiable Information Processing and Transparency


The personal data design is held in \<PII Processing Management\>: the authority, purposes and lawful basis, the personal data inventory, special category data, the privacy notice, people's rights, minimisation and the retention schedule, and the parameter values. It is not repeated here.

| **CHAPTER RA** |
| --- |

## RA Risk Assessment


The risk assessment design is held in \<Risk Assessment Management\>: the vulnerability timetable, the critical components, the first supply chain review, how vulnerability monitoring stands today, and the parameter values. It is not repeated here.

| **CHAPTER SA** |
| --- |

## SA System and Services Acquisition


The acquisition design is held in \<System and Services Acquisition Management\>: the development framework, the external services, the developer test plan, the tools and their configuration, how \<System Name\> is built today, and the parameter values. It is not repeated here.

| **CHAPTER SC** |
| --- |

## SC System and Communications Protection


The communications protection design is held in \<System and Communications Protection Management\>: the cryptographic and key register, the TLS profile, the host firewall allow-lists, the page policy, how protection stands today, and the parameter values. It is not repeated here.

| **CHAPTER SI** |
| --- |

## SI System and Information Integrity


The integrity design is held in \<System and Information Integrity Management\>: the upload checks, the advisory sources, the detection use cases, the integrity baseline, the retention periods, how integrity stands today, and the parameter values. It is not repeated here.

