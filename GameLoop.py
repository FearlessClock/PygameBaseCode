# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:14:25 2017

@author: piete
"""
import os

import pygame

from GameStates import GameStates
# Size of the screen
from StartMenu import StartUpMenu
import UserEvents
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
        self.startMenu = StartUpMenu(self.window.tileLoader)
        self.window.addScreenToRender(self.startMenu, "StartMenu")
        pygame.mixer.init()

        # Fill background
        self.window.clearScreen()

        # Dictionary to hold all the states and their corresponding Game states
        self.stateFunctionDict = {}
        self.addStateFunction(GameStates.STARTMENU, self.StartMenuState)
        self.addStateFunction(GameStates.GAME, self.GameState)
        self.addStateFunction(GameStates.MENU, self.MenuState)

        # Init the player
        #self.player = Player(2, 1 + 0.2, window.tileLoader, window.TILE_SIZE)

        # window.drawScreen(mapHolder, player, NPCManagerIns)
        self.clock = pygame.time.Clock()
        self.deltaTime = 0

        pygame.mixer.init()
        # ~ default_font = pygame.font.get_default_font()
        self.window.drawScreen("StartMenu")

    def addStateFunction(self, state, function):
        self.stateFunctionDict.update({state: function})

    def getStateFunctionCallback(self, state):
        return self.stateFunctionDict.get(state)

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
        self.startMenu.handleInput(self.getInputs())
        self.window.updateScreen("StartMenu", self.deltaTime)
        self.window.drawScreen("StartMenu")
        return True

    def MenuState(self):
        return True

    def GameState(self):

        return True

    def getInputs(self):
        return pygame.event.get(pygame.KEYDOWN)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == UserEvents.STARTGAME:
                self.changeGameLoopStateToGAME()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pygame.event.post(event)


    def startLoop(self):
        """The main function that runs the whole game."""
        # Game loop
        while pygame.display.get_init():
            self.deltaTime = self.clock.get_time()
            print(self.deltaTime, self.clock.get_time())
            for stateOfGame in self.stateFunctionDict.keys():
                if self.gameState == stateOfGame:
                    self.getStateFunctionCallback(self.gameState)()
            self.handleEvents()
            pygame.event.pump()

            try:
                pygame.display.update()
            except:
                print("Error")

            self.clock.tick(60)
