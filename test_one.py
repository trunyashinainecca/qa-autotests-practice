def test_sum():
    assert 2 + 2 == 4 # == сравнить, assert проверить

def test_text():
    text = "hello" #положить
    assert text == "hello" 

def test_users_count_list():
    users = ["ivan","inessa","ilya"]
    assert len(users) == 3 # len() количество элементов 

def test_age():
    age = 25
    assert age >= 18

def test_name():
    name = "Inessa"
    assert name == "Inessa"    

def test_text_contains():
    text = "I am learning autotests"
    assert "autotests" in text # проверь что слова находится в переменной text

def test_text_contains_at():
    email = "test@in.com"
    assert "@" in email

def test_users_in_list():
    users = ["INNA","IVAN","MASHA"]
    assert "IVAN" in users

def test_users_count():
    users = ["INNA","IVAN","MASHA"]
    assert len(users) == 3

def test_user_name():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
    assert user["name"] == "Inessa"
     # user["name"] - возьми из словаря user значение по ключу name
    

def test_user_email():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
    assert user["email"] == "test@in.com"

#actual and expentend

#expected_name = "Inessa" - что ожидвем
#actual_name = user["name"] - что получили реально
#assert actual_name == expected_name - сравниваем

def test_user_name_actual_expentend():
     user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
     
     expected_name = "Inessa"
     actual_name = user["name"]
    
     assert actual_name == expected_name

def test_user_email_actual_expected():
     user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
     
     expected_email = "test@in.com"
     actual_email = user["email"]
    
     assert actual_email == expected_email

def test_user_age_actual_expected():
     user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
     
     expected_age = 25
     actual_age = user["age"]
    
     assert actual_age == expected_age

def test_user_has_email_key():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
    assert "email" in user # проверяем что в соержится ключ email в словаре user

def test_user_has_name_key():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
    assert "name" in user

def test_user_has_age_key():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
    assert "age" in user

def test_user_name_is_strining():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
    assert  isinstance(user["name"], str) # проверь что name является строкой

def test_user_age_is_int():
     user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
     assert  isinstance(user["age"], int) # проверь что age является числом

def test_user_email_is_string():
     user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }
     assert  isinstance(user["email"], str)


def test_user_email_contains_at():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }

    assert "@" in user["email"] 

def test_user_age_is_adult():
    user ={
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
    }

    assert user["age"] >= 18 

def test_users_email_contains_at():
    users = [
        {
        "name": "Inessa",
        "age": 25,
        "email": "test@in.com"
        },
        {
        "name": "Ivan",
        "age": 30,
        "email": "ivan@test.com"
        }
    ]

    first_user = users[0] #возьми первого пользователя из списка
    second_user = users[1]

    assert "@" in first_user["email"]
    assert "@" in second_user["email"]