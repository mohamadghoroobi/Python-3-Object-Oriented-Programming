stocks = {
    "GOOG": (1.0, 2.0, 3.0),
    "MSFT": (4.0, 5.0, 6.0)
}

random_keys = {}
random_keys["a string"] = "some string"
random_keys[5] = "an integer"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"


class AnObject:
    pass