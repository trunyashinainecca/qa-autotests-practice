import pytest
import requests

@pytest.fixture #нужно чтобы вынести общий код в одно место #специальная функция подготовкиа
def users(): # назывние фикстуры.Потом ее будем исполтьзовать users прямо в текте
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200
    return response.json() # фикстур возращает список пользователей

URL = "https://jsonplaceholder.typicode.com/users"

def test_get_users_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users") # отправляем гетзапрос на сервер
    
    assert response.status_code == 200 #проверяем что  код ответил успешно

def test_get_users_response_is_list():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    body = response.json() # преобразуем ответ от сервера в python - данные

    assert isinstance(body, list) #в данном случае сервер возращает список пользователей поэтому проверяем что body - это список

def test_get_users_not_empty():

    response = requests.get("https://jsonplaceholder.typicode.com/users")

    body = response.json()

    assert len(body) > 0 #длина списка больше 0

def test_first_user_has_email():
     
     response = requests.get("https://jsonplaceholder.typicode.com/users")

     body = response.json()
     first_user = body[0]

     assert "email" in first_user

def test_first_user_email_is_string():

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    body = response.json()
    first_user = body[0]

    assert isinstance(first_user["email"], str)

def test_first_user_email_contains_at():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    body = response.json()
    first_user = body[0]

    assert "@" in first_user["email"]

def test_first_user_has_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    body = response.json()
    first_user = body[0]

    assert "name" in first_user

def test_first_user_name_is_string():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    body = response.json()
    first_user = body[0]

    assert isinstance(first_user["name"], str)

def test_first_user_has_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    body = response.json()
    first_user = body[0]

    assert "id" in first_user

def test_first_user_id_is_int():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    body = response.json()
    first_user = body[0]

    assert isinstance(first_user["id"], int)



#с циклами

def test_email_all_users():
    response = requests.get(URL)
    body = response.json()

    for user in body:
        assert "email" in user  #для каждого пользователя из списка body проверь что у него есть ключ email

def test_all_users_have_name():
    response = requests.get(URL)
    body = response.json()

    for user in body: #пройтись по каждому пользователбю из списка(возьми каждого пользователя из боди)
        assert "name" in user

def test_all_users_have_id():
    response = requests.get(URL, timeout=5)
    body = response.json()

    for user in body:
        assert "id" in user

def test_all_email_is_string():
    response = requests.get(URL, timeout=5)
    body = response.json()

    for user in body:
        assert "email" in user #проверить что ключ эмйла есть вообще
        assert isinstance(user["email"], str)
        
def test_all_email_is_contains_at():
    response = requests.get(URL, timeout=5)
    body = response.json()

    for user in body:
        assert "email" in user
        assert "@" in user["email"]

def test_all_users_id_is_int():
    response = requests.get(URL, timeout=5)
    body = response.json()

    for user in body:
        assert "id" in user
        assert isinstance(user["id"], int)

def test_all_users_have_username():
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200

    body = response.json()

    for user in body:
        assert "username" in user

def test_all_users_have_phone():
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200

    body = response.json()

    for user in body:
        assert "phone" in user
        assert isinstance(user["phone"], str)
    
def test_all_users_have_website():
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200

    body = response.json()

    for user in body:
        assert "website" in user
        assert isinstance(user["website"], str)

def test_all_users_have_address_city():
    response = requests.get(URL, timeout=5)
    assert response.status_code == 200

    body = response.json()

    for user in body:
        assert "address" in user
        assert "city" in user["address"]
        assert isinstance(user["address"]["city"], str) # внутри адреса есть город

def test_all_users_have_address_street(users):
    for user in users:
        assert "address" in user
        assert "street" in user["address"]
        assert isinstance(user["address"]["street"], str)


def test_all_users_have_address_geo_lat(users):
    for user in users:
        assert "address" in user
        assert "geo" in user["address"]
        assert "lat" in user["address"]["geo"]
        assert isinstance(user["address"]["geo"]["lat"], str)


def test_all_users_have_address_geo_lng(users):
    for user in users:
        assert "address" in user
        assert "geo" in user["address"]
        assert "lng" in user["address"]["geo"]
        assert isinstance(user["address"]["geo"]["lng"], str)

def test_all_users_have_company_name(users):
    for user in users:
        assert "company" in user
        assert "name" in user["company"]
        assert isinstance(user["company"]["name"], str)


def test_all_users_have_company_catch_phrase(users):
    for user in users:
        assert "company" in user
        assert "catchPhrase" in user["company"]
        assert isinstance(user["company"]["catchPhrase"], str)


def test_all_users_have_company_bs(users):
    for user in users:
        assert "company" in user
        assert "bs" in user["company"]
        assert isinstance(user["company"]["bs"], str)

