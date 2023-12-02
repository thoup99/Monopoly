import pygame
from input import Input
from timers import Timer
pygame.init()

import sys
from monopoly import Monopoly
from renderer import Renderer
from ui.player_card import PlayerCard
from ui.image import Image
from ui.entrybox import EntryBox
from ui.button_array import ButtonArray
from ui.colored_rectangle import ColoredRectangle

from tiles.ownable_tile import OwnableTile

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

Image("./images/board.png", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
ColoredRectangle((120, 117), 220, 162, (191, 191, 191))

monopoly = Monopoly()

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


#-----Cheats Debug-----#

cheats_on = False

def handleCheatInputs(key, unicode):
    global monopoly, cheats_on

    if key == pygame.K_RIGHTBRACKET:
        cheats_on = not cheats_on
        print(f"Cheats Toggled. Set to {cheats_on}.")
    
    if cheats_on:
        if key == pygame.K_1:
            for player in monopoly.players:
                if player.number != monopoly.current_player_index:
                    player.money = 0
            print("Set money to zero for all players except current.")

        if key == pygame.K_2:
            for tile in monopoly.board:
                if isinstance(tile, OwnableTile):
                    tile.setOwner(monopoly.players[monopoly.current_player_index])
            monopoly.updateTileOwners()
            print("Gave all property to the current player.")
            
        if key == pygame.K_3:
            monopoly.players[monopoly.current_player_index].money += 1000
            print("Gave 1k to the current player.")

        if key == pygame.K_4:
            index = monopoly.current_player_index + 1
            if index == monopoly.num_players:
                index = 0

            monopoly.jailPlayer(monopoly.players[index])
            print("Jailed the Next Player.")

        if key == pygame.K_5:
            index = monopoly.current_player_index + 1
            if index == monopoly.num_players:
                index = 0

            monopoly.players[index].get_out_of_jail_free = True
            print("Gave the Next Player a 'Get Out of Jail Free' Card.")

Input.subscribe(pygame.KEYDOWN, handleCheatInputs)

#-----Cheats Debug-----#

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


    if monopoly.done:
        running = False
        close_game()

    renderer.renderAll()