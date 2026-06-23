from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_recommendations():

    response = client.post(
        "/recommendations/"
    )

    assert response.status_code == 200