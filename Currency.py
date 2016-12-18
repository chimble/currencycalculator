#from CurrencyConverter import CurrencyConverter

class Currency():
    def __init__(self, currency_code, amount = 0):
        if amount == 0:
            if currency_code[0] == '$':
                self.currency_code = 'USD'
                self.amount = float(currency_code[1:])
            elif currency_code[0] == '€':
                self.currency_code = 'EUR'
                self.amount = float(currency_code[1:])
            elif currency_code[0] == '£':
                self.currency_code = 'GBP'
                self.amount = float(currency_code[1:])
        else:
            self.currency_code = currency_code
            self.amount = amount

    def __eq__(self, other):
        if self.currency_code == other.currency_code and self.amount == other.amount:
            return True
        return False

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.currency_code, self.amount + other.amount)
        else:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.currency_code, self.amount - other.amount)
        else:
            raise DifferentCurrencyCodeError()

    def __mul__(self, c):
        return Currency(self.currency_code, (self.amount) * c)


class DifferentCurrencyCodeError(Exception):
    pass
