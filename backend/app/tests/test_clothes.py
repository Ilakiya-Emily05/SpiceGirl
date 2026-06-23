from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_clothes():

    response = client.get(
        "/clothes/"
    )

    assert response.status_code == 200