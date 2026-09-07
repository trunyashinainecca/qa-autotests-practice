import pytest

def test_error():
    with pytest.raises(ValueError):
        int("hello")

def test_error():
    with pytest.raises(ValueError):
        int("123")

# ожидали ValueError, получили ValueError → PASSED
# ожидали TypeError, получили ValueError → FAILED

def test_errorzero():
    with pytest.raises(ZeroDivisionError):
        10/0

def check_age(age):
        if age < 18:
             raise ValueError
check_age(16) #создает ошибкау

def test_check_age():
    with pytest.raises(ValueError): #проверяет что ошибка появилась
        check_age(16)

def check_number(number):
     if number < 0:
          raise ValueError
     
def test_check_number():
     with pytest.raises(ValueError):
          check_number(-5)

def check_price(price):
     if price < 0:
          raise ValueError("Price cannot be negative")

def test_check_price():
     with pytest.raises(ValueError,match="Price cannot be negative"):
          check_price(-10)