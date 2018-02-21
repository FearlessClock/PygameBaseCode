from pygame.constants import BLEND_MULT
from pygame.rect import Rect

from UIElement import UIElement


class UIBar(UIElement):
    """A UIELement that shows an image on the screen and allows it to be 'filled' to a certain percent

    See Sims stat bars"""
    def __init__(self, id, width, height, x, y, image, filler):
        UIElement.__init__(self, id, width, height, x, y, image)
        self.fillPercent = 0.5
        self.filler = filler
        self.logo = self.image
        self.id = id

    def setFillPercent(self, amount):
        """Fill the bar to a certain percent"""
        self.fillPercent = amount

    def drawToScreen(self, screen, font_renderer=None):
        """Draw the bar to the screen"""
        logoBlit = self.logo.copy()
        screen.blit(self.filler, (self.x, self.y + self.logo.get_height()*self.fillPercent))
        screen.blit(logoBlit, (self.x, self.y))
