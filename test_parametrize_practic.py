import pytest 

@pytest.mark.parametrize("number", [1,2,3])
def test_number_is_int(number):
    assert isinstance(number, int)  

@pytest.mark.parametrize(
        "value, expected_type",
    [
        ("hello", str),
        (10, int),
        (True, bool),
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