import pygame

from UIElement import UIElement

class UIButton(UIElement):
    def __init__(self, id, width, height, x, y, notSelectedimage, selectedImage, callback, text, fontRenderer):
        UIElement.__init__(self, id, width, height, x, y, notSelectedimage)
        self.isSelected = False
        self.imageSelected = pygame.transform.scale(selectedImage, (width, height))
        self.imageNotSelected = pygame.transform.scale(notSelectedimage, (width, height))
        self.callback = callback
        self.text = text
        self.fontRenderer = fontRenderer

    def setSelected(self, state):
        self.isSelected = state
        if state:
            self.image = self.imageSelected
        else:
            self.image = self.imageNotSelected

    def draw(self, window):
        window.screen.blit(self.image, (self.x, self.y))
        textSize = self.fontRenderer.size(self.text)
        window.screen.blit(self.fontRenderer.render(self.text, False, (0,0,0)), (self.x+self.width/2-textSize[0]
                                                                                 /2, self.y))