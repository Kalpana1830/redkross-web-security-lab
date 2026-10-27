
from app import app


def test_home_page_returns_success():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"RedKross Web Security Lab" in response.data
