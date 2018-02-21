import pygame
from pygame.rect import Rect


class UIElement(pygame.sprite.Sprite):
    """Parent object for all the UiElements in the engine."""
    def __init__(self, id, width, height, x, y, image=None):
        """Give the element an id, size, position and image

        All elements have to give the id, size, and position but the image is optional"""
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
        """Add an animation controller to the element.

        This allows the creator to have animations in elements on the screen"""
        self.isAnimation = True
        self.animationController = controller

    def draw(self, window):
        """Draw the element to the screen"""
        if self.image is not None:
            window.screen.blit(self.image, (self.x, self.y))

    def changeImage(self, newImage):
        """Update the image of the element"""
        self.image = newImage

    def update(self, deltaTime):
        """If there is an animation on the element, step the current animation"""
        if self.isAnimation:
            self.animationController.stepCurrentAnimation(deltaTime)
            self.image = self.animationController.getCurrentAnimationFrame()