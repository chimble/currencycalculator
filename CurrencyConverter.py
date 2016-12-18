from Currency import Currency


class UnknownCurrencyCodeError(Exception):
    pass


class CurrencyConverter():

    def __init__(self, rates):
        self.rates = rates

    def convert(self, currency, to_code):
        try:
            return Currency(to_code, round(currency.amount * (self.rates[to_code]/self.rates[currency.currency_code]), 2))
        except:
            raise UnknownCurrencyCodeError()
