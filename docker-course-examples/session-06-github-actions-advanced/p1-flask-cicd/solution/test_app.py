import pytest

from app import add, app, is_positive


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello from CI/CD!"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_positive():
    assert is_positive(1) is True
    assert is_positive(-1) is False
    assert is_positive(0) is False
