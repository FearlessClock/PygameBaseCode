from cmath import sqrt

import math

import pygame


class Vector(pygame.math.Vector2):
    def __init__(self, x, y):
        pygame.math.Vector2.__init__(self, x, y)

    def toArray(self):
        return [self.x, self.y]

    def toTuple(self):
        return (self.x, self.y)

    def ix(self):
        return int(self.x)

    def iy(self):
        return int(self.y)