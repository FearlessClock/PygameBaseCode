# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:14:25 2017

@author: piete
"""
import os

import pygame
from pygame.locals import *

from GUI import GUI
from GameStates import GameStates
from MapHolder import MapHolder
from NPCManager import NPCManager
from Player import Player
from StartMenu import StartUpMenu
# Size of the screen
from TileLoader import TileLoader
from Vector import Vector
from Window import Window
import time as Time

import timeit

width = 640
height = 640
# size of the tile
TILE_SIZE = Vector(80, 80)


def setMusic(f):
    pygame.mixer.music.fadeout(100)  # Avoid music change being too sudden!
    pygame.mixer.music.load(f)
    pygame.mixer.music.play(-1)


def changeGameLoopStateToRPG():
    setMusic("music/main.ogg")
    global gameState
    gameState = GameStates.RPG


def changeGameLoopStateToManagament():
    setMusic("music/qg.ogg")
    global gameState
    gameState = GameStates.MANAGE


def changeGameLoopStateToMenu():
    global gameState
    gameState = GameStates.MENU


def changeGameLoopStateToInteraction():
    setMusic("music/talk.ogg")
    global gameState
    gameState = GameStates.INTERACTION


def quitGame():
    pygame.quit()
    exit(0)


pygame.mixer.init()
setMusic("music/menu.ogg")
gameState = GameStates.STARTMENU
startMenu = None
managementMenu = None
interactionMenu = None


def StartMenuState(window, font_renderer, dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return
        if event.type == KEYDOWN or event.type == KEYUP:
            startMenu.handleInput(event.key, event.type)
    startMenu.update(dt)
    startMenu.drawScreen(window, font_renderer)
    return True


def MenuState():
    return True


def RPGState(window, player, mapHolder, NPCManagerIns, sect, clock, font_renderer):
    """Event loop: Checks all the events and acts accordingly"""
    currentMap = mapHolder.getCurrentMap()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return
        if event.type == KEYUP or event.type == KEYDOWN:
            # Move the player around
            player.move(event, currentMap, NPCManagerIns)
            if player.interactionFlag:
                changeGameLoopStateToInteraction()
                interactionMenu.setupInteractionMenu(NPCManagerIns.getNPCFromID(player.NPCToInteractWith))

    sect.Update()

    player.update(clock.get_time(), mapHolder, window)
    if player.hq_flag:
        player.hq_flag = False
        changeGameLoopStateToManagament()

    player.update(clock.get_time(), mapHolder, window)
    NPCManagerIns.update(clock.get_time(), currentMap)
    window.drawScreen(currentMap, player, NPCManagerIns)
    window.GUI.update(window.imageLoader, sect)
    window.GUI.drawScreen(window, font_renderer)

    return True


def ManageState(window, font_renderer, player, sect):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return
        if event.type == KEYDOWN or event.type == KEYUP:
            managementMenu.handleInput(event.key, event.type)
            if managementMenu.backToRPGFlag:
                changeGameLoopStateToRPG()
                player.pos.y = player.hqLocation.y + 0.5
                player.stopMovement()
                managementMenu.resetMenu()

    managementMenu.drawScreen(window, font_renderer)
    window.GUI.update(window.imageLoader, sect)
    window.GUI.drawScreen(window, font_renderer)
    return True


def InteractionState(window, player, font_renderer, dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return
        if event.type == KEYDOWN or event.type == KEYUP:
            interactionMenu.handleInput(event.key, event.type)

    interactionMenu.update(dt)
    interactionMenu.drawScreen(window, font_renderer)
    if interactionMenu.interactionDone:
        changeGameLoopStateToRPG()
        player.finishInteraction()


def gameLoop():
    """The main function that runs the whole game."""

    score = 0
    # Initialise screen
    pygame.font.init()
    # ~ default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(os.path.join("images", 'Millennium-Regular_0.ttf'), 24)

    window = Window(Vector(width, height), None, 'SectQuest', TILE_SIZE, font_renderer)
    tileLoader = TileLoader(TILE_SIZE, Vector(width, height))

    window.imageLoader = tileLoader
    window.GUI = GUI(tileLoader)

    pygame.mixer.init()

    mapHolder = MapHolder(TILE_SIZE, tileLoader)
    NPCManagerIns = NPCManager(TILE_SIZE, mapHolder, tileLoader)
    sect = Sect()

    global managementMenu
    global startMenu
    global interactionMenu
    managementMenu = ManagementScreen(tileLoader, sect)
    startMenu = StartUpMenu(tileLoader, changeGameLoopStateToRPG, quitGame)
    # Fill background
    window.clearScreen()

    # Initialise both users
    player = Player(2, 1 + 0.2, tileLoader, 'images/playerDown.png', TILE_SIZE)

    interactionMenu = InteractionMenu(tileLoader, player, sect, 0, None)

    # window.drawScreen(mapHolder, player, NPCManagerIns)
    clock = pygame.time.Clock()
    time = 0
    global gameState
    gameState = GameStates.STARTMENU
    # Game loop
    while pygame.display.get_init():
        start = Time.clock()
        if gameState == GameStates.RPG:
            RPGState(window, player, mapHolder, NPCManagerIns, sect, clock, font_renderer)
        elif gameState == GameStates.MANAGE:
            ManageState(window, font_renderer, player, sect)
        elif gameState == GameStates.MENU:
            MenuState()
        elif gameState == GameStates.STARTMENU:
            StartMenuState(window, font_renderer, clock.get_time())
        elif gameState == GameStates.INTERACTION:
            InteractionState(window, player, font_renderer, clock.get_time())

        try:
            pygame.display.update()
        except:
            print("Error")
        end = Time.clock()
        print(end-start)
        clock.tick(60)
