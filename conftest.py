import pytest
import requests

URL = "https://jsonplaceholder.typicode.com/users"

@pytest.fixture #нужно чтобы вынести общий код в одно место #специальная функция подготовкиа
def users(): # назывние фикстуры.Потом ее будем исполтьзовать users прямо в текте
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200
    return response.json() # фикстур возращает список пользователей

@pytest.fixture # декоратор
def prosucts():
    return [
    {"name": "phone", "price": 500},
    {"name": "book", "price": 20}
 ]

def test_products(prosucts):
    assert len(prosucts) > 0

def get_status(status):
    return status
   

def test_status():
    status = get_status("OK")
    assert status == "OK"

@pytest.fixture
def user():
    return {"name": "Inessa", "age": 25}


def get_user_name(user):
    return user["name"]


def test_user_name(user):
    name = get_user_name(user)
    assert name == "Inessa"

def test_user_age(user):
    assert isinstance(user["age"], int)
    assert user["age"] > 0



