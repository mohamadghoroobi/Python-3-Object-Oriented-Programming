from collections import defaultdict

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

