import pygame
pygame.init()

import sys
from monopoly import Monopoly
from renderer import Renderer
from ui.player_card import PlayerCard
from ui.board import Board


def get_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            match (event.key):
                case(pygame.K_ESCAPE):
                    close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                MOUSEDOWN = True

def close_game():
    global running
    running = False
    pygame.quit()
    pygame.mixer.quit()
    sys.exit()

  
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
    get_input()

    if not monopoly.game_over:
        pass

    if monopoly.game_over:
        running = False

    renderer.renderAll()