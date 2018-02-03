import os
import pygame

from Direction import Direction
from Spritesheet import SpriteSheet
from Vector import Vector


class TileLoader:
    def __init__(self, tileSize, screenSize):
        self.screenSize = screenSize
        self.tileSize = tileSize

        self.loadedAnimations = {}
        self.loadedImages = {}
        self.lastAnimation = None
        self.playerKeyframe = 0
        self.time = 0
        self.animationTime = 200

        self.lastNPCAnimation = None
        self.NPCKeyframe = 0
        self.NPCTime = 0
        self.currentAnimationLength = 0

    def addSpriteSheet(self, spriteName, filename, realSpriteSize, scaledSpriteSize, rowCount, columeCount):
        spriteSheet = SpriteSheet(filename)
        self.loadedImages.update({spriteName: spriteSheet.load_grid((0, 0, realSpriteSize.x, realSpriteSize.y), columeCount, rowCount, Vector(scaledSpriteSize.x, scaledSpriteSize.y), (255,0,255))})

    def addAnimation(self, animationName, animationController):
        self.loadedAnimations.update({animationName: animationController})

    def getAnimationController(self, animationName):
        return self.loadedAnimations.get(animationName)

    def getAnimationFrameByName(self, animationName):
        return self.loadedAnimations.get(animationName).getCurrentAnimationFrame()

    def setAnimationForNameToName(self, animationControllerName, animationName):
        self.loadedAnimations.get(animationControllerName).changeCurrentAnimationTo(animationName)

    def getImageByName(self, imageName, row, colume):
        return self.loadedImages.get(imageName)[row][colume]

    def getImageStripByName(self, imageName, row):
        return self.loadedImages.get(imageName)[row]

    def getImageGridByName(self, imageName):
        return self.loadedImages.get(imageName)