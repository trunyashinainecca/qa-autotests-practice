import pytest
import requests


URL = "https://jsonplaceholder.typicode.com/comments"

@pytest.fixture
def comments():
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200

    return response.json()


def test_get_comments_response_is_list(comments):
    assert isinstance(comments, list)


def test_get_comments_not_empty(comments):
    assert len(comments) > 0

@pytest.mark.parametrize("field",["postId","id","name","email","body"])
def test_all_comments_have_field(comments, field):
    for comment in comments:
        assert field in comment

@pytest.mark.parametrize(
    "field, expected_type",
     [
        ("postId", int),
        ("id", int),
        ("name", str),
        ("email", str),
        ("body", str)
    ]
)
def test_all_comments_have_field_is_string(comments, field, expected_type):
    for comment in comments:
        assert field in comment
        assert isinstance(comment[field], expected_type)

@pytest.mark.parametrize("field",["id","postId"])
def test_id_and_postid_have_comments_is_positive(comments,field):
    for comment in comments:
        assert field in comment
        assert comment[field] > 0

def test_email_have_sign(comments):
    for comment in comments:
     assert "email" in comment
     assert "@" in comment["email"]

@pytest.mark.parametrize("field",["name","email","body"])
def test_all_text_field_is_not_empty(field, comments):
    for comment in comments:
        assert field in comment
        assert comment[field] != ""