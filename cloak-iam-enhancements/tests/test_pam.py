from cloak_iam.pam import request_elevation, end_elevation, get_active_session

def test_pam_elevation_flow():
    session = request_elevation("alice")
    assert get_active_session("alice") == session
    end_elevation("alice")
    assert get_active_session("alice") is None
