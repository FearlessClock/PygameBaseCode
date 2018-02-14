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

        self.tileLoader.addSpriteSheet("player", os.path.join('images', 'playerSpriteSheet.png'), Vector(400, 600), Vector(40, 60), 8, 4)
        self.tileLoader.addSpriteSheet("startMenuBackground", os.path.join('images', 'blablaMockup.png'), Vector(640, 540), Vector(500, 500), 1, 1)
        self.tileLoader.addSpriteSheet("menuBackground", os.path.join('images', 'menuBackground.png'), Vector(347, 399), Vector(300, 310), 1, 1)

        self.tileLoader.addSpriteSheet("button", os.path.join('images', 'buttonSpriteSheet.png'), Vector(100, 30), Vector(100, 30), 1, 2)

        self.tileLoader.addSpriteSheet("mapTiles", os.path.join('images', "TileSheet.png"), Vector(16,16), Vector(self.TILE_SIZE.x,self.TILE_SIZE.y), 3,3)
        self.tileLoader.addSpriteSheet("healthBars", os.path.join('images', 'healthBarSpriteSheet.png'), Vector(200, 50), Vector(200, 50), 1, 5)

        self.tileLoader.addSpriteSheet("NPC", os.path.join("images", "NPC.png"), Vector(32,32), Vector(36,36), 3, 4)

        NPCAnimationDown = AnimationStrip(self.tileLoader.getImageStripByName("NPC", 0), "NPCDown", 200)
        NPCAnimationLeft = AnimationStrip(self.tileLoader.getImageStripByName("NPC", 1), "NPCLeft", 200)
        NPCAnimationRight = AnimationStrip(self.tileLoader.getImageStripByName("NPC", 2), "NPCRight", 200)

        playerAnimationUp = AnimationStrip(self.tileLoader.getImageStripByName("player", 1), "playerUp", 200)
        playerAnimationDown = AnimationStrip(self.tileLoader.getImageStripByName("player", 0), "playerDown", 200)
        playerAnimationLeft = AnimationStrip(self.tileLoader.getImageStripByName("player", 2), "playerLeft", 200)
        playerAnimationRight = AnimationStrip(self.tileLoader.getImageStripByName("player", 3), "playerRight", 200)
        playerAnimationIdleUp = AnimationStrip(self.tileLoader.getImageStripByName("player", 5), "playerIdleUp", 200)
        playerAnimationIdleDown = AnimationStrip(self.tileLoader.getImageStripByName("player", 4), "playerIdleDown", 200)
        playerAnimationIdleLeft = AnimationStrip(self.tileLoader.getImageStripByName("player", 6), "playerIdleLeft", 200)
        playerAnimationIdleRight = AnimationStrip(self.tileLoader.getImageStripByName("player", 7), "playerIdleRight", 200)

        animationController = AnimationController()
        animationController.addAnimations(playerAnimationUp, playerAnimationDown, playerAnimationLeft, playerAnimationRight, playerAnimationIdleUp, playerAnimationIdleDown, playerAnimationIdleLeft, playerAnimationIdleRight)
        self.tileLoader.addAnimation("player", animationController)

        animationController = AnimationController()
        animationController.addAnimations(NPCAnimationDown)
        animationController.addAnimations(NPCAnimationLeft)
        animationController.addAnimations(NPCAnimationRight)
        self.tileLoader.addAnimation("NPC", animationController)
        self.tileLoader.setAnimationForNameToName("player", "playerRight")
        # self.mapHolder = MapHolder(TILE_SIZE, self.tileLoader)

        # startMenu = StartUpMenu(tileLoader, changeGameLoopStateToRPG, quitGame)

    def addScreenToRender(self, screenToImport, screenName):
        self.screenDictionary.update({screenName:len(self.screens)})
        self.screens.append(screenToImport)

    def getScreen(self, screenName):
        return self.screens[self.screenDictionary[screenName]]

    def getSize(self):
        return self.screen.get_size()

    def clearScreen(self):
        background = pygame.Surface(self.getSize())
        background = background.convert()
        background.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))

    def drawScreen(self, screenName):
        """Draw the screen, characters and pop up if activated"""
        #self.clearScreen()
        self.screens[self.screenDictionary[screenName]].drawScreen(self)

    def updateScreen(self, screenName, deltaTime):
        self.screens[self.screenDictionary[screenName]].updateScreen(deltaTime)