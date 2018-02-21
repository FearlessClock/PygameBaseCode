from cmath import sqrt

import math

import pygame


class Vector(pygame.math.Vector2):
    """Vector class adding small additions on the bzse class"""
    def __init__(self, x, y):
        """Create the vector pointing to x,y"""
        pygame.math.Vector2.__init__(self, x, y)

    def toArray(self):
        """Return an array with the 2 coords"""
        return [self.x, self.y]

    def toTuple(self):
        """Return a tuple with the 2 coords"""
        return (self.x, self.y)

    def ix(self):
        """Return an int of the X"""
        return int(self.x)

    def iy(self):
        """Return an int of the Y"""
        return int(self.y)