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

def test_sub_values_dollars():
    a = Currency('USD', 8)
    b = Currency('USD', 5)
    assert a - b == Currency('USD', 3)

def test_mult_values():
    a = Currency('USD', 8)
    c = 5
    b = a.amount * c
    assert a * c == Currency('USD', 40)
