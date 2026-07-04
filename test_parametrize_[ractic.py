import pytest 

@pytest.mark.parametrize("number", [1,2,3])
def test_number_is_int(number):
    assert isinstance(number, int)  

@pytest.mark.parametrize("value", "expected_type",
    [
        ("hello", str),
        (10, int),
        (True, bool),
    ]
)
def test_value_has_correct_type(valye,excpected_type):
    assert isinstance(valye,excpected_type)