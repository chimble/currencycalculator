from Currency import Currency


def test_equals_eight_dollars():
    a = Currency('USD', 8)
    b = Currency('USD', 8)
    assert a == b
