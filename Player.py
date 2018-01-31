import pygame, os
from pygame.locals import *

from MobileUnit import MobileUnit
from TileLoader import loadImage
from Direction import Direction
from Vector import Vector


class Player(MobileUnit):
    """Structure to store the player information"""

    def __init__(self, x, y, tileLoader, filename, tileSize):
        self.size = 0.5
        MobileUnit.__init__(self, x, y, filename, tileSize, self.size)
        self.up = pygame.K_UP
        self.down = pygame.K_DOWN
        self.right = pygame.K_RIGHT
        self.left = pygame.K_LEFT

        self.sideOffset = 0.2
        self.tileSize = tileSize

        self.speed_x = 0
        self.speed_y = 0

        self.headOffset = 1

        self.direction = Direction.IDLES
        tileLoader.loadPlayerImages(self.size)
        self.tileLoader = tileLoader

        self.hq_flag = False
        self.hqLocation = None

        self.interactionFlag = False
        self.NPCToInteractWith = None
        self.changeLevel = -1

        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False

    def update(self, dt, mapHolder, window):
        # pos.x/y are in "world units"
        new_x = self.pos.x + self.speed_x * dt / 60 / 5
        new_y = self.pos.y + self.speed_y * dt / 60 / 5

        new_lt = Vector(int(new_x + self.sideOffset), int(new_y - self.sideOffset + self.headOffset))
        new_rt = Vector(int(new_x + self.size - self.sideOffset), int(new_y - self.sideOffset + self.headOffset))
        new_rb = Vector(int(new_x + self.size - self.sideOffset), int(new_y + self.size + self.sideOffset + self.headOffset))
        new_lb = Vector(int(new_x + self.sideOffset), int(new_y + self.size + self.sideOffset + self.headOffset))
        currentMap = mapHolder.getCurrentMap()

        h = currentMap.getHeight()
        w = currentMap.getWidth()
        if (w > new_lt.x >= 0 and h > new_lt.y >= 0 and not currentMap.getTileAt(new_lt).solid) and (
            w > new_rt.x >= 0 and h > new_rt.y >= 0 and not currentMap.getTileAt(new_rt).solid) and \
            w > new_rb.x >= 0 and h > new_rb.y >= 0 and not currentMap.getTileAt(new_rb).solid and \
            w > new_lb.x >= 0 and h > new_lb.y >= 0 and not currentMap.getTileAt(new_lb).solid:
            self.pos.x = new_x
            self.pos.y = new_y

        # Extremities
        tile = currentMap.getTileAt(Vector(int(new_x), int(new_y+self.headOffset)))
        if (self.pos.x < 1 or self.pos.x + 1 > currentMap.getWidth() - 2 or
                    self.pos.y < 1 or self.pos.y + 1 > currentMap.getHeight() - 2) and \
                            tile.doorway is not None and tile.doorway is not 6:

            mapHolder.changeToMap(currentMap.neighbors[int(tile.doorway - 2)])
            if tile.doorway == 2:
                self.pos.y = mapHolder.getCurrentMap().height - 1-self.sideOffset-self.headOffset
            elif tile.doorway == 3:
                self.pos.x = 1
            elif tile.doorway == 4:
                self.pos.y = 0
            elif tile.doorway == 5:
                self.pos.x = mapHolder.getCurrentMap().width - 2
        # QG
        if currentMap.getTileAt(Vector(int(self.pos.x), int(self.pos.y+self.headOffset))).doorway == 6:
            self.hq_flag = True
            self.hqLocation = Vector(int(self.pos.x), int(self.pos.y+self.headOffset))

        self.icon = self.tileLoader.getPlayerAnimationFrame(self.direction, dt)

            # Check for a colision between the walls and a point
            # ~ def checkCollision(self, map, px, py):
            # ~ return (not map.getTileAt(int(px), int(py)).solid)

    def move(self, event, map, NPCManager):
        if event.type == KEYDOWN:
            if event.key == self.up:
                self.upPressed = True
                self.direction = Direction.UP
                self.speed_y = -1
            if event.key == self.down:
                self.downPressed = True
                self.direction = Direction.DOWN
                self.speed_y = 1
            if event.key == self.left:
                self.leftPressed = True
                self.direction = Direction.LEFT
                self.speed_x = -1
            if event.key == self.right:
                self.rightPressed = True
                self.direction = Direction.RIGHT
                self.speed_x = 1
            elif event.key == pygame.K_SPACE:
                NPC = NPCManager.getNPCAtLocation(self.pos)
                if NPC is not None:
                    self.NPCToInteractWith = NPC.id
                    self.interactionFlag = True
        elif event.type == KEYUP:
            if event.key == self.up:
                self.upPressed = False
                self.direction = Direction.IDLEN
                self.speed_y = 0 if not self.downPressed else 1
            if event.key == self.down:
                self.downPressed = False
                self.direction = Direction.IDLES
                self.speed_y = 0 if not self.upPressed else -1
            if event.key == self.left:
                self.leftPressed = False
                self.direction = Direction.IDLEE
                self.speed_x = 0 if not self.rightPressed else 1
            if event.key == self.right:
                self.rightPressed = False
                self.direction = Direction.IDLEW
                self.speed_x = 0 if not self.leftPressed else -1
        else:
            if self.direction == Direction.UP:
                self.direction = Direction.IDLEN
            elif self.direction == Direction.DOWN:
                self.direction = Direction.IDLES
            elif self.direction == Direction.LEFT:
                self.direction = Direction.IDLEW
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.IDLEE

    def finishInteraction(self):
        self.NPCToInteractWith = None
        self.interactionFlag = False
        self.stopMovement()

    def stopMovement(self):
        self.speed_x = 0
        self.speed_y = 0

        self.hq_flag = False
        self.hqLocation = None

        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False