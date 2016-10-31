from Currency import Currency

rates = {'USD': 1, 'GBP': 0.82, 'EUR': 0.91}
class CurrencyConverter():

    def __init__(self, rates):
        pass
    def convert(self, currency_code, to):

        if self.currency_code == to:
            return Currency(self.currency_code, self.amount)
        elif self.currency_code != to:
            if self.currency_code == 'GBP':
                if to == 'USD':
                    return Currency(to, self.amount * (rates['GBP']/rates['USD']))
                elif to == 'EUR':
                    return Currency(to, self.amount * (rates['GBP']/rates['EUR']))
            elif self.currency_code == 'EUR':
                if to == 'USD':
                    return Currency(to, self.amount * (rates['USD']/rates['EUR']))
                elif to == 'GBP':
                    return Currency(to, self.amount * (rates['GBP']/rates['EUR']))
            elif self.currency_code == 'USD':
                if to ==  'GBP':
                    return Currency(to, self.amount * (rates['GBP']/rates['USD']))
                elif to == 'EUR':
                    return Currency(to, self.amount * (rates['EUR']/rates['USD']))
        if self.currency_code or to not in rates:
            raise Exception("UnknownCurrencyCodeError")

class UnknownCurrencyCodeError(Exception):
    pass
