import pygame
from renderer import Renderer

class Board:
    def __init__(self, screen_x, screen_y) -> None:
        self.image = pygame.image.load("./images/monopoly.jpg")
        self.rect = self.image.get_rect()

        self.rect.centerx = screen_x / 2
        self.rect.centery = screen_y / 2

        Renderer.elements.append(self)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)