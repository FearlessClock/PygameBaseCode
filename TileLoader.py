import os
import pygame

from Direction import Direction
from Spritesheet import SpriteSheet
from Vector import Vector


class TileLoader:
    def __init__(self, tileSize, screenSize):
        self.screenSize = screenSize
        self.tileSize = tileSize

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

    def getImageByName(self, imageName, row, colume):
        return self.loadedImages.get(imageName)[row][colume]

    def getImageStripByName(self, imageName, row):
        return self.loadedImages.get(imageName)[row]

    def getImageGridByName(self, imageName):
        return self.loadedImages.get(imageName)

    def getTile(self, ID):
        return self.images[ID]

    def getButton(self, ID):
        return self.buttonIcons[ID]

    def getNPCAnimationLength(self):
        return self.currentAnimationLength

    def getStatBar(self, id):
        return self.statBarIcons[id]

    def loadPlayerImages(self, scale):
        self.image_up = loadImage(os.path.join('images', 'playerUp.png'), self.tileSize, scale)
        self.image_down = loadImage(os.path.join('images', 'playerDown.png'), self.tileSize, scale)
        self.image_left = loadImage(os.path.join('images', 'playerLeft.png'), self.tileSize, scale)
        self.image_right = loadImage(os.path.join('images', 'playerRight.png'), self.tileSize, scale)


def loadImage(filename, tileSize, scale, colorKey=None):
    image = pygame.image.load_extended(filename)
    if colorKey is not None:
        image = image.convert()
        image.set_colorkey(image.get_at((0, 0)), pygame.RLEACCEL)
    return pygame.transform.scale(image, (int(tileSize.x * scale), int(tileSize.y * scale)))
