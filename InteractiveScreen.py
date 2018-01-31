import pygame


class InteractiveScreen:
    def __init__(self):
        self.elements = pygame.sprite.Group()
        self.interactiveElements = pygame.sprite.Group()
        self.selectedButton = 0
        self.useRacks = True

    def drawScreen(self, surface):
        self.elements.draw(surface)
        self.interactiveElements.draw(surface)

    def update(self):
        self.elements.update()
        self.interactiveElements.update()
