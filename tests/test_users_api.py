import requests


def test_get_single_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != ""
    assert data["body"] != ""

def test_get_list_of_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "userId" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]