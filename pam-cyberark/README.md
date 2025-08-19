# CyberArk PAM Demo

## Contents
- `scripts/cyberark_onboard.py` — onboarding script for CyberArk PAM (dry-run mode available)
- `samples/sample_accounts.csv` — sample accounts for bulk onboarding
- `tests/` — simple unit test for dry-run mode
- `.github/workflows/ci.yml` — CI workflow to lint and test
- `demo-playbook.md` — instructions

## Setup and Run
1. Configure CyberArk PVWA API endpoint and credentials in environment variables.
2. Run dry-run onboarding script to validate input without changes.
3. Run onboarding script to provision accounts.
