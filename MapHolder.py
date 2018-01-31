from Map import Map
from TileLoader import TileLoader


class MapHolder:

    def __init__(self, tileSize, tileLoader):
        self.mapNames = ["map1", "map2", "map3", "map4", "map5"]
        self.maps = []
        self.loadedMap = None
        mapValues = []
        idValues = []
        self.currentMap = 1
        self.tileSize = tileSize
        for i in range(len(self.mapNames)):
            mapValues.append(Map(self.mapNames[i], self.tileSize, tileLoader))
            idValues.append(mapValues[len(mapValues)-1].id)
        self.maps = dict(zip(idValues, mapValues))
        self.changeToMap(self.currentMap)

    def getCurrentMap(self):
        return self.loadedMap

    def changeToMap(self, id):
        self.currentMap = int(id)
        self.loadedMap = self.maps[self.currentMap]

    def getMapById(self, id):
        for key, mapTested in self.maps.items():
            if (mapTested.id == id):
                return mapTested
        return None
