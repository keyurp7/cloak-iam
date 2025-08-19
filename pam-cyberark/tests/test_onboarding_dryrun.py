def test_dry_run_executes():
    import subprocess
    rc = subprocess.call(["python3", "scripts/cyberark_onboard.py", "--file", "samples/sample_accounts.csv", "--dry-run"])
    assert rc == 0
