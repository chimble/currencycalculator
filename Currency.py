class Currency():
    def __init__(self, currency_code, amount):
        self.currency_code = currency_code
        self.amount = amount
    def __eq__(self, other):
        if self.currency_code == other.currency_code and self.amount == other.amount:
            return True
        return False
