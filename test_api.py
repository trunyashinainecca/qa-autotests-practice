import requests

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