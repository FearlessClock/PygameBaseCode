from Map import Map
from TileLoader import TileLoader


class MapHolder:
    """Class holding all the loaded maps"""
    def __init__(self, filenames, tileSize, tileLoader):
        self.mapNames = filenames  #
        self.maps = []
        self.loadedMap = None
        mapValues = []
        idValues = []
        self.currentMap = 3
        self.tileSize = tileSize
        self.nmbrOfCreautresPerMap = 50
        for i in range(len(self.mapNames)):
            map = Map(self.mapNames[i], self.tileSize, tileLoader, self.nmbrOfCreautresPerMap)
            mapValues.append(map)
            idValues.append(map.id)
        self.maps = dict(zip(idValues, mapValues))
        self.changeToMap(self.currentMap)

    def getNumberOfCreatures(self):
        """Return the number of creatures loaded across all the maps"""
        return len(self.maps) * self.nmbrOfCreautresPerMap

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
