from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# first requirement: /ping endpoint with get method should respond with 200 status and JSON {"msg": "pong"}
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "pong"}

