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

def test_get_single_post_by_id():
    response = requests.get(f"{URL}/1", timeout=5)

    assert response.status_code == 200

    post = response.json()

    assert "userId" in post
    assert "title" in post
    assert "body" in post

    assert isinstance(post, dict)
    assert post["id"] == 1

    assert isinstance(post["userId"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
    

    
@pytest.mark.parametrize("field",["id","userId"])
def test_all_posts_have_userid_id_positive(posts, field):
    for post in posts:
        assert field in post
        assert post[field] > 0

def test_get_non_existing_post_returns_404():
    response = requests.get(f"{URL}/999999", timeout=5)

    assert response.status_code == 404

    body= response.json()

    assert body == {}


def test_create_posts():
    new_post={
        "userId":1,
        "title":"Test title",
        "body":"Test body"
    }
    response = requests.post(URL,json=new_post, timeout=10) #отправить пост запрос на адрес постс и передай тело запроса в нью пост в формат json
    assert response.status_code == 201

    create_post = response.json()

    assert isinstance(create_post,dict)
    assert create_post["userId"] == new_post["userId"]
    assert create_post["title"] == new_post["title"]
    assert create_post["body"] == new_post["body"]
    assert "id" in create_post
    assert isinstance(create_post["id"], int) # если объект создан то появится его айди

def test_create_post_with_another_data():
    new_post={
        "userId":2,
        "title":"Test love text",
        "body":"Test body love text"
    }
    response = requests.post(URL, json=new_post, timeout=5)

    assert response.status_code == 201

    create_post = response.json()

    assert isinstance(create_post, dict) #так проверяем что среатпост у нас словарь
    assert create_post["userId"] == new_post["userId"]
    assert create_post["title"] == new_post["title"]
    assert create_post["body"] == new_post["body"]
    assert "id" in create_post
    assert isinstance(create_post["id"], int)

def test_update_post():
    updated_post = {
        "userId": 1,
        "id": 1,
        "title": "update title",
        "body": "update body"
        }
    response = requests.put(f"{URL}/1", json=updated_post, timeout=5)

    assert response.status_code == 200

    post = response.json()
    
    assert isinstance(post, dict)
    assert updated_post["userId"] == post["userId"]
    assert updated_post["id"] == post["id"]
    assert updated_post["title"] == post["title"]
    assert updated_post["body"] == post["body"]

def test_patch_post_title():
    patched_data={"title":"Test love r"}
    response = requests.patch(f"{URL}/1", json=patched_data, timeout=5)
    assert response.status_code == 200
    post = response.json()
    assert isinstance(post, dict)
    assert post["title"] == patched_data["title"]

def test_delete_post():
     response = requests.delete(f"{URL}/1", timeout=5) #Отправляем запрос на удаление поста с id = 1
     assert response.status_code == 200
     body = response.json()
     assert body == {}