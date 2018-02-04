import os

import Vector
import pygame

from Cell import Cell


class Map:
    """The base class for the interacting candidates"""

    def __init__(self, mapName, tileSize, tileLoader):
        self.id = 0
        self.neighbors = []

        # Used for collision detection
        self.solidObjectGroup = pygame.sprite.Group()
        self.notSolidObjectGroup = pygame.sprite.Group()
        # Used to show the correct blocks on screen
        self.cameraViewGroup = pygame.sprite.Group()

        self.map, self.width, self.height = self.readMap("maps", mapName, tileLoader, "mapTiles",
                                                         {0: False, 1: True, 2: False, 3: True, 4: True},
                                                         {1: 0, 2: 0, 3: 0, 4: 0})
        self.tileSize = tileSize

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getTileAt(self, pos):
        return self.map[pos.y][pos.x]

    def getTilesInRect(self, rect):
        x = 0
        y = 0
        tiles = []
        for i in range(rect[1], rect[1] + rect[3]):
            for j in range(rect[0], rect[0] + rect[2]):
                self.map[i][j].setPosition(x, y)
                tiles.append(self.map[i][j])
                x += 1
            x = 0
            y += 1
        return tiles


    def setVisibleTiles(self, rect):
        tiles = self.getTilesInRect(rect)
        # if tiles is not None:
        #     for tile in tiles:
        self.cameraViewGroup.add(tiles)

    def isObstacle(self, x, y):
        if self.map[int(y)][int(x)].solid:
            return True
        return False

    def readMap(self, filelocation, mapName, tileLoader, spriteSheetName, tileSignificanceDict,
                doorwaySignificanceDict):
        """Return:
                Tile size, map size, the map and the position of the item
        """

        # Read the file containing the map
        file = open(os.path.join(filelocation, str(mapName) + '.csv'), 'r')

        # Get the id
        self.id = int(file.readline())

        # Get the neighbors ID
        neighbors = file.readline().split(',')
        neighbors = [line.rstrip('\n') for line in neighbors]
        self.neighbors = neighbors

        # Get the size of the map
        mapSize = file.readline().split(',')
        mapSize = [line.rstrip('\n') for line in mapSize]  # Strip all the trailling newlines

        width = int(mapSize[0])
        height = int(mapSize[1])

        map = []

        """ Fill the map with the contents of the map text
            If the value is > 0, the value is a tile, if < 0 the value is a door"""
        for i in range(height):
            map.append([])
            fileRead = file.readline().split(',')
            # If the line is empty
            if len(fileRead) == 1:
                continue
            for j in range(width):
                value = int(fileRead[j])
                if value >= 0:
                    tile = value
                    isSolid = tileSignificanceDict.get(value)
                    cell = Cell(j, i, isSolid, tileLoader.getTileFromName(spriteSheetName, tile))
                    map[i].append(cell)
                    if isSolid:
                        self.solidObjectGroup.add(cell)
                    else:
                        self.notSolidObjectGroup.add(cell)
                elif value < 0:  # Doorway to another world
                    cell = Cell(j, i, False, tileLoader.getTileFromName(spriteSheetName,
                                                                        doorwaySignificanceDict[abs(int(fileRead[j]))]),
                                abs(int(fileRead[j])))
                    map[i].append(cell)
                    self.notSolidObjectGroup.add(cell)

        file.close()

        return map, width, height

    def draw(self, surface):
        self.cameraViewGroup.draw(surface)
