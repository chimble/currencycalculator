class Currency():
    def __init__(self, currency_code, amount):
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
            pass
    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return Currency(self.currency_code, self.amount - other.amount)
        else:
            pass
