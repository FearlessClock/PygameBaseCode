import pygame


class UIElement:

    def __init__(self, width, height, x, y, image):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = image

    def drawToScreen(self, screen, font_renderer=None):
        if self.image is not None:
            screen.blit(self.image, (self.x, self.y))
