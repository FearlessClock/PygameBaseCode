# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:14:25 2017

@author: piete
"""
import os
import time as Time

import pygame

from GameStates import GameStates
from Player import Player
# Size of the screen
from StartMenu import StartUpMenu
from Window import Window


# Class with all the game loop functions and information
class Gameloop:
    def __init__(self, gameName, screenSize, tileSize):
        self.width = screenSize.x
        self.height = screenSize.y
        self.TILE_SIZE = tileSize
        self.gameState = GameStates.STARTMENU

        # Initialise screen
        pygame.font.init()

        self.font_renderer = pygame.font.Font(os.path.join("fonts", 'Millennium-Regular_0.ttf'), 24)
        self.window = Window(screenSize, gameName, self.TILE_SIZE, self.font_renderer)
        self.startMenu = StartUpMenu()
        self.window.addScreenToRender(self.startMenu, "StartMenu")
        pygame.mixer.init()

        # Fill background
        self.window.clearScreen()

        # Init the player
        #self.player = Player(2, 1 + 0.2, window.tileLoader, window.TILE_SIZE)

        # window.drawScreen(mapHolder, player, NPCManagerIns)
        self.clock = pygame.time.Clock()
        time = 0

        pygame.mixer.init()
        # ~ default_font = pygame.font.get_default_font()
        self.window.drawScreen("StartMenu")

    def setMusic(self, filename):
        pygame.mixer.music.fadeout(100)  # Avoid music change being too sudden!
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)

    def changeGameLoopStateToGAME(self):
        self.gameState = GameStates.GAME

    def changeGameLoopStateToMenu(self):
        self.gameState = GameStates.MENU  # Ingame menu

    def changeGameLoopStateToStartMenu(self):
        self.gameState = GameStates.STARTMENU

    def quitGame(self):
        pygame.quit()
        exit(0)

    def StartMenuState(self):
        self.startMenu.handleInput(self.getHandleInputs())
        self.window.drawScreen("StartMenu")
        return True

    def MenuState(self):
        return True

    def GameState(self):

        return True

    def getHandleInputs(self):
        return pygame.event.get(pygame.KEYDOWN)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.USEREVENT:
                print(event.code)
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pygame.event.post(event)


    def startLoop(self):
        """The main function that runs the whole game."""

        # Game loop
        while pygame.display.get_init():
            if self.gameState == GameStates.GAME:
                self.RPGState()
            elif self.gameState == GameStates.MENU:
                self.MenuState()
            elif self.gameState == GameStates.STARTMENU:
                self.StartMenuState()
            self.handleEvents()
            pygame.event.pump()

            try:
                pygame.display.update()
            except:
                print("Error")
