import pygame as pygame

import TileLoader
from Vector import Vector


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, solid, image, doorway=None):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.position = Vector(x, y)
        self.solid = solid
        if doorway is None:
            doorway = None
        self.doorway = doorway
        self.image = image
        self.rect = self.image.get_rect()
