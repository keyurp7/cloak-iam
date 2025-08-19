import pytest
from cloak_iam.provisioning import provision_user, deprovision_user, is_active

def test_user_provisioning():
    provision_user("charlie")
    assert is_active("charlie") is True

def test_user_deprovisioning():
    deprovision_user("charlie")
    assert is_active("charlie") is False
