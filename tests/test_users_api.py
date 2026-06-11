import requests


def test_get_single_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != ""
    assert data["body"] != ""