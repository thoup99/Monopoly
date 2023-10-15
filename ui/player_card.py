import pygame
from player import Player
from renderer import Renderer

class PlayerCard:
    font = pygame.font.SysFont('Arial', 30)

    def __init__(self, player: Player, player_num) -> None:
        self.x = 20
        self.y = 40 + 40 * player_num
        self.player = player
        Renderer.elements.append(self)

    def render(self, screen: pygame.surface.Surface):
        text_surface = PlayerCard.font.render(f"{self.player.name}: ${self.player.money}", False, (255,255,255))
        screen.blit(text_surface, (self.x, self.y))