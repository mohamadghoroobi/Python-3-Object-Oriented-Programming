from dataclasses import make_dataclass

Stock = make_dataclass("Stock", "symbol", "cur", "high", "low")
stock = Stock("FB", 177, 178, 175)
