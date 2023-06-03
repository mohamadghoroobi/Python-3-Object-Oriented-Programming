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
    cur : float
    high : float
    low : float


@dataclass
class StockDefaults:
    name: str
    cur: float = 0.0
    high: float = 0.0
    low: float = 0.0


@dataclass(order=True)
class StockOrdered:
    name: str
    cur: float = 1.0
    high: float = 2.0
    low: float = 3.0


stock_ordered1 = StockOrdered("FB", 177.46, high=178.67, low=200.79)
stock_ordered2 = StockOrdered("FB")
stock_ordered3 = StockOrdered("FB", 178.42, high=179.28, low=176.39)
