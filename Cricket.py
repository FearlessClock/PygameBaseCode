import math
from random import random

import pygame
from pygame.rect import Rect

from Direction import Direction
from MobileUnit import MobileUnit
from Vector import Vector


class Cricket(MobileUnit):
    def __init__(self, id, x, y, tileSize, animationController, scale):
        self.directionSignificanceDict = {Direction.DOWN: "NPCDown", Direction.LEFT: "NPCLeft",
                                          Direction.RIGHT: "NPCRight"}
        MobileUnit.__init__(self, id, x, y, tileSize, animationController, self.directionSignificanceDict, scale)
        self.closeness = 2
        self.maxSpeed = 3
        self.velocity = Vector(1, 0)
        self.uniqueRandom = random()

    def updateNPC(self, dt, level, player, enemies):
        deg = random() * 360
        angle = math.radians(deg)
        radius = 0.5
        randomCircleVec = Vector(radius * math.cos(angle), radius * math.sin(angle))
        distanceToPlayerSqr = self.pos.distance_squared_to(player.pos)
        # Make the bug run away from the player
        if distanceToPlayerSqr < 6:
            fromPlayer = self.pos - player.pos
            if fromPlayer.length() != 0:
                fromPlayer.normalize_ip()
            fromPlayer.x /= 2
            fromPlayer.y /= 2
        else:
            fromPlayer = Vector(0, 0)

        collisions = pygame.sprite.spritecollide(self, enemies, False)
        pushAwayFrom = Vector(0,0)
        if len(collisions) > 1:
            for collision in collisions:
                if collision.id != self.id:
                    pushAwayFrom += self.pos - collision.pos
            pushAwayFrom.x = (pushAwayFrom.x / (len(collisions)-1))
            pushAwayFrom.y = (pushAwayFrom.y / (len(collisions)-1))

        self.velocity = self.velocity + randomCircleVec + fromPlayer + pushAwayFrom
        temp = Rect(self.rect)
        self.velocity.normalize_ip()
        self.velocity *= self.maxSpeed
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        # Change the rect to get the collision to work
        collision = pygame.sprite.spritecollideany(self, level.solidObjectGroup)
        if collision:
            # Don't move
            self.rect = temp
            self.velocity = self.velocity * -1
        else:
            self.pos.x = self.rect.x / self.tileSize.x
            self.pos.y = self.rect.y / self.tileSize.y
            # Move
            self.getNPCDirection()
            self.updateNPCAnimation(dt)

    def updateNPCAnimation(self, dt):
        self.updateAnimation()
        self.image = self.currentAnimationFrame()
        self.stepCurrentAnimation(dt)

    def getNPCDirection(self):
        x = self.velocity.x
        y = self.velocity.y

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
