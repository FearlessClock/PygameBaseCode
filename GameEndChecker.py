import pygame

import UserEvents


def gameEnd(nmbrOfCreatures, nmbrOfCreaturesCaught):
    """Check if the game is over"""
    if nmbrOfCreatures <= nmbrOfCreaturesCaught:
        pygame.event.post(pygame.event.Event(UserEvents.WINSTATE))