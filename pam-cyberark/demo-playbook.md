# CyberArk PAM Playbook

1. Set environment variables for CyberArk PVWA API endpoint and credentials.
2. Run dry-run: `python3 scripts/cyberark_onboard.py --file samples/sample_accounts.csv --dry-run`
3. Run onboarding: `python3 scripts/cyberark_onboard.py --file samples/sample_accounts.csv`
4. Verify accounts created in PVWA UI.
