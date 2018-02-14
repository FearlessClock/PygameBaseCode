import pygame.constants

from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIImage import UIImage


class StartUpMenu(InteractiveScreen):
    def __init__(self, tileLoader, fontRenderer):
        InteractiveScreen.__init__(self)
        self.tileLoader = tileLoader
        self.screenSize = (500, 500)
        self.addVisuelElement(UIImage(0, self.screenSize[0], self.screenSize[1], 0, 0, tileLoader.getImageByName('startMenuBackground', 0, 0)))
        self.addVisuelElement(UIImage(1,80, 80, 200, self.screenSize[1]-80, tileLoader.getAnimationFrameByName('player')))
        self.getVisuelElementByIndex(1).addAnimationController(tileLoader.getAnimationController('player'))
        self.animationCounter = 0
        buttonSize = fontRenderer.size("Start Game")
        self.addInteractiveElement(UIButton(0, buttonSize[0]+16, 30, self.screenSize[0]/2-(buttonSize[0]+16)/2, 150, tileLoader.getImageByName('button', 0, 1),
                                            tileLoader.getImageByName('button', 0, 0), self.StartGame, "Start Game", fontRenderer))
        buttonSize = fontRenderer.size("Turn Animation")
        self.addInteractiveElement(UIButton(1, buttonSize[0]+16, 30, self.screenSize[0]/2-(buttonSize[0]+16)/2, 250, tileLoader.getImageByName('button', 0, 1),
                                            tileLoader.getImageByName('button', 0, 0), self.animationChange, "Turn animation", fontRenderer))
        buttonSize = fontRenderer.size("Quit")
        self.addInteractiveElement(UIButton(2, buttonSize[0]+16, 30, self.screenSize[0]/2-(buttonSize[0]+16)/2, 350, tileLoader.getImageByName('button', 0, 1),
                                            tileLoader.getImageByName('button', 0, 0), self.QuitGame, "Quit", fontRenderer))

        self.getInteractiveElementByIndex(0).setSelected(True)
        self.animationStep = 0
        self.selectedButton = 0


    def QuitGame(self):
        try:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        except pygame.error:
            print("Queue is full")

    def animationChange(self):
        self.animationCounter = (self.animationCounter + 1 ) %4
        if self.animationCounter == 0:
            self.tileLoader.setAnimationForNameToName("player", 'playerUp')
        elif self.animationCounter == 1:
            self.tileLoader.setAnimationForNameToName("player", 'playerDown')
        elif self.animationCounter == 2:
            self.tileLoader.setAnimationForNameToName("player", 'playerLeft')
        elif self.animationCounter == 3:
            self.tileLoader.setAnimationForNameToName("player", 'playerRight')

    def StartGame(self):
        try:
            import UserEvents
            pygame.event.post(pygame.event.Event(UserEvents.STARTGAME))
        except pygame.error:
            print("Queue is full")