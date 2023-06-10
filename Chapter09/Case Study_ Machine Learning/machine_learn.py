import csv
from random import randint
from collections import Counter

dataset_filename = "colors.csv"


def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i: i + 2], 16) for i in range(1, 6, 2))


def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            label, hex_color = line
            yield (hex_to_rgb(hex_color), label)
