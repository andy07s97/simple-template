# tests/test_home.py
from app import create_app

def test_home_page():
    app = create_app()
    client = app.test_client()

    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode("utf-8") == "This is Flask app"

