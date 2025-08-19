#!/usr/bin/env python3
import csv, argparse, os, sys

def dry_run_print(accounts):
    print("Dry-run mode: listing accounts to onboard")
    for acc in accounts:
        print(acc)

def onboard_accounts(accounts):
    print("Onboarding accounts (simulated)")
    # TODO: Replace with real API calls
    for acc in accounts:
        print(f"Onboarded account: {acc['AccountName']} in safe {acc['SafeName']}")

def main():
    parser = argparse.ArgumentParser(description="CyberArk onboarding script (dry-run supported)")
    parser.add_argument('--file', required=True, help='CSV file with accounts')
    parser.add_argument('--dry-run', action='store_true', help='Dry run only, do not onboard')
    args = parser.parse_args()

    with open(args.file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        accounts = list(reader)

    if args.dry_run:
        dry_run_print(accounts)
    else:
        onboard_accounts(accounts)

if __name__ == '__main__':
    main()
