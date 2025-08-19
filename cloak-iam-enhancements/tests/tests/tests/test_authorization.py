import pytest
from cloak_iam.authz import check_access

def test_admin_access():
    assert check_access("alice", "admin_panel") is True

def test_viewer_denied():
    assert check_access("bob", "admin_panel") is False
