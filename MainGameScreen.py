import pygame

import GameEndChecker
from Camera import Camera
from Vector import Vector
from GUI import GUI


class MainGameScreen:
    def __init__(self, mapHolder, tileLoader, player, screenSize, fontRenderer):
        self.mapHolder = mapHolder
        self.player = pygame.sprite.Group(player)
        self.camera = Camera(Vector(8, 8), self.mapHolder.tileSize, screenSize)
        self.GUI = GUI(tileLoader, fontRenderer)

    def updateScreen(self, dt):
        self.player.update(dt, self.mapHolder)
        self.GUI.setScore(self.player.sprites()[0].score)
        self.mapHolder.getCurrentMap().NPCManager.update(dt, self.mapHolder.getCurrentMap(), self.player.sprites()[0])
        self.camera.setPosition(int(self.player.sprites()[0].pos.x),
                                int(self.player.sprites()[0].pos.y))
        GameEndChecker.gameEnd(self.mapHolder.getNumberOfCreatures(), self.player.sprites()[0].score)

    def movePlayer(self, event):
        for player in self.player.sprites():
            player.move(event)

    def drawScreen(self, surface):
        self.camera.setVisibleSprites(self.mapHolder.getCurrentMap())
        self.camera.draw(surface.screen, self.player.sprites()[0], self.mapHolder.getCurrentMap().NPCManager.getNPCs())
        self.GUI.drawScreen(surface)

    def getCurrentMap(self):
        return self.mapHolder.getCurrentMap()