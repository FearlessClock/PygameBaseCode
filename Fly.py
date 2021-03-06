from random import randrange

import pygame
from pygame.rect import Rect

from Direction import Direction
from MobileUnit import MobileUnit
from Vector import Vector


class Fly(MobileUnit):
    """Fly creature that has to be caught by the player"""

    def __init__(self, id, x, y, tileSize, animationController, scale):
        self.directionSignificanceDict = {Direction.DOWN: "NPCDown", Direction.LEFT: "NPCLeft",
                                          Direction.RIGHT: "NPCRight",
                                          Direction.UP: "NPCUp"}  # Useless!! I could have used it directly in the dict! Idiot!

        MobileUnit.__init__(self, id, x, y, tileSize, animationController, self.directionSignificanceDict, scale)
        self.target = None
        self.speed = Vector(0, 0)
        self.closeness = 2

    def updateNPC(self, dt, level, player, enemies):
        """Find a random position, move in that direction while moving away from the player"""
        if self.target is None:
            self.target = self.getNewTarget(level)
        direction = self.target - self.pos
        oppPlayer = self.pos - player.pos
        oppPlayerMag = oppPlayer.length()

        if (oppPlayerMag < self.closeness):
            self.target = None
            oppPlayer.x *= self.closeness * 2 - oppPlayerMag
            oppPlayer.y *= self.closeness * 2 - oppPlayerMag
            direction = direction + oppPlayer

        direction.x = direction.x * (dt / 1000)
        direction.y = direction.y * (dt / 1000)

        tempRect = Rect(self.rect)
        self.rect.x = self.pos.x * self.tileSize.x + direction.x * self.tileSize.x
        self.rect.y = self.pos.y * self.tileSize.y + direction.y * self.tileSize.y

        collision = pygame.sprite.spritecollideany(self, level.solidObjectGroup)
        if collision:
            self.target = None
            self.rect = tempRect
        else:
            self.pos = self.pos + direction
            self.speed = direction
            if self.target is not None and abs(self.pos.x - self.target.x) < 1 and abs(self.pos.y - self.target.y) < 1:
                self.target = None
            self.getNPCDirection()
            self.updateNPCAnimation(dt)

    def updateNPCAnimation(self, dt):
        """Set the current animation to the correct frame and controller"""
        self.updateAnimation()
        self.image = self.currentAnimationFrame()
        self.stepCurrentAnimation(dt)

    def getNPCDirection(self):
        """Get the direction of the creature by looking at its speed"""
        x = self.speed.x
        y = self.speed.y

        if abs(x) > abs(y):
            y = 0
        else:
            x = 0

        if y > 0:
            self.direction = Direction.DOWN
        elif y < 0:
            self.direction = Direction.UP
        if x > 0:
            self.direction = Direction.RIGHT
        elif x < 0:
            self.direction = Direction.LEFT

        if x == 0 and y == 0:
            if self.direction == Direction.UP:
                self.direction = Direction.IDLE_UP
            elif self.direction == Direction.DOWN:
                self.direction = Direction.IDLE_DOWN
            elif self.direction == Direction.RIGHT:
                self.direction = Direction.IDLE_RIGHT
            elif self.direction == Direction.LEFT:
                self.direction = Direction.IDLE_LEFT

    def getNewTarget(self, level):
        """Get a new target for the movement"""
        counter = 0
        randomTarget = Vector(randrange(0, level.width), randrange(0, level.height))
        while level.getTileAt(randomTarget).solid and counter < 100:
            counter += 1
            randomTarget = Vector(randrange(0, level.width), randrange(0, level.height))
        return randomTarget
