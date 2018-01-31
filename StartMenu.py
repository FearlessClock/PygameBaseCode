import pygame.constants

from Direction import Direction
from InteractiveScreen import InteractiveScreen
from UIButton import UIButton
from UIImage import UIImage
from UIText import UIText


class StartUpMenu(InteractiveScreen):
    def __init__(self, tileLoader, toGameCallback, quitCallback):
        InteractiveScreen.__init__(self)
        self.elements = [UIImage(0, 0, 0, 0, tileLoader.blablaBackground),
                         UIImage(0, 0, 250, tileLoader.screenSize.y - 90 - 120, tileLoader.getPlayerAnimationFrame(Direction.YOUPI, 0))]
        self.toGameCallback = toGameCallback

        self.tileLoader = tileLoader
        self.useRacks = False
        self.interactiveElements = [
            UIButton(100, 50, tileLoader.screenSize.x / 2 - 168 / 2, 200, tileLoader.getButton(1),
                     tileLoader.getButton(2), self.playButton, "Play"),
            UIButton(100, 50, tileLoader.screenSize.x / 2 - 168 / 2, 300, tileLoader.getButton(1),
                     tileLoader.getButton(2), quitCallback, "Quit")]
        self.interactiveElements[self.selectedButton].isSelected = True

    def update(self, dt):
        self.elements[1].image = self.tileLoader.getPlayerAnimationFrame(Direction.PICKUPHAT, dt)

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

    def playButton(self):
        self.interactiveElements = [self.interactiveElements[0]]
        self.interactiveElements[0].callback = self.toGameCallback
        self.interactiveElements[0].text = "Let's go!"
        self.interactiveElements[0].y = 320
        self.interactiveElements[0].isSelected = False
        textPos = (50, 70)
        textStep = 25
        textColor = (0,0,0)
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1], textColor, "Welcome to SectQuest!"))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep, textColor , "You want to create your own sect"))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*2, textColor, "and you are ready for anything to make it work!"))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*3, textColor, "You have to walk around and convert people."))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*4, textColor, "When your sect becomes bigger,"))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*5, textColor, "you can start sending people to work for you"))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*6, textColor, "or bribe the president."))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*7, textColor, "Good luck!"))
        self.elements.append(UIText(0, 0, 0, textPos[0], textPos[1]+textStep*8, textColor, "May you find the followers that you deserve!"))
