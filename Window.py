from threading import Timer

from GUI import GUI
from MapHolder import MapHolder
from Map import Map
from NPCManager import NPCManager
from TileLoader import TileLoader
import pygame

from Vector import Vector


class Window:
    def __init__(self, windowSize, tileLoader, caption, TILE_SIZE, font_renderer):
        self.width = windowSize.x
        self.height = windowSize.y
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(caption)
        self.font_renderer = font_renderer
        self.GUI = None
        self.TILE_SIZE = TILE_SIZE

        self.imageLoader = None

    def getSize(self):
        return self.screen.get_size()

    def clearScreen(self):
        background = pygame.Surface(self.getSize())
        background = background.convert()
        background.fill((255, 255, 255))
        self.screen.blit(background, (0,0))

    def showScreen(self, currentMap):
        # Display the map
        stepSize = self.TILE_SIZE
        tileMap = currentMap
        """For each cell, find the icon and show it on the screen"""
        for i in range(0, tileMap.getHeight()):
            for j in range(0, tileMap.getWidth()):
                curRect = (j* stepSize.x, i * stepSize.y, stepSize.x, stepSize.y)
                wall = tileMap.getTileAt(Vector(j, i))
                self.screen.blit(wall.image, (curRect[0], curRect[1]))
        self.GUI.drawScreen(self, self.font_renderer)

    def drawScreen(self, tileMap, player, NPCManagerIns):
        """Draw the screen, characters and pop up if activated"""
        self.clearScreen()
        self.showScreen(tileMap)
        NPCManagerIns.showNPCs(self.screen, self.TILE_SIZE)
        player.drawNPC(self.screen, self.TILE_SIZE)
