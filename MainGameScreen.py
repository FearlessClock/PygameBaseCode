import pygame


class MainGameScreen:
    def __init__(self, mapHolder, player):
        self.mapHolder = mapHolder
        self.loadedMap = mapHolder.getCurrentMap()
        self.player = pygame.sprite.Group(player)

    def updateScreen(self, dt):
        self.player.update(dt, self.mapHolder)

    def movePlayer(self, event):
        for player in self.player.sprites():
            player.move(event)

    def drawScreen(self, surface):
        self.loadedMap.setVisibleTiles((2,2,8,8))
        self.loadedMap.draw(surface.screen)
        self.player.draw(surface.screen)