import random, string


class StringJoiner(list):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.result = " ".join(self)


with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))

print(joiner.result)


def arguments(x, y='default', *, a, b='only'):
    print(x, y, a, b)


number = 5


def funky_func(number=number):
    print(number)


number = 6
funky_func(8)
funky_func()
print(number)
