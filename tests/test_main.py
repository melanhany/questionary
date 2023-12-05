from starlette.testclient import TestClient

from questionary.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
