# Dummy Dependency Analyzer Test Repository

This is a **harmless test fixture** for a repository dependency/security analyzer.
It intentionally pins old third-party package versions so a scanner can test
version detection, vulnerability matching, dependency extraction, and remediation
recommendations. It contains no exploit code.

## Test cases

- `requirements.txt`: intentionally outdated Python dependencies.
- `app.py`: tiny demo application; it does not exercise vulnerable behavior.
- `dependency-notes.md`: expected checks and interpretation notes.

## Run a dependency scan

Upload this repository ZIP to your analyzer, or point the analyzer at the extracted
folder.

If you want to inspect dependency metadata locally, use a disposable virtual
environment. Do not install these old dependencies into a production environment.

## Important

A package being old does not automatically mean it is vulnerable or deprecated.
The scanner should match exact package names and versions against a vulnerability
database/advisory source, and distinguish confirmed vulnerabilities from
maintenance/deprecation warnings.
