from app import add, app


def test_add():
    assert add(2, 3) == 5


def test_health():
    app.config["TESTING"] = True
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json()["status"] == "ok"
