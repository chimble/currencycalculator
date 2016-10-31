from Currency import Currency


def test_equals_eight_dollars():
    a = Currency('USD', 8)
    b = Currency('USD', 8)
    assert a == b

def test_not_equals_amount():
    a = Currency('USD', 8)
    b = Currency('USD', 5)
    assert a != b

def test_not_equals_currency():
    a = Currency('USD', 8)
    b = Currency('EUR', 8)
    assert a != b

def test_add_values_dollars():
    a = Currency('USD', 8)
    b = Currency('USD', 5)
    assert a + b == Currency('USD', 13)
