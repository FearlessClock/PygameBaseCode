import pygame.constants

from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIImage import UIImage


class StartUpMenu(InteractiveScreen):
    def __init__(self, tileLoader):
        InteractiveScreen.__init__(self)
        self.tileLoader = tileLoader
        self.addVisuelElement(UIImage(500, 500, 0, 0, tileLoader.getImageByName('startMenuBackground', 0, 0)))
        self.addVisuelElement(UIImage(80, 80, 0, 0, tileLoader.getAnimationFrameByName('player')))
        self.addInteractiveElement(UIButton(0, 100, 30, 100, 150, tileLoader.getImageByName('button', 0, 1),
                                            tileLoader.getImageByName('button', 0, 0), self.StartGame, "button"))
        self.addInteractiveElement(UIButton(1, 100, 30, 100, 250, tileLoader.getImageByName('button', 0, 1),
                                            tileLoader.getImageByName('button', 0, 0), None, "button"))
        self.addInteractiveElement(UIButton(2, 100, 30, 100, 350, tileLoader.getImageByName('button', 0, 1),
                                            tileLoader.getImageByName('button', 0, 0), self.QuitGame, "button"))

        self.getInteractiveElement(0).setSelected(True)
        self.animationStep = 0
        self.selectedButton = 0


    def handleInput(self, press):
        for keypress in press:
            if keypress.key == pygame.K_DOWN:
                self.getInteractiveElement(self.selectedButton).setSelected(False)
                if self.selectedButton + 1 < len(self.interactiveElements):
                    self.selectedButton += 1
                else:
                    self.selectedButton = 0
                self.getInteractiveElement(self.selectedButton).setSelected(True)

            elif keypress.key == pygame.K_UP:
                self.getInteractiveElement(self.selectedButton).setSelected(False)
                if self.selectedButton - 1 >= 0:
                    self.selectedButton -= 1
                else:
                    self.selectedButton = len(self.interactiveElements) - 1
                self.getInteractiveElement(self.selectedButton).setSelected(True)

            elif keypress.key == pygame.K_SPACE or keypress.key == pygame.K_RETURN:
                if self.getInteractiveElement(self.selectedButton).callback is not None:
                    self.getInteractiveElement(self.selectedButton).callback()
            else:
                print("Key fail")

    def QuitGame(self):
        try:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        except pygame.error:
            print("Queue is full")

    def StartGame(self):
        try:
            import UserEvents
            pygame.event.post(pygame.event.Event(UserEvents.STARTGAME))
        except pygame.error:
            print("Queue is full")