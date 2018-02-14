import copy

import pygame
from pygame.rect import Rect

from Vector import Vector


class Camera(pygame.sprite.Group):
    # Position of the camera is the top left corner
    def __init__(self, nmbrOfTilesOnScreen, tileSize, screenSize):
        pygame.sprite.Group.__init__(self)
        self.tileSize = tileSize
        self.nmbrOfTilesOnScreen = nmbrOfTilesOnScreen
        self.screenRect = Rect(0, 0, screenSize.x, screenSize.y)
        self.tileRect = Rect(0, 0, nmbrOfTilesOnScreen.x, nmbrOfTilesOnScreen.y)
        self.levelSize = Vector(0,0)

    def setPosition(self, x, y):
        x = x - self.tileRect.x-self.tileRect.width/2
        y = y - self.tileRect.y-self.tileRect.height/2

        # print(self.tileRect.x, self.levelSize.x - self.tileRect.width/2)
        self.tileRect = self.tileRect.move(x, y)

    def setVisibleSprites(self, level):
        tiles = level.getTilesInRect(self.tileRect, self.tileRect)
        self.levelSize = Vector(level.width, level.height)
        self.empty()
        self.add(tiles)
        #print(len(self.sprites()))

    def MoveCameraToPlayerLocation(self, player):
        self.screenRect.x = max(player.x - self.screenRect.width/2, 0)
        self.screenRect.x = min((self.levelSize.x*self.tileSize.x - self.screenRect.width), self.screenRect.x)
        self.screenRect.y = max(player.y - self.screenRect.height/2, 0)
        self.screenRect.y = min((self.levelSize.y*self.tileSize.y - self.screenRect.height), self.screenRect.y)


    def draw(self, surface, player, npcList):
        self.MoveCameraToPlayerLocation(player.rect)
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            rect = Rect(spr.rect.x - self.screenRect.x, spr.rect.y - self.screenRect.y, 0, 0)
            self.spritedict[spr] = surface_blit(spr.image, rect)

        for npc in npcList:
            rect = Rect(npc.rect.x - self.screenRect.x, npc.rect.y - self.screenRect.y, 0, 0)
            surface_blit(npc.image, rect)

        rect = copy.deepcopy(player.rect)
        rect.x -= self.screenRect.x
        rect.y -= self.screenRect.y
        surface_blit(player.image, rect)

        self.lostsprites = []
