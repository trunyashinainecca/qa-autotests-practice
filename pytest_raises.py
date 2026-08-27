import pytest

def test_error():
    with pytest.raises(ValueError):
        int("hello")
