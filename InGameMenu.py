import pygame

import UserEvents
from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIImage import UIImage


class InGameMenu(InteractiveScreen):
    def __init__(self, screenSize, tileLoader, fontRenderer):
        InteractiveScreen.__init__(self)
        self.addVisuelElement(UIImage(0, 300, 300, screenSize.x / 2 - 150, screenSize.y / 2 - 150,
                                      tileLoader.getImageByName("menuBackground", 0, 0)))
        self.addInteractiveElement(UIButton(0, 100, 30, screenSize.x / 2 - 50, screenSize.y / 2 - 100,
                                            tileLoader.getImageByName("button", 0, 1),
                                            tileLoader.getImageByName("button", 0, 0), self.resumeGame, "Resume", fontRenderer))
        self.addInteractiveElement(UIButton(0, 100, 30, screenSize.x / 2 - 50, screenSize.y / 2 - 60,
                                            tileLoader.getImageByName("button", 0, 1),
                                            tileLoader.getImageByName("button", 0, 0), self.quitGame, "Quit", fontRenderer))
        self.resumeGame = False
        self.quitGame = False

    def resumeGame(self):
        try:
            pygame.event.post(pygame.event.Event(UserEvents.RESUMEGAME))
        except pygame.error:
            print("Queue is full")

    def quitGame(self):
        try:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        except pygame.error:
            print("Queue is full")
