from enum import Enum


class GameStates(Enum):
    """The different states of the game"""
    STARTMENU = 1
    GAME = 2
    MENU = 3
    WINSCREEN = 4
