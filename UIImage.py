from pygame.constants import BLEND_MULT
from pygame.rect import Rect

from UIElement import UIElement


class UIImage(UIElement):
    def __init__(self, width, height, x, y, image):
        UIElement.__init__(self, width, height, x, y, image)
        self.rect = Rect(x,y, width, height)