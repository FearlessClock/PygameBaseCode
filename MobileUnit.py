import pygame

from Vector import Vector

class MobileUnit:
    """The base class for the interacting candidates"""

    def __init__(self, x, y, filename, tileSize, scale):
        self.pos = Vector(x, y)
        self.scale = scale
        self.loadImage(filename, tileSize)
        self.icon = self.loadImage(filename, tileSize)

    def drawNPC(self, screen, stepSize):
        curRect = (self.pos.x * stepSize.x, self.pos.y * stepSize.y, stepSize.x - 2, stepSize.y - 2)
        screen.blit(self.icon, (curRect[0], curRect[1]))

    def loadImage(self, filename, tileSize):
        image = pygame.image.load(filename)
        return pygame.transform.scale(image, (int(tileSize.x*self.scale), int(tileSize.y*self.scale)))

    @staticmethod
    def checkEmpty(x, y, maze):
        return True
