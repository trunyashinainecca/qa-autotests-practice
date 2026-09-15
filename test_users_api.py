import requests
import pytest

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0 
    user = data[0]
    assert isinstance(user, dict)
    assert "id" in user
    assert isinstance(user["id"], int)
    assert "email" in user
    assert isinstance(user["email"], str)
    assert "@" in user["email"]

@pytest.mark.parametrize("field, expected_type",
    [
        ("name", str),
        ("email", str),
        ("phone", str),
        ("id", str)
    ]
)
def test_api(field, expected_type):
    assert isinstance(field, expected_type)


