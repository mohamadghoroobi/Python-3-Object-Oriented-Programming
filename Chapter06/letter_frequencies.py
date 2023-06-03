import string
from collections import defaultdict, Counter


def letter_frequency(sentence):
    frequencies = defaultdict(float)
    for letter in sentence:
        # frequency = frequencies.setdefault(letter, 0)
        # frequencies[letter] = frequency + 1
        frequencies[letter] += 1
    return frequencies


num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)


def counter_letter_frequency(sentence):
    return Counter(sentence)


responses = [
    "vanilla",
    "chocolate",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]
print(
    "The children voted for {} ice cream".format(
        Counter(responses).most_common(1)[0][0]
    )
)


CHARACTERS = list(string.ascii_letters) + [" "]


def list_letter_frequency(sentence):
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1]+1)
    return frequencies

