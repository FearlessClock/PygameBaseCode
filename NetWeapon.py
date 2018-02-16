import pygame
from pygame.rect import Rect

from Direction import Direction
from Vector import Vector


class Net(pygame.sprite.Sprite):
    def __init__(self, animationController, tileSize):
        pygame.sprite.Sprite.__init__(self)
        self.animationController = animationController
        self.animationController.changeCurrentAnimationTo(Direction.UP)
        self.image = self.animationController.getCurrentAnimationFrame()
        self.tileSize = tileSize
        self.pos = Vector(-1, -1)
        self.rect = Rect(-1, -1, self.tileSize.x/2, self.tileSize.y/2)
        self.hitPos = Vector(0, 0)
        self.netDirection = Direction.UP

    def spawnWeapon(self, direction, position):
        offset = 0.4
        if direction == Direction.UP or direction == Direction.IDLE_UP:
            self.hitPos = position + Vector(0, -offset)
            if self.netDirection is not Direction.UP:
                self.netDirection = Direction.UP
                self.animationController.changeCurrentAnimationTo(Direction.UP)

        elif direction == Direction.DOWN or direction == Direction.IDLE_DOWN:
            self.hitPos = position + Vector(-offset, offset*1.5)
            if self.netDirection is not Direction.DOWN:
                self.netDirection = Direction.DOWN
                self.animationController.changeCurrentAnimationTo(Direction.DOWN)

        elif direction == Direction.LEFT or direction == Direction.IDLE_LEFT:
            self.hitPos = position + Vector(-offset*1.5, 0)
            if self.netDirection is not Direction.LEFT:
                self.netDirection = Direction.LEFT
                self.animationController.changeCurrentAnimationTo(Direction.LEFT)

        elif direction == Direction.RIGHT or direction == Direction.IDLE_RIGHT:
            self.hitPos = position + Vector(offset*0.8, offset)
            if self.netDirection is not Direction.RIGHT:
                self.netDirection = Direction.RIGHT
                self.animationController.changeCurrentAnimationTo(Direction.RIGHT)

    def despawn(self):
        self.hitPos = Vector(-1, -1)
        self.rect.x = -1
        self.rect.y = -1

    def updateAnimation(self, dt):
        self.animationController.stepCurrentAnimation(dt)
        self.image = self.animationController.getCurrentAnimationFrame()

    def draw(self, surface_blit, screenRect):
        self.pos = self.hitPos
        self.rect.x = self.hitPos.x * self.tileSize.x
        self.rect.y = self.hitPos.y * self.tileSize.y
        surface_blit(self.image, (self.pos.x*self.tileSize.x-screenRect.x, self.pos.y*self.tileSize.y-screenRect.y))