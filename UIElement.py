import pygame
from pygame.rect import Rect


class UIElement(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image
        self.rect = Rect(x, y, width, height)