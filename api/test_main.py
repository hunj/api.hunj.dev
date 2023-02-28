from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert "sha" in response.json()
