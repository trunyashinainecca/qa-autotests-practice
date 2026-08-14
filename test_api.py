import pytest

def check_field(user, field, expected_type):
    assert field in user
    assert isinstance(user[field], expected_type)


@pytest.mark.parametrize(
    "field, expected_type",
    [
        ("name", str),
        ("email", str),
        ("phone", str),
        ("website", str),
    ]
)
def test_all_users_have_field(users, field, expected_type):
    for user in users:
        check_field(user, field, expected_type)












# parametrize запускает один и тот же тест несколько раз,
# каждый раз подставляя новое значение в переменную field
# field приходит из parametrize
@pytest.mark.parametrize("field", ["name", "email", "phone", "website"])
def test_all_users_have_field(users, field):
    for user in users:
        assert field in user

# parametrize может передавать сразу два значения:
# field — название поля, expected_type — ожидаемый тип данных
# field и expected_type приходят из parametriz
@pytest.mark.parametrize(
    "field, expected_type",
    [
        ("name", str),
        ("email", str),
        ("phone", str),
        ("website", str),
        ("id", int)
    ]
)
def test_all_users_field_has_correct_type(users, field, expected_type):
    for user in users:
        assert field in user
        assert isinstance(user[field], expected_type)


# Параметризуем company: проверяем, что внутри company есть нужные поля
@pytest.mark.parametrize("field", ["bs", "catchPhrase", "name"])
def test_all_users_company_has_field(users, field):
    for user in users:
        assert "company" in user
        assert field in user["company"]


# Проверяем, что поля внутри company являются строками
@pytest.mark.parametrize("field", ["bs", "catchPhrase", "name"])
def test_all_users_company_field_is_string(users, field):
    for user in users:
        assert "company" in user
        assert field in user["company"]
        assert isinstance(user["company"][field], str)

#1. @pytest.mark.parametrize всегда должен стоять прямо над тем тестом, к которому относится.

#2. Если в тесте есть field, он должен приходить из parametrize.

#3. Если в тесте есть users, он приходит из fixture.

#4. "field" и field — это разные вещи.
   #"field" — просто текст.
   #field — переменная.

@pytest.mark.parametrize("field",["city","street"])
def test_all_address_has_field_is_string(users, field):
    for user in users:
        assert "address" in user 
        assert field in user["address"]
        assert isinstance(user["address"][field], str)
# Проверяем координаты пользователя.
# Внутри address должен быть объект geo.
# Внутри geo должны быть поля lat и lng.
# Оба значения должны быть строками.
# parametrize нужен, чтобы одним тестом проверить и lat, и lng.
@pytest.mark.parametrize("field",["lat","lng"])
def test_all_address_has_field_is_string_and_lat_lng(users, field):
    for user in users:
        assert "address" in user
        assert "geo" in user["address"]
        assert field in user["address"]["geo"]
        assert isinstance(user["address"]["geo"][field], str)


def test_get_users_response_is_list(users):
    assert isinstance(users, list) #в данном случае сервер возращает список пользователей поэтому проверяем что body - это список

def test_get_users_not_empty(users):
    assert len(users) > 0 #длина списка больше 0


#с циклами
        
def test_all_email_is_contains_at(users):
    for user in users:
        assert "email" in user
        assert "@" in user["email"]


def test_all_users_have_username(users):
    for user in users:
        assert "username" in user 



@pytest.mark.parametrize(
    "field, expected_type",
     [
     ("name", str),
     ("email", str), 
     ("id", int)
     ]
    )
def test_users_field_type(users, field, expected_type):
    for user in users:
        assert field in user
        assert isinstance(user[field], expected_type)
    




