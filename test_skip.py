import pytest

@pytest.mark.skip(reason="функционально не готов")
def  test_payment():
    assert 1 == 2

@pytest.mark.skipif(5 ==5, reason="условие сработало")
def test_example():
    assert False

@pytest.mark.xfail #ожидаемо падает я, но если условие выполнилдось то неожиданно прошел
def test_bug():
    assert 1 == 1

def test_pass():
    assert 1 == 1

@pytest.mark.skip()
def test_skip():
    assert 1 == 2

@pytest.mark.xfail(strict=True)# неожиданны  спех - проблема
def test1_bug():
    assert 5 == 5

@pytest.mark.smoke #свои маркер и запускать так  pytest -m smoke
def test_login():
    assert True
    
