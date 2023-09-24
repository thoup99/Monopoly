import pygame
from monopoly import Monopoly
from ui.buttons import button
  
pygame.init()
  
# Create Canvas
canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Monopoly")

monopoly = Monopoly(2)
running = True
clock = pygame.time.Clock()
fps = 60
  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    monopoly.doOneTurn()

    if monopoly.game_over:
        running = False

    pygame.display.update()