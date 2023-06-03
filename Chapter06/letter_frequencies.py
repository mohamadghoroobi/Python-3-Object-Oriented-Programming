from collections import defaultdict

def letter_frequency(sentence):
    frequencies = defaultdict
    for letter in sentence:
        # frequency = frequencies.setdefault(letter, 0)
        # frequencies[letter] = frequency + 1
        frequencies[letter] += 1
    return frequencies
