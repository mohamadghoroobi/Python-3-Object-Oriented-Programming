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
    def lock(self, item_type):
        """Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers."""
        pass

    def unlock(self, item_type):
        """Release the given type so that other
        customers can access it."""
        pass

    def purchase(self, item_type):
        """If the item is not locked, raise an
        exception. If the item_type does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left."""
        pass


class OutOfStock(Exception):
    pass


class InvalidItemType(Exception):
    pass

# item_type = "widget"
# inv = Inventory()
# inv.lock(item_type)
# try:
#     num_left = inv.purchase(item_type)
# except Invad
