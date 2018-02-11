from random import Random, randrange

import copy
import pygame

from Direction import Direction
from MobileUnit import MobileUnit
from Vector import Vector


class NPC(MobileUnit):
    def __init__(self, x, y, tileSize, animationController, scale):
        self.directionSignificanceDict = {Direction.DOWN: "NPCDown"}

        MobileUnit.__init__(self, x, y, tileSize, animationController, self.directionSignificanceDict, scale)
        self.target = None
        self.speed = Vector(0, 0)

    def updateNPC(self, dt, level):
        if self.target is None:
            self.target = self.getNewTarget(level)

        direction = self.target - self.pos
        direction.x = direction.x*(dt/1000)
        direction.y = direction.y*(dt/1000)

        tempRect = copy.deepcopy(self.rect)
        self.rect.x = self.pos.x*self.tileSize.x + direction.x * self.tileSize.x
        self.rect.y = self.pos.y*self.tileSize.y + direction.y * self.tileSize.y

        collision = pygame.sprite.spritecollideany(self, level.solidObjectGroup)
        if collision:
            self.target = None
            self.rect = tempRect
        else:
            self.pos = self.pos + direction
            self.speed = direction
            if abs(self.pos.x - self.target.x) < 1 and abs(self.pos.y - self.target.y) < 1:
                self.target = None

    def getNewTarget(self, level):
        counter = 0
        randomTarget = Vector(randrange(0, level.width), randrange(0, level.height))
        while level.getTileAt(randomTarget).solid and counter < 100:
            counter+=1
            randomTarget = Vector(randrange(0, level.width), randrange(0, level.height))
        return randomTarget
