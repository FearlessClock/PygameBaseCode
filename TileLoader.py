import os
import pygame

from Direction import Direction
from Spritesheet import SpriteSheet
from Vector import Vector


class TileLoader:
    def __init__(self, tileSize, screenSize):
        spritesheet = SpriteSheet(os.path.join('images', 'TilesSpriteSheet.png'))
        buttonSheet = SpriteSheet(os.path.join('images', 'buttons.png'))
        statBarSheet = SpriteSheet(os.path.join('images', 'statBarSheet.png'))

        walkingSAnimationG = SpriteSheet(os.path.join('images', 'Gourou', 'marcheFaceG.png'))
        walkingNAnimationG = SpriteSheet(os.path.join('images', 'Gourou','marcheBackG.png'))
        walkingSideAnimationG = SpriteSheet(os.path.join('images', 'Gourou','marcheSideG.png'))
        youpiAnimationG = SpriteSheet(os.path.join('images', 'Gourou','youpiG.png'))
        unhappyAnimationG = SpriteSheet(os.path.join('images', 'Gourou','colèreG.png'))
        neutralAnimationG = SpriteSheet(os.path.join('images', 'Gourou','neutreG.png'))
        idleAnimationNG = SpriteSheet(os.path.join('images', 'Gourou','idleBackG.png'))
        idleAnimationSideG = SpriteSheet(os.path.join('images', 'Gourou','idleSideG.png'))
        idleAnimationSG = SpriteSheet(os.path.join('images', 'Gourou','idleFaceG.png'))
        talkAnimationG = SpriteSheet(os.path.join('images', 'Gourou','blablaG.png'))

        walkingSAnimationNPC = SpriteSheet(os.path.join('images', 'People', 'marcheFace.png'))
        walkingNAnimationNPC = SpriteSheet(os.path.join('images', 'People','marcheBack.png'))
        walkingSideAnimationNPC = SpriteSheet(os.path.join('images', 'People','marcheSide.png'))
        youpiAnimationNPC = SpriteSheet(os.path.join('images', 'People','youpi.png'))
        unhappyAnimationNPC = SpriteSheet(os.path.join('images', 'People','colère.png'))
        neutralAnimationNPC = SpriteSheet(os.path.join('images', 'People','neutre.png'))
        idleAnimationNNPC = SpriteSheet(os.path.join('images', 'People','idleBack.png'))
        idleAnimationSideNPC = SpriteSheet(os.path.join('images', 'People','idleSide.png'))
        idleAnimationSNPC = SpriteSheet(os.path.join('images', 'People','idleFace.png'))
        talkAnimationNPC = SpriteSheet(os.path.join('images', 'People','blabla.png'))

        self.screenSize = screenSize
        self.tileSize = tileSize
        self.images = spritesheet.load_strip((0, 0, 80, 80), 10, Vector(80, 80))
        self.buttonIcons = buttonSheet.load_strip((0, 0, 168, 56), 3, Vector(168, 56), -1)

        self.walkingSG = walkingSAnimationG.load_strip((0, 0, 60, 120), 8, Vector(60, 120), -1)
        self.walkingNG = walkingNAnimationG.load_strip((0, 0, 60, 120), 8, Vector(60, 120), -1)
        self.walkingSideG = walkingSideAnimationG.load_strip((0, 0, 60, 120), 8, Vector(60, 120), -1)
        self.youpiG = youpiAnimationG.load_strip((0, 0, 60, 120), 10, Vector(60, 120), -1)
        self.unhappyG = unhappyAnimationG.load_strip((0, 0, 60, 120), 10, Vector(60, 120), -1)
        self.neutralG = neutralAnimationG.load_strip((0, 0, 60, 120), 10, Vector(60, 120), -1)
        self.idleNG = idleAnimationNG.load_strip((0, 0, 60, 120), 7, Vector(60, 120), -1)
        self.idleSideG = idleAnimationSideG.load_strip((0, 0, 60, 120), 7, Vector(60, 120), -1)
        self.idleSG = idleAnimationSG.load_strip((0, 0, 60, 120), 7, Vector(60, 120), -1)
        self.talkG = talkAnimationG.load_strip((0, 0, 60, 120), 5, Vector(60, 120), -1)

        self.walkingSNPC = walkingSAnimationNPC.load_strip((0, 0, 60, 92), 8, Vector(60, 92), -1)
        self.walkingNNPC = walkingNAnimationNPC.load_strip((0, 0, 60, 92), 8, Vector(60, 92), -1)
        self.walkingSideNPC = walkingSideAnimationNPC.load_strip((0, 0, 60, 92), 8, Vector(60, 92), -1)
        self.youpiNPC = youpiAnimationNPC.load_strip((0, 0, 60, 92), 10, Vector(60, 92), -1)
        self.unhappyNPC = unhappyAnimationNPC.load_strip((0, 0, 60, 92), 10, Vector(60, 92), -1)
        self.neutralNPC = neutralAnimationNPC.load_strip((0, 0, 60, 92), 10, Vector(60, 92), -1)
        self.idleNNPC = idleAnimationNNPC.load_strip((0, 0, 60, 92), 7, Vector(60, 92), -1)
        self.idleSideNPC = idleAnimationSideNPC.load_strip((0, 0, 60, 92), 7, Vector(60, 92), -1)
        self.idleSNPC = idleAnimationSNPC.load_strip((0, 0, 60, 92), 7, Vector(60, 92), -1)
        self.talkNPC = talkAnimationNPC.load_strip((0, 0, 60, 92), 5, Vector(60, 92), -1)

        self.statBarIcons = statBarSheet.load_strip((0, 0, 640, 80), 3, Vector(640, 80))
        self.lastAnimation = None
        self.playerKeyframe = 0
        self.time = 0
        self.animationTime = 200

        self.lastNPCAnimation = None
        self.NPCKeyframe = 0
        self.NPCTime = 0

        self.wall = self.images[2]  # oadImage(os.path.join('images', 'wall.png'), tileSize)
        self.grass = self.images[1]  # loadImage(os.path.join('images', 'floor.png'), tileSize)
        self.cement = self.images[0]
        self.doorway = self.images[0]  # loadImage(os.path.join('images', 'doorway.png'), tileSize)

        self.cultistLogo = loadImage(os.path.join('images', 'Cultists.png'), tileSize, 1)
        self.moneyLogo = loadImage(os.path.join('images', 'money.png'), tileSize, 1)
        self.reputationLogo = loadImage(os.path.join('images', 'reputation.png'), tileSize, 1)
        self.logoFiller = loadImage(os.path.join('images', 'statFiller.png'), Vector(104, 80), 1)

        self.HQBackground = loadImage(os.path.join('images', 'HQ.png'), Vector(screenSize.x, screenSize.y), 1)
        self.blablaBackground = loadImage(os.path.join('images', 'blablaMockup.png'), Vector(screenSize.x, screenSize.y), 1)

        self.nonSelectedButton = loadImage(os.path.join('images', 'button.png'), Vector(100, 30), 1)
        self.selectedButton = loadImage(os.path.join('images', 'buttonSelected.png'), Vector(100, 30), 1)

        self.hourglass = loadImage(os.path.join('images', 'hourglass.png'), Vector(104, 80), 1, True)

        self.currentAnimationLength = 0

    def getTile(self, ID):
        return self.images[ID]

    def getButton(self, ID):
        return self.buttonIcons[ID]

    def getNPCAnimationLength(self):
        return self.currentAnimationLength

    def getPlayerAnimationFrame(self, direction, dt):
        if direction is Direction.DOWN:
            if self.lastAnimation is not Direction.DOWN:
                self.lastAnimation = Direction.DOWN
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.walkingSG):
                self.playerKeyframe = 0
            res = self.walkingSG[self.playerKeyframe]
            self.time += dt
            if self.time > self.animationTime:
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.UP:
            if self.lastAnimation is not Direction.UP:
                self.lastAnimation = Direction.UP
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.walkingNG):
                self.playerKeyframe = 0
            res = self.walkingNG[self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.LEFT:
            if self.lastAnimation is not Direction.LEFT:
                self.lastAnimation = Direction.LEFT
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.walkingSideG):
                self.playerKeyframe = 0
            res = self.walkingSideG[len(self.walkingSideG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.RIGHT:
            if self.lastAnimation is not Direction.RIGHT:
                self.lastAnimation = Direction.RIGHT
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.walkingSideG):
                self.playerKeyframe = 0
            res = self.walkingSideG[len(self.walkingSideG) - 1 - self.playerKeyframe]
            res = pygame.transform.flip(res, True, False)
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.YOUPI:
            if self.lastAnimation is not Direction.YOUPI:
                self.lastAnimation = Direction.YOUPI
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.youpiG):
                self.playerKeyframe = 0
            res = self.youpiG[len(self.youpiG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.UNHAPPY:
            if self.lastAnimation is not Direction.UNHAPPY:
                self.lastAnimation = Direction.UNHAPPY
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.unhappyG):
                self.playerKeyframe = 0
            res = self.unhappyG[len(self.unhappyG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.IDLEN:
            if self.lastAnimation is not Direction.IDLEN:
                self.lastAnimation = Direction.IDLEN
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.idleNG):
                self.playerKeyframe = 0
            res = self.idleNG[len(self.idleNG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.IDLEE:
            if self.lastAnimation is not Direction.IDLEE:
                self.lastAnimation = Direction.IDLEE
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.idleSideG):
                self.playerKeyframe = 0
            res = self.idleSideG[len(self.idleSideG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.IDLES:
            if self.lastAnimation is not Direction.IDLES:
                self.lastAnimation = Direction.IDLES
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.idleSideG):
                self.playerKeyframe = 0
            res = self.idleSideG[len(self.idleSideG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.IDLEW:
            if self.lastAnimation is not Direction.IDLEW:
                self.lastAnimation = Direction.IDLEW
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.idleSideG):
                self.playerKeyframe = 0
            res = self.idleSideG[self.playerKeyframe]
            res = pygame.transform.flip(res, True, False)
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.TALKING:
            if self.lastAnimation is not Direction.TALKING:
                self.lastAnimation = Direction.TALKING
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.talkG):
                self.playerKeyframe = 0
            res = self.talkG[self.playerKeyframe]
            self.time += dt
            if self.time > self.animationTime:
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.NEUTRAL:
            if self.lastAnimation is not Direction.NEUTRAL:
                self.lastAnimation = Direction.NEUTRAL
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.neutralG):
                self.playerKeyframe = 0
            res = self.neutralG[len(self.neutralG) - 1 - self.playerKeyframe]
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res
        elif direction is Direction.PICKUPHAT:
            if self.lastAnimation is not Direction.PICKUPHAT:
                self.lastAnimation = Direction.PICKUPHAT
                self.playerKeyframe = 0
            if self.playerKeyframe >= len(self.youpiG):
                self.playerKeyframe = 0
            res = self.youpiG[len(self.youpiG) - 1 - self.playerKeyframe]
            res = pygame.transform.flip(res, True, False)
            self.time += dt
            if (self.time > self.animationTime):
                self.time = 0
                self.playerKeyframe = self.playerKeyframe + 1
            return res

    def getNPCAnimationFrame(self, direction, dt):
        if direction is Direction.DOWN:
            if self.lastNPCAnimation is not Direction.DOWN:
                self.lastNPCAnimation = Direction.DOWN
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.walkingSNPC)
            if self.NPCKeyframe >= len(self.walkingSNPC):
                self.NPCKeyframe = 0
            res = self.walkingSNPC[self.NPCKeyframe]
            self.NPCTime += dt
            if self.NPCTime > self.animationTime:
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.UP:
            if self.lastNPCAnimation is not Direction.UP:
                self.lastNPCAnimation = Direction.UP
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.walkingNNPC)
            if self.NPCKeyframe >= len(self.walkingNNPC):
                self.NPCKeyframe = 0
            res = self.walkingNNPC[self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.LEFT:
            if self.lastNPCAnimation is not Direction.LEFT:
                self.lastNPCAnimation = Direction.LEFT
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.walkingSideNPC)
            if self.NPCKeyframe >= len(self.walkingSideNPC):
                self.NPCKeyframe = 0
            res = self.walkingSideNPC[len(self.walkingSideNPC) - 1 - self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.RIGHT:
            if self.lastNPCAnimation is not Direction.RIGHT:
                self.lastNPCAnimation = Direction.RIGHT
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.walkingSideNPC)
            if self.NPCKeyframe >= len(self.walkingSideNPC):
                self.NPCKeyframe = 0
            res = self.walkingSideNPC[len(self.walkingSideNPC) - 1 - self.NPCKeyframe]
            res = pygame.transform.flip(res, True, False)
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.YOUPI:
            if self.lastNPCAnimation is not Direction.YOUPI:
                self.lastNPCAnimation = Direction.YOUPI
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.youpiNPC)
            if self.NPCKeyframe >= len(self.youpiNPC):
                self.NPCKeyframe = 0
            res = self.youpiNPC[len(self.youpiNPC) - 1 - self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.UNHAPPY:
            if self.lastNPCAnimation is not Direction.UNHAPPY:
                self.lastNPCAnimation = Direction.UNHAPPY
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.unhappyNPC)
            if self.NPCKeyframe >= len(self.unhappyNPC):
                self.NPCKeyframe = 0
            res = self.unhappyNPC[len(self.unhappyNPC) - 1 - self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.NEUTRAL:
            if self.lastNPCAnimation is not Direction.NEUTRAL:
                self.lastNPCAnimation = Direction.NEUTRAL
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.neutralNPC)
            if self.NPCKeyframe >= len(self.neutralNPC):
                self.NPCKeyframe = 0
            res = self.neutralNPC[len(self.neutralNPC) - 1 - self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.IDLEN:
            if self.lastNPCAnimation is not Direction.IDLEN:
                self.lastNPCAnimation = Direction.IDLEN
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.idleNNPC)
            if self.NPCKeyframe >= len(self.idleNNPC):
                self.NPCKeyframe = 0
            res = self.idleNNPC[self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.IDLEE:
            if self.lastNPCAnimation is not Direction.IDLEE:
                self.lastNPCAnimation = Direction.IDLEE
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.idleSideNPC)
            if self.NPCKeyframe >= len(self.idleSideNPC):
                self.NPCKeyframe = 0
            res = self.idleSideNPC[self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.IDLES:
            if self.lastNPCAnimation is not Direction.IDLES:
                self.lastNPCAnimation = Direction.IDLES
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.idleSNPC)
            if self.NPCKeyframe >= len(self.idleSNPC):
                self.NPCKeyframe = 0
            res = self.idleSNPC[self.NPCKeyframe]
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.IDLEW:
            if self.lastNPCAnimation is not Direction.IDLEW:
                self.lastNPCAnimation = Direction.IDLEW
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.idleSideNPC)
            if self.NPCKeyframe >= len(self.idleSideNPC):
                self.NPCKeyframe = 0
            res = self.idleSideNPC[self.NPCKeyframe]
            res = pygame.transform.flip(res, True, False)
            self.NPCTime += dt
            if (self.NPCTime > self.animationTime):
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res
        elif direction is Direction.TALKING:
            if self.lastNPCAnimation is not Direction.TALKING:
                self.lastNPCAnimation = Direction.TALKING
                self.NPCKeyframe = 0
            self.currentAnimationLength = len(self.talkNPC)
            if self.NPCKeyframe >= len(self.talkNPC):
                self.NPCKeyframe = 0
            res = self.talkNPC[self.NPCKeyframe]
            self.NPCTime += dt
            if self.NPCTime > self.animationTime:
                self.NPCTime = 0
                self.NPCKeyframe = self.NPCKeyframe + 1
            return res

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
