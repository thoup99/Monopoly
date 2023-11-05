import pygame
from input import Input
pygame.init()

import sys
from monopoly import Monopoly
from renderer import Renderer
from ui.player_card import PlayerCard
from ui.board import Board
from ui.button import Button
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

monopoly = Monopoly(2)

#Creates a player card for each player
for x, player in enumerate(monopoly.players):
    PlayerCard(player, x)

running = True
clock = pygame.time.Clock()
fps = 30
while running:
    clock.tick(fps)
    Input.get_inputs()

    if not monopoly.game_over:
        if monopoly.state == Monopoly.MAKE_PLAYER_COUNT:
            ButtonArray("How many Players?", ["1", "2", "3", "4"], monopoly.setPlayerNumber)
            monopoly.state = Monopoly.PLAYER_COUNT

        elif monopoly.state == Monopoly.MAKE_PLAYER_COUNT:
            print(monopoly.num_players)
            monopoly.state = Monopoly.PLAYER_COUNT


    if monopoly.game_over:
        running = False

    renderer.renderAll()