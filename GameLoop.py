# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:14:25 2017

@author: piete
"""
import os

import pygame

import GameEndChecker
import UserEvents
from GameStates import GameStates
from InGameMenu import InGameMenu
from MainGameScreen import MainGameScreen
from MapHolder import MapHolder
from Player import Player
from StartMenu import StartUpMenu
from Vector import Vector
from WinScreen import WinScreen
from Window import Window


class Gameloop:
    """Class all the game loop functions and informations"""
    def __init__(self, gameName, screenSize, tileSize):

        self.width = screenSize.x
        self.height = screenSize.y
        self.screenSize = screenSize
        self.TILE_SIZE = tileSize
        self.gameState = GameStates.STARTMENU

        # Initialise screen
        pygame.font.init()

        self.font_renderer = pygame.font.Font(os.path.join("fonts", 'Millennium-Regular_0.ttf'), 24)
        self.window = Window(screenSize, gameName, self.TILE_SIZE, self.font_renderer)

        # pygame.mixer.init()

        # Fill background
        self.window.clearScreen()

        # Dictionary to hold all the states and their corresponding Game states
        self.stateFunctionDict = {}
        self.addStateFunction(GameStates.STARTMENU, self.StartMenuState)
        self.addStateFunction(GameStates.GAME, self.GameState)
        self.addStateFunction(GameStates.MENU, self.MenuState)
        self.addStateFunction(GameStates.WINSCREEN, self.winState)

        self.player = Player(2, 1, self.window.tileLoader, self.TILE_SIZE, Vector(0, 10))

        # Init the maps
        self.mapHolder = MapHolder(["map1", "map2", "map3"], self.TILE_SIZE, self.window.tileLoader)

        # Init the different screens and add them to the renderer
        self.startMenu = StartUpMenu(self.window.tileLoader, self.font_renderer)
        self.window.addScreenToRender(self.startMenu, "StartMenu")

        self.inGameMenu = InGameMenu(screenSize, self.window.tileLoader, self.font_renderer)
        self.window.addScreenToRender(self.inGameMenu, "inGameMenu")

        self.mainGameScreen = MainGameScreen(self.mapHolder, self.window.tileLoader, self.player, screenSize, self.font_renderer)
        self.window.addScreenToRender(self.mainGameScreen, "MainGame")

        self.winScreen = WinScreen(screenSize, self.window.tileLoader, self.font_renderer)
        self.window.addScreenToRender(self.winScreen, "WinScreen")

        self.clock = pygame.time.Clock()
        self.deltaTime = 0

    def addStateFunction(self, state, function):
        """Add a function called by each state"""
        self.stateFunctionDict.update({state: function})

    def getStateFunctionCallback(self, state):
        """Return the state functions callback"""
        return self.stateFunctionDict.get(state)

    def setMusic(self, filename):
        """Set the music playing"""
        pygame.mixer.music.fadeout(100)  # Avoid music change being too sudden!
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)

    def changeGameLoopStateToGAME(self):
        self.gameState = GameStates.GAME

    def changeGameLoopStateToMenu(self):
        self.gameState = GameStates.MENU  # Ingame menu

    def changeGameLoopStateToStartMenu(self):
        self.gameState = GameStates.STARTMENU

    def changeGameLoopStateToWin(self):
        self.player = Player(2, 1, self.window.tileLoader, self.TILE_SIZE, Vector(0, 10))
        self.mapHolder = MapHolder(["map1", "map2", "map3"], self.TILE_SIZE, self.window.tileLoader)
        self.window.updateScreenFromRender("MainGame", self.mainGameScreen)
        self.mainGameScreen = MainGameScreen(self.mapHolder, self.window.tileLoader, self.player, self.screenSize,
                                             self.font_renderer)
        self.window.addScreenToRender(self.mainGameScreen, "MainGame")
        self.gameState = GameStates.WINSCREEN

    def quitGame(self):
        pygame.quit()
        exit(0)

    """State functions for each State"""
    def StartMenuState(self):
        self.startMenu.handleInput(self.getInputs())
        self.window.updateScreen("StartMenu", self.deltaTime)
        self.window.drawScreen("StartMenu")
        return True

    def MenuState(self):
        self.inGameMenu.handleInput(self.getInputs())
        self.window.updateScreen("inGameMenu", self.deltaTime)
        self.window.drawScreen("inGameMenu")
        return True

    def GameState(self):
        self.window.clearScreen()
        self.window.getScreen("MainGame").movePlayer(self.getInputs())
        self.window.updateScreen("MainGame", self.deltaTime)
        self.window.drawScreen("MainGame")
        return True

    def winState(self):
        self.winScreen.handleInput(self.getInputs())
        self.window.clearScreen()
        self.window.updateScreen("WinScreen", self.deltaTime)
        self.window.drawScreen("WinScreen")

    def getInputs(self):
        """Return the events corresponding to each button press"""
        events = pygame.event.get([pygame.KEYDOWN, pygame.KEYUP])
        return events

    def handleEvents(self):
        """Handle the events thrown by the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == UserEvents.STARTGAME:
                self.changeGameLoopStateToGAME()
            elif event.type == UserEvents.RESUMEGAME:
                if self.gameState == GameStates.GAME:
                    self.changeGameLoopStateToMenu()
                else:
                    self.changeGameLoopStateToGAME()
            elif event.type == UserEvents.WINSTATE:
                self.changeGameLoopStateToWin()
            elif event.type == UserEvents.GOTOSTARTMENU:
                self.changeGameLoopStateToStartMenu()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pygame.event.post(event)

    def startLoop(self):
        """The main function that runs the whole game."""
        # Game loop
        while pygame.display.get_init():
            self.deltaTime = self.clock.get_time()
            # print(self.clock.get_fps())
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

