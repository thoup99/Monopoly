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

def timer_test():
    print("Times Up")

dice_timer = Timer(500, timer_test)

running = True
clock = pygame.time.Clock()
fps = 30
while running:
    time = clock.tick(fps)
    Input.get_inputs()
    Timer.tickTimers(time)

    if not monopoly.game_over:
        if monopoly.state == Monopoly.MAKE_PLAYER_COUNT:
            ButtonArray("How many Players?", ["2", "3", "4"], monopoly.setPlayerNumber)
            monopoly.setState(Monopoly.PLAYER_COUNT)

        elif monopoly.state == Monopoly.MAKE_NAME_SELECTION:
            player_num = len(monopoly.player_names) + 1
            EntryBox(f"Enter Player {player_num}'s Name:", monopoly.appendPlayerName)
            monopoly.setState(Monopoly.NAME_SELCTION)

        elif monopoly.state == Monopoly.CREATE_PLAYER_CARDS:
            monopoly.createPlayers()
            for player in monopoly.players:
                PlayerCard(player)
            monopoly.setState(Monopoly.ROLLING_DICE)
            dice_timer.beginTicking()


    if monopoly.game_over:
        running = False

    renderer.renderAll()