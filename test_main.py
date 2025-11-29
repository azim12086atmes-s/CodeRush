from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()

def test_create_note():
    response = client.post("/notes/", json={"content": "Build the best AI app", "tags": ["hackathon"]})
    assert response.status_code == 200
    assert response.json()["content"] == "Build the best AI app"
