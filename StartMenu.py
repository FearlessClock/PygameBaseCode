import pygame.constants

from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIButton import Action
from UIImage import UIImage


class StartUpMenu(InteractiveScreen):
    def __init__(self):
        InteractiveScreen.__init__(self)
        self.elements.add(UIImage(500, 500, 0, 0, pygame.image.load_extended("images\\blablaMockup.png")))
        self.interactiveElements.add(UIButton(0, 100, 30, 100, 150, pygame.image.load_extended("images\\button.png"),
                                              pygame.image.load_extended("images\\buttonSelected.png"), self.StartGame, "button"),
                                     UIButton(1, 100, 30, 100, 250, pygame.image.load_extended("images\\button.png"),
                                              pygame.image.load_extended("images\\buttonSelected.png"), None, "button")
                                     ,
                                     UIButton(2, 100, 30, 100, 350, pygame.image.load_extended("images\\button.png"),
                                              pygame.image.load_extended("images\\buttonSelected.png"), self.QuitGame, "button")
                                     )
        self.interactiveElements.update(Action.MOVE, 0, True)
        self.selectedButton = 0

    def handleInput(self, press):
        for keypress in press:
            if keypress.key == pygame.K_DOWN:
                self.interactiveElements.update(Action.MOVE, self.selectedButton, False)
                if self.selectedButton + 1 < len(self.interactiveElements):
                    self.selectedButton += 1
                else:
                    self.selectedButton = 0
                self.interactiveElements.update(Action.MOVE, self.selectedButton, True)
            elif keypress.key == pygame.K_UP:
                self.interactiveElements.update(Action.MOVE, self.selectedButton, False)
                if self.selectedButton - 1 >= 0:
                    self.selectedButton -= 1
                else:
                    self.selectedButton = len(self.interactiveElements) - 1
                self.interactiveElements.update(Action.MOVE, self.selectedButton, True)
            elif keypress.key == pygame.K_SPACE or keypress.key == pygame.K_RETURN:
                self.interactiveElements.update(Action.CALLBACK, self.selectedButton, None)
            else:
                print("Key fail")

    def QuitGame(self):
        try:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        except pygame.error:
            print("Queue is full")

    def StartGame(self):
        try:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, code="StartGame"))
        except pygame.error:
            print("Queue is full")