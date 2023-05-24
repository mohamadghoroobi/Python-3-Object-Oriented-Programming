class InvalidWithdrawl(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


raise InvalidWithdrawl(25, 50)
