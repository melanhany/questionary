from starlette.testclient import TestClient

from questionary.main import app


def test_ping(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
