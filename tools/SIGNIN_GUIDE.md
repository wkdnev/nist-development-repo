# Sign-in and sessions: aligning the text

The reference wording is in `Access Control Management.md`, section 1 (fourth paragraph), section 3.1 items 7 and 8, and sections 3.14 and 3.15. Read those first and match them.

## The facts

- **Sign-in is PingFederate.** \<Organisation\>'s PingFederate authenticates every user with multi-factor authentication, by OpenID Connect, and gives \<System Name\> a signed response that names the person. It carries no groups. The API reads the person's group membership from Active Directory over LDAPS (flow F7). \<System Name\> holds no accounts or passwords. There is no AD FS anywhere: every mention of AD FS, ADFS or Active Directory Federation Services becomes PingFederate, and the sentence is fixed so it stays true (no SAML, no claims or groups in the token, no relying party trust: say "PingFederate connection" or "OpenID Connect client" where needed).
- **No session management.** \<System Name\> has no sessions, session records, session store, idle timeout, idle sign-out, absolute timeout, session limit, concurrent session limit, page lock, sign-out or "end session" function. Do not present any of these as something \<System Name\> has, plans or should build.
- **What does that job instead.** How long a sign-in lasts is set by PingFederate's sign-in lifetime (P-AC-10). The app holds the sign-in only in its authentication cookie, no longer than PingFederate's lifetime. An unattended screen is locked by the operating system on \<Organisation\>'s managed devices and the servers (P-AC-15). Ending a person's access is done by disabling the AD account or removing group membership, and ending their PingFederate sign-in.
- **Other uses of "session" are fine** where they are not the application's: a training session, a VPN session, a remote maintenance or supplier support session, a PingFederate sign-in. Prefer "sign-in" for the user's signed-in state.

## Records of tests and findings

The Control Assessment Record, Security Assessment Report, Plan of Action and Milestones, Risk List and Decision Register record what was found or decided. Keep every result, rating, status, ID and determination as it is. Change the wording so it names PingFederate and does not present session management as a capability of \<System Name\>. Where a finding, risk, plan item or decision exists only because of a session feature (for example a fix to an idle timeout value), do not delete it and do not change its result: list it in your report so it can be put to the system owner.

## Rules

- Edit only the files you are given. Other people are editing other files at the same time. No git commands.
- Plain British English, no em dashes, no NIST (write CSS), no new dates or approvals.
- Keep section and table numbering unchanged.
- Report: per file, how many changes; and the list of findings, risks, plan items or decisions that exist only because of a session feature.
