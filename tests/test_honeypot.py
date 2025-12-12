import json
from server.honeypot import app

def test_login_attempt():
    client = app.test_client()

    response = client.post(
        "/login",
        data=json.dumps({"username": "admin", "password": "1234"}),
        content_type="application/json"
    )

    assert response.status_code == 401

def test_admin_probe():
    client = app.test_client()
    response = client.get("/admin")

    assert response.status_code == 403
