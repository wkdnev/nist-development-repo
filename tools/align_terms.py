"""Term alignment with the System Description (generic Secure by Design reference).
Mechanical first pass only. Every document still needs a reading pass afterwards.
Usage: python3 tools/align_terms.py "<Document>.md" [...]"""
import re, sys

PAIRS = [
    # roles
    ("project access approvers", "Data Owners"), ("Project access approvers", "Data Owners"),
    ("project access approver", "Data Owner"), ("Project access approver", "Data Owner"),
    ("global administrators'", "administrators'"), ("Global administrators'", "Administrators'"),
    ("global administrators", "administrators"), ("Global administrators", "Administrators"),
    ("global administrator", "administrator"), ("Global administrator", "Administrator"),
    # applications
    ("user app ", "UI app "), ("user app,", "UI app,"), ("user app.", "UI app."), ("user app's", "UI app's"),
    ("user application", "UI application"), ("User application", "UI application"),
    ("admin portal", "Admin application"), ("Admin portal", "Admin application"),
    # sign-in
    ("AD FS's", "PingFederate's"), ("AD FS", "PingFederate"),
    ("sent as group claims", "read from Active Directory by the API over LDAPS"),
    ("as group claims", "read from Active Directory by the API over LDAPS"),
    ("group claims", "group memberships read from Active Directory"),
    # database
    ("PostgreSQL 18", "SQL Server 2022"), ("PostgreSQL", "SQL Server"), ("Postgres", "SQL Server"),
    ("Npgsql", "Microsoft.Data.SqlClient"),
    ("TCP 5432", "TCP 1433"),
    ("built-in postgres superuser", "built-in sa login"), ("Built-in postgres superuser", "Built-in sa login"),
    ("superuser", "sysadmin"),
    # groups
    ("DocViewer\\_", "\\<Code\\>\\_"), ("DocViewer_", "\\<Code\\>_"),
    # schemas (the library's separated areas)
    ("projects'", "schemas'"), ("project's", "schema's"), ("Project's", "Schema's"),
    ("projects", "schemas"), ("Projects", "Schemas"), ("project", "schema"), ("Project", "Schema"),
]
# review / approval state: the set is treated as not yet reviewed or approved
REVIEW = [
    (r"\bApproved \((D-[A-Z0-9-]+(?:, D-[A-Z0-9-]+)*)\)", r"Proposed (\1), not yet approved"),
    (r"\bApproved; ", "Not yet approved; "), (r"\bApproved\. ", "Not yet approved. "),
    (r"\bApproved, ", "Not yet approved, "),
]

def run(path):
    s = open(path, encoding="utf-8").read(); o = s
    for a, b in PAIRS:
        s = s.replace(a, b)
    for a, b in REVIEW:
        s = re.sub(a, b, s)
    s = s.replace(" a administrator", " an administrator").replace("A administrator", "An administrator")
    s = s.replace("Administrator and administrator", "Administrator").replace("administrator and administrator", "administrator")
    s = re.sub(r"(Risk decision \| NC-\d+, rated \w+): (approved|accepted)", r"\1: acceptance proposed, not yet decided", s)
    s = re.sub(r"Accepted for 12 months as a (\w+) risk", r"Proposed for acceptance for 12 months as a \1 risk", s)
    s = s.replace("schema schema", "schema").replace("database schema for each schema", "database schema for each schema")
    if s != o:
        open(path, "w", encoding="utf-8").write(s)

for p in sys.argv[1:]:
    run(p)
