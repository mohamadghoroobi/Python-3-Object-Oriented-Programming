def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"


print(funny_division(0))
print(funny_division(50.0))
print(funny_division("hello"))


def funny_division2(divider):
    try:
        if divider == 13:
            raise ValueError("13 is unlocky number")
        return 100/divider
    except(ZeroDivisionError, TypeError):
        return "Enter a number another than zero."

for val in (0, "hello", 50.0, 13):
    print("Testing {}:".format(val), end=" ")
    print(funny_division2(val))