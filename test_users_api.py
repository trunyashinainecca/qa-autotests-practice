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
        ("id", int)
    ]
)

def test_get_request(field, expected_type):
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    assert response.status_code == 200
    test = response.json()
    for user in test:
        assert field in user
        assert isinstance(user[field], expected_type)

def test_get_user_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1",timeout=5)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "email" in user
    assert "@" in user["email"]
    assert "name" in user

def test_get_nonexistent_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999",timeout=5)
    assert response.status_code == 404
    data = response.json()
    assert data == {}

@pytest.mark.parametrize("user_id",[1,5,10])
def test_get_users_by_id(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}",timeout=5)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id

def test_get_user_by_username():
    params = {"username":"Bret"}
    response = requests.get(f"https://jsonplaceholder.typicode.com/users",params=params, timeout=5)
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    assert users[0]["username"] == "Bret"

@pytest.mark.parametrize("username",["Bret", "Anton","Vasia"])
def test_get_user_bay_username(username):
    params = username
    response = requests.get(f"https://jsonplaceholder.typicode.com/users",params=params, timeout=5)
    assert response.status_code == 200

