from email import header, message

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200


def test_auth_error():
    response = client.post("/token", data={"username": "", "password": ""})
    assert response.status_code == 422
    access_token = response.json().get("access_token")
    assert access_token is None
    message = response.json().get("detail")[0].get("msg")
    assert message == "field required"


def test_auth_success():
    response = client.post("/token", data={"username": "man", "password": "man"})
    assert response.status_code == 201
    access_token = response.json().get("access_token")
    assert access_token
    assert isinstance(access_token, str)


def test_post_article():
    auth = client.post("/token", data={"username": "man", "password": "man"})
    access_token = auth.json().get("access_token")
    assert access_token

    response = client.post(
        "/article/",
        json={
            "title": "Article Title",
            "content": "Test Content",
            "published": True,
            "creator_id": 1,
        },
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 201
    assert response.json().get("title") == "Article Title"


def test_user_create():
    response = client.post(
        "/user/", json={"username": "test", "email": "abcd", "password": "test"}
    )
    assert response.status_code == 201
    assert response.json().get("username") == "test"
