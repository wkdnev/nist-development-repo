# Secure by Design assessment document set

A generic, unapproved set of 42 documents for designing, running and assessing an internal application against the CSS (NIST-based) Moderate baseline, with the privacy baseline. Placeholders in angle brackets, such as \<System Name\> and \<Organisation\>, are replaced for each application.

Start with [Guide to the Document Set](Guide%20to%20the%20Document%20Set.md). [Documentation Map](Documentation%20Map.md) is the index, and [System Description](System%20Description.md) describes the reference system in one place.

`tools/Test-PlanConsistency.py` is the automatic check on the set ([Documentation Map](Documentation%20Map.md), section 4.11). Run `python tools/Test-PlanConsistency.py` from this folder: it makes 24 checks, L1 to L24, on the totals, identifiers, links and references across the documents, and changes nothing. `--census` counts the facts still to be supplied, by who supplies them.
