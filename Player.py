import pygame
from pygame.locals import *

import UserEvents
from Direction import Direction
from MobileUnit import MobileUnit
from NetWeapon import Net
from Vector import Vector

UP = pygame.K_UP
DOWN = pygame.K_DOWN
RIGHT = pygame.K_RIGHT
LEFT = pygame.K_LEFT


class Player(MobileUnit):
    """Structure to store the player information"""

    def __init__(self, x, y, tileLoader, tileSize, imageCollisionOffset):
        self.size = 0.5
        self.directionSignificanceDict = {Direction.UP: "playerUp", Direction.DOWN: "playerDown",
                                          Direction.LEFT: "playerLeft", Direction.RIGHT: "playerRight",
                                          Direction.IDLE_UP: "playerIdleUp", Direction.IDLE_DOWN: "playerIdleDown",
                                          Direction.IDLE_LEFT: "playerIdleLeft",
                                          Direction.IDLE_RIGHT: "playerIdleRight"}
        MobileUnit.__init__(self, 0, x, y, tileSize, tileLoader.getAnimationController("player"),
                            self.directionSignificanceDict, self.size)
        self.imageCollisionOffset = imageCollisionOffset
        self.tileSize = tileSize

        self.speed = 1.5

        self.speedX = 0
        self.speedY = 0

        self.movementSpeed = 1

        # Put the midpoint in the middle bottom of the image
        self.collisionOffset = Vector((self.image.get_width() / 2) / self.tileSize.x,
                                      (self.image.get_height()) / self.tileSize.y)

        self.tileLoader = tileLoader

        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False

        self.net = Net(self.tileLoader.getAnimationController("netAnimation"), self.tileSize)
        self.attack = False

        self.score = 0

    def update(self, dt, mapHolder):
        # pos.x/y are in "world units"
        newX = self.pos.x + self.speedX * dt / 60 / 5 * self.speed
        newY = self.pos.y + self.speedY * dt / 60 / 5 * self.speed
        currentMap = mapHolder.getCurrentMap()
        tempRectHolder = Rect(self.rect)
        res = Rect(self.rect)
        self.rect[0] = newX * self.tileSize.x + self.imageCollisionOffset.x
        self.rect[2] -= self.imageCollisionOffset.x * 2
        self.rect[1] += self.imageCollisionOffset.y
        self.rect[3] -= self.imageCollisionOffset.y * 2
        collision = pygame.sprite.spritecollideany(self, currentMap.solidObjectGroup)

        if collision is None:
            self.pos.x = newX
            res[0] = self.rect[0]

        self.rect = tempRectHolder
        self.rect[1] = newY * self.tileSize.y + self.imageCollisionOffset.y
        self.rect[3] -= self.imageCollisionOffset.y * 2
        self.rect[0] += self.imageCollisionOffset.x
        self.rect[2] -= self.imageCollisionOffset.x * 2
        collision = pygame.sprite.spritecollideany(self, currentMap.solidObjectGroup)

        if collision is None:
            self.pos.y = newY
            res[1] = newY * self.tileSize.y
        self.rect = res

        # Extremities
        tile = currentMap.getTileAt(Vector(int(newX + self.collisionOffset.x), int(newY + self.collisionOffset.y)))
        if tile.doorway is not None and tile.doorway is not 0:
            mapHolder.changeToMap(currentMap.neighbors[int(tile.doorway - 1)])
            if tile.doorway == 1:
                self.pos.y = (mapHolder.getCurrentMap().height - 2)
                if self.pos.x > mapHolder.getCurrentMap().width:
                    empty = self.getFirstEmptyFromMax(mapHolder.getCurrentMap(), False, self.pos.x, self.pos.y)
                    if empty is not None:
                        self.pos.x = empty
                    else:
                        self.pos.x = 2
            elif tile.doorway == 2:
                self.pos.x = 1
                if self.pos.y > mapHolder.getCurrentMap().height:
                    empty = self.getFirstEmptyFromMax(mapHolder.getCurrentMap(), True, self.pos.x, self.pos.y)
                    if empty is not None:
                        self.pos.y = empty
                    else:
                        self.pos.y = 0
            elif tile.doorway == 3:
                self.pos.y = 1
                if self.pos.x > mapHolder.getCurrentMap().width:
                    empty = self.getFirstEmptyFromMax(mapHolder.getCurrentMap(), False, self.pos.x, self.pos.y)
                    if empty is not None:
                        self.pos.x = empty
                    else:
                        self.pos.x = 2
            elif tile.doorway == 4:
                self.pos.x = mapHolder.getCurrentMap().width - 2
                if self.pos.y > mapHolder.getCurrentMap().height:
                    empty = self.getFirstEmptyFromMax(mapHolder.getCurrentMap(), True, self.pos.x, self.pos.y)
                    if empty is not None:
                        self.pos.y = empty
                    else:
                        self.pos.y = 0

        self.updateAnimation()
        if self.attack:
            self.net.spawnWeapon(self.direction, self.pos)
            collision = pygame.sprite.spritecollide(self.net, currentMap.NPCManager.npcHolder, True)
            self.score += len(collision)
        self.net.updateAnimation(dt)
        self.image = self.currentAnimationFrame()
        self.stepCurrentAnimation(dt)

    def move(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == UP:
                    self.upPressed = True
                    # self.direction = Direction.UP
                    self.speedY = -self.movementSpeed
                elif event.key == DOWN:
                    self.downPressed = True
                    # self.direction = Direction.DOWN
                    self.speedY = self.movementSpeed
                elif event.key == LEFT:
                    self.leftPressed = True
                    # self.direction = Direction.LEFT
                    self.speedX = -self.movementSpeed
                elif event.key == RIGHT:
                    self.rightPressed = True
                    # self.direction = Direction.RIGHT
                    self.speedX = self.movementSpeed
                elif event.key == K_SPACE:
                    # Create sprite and spawn in world.
                    # Check for collisions with flies
                    # Remove flies from game
                    self.attack = True
                    self.net.spawnWeapon(self.direction, self.pos)
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(UserEvents.RESUMEGAME))
                else:
                    pygame.event.post(event)
            elif event.type == KEYUP:
                if event.key == UP:
                    self.upPressed = False
                    if not self.downPressed:
                        # self.direction = Direction.IDLE_UP
                        self.speedY = 0
                    else:
                        self.speedY = self.movementSpeed
                elif event.key == DOWN:
                    self.downPressed = False
                    if not self.upPressed:
                        # self.direction = Direction.IDLE_DOWN
                        self.speedY = 0
                    else:
                        self.speedY = -self.movementSpeed
                elif event.key == LEFT:
                    self.leftPressed = False
                    if not self.rightPressed:
                        # self.direction = Direction.IDLE_LEFT
                        self.speedX = 0
                    else:
                        self.speedX = self.movementSpeed
                elif event.key == RIGHT:
                    self.rightPressed = False
                    if not self.leftPressed:
                        # self.direction = Direction.IDLE_RIGHT
                        self.speedX = 0
                    else:
                        self.speedX = -self.movementSpeed
                elif event.key == K_SPACE:
                    self.attack = False
                    self.net.despawn()
                else:
                    pygame.event.post(event)

            else:
                pygame.event.post(event)

        self.getPlayerDirection()

    def getPlayerDirection(self):
        if self.speedY > 0:
            self.direction = Direction.DOWN
        elif self.speedY < 0:
            self.direction = Direction.UP
        if self.speedX > 0:
            self.direction = Direction.RIGHT
        elif self.speedX < 0:
            self.direction = Direction.LEFT
        if self.speedX == 0 and self.speedY == 0:
            if self.direction == Direction.UP:
                self.direction = Direction.IDLE_UP
            elif self.direction == Direction.DOWN:
                self.direction = Direction.IDLE_DOWN
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.IDLE_RIGHT
            elif self.direction == Direction.LEFT:
                self.direction = Direction.IDLE_LEFT

    def stopMovement(self):
        self.speedX = 0
        self.speedY = 0

        self.upPressed = False
        self.downPressed = False
        self.leftPressed = False
        self.rightPressed = False

    def getFirstEmptyFromMax(self, level, vertical, x, y):
        xMax = level.width - 1
        yMax = level.height - 1
        if vertical:
            for i in range(level.height - 1):
                if not level.isObstacle(x-1, yMax - i):
                    return yMax - i
        else:
            for i in range(level.width - 1):
                if not level.isObstacle(xMax - i, y-1):
                    return xMax - i
        return None
