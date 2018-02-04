class MainGameScreen:
    def __init__(self, mapHolder):
        self.mapHolder = mapHolder
        self.loadedMap = mapHolder.getCurrentMap()

    def drawScreen(self, surface):
        self.loadedMap.setVisibleTiles((2,2,8,8))
        self.loadedMap.draw(surface.screen)