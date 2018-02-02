import os
import pygame

from AnimationController import AnimationStrip, AnimationController
from TileLoader import TileLoader
from Vector import Vector


class Window:
    def __init__(self, windowSize, caption, TILE_SIZE, font_renderer):
        self.width = windowSize.x
        self.height = windowSize.y

        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(caption)
        pygame.mouse.set_visible(False)

        self.font_renderer = font_renderer
        self.TILE_SIZE = TILE_SIZE

        self.screens = []
        self.activeScreen = 0
        self.screenDictionary = {}

        self.tileLoader = TileLoader(TILE_SIZE, windowSize)

        self.tileLoader.addSpriteSheet("player", os.path.join('images', 'playerSpriteSheet.png'), Vector(460, 559), Vector(80, 80), 4, 4)
        self.tileLoader.addSpriteSheet("startMenuBackground", os.path.join('images', 'blablaMockup.png'), Vector(640, 540), Vector(500, 500), 1, 1)
        self.tileLoader.addSpriteSheet("button", os.path.join('images', 'buttonSpriteSheet.png'), Vector(100, 30), Vector(100, 30), 1, 2)

        playerAnimationUp = AnimationStrip(self.tileLoader.getImageStripByName("player", 3), "playerUp")
        playerAnimationDown = AnimationStrip(self.tileLoader.getImageStripByName("player", 0), "playerDown")
        playerAnimationLeft = AnimationStrip(self.tileLoader.getImageStripByName("player", 2), "playerLeft")
        playerAnimationRight = AnimationStrip(self.tileLoader.getImageStripByName("player", 1), "playerRight")

        self.animationController = AnimationController()
        self.animationController.addAnimations(playerAnimationUp, playerAnimationDown, playerAnimationLeft, playerAnimationRight)

        self.tileLoader.addAnimation("player", self.animationController)
        self.tileLoader.setAnimationForNameToName("player", "playerUp")
        # self.mapHolder = MapHolder(TILE_SIZE, self.tileLoader)

        # startMenu = StartUpMenu(tileLoader, changeGameLoopStateToRPG, quitGame)

    def addScreenToRender(self, screenToImport, screenName):
        self.screenDictionary.update({screenName:len(self.screens)})
        self.screens.append(screenToImport)

    def getSize(self):
        return self.screen.get_size()

    def clearScreen(self):
        background = pygame.Surface(self.getSize())
        background = background.convert()
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))

    def drawScreen(self, screenName):
        """Draw the screen, characters and pop up if activated"""
        self.clearScreen()
        self.screens[self.screenDictionary[screenName]].drawScreen(self)

