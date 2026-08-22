import pytest

@pytest.fixture
def user():
    return {"name": "Inessa", "age": 25}

@pytest.fixture
def user_name(user):
    return user["name"]

def test_user_name(user_name):
    assert user_name == "Inessa"

@pytest.fixture
def user_age(user):
    return user["age"]

def test_user_name(user_age):
    assert user_age == 25

@pytest.fixture
def product():
    return {"name": "phone", "price": 500}

@pytest.fixture
def product_price(product):
    return product["price"]

def test_product_price(product_price):
    assert product_price == 500

@pytest.fixture
def is_expensive(product_price):
    return product_price > 300

def test_is_expensive(is_expensive):
    assert is_expensive 

@pytest.fixture
def order():
    return {
        "id": 101,
        "total": 700,
        "status": "paid"
    }
@pytest.fixture
def order_total(order):
    return order["total"]

@pytest.fixture
def is_big_order(order_total):
    return order_total > 1000

def test_is_not_big_order(is_big_order):
    assert not is_big_order

@pytest.fixture
def order_status(order):
     return order["status"]

def test_order_status(order_status):
    assert order_status == "paid"

@pytest.fixture
def is_paid(order_status):
    return order_status == "paid"

def test_is_paid(is_paid):
    assert is_paid

# ошибка до yield в fixture → ERROR
# ошибка в самом тесте → FAILED
# ошибка после yield в teardown → ERROR

@pytest.fixture
def order1():
    print("Cоздаем заказ")
    yield  {"id": 1, "status": "paid"}
    print("Удаляем заказ")

@pytest.fixture
def order1_status(order1):
    return order1["status"]

def test_order1_status(order1_status):
    assert order1_status == "paid"
# ошибка в тесте после yield → teardown выполняется
# ошибка в фикстуре до yield → teardown после yield не выполняется

@pytest.fixture
def user1():
    print("create user")
    yield {"name": "Inessa", "age": 16}
    print("delete user")

@pytest.fixture
def user1_age(user1):
    return user1["age"]

@pytest.fixture
def is_adult(user1_age):
    return user1_age >=18

def test_is_adult(is_adult):
    assert is_adult == False

@pytest.fixture
def product1():
    print("create product")
    yield {"name": "phone", "price": 500}
    print("delete product")

@pytest.fixture
def product1_price(product1):
    return product1["price"]

@pytest.fixture
def is_expensive1(product1_price):
    return product1_price > 1000

def test_is_expensive(is_expensive1):
    assert  not is_expensive1

@pytest.fixture(scope="module")
def order1():
    print("create order")
    yield  {"id": 101, "total": 750, "status": "paid"}
    print("delete order")

@pytest.fixture
def order1_total(order1):
    return order1["total"]

@pytest.fixture
def is_big1_total(order1_total):
    return order1_total > 1000

def test_is_big_total(is_big1_total):
    assert not is_big1_total

def test_order_status(order1):
    assert order1["status"] == "paid"

@pytest.fixture
def api_user():
    print("create user")
    yield {"id": 10, "name": "Inessa", "active": False}
    print("delete user")
 
@pytest.fixture
def user_active(api_user):
    return api_user["active"]

def test_active_user(user_active):
    assert  not user_active