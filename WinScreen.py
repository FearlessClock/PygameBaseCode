import pygame

import UserEvents
from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIImage import UIImage


class WinScreen(InteractiveScreen):
    def __init__(self, screenSize, tileLoader, fontRenderer):
        InteractiveScreen.__init__(self)
        print(screenSize)
        self.addVisuelElement(UIImage(0, screenSize.x, screenSize.y, 0, 0,
                                      tileLoader.getImageByName("winBackground", 0, 0)))
        self.addInteractiveElement(UIButton(0, 100, 30, screenSize.x / 2 - 50, screenSize.y / 2 - 100,
                                            tileLoader.getImageByName("button", 0, 1),
                                            tileLoader.getImageByName("button", 0, 0), self.newGame, "New Game", fontRenderer))
        self.addInteractiveElement(UIButton(0, 100, 30, screenSize.x / 2 - 50, screenSize.y / 2 - 60,
                                            tileLoader.getImageByName("button", 0, 1),
                                            tileLoader.getImageByName("button", 0, 0), self.quitGame, "Quit", fontRenderer))
        self.getInteractiveElementByIndex(0).setSelected(True)

    def newGame(self):
        try:
            pygame.event.post(pygame.event.Event(UserEvents.RESUMEGAME))
        except pygame.error:
            print("Queue is full")

    def quitGame(self):
        try:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        except pygame.error:
            print("Queue is full")
