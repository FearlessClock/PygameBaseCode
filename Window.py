import pygame

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

        # self.tileLoader = TileLoader(TILE_SIZE, windowSize)

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
        self.screens[self.screenDictionary[screenName]].drawScreen(self.screen)
        pygame.display.flip()
