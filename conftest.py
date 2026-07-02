import pytest
import requests

URL = "https://jsonplaceholder.typicode.com/users"

@pytest.fixture #нужно чтобы вынести общий код в одно место #специальная функция подготовкиа
def users(): # назывние фикстуры.Потом ее будем исполтьзовать users прямо в текте
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200
    return response.json() # фикстур возращает список пользователей

