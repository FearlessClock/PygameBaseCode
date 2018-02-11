import pygame

from Camera import Camera
from Vector import Vector


class MainGameScreen:
    def __init__(self, mapHolder, player, screenSize):
        self.mapHolder = mapHolder
        self.player = pygame.sprite.Group(player)
        self.camera = Camera(Vector(8, 8), self.mapHolder.tileSize, screenSize)

    def updateScreen(self, dt):
        self.player.update(dt, self.mapHolder)
        self.mapHolder.getCurrentMap().NPCManager.update(dt, self.mapHolder.getCurrentMap())
        self.camera.setPosition(int(self.player.sprites()[0].pos.x),
                                int(self.player.sprites()[0].pos.y))

    def movePlayer(self, event):
        for player in self.player.sprites():
            player.move(event)

    def drawScreen(self, surface):
        self.camera.setVisibleSprites(self.mapHolder.getCurrentMap())
        self.camera.draw(surface.screen, self.player.sprites()[0], self.mapHolder.getCurrentMap().NPCManager.getNPCs())

    def getCurrentMap(self):
        return self.mapHolder.getCurrentMap()