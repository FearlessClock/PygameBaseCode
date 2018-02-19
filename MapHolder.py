from Map import Map
from TileLoader import TileLoader


class MapHolder:

    def __init__(self, filenames, tileSize, tileLoader):
        self.mapNames = filenames  #
        self.maps = []
        self.loadedMap = None
        mapValues = []
        idValues = []
        self.currentMap = 3
        self.tileSize = tileSize
        for i in range(len(self.mapNames)):
            map = Map(self.mapNames[i], self.tileSize, tileLoader)
            mapValues.append(map)
            idValues.append(map.id)
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
