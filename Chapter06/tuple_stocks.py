from collections import namedtuple

Stock = namedtuple("Stock", ["symblo", "current", "high", "low"])
stock = Stock("FB", 177, high=78, low=175)