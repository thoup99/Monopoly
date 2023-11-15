import pygame
from input import Input
from timers import Timer
pygame.init()

import sys
from monopoly import Monopoly
from renderer import Renderer
from ui.player_card import PlayerCard
from ui.board import Board
from ui.entrybox import EntryBox
from ui.button_array import ButtonArray
from ui.label import Label

def check_keys(key, unicode):
    match (key):
        case(pygame.K_ESCAPE):
            close_game()

def close_game():
    global running
    running = False
    pygame.quit()
    pygame.mixer.quit()
    sys.exit()


Input.subscribe(pygame.QUIT, close_game)
Input.subscribe(pygame.KEYDOWN, check_keys) 
  
# Create Canvas
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monopoly")


renderer = Renderer(canvas)
Board(SCREEN_WIDTH, SCREEN_HEIGHT)

monopoly = Monopoly()

#-----Mouse Position Debug-----#

l = Label("Mouse: ", 100, 270)

def setLabelText(pos):
    l.setText(f"Mouse: {pos}")

Input.subscribe(pygame.MOUSEMOTION, setLabelText)

#-----Mouse Position Debug-----#

#-----Click Recorder Debug-----#

recording = False

positions = []

def recordClick(button, pos):
    global recording

    if recording:
        positions.append(pos)
        print(f"Recorded Position {pos}")

def handleRecordInput(key, unicode):
    global recording

    if key == pygame.K_d:
        if len(positions) > 0:
            positions.pop()
            print("Removed last recorded position")
    if key == pygame.K_s:
        if len(positions) > 0:
            print("Saving Positions")
            with open("recorded_positions.txt", "w") as file:
                file.write(str(positions))
    if key == pygame.K_BACKSLASH:
        recording = not recording
        print(f"Recording Toggled. Set to {recording}.")


Input.subscribe(pygame.MOUSEBUTTONDOWN, recordClick)
Input.subscribe(pygame.KEYDOWN, handleRecordInput)

#-----Click Recorder Debug-----#

running = True
clock = pygame.time.Clock()
fps = 30
while running:
    time = clock.tick(fps)
    Input.get_inputs()
    Timer.tickTimers(time)

    if not monopoly.game_over:
        if monopoly.state == Monopoly.MAKE_PLAYER_COUNT:
            ButtonArray("How many players?", [["2", 2], ["3", 3], ["4", 4]], monopoly.setPlayerNumber)
            monopoly.setState(Monopoly.PLAYER_COUNT)

        elif monopoly.state == Monopoly.MAKE_NAME_SELECTION:
            player_num = len(monopoly.player_names) + 1
            EntryBox(f"Enter Player {player_num}'s Name:", monopoly.appendPlayerName)
            monopoly.setState(Monopoly.NAME_SELCTION)

        elif monopoly.state == Monopoly.CREATE_PLAYER_CARDS:
            monopoly.createPlayers()
            for player in monopoly.players:
                PlayerCard(player)

            monopoly.setState(monopoly.PLAYING_GAME)
            monopoly.startNextTurn()


    if monopoly.game_over:
        running = False

    renderer.renderAll()