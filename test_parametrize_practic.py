import pytest 

@pytest.mark.parametrize("number", [1,2,3])
def test_number_is_int(number):
    assert isinstance(number, int)  

@pytest.mark.parametrize(
        "value, expected_type",
    [
        ("hello", str),
        (10, int),
        (True, bool)
    ]
)
def test_value_has_correct_type(value, expected_type):
    assert isinstance(value, expected_type)

@pytest.fixture
def names():
    return["Inecca","Ivan","Masha"]

def test_names_not_empty(names):
    assert len(names) > 0
    
def test_all_names_are_string(names):
    for name in names:
        assert isinstance(name, str)

@pytest.fixture()
def product(scope="module"):
    print("product fixture")
    return {
    "name": "phone",
    "price": 500,
    "available": True,
    "rating": 4.8
}


@pytest.mark.parametrize(
        "field, expected_type",
    [
        ("name", str),
        ("price", int),
        ("available", bool),
        ("rating", (float, int))
    ]
)
def test_product_field_type(product, field, expected_type):
    assert field in product
    assert isinstance(product[field],expected_type)

@pytest.fixture()
def order():
    return {
    "id": 101,
    "total": 1500.5,
    "paid": True
}

@pytest.mark.parametrize(
        "field, expected_type",
    [
        ("id", int),
        ("total", float),
        ("paid", bool)
    ]
)
def test_order_field_type(order, field, expected_type):
    assert field in order
    assert isinstance(order[field],expected_type)

#@pytest.fixture(scope="module") означает создать фикстуру один раз для всего текстового файла 
#def user():

#@pytest.fixture(scope="function") фикстура запускается занового для каждого теста
#def user():