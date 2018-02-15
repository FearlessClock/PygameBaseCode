from cmath import sqrt

import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toArray(self):
        return [self.x, self.y]

    def toTuple(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def magnitude(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude != 0:
            self.x = self.x/magnitude
            self.y = self.y/magnitude

    def __str__(self):
        return "("+str(self.x) + ":" + str(self.y)+")"