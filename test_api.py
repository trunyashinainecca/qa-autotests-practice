import pytest

# parametrize запускает один и тот же тест несколько раз,
# каждый раз подставляя новое значение в переменную field
@pytest.mark.parametrize("field", ["name", "email", "phone", "website"])
def test_all_users_have_field(users, field):
    for user in users:
        assert field in user

# parametrize может передавать сразу два значения:
# field — название поля, expected_type — ожидаемый тип данных
@pytest.mark.parametrize(
    "field, expected_type",
    [
        ("name", str),
        ("email", str),
        ("phone", str),
        ("website", str),
        ("id", int),
    ]
)
def test_all_users_field_has_correct_type(users, field, expected_type):
    for user in users:
        assert field in user
        assert isinstance(user[field], expected_type)

def test_get_users_response_is_list(users):
    assert isinstance(users, list) #в данном случае сервер возращает список пользователей поэтому проверяем что body - это список

def test_get_users_not_empty(users):
    assert len(users) > 0 #длина списка больше 0

def test_first_user_has_email(users):
     first_user = users[0]

     assert "email" in first_user

def test_first_user_email_is_string(users):
    first_user = users[0]

    assert isinstance(first_user["email"], str)

def test_first_user_email_contains_at(users):
    first_user = users[0]

    assert "@" in first_user["email"]

def test_first_user_has_name(users):
    first_user = users[0]

    assert "name" in first_user

def test_first_user_name_is_string(users):
    first_user = users[0]

    assert isinstance(first_user["name"], str)

def test_first_user_has_id(users):
    first_user = users[0]

    assert "id" in first_user

def test_first_user_id_is_int(users):
    first_user = users[0]

    assert isinstance(first_user["id"], int)



#с циклами

def test_email_all_users(users):

    for user in users:
        assert "email" in user  #для каждого пользователя из списка body проверь что у него есть ключ email

def test_all_users_have_name(users):
    for user in users: #пройтись по каждому пользователбю из списка(возьми каждого пользователя из боди)
        assert "name" in user

def test_all_users_have_id(users):
    for user in users:
        assert "id" in user

def test_all_email_is_string(users):
    for user in users:
        assert "email" in user #проверить что ключ эмйла есть вообще
        assert isinstance(user["email"], str)
        
def test_all_email_is_contains_at(users):
    for user in users:
        assert "email" in user
        assert "@" in user["email"]

def test_all_users_id_is_int(users):
    for user in users:
        assert "id" in user
        assert isinstance(user["id"], int)

def test_all_users_have_username(users):
    for user in users:
        assert "username" in user

def test_all_users_have_phone(users):
    for user in users:
        assert "phone" in user
        assert isinstance(user["phone"], str)
    
def test_all_users_have_website(users):
    for user in users:
        assert "website" in user
        assert isinstance(user["website"], str)

def test_all_users_have_address_city(users):
    for user in users:
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

