import pygame
from renderer import Renderer

class Label:
    def __init__(self, text, center_x, center_y, font_size = 30) -> None:

        font = pygame.font.SysFont('Arial', font_size)
        
        self.text_surface = font.render(text, True, (0,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx, self.text_rect.centery = center_x, center_y

        Renderer.addElement(self)

    def __del__(self):
        print("Deleting Label")

    def destroy(self):
        Renderer.removeElement(self)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.text_surface, self.text_rect)