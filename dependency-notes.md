# Dependency scan notes

## What the analyzer should do

1. Detect `requirements.txt` as a Python dependency manifest.
2. Parse each direct dependency and its pinned version.
3. Resolve or retrieve package metadata if the product supports transitive dependency trees.
4. Check each package/version against its configured advisory source (for example, OSV or
   the Python package ecosystem's published advisories).
5. Show evidence for every finding: advisory/CVE ID, affected version range, severity,
   source, and a fixed version where one is published.
6. Separate confirmed security findings from generic "old version" or deprecated-package
   warnings. Do not mark every old version as vulnerable without evidence.

## Expected fixture characteristics

- Several intentionally old pinned versions are present.
- The manifest contains multiple direct dependencies.
- The app imports Flask, providing a simple manifest-to-source consistency check.
- Transitive dependencies (for example, dependencies required by Flask or requests)
  can only be shown if the analyzer resolves package metadata; they are not explicitly
  listed as direct requirements here.

## Caution

This fixture is designed to test detection, not to assert that every listed package
has a currently applicable vulnerability. Advisory databases and affected-version
ranges change over time. Use the analyzer's source of truth to determine exact findings.
