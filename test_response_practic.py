import pytest

def test_user_data():
    data = { "id": 15, "nam": "Inessa", "email": "inessa@test.ru", "age": 25, "active": True, "rating": 4.7}
    assert "id" in  data 
    assert isinstance(data["id"],int)
    assert data["id"] > 0

    assert "nam" in data 
    assert isinstance(data["nam"], str)
    assert len(data["nam"]) > 0

    assert "email" in data 
    assert isinstance(data["email"], str)
    assert len(data["email"]) > 0
    assert "@" in data["email"]