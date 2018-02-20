import pygame

import UserEvents


def gameEnd(nmbrOfCreatures, nmbrOfCreaturesCaught):
    if nmbrOfCreatures <= nmbrOfCreaturesCaught:
        pygame.event.post(pygame.event.Event(UserEvents.WINSTATE))