# Redrawing a figure

Each figure is an SVG in `figures/src/<name>.html`, rendered to `figures/<name>.png` with `node tools/render_figures.js <name>`. `figures/src/sd-figure-1.html` is the house style: copy its fonts, colours, box shapes, arrow marker and title/subtitle layout.

## Style

- Canvas 1520 px wide, height to fit. White background. Title 30 px bold `#1a1a1a` at (48, 55); subtitle 21 px `#555` at (48, 92).
- Boxes: `rx` 12, white fill, `#999` stroke 2 px. Highlight with `#2f6fd6` stroke 3 px (and `#d9e1ec` fill if needed); a good/end state with `#2e9e44`. Grouping areas `#efeeeb`. Dashed stroke (`8 6`) means planned, inherited or outside the system.
- Box heading 24 to 26 px bold; body 19 to 21 px `#555`. Arrows `#999`, 2.5 px, marker `url(#a)`.
- Text must fit inside its box with at least 24 px padding. No overlaps. Plain English, no em dashes.
- After rendering, open the PNG and check it.

## Content rules

The figure must match the document's current text and the reference system in `tools/ALIGNMENT_GUIDE.md` section 2. Read the section around the figure before drawing. In particular:

- No mention of NIST or any NIST publication (SP 800-xx, FIPS, SSDF). Write **CSS** (Cyber Security Standards) instead.
- No "ABC Technologies", "ABC UK" or any real organisation name: use `<Organisation>`. No "DocuView" or "DocViewer": use `<System Name>`. Group and service names such as `DV_API` or `DocViewer_Admins` become `<Code>_...` or a plain description.
- Sign-in is **PingFederate** by OpenID Connect with MFA, never AD FS. The signed response names the person and carries no groups: the **API reads group membership from Active Directory over LDAPS** (flow F7).
- **No session management**: no sessions, idle lock, timeout, session limit or sign-out in the application. Sign-in lifetime comes from PingFederate and screen lock from the device.
- Database is **SQL Server 2022** with Windows authentication, never PostgreSQL. Only the API reaches it.
- Separated areas are **schemas**, never projects. Each schema's groups are owned by its **Data Owner**. Roles: Reader, Editor, Administrator, Auditor, Security officer. There is no global administrator.
- Access approval is a **ServiceNow** workflow, never Jira. Builds follow the organisation's corporate SDLC.
- Flows F1 to F9 as in the System Description, section 6.
- No dates, approvals, "approved by", "reviewed on" or version numbers.

If the document's text itself still contradicts these rules near the figure, fix the figure to the rules, and fix the figure's alt text and the one sentence that introduces or describes it. Change nothing else in the documents.
