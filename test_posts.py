import pytest
import requests


URL = "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture
def posts():
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200

    return response.json()


def test_get_posts_response_is_list(posts):
    assert isinstance(posts, list)


def test_get_posts_not_empty(posts):
    assert len(posts) > 0
# проверяем что у каждого поста должны быть поля
@pytest.mark.parametrize("field",["userId","id","title","body"])
def test_all_posts_have_field(posts,field):
    for post in posts:
        assert field in post

@pytest.mark.parametrize(
        "field, excepted_type",
  [
    ("userId", int),
    ("id", int),
    ("title", str),
    ("body", str)
  ]
)
def test_all_posts_have_field_is_strining(posts, field,excepted_type):
    #возьми каждый пост из списка posts по очереди
#и временно называй его post
    for post in posts:
        assert field in post
        assert isinstance(post[field], excepted_type) # isinstance использовать для проверки типа

def test_all_posts_have_id_not_empty(posts):
    for post in posts:
        assert post["body"] != ""
        assert post["title"] != ""


@pytest.mark.parametrize("field",["id","userId"])
def test_all_posts_have_userid_id_positive(posts, field):
    for post in posts:
        assert field in post
        assert post[field] > 0