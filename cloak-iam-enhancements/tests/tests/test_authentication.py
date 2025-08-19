import pytest
from cloak_iam.auth import authenticate_user, generate_mfa_token, verify_mfa_token

def test_valid_login():
    assert authenticate_user("alice", "correct_password") is True

def test_invalid_login():
    assert authenticate_user("alice", "wrong_password") is False

def test_mfa_flow():
    token = generate_mfa_token("alice")
    assert verify_mfa_token("alice", token) is True
    assert verify_mfa_token("alice", "000000") is False
