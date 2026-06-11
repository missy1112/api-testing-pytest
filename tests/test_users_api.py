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

def test_create_new_post():
    new_post = {
        "title": "My first API test",
        "body": "This post was created using an automated API test.",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "My first API test"
    assert data["body"] == "This post was created using an automated API test."
    assert data["userId"] == 1
    assert "id" in data