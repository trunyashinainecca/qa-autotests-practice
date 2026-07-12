import pytest

def test_practice():
    users = [
    {"name":"inessa","age":17},
    {"name":"ivan","age":25},
    {"name":"Masha","age":20}
    ]
    assert len(users) > 0

    for user in users:
        assert "name" in user
        assert isinstance(user["name"],str)

        assert "age" in user
        assert isinstance(user["age"],int)
        assert user["age"] > 0

