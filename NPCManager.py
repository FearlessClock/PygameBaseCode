#Each map has a NPCManager
#NPC's are unique to each map and update only if the map is loaded.
from random import randrange

import pygame

from NPC import NPC


class NPCManager:
    def __init__(self, nmbrOfNPC, tileSize, tileLoader, level):
        self.npcHolder = pygame.sprite.Group()
        for i in range(nmbrOfNPC):
            x, y = randrange(1, level.width-1),randrange(1, level.height-1)
            while level.isObstacle(x, y):
                x, y = randrange(1, level.width-1),randrange(1, level.height-1)

            self.npcHolder.add(NPC(x,y, tileSize, tileLoader.getAnimationController("NPC"), randrange(1, 2)))

    def update(self, dt, level):
        for npc in self.npcHolder:
            npc.updateNPC(dt, level)

    def getNPCs(self):
        return self.npcHolder.sprites()