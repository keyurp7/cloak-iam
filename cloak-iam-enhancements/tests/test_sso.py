from cloak_iam.sso import sso_login, validate_token, get_claims

def test_sso_login():
    token = sso_login("alice")
    assert validate_token("alice", token) is True
    claims = get_claims("alice", token)
    assert claims.get("role") == "admin"
