def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequncy = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequncy + 1
    return frequencies
