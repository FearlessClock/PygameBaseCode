import copy

import pygame
from pygame.rect import Rect


class Camera(pygame.sprite.Group):
    # Position of the camera is the top left corner
    def __init__(self, nmbrOfTilesOnScreen, tileSize, screenSize):
        pygame.sprite.Group.__init__(self)
        self.tileSize = tileSize
        self.nmbrOfTilesOnScreen = nmbrOfTilesOnScreen
        self.screenRect = Rect(0, 0, screenSize.x, screenSize.y)
        self.tileRect = Rect(0, 0, nmbrOfTilesOnScreen.x, nmbrOfTilesOnScreen.y)

    def setPosition(self, x, y):
        x = x - self.tileRect.x-self.tileRect.width/2
        y = y - self.tileRect.y-self.tileRect.height/2
        self.tileRect = self.tileRect.move(x, y)

    def setVisibleSprites(self, level):
        tiles = level.getTilesInRect(self.tileRect)
        self.empty()
        self.add(tiles)

    def MoveCameraToPlayerLocation(self, player):
        self.screenRect.x = player.x - self.screenRect.width/2
        self.screenRect.y = player.y - self.screenRect.height/2

    def draw(self, surface, player):
        self.MoveCameraToPlayerLocation(player.rect)
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            rect = copy.deepcopy(spr.rect)
            rect.x -= self.screenRect.x
            rect.y -= self.screenRect.y
            self.spritedict[spr] = surface_blit(spr.image, rect)

        rect = copy.deepcopy(player.rect)
        rect.x -= self.screenRect.x
        rect.y -= self.screenRect.y
        surface_blit(player.image, rect)

        self.lostsprites = []
