from dataclasses import make_dataclass, dataclass

Stock = make_dataclass("Stock", ["symbol", "cur", "high", "low"])
stock = Stock("FB", 177, high=178, low=175)


class StockRegClass:
    def __init__(self, name, cur, high, low):
        self.name = name
        self.cur = cur
        self.high = high
        self.low = low


stock_reg_class = StockRegClass("FB", 156, 45, 78)


@dataclass
class StockDecorated:
    name: str
    cur = float
    high = float
    low = float
