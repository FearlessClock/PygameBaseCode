import os

import Vector
import pygame

from Cell import Cell

class Map:
    """The base class for the interacting candidates"""
    def __init__(self, mapName, tileSize, tileLoader):
        self.id = 0
        self.neighbors = []
        self.map, self.width, self.height = self.readMap(mapName, tileLoader)
        self.tileSize = tileSize

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getTileAt(self, pos):
        return self.map[pos.y][pos.x]

    def isObstacle(self, x, y):
        if self.map[int(y)][int(x)].solid:
            return True
        return False


    def readMap(self, mapName, tileLoader):
        """Return:
                Tile size, maze size, the maze and the position of the item
        """

        # Read the file containing the maze
        file = open(os.path.join('Maps', str(mapName) + '.csv'), 'r')

        # Get the id
        self.id = int(file.readline())

        # Get the neighbors
        neighbors = file.readline().split(',')
        neighbors = [line.rstrip('\n') for line in neighbors]
        self.neighbors = neighbors

        # Get the size of the map
        mapSize = file.readline().split(',')
        mapSize = [line.rstrip('\n') for line in mapSize]   # Strip all the trailling newlines



        width = int(mapSize[0])
        height = int(mapSize[1])

        maze = []

        """Generate the empty maze"""
        for i in range(height):
            maze.append([])
            for j in range(width):
                maze[i].append(Cell(j, i, False, tileLoader.grass))

        """Fill the maze with the contents of the maze text"""
        for i in range(height):
            fileRead = file.readline().split(',')
            if len(fileRead) == 1:
                continue
            for j in range(width):
                value = int(fileRead[j])
                if value >= 0:
                    isSolid = False
                    tile = tileLoader.grass
                    if value == 0:
                        isSolid = False
                        tile = 0
                    elif value == 1:
                        isSolid = False
                        tile = 1
                    elif value == 2:
                        isSolid = True
                        tile = 2
                    elif value == 3:
                        isSolid = True
                        tile = 3
                    elif value == 4:
                        isSolid = False
                        tile = 4
                    elif value == 5:
                        isSolid = True
                        tile = 5
                    elif value == 6:
                        isSolid = True
                        tile = 6
                    elif value == 7:
                        isSolid = True
                        tile = 7
                    elif value == 8:
                        isSolid = True
                        tile = 8
                    elif value == 9:
                        isSolid = True
                        tile = 9

                    maze[i][j] = Cell(j, i, isSolid, tileLoader.getTile(tile))
                elif -6 <= value <= -2:         # Doorway to another world
                    maze[i][j] = Cell(j, i, False, tileLoader.getTile(4 if abs(int(fileRead[j])) == 6 else 0), abs(int(fileRead[j])))

        file.close()

        return maze, width, height
