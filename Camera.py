import pygame
from pygame.rect import Rect

from Vector import Vector


class Camera(pygame.sprite.Group):
    """Camera class. Follow the player on the screen"""
    # Position of the camera is the top left corner
    def __init__(self, nmbrOfTilesOnScreen, tileSize, screenSize):
        """Basic camera information"""
        pygame.sprite.Group.__init__(self)
        self.tileSize = tileSize
        self.nmbrOfTilesOnScreen = nmbrOfTilesOnScreen
        self.screenRect = Rect(0, 0, screenSize.x, screenSize.y)
        self.tileRect = Rect(0, 0, nmbrOfTilesOnScreen.x, nmbrOfTilesOnScreen.y)
        self.levelSize = Vector(0, 0)

    def setPosition(self, x, y):
        """Set the position of the camera"""
        x = x - self.tileRect.x - self.tileRect.width / 2
        y = y - self.tileRect.y - self.tileRect.height / 2

        self.tileRect = self.tileRect.move(x, y)

    def setVisibleSprites(self, level):
        """Get the tiles that fall inside the screen and show them"""
        tiles = level.getTilesInRect(self.tileRect, self.tileRect)
        self.levelSize = Vector(level.width, level.height)
        self.empty()
        self.add(tiles)

    def MoveCameraToPlayerLocation(self, player):
        """Move the camera so that it is centered on the player but doesn't go past the side"""
        self.screenRect.x = max(player.x - self.screenRect.width / 2, 0)
        self.screenRect.x = min(max(0, (self.levelSize.x * self.tileSize.x - self.screenRect.width)), self.screenRect.x)
        self.screenRect.y = max(player.y - self.screenRect.height / 2, 0)
        self.screenRect.y = min(max(0, (self.levelSize.y * self.tileSize.y - self.screenRect.height)), self.screenRect.y)

    def draw(self, surface, player, npcList):
        """Draw the player, creatures and tiles with the camera movement"""
        self.MoveCameraToPlayerLocation(player.rect)
        sprites = self.sprites()
        surface_blit = surface.blit
        # Move every sprite so as to be well placed with the camera
        for spr in sprites:
            rect = Rect(spr.rect.x - self.screenRect.x, spr.rect.y - self.screenRect.y, 0, 0)
            self.spritedict[spr] = surface_blit(spr.image, rect)

        for npc in npcList:
            rect = Rect(npc.rect.x - self.screenRect.x, npc.rect.y - self.screenRect.y, 0, 0)
            surface_blit(npc.image, rect)

        rect = Rect(player.rect)
        rect.x -= self.screenRect.x
        rect.y -= self.screenRect.y
        player.net.draw(surface_blit, self.screenRect)
        surface_blit(player.image, rect)

        self.lostsprites = []
