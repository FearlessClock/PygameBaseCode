from enum import Enum
from select import select

from NPC import NPC


class NPCType(Enum):
    FLY = 1

class NPCFactory:
    def __init__(self, tileSize, tileLoader):
        self.tileSize = tileSize
        self.tileLoader = tileLoader

    def createNPC(self, npcType, x,y, animationControllerName, scale):
        if npcType == NPCType.FLY:
            return NPC(x, y, self.tileSize, self.tileLoader.getAnimationController(animationControllerName), scale)
        else:
            return None
