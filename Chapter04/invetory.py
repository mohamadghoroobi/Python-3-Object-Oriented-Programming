class InvalidWithdrawl(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


# try:
#     raise InvalidWithdrawl(25, 50)
# except InvalidWithdrawl as e:
#     print(f"""I'm sorry, but your withdrawal is
#           more than your balance by
#           ${e.overage()}""")


class Inventory:
    pass