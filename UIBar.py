from pygame.constants import BLEND_MULT
from pygame.rect import Rect

from UIElement import UIElement


class UIBar(UIElement):
    def __init__(self, id, width, height, x, y, image, filler):
        UIElement.__init__(self, width, height, x, y, image)
        self.fillPercent = 0.5
        self.filler = filler
        self.logo = self.image
        self.id = id

    def setFillPercent(self, amount):
        self.fillPercent = amount

    def drawToScreen(self, screen, font_renderer=None):
        logoBlit = self.logo.copy()
        screen.blit(self.filler, (self.x, self.y + self.logo.get_height()*self.fillPercent))
        screen.blit(logoBlit, (self.x, self.y))
