import pygame.constants

from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIImage import UIImage


class StartUpMenu(InteractiveScreen):
    def __init__(self):
        InteractiveScreen.__init__(self)
        self.elements.add(UIImage(500, 500, 0, 0, pygame.image.load_extended("images\\blablaMockup.png")))
        self.interactiveElements.add(UIButton(100, 30, 100, 250, pygame.image.load_extended("images\\button.png"),
                                              pygame.image.load_extended("images\\buttonSelected.png"), None, "button"))

    def handleInput(self, key, press):
        if press == pygame.KEYDOWN:
            if key == pygame.K_DOWN:
                if self.selectedButton + 1 < len(self.interactiveElements):
                    self.interactiveElements[self.selectedButton].isSelected = False
                    self.selectedButton += 1
                    self.interactiveElements[self.selectedButton].isSelected = True
            elif key == pygame.K_UP:
                if self.selectedButton - 1 >= 0:
                    self.interactiveElements[self.selectedButton].isSelected = False
                    self.selectedButton -= 1
                    self.interactiveElements[self.selectedButton].isSelected = True
            elif key == pygame.K_SPACE or key == pygame.K_RETURN:
                self.interactiveElements[self.selectedButton].callback()
