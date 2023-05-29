import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def perimeter(polygon):
    perimeter = 0
    # print([polygon[0]])
    # print(polygon)
    points = polygon + [polygon[0]]
    # print(points)
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i + 1])
    return perimeter


square = [(1, 1), (1, 2), (2, 2), (2, 1)]
perimeter(square)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)
