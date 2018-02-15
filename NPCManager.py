# Each map has a NPCManager
# NPC's are unique to each map and update only if the map is loaded.
from random import randrange

import pygame

from NPCFactory import NPCFactory, NPCType


class NPCManager:
    def __init__(self, nmbrOfNPC, tileSize, tileLoader, level):
        self.npcHolder = pygame.sprite.Group()
        self.npcFactory = NPCFactory(tileSize, tileLoader)
        for i in range(nmbrOfNPC):
            x, y = randrange(1, level.width - 1), randrange(1, level.height - 1)
            while level.isObstacle(x, y):
                x, y = randrange(1, level.width - 1), randrange(1, level.height - 1)

            self.npcHolder.add(self.npcFactory.createNPC(NPCType.FLY, x, y, "NPC", randrange(1, 2)))

    def update(self, dt, level, player):
        for npc in self.npcHolder:
            npc.updateNPC(dt, level, player)

    def getNPCs(self):
        return self.npcHolder.sprites()
