import pygame

from UIElement import UIElement

class UIButton(UIElement):
    def __init__(self, id, width, height, x, y, notSelectedimage, selectedImage, callback, text):
        UIElement.__init__(self, width, height, x, y, notSelectedimage)
        self.isSelected = False
        self.id = id
        self.imageSelected = pygame.transform.scale(selectedImage, (width, height))
        self.imageNotSelected = pygame.transform.scale(notSelectedimage, (width, height))
        self.callback = callback
        self.text = text

    def setSelected(self, state):
        self.isSelected = state
        if state:
            self.image = self.imageSelected
        else:
            self.image = self.imageNotSelected