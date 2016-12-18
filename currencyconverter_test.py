from Currency import Currency, DifferentCurrencyCodeError
from CurrencyConverter import CurrencyConverter, UnknownCurrencyCodeError
from nose.tools import raises


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
    assert a * c == Currency('USD', 40)


def test_single_arg():
    a = Currency('$8')
    b = Currency('USD', 8)
    assert a == b

# create a new currencyconverter object with the rates you'll be using

converter = CurrencyConverter({'USD': 1, 'GBP': 0.82, 'EUR': 0.91})


def test_currency_code_same():
    a = Currency('USD', 8)
    assert converter.convert(a, 'USD') == Currency('USD', 8)


def test_currency_code_dif():
    a = Currency('USD', 2)
    assert converter.convert(a, 'GBP') == Currency('GBP', 1.64)


@raises(UnknownCurrencyCodeError)
def test_unknown_currency():
    a = Currency('USD', 1)
    assert converter.convert(a, 'X') == Currency('X', 1)


@raises(DifferentCurrencyCodeError)
def test_dissimmilar_codes_add():
    a = Currency('EUR', 8)
    b = Currency('USD', 5)
    assert a + b == Currency('USD', 13)
