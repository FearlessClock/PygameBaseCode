import pygame
from pygame.rect import Rect

from Direction import Direction
from Vector import Vector


class MobileUnit(pygame.sprite.Sprite):
    """The base class for the interacting candidates"""

    def __init__(self, x, y, tileLoader, tileSize, animationController, directionSigDict, scale):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector(x, y)
        self.scale = scale
        self.tileSize = tileSize
        self.animationController = animationController
        self.directionSignificanceDict = directionSigDict
        animationController.changeCurrentAnimationTo(directionSigDict.get(Direction.DOWN))
        image = animationController.getCurrentAnimationFrame()
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = Rect(x*tileSize.x, y*tileSize.y, image.get_width(), image.get_height())
        self.direction = Direction.DOWN

    def setPosition(self, x, y):
        self.pos = Vector(x, y)
        self.rect = (x*100, y*100, self.image.get_width(), self.image.get_height())

    def setDirection(self, direction):
        self.direction = direction

    def currentAnimationFrame(self):
        return self.animationController.getCurrentAnimationFrame()

    def stepCurrentAnimation(self, dt):
        self.animationController.stepCurrentAnimation(dt)

    def updateAnimation(self):
        self.animationController.changeCurrentAnimationTo(self.directionSignificanceDict.get(self.direction))