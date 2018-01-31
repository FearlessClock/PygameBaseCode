import pygame

from UIElement import UIElement


class UIButton(UIElement):
    def __init__(self, width, height, x, y, image, selectedImage, callback, text):
        UIElement.__init__(self, width, height, x, y, image)
        self.isSelected = False
        self.imageSelected = selectedImage
        self.imageNotSelected = self.image
        self.callback = callback
        self.text = text

    def checkIfInside(self, cursorX, cursorY):
        if self.x + self.width / 2 < cursorX > self.x - self.width / 2:
            if self.y + self.height / 2 < cursorY > self.y - self.height / 2:
                return True
        return False

    def drawToScreen(self, screen, font_renderer=None):
        if self.isSelected:
            self.image = self.imageSelected
        else:
            self.image = self.imageNotSelected
        UIElement.drawToScreen(self, screen)
        offsetX = self.image.get_width()/2 -(len(self.text)*13)/2
        offsetY = self.image.get_height()/2 -15
        # 2nd argument = Antialiasing
        screen.blit(font_renderer.render(self.text, 0, (255,255,255)), (self.x+offsetX, self.y+offsetY))

