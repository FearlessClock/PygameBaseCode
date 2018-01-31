import pygame

from UIElement import UIElement
from enum import Enum

class Action(Enum):
    MOVE = 1
    CALLBACK = 2


class UIButton(UIElement):
    def __init__(self, id, width, height, x, y, notSelectedimage, selectedImage, callback, text):
        UIElement.__init__(self, width, height, x, y, notSelectedimage)
        self.isSelected = False
        self.id = id
        self.imageSelected = pygame.transform.scale(selectedImage, (width, height))
        self.imageNotSelected = pygame.transform.scale(notSelectedimage, (width, height))
        self.callback = callback
        self.text = text

    def update(self, action, id, state):
        if action == Action.MOVE:
            if self.id == id:
                self.isSelected = state
                if self.isSelected:
                    self.image = self.imageSelected
                else:
                    self.image = self.imageNotSelected
        elif action == Action.CALLBACK:
            if self.id == id:
                if self.callback is not None:
                    self.callback()