import pygame
from pygame.rect import Rect


class UIElement(pygame.sprite.Sprite):

    def __init__(self, id, width, height, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        if image is not None:
            self.image = pygame.transform.scale(image, (int(width), int(height)))
        else:
            self.image = None
        self.isAnimation = False
        self.animationController = None
        self.rect = Rect(x, y, width, height)

    def addAnimationController(self, controller):
        self.isAnimation = True
        self.animationController = controller

    def draw(self, window):
        if self.image is not None:
            window.screen.blit(self.image, (self.x, self.y))

    def changeImage(self, newImage):
        self.image = newImage

    def update(self, deltaTime):
        if self.isAnimation:
            self.animationController.stepCurrentAnimation(deltaTime)
            self.image = self.animationController.getCurrentAnimationFrame()