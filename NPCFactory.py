from enum import Enum
from select import select

from Cricket import Cricket
from NPC import NPC


class NPCType(Enum):
    FLY = 1
    CRICKET = 2

class NPCFactory:
    def __init__(self, tileSize, tileLoader):
        self.tileSize = tileSize
        self.tileLoader = tileLoader

    def createNPC(self, id, npcType, x,y, animationControllerName, scale):
        if npcType == NPCType.FLY:
            return NPC(id, x, y, self.tileSize, self.tileLoader.getAnimationController(animationControllerName), scale)
        elif npcType == NPCType.CRICKET:
            return Cricket(id, x, y, self.tileSize, self.tileLoader.getAnimationController(animationControllerName), scale)
        else:
            return None
