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
    def __init__(self, value):
        self.value = value


my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.value = 12
try:
    random_keys[[1, 2, 3]] = "We can't store lists though"
except:
    print("unable to store list\n")

for key, value in random_keys.items():
    print("{} has value {}".format(key, value))
