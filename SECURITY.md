# Security Policy

## Supported Versions

- Main branch: actively maintained with security updates
- Releases: security fixes will be backported to the two most recent minor versions when feasible

## Reporting a Vulnerability

Please report suspected vulnerabilities to security@cloak-iam.com. Include:
- Affected component(s) and version/commit
- Reproduction steps or PoC
- Impact assessment and suggested mitigation (if any)

We will acknowledge within 72 hours and provide regular status updates until resolution.

## Secure Development Practices

- All changes go through CI (lint, type-check, tests)
- Secrets never committed; use environment variables and secret managers
- Dependencies pinned; update via PR with security review
- Containers run as non-root; minimal base images
- SBOM and provenance can be added in release pipelines
