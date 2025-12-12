from server.honeypot import app

def test_wordpress_probe():
    client = app.test_client()

    response = client.post(
        "/wp-login.php",
        headers={"User-Agent": "curl/7.88.1"}
    )

    assert response.status_code == 404
