import pygame
from ui.buttons import button
  
pygame.init()
  
# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))
  
# TITLE OF CANVAS
pygame.display.set_caption("Monopoly")
running = True
clock = pygame.time.Clock()
fps = 60
  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()